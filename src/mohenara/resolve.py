"""The resolution system: one case in, one schema-valid resolution out.

Built on the Claude Agent SDK, routed to Amazon Bedrock. The split of
responsibility is deliberate:

  the model  decides root cause, next action, evidence, and whether it must
             stop and ask a human;
  the harness fills case_id, input_format, usage and cost from MEASURED facts.

The model is never asked to report its own token counts, so a hallucinated
number cannot reach results/. Every resolution is schema-validated before it
is persisted -- an invalid resolution is never written.
"""
from __future__ import annotations

import json
import os
import pathlib
import shutil
import time
from collections.abc import Callable
from dataclasses import dataclass, field

import anyio
import jsonschema
from claude_agent_sdk import ClaudeAgentOptions, ResultMessage, query

from . import config, pricing, spend
from .loader import Case
from .prompts import MODEL_OUTPUT_SCHEMA, system_prompt, user_prompt

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "schema" / "resolution.json"
_VALIDATOR = jsonschema.Draft202012Validator(json.loads(SCHEMA_PATH.read_text()))

DEFAULT_MODEL = "us.anthropic.claude-opus-4-6-v1"
DEFAULT_EFFORT = "high"


class ResolutionInvalid(ValueError):
    """The assembled resolution failed schema validation; it is not persisted."""


class ResolveAborted(RuntimeError):
    """The operator cancelled this resolve; no further attempt may spend.

    One honesty note lives here rather than in a UI string: a call killed
    MID-STREAM returns no usage, so the tokens the provider generated before
    the kill are billed by the provider but never reach the ledger. Cancelling
    trades a small unrecorded remainder for not spending the rest -- the only
    direction an operator ever wants, but the ledger understates by the
    fragment. Reconcile against the provider console, not the ledger, for any
    period containing cancels."""


@dataclass
class ResolveResult:
    resolution: dict
    raw: dict = field(repr=False)
    transcript: dict = field(repr=False)

    @property
    def status(self) -> str:
        return self.resolution["status"]

    @property
    def cost_usd(self) -> float:
        return self.resolution["usage"]["cost_usd"]


# The wrapper the CLI is exec'd through, and the private HOME it gets.
# tools/cli_guard.py rebuilds the environment from the allowlist, points HOME
# at CLI_HOME so ~/.claude.json belongs to this project and starts with no
# login in it, and closes inherited file descriptors. All three measures exist
# because each closed a credential channel that actually served calls billed
# to the wrong account -- see results/notes/anthropic-billing-postmortem.md.
CLI_GUARD = REPO_ROOT / "tools" / "cli_guard.py"
CLI_HOME = REPO_ROOT / ".cli-home"

# The SDK's pre-flight version check spawns cli_path with the PARENT process's
# environment, which does not carry the guard's MOHENARA_* variables -- so the
# guard would refuse and the check would report garbage. Skip it: the guard
# execs the same CLI the SDK would have found, so the version is the same.
os.environ.setdefault("CLAUDE_AGENT_SDK_SKIP_VERSION_CHECK", "1")


def _agent_env(model_name: str) -> dict[str, str]:
    """Environment for the CLI subprocess, per the model's provider config.

    Bedrock needs CLAUDE_CODE_USE_BEDROCK=1; the first-party Anthropic API
    needs that flag ABSENT, or the CLI routes to Bedrock and the call is
    charged to the wrong budget.

    Two layers, both deliberate:

      1. This dict blanks (never pops -- the Agent SDK merges options.env OVER
         os.environ, so a popped key silently comes back from the parent)
         every other provider's credentials and every host-managed auth
         channel named in config.
      2. The subprocess is exec'd through tools/cli_guard.py, which rebuilds
         the environment DEFAULT-DENY from config's subprocess_env_allowlist
         plus this provider's own variables, gives the CLI a private empty
         HOME, and closes inherited file descriptors. Layer 1 alone was not
         enough: with every env channel blanked, the CLI still authenticated
         from ~/.claude.json's on-disk login.

    Behavioural proof for both layers: tools/anthropic_auth_probe.py step 1,
    which runs this pipeline with a bogus key and must see an auth failure.
    """
    env = dict(os.environ)
    prov = config.provider_for(model_name)
    env.pop("CLAUDE_CODE_USE_BEDROCK", None)

    for other, spec in config.providers().items():
        if other == prov["name"]:
            continue
        for key in spec.get("credential_env", []):
            if key not in prov.get("credential_env", []):
                env[key] = ""

    for key in config.host_managed_auth_env():
        env[key] = ""

    env.update(prov.get("env", {}))
    missing = [k for k in prov.get("credential_env", []) if not env.get(k)]
    if missing:
        raise RuntimeError(
            f"provider {prov['name']!r} needs {missing} in the environment; "
            "load .env.local first"
        )

    # Everything the guard is allowed to pass through: the shared allowlist,
    # this provider's credentials, and this provider's routing flags.
    allow = (config.subprocess_env_allowlist()
             + list(prov.get("credential_env", []))
             + list(prov.get("env", {})))
    real_cli = shutil.which("claude")
    if not real_cli:
        raise RuntimeError("no `claude` CLI on PATH for the resolver to exec")
    env["MOHENARA_ENV_ALLOWLIST"] = ",".join(dict.fromkeys(allow))
    env["MOHENARA_REAL_CLI"] = real_cli
    env["MOHENARA_CLI_HOME"] = str(CLI_HOME)
    return env


async def _run_query(case: Case, *, model: str, effort: str,
                     human_answer: str | None,
                     thinking: str = "adaptive",
                     on_delta: Callable[[str, str], None] | None = None,
                     pidfile: pathlib.Path | None = None,
                     ) -> tuple[dict | None, dict, str, str | None]:
    """Drive one Agent SDK turn.

    Returns (structured_output, usage, raw_text, failure). `failure` is a
    reason string rather than an exception precisely so that a billed-but-
    failed turn still hands its usage back to be recorded.
    """
    env = _agent_env(model)
    if pidfile is not None:
        # The guard writes its PID here just before exec'ing the CLI, so a
        # cancel can SIGTERM the in-flight call. Guard-only: not on the
        # allowlist, so the variable never reaches the CLI itself.
        env["MOHENARA_PIDFILE"] = str(pidfile)
    options = ClaudeAgentOptions(
        model=model,
        system_prompt=system_prompt(),      # stable, cacheable prefix
        effort=effort,
        thinking={"type": thinking},
        output_format=MODEL_OUTPUT_SCHEMA,
        max_turns=4,  # room for a structured-output retry; no tools, so it cannot loop
        allowed_tools=[],                   # pure judgement; no tool surface
        setting_sources=[],                 # never inherit ambient config
        env=env,
        # Exec'd through the guard so the CLI sees ONLY the allowlisted
        # environment, a private HOME, and no inherited descriptors.
        cli_path=str(CLI_GUARD),
        cwd="/tmp",                         # keep the CLI out of the repo tree
        # Only when someone is watching. Partial events are off by default so
        # the eval path stays byte-for-byte the request it has always sent.
        include_partial_messages=on_delta is not None,
    )

    structured: dict | None = None
    usage: dict = {}
    raw_text = ""
    failure: str | None = None

    # Never raise inside the `async for`: that tears the generator down
    # mid-iteration and surfaces as "aclose(): asynchronous generator is
    # already running", hiding the actual cause. Capture and raise after.
    async for message in query(prompt=user_prompt(case.rendered, human_answer),
                               options=options):
        # Real deltas off the wire, not a simulated typewriter. The demo view
        # reads the rationale out of this as it is written; a progress animation
        # driven by a timer would be a lie told to whoever is watching.
        if on_delta is not None and type(message).__name__ == "StreamEvent":
            delta = (getattr(message, "event", None) or {}).get("delta") or {}
            # Three delta shapes carry content, and the consumer must know
            # which is which. With structured output the answer streams as
            # input_json_delta (`partial_json`), but a model that thinks out
            # loud streams `thinking` deltas too -- and thinking prose can
            # contain the very key names the partial-JSON readers look for.
            # One run on a heavier-thinking model fed both into a single
            # buffer and the mid-run displays read the thinking's draft
            # instead of the real fields. So the kind travels with the chunk.
            for kind in ("text", "thinking", "partial_json"):
                chunk = delta.get(kind) or ""
                if chunk:
                    try:
                        on_delta(chunk, "json" if kind == "partial_json" else kind)
                    except Exception:                         # noqa: BLE001
                        # A broken consumer must never take the resolve with
                        # it: the denial matters, the animation does not.
                        pass
        if isinstance(message, ResultMessage):
            structured = message.structured_output
            usage = message.usage or {}
            raw_text = message.result or ""
            if message.is_error:
                failure = message.api_error_status or message.subtype

    # Deliberately does NOT raise on failure. A failed turn has usually already
    # been BILLED -- the tokens were generated, the turn just did not finish --
    # and raising here threw that usage away before the ledger ever saw it.
    # Money spent that the budget guard cannot see is the one failure mode this
    # module exists to prevent, so the failure is returned and the caller
    # records the cost before deciding what to do about it.
    if failure == "error_max_turns":
        failure += (" -- the turn budget was exhausted before a final answer; "
                    "structured output can cost an extra turn when the first "
                    "attempt does not validate")
    return structured, usage, raw_text, failure


def resolve_case(case: Case, *, model: str = DEFAULT_MODEL,
                 effort: str = DEFAULT_EFFORT, run_id: str = "adhoc",
                 human_answer: str | None = None,
                 is_eval_run: bool = False,
                 thinking: str = "adaptive",
                 on_delta: Callable[[str, str], None] | None = None,
                 attempts: int = 4,
                 pidfile: pathlib.Path | None = None,
                 should_abort: Callable[[], bool] | None = None) -> ResolveResult:
    """Resolve one case. Raises BudgetExceeded before spending past the cap.

    `attempts` exists for the auth probe: a deliberately bad credential takes
    the CLI ~3 minutes of internal retries to surface as a 401, and multiplying
    that by four retries here turns a diagnostic into a 13-minute wait.
    """
    spend.check_before_call(model_name=model, is_eval_run=is_eval_run)
    model = pricing.resolve_model(model)

    # Retry transient transport failures. A 140-case run died at case 18 on a
    # single "Claude Code returned an error result: success" out of the SDK --
    # a bare Exception with a nonsense message, gone on the next attempt. One
    # flaky call must not cost a whole run, and the budget gate is re-checked
    # before each attempt so a retry cannot spend past the cap.
    def _bill(usage: dict) -> float:
        """Record whatever this attempt actually cost, before anything raises."""
        if not usage:
            return 0.0
        c = pricing.cost_from_usage(model, usage)
        spend.record(run_id=run_id, case_id=case.case_id, model=model,
                     effort=effort, usage=usage, cost=c)
        return c

    # 5s, 15s, 45s. The first version backed off 1s then 2s, which is too
    # short if the cause is throttling rather than a one-off hiccup -- and the
    # observed failures came in bursts on consecutive cases, which is what
    # throttling looks like. A retry that fires before the condition clears
    # just spends the attempt.
    backoff = (0, 5, 15, 45)
    last: str | None = None
    structured = usage = raw_text = None
    for attempt in range(1, attempts + 1):
        # Checked before EVERY attempt, including the first: a cancelled call
        # dies as an SDK exception, and without this check the retry loop
        # would faithfully respawn the very spend the operator just killed.
        if should_abort is not None and should_abort():
            raise ResolveAborted(f"{case.case_id}: cancelled by the operator; "
                                 "no further attempt will spend")
        if attempt > 1:
            spend.check_before_call(model_name=model, is_eval_run=is_eval_run)
            time.sleep(backoff[attempt - 1])
        try:
            structured, usage, raw_text, failure = anyio.run(
                lambda: _run_query(case, model=model, effort=effort,
                                   human_answer=human_answer, thinking=thinking,
                                   on_delta=on_delta, pidfile=pidfile)
            )
        except (KeyboardInterrupt, spend.BudgetExceeded):
            raise
        except Exception as exc:                       # noqa: BLE001
            # A transport-level failure: no usage came back, so there is
            # nothing to bill and nothing was recorded.
            last = f"{type(exc).__name__}: {exc}"
            print(f"    {case.case_id}: attempt {attempt}/{attempts} failed "
                  f"({last[:120]})", flush=True)
            continue

        cost = _bill(usage)          # bill FIRST, on success or failure alike
        if failure:
            last = failure
            print(f"    {case.case_id}: attempt {attempt}/{attempts} failed "
                  f"({failure[:120]}) -- ${cost:.4f} billed and recorded",
                  flush=True)
            continue
        if not structured:
            last = "model returned no structured output"
            print(f"    {case.case_id}: attempt {attempt}/{attempts} returned no "
                  f"structured output -- ${cost:.4f} billed and recorded",
                  flush=True)
            continue
        break
    else:
        if should_abort is not None and should_abort():
            # The final attempt died BECAUSE it was killed; that is a cancel,
            # not a failure.
            raise ResolveAborted(f"{case.case_id}: cancelled by the operator")
        raise ResolutionInvalid(
            f"{case.case_id}: {attempts} attempts all failed; last was {last}. "
            f"Any tokens these attempts consumed are in the ledger."
        )

    resolution = _assemble(case, structured, usage, cost, model, effort)
    errors = sorted(_VALIDATOR.iter_errors(resolution), key=lambda e: list(e.path))
    if errors:
        raise ResolutionInvalid(
            f"{case.case_id}: resolution failed schema validation and was not "
            "persisted:\n  " + "\n  ".join(e.message for e in errors[:5])
        )

    transcript = {
        "case_id": case.case_id, "run_id": run_id, "model": model, "effort": effort,
        "input_format": case.input_format, "artifacts": list(case.artifacts),
        "thinking": thinking,
        "human_answer": human_answer,
        "system_prompt_chars": len(system_prompt()),
        "user_prompt_chars": len(user_prompt(case.rendered, human_answer)),
        "usage": usage, "cost_usd": cost,
        "cache_hit_rate": pricing.cache_hit_rate(usage),
        "model_output": structured, "raw_text": raw_text,
    }
    return ResolveResult(resolution=resolution, raw={"usage": usage, "structured_output": structured,
                                                     "result": raw_text, "model": model},
                         transcript=transcript)


def _assemble(case: Case, structured: dict, usage: dict, cost: float,
              model: str, effort: str) -> dict:
    """Merge the model's judgement with the harness's measured accounting."""
    doc = {
        "schema_version": "1.0",
        "case_id": case.case_id,
        "input_format": case.input_format,
        "status": structured.get("status", "resolved"),
        "rationale": structured.get("rationale") or "(no rationale supplied)",
        "usage": {
            "input_tokens": int(usage.get("input_tokens", 0)),
            "output_tokens": int(usage.get("output_tokens", 0)),
            "cache_read_input_tokens": int(usage.get("cache_read_input_tokens", 0)),
            "cache_creation_input_tokens": int(usage.get("cache_creation_input_tokens", 0)),
            # Stored unrounded so it round-trips exactly against a
            # recomputation from the raw response. Rounding here cost 5e-9 of
            # precision and made the replay test fail for no real reason;
            # display rounding belongs in the UI, which already does it.
            "cost_usd": cost,
            "model": model,
            "effort": effort,
            "calls": 1,
        },
    }
    if doc["status"] == "awaiting_human":
        doc["awaiting_human"] = structured.get("awaiting_human") or {
            "question": "(model set awaiting_human without a question)",
            "why_needed": "unspecified", "blocks": ["root_cause.family"],
        }
        # The settled ground. This assembler once copied only the fields it
        # knew, so the model's partial findings were silently dropped between
        # the structured output and the persisted prediction -- the schema
        # allowed them, the prompt asked for them, and a live run proved they
        # never arrived. Every field the model is ASKED to produce must be
        # carried by hand here, and this one now is.
        if structured.get("partial"):
            doc["partial"] = structured["partial"]
    else:
        doc["resolution"] = structured.get("resolution") or {}
    return doc


def persist(result: ResolveResult, run_dir: pathlib.Path) -> None:
    """Write prediction, raw response, and transcript for one case."""
    case_id = result.resolution["case_id"]
    for sub, payload in (("predictions", result.resolution),
                         ("raw", result.raw),
                         ("transcripts", result.transcript)):
        target = run_dir / sub
        target.mkdir(parents=True, exist_ok=True)
        (target / f"{case_id}.json").write_text(json.dumps(payload, indent=2) + "\n")
