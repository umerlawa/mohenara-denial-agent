"""The budget ledger. Deterministic: no model calls.

Two budgets that never mix. Bedrock carries $50 for the build; the Anthropic
API carries $9 for the frontier-comparison phase only. Each has its own hard
refuse ceiling and its own soft stop for eval runs, both read from
config/models.json and both enforced HERE rather than by convention.

`check_before_call` is the gate and it runs BEFORE spending, because a ledger
that only notices an overrun afterwards has not enforced anything. Spending is
attributed to the provider that served the call, so exhausting one budget can
never consume the other.
"""
from __future__ import annotations

import contextlib
import fcntl
import json
import os
import pathlib
import threading

from .config import all_models as _all_models
from .config import provider as provider_cfg
from .config import provider_for

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]

# The ledger location is overridable so that a checkout run OUTSIDE the working
# tree -- the clean-checkout verification, for one -- still accounts to the one
# real budget. Without this, a second checkout starts from a $0 ledger and
# spends real money that the enforced budget never sees, which is exactly the
# hole the gate exists to close.
SPEND_PATH = pathlib.Path(
    os.environ.get("MOHENARA_SPEND_PATH") or REPO_ROOT / "results" / "spend.json"
).resolve()

_LOCK = threading.Lock()


@contextlib.contextmanager
def _file_lock(path: pathlib.Path):
    """Cross-process exclusive lock around the read-modify-write.

    The eval runner, the web server and the test suites are separate
    processes writing one ledger. A thread lock does not span them, and two
    concurrent read-modify-writes silently drop one call's cost -- which
    understates spend, the one direction a budget guard must never fail in.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    fd = os.open(str(path) + ".lock", os.O_CREAT | os.O_RDWR, 0o600)
    try:
        fcntl.flock(fd, fcntl.LOCK_EX)
        yield
    finally:
        fcntl.flock(fd, fcntl.LOCK_UN)
        os.close(fd)


class BudgetExceeded(RuntimeError):
    """Raised instead of spending past a provider's cap."""


def _empty() -> dict:
    return {"providers": {}, "total_usd": 0.0, "calls": 0, "by_run": {}, "entries": []}


# The committed snapshot of what the build spent. Tracked in git; NEVER written
# at runtime.
#
# results/spend.json used to be the tracked file, and it is also the file every
# running server appends to. Two deployments of this repo therefore edited the
# same tracked file, and `git pull` had to pick a winner: one pull silently
# dropped a real $0.407045 call that a demo had already spent. A budget guard
# whose ledger loses entries to a merge is not a guard.
#
# So the two roles are separated. This file is the record and only changes when
# someone deliberately runs `make record-spend`. The live ledger beside it is
# gitignored, per-deployment, and seeded from this record the first time it is
# needed -- which keeps the property the tracked ledger existed for: a fresh
# checkout does not start from $0 and spend money the cap has already accounted
# for.
SPEND_RECORD = REPO_ROOT / "results" / "spend_record.json"

# THE one ledger this process treats as its deployment's, fixed at import.
#
# Deliberately not `SPEND_PATH` itself, which tests reassign: four suites hand
# in a temp path precisely because they want an empty ledger, and seeding those
# from the record started them at the build's $53. Capturing the path at import
# means a real deployment -- including one pointed elsewhere by
# MOHENARA_SPEND_PATH, which is read at import too -- seeds, and a test that
# reassigns SPEND_PATH afterwards does not.
DEPLOYMENT_LEDGER = SPEND_PATH


def load(path: pathlib.Path = SPEND_PATH) -> dict:
    if not path.exists():
        if path == DEPLOYMENT_LEDGER and SPEND_RECORD.is_file():
            record = json.loads(SPEND_RECORD.read_text())
            record.setdefault("providers", {})
            return record
        return _empty()
    try:
        ledger = json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        # A corrupt ledger must never read as "$0 spent" -- that silently
        # reopens a budget that may already be exhausted.
        raise RuntimeError(
            f"{path} is unreadable ({exc}). Refusing to treat a corrupt ledger "
            "as zero spend; repair or move it deliberately."
        ) from exc
    ledger.setdefault("providers", {})
    return ledger


def entry_count(path: pathlib.Path = SPEND_PATH) -> int:
    """How many entries the ledger holds. Snapshot this at the start of a run."""
    return len(load(path).get("entries", []))


def cost_of(*, run_id: str, case_id: str, since: int = 0,
            path: pathlib.Path = SPEND_PATH) -> float:
    """Total recorded for one case in one run, across every attempt it took.

    A case that failed after three billed attempts has three entries. Summing
    them is how a run's reported cost can include the cases that produced no
    prediction -- otherwise every published per-run cost understates what was
    actually spent.

    `since` is an entry-count snapshot taken when the run started. A run id can
    be reused -- an abandoned run and its replacement legitimately share one --
    and without the snapshot this would attribute the abandoned run's spend to
    the new one.
    """
    return round(sum(
        e["cost_usd"] for e in load(path).get("entries", [])[since:]
        if e.get("run_id") == run_id and e.get("case_id") == case_id
    ), 6)


def provider_total(name: str, path: pathlib.Path = SPEND_PATH) -> float:
    return float(load(path).get("providers", {}).get(name, {}).get("usd", 0.0))


def total(path: pathlib.Path = SPEND_PATH) -> float:
    """Grand total across providers. Informational only -- never a gate."""
    return float(load(path).get("total_usd", 0.0))


def check_provider(name: str, *, is_eval_run: bool = False,
                   path: pathlib.Path = SPEND_PATH) -> float:
    """Gate on a provider without naming a model.

    For callers that hit a provider with an id the registry does not carry --
    the capability preflight walks a ladder of models precisely to discover
    which ones exist. They still spend real money, so they still gate.
    """
    prov = provider_cfg(name)
    spent = provider_total(name, path)
    if spent >= prov["budget_usd"]:
        raise BudgetExceeded(
            f"[{name}] ${spent:.2f} spent of ${prov['budget_usd']:.2f}. "
            "Refusing to spend further on this provider."
        )
    if is_eval_run and spent >= prov["stop_eval_usd"]:
        raise BudgetExceeded(
            f"[{name}] ${spent:.2f} spent, at or past the "
            f"${prov['stop_eval_usd']:.2f} eval stop."
        )
    return spent


def upper_bound_rates(provider_name: str) -> dict:
    """The most expensive registered rates on a provider.

    Used to price a call whose model is not in the registry. Over-counting is
    the only safe direction for a budget guard: an unpriced call recorded at
    $0.00 silently reopens a budget that may already be exhausted.
    """
    priced = [m["rates"] for m in _all_models().values()
              if m.get("provider") == provider_name and m.get("rates")]
    if not priced:
        raise KeyError(f"no priced model on provider {provider_name!r} to bound against")
    return {field: max(r.get(field, 0.0) for r in priced)
            for field in ("input", "output", "cache_write_5m", "cache_read")}


def check_before_call(*, model_name: str, is_eval_run: bool = False,
                      path: pathlib.Path = SPEND_PATH) -> float:
    """Raise BudgetExceeded if this call must not happen on its provider."""
    prov = provider_for(model_name)
    spent = provider_total(prov["name"], path)
    refuse, stop = prov["budget_usd"], prov["stop_eval_usd"]

    if spent >= refuse:
        raise BudgetExceeded(
            f"[{prov['name']}] ${spent:.2f} spent of ${refuse:.2f}. "
            "Refusing to spend further on this provider."
        )
    if is_eval_run and spent >= stop:
        raise BudgetExceeded(
            f"[{prov['name']}] ${spent:.2f} spent, at or past the ${stop:.2f} "
            "eval stop. Eval runs halted; report rather than continue."
        )
    return spent


def record(*, run_id: str, case_id: str, model: str, effort: str,
           usage: dict, cost: float, path: pathlib.Path = SPEND_PATH) -> dict:
    """Append one call, attributed to its provider. Returns provider totals."""
    prov = provider_for(model)["name"]
    with _LOCK, _file_lock(path):
        ledger = load(path)
        p = ledger["providers"].setdefault(prov, {"usd": 0.0, "calls": 0})
        p["usd"] = round(p["usd"] + cost, 6)
        p["calls"] += 1
        ledger["total_usd"] = round(sum(v["usd"] for v in ledger["providers"].values()), 6)
        ledger["calls"] = sum(v["calls"] for v in ledger["providers"].values())
        # by_run is a secondary index. `provider` on it was set once, when the
        # bucket was created, and then never revisited -- so a run served by two
        # providers reported whichever billed first, for all of its calls. The
        # `queue` run did exactly that: it ran on the Anthropic API before the
        # serving default moved to Bedrock, and every later Bedrock call was
        # then labelled anthropic. Reading provider totals off this index
        # understated one budget and overstated the other by the same amount.
        #
        # `ledger["providers"]` above was always right and is what the gate
        # reads, so no call was ever mis-gated. This keeps the index from
        # misleading anything that reads it: the per-provider breakdown is
        # authoritative within the run, and `provider` degrades to "mixed"
        # rather than naming one of two.
        run = ledger.setdefault("by_run", {}).setdefault(
            run_id, {"usd": 0.0, "calls": 0, "provider": prov, "providers": {}})
        run["usd"] = round(run["usd"] + cost, 6)
        run["calls"] += 1
        rp = run.setdefault("providers", {}).setdefault(prov, {"usd": 0.0, "calls": 0})
        rp["usd"] = round(rp["usd"] + cost, 6)
        rp["calls"] += 1
        run["provider"] = prov if len(run["providers"]) == 1 else "mixed"
        ledger["entries"].append({
            "run_id": run_id, "case_id": case_id, "provider": prov,
            "model": model, "effort": effort, "cost_usd": round(cost, 6),
            "input_tokens": usage.get("input_tokens", 0),
            "output_tokens": usage.get("output_tokens", 0),
            "cache_read_input_tokens": usage.get("cache_read_input_tokens", 0),
            "cache_creation_input_tokens": usage.get("cache_creation_input_tokens", 0),
        })
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(ledger, indent=2) + "\n")
        tmp.replace(path)   # atomic: a crash mid-write must not truncate the ledger
        return dict(ledger["providers"])


def summary(path: pathlib.Path = SPEND_PATH) -> str:
    ledger = load(path)
    lines = []
    for name, p in sorted(ledger.get("providers", {}).items()):
        cfg = provider_cfg(name)
        lines.append(f"{name}: ${p['usd']:.2f} of ${cfg['budget_usd']:.2f} "
                     f"({p['calls']} calls, stop at ${cfg['stop_eval_usd']:.2f})")
    return " | ".join(lines) or "no spend recorded"
