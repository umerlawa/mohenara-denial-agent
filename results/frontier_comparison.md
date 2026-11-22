# Frontier comparison — Claude 4.6 against Claude 5, on identical cases

> **Billing note (2026-08-20).** Dollar figures for Anthropic-served
> runs in this file are computed token value at list rates. The calls
> were served through the managed session's own credentials -- never
> billed to the project's API key. See
> `results/notes/anthropic-billing-postmortem.md`.


15 cases (`eval/slices/dev15.txt`), both input formats, effort `low`, adaptive
thinking, identical system prompt and reference cards. **The model is the only
variable.**

Accuracy is copied from the scorer's own reports. Cost and tokens are summed
from the prediction files' usage blocks, which `eval/test_token_accounting.py`
checks against the raw API responses. Nothing here recomputes an accuracy.

The 4.6 rows come from re-scoring the completed Bedrock runs against the same
15 case ids — the same predictions, the same scorer, no re-running, no
additional Bedrock spend.

## `edi`

| model | joint | root cause | next action | parked | out tok | cache hit | $/case |
|---|---:|---:|---:|---:|---:|---:|---:|
| `sonnet-4-6` (Bedrock) | 86.7% | 93% | 87% | 1 | 24,060 | 89% | $0.0636 |
| `sonnet-5` | 86.7% | 93% | 87% | 1 | 37,735 | 90% | $0.0738 |
| **`opus-5`** | **93.3%** | 93% | **93%** | 1 | 30,172 | 90% | $0.1584 |

## `md`

| model | joint | root cause | next action | parked | out tok | cache hit | $/case |
|---|---:|---:|---:|---:|---:|---:|---:|
| `sonnet-4-6` (Bedrock) | 80.0% | 93% | 80% | 1 | 27,850 | 81% | $0.0851 |
| `sonnet-5` | 73.3% | 93% | 73% | 1 | 42,183 | 94% | $0.0774 |
| **`opus-5`** | **93.3%** | 93% | **93%** | 1 | 32,793 | 93% | $0.1591 |

## Verdict

**Yes for Opus 5. No for Sonnet 5.**

**Opus 5 changes the recommendation.** It is the only model that reaches 93.3%
on *both* formats, and the only one that does not lose ground moving from `edi`
to `md` — every other configuration drops 7 to 13 points on the prose
rendering. It costs about **2.2x** Sonnet 4.6 per case. On a 15-case slice that
buys one extra case on `edi` and two on `md`, so the size of the gain is not
resolved here; its *direction* is consistent across both formats, which a
one-case fluke would not be.

**Sonnet 5 does not.** It ties Sonnet 4.6 exactly on `edi` (13/15 both) and
comes in one case *behind* on `md` (11/15 against 12/15), at slightly higher
cost on `edi` and slightly lower on `md`. For this task, at this effort, the
generational jump at the Sonnet tier is a wash — worth stating plainly rather
than dressing up, because "the newer model is not better here" is the useful
answer when it is the true one.

**Root cause is 93% in every single cell.** All six configurations identify the
defect equally well; the entire spread is in `next_action`. The models agree on
what went wrong and differ on what to do about it — which is exactly where the
reference cards carry the decision, and it says the remaining headroom is in
routing rules rather than in comprehension.

**Every cell parks exactly one case.** The refusal to guess the NCCI CCMI
behaves identically across models and generations. It is a property of the
system, not of the model.

## Two things this table would mislead you about if read carelessly

**Token counts are not comparable across the generation boundary.** Models from
4.7 onward use a tokenizer that emits roughly 30% more tokens for the same
text. Sonnet 5's 37,735 output tokens against Sonnet 4.6's 24,060 on `edi` is
mostly that change of unit, not 57% more reasoning. Cost is comparable and is
what the verdict rests on; tokens are listed per model and deliberately not
differenced.

**Fifteen cases means one case is 6.7 points.** This comparison can support a
verdict on cost, and on a difference that reproduces across both formats. It
cannot resolve small differences, and no ranking here should be read as
precise. The same caveat governs `results/matrix.md` and for the same reason.

## What it cost

$7.03 of the $9 Anthropic budget, gated separately from the $50 Bedrock budget
throughout; the two never mixed. The 4.6 baselines cost $0.00 because they were
re-scored from predictions already bought.

Sized before spending, from a measured probe rather than an estimate — see
`results/frontier_plan.md`.

## If the budget were not the constraint

`opus-5` on `md` at 93.3% is the strongest cell measured anywhere in this
project, including the full 140-case Bedrock run. The obvious next step is
`opus-5` over the full labeled slice in both formats, which at $0.159/case
would be about **$44** — more than the entire Bedrock budget this build ran on,
and the reason it is a recommendation rather than a result.
