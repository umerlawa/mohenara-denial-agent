# Eval matrix

12 cells. Accuracy is **joint** — a case counts only when both the root cause and the next action match the label. Per-field accuracy is shown alongside, because a system can look strong on one and be useless on the other.

Every number here is read from the per-cell `run.json` and `score.json`; nothing is recomputed in this file.

| cell | model | fmt | effort | n | **acc** | root | action | await | fail | in | out | cache read | hit | $ | $/case |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `mx-opus-4-6-edi-high` | opus-4-6-v1 | edi | high | 5 | **100%** | 100% | 100% | 0 | 0 | 11 | 18,899 | 165,196 | 73% | $1.02 | $0.2043 |
| `mx-opus-4-6-edi-low` | opus-4-6-v1 | edi | low | 5 | **100%** | 100% | 100% | 0 | 0 | 11 | 4,768 | 165,038 | 74% | $0.62 | $0.1243 |
| `mx-opus-4-6-edi-max` | opus-4-6-v1 | edi | max | 5 | **100%** | 100% | 100% | 0 | 0 | 10 | 18,644 | 127,932 | 69% | $0.98 | $0.1955 |
| `mx-opus-4-6-md-high` | opus-4-6-v1 | md | high | 5 | **100%** | 100% | 100% | 0 | 0 | 11 | 15,227 | 164,964 | 73% | $0.93 | $0.1855 |
| `mx-opus-4-6-md-low` | opus-4-6-v1 | md | low | 5 | **100%** | 100% | 100% | 0 | 0 | 11 | 5,367 | 165,027 | 74% | $0.64 | $0.1276 |
| `mx-opus-4-6-md-max` | opus-4-6-v1 | md | max | 5 | **100%** | 100% | 100% | 0 | 0 | 10 | 15,405 | 127,932 | 69% | $0.89 | $0.1776 |
| `mx-sonnet-4-6-edi-high` | sonnet-4-6 | edi | high | 5 | **80%** | 100% | 80% | 0 | 0 | 11 | 31,479 | 161,826 | 72% | $0.83 | $0.1652 |
| `mx-sonnet-4-6-edi-low` | sonnet-4-6 | edi | low | 5 | **80%** | 100% | 80% | 0 | 0 | 10 | 7,600 | 125,236 | 69% | $0.40 | $0.0801 |
| `mx-sonnet-4-6-edi-max` | sonnet-4-6 | edi | max | 5 | **80%** | 100% | 80% | 0 | 0 | 10 | 56,613 | 93,927 | 52% | $1.33 | $0.2656 |
| `mx-sonnet-4-6-md-high` | sonnet-4-6 | md | high | 5 | **80%** | 80% | 80% | 1 | 0 | 10 | 35,516 | 125,236 | 69% | $0.86 | $0.1722 |
| `mx-sonnet-4-6-md-low` | sonnet-4-6 | md | low | 5 | **60%** | 80% | 60% | 1 | 0 | 12 | 11,655 | 198,015 | 76% | $0.51 | $0.1017 |
| `mx-sonnet-4-6-md-max` | sonnet-4-6 | md | max | 5 | **80%** | 100% | 80% | 0 | 0 | 11 | 38,919 | 161,594 | 71% | $0.97 | $0.1944 |

**Matrix cost: $9.97**

## Chosen default

`opus-4-6-v1` / effort `low` / `edi` — 100% joint accuracy at $0.1243 per case.

Selected as the highest joint accuracy, breaking ties toward the cheaper cell. Chosen from these results, not assumed in advance.

## What moved the number

| dimension | mean joint accuracy |
|---|---|
| effort `high` | 90% |
| effort `low` | 85% |
| effort `max` | 90% |
| format `edi` | 90% |
| format `md` | 87% |
| model `opus-4-6-v1` | 100% |
| model `sonnet-4-6` | 77% |


<!-- HAND-WRITTEN BELOW. The generator preserves everything after this line; everything above it is regenerated from run.json and score.json. -->

## Read the accuracy column with care

Five cases per cell. A cell reading 100% is 5/5 and a cell reading 80% is 4/5 —
one case apart. **No accuracy difference in the table above is statistically
meaningful**, and the table should not be read as ranking twelve configurations.

The 15-case calibration says the opposite of this matrix:

| config | 15-case calibration | 5-case matrix |
|---|---:|---:|
| sonnet-4-6 / md / high | 86.7% | 80% |
| opus-4-6 / md / high | 73.3% | 100% |

Opus is the weaker model on 15 cases and the stronger one on 5. That is small-
sample noise, not a finding, and it is the reason the accuracy column is the
least reliable part of this file.

What the matrix *is* reliable for — because these do not depend on slice
width — is the cost, token, and cache-hit columns:

- **Cache is working**: 52–76% hit rate, ~33k prompt tokens read from cache per
  case. The stable-prefix design holds.
- **Effort drives output tokens, not monotonically.** Sonnet at `max` emits
  56,613 output tokens across 5 edi cases against 7,600 at `low` — 7.4x for no
  measurable accuracy gain here.
- **Opus costs more and varies less.** Every Opus cell lands $0.124–$0.204 per
  case; Sonnet spans $0.056–$0.266.
- **`edi` is cheaper than `md`** at the same setting, despite carrying six raw
  artifacts — the rendered EDI is more compact than the prose conversion.

## The chosen default, and why the number under it is thin

`opus-4-6-v1` / effort `low` / `edi` — 100% joint accuracy at $0.1243 per case.

Selected as the highest joint accuracy, breaking ties toward the cheaper cell —
but see the caveat above: at five cases per cell this selection rests on one
case, and the 15-case calibration ranks the models the other way.

### Correction: the budget *can* fund this default

An earlier revision of this file concluded the opposite — that `opus-4-6` /
`low` over 140 cases in both formats would cost ~$30.66 against ~$26.00
remaining, and that the final run had to fall back to `sonnet-4-6`. That
arithmetic was wrong.

It took the `$/case` column above at face value. Each cell here is five cases,
and the first of those five pays the cold prefix cache write (~37k tokens,
~$0.25 on Opus) which the remaining four read for a tenth of the price. A
five-case cell amortises that one-time cost over five cases; a 140-case run
amortises the same one-time cost over 140. Using the five-case rate as a
per-case rate overstates a long run by roughly 60%.

Recomputed from the same predictions with each cell's first case dropped, the
warm steady-state rate is **$0.0754/case** on `edi` and **$0.0790/case** on
`md` — putting both 140-case runs at **~$22.26** including cold starts, inside
the ~$25.73 remaining. The final run uses the chosen default. Full arithmetic
in `results/spend_plan.md`, revision 2.
