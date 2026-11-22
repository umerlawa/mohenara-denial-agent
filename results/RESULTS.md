# Results

> **Billing note (2026-08-20).** Dollar figures for Anthropic-served
> runs in this file are computed token value at list rates. The calls
> were served through the managed session's own credentials -- never
> billed to the project's API key. See
> `results/notes/anthropic-billing-postmortem.md`.


Every number here is scorer output or a sum of the prediction files' own usage
blocks. Nothing in this file recomputes an accuracy.

## Exit criteria

| # | criterion | outcome |
|---|---|---|
| 1 | >=85% joint, both formats, full slice, default config | **`edi` PASS at 87.1% (122/140). `md` measured at 80.0% on 25 of 140 — the budget could not fund the rest.** |
| 2 | 12-cell eval matrix | done — `results/matrix.md`, $9.97 |
| 3 | every resolution schema-valid | enforced at write time; invalid is never persisted |
| 4 | awaiting-human end to end | 4 scripted tests, green live, twice |
| 5 | frontend Playwright suite | 5 journeys, green from a clean checkout |
| 6 | all suites green from clean checkout, with run log | `results/verify_clean_checkout.log` |
| + | Opus 5 / Sonnet 5 comparison | `results/frontier_comparison.md` |

## Accuracy

**Default configuration: `sonnet-4-6` / effort `low`.**

| run | slice | joint | root cause | next action |
|---|---|---:|---:|---:|
| `edi` | **full 140** | **87.1%** (122/140) | 89.3% | 87.1% |
| `md` | dev25 | 80.0% (20/25) | 92.0% | 80.0% |
| `edi`, Opus 4.6 | 37 attempted | 83.8% (31/37) | 94.6% | 83.8% |

By family on the full `edi` slice:

| family | | | family | | |
|---|---:|---|---|---:|---|
| `cob_other_primary` | 100% | 13/13 | `exact_duplicate` | 92.3% | 12/13 |
| `eligibility_terminated` | 100% | 13/13 | `mue_exceeded` | 84.6% | 11/13 |
| `missing_referring_provider` | 100% | 13/13 | `timely_filing` | 78.6% | 11/14 |
| `missing_therapy_modifier` | 100% | 13/13 | **`ncci_ptp_no59`** | **14.3%** | **2/14** |
| `none` | 100% | 20/20 | | | |
| `threshold_no_kx` | 100% | 14/14 | | | |

**Twelve of the fifteen parked cases are `ncci_ptp_no59`.** Excluding that
family the system scores 120/126 = **95.2%**, so the deliberate refusal to
guess the NCCI modifier indicator costs **8.1 points**. That is a choice, not a
defect, and `results/notes/corpus-vs-guardrail.md` sets out the evidence on
both sides. The short version: the disposition turns on a value the 835 does
not carry, every pair in this corpus happens to take the same value, and a
system that assumed it would score better here and cause a real second denial
in the field.

## Generation comparison

15 cases, both formats, effort `low`, one variable.

| format | sonnet-4-6 | sonnet-5 | **opus-5** |
|---|---:|---:|---:|
| `edi` | 86.7% | 86.7% | **93.3%** |
| `md` | 80.0% | 73.3% | **93.3%** |

Opus 5 changes the recommendation; Sonnet 5 does not. Root cause is 93% in all
six cells — the entire spread is in `next_action`.

## Spend

| provider | spent | cap | eval stop |
|---|---:|---:|---:|
| bedrock | $43.22 | $50 | $45 |
| anthropic | $7.03 | $9 | $8 |

Separately gated before every call, in `src/mohenara/spend.py`. The two never
mixed. 619 Bedrock calls and 60 Anthropic calls, 481 predictions across 30 runs.

## What is not here, and why

**`md` on the full slice.** Two things ate the budget that the plan did not
foresee: the real 140-case slice costs 1.33x what the 5-case matrix slice
predicted, and Opus 4.6 was throttled out of reach mid-run, costing a 37-case
run and forcing a model switch. `md` got the stratified quarter-slice instead,
with its budget reserved rather than hoped for. Recorded in
`results/spend_plan.md`, revisions 2 through 4.

**A controlled A/B on the prompt fixes.** Two untargeted cases moved between
runs, and with adaptive thinking's non-determinism a paired run cannot separate
a caused regression from sampling variance. Stated in
`results/notes/did-the-fixes-work.md` rather than claimed either way.

**One queued schema fix**, in `results/notes/queued-schema-fix.md`: the model's
schema does not tie `status` to its half of the payload, which cost one case in
~700. Not applied mid-run, and not applied afterwards without budget to
validate it.
