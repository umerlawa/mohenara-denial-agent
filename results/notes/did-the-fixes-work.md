# Did the three fixes work? Partly, and one of them cost more than predicted

I predicted the three specification fixes would take joint accuracy from 78.9%
to about 90%. Measured on the 36 cases both runs have in common:

| | pre-fix | post-fix |
|---|---:|---:|
| joint accuracy, 36 matched cases | **86.1%** (31/36) | **83.3%** (30/36) |

**Net −1 case.** The prediction was wrong and this note says why rather than
quietly moving on.

## Decomposed by what each fix targeted

| family | n | pre | post | which fix, and what it was meant to do |
|---|---:|---:|---:|---|
| `none` | 3 | 1 | **2** | fix 1: family `none` takes path `none` |
| `timely_filing` | 5 | 3 | **5** | fix 2a: the state floor settles it; do not park |
| `ncci_ptp_no59` | 3 | 2 | **0** | fix 2b: told it explicitly to KEEP parking here |
| everything untargeted | 25 | 25 | 23 | nothing aimed at these |

Two fixes landed. **Fix 1 worked** — the `bill_patient`-for-routine-coinsurance
error is mostly gone, though `MOH2-000162` still makes it, so the instruction
is not airtight. **Fix 2a worked cleanly** — every timely-filing park became a
correct answer, 3/5 to 5/5, because the state filing floor really was
determinable from the subscriber's address on the claim.

## Fix 2b did exactly what I told it to, and that is the problem

I wrote into the prompt that the PTP edit file's CCMI is the standing example of
a park that must not be talked out of. The model complied: `ncci_ptp_no59` went
from 2/3 correct to 0/3, all parks.

**Pre-fix, the model was answering these — and answering them right.** It
reasoned from the chart documentation to "a separate site is documented, so a
bypass modifier is appropriate" and landed on `correct_and_resubmit`, which is
what the label says.

That reasoning skips a necessary condition. `reference/runtime/07-ncci-and-mue.md`
says `correct_and_resubmit` requires **CCMI = 1 *and*** documented distinctness.
Documentation alone is not sufficient: on a CCMI-0 pair no modifier can bypass
the edit no matter what the chart says, and the resubmission draws a second
denial. The CCMI is in the quarterly CMS edit file, not in any artifact the
system is given, and the card says look it up or ask — never guess.

So pre-fix the system was scoring well by assuming the unknowable value, and
every case in this corpus happens to be CCMI-1, which is exactly why the
assumption looked reliable.

**I underestimated this cost.** `results/notes/corpus-vs-guardrail.md` treated
the family as already mostly lost. It was not: the model was recovering about
two thirds of it by guessing, and the fix gives that back. On the full slice
the family is 14 of 140 cases, so this is worth roughly 6–10 points of joint
accuracy on its own.

## The two untargeted cases that moved

`MOH2-000078` and `MOH2-000140`, both `cob_other_primary`, went from
`resubmit_other_payer` to `correct_and_resubmit`. Nothing in the three fixes
addresses COB routing. With adaptive thinking the model is not deterministic,
so two runs of the same configuration differ on borderline cases — 2 of 25 is
consistent with sampling variance rather than a caused regression. I cannot
distinguish the two from one paired run and I am not going to claim I can; a
controlled A/B would cost budget that is committed elsewhere.

## The decision this forces

The brief asks for two things that collide here: **>=85% joint accuracy**, and
**never guess facts it does not have**. On `ncci_ptp_no59` they are mutually
exclusive — the corpus rewards the guess.

The guardrail wins, and the score pays for it. That is the choice the brief's
own wording makes, and reverting fix 2b to recover 6–10 points would be
teaching the system to assume an unknowable value because the assumption
happens to hold in this corpus. It would score better here and cause a real
second denial in the field on the first CCMI-0 pair it met.

The consequence is stated plainly: **exit criterion 1 is unlikely to be met at
85%, and this is the largest single reason.**
