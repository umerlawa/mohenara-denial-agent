# Spend plan (recomputed from measurement)

Hard cap **$50**. Stop all eval runs at **$45**. Refuse to spend at **$50**.
Enforced in `src/mohenara/spend.py`, checked *before* each call.

`eval/VERIFICATION.md` committed to recomputing this from measured numbers
before any matrix cell runs, and to shrinking the slice rather than the budget
if it did not fit. It did not fit. This is the revision.

## What the first estimate got wrong

Planned $18 for the matrix on a 50-case slice, from a guessed $0.06/case.
Measured on a real run (`results/baseline-noref-sonnet-low/`, Sonnet 4.6,
low effort, reference library still empty):

| Component | Warm case | Share |
|---|---|---|
| output (thinking + JSON) | $0.0413 | 54% |
| cache **write** of case data | $0.0211 | 28% |
| cache read of prefix | $0.0140 | 18% |
| **total** | **$0.0764** | |

Two surprises. Output dominated — 2,503 tokens at *low* effort, mostly
thinking, for a document that needs a few hundred. And the per-case cache
*write* is pure overhead: the varying tail gets cached and is never reused.

Then the reference library landed at 294KB (~74k tokens). Loading it whole
put the prefix at ~96k tokens including harness overhead, which would have
made the twelve-cell matrix roughly **$34** — nearly the entire remaining
budget, for one artifact.

## Changes made in response

1. **Runtime reads distilled cards, not raw research.** `reference/*.md` stays
   as the cited authority; `reference/runtime/` holds decision cards derived
   from it. Cuts the prefix by roughly 6x.
2. **Brevity enforced, not requested.** Prompt caps explanation and detail at
   50 words, rationale at 80; `schema/resolution.json` enforces 700/700/1200
   characters, so an overrun is invalid and never persisted.
3. **Matrix slice shrinks to 25 cases**, stratified, five per family — down
   from 50. The budget does not move.

## Revised envelope

| Phase | Cap | Basis |
|---|---|---|
| Spent to date | $0.46 | capability probes, smoke test, cost measurement |
| Calibration (dev15, both models) | $3 | re-measure after the changes above |
| Eval matrix, 12 cells x 25 cases | $18 | sized from calibration, not from guesswork |
| Final labeled slice, 140 x 2 formats | $14 | once, at the chosen default |
| Reserve | $14 | re-runs after a fix; frontend and live suites |
| **Total** | **<= $50** | |

The matrix figure is a ceiling, not a forecast. If calibration says twelve
cells at 25 cases exceed $18, the slice shrinks again — to 15, matching the
iteration tier — and this file is revised before the run, not after.

## Tiering, enforced in code

`eval/run_eval.py` refuses a slice that is not a defined tier (15 / 25 / 50 /
140) unless `--allow-any-size` is passed deliberately. An accidental
full-corpus run cannot quietly consume the budget.

---

# Revision 2 — the final run, priced from warm-cache measurement

Written **before** the final run spends anything, as the brief requires.

## The error this revision corrects

`results/matrix.md` concluded that the budget could not fund the chosen
default (`opus-4-6` / `low`) across both formats, and fell back to
`sonnet-4-6`. That conclusion was wrong, and wrong in a way worth naming: it
divided each matrix cell's total cost by five cases.

A five-case cell pays the cold prefix cache write once (~37k tokens) and
amortises it over five cases. A 140-case run amortises the identical one-time
write over 140. Using the five-case figure as a per-case rate therefore
inflates a long run by roughly 60%.

Measured directly from the matrix predictions, dropping each cell's first
case (the one that paid the cold write):

| config | cold first case | **warm $/case** | cache write/case | output/case |
|---|---:|---:|---:|---:|
| `opus-4-6` / `edi` / low | $0.3201 | **$0.0754** | 5,058 | 838 |
| `opus-4-6` / `md` / low | $0.3222 | **$0.0790** | 5,045 | 971 |
| `sonnet-4-6` / `edi` / low | $0.1754 | $0.0563 | 5,058 | 1,520 |
| `sonnet-4-6` / `md` / low | $0.2214 | $0.0718 | 5,574 | 2,150 |

## The plan

| line | cost |
|---|---:|
| Spent before this phase | $19.27 |
| Frontend Playwright suite (live, sonnet/low, ~5 calls) | ~$0.30 |
| Live verification suites in `make verify` | ~$0.60 |
| Final run — `opus-4-6` / `low` / `edi`, 140 cases | $10.56 + $0.32 cold = **$10.88** |
| Final run — `opus-4-6` / `low` / `md`, 140 cases | $11.06 + $0.32 cold = **$11.38** |
| **Projected total at the $45 eval stop** | **~$42.43** |
| Headroom to the eval stop | ~$2.57 |
| Headroom to the $50 refuse ceiling | ~$7.57 |

The chosen default is affordable. `sonnet-4-6` is not needed as a fallback and
the two partial Sonnet cases already run are parked under
`results/abandoned/`; their $0.26 is already in the ledger and is not
re-counted above.

## What protects the headroom

- `--resume` on `eval/run_eval.py` skips cases already predicted, so a run
  that dies at case 90 costs nothing to restart. Before this flag a restart
  re-bought every completed case, which is how a $22 plan becomes a $44 one.
- The gate in `spend.py` still runs before every call. At $45 eval runs halt
  mid-slice and the partial run is scored and reported as partial. The plan
  above is a forecast; the gate is the enforcement.
- Contingency if warm cost runs high: `edi` is the chosen default format and
  runs first, so exit criterion 1 has a scored result on the default
  configuration even if `md` is cut short.

## The Anthropic budget is untouched by all of this

$9.00, $0.00 spent, separate ledger, separate gate. The frontier comparison
prices itself from its own measured subset and never draws on the $50.

---

# Revision 3 — the budget cannot buy both full formats, and here is the number

Written mid-run, from 29 completed cases of the final `edi` run, before the
`md` run spends anything.

## What revision 2 got wrong, and why

Revision 2 fixed a real error (dividing five-case cells by five, which double-
counted the cold cache write) and introduced a smaller one: it took the warm
per-case rate from the **five-case matrix slice** and applied it to 140 cases.

The matrix slice is not representative of the full slice. Measured:

| | warm $/case | output tok/case |
|---|---:|---:|
| `dev5` matrix slice, opus-4-6/edi/low | $0.0754 | 838 |
| full 140 slice, same configuration | **$0.0999** | **1,376** |

**1.33x.** Nothing about the pricing changed; the cases are harder. Five cases
sampled the cheap end of a distribution whose median ($0.0838) sits well below
its mean, because a minority of cases reason far longer than the rest.

This is the same class of error twice in a row — extrapolating a long run from
a short sample — and it is worth naming as such rather than quietly patching
the number again. A five-case cell is a cost *probe*, not a cost *rate*.

## Where that leaves the budget

| line | $ |
|---|---:|
| spent at the time of writing | 22.96 |
| finish `edi` (111 cases remaining) | 11.09 |
| **subtotal, `edi` complete at the chosen default** | **34.05** |
| `md`, full 140 cases, would cost | 14.66 |
| would land at | **48.71** |
| eval stop | **45.00** |

**Both full formats do not fit, at any configuration measured.** $22.04 remains
for 280 cases, which is $0.079/case; the cheapest measured warm rate on the
real slice is Sonnet 4.6 / `edi` at roughly $0.077, and `md` costs more than
`edi` in every cell of the matrix. Switching the default to Sonnet would not
close the gap either, and it would abandon the 29 Opus cases already bought.

## The decision

The brief's own rule for this situation is *shrink the slice, never the
budget*. So:

1. **`edi` runs to completion** at the chosen default. That is the default
   format, and it yields one complete 140-case result at the chosen
   configuration — exit criterion 1 answerable on `edi`.
2. **`md` runs on the same full slice with `--resume`**, and the $45 gate stops
   it where it stops — roughly 104 of 140 cases. Not truncated to a smaller
   tier: 104 scored cases carry more evidence than a clean 50, and `--resume`
   means the remainder costs nothing extra if budget is ever added.
3. **`md` is scored twice, and both numbers are reported.** Strictly against
   the full slice, where missing counts as wrong and a cut-short run scores low
   *by construction*; and against the subset it actually attempted. The first
   says how much of the slice the budget bought. The second says how the system
   performed on what it bought. Neither is offered instead of the other, and
   the strict number is the headline.

## What is not being done

The gate is not being raised, the slice is not being cherry-picked, and no
per-case cost is being reduced by asking for less reasoning — the brief puts
accuracy first and cost second, and 1,376 output tokens at `low` effort is what
this corpus costs to reason about correctly.

The live verification suites are unaffected. They are not eval runs, so they
draw from the $45–$50 band by design; that band exists precisely so that
proving the system works cannot be crowded out by measuring how well it works.

---

# Revision 4 — what the last of the budget buys, and why `md` runs `dev25`

The three specification fixes cost the 71-case pre-fix run (kept as the before
side) and left roughly $17 to the $45 stop. The full `edi` slice takes about
$13 of that, so `md` gets about $3.7 — enough for roughly 35 cases of the full
slice, or for `dev25` complete.

**`md` runs `dev25`.** Three reasons, in order:

1. **Complete beats truncated.** 35 cases cut off by a budget gate is a partial
   run that has to be reported with a caveat and scored twice. 25 cases that
   finish is a result.
2. **Stratified beats arbitrary.** `dev25` is sampled across defect families by
   design. A 35-case prefix of `full140.txt` is whatever the case-id ordering
   happens to give, which covers the common families well and can miss a rare
   one entirely — exactly the families most worth seeing.
3. **It is the subset the frontier comparison needs.** That phase compares
   Opus 5 and Sonnet 5 against the 4.6 results *on identical cases*, and the
   4.6 side is meant to come free by re-scoring the final runs with
   `--slice eval/slices/dev25.txt`. That works for `edi` because `dev25` is a
   subset of `full140`. It only works for `md` if the `md` run actually covers
   `dev25` — which a 35-case prefix would not.

So `edi` answers exit criterion 1 on the full labeled slice at the chosen
default, and `md` gives a complete, stratified, comparable result on a quarter
of it. `md` on the full slice is unfunded, and that is stated rather than
worked around.
