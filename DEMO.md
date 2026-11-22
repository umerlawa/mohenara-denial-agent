# Running the demo

## Locally, in two minutes

    git clone <this repo> && cd mohenara-denial-agent
    make venv
    cp .env.local.example .env.local     # fill in AWS keys and/or ANTHROPIC_API_KEY
    npm install                          # only if you want the Playwright suite

    set -a; . ./.env.local; set +a
    .venv/bin/uvicorn mohenara.api:app --app-dir src --port 8765

Open <http://127.0.0.1:8765>.

Three ways to give it a case, all on the Resolve tab:

- **Paste** a `case.md` or raw EDI into the box — nothing else needed.
- **Upload** an EDI artifact set (the six files for one case). Renders
  byte-identically to the corpus loader; there is a test that proves it.
- **Type a case ID** like `MOH2-000009` if the corpus is present.

The Inbox tab holds cases the system refused to guess at, with the question it
asked. Type the answer and it resumes. The Results tab reads `results/` and
shows every eval run with its real cost.

## Picking up changes from the other session

Changes are made in the remote session and pushed; this clone gets them with
`git pull`. What happens after the pull depends on the file, and the difference
below is measured against a running server, not assumed:

| changed file | to see it |
|---|---|
| `src/mohenara/static/index.html` — the whole UI | **browser refresh.** It is read from disk on every request |
| any `*.py` | **automatic**, if you started with `--reload` |
| `config/models.json`, `reference/runtime/*.md` | **restart the server** |
| `.env.local` (budgets, credentials) | **restart the server** |

The last two need a restart for two independent reasons: uvicorn's reloader
watches `*.py` only, and those values are `lru_cache`d for the process lifetime
so the system prompt stays byte-identical across a run.

Do **not** widen the watcher to `*.json` to fix that. The app writes
`results/spend.json` on every resolve, so the server would restart mid-request,
while a client is watching.

Treat this clone as **pull-only**. Editing here and pushing from the other
session diverges the two and every later pull conflicts. Budgets are the one
thing meant to differ locally, which is why they are environment variables in
gitignored `.env.local` rather than an edit to a tracked file.

## Which model the demo runs on

**The app has no model control.** There is no dropdown, no effort selector, and
no route that will tell a client which model answered. That is deliberate: the
model is a backend concern, and a client watching a demo should not be shown a
knob they have no basis to turn. Changing it is a one-line edit to `default` in
`config/models.json` followed by a restart.

The default is **`opus-5` at `high` effort, `edi` intake**, served through the
first-party Anthropic API.

| model | provider | edi | md | $/denial | |
|---|---|---:|---:|---:|---|
| **`opus-5`** | Anthropic API | **93%** | **93%** | ~$0.38 cold, less warm | **the default** |
| `opus-4-6` | Bedrock | 87% | 80% | ~$0.39 at `high` | the strongest Bedrock option |
| `sonnet-4-6` | Bedrock | 87% | 80% | ~$0.075 | the cheap one |
| `sonnet-5` | Anthropic API | 87% | 73% | ~$0.077 | |

`opus-5` is the only model that holds 93% on **both** input formats, and the
only one that does not lose ground on the prose rendering — a client pasting
their own messy case is closer to `md` than to clean EDI. That is the reason to
pay for it.

It runs through the Anthropic API rather than Bedrock because this AWS account
is **not entitled** to it: `python tools/bedrock_preflight.py` reports
`NOT-ENTITLED us.anthropic.claude-opus-5`. If you would rather it went through
Bedrock, that is a console change and not a code change — AWS console → Bedrock
→ Model access → request Claude Opus 5, re-run the preflight until it says
`SUCCESS`, then add it to `config/models.json` under the `bedrock` provider and
set `serving_provider` back to `bedrock`.

`serving_provider` in `config/models.json` names the one provider the apps may
spend on, and `config.check_default()` refuses to start an app whose default
sits anywhere else. That guard exists because the default once named a model
this account could not invoke, and nothing noticed until an operator submitted a
denial and it failed four retries deep.

## Before you demo to anyone: raise the cap

The budgets in `config/models.json` were **build guardrails**, not business
limits. They exist so an autonomous build could not run up a bill. The frontend
refuses to call at the cap.

As of this commit:

| provider | spent | cap | denials left |
|---|---:|---:|---:|
| **anthropic** — serves the apps | **$7.91** | **$9** | **~2** |
| bedrock — the build and every eval run | $45.86 | $50 | ~10 |

**Two denials is not a demo.** Raise the Anthropic cap before showing this to
anyone:

    // config/models.json
    "anthropic": { "budget_usd": 250.00, "stop_eval_usd": 200.00, ... }

or, without editing a tracked file:

    MOHENARA_BUDGET_ANTHROPIC=250 MOHENARA_STOP_ANTHROPIC=200 make serve

`make verify-default` fails while there is under one denial of headroom left, so
the budget runs out in a test rather than in front of a client.

Restart after editing. Nothing else changes — the gate, the per-call
accounting, and the two-budget separation all keep working at any number.

Two things worth keeping even for a demo. Leave `stop_eval_usd` below
`budget_usd`: eval runs halt at the lower one, so a stray eval can never
consume the headroom the live demo needs. And keep the ledger on a mounted
volume, or a redeploy resets spend to zero and the cap stops meaning anything.

## Deploying it

The app drives the Claude Code CLI as a subprocess through the Agent SDK, so it
needs a real process with Node on PATH. **Serverless hosts will not run it** —
no persistent process, no CLI binary, and a resolve takes 20-60s against
typical function timeouts. A container is the deployable unit.

**Not build-tested.** This container has a `docker` client but no daemon, so I
could not run the build. What I did check: every `COPY` source exists, the
pinned CLI version matches the one the build ran against (2.1.42), and
`.dockerignore` excludes `.env.local` and `results/`. Expect to iterate on the
first build — most likely on the `nodejs`/`npm` apt packages, whose Debian
versions lag what the CLI wants.

    docker build -t mohenara .
    docker run -p 8080:8080 \
      -e AWS_ACCESS_KEY_ID=... -e AWS_SECRET_ACCESS_KEY=... -e AWS_REGION=us-east-1 \
      -e ANTHROPIC_API_KEY=... \
      -v "$PWD/results:/app/results" \
      mohenara

That image runs unchanged on Cloud Run, Fly, Render, ECS, or any VM.

Credentials are read from the environment at run time and are never copied into
the image; `.dockerignore` excludes `.env.local` explicitly.

## If you put it somewhere clients can reach

The app has **no authentication**. Anyone with the URL can spend your budget and
read every case in `results/`. Before it goes anywhere public, put it behind
your host's access control — Cloud Run IAM, a Fly private network, or an
authenticating proxy. Easiest safe option for a live pitch: run it locally and
share your screen.

## What to show, in order

1. **Paste a case, resolve it.** Root cause, next action, the evidence it cited
   with the artifact each fact came from, and the real cost and token counts.
   The cost is read from the API's usage fields, not estimated.
2. **Show a case it refuses.** This is the differentiator. On an NCCI bundling
   denial it stops and asks for the modifier indicator instead of guessing,
   because the value is not in the claim. Answer it in the Inbox and watch it
   resume using what you told it. Most tools guess here, and a wrong guess
   sends a claim back out to be denied a second time.
3. **Open the Results tab.** Every eval run, its accuracy, and what it cost —
   the same numbers as the files on disk, which a test asserts.
