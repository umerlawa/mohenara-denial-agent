## What the failures turned out to be

Fifteen failures in the pre-fix baseline. None of them was a reasoning error.
Every one traced to the same shape of defect: **a contract the labels or the
validator enforce, that the model was never told**. Three clusters, and a
disagreement.

### 1. `next_action` had no stated meaning — 5 cases

Every `none`-family failure got the root cause *right*: "claim adjudicated
correctly. CO-45 is the contractual fee-schedule write-off; PR-2 is patient
coinsurance. No denial, no defect." Then it answered `bill_patient`, because
PR-2 coinsurance genuinely is billable.

Step 5 of the prompt said "determine the next action from the closed list" and
never said what `next_action` *means*. Read as "what should the biller do
next", `bill_patient` is correct. Read as "what resolves the denial", `none` is
correct. The enum contains both and the spec chose neither.

Fixed by defining the term: `next_action` is the step that resolves the denial.
Family `none` takes path `none` even where routine patient responsibility
remains, because that is ordinary AR. `bill_patient` is for denials whose
resolution *is* that the balance became the patient's.

### 2. Avoidable parks — 3 cases

Three timely-filing cases asked a human for the payer's contractual filing
limit. The system's own card carries the **state floor that overrides that
contract**, keyed to the subscriber's address printed on the claim. On
`MOH2-000055`: DOS 2025-04-16, submitted 2025-08-10, 116 days, subscriber in
Staten Island NY — inside NY Ins. Law §3224-a's 120-day floor.

Applying a documented rule to a fact that is present is not guessing. Fixed by
requiring the reference library be checked for a *determining* rule before a
fact is declared absent.

### 3. The index base — every case

Diagnosed separately in `results/notes/line-index-base.md`. `schema/resolution.json`
documented `denied_line_idxs` as zero-based; the schema the *model* saw carried
no description, so it used the artifacts' own `LX*1` numbering. 36 of 43
divergences were exactly one.

### The disagreement: NCCI PTP parks — 4 cases, left wrong on purpose

Four failures are `ncci_ptp_no59` cases the system parked, asking for the
Column One/Column Two Modifier Indicator. `reference/runtime/07-ncci-and-mue.md`
says, in the system's own cited authority:

> The 835 carries **neither the partner code nor the CCMI**; look the pair up in
> the PTP edit file for the **DOS quarter**, else `awaiting_human` — do not guess.

The system did exactly what its reference told it to. The labels expect
`correct_and_resubmit`, which requires knowing CCMI = 1 — a value that is in
neither the artifacts nor the cards.

**These four were not fixed.** Making the model answer anyway would be teaching
it to guess a fact it does not have in order to score better, which the brief
forbids twice: *never guess facts it does not have*, and *CARC/RARC meanings
come from `reference/runtime/*.md`, cited by filename*. The prompt was changed
in the opposite direction — CCMI is now named as the standing example of a park
that must **not** be talked out of.

The cost is about 5.6 accuracy points on this slice. It is recorded here rather
than recovered, because the alternative is a system that looks better and is
less trustworthy. If the corpus intends these to be resolvable, the fix belongs
in the reference library — a PTP edit table for the corpus's DOS quarters —
not in an instruction to guess.

### Two that are neither

`MOH2-000187` (expected `exact_duplicate`/`do_not_resubmit`, said
`correct_and_resubmit`) is a judgement call about whether the duplicate is
false, given a chart documenting two distinct timed sessions. `MOH2-000210`
(expected `threshold_no_kx`, parked) turns on what that specific chart note
carries. Neither is a missing contract, so neither was fixed by rule.
