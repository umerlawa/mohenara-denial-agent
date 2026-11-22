# Verification plan

`make verify` is the only definition of done. Every loop below is a command
that is green or red with no judgement call. Accuracy claims exist only as
scorer output; nothing in this repo asserts a number a human typed.

This document ships **before** the resolution system, with the scorer, so
nothing that gets measured is built before the thing that measures it.

---

## 0. Model configuration, and a deviation you need to know about

The task specifies Claude Opus 5 and Claude Sonnet 5. **Neither is reachable
from this AWS account.** Verified against Bedrock, reproducible with
`python tools/bedrock_preflight.py`:

```
NOT-ENTITLED   us.anthropic.claude-opus-5      (account model access; AWS case open)
NOT-ENTITLED   us.anthropic.claude-sonnet-5
NOT-ENTITLED   us.anthropic.claude-opus-4-8 / 4-7
SUCCESS        us.anthropic.claude-opus-4-6-v1
SUCCESS        us.anthropic.claude-sonnet-4-6
```

The build therefore runs on **Opus 4.6 + Sonnet 4.6**, the nearest faithful
substitute: an Opus/Sonnet pair with the same effort parameter, adaptive
thinking, and prompt caching, which preserves the shape of the matrix exactly.

One consequence: **efforts are `low` / `high` / `max`, not low/high/xhigh.**
`xhigh` arrived with Opus 4.7 and returns a 400 on 4.6:

```
output_config.effort: Input should be 'low', 'medium', 'high' or 'max'
```

Three distinct tiers, same experiment. Switching to Opus 5 later is a model-ID
change plus a matrix re-run; the scorer, schema, reference files,
awaiting-human flow, and frontend are all model-agnostic.

Capabilities exercised against both models before committing to them, not
assumed:

| Capability | Opus 4.6 | Sonnet 4.6 |
|---|---|---|
| InvokeModel via Anthropic SDK | yes | yes |
| `effort` low/medium/high/max | yes | yes |
| adaptive thinking, populated blocks | yes | yes |
| prompt caching, real `cache_read` | yes | yes |

Caching proof (identical on both): first call `cache_write=9635`,
`cache_read=0`; second call `cache_write=0`, `cache_read=9635`.

**Opus 4.6 needs a >=4096-token stable prefix** before caching engages at all
(Sonnet 4.6: 1024). Below that it silently no-ops — no error, just
`cache_creation_input_tokens: 0`. The suite asserts a nonzero cache read
rather than trusting the prompt layout (§5).

---

## 1. Spend plan

Hard cap **$50**. The harness accumulates real dollar cost from API usage
fields into `results/spend.json` after every call. At **$45** all eval runs
stop and the harness reports; at **$50** it refuses to spend.

Bedrock `us.*` rates (not Anthropic first-party), per MTok:

| | input | output | cache write 5m | cache read |
|---|---|---|---|---|
| Opus 4.6 | $5.50 | $27.50 | $6.875 | $0.55 |
| Sonnet 4.6 | $3.30 | $16.50 | $4.125 | $0.33 |

Envelope:

| Phase | Cap | Notes |
|---|---|---|
| Calibration + iteration | $14 | fixed 15-case slice, repeated |
| Eval matrix, 12 cells | $18 | fixed 50-case stratified slice |
| Final full labeled slice | $12 | 140 cases x 2 formats, once, at the default config |
| Reserve | $6 | re-runs after a fix |
| **Total** | **$50** | |

**These are estimates and I do not trust them yet.** Phase 0 is a calibration
run on the 15-case slice at one effort per model, purely to measure real
per-case cost. The matrix cost is recomputed from measured numbers and written
to `results/spend_plan.md` *before* any matrix cell runs. If the measured
matrix exceeds $18, the slice shrinks — the budget does not move.

Tiering rule, enforced by the runner refusing out-of-tier sizes:

* iterate on the fixed 15-case slice;
* at each milestone, the fixed 50-case stratified slice (the matrix runs here);
* the full 140-case labeled slice runs **once**, at the end, at the chosen default.

---

## 2. Scorer — `make verify-scorer` *(implemented)*

`eval/score.py` is the only code in the repo that opens `dev_labels.jsonl`.
No model calls: same inputs, same numbers, always.

Headline metric is **joint accuracy** — a case is correct only when both the
root-cause family and the next-action path match. Per-field accuracy is
reported alongside, because a system can look strong on one field and be
useless on the other.

Scoring decisions that are easy to get wrong, made explicit and tested:

* a labeled case with **no prediction counts as wrong**, not skipped —
  otherwise a run inflates its score by answering only the easy cases;
* malformed, schema-invalid, and still-parked predictions each count as wrong
  under their **own** reason code, so a red score is diagnosable;
* predictions for unlabeled cases are ignored and counted, not errors;
* trap cases score normally on the headline fields and are excluded from the
  line-level metric, per corpus governance.

Fixtures in `eval/fixtures/` carry scores decided when they were written:

| Fixture | Joint | Asserts |
|---|---|---|
| `perfect` | 100% | exit 0 |
| `zero` | 0% | **negative control**: every field wrong scores 0, not "low"; exit 1 |
| `partial` | 60% | per-field 70%/70% — joint and per-field must not collapse |
| `malformed` | 90% | `unreadable_json` = 1 |
| `schema_invalid` | 90% | `schema_invalid` = 1 — proves the validator rejects |
| `missing` | 70% | `missing_prediction` = 3, denominator stays 10 |

17 tests, currently green. Includes a determinism check and a static guard
that no file outside the scorer references the label file.

## 3. Leakage — `make verify-leakage`

Copies the repo to a temp dir, **deletes `eval/dev_labels.jsonl`**, and runs
the resolution system on the 15-case slice there. Asserts byte-identical
predictions to a run with labels present. The system is physically unable to
read labels; this proves it rather than asserting it. §2's static guard is the
cheap review-time version of the same check.

## 4. Awaiting-human — `make verify-human`

Scripted, no browser:

1. feed a case whose resolution needs an outside fact;
2. assert `status == "awaiting_human"` and that `awaiting_human.question` is a
   specific question, not a generic "need more info" (asserted against a
   substring the case makes necessary);
3. inject a canned reply **through the same API the frontend uses** — not a
   test-only side door;
4. assert the case resumes, reaches `status == "resolved"`, and that the final
   resolution **uses the injected fact** (the fact appears in the evidence
   array with `artifact: "human_input"`).

Plus the inverse: a case needing no outside information must **never** enter
`awaiting_human`. Both directions, or the state is decorative.

## 5. Output schema — `make verify-schema`

Every prediction is validated against `schema/resolution.json` **at write
time**; an invalid resolution is never persisted. The `schema_invalid` fixture
proves the validator rejects rather than warns.

The schema enforces the two states as disjoint: `resolved` requires
`resolution` and forbids `awaiting_human`; `awaiting_human` requires
`awaiting_human` and forbids `resolution`. `evidence` has `minItems: 1` — a
resolution citing nothing is a guess, and the schema refuses it.

## 6. Token accounting — `make verify-tokens`

Raw API responses are stored per call under `results/<run>/raw/`. A replay
test recomputes totals from the raw responses and asserts they equal (a) the
harness's reported per-case numbers, (b) the `usage` block in each prediction,
and (c) the numbers the frontend displays. Cost is recomputed from the rate
table above, so a pricing error is a test failure rather than a silent
mis-report. Also asserts `cache_read_input_tokens > 0` on the second and later
cases of a run — the check that catches a silently broken cacheable prefix.

## 7. Transcripts — enforced by §6

Every eval run writes a per-case transcript: rendered prompt, raw response,
parsed resolution, timings. Failures are diagnosed by reading what actually
happened. A run directory without a transcript per case fails the suite.

## 8. Frontend — `make verify-frontend`

Playwright, one test per user journey:

1. run an `md` case, see root cause, next action, rationale, and **nonzero** cost;
2. run an `edi` case, same assertions;
3. awaiting-human inbox end to end: case parks, operator types the answer, case
   resumes, and the resumed resolution **contains the injected fact** and the
   case **leaves the inbox**. The journey targets the case by id rather than
   clicking the first inbox row: the inbox is shared with eval runs, and
   answering someone else's parked case would satisfy every other assertion
   while proving nothing about this one;
4. results view over `results/` showing numbers **identical** to the files on
   disk, not recomputed in the browser;
5. **upload** an `edi` artifact set through the file picker, resolve it, and
   assert the cache still engages — a nonzero cache read is the observable
   signal that the uploaded case rendered to the same prefix the eval scored.

Screenshot on failure. **I read the screenshot before attempting a fix** —
no blind fixes.

## 8b. Input paths — `make verify-loader`

The brief asks for paste **or upload**, and an `edi` case is an artifact *set*,
not a document. The risk this loop covers is not "upload fails loudly" but
"upload succeeds and renders differently": the frontend and the eval share one
resolver and one cached prefix, so a second renderer would mean every cost,
token and accuracy number shown to the operator described a prompt the eval
never scored, and nothing else in the suite would notice.

There is therefore exactly one renderer, `loader.render_edi`, and both entry
points go through it. Offline tests assert an uploaded artifact set is
**byte-identical** to the same case read off disk, that the render does not
depend on the order a file picker hands the files over, that a missing artifact
is reported as absent rather than silently omitted (absence is evidence), that
unknown files are ignored rather than appended, and that a full path is matched
by basename.

## 8c. Loops added by an adversarial review

Five review agents, one refutation pass; 40 findings raised, 28 survived. The
loops those produced, each named by what would be wrong if it failed:

- **`verify-billing`** — a call could be charged and never reach the ledger.
  Two paths raised before recording: a failed turn, and a turn that returned no
  structured output. Both had already been billed. With retries on top, one
  case could burn three billed turns and record none. The SDK turn is stubbed,
  so this is offline.
- **`verify-inbox`** — a case that parks a second time could vanish. `answer()`
  filed every resumed case as resolved and deleted it from the inbox, including
  when the resumed case had come back `awaiting_human` with a new question.
- **`verify-citations`** — a citation could name a file that does not exist. An
  invented citation reads as provenance and cannot be followed. Measured: 382
  citations, all resolving to real files at one of the two legitimate levels.
- **`verify-leakage-static`** — the label invariant was bundled into a
  live-gated suite, so the five OFFLINE tests that enforce it never ran in
  `make verify-offline`.
- **`verify-gate`** now derives its list of live targets from the Makefile
  rather than hardcoding it, so a new money-spending target cannot go
  uncovered.

`verify-tokens` moved from the live group to the offline one: it calls no
model, and the gate was hiding 128 free tests. The offline suite went from 69
tests to 195.

## 9. `make verify`

Runs §2–§8c from a clean checkout. Offline loops (scorer, schema, fixtures)
run unconditionally. Loops that spend money are gated behind
`VERIFY_LIVE=1` and refuse to start if `results/spend.json` is at the $45
stop, so a clean-checkout verification cannot silently burn budget.

Without `VERIFY_LIVE=1`, `make verify` names the suites that did not run and
**exits non-zero**. It used to print "all suites green" directly beneath four
"skipped" lines, which is a false claim of doneness in the one place that
defines doneness.

`tools/verify_clean_checkout.sh` clones HEAD into scratch, builds a venv from
`requirements.txt`, copies in only `.env.local`, and points the clone's ledger
back at the real one via `MOHENARA_SPEND_PATH` — otherwise the verification
spends real money outside the budget it exists to verify. `VERIFY_OFFLINE_ONLY=1`
proves the checkout builds and the free suites pass without spending.

---

## Exit criteria and how each is proven

| Criterion | Proof |
|---|---|
| >=85% joint accuracy, both formats, default config | `eval/score.py` on the full labeled slice |
| Eval matrix, 12 cells | `results/matrix.md` with accuracy, tokens, cache hit rate, cost per cell |
| Every resolution schema-valid | §5, validated at write time |
| Awaiting-human works end to end | §4 scripted test |
| Frontend passes | §8 Playwright suite, five journeys |
| Paste and upload both work | §8b byte-identity tests + journey 5 |
| All suites green from clean checkout | run log in the final PR |

If accuracy plateaus below 85% after real effort, the deliverable becomes
`results/failure_analysis.md` with per-case diagnoses — read off transcripts,
not guessed.
