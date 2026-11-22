# Frontier comparison — the spend plan, stated before anything is spent

Separate budget: **$9.00** on the Anthropic API, **$0.00 spent**, soft stop at
$8.00, gated in `src/mohenara/spend.py` per provider. The Bedrock $50 is
untouched by this phase and the two never mix.

## Published rates, read on 2026-08-13

From `platform.claude.com/docs/en/about-claude/pricing`, USD per million tokens:

| model | input | 5m cache write | cache read | output |
|---|---:|---:|---:|---:|
| Claude Opus 5 | $5.00 | $6.25 | $0.50 | $25.00 |
| Claude Sonnet 5 | $2.00 | $2.50 | $0.20 | $10.00 |

These are **first-party global** rates. They are not the Bedrock figures scaled
by anything: the `us.*` Bedrock profiles used for the 4.6 runs carry a 1.1x
regional premium that first-party global routing does not. Opus 5 at $5.00/MTok
input is therefore *cheaper per token* than Opus 4.6 on Bedrock at $5.50.

## The tokenizer changes what "tokens" means

Models from 4.7 onward use a tokenizer that emits roughly **30% more tokens for
the same text**. Opus 5 and Sonnet 5 are on it; Opus 4.6 and Sonnet 4.6 are not.

Two consequences, both of which the comparison report must respect:

1. **Token counts are not comparable across the generation boundary.** A 30%
   token increase on identical inputs is a change of unit, not a regression.
   Cost and accuracy are comparable; raw token counts are not.
2. **Every projection below multiplies measured 4.6 token counts by 1.3.**

## Measured basis, not guessed

From `results/mx-opus-4-6-edi-low/predictions`, dropping the first case (which
pays the cold prefix write) — the same warm/cold split that corrected the
Bedrock budget arithmetic:

| quantity | measured |
|---|---:|
| cache read per warm case | 31,983 tok |
| cache write per warm case | 5,058 tok |
| output per warm case | 838 tok |
| cold prefix write, once per run | 37,916 tok |

Projected at 1.3x tokens:

| model | expected warm $/case | worst case (2x output) | cold start |
|---|---:|---:|---:|
| Opus 5 | $0.0891 | $0.1163 | $0.3081 |
| Sonnet 5 | $0.0356 | $0.0465 | $0.1232 |

Four runs — 2 models x 2 formats, each paying one cold start:

| subset size | expected total | worst case total |
|---:|---:|---:|
| 5 | $1.86 | $2.17 |
| 10 | $3.11 | $3.79 |
| 15 | $4.36 | $5.42 |
| **25** | **$6.85** | **$8.68** |

## The plan

**Twenty-five cases does fit the $9 worst case ($8.68), but not the $8 soft
stop.** Sizing straight to 25 on a doubled-output assumption would risk the
gate halting the fourth run midway, which would leave the comparison
asymmetric — the one outcome that makes a comparison worthless.

So the phase runs in two steps, and the second is sized from measurement rather
than from the 2x guess:

**Step 1 — probe (~$0.93 expected).** `dev5`, both models, `edi` only, effort
`low`. Its only job is to replace the assumed 1.3x token inflation and the
assumed output length with measured numbers for these two models.

**Step 2 — comparison, sized from step 1.** Re-derive warm $/case from the
probe's own usage fields, then take the largest defined tier (25, else 15)
whose *measured* worst case leaves the $8 soft stop intact, and run it on both
models and both formats. The chosen size and its arithmetic get appended to
this file before step 2 spends anything.

## The 4.6 baseline costs nothing

Every slice file is a subset of `full140.txt` (verified), so the 4.6 side of the
comparison comes from re-scoring the existing final runs with
`--slice eval/slices/dev25.txt`. Same predictions, same scorer, same cases — no
additional Bedrock spend, and no risk of comparing against a differently-sampled
baseline.

## Configuration held constant

Effort `low`, adaptive thinking, identical system prompt and reference cards,
identical schema. The only variable is the model. Opus 5 and Sonnet 5 support
an `xhigh` effort that 4.6 does not; it is deliberately **not** used, because a
comparison that changed two things at once would not tell us which one moved
the number.

---

# Amendment — the 4.6 baseline is Sonnet, because Opus 4.6 was throttled away

`us.anthropic.claude-opus-4-6-v1` began returning `ThrottlingException`
partway through the final runs and had not cleared fifty minutes later. See
`results/notes/throttling.md`. The Bedrock phase moved to `sonnet-4-6`, which
probes SUCCESS on the same credentials at the same moment.

That changes what this comparison compares.

## What the comparison is now

| | |
|---|---|
| baseline | `sonnet-4-6` on `dev25`, **both formats**, effort `low` |
| frontier | `sonnet-5` and `opus-5` on the same 25 cases, same formats, same effort |

Two readings come out of it, and they answer different questions:

- **`sonnet-4-6` → `sonnet-5`** is the clean generational comparison. Same
  tier, same vendor, one variable: the model generation. This is the one that
  answers "does the newer generation change the default recommendation".
- **`sonnet-4-6` → `opus-5`** crosses a tier as well as a generation, so it
  answers a different and coarser question: what the best available model does
  on this task, at what price.

## A partial Opus 4.6 column, honestly labelled

The throttled Opus run reached 11 of the 25 `dev25` cases in `edi` before it
stopped. Those 11 are reported as a separate column, on their own 11-case
denominator, never merged into the 25-case figures. Eleven cases is far too few
to rank models on and the report says so where the number appears.

## What does not change

The $9 budget, the $8 soft stop, the separate ledger, the two-step probe-then-
size procedure, and the decision to pin effort to `low` on both sides rather
than reach for the `xhigh` that only the frontier models offer.

---

# Step 2 sizing, from the probe's measured cost

The probe ran `dev5` / `edi` / `opus-5` / effort `low`: 5 cases, **$0.9618**,
zero failures, cache hit 92–98%.

| | measured |
|---|---:|
| cold first case | $0.4000 (51,043 cache-write tokens) |
| warm per case | **$0.1392** |
| output per warm case | ~1,840 tokens |

The 51k cold prefix against Bedrock's 37k for the same reference cards is the
1.3x tokenizer, visible directly rather than assumed.

Sonnet 5's published rates are exactly **0.4x** Opus 5's on every field
(input, output, both cache columns). Sonnet emits more output than Opus on this
task — 4.6 Sonnet ran about 1.8x Opus's output tokens on identical cases — so
Sonnet 5 is costed at `0.4 x 1.8 = 0.72x` of Opus 5 rather than at 0.4x, which
is the conservative direction.

## What fits

Four runs — 2 models x 2 formats — with the probe's 5 cases seeded into the
`opus-5` / `edi` cell, so they are not bought twice:

| subset | projected total | against the $8 stop |
|---|---:|---|
| `dev10` | **$5.43** | fits, $2.57 margin |
| `dev15` | $7.82 | fits on paper, **$0.18 margin** |
| `dev25` | $13.15 | does not fit |

**`dev10`.** `dev15` is arithmetically under the stop and practically not: one
retry, one long case, or one cold-cache miss consumes the entire margin, and
the gate would then halt the fourth run mid-slice. An asymmetric comparison —
three models measured on 15 cases and one on 11 — answers nothing, which is
the outcome this whole two-step procedure exists to avoid. The same reasoning
that reserved `md`'s budget in the Bedrock phase applies here: complete and
symmetric beats larger and truncated.

`dev5` ⊂ `dev10` ⊂ `dev15` ⊂ `dev25`, all verified, and the 4.6 baselines cover
`dev10` fully in **both** formats — so the comparison is against the same cases
with no re-running.

## Stated plainly

Ten cases per cell is thin. A one-case difference is ten percentage points, so
this comparison can support a verdict on **cost** and on **gross** accuracy
differences, and cannot resolve small ones. The report says so where the
numbers appear, exactly as `results/matrix.md` does for its five-case cells.
