# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with
code in this repository.

## Operating mode

Operating mode: after completing any milestone, immediately start the next one.
Never pause to report and wait. Status reporting happens in commit messages and
PR descriptions only. The only valid stops are the budget gates or a blocker
that cannot be resolved without Umer. This rule overrides any instinct to check
in.

## Budgets — the only valid stops

Two budgets that never mix, both gated in `src/mohenara/spend.py` before each
call:

| provider | cap | eval stop | purpose |
|---|---|---|---|
| bedrock | $100 | $90 | the build: eval runs, the matrix, **and serving the apps** (since 2026-09-04; cap raised $50→$100 the same day, funded by the AWS credits) |
| anthropic | $9 | $8 | the frontier comparison, and the fallback route to opus-5 |

`config/models.json` is the registry. A model with `rates: null` raises rather
than costing $0.00 — an unpriced model must never read as free.

Serving history, because it explains the registry: the apps first served
`opus-5` (93.3% on both input formats) through the first-party API, back when
this AWS account was not entitled to it on Bedrock. On 2026-09-04 the
entitlement arrived — `tools/bedrock_preflight.py` reports `SUCCESS` for
`us.anthropic.claude-opus-5` — and serving moved to `opus-5-bedrock`: the
same model, billed to the AWS credits, at the us.* 1.1x regional premium.
`serving_provider` in `config/models.json` names the one provider the apps
may spend on, and `config.check_default()` refuses to start an app whose
default sits anywhere else. Serving draws on the bedrock cap (raised to
$100/$90 with Umer's approval on 2026-09-04, alongside the pin in
`eval/test_budget_isolation.py` — a cap changes config and test together or
not at all); `MOHENARA_BUDGET_BEDROCK` remains the per-day override if a
demo ever needs more.

**Billing is enforced, not assumed.** The spawned CLI can authenticate through
a machine's own login (host-managed session credentials, `~/.claude.json`) and
will silently prefer it — $8.96 of "anthropic" spend was once billed that way
while the configured key sat unused. The resolver now execs through
`tools/cli_guard.py`, which allowlists the environment
(`subprocess_env_allowlist` in `config/models.json`), gives the CLI a private
HOME, and closes inherited descriptors. On any new deployment, run
`python tools/anthropic_auth_probe.py` (~3 min, ≤$0.001): a bogus key must
fail, the real key's usage must appear in the console. Full story:
`results/notes/anthropic-billing-postmortem.md`.

The anthropic ledger was reset to $0 on 2026-08-20 (phantom entries archived in
`results/abandoned/spend_anthropic_phantom.json`). One denial on opus-5 at
high effort costs about $0.40–0.55 cold and ~$0.20 warm at Bedrock rates.
Keep `stop_eval_usd` below `budget_usd` on the serving provider either way,
so a stray eval run can never eat the headroom a live demo depends on.

## Invariants

- `.env.local` holds all credentials, is gitignored, and never appears in a
  committed file, log, or PR.
- Only `eval/score.py` may open `eval/dev_labels.jsonl`. Enforced by
  `eval/test_leakage.py`.
- Deterministic layers contain no model calls: `loader`, `pricing`, `spend`,
  `score`, `config`.
- CARC/RARC meanings come from `reference/runtime/*.md`, cited by filename,
  never recalled from memory.
- Every prediction is schema-validated before it is persisted.
- Accuracy claims exist only as scorer output.

## Architecture

One denial in, one schema-valid resolution out — or an explicit
`awaiting_human` park with a specific question. Parked cases score as wrong on
purpose (the label space has no "need more information" value); the trade is
documented in `results/notes/parking-hypothesis.md`.

**Exactly one module calls a model.** `src/mohenara/resolve.py` drives the
Claude Agent SDK (which spawns the Claude Code CLI as a subprocess), enforces
structured output against the schema, retries, and hands usage to the ledger
even for failed turns — a billed-but-failed call that the budget guard cannot
see is the failure mode the module exists to prevent. Everything upstream and
downstream of it is deterministic and testable offline.

The resolve path: `loader.py` renders a case (an `.edi` artifact set or a
`case.md`) into a byte-stable prompt — filenames fix each artifact's position
so the prefix stays cacheable; `prompts.py` supplies the stable system prompt;
`resolve.py` calls the model through `tools/cli_guard.py` (see billing above)
with `_agent_env` blanking every other provider's credentials; the structured
output is schema-validated, assembled into a prediction, and priced into
`results/spend.json` before anything else happens with it.

**Two apps, two processes, one deliberate wall.** `api.py` (port 8765) is the
operator app: submit denials, watch the queue, answer parked cases. It is
deliberately incurious — no route on it can name a model, an effort, or a cost
(`jobs.client_safe`/`public` strip `usage` server-side; `eval/
test_client_surface.py` pins this). `internal_api.py` (port 8766) is where
spend, runs, and accuracy live. The separation is structural: the operator
process has no route that serves any of it, so the wall survives a `curl`.

**The demo is a second frontend on the same backend.** `/demo?v=<variant>`
serves `static/demo/<variant>/index.html` against the same API and queue.
`?live=a|b|c` picks one of three mid-run displays (headline / stage checklist /
findings-as-written); `?job=<id>` replays a finished run free. Nothing in any
of them advances on a timer — every element is driven by real stream facts.

**The queue** (`jobs.py`) runs resolves on a small pool (default 3,
`MOHENARA_RESOLVE_CONCURRENCY`) with one deliberate brake: the first call
after a cold gap runs ALONE so it writes the ~90k-token cached prefix once,
then the rest fan out against the warm cache — all-parallel would pay that
write per call. Every job is cancellable: queued jobs never start, running
ones are killed via the pidfile the guard writes (`results/queue/<job>.pid`,
SIGTERM), and the resolver's abort check stops the retry loop from respawning
the spend; a killed call's already-generated tokens are billed by the provider
but never reach the ledger (documented on `ResolveAborted`). The queue
persists one JSON file per job under `results/queue/`, and keeps two
in-memory live-stream buffers per job that must never mix: `text` (the
structured output as written) and `reasoning` (the model thinking out loud). Thinking prose can contain the literal key names the
partial-JSON readers in `annotate.py` anchor on; folding the buffers together
once made the mid-run displays parse the model's draft instead of its answer.
`api.py` serves both as server-sent events.

**The honesty boundary** (`annotate.py`, assembled in `jobs.demo_view`): the
demo highlights only segments the model quoted verbatim, matched against the
artifact bytes server-side. A quotation that does not occur is reported
unanchored, never placed somewhere plausible. A quote that occurs on several
identical lines anchors on all of them; a correction that would be ambiguous
the same way is dropped, never applied everywhere — highlighting states a fact,
rewriting invents claim content. The frontend receives finished annotations and
has nothing to analyse with.

**Park and resume** (`store.py`): a case that stops to ask writes
`results/inbox/<case>.json`; answering re-runs the resolver with the answer and
files the case to `inbox_resolved/` (or re-parks it without losing the first
answer). The operator UI, the demo dialog, and the scripted tests all go
through the same `store.answer`, so the tested path is the operator's path.

**Eval is two separate commands on purpose**: `eval/run_eval.py` writes
predictions under `results/<run-id>/`; `eval/score.py` reads them against
`eval/dev_labels.jsonl` and is the only code allowed to open that file.

## Commands

    make verify-offline     # free: scorer, schema, budget isolation
    make verify             # everything; live suites need VERIFY_LIVE=1
    python tools/bedrock_preflight.py
    python eval/run_eval.py --slice eval/slices/dev25.txt --format md \
        --model opus-4-6 --effort high --run-id <id>
    python eval/score.py --predictions results/<id>

Everything runs from the repo root with the venv from `make venv`. One test
file, or one test: `.venv/bin/python -m pytest eval/test_annotations.py -q`
(add `-k <name>` for a single test). The suites under `eval/test_*.py` are the
offline verification; anything that would spend is gated behind `VERIFY_LIVE=1`
and skips without it.

Serving: `make serve` (operator, 8765), `make serve-internal` (8766 — never
expose publicly). The demo needs no server of its own.

Playwright (config in `playwright.config.js`) has three projects — `operator`
(journeys), `demo`, `internal` — and starts the servers itself; a suite run
against an already-running server silently verifies the wrong code, so
`PW_REUSE_SERVER=1` is opt-in for local iteration only. The demo project mixes
seeded free tests with live ones that spend on the serving provider:

    npx playwright test --project=demo --grep-invert "demo live|end to end"  # free
    npx playwright test --project=demo                                       # spends

On a Playwright failure, read the screenshot in `results/playwright-artifacts/`
before changing anything.

`make record-spend` commits the live ledger as the record (deliberate, never
automatic). `make verify-headroom` answers "is there budget left to demo with"
and is kept out of CI on purpose.

## results/ storage

Committed as the scored record: `predictions/`, `run.json`, `matrix.md`,
`spend_record.json`, `spend_plan.md`. Raw responses are archived compressed once
a run is scored; transcripts stay uncompressed while a run is being diagnosed.

**The ledger is two files, not one.** `spend.json` is live state — every running
server appends to it — and is gitignored. `spend_record.json` is the committed
record and is written only by `make record-spend`. They were one tracked file
once, which meant two deployments edited it and a `git pull` had to pick a
winner; one pull silently dropped a real $0.407045 call. A fresh checkout's
`spend.json` is seeded from the record, so a second deployment still cannot
re-spend a budget the record already accounts for.

Both caps are per-**account**, so two deployments' ledgers need reconciling:

    make merge-ledger LEDGER=/path/to/other/results/spend.json

It reports the union and writes nothing unless asked. `queue/`, `inbox/` and
`inbox_resolved/` are live state too, and gitignored for the same reason —
answering a parked case rewrites them at runtime.
