# Architecture — as built

This document describes the system as it exists in this repository at the
commit that contains it. Every statement is derived from the cited file; where
this document and the code disagree, the code wins. It describes what exists,
not what is planned.

---

## 1. Components

All backend code is Python 3.11 (`.venv` built by `make venv`, `Makefile`).
All frontends are single-file vanilla-JS/HTML pages with no framework and no
build step (`src/mohenara/static/*.html` — zero imports, no bundler). Tests
are pytest (offline) and Playwright/Node 22 (browser).

| Component | Language / framework | Entry point | Role |
|---|---|---|---|
| Resolution pipeline | Python; Claude Agent SDK (`claude_agent_sdk.query`) | `src/mohenara/resolve.py` (`resolve_case`) | One case in, one schema-valid resolution out. The only module that calls a model. |
| CLI guard | Python (stdlib only) | `tools/cli_guard.py` | Exec wrapper the SDK's CLI subprocess is launched through: default-deny environment, private HOME, closed descriptors. |
| Operator app | Python, FastAPI + uvicorn | `src/mohenara/api.py` (`uvicorn mohenara.api:app --port 8765`, `make serve`) | Submit denials, watch the queue, answer parked cases. Serves the operator frontend and both demo variants. |
| Internal app | Python, FastAPI + uvicorn | `src/mohenara/internal_api.py` (port 8766, `make serve-internal`) | Spend, runs, accuracy, failure taxonomy. Reads `results/`; computes no model output. |
| Job queue | Python (in-process) | `src/mohenara/jobs.py` | Serialised resolve worker, job persistence, live stream buffers. |
| Park/resume store | Python | `src/mohenara/store.py` | The awaiting-human flow: park, list, answer, resume. |
| Case loader | Python | `src/mohenara/loader.py` | Renders a case (corpus dir, upload, or pasted text) into one byte-stable prompt string. |
| Case-header parser | Python | `src/mohenara/caseinfo.py` | Deterministic 835 header facts (amounts, patient, payer) for the practice demo, pre-resolution. |
| Annotator | Python | `src/mohenara/annotate.py` | Anchors model-quoted segments against artifact bytes; partial-JSON stream readers. |
| Budget ledger | Python | `src/mohenara/spend.py` | Pre-call gates and post-call recording, per provider. |
| Pricing | Python | `src/mohenara/pricing.py` | Cost from measured usage against `config/models.json` rates. |
| Config registry | Python | `src/mohenara/config.py` reading `config/models.json` | Models, providers, budgets, serving default, env allowlists. |
| Secrets loader | Python | `src/mohenara/env.py` | Parses `.env.local` into `os.environ` (overriding), from `src/mohenara/__init__.py`. |
| Eval runner | Python CLI | `eval/run_eval.py` (argparse: `--slice --format --model --effort --run-id`) | Runs a slice, persists predictions/raw/transcripts per case, writes `run.json`. |
| Matrix runner | Python CLI | `eval/run_matrix.py` (`make matrix`) | The 12-cell model×format×effort matrix. |
| Scorer | Python CLI | `eval/score.py` | Scores predictions against `eval/dev_labels.jsonl`; the only code permitted to open that file. |
| Report generators | Python CLIs | `eval/make_matrix_report.py`, `eval/make_frontier_report.py`, `eval/make_failure_analysis.py` | Render `results/*.md` from scored runs. |
| Raw archiver | Python CLI | `eval/archive_raw.py` (`make archive-raw`) | Compresses a scored run's `raw/` into `raw.tar.gz` and deletes the originals. |
| EDI→MD converter | Python CLI, deterministic, no LLM | `tools/edi2md/convert.py` | Reads `corpus/v2-chain-corpus-v1.1/`, writes `corpus/v2-chain-corpus-v1.1-md/<CASE>/case.md`. Decode tables in `tools/edi2md/codes.py`, X12 parsing in `tools/edi2md/x12.py`. |
| Operator frontend | Vanilla JS in one HTML file | `src/mohenara/static/index.html`, served at `/` by `api.py` | Paste/upload cases, queue view, inbox answering. |
| Demo frontend v1 | Vanilla JS | `src/mohenara/static/demo/v1/index.html`, served at `/demo?v=v1` | Artifact-level demo: anchored annotations, corrected claim, three mid-run displays (`?live=a\|b\|c`), replay (`?job=`). |
| Demo frontend "practice" | Vanilla JS | `src/mohenara/static/demo/practice/index.html`, `/demo?v=practice` | Practice-owner view: staged multi-case intake, money buckets, breakdowns. |
| Internal frontend | Vanilla JS | `src/mohenara/static/internal.html`, served at `/` by `internal_api.py` | Data app UI. |
| Preflight / probes | Python CLIs | `tools/bedrock_preflight.py`, `tools/anthropic_auth_probe.py` | Bedrock entitlement report; behavioural billing proof. |
| Ledger merge | Python CLI | `tools/merge_ledger.py` (`make merge-ledger`) | Reconciles two deployments' ledgers. |
| Browser tests | Node 22, `@playwright/test` | `playwright.config.js`; specs in `tests/*.spec.js` (projects `operator`, `demo`, `internal`) | Journeys, demo suites (free + live), internal app. Starts its own servers (`webServer` blocks). |

## 2. Data storage

Everything is plain files — JSON, JSONL, Markdown, raw X12 text — under the
repository tree. There is no database of any kind (no SQLite, no server):
`grep -r sqlite src/ eval/ tools/` returns nothing.

| Data | Location | Format | Git-tracked | On restart |
|---|---|---|---|---|
| Case corpus (synthetic) | `corpus/v2-chain-corpus-v1.1/edi/<CASE>/` (six artifacts per case, `src/mohenara/loader.py:18-25`); md renderings in `corpus/v2-chain-corpus-v1.1-md/<CASE>/case.md` (`loader.py:14`); `dev_index.jsonl`, `MANIFEST.md` | raw X12 / text / md | yes | persists |
| Eval labels | `eval/dev_labels.jsonl` (only `eval/score.py` opens it; enforced by `eval/test_leakage.py`) | JSONL | yes | persists |
| Predictions | `results/<run-id>/predictions/<CASE>.json` (`resolve.persist`, `src/mohenara/resolve.py:360-368`) | JSON (schema `schema/resolution.json`) | yes (the scored record) | persists |
| Raw API responses | `results/<run-id>/raw/<CASE>.json` — usage, structured output, and the model's final text (`resolve.py:313-314`); compressed to `raw.tar.gz` after scoring (`eval/archive_raw.py`) | JSON / tar.gz | yes (379 files currently tracked) | persists |
| Transcripts | `results/<run-id>/transcripts/<CASE>.json` — run metadata, usage, `model_output`, `raw_text`; prompt sizes only, not the rendered case (`resolve.py:302-312`) | JSON | yes (483 files currently tracked) | persists |
| Run state | `results/<run-id>/run.json` (`eval/run_eval.py:152`), `score.json` (scorer output) | JSON | yes | persists |
| Live spend ledger | `results/spend.json` (+ `results/spend.json.lock`), path overridable via `MOHENARA_SPEND_PATH` (`src/mohenara/spend.py:33-35`) | JSON: providers, by_run, per-call entries (tokens + cost; no case content) | **no** (gitignored) | persists; a missing file is re-seeded from `results/spend_record.json` (`spend.py:95-101`) |
| Committed spend record | `results/spend_record.json`, written only by `make record-spend` (`Makefile:29-33`) | JSON | yes | persists |
| Job queue | `results/queue/<12-hex>.json` — one file per submitted denial, including `_source` with the **full uploaded case text** (`src/mohenara/jobs.py`); plus a transient `<job>.pid` while its CLI call runs (written by `tools/cli_guard.py`, removed when the job finishes) | JSON / pid text | **no** (gitignored, `.gitignore`) | persists; a resolve in flight when the *server process* dies stays in state `resolving` forever (nothing re-queues it on boot). Operator cancellation is different and handled: see §6 |
| Awaiting-human inbox | `results/inbox/<CASE>.json` — includes the **full rendered case** plus the model's partial resolution (`src/mohenara/store.py:58-79`); answered cases filed to `results/inbox_resolved/<CASE>.json` with the question and the human's answer (`store.py:153-158`) | JSON | **no** (gitignored) | persists |
| Live stream buffers | `jobs._STREAMS` — per-job in-memory dicts, two buffers (`text` = structured output, `reasoning` = thinking), bounded 200 KB each (`jobs.py:45-76`) | process memory | n/a | **lost** on restart; the finished rationale survives on the job record |
| CLI subprocess state | `.cli-home/` — the private HOME `tools/cli_guard.py` gives the CLI. Contains `.claude.json` (CLI settings, no login) and `.claude/projects/-tmp/*.jsonl`: the CLI's **own session transcripts, one per resolve, containing the full prompt (case text) and response**. 26 of 26 current files contain case ids. Also `.claude/sessions/*.key`, `backups/` | JSON / JSONL | **no** (gitignored) | persists; nothing in this repo prunes it |
| Playwright artifacts | `results/playwright-artifacts/` (screenshots on failure, traces; the artifacts render case content), `results/playwright-report/` | PNG/zip/HTML | no (gitignored) | persists until the next test run clears it |
| Notes / postmortems | `results/notes/*.md`, `results/*.md` reports | Markdown | yes | persists |

## 3. Data flow: one case, upload to resolution

Using the operator/demo upload path (the eval path differs only at the ends —
`eval/run_eval.py` reads the corpus and calls the same `resolve_case`).

1. **Browser → server.** The page reads the dropped files with `FileReader`
   and POSTs their full contents as JSON to `POST /api/batch`
   (`static/demo/v1/index.html` `submitDenial`; practice variant first POSTs
   the same contents to `POST /api/demo/parse` for deterministic header
   facts, `src/mohenara/api.py`). Transport is plain HTTP on localhost —
   uvicorn is started without TLS everywhere (`Makefile:116-122`,
   `playwright.config.js` webServer).
2. **Queue write #1.** `jobs.submit` writes
   `results/queue/<job>.json` including `_source.files` — the verbatim case
   text (`jobs.py:118-139`) — then enqueues `_run` on the one-worker pool.
3. **Render.** `_build_case` → `loader.load_from_files` → `render_edi`
   produces the rendered prompt string in memory (`loader.py:62-92`). The
   deterministic header parse (`caseinfo.parse`) also runs over the same
   bytes for the practice view.
4. **Model call.** `resolve.resolve_case`: budget gate
   (`spend.check_before_call`), then `_run_query` drives the Agent SDK, which
   spawns the Claude Code CLI **as a subprocess** via `tools/cli_guard.py`
   with `cwd=/tmp` and the allowlisted environment (`resolve.py:145-162`).
   The prompt — system prompt (role + the distilled reference cards from
   `reference/runtime/*.md` + procedure, `src/mohenara/prompts.py`) plus the
   rendered case and any human answer — passes to the CLI over the SDK's
   stdin/stdout pipe. The CLI writes its own session transcript of that
   exchange under `.cli-home/.claude/projects/-tmp/` (observed; see §2) and
   sends the prompt over HTTPS to the provider (§4).
5. **Streaming.** With a watcher attached, partial deltas flow back through
   `on_delta(chunk, kind)` into the two in-memory buffers (`jobs.py:62-76`),
   and out to the browser as server-sent events on
   `GET /api/demo/stream/<job>` — state, elapsed, partial rationale, a
   4,000-char thinking tail, and completed evidence items (`api.py` events).
6. **Billing.** Usage from the result message is priced and appended to
   `results/spend.json` before anything else happens — including on failed
   attempts (`resolve.py:237-244`, `spend.record`).
7. **Assembly + validation.** `_assemble` merges model judgement with
   measured usage; `jsonschema` validates against `schema/resolution.json`;
   an invalid resolution raises and is never persisted (`resolve.py:294-300`).
8. **Queue write #2.** The job file is rewritten with the resolution
   (`jobs._run` → `_set`). A parked case additionally writes
   `results/inbox/<CASE>.json` with the full rendered case (`store.park`).
9. **Serve.** `GET /api/demo/view/<job>` re-renders the artifacts from the
   stored `_source`, anchors the model's quoted segments against them
   server-side (`jobs.demo_view`, `annotate.annotations`), and returns
   artifacts + annotations + resolution fields to the browser. `usage`
   (model, effort, cost) is stripped from everything the operator process
   serves (`jobs.client_safe`/`public`; pinned by
   `eval/test_client_surface.py`).
10. **Answering a parked case.** `POST /api/queue/<job>/answer` →
    `store.answer`: the answer (and any attached documents, inlined verbatim
    into the prompt, `store.py:120-129`) is appended after the cached prefix
    and the resolver runs again — repeating steps 4–9 — then the case files
    to `results/inbox_resolved/`.

On the eval path, step 2/8/9 are replaced by `persist()` writing
`predictions/`, `raw/`, and `transcripts/` under `results/<run-id>/`
(`resolve.py:360-368`), and `run.json` summarising the run.

## 4. External network calls

Everything that leaves the machine, and what is in it:

| Caller | Destination | What leaves |
|---|---|---|
| Claude Code CLI subprocess (spawned by the Agent SDK from `resolve._run_query`) — the only model path | **Amazon Bedrock** runtime (AWS endpoint for the region in `AWS_REGION`) when the model's provider is `bedrock` (`CLAUDE_CODE_USE_BEDROCK=1`, `config/models.json` providers.bedrock.env); **`api.anthropic.com`** when the provider is `anthropic` | The full prompt: system prompt (role, distilled reference cards, procedure), the **entire rendered case** (all six artifacts verbatim — patient names, DOB-adjacent dates, payer ids, chart note), any **human answer and attached documents** verbatim, plus the credentials for that provider. Responses (thinking + structured output) come back over the same connection. |
| `tools/anthropic_auth_probe.py` | `api.anthropic.com` (`API` constant, line 48) | Step 1 runs the real pipeline (a full corpus case) with a bogus key; step 2 `GET /v1/models` (key only); step 3 a minimal 4-token `POST /v1/messages`. |
| `tools/bedrock_preflight.py` | AWS Bedrock control/runtime APIs via `boto3` | Model-id invocation probes; no case data. |
| Playwright live tests (`tests/*.spec.js` titled "demo live"/"end to end") | Same model endpoints, indirectly, by driving real resolves through the local server | Same as the model path. |

Not present: no telemetry, analytics, or error-reporting calls in this
repo's code (`grep -rn "sentry\|statsig\|analytics" src/ eval/ tools/`
returns nothing). The CLI binary itself is third-party; the guard's
allowlist (`config/models.json` `subprocess_env_allowlist`) passes proxy and
CA variables through to it, and this repo does not configure or disable any
network behaviour internal to that binary beyond the environment it grants.
`git push`/`pip`/`npm` move code and tracked results (including
`results/*/predictions|raw|transcripts`) to GitHub and package registries at
development time.

## 5. Secrets

- **Loading.** `src/mohenara/env.py` parses `.env.local` (KEY=VALUE, path
  overridable via `MOHENARA_ENV_FILE`) and writes the values into
  `os.environ`, **overriding** ambient values (`env.load`, called from
  `src/mohenara/__init__.py` so every entry point agrees). Keys present:
  `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`,
  `ANTHROPIC_API_KEY` (matching `config/models.json` `credential_env`).
  `.env.local` is gitignored (`.gitignore`).
- **Propagation.** The resolver's subprocess receives only the selected
  provider's credentials: `_agent_env` blanks the other provider's keys and
  every `host_managed_auth_env` channel; `tools/cli_guard.py` then rebuilds
  the environment default-deny from `subprocess_env_allowlist` + the
  provider's own variables, sets `HOME=.cli-home/`, and closes inherited
  descriptors (`clean_env`, `main`).
- **Leak surfaces, as they exist.**
  - Nothing in the repo prints a credential value: `env.describe()` and the
    probe emit SHA-256 **fingerprints** only (`env.py:74-86`,
    `tools/anthropic_auth_probe.py`).
  - Error strings can name credential **variables** (not values): the
    missing-credential error lists key names (`resolve.py:113-118`) and can
    reach a queue job's `error` field on disk; the operator API replaces it
    with a fixed sentence before serving (`jobs.OPERATOR_FAILURE`,
    `jobs.public`).
  - `results/spend.json`, predictions, transcripts, and raw responses carry
    tokens/costs/model ids — no credentials.
  - The CLI's own files under `.cli-home/` are written by a third-party
    binary; the guard starts it with no login on disk, and the observed
    `.cli-home/.claude.json` holds feature flags, not keys.
  - uvicorn access logs (stdout) record URLs; `POST /api/inbox/<case_id>/answer`
    and queue-job URLs put case/job identifiers — not credentials — into
    those logs.

## 6. Concurrency

- **Resolves run on a small pool with a cache-aware brake.** A
  `ThreadPoolExecutor` of `MOHENARA_RESOLVE_CONCURRENCY` workers (default 3)
  runs queue jobs (`jobs._POOL`), but the first call after a cold gap (>240 s
  since the last completion, `jobs._CACHE_FRESH_S`) takes a lock and runs
  alone — one write of the ~90k-token cached prompt prefix — before the rest
  fan out against the warm cache (`jobs._with_cache_warmup`). Provider
  throttling on parallel calls is absorbed by the resolver's 5/15/45 s retry
  backoff (`resolve.py`).
- **Cancellation.** `POST /api/queue/{id}/cancel` and `/api/queue/cancel-all`
  (`api.py`) mark a job `cancelling`; `tools/cli_guard.py` publishes the CLI
  subprocess PID to `results/queue/<job>.pid` before exec, `jobs.cancel`
  SIGTERMs it, and `resolve_case`'s `should_abort` check stops the retry loop
  from respawning the call (`ResolveAborted` → job state `cancelled`). A call
  killed mid-stream returns no usage, so its already-generated tokens are
  billed by the provider but never reach the ledger — stated on the
  `ResolveAborted` docstring; reconcile such periods against the provider
  console.
- **Shared state between threads** (request handlers vs the worker): job
  files are guarded by `jobs._LOCK` around read-modify-write (`jobs._set`);
  stream buffers by `jobs._STREAM_LOCK`. Job persistence is
  write-temp-then-`os.replace` atomic (`jobs._write`).
- **Shared state between processes** (eval runner, operator app, internal
  app, tests — all separate processes appending one ledger): `spend.record`
  takes a threading lock **and** an `fcntl.flock` exclusive file lock on
  `results/spend.json.lock` around the read-modify-write, with an atomic
  temp-file replace (`spend.py:40-56`, `247-251`).
- **Between deployments** (two machines, one account): nothing is shared at
  runtime. Each deployment's live ledger seeds from the committed record
  (`spend.py:95-101`); reconciliation is manual via
  `make merge-ledger LEDGER=...` (`tools/merge_ledger.py`).
- **Eval runs** are sequential over the slice (`eval/run_eval.py` main loop);
  `--resume` skips cases whose prediction file already exists.
- The in-memory stream buffers are per-process: a demo page polling a
  different server process than the one running the resolve would see states
  but no live text (`jobs._STREAMS`).

## 7. Dependencies

Python (`requirements.txt`, floors; installed versions from `pip freeze` in
the current venv, Python 3.11.15):

| Package | Required | Installed |
|---|---|---|
| anthropic[bedrock] | >=0.121.0 | 0.121.0 |
| boto3 | >=1.43.0 | 1.43.69 (botocore 1.43.69) |
| jsonschema | >=4.23.0 | 4.26.0 |
| pytest | >=8.0.0 | 9.1.1 |
| claude-agent-sdk | >=0.2.136 | 0.2.136 |
| fastapi | >=0.115.0 | 0.141.1 |
| uvicorn[standard] | >=0.32.0 | 0.52.1 |
| python-multipart | >=0.0.9 | 0.0.32 |
| anyio | >=4.0.0 | 4.14.2 |
| pydantic | >=2.0.0 | 2.13.4 |

Node (`package.json`): `@playwright/test ^1.49.0` (dev-only), Node 22.22.2,
Chromium from the image at `/opt/pw-browsers` (`playwright.config.js`).
Runtime-external: the Claude Code CLI binary found on `PATH`
(`resolve.py:125-127`), version whatever is installed on the machine.

---

## 8. PHI-touchpoint inventory

Every location where real patient data would sit or travel if this system
processed production denials instead of the synthetic corpus. "Encrypted at
rest": whether **this repo** provides encryption (whole-disk encryption of a
host is outside the repo and not assumed). "Access-controlled": beyond
ordinary filesystem permissions. "Deletable": whether the repo provides a
deletion path.

| # | Touchpoint | At rest encrypted | Access-controlled | Deletable | Notes |
|---|---|---|---|---|---|
| 1 | `corpus/…` case artifacts (in production: the ingested denial documents) | no — plaintext files | filesystem only | `rm` only; no tooling | Also tracked in git → full history on every clone and on GitHub. |
| 2 | `results/queue/<job>.json` — full case text in `_source`, plus resolution | no | filesystem only | `POST /api/queue/clear` deletes **finished** jobs (`jobs.clear_finished`); parked/running jobs have no deletion path | Survives restarts. |
| 3 | `results/inbox/` and `results/inbox_resolved/` — full rendered case, model partials, the human's answer and any attached documents | no | filesystem only | no deletion path in code | Gitignored (not committed), but persistent. |
| 4 | `results/<run>/predictions/`, `raw/`, `transcripts/`, `raw.tar.gz` — model output quotes case segments verbatim (evidence `segments[].text`); `raw_text`/`model_output` carry the full response | no (tar.gz is compression, not encryption) | filesystem only | `rm` only | **Git-tracked and pushed** (483 transcript + 379 raw files currently). In production this is PHI in version control on GitHub. |
| 5 | `.cli-home/.claude/projects/-tmp/*.jsonl` — the CLI's own per-resolve session transcripts containing the **full prompt (entire case) and response** | no | filesystem only | no pruning in this repo | Written by the third-party CLI on every resolve; accumulates indefinitely (currently 26 files / 1.3 MB). Easy to miss in any data-handling review. |
| 6 | In-memory stream buffers (`jobs._STREAMS`) and the SSE stream to the browser | n/a (memory) / **HTTP without TLS** in transit | none — any process that can reach the port | gone on restart | All serving is `http://127.0.0.1`; any non-localhost exposure transmits case text and model reasoning in cleartext. |
| 7 | Browser: demo/operator pages hold artifacts, names, amounts in DOM/JS memory | n/a | whoever can open the page — **no authentication on any route** (`api.py` has no auth middleware) | tab close | No `localStorage`/`sessionStorage` use (grep: 0 hits in all three pages). |
| 8 | Model provider calls: the full case + human answers to **Amazon Bedrock** or **`api.anthropic.com`** (§4) | TLS in transit; provider-side retention governed by the provider, not this repo | provider credentials | provider-side; nothing in-repo | **HIPAA hinges here**: production PHI may only go to an endpoint covered by a BAA. Nothing in this repo establishes one for either endpoint; AWS Bedrock and the Anthropic API each require an executed agreement outside this codebase. The reference cards and prompts add no PHI, but the case body is transmitted whole. |
| 9 | `results/spend.json` / `spend_record.json` — `case_id` per entry | no | filesystem only | `rm`/edit only | Case **identifiers** only, no clinical content; identifiers can still be PHI if case ids encode patient info in production. |
| 10 | uvicorn access logs (stdout / wherever the operator redirects them) — URLs with case ids (`/api/inbox/<case_id>/answer`) and job ids | wherever stdout goes | n/a | n/a | Identifiers in logs; no clinical content in URLs. |
| 11 | Playwright artifacts: failure screenshots, traces (`results/playwright-artifacts/`) render case content pixel-for-pixel | no | filesystem only | cleared by the next test run | Only exists where the test suite runs; keep test machines off production data. |
| 12 | `eval/dev_labels.jsonl`, reports (`results/*.md`), notes | no | read-gate by convention + test (`eval/test_leakage.py`) for labels | `rm` only | Labels/reports reference case ids and denial semantics, not patient identity, in the current corpus. |

**Flags — what would be a problem under HIPAA with production data, as the
code stands:**

1. **PHI to a non-BAA endpoint (touchpoint 8).** The entire case, including
   chart notes and any operator-supplied documents, is transmitted to
   Bedrock or the Anthropic API on every resolve. Without an executed BAA
   covering the specific endpoint and account, this is the largest single
   issue. Nothing in the repo asserts or checks for one.
2. **PHI in version control (touchpoint 4).** Predictions, transcripts, and
   raw model responses — which quote case segments verbatim — are committed
   and pushed. With production data this puts PHI into git history on
   GitHub, where deletion is effectively impossible without history rewrite.
3. **Unencrypted, unauthenticated local storage (touchpoints 1–5, 9).**
   Every persistence layer is plaintext JSON/text under `results/` and
   `corpus/` with no encryption at rest, no authentication on the serving
   apps, and (except queue-clear for finished jobs) no deletion tooling.
4. **A shadow copy of every prompt in `.cli-home/` (touchpoint 5).** The
   CLI's own session transcripts duplicate the full case per resolve outside
   the directories the repo's own storage story documents, with no pruning.
5. **Cleartext transport (touchpoint 6/7).** All app traffic — case uploads,
   SSE streams carrying model reasoning, inbox answers — is plain HTTP;
   safety currently rests entirely on binding to localhost. `internal_api`'s
   own docstring says "do not expose publicly"; nothing enforces it.
6. **PHI in reasoning streams (touchpoints 5, 6).** The `reasoning` buffer
   and SSE stream forward the model's thinking, which restates case facts;
   it is retained in the CLI transcripts (5) even though the app's own
   buffers are memory-only.
