# Mohenara Denial Agent

**An AI agent that resolves US medical claim denials the way an experienced biller does: it reads the claim and the remittance, finds the root cause, and returns the exact next action, or stops and asks for the one fact it is missing.**

Built by [Mohenara](https://mohenara.com), AI-native, end-to-end medical billing for independent US practices. This repository is the denial-resolution engine, released as open source. It runs on the Claude Agent SDK, served through Amazon Bedrock or the Anthropic API.

| | |
|---|---|
| **Accuracy** | **87.1%** joint accuracy on 140 labeled denial cases (122/140): root cause and next action both correct |
| **Excluding deliberate escalations** | **95.2%** (120/126): the agent refuses to guess one NCCI modifier fact and hands those cases to a person by design |
| **Newest model** | **93.3%** on the 15-case comparison set with Claude Opus 5 |
| **Families at 100%** | coordination of benefits, terminated eligibility, missing referring provider, missing therapy modifier, therapy threshold (KX), clean paid claims |
| **Every output** | schema-validated before it is stored; every citation points to a real reference file |
| **Tests** | 391 offline tests (no API key, no spend) plus live suites for the human-in-the-loop flow and the operator frontend |

## Why denials

Roughly one claim in seven is denied or delayed on first submission, and a large share of denials are never worked, because working them means reading X12 835 remittances, CARC and RARC codes, payer rules and the original 837 claim side by side. For an independent practice that is revenue left on the table every month.

This agent does the reading. For each denial it produces:

- **Root cause**: why the payer denied it, in billing terms (for example "secondary claim filed as primary: Medicare is primary").
- **Next action**: the specific correction (rebill to the right payer, add the KX modifier, appeal with the referring provider's NPI, write off a true duplicate).
- **Rationale with citations**: the segments of the claim and remittance it relied on, and the reference card that supports the rule.
- **Or a question**: when the answer depends on a fact that is not in the paperwork (was prior authorization obtained? what is this commercial payer's filing limit?), it parks the case in an `awaiting_human` state, asks one specific question, and resumes once a person answers.

## What it handles

Ten denial families common in outpatient physical therapy billing:

| Family | Remit signature | Typical fix |
|---|---|---|
| Coordination of benefits | `MA04`, `CO-22` / `OA-22` | Bill the true primary payer first, then rebill as secondary |
| Terminated eligibility | `N30`, `PR-27` / `CO-27` | Verify coverage dates, bill the active payer or the patient |
| Exact duplicate | `OA-18` + `N111` | Confirm the original paid; do not resubmit |
| Missing referring provider | `CO-16` + `N286` | Add the referring provider and NPI, resubmit as a corrected claim |
| Missing therapy modifier | `CO-4` + `N822` | Add GP/GO/GN and resubmit |
| MUE exceeded | `CO-151` + `N362` | Check units against the medically unlikely edit, correct or appeal |
| NCCI procedure-to-procedure | `CO-236` + `N20` | Decide on modifier 59 / X{EPSU} from documentation, or escalate |
| Therapy threshold without KX | `CO-119` + `N435` | Append KX with medical-necessity documentation |
| Timely filing | `CO-29` + `N211` | Find proof of timely filing or write off |
| Clean paid claim | `PR-2` + `CO-45` | No action; recognise and close |

## Inputs

Either the raw X12 artifact set for one case (`837P` claim, `835` remittance, `277CA` acknowledgment, `270`/`271` eligibility, chart note) or a prose `case.md` rendering of the same case. A deterministic converter (`tools/edi2md/`, no model involved) turns one into the other, and both are scored.

## Data

All patients, practices, payers and claims in `corpus/` are synthetic and were generated for this project. Provider NPIs in the corpus are deliberately invalid (they fail the NPI check digit) so none can match a real provider. No real patient data, protected health information or licensed code descriptors are included. CPT codes appear as codes only. Do not put real patient data into this repository or its issues.

## Quick start

    git clone https://github.com/umerlawa/mohenara-denial-agent.git
    cd mohenara-denial-agent
    make venv
    make verify-offline                   # 391 tests, no keys, no spend

    cp .env.local.example .env.local      # add AWS (Bedrock) keys or ANTHROPIC_API_KEY
    set -a; . ./.env.local; set +a
    .venv/bin/uvicorn mohenara.api:app --app-dir src --port 8765

Open <http://127.0.0.1:8765>, paste a `case.md` or upload an EDI set, and run it. The screen shows the resolution, the cited segments, the token usage and the cost of the call. `DEMO.md` covers the demo views and Docker.

## How it was built

The system was specified, built and verified by one founder directing AI coding agents, with verification as the definition of done: locked tests written before the code they check, a scorer that is the only code allowed to open the answer key, a static guard that fails the build if anything else names it, and spend gates that run before every model call. The full record of runs, costs and what did not work is in `results/`.

## Repository map

    src/mohenara/     the agent, loader, park/resume store, budget gate, FastAPI apps
    reference/        research behind every rule, cited by filename
    reference/runtime the distilled cards the agent actually loads
    corpus/           140 labeled synthetic cases, EDI and markdown
    eval/             runner, scorer and verification suites
    results/          every scored run, the matrix, model comparisons, notes
    docs/             architecture as built

---

## What it will not do

**Guess.** A denial whose resolution depends on a fact that is not in the
artifacts — whether a prior authorization was actually obtained, what a
commercial payer's contractual filing limit is — does not get a confident
answer. It parks in an explicit `awaiting_human` state with a specific
question, waits for the answer, and resumes to completion using it. The
frontend's inbox and the scripted test go through the same function
(`store.answer`), so the tested path is the operator's path.

The trade is real and visible in the numbers: parked cases score as wrong,
because the label space has no "need more information" value. See
`results/notes/parking-hypothesis.md`.

## Run it

    make venv
    cp .env.local.example .env.local     # AWS creds; gitignored, never committed
    python tools/bedrock_preflight.py    # which models this account can invoke

    # the local frontend: paste or upload a case, run it, see cost and tokens
    .venv/bin/uvicorn mohenara.api:app --app-dir src --port 8765

    # one eval run, then score it -- separate commands, deliberately
    python eval/run_eval.py --slice eval/slices/dev15.txt --format edi \
        --model opus-4-6 --effort low --run-id my-run
    python eval/score.py --predictions results/my-run --slice eval/slices/dev15.txt

## Verification is the definition of done

    make verify-offline          # free: scorer, schema, loader, gate, budgets
    make verify VERIFY_LIVE=1    # everything, including the suites that spend
    tools/verify_clean_checkout.sh   # the same, from a fresh clone of HEAD

`eval/VERIFICATION.md` is the plan and says what each loop proves. The short
version:

**Offline** — 391 tests, no API key needed, nothing spent:

| loop | what would be wrong if it failed |
|---|---|
| `verify-scorer` | the accuracy number itself |
| `verify-schema` | an invalid resolution could be persisted |
| `verify-loader` | an uploaded case could render differently from the same case on disk |
| `verify-leakage-static` | something other than the scorer could be reading the answer key |
| `verify-gate` | a verification run could spend money while reporting "skipped" |
| `verify-billing` | a call could be charged and never reach the ledger |
| `verify-inbox` | a case that parks twice could vanish from the inbox |
| `verify-citations` | a citation could name a file that does not exist |
| `verify-tokens` | the displayed cost could differ from what the API charged |
| `verify-budget` | the two budgets could bleed into each other |

**Live** — needs `VERIFY_LIVE=1` and spends money:

| loop | what would be wrong if it failed |
|---|---|
| `verify-leakage` | the system could behave differently with the answer key present |
| `verify-human` | the parked-case round trip could be broken |
| `verify-frontend` | the operator's five journeys |

`make verify` without `VERIFY_LIVE=1` names the suites that did not run and
**exits non-zero**. Only the full run earns the green line.

## How it is put together

    src/mohenara/
      loader.py    corpus -> Case. Byte-stable. ONE renderer, shared by the
                   eval and the frontend's upload path, so both measure the
                   same prompt.
      prompts.py   the cacheable prefix: system prompt + distilled reference
                   cards. Case data always last.
      resolve.py   one Agent SDK turn, structured output, schema-validated
                   before anything is persisted.
      store.py     park / answer / resume. The awaiting-human state machine.
      spend.py     the budget gate. Runs BEFORE each call, per provider,
                   under an flock so separate processes cannot lose a write.
      pricing.py   usage fields -> dollars. A model with no rates RAISES.
      config.py    config/models.json. Swapping a model is a config change.
      api.py       FastAPI + a single-page frontend.

    reference/          full research, cited by filename
    reference/runtime/   the distilled cards the system actually loads
    eval/               runner, scorer, and the verification suites
    results/            the scored record

**Deterministic layers contain no model calls**: `loader`, `pricing`, `spend`,
`score`, `config`. Anything that parses, renders, or scores is testable without
an API key, and is tested that way.

**The system cannot read its own answer key.** Only `eval/score.py` opens the
label file. A static guard fails the build if any other file so much as names
it, and `eval/test_leakage.py` deletes the labels from a checkout and asserts
the assembled prompt bytes are identical with and without them.

## Cost

Every call's usage fields are recorded per case: input, output, cache read,
cache write, and dollars. The prefix is engineered to be cacheable and holds an
86–92% cache hit rate in the final runs.

Two budgets that never mix, both gated in `spend.py` before the call:

| provider | cap | eval stop |
|---|---:|---:|
| bedrock | $50 | $45 |
| anthropic | $9 | $8 |

The eval stop is lower than the cap on purpose. Eval runs halt at the stop; the
live verification suites are not eval runs and draw from the band above it, so
proving the system works can never be crowded out by measuring how well it
works.

`results/spend_plan.md` records what was planned and, in three revisions, what
the plan got wrong.
