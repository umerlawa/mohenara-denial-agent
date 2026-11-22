# Observed mid-run: parking is the likely dominant failure mode

Recorded during the final `edi` run, before scoring, so that the diagnosis is
on record as a *hypothesis formed from the artifacts* rather than something
reverse-engineered from the score afterwards.

## The observation

At 36 of 140 cases the run had parked 4 — an **11.1% park rate**. Three of the
four are CARC 29 timely-filing cases asking the same question: *do you have a
clearinghouse acceptance report showing an earlier, timely submission?*

`schema/resolution.json` offers no "need more information" value in
`next_action.path` — the enum is `none | appeal | bill_patient |
correct_and_resubmit | do_not_resubmit | resubmit_other_payer`. The scorer
therefore counts a parked case as wrong (`REASON_PARKED`). If most parks are
scored wrong, the park rate is very close to the gap between passing and
failing the 85% bar, so this is the first thing to check once the run scores.

## `MOH2-000055`, worked from the artifacts

| fact | source |
|---|---|
| DOS 2025-04-16 | `remit_835.edi` `DTM*232*20250416` |
| claim submitted 2025-08-10 | `claim_837p.edi` ISA/GS date, `BHT` |
| **116 days** DOS to submission | arithmetic |
| commercial product line | `remit_835.edi` `CLP*...*CI*` |
| denial CO-29 on all three lines | `remit_835.edi` `CAS*CO*29*` x3 |
| subscriber in Staten Island, **NY** | `claim_837p.edi` `N4*STATEN ISLAND*NY*10332` |
| no 277CA at all | the artifact is absent, and the render says so |

The system asked the human for Keystone's contractual filing limit. But
`reference/runtime/03-timely-filing.md` already answers it:

> **State floors override contracts** — ... NY 120d unless more favorable
> (NY Ins. Law §3224-a)

116 days is **inside** a 120-day floor. The claim is timely under the state
floor regardless of what Keystone's contract says, which makes the CO-29
contestable on the receipt date rather than a matter needing outside
information.

## Why this is a defect and not a labelling disagreement

Parking is the *correct* behaviour when a fact is genuinely absent — the brief
is explicit that the system must never guess facts it does not have, and three
of these four parks would be right if the filing limit really were unknowable
from the artifacts. It is not. The subscriber's state is on the claim and the
state floor is in the system's own reference card. Applying a documented rule
to a fact present in the artifact is not guessing; failing to apply it is a
reasoning gap.

That distinction is what keeps this from being label-fitting: the fix is
justified by `reference/runtime/03-timely-filing.md`, which was written from
primary sources long before any of these cases ran, and the label for
`MOH2-000055` has not been looked at and will not be.

## What is deliberately NOT being done

The prompt is **frozen** for the rest of both final runs. Changing it now would
invalidate the 36 cases already bought, break the cached prefix, and — worse —
mean `edi` and `md` ran different systems, which would make the format
comparison in exit criterion 1 meaningless.

The order is: finish both runs, score them, and check whether `REASON_PARKED`
actually dominates. If it does, this note is the diagnosis and the remedy is a
prompt change requiring the model to exhaust the determinable rules in the
reference cards — state floors keyed to the subscriber's address among them —
before concluding that a fact lies outside the artifacts. If it does not
dominate, this note stands as a hypothesis that measurement rejected, which is
worth as much.

---

## Confirmed by the scorer at 42 of 140 cases

Scored the completed portion against the cases actually attempted (free — the
scorer costs nothing to run):

```
  cases scored        42
  ACCURACY (joint)    85.7%  (36/42)
    root cause        90.5%
    next action       85.7%

  failures by reason
    awaiting_human         4
    wrong_next_action      2

  accuracy by defect family
    cob_other_primary            100.0%  (9/9)
    eligibility_terminated       100.0%  (5/5)
    exact_duplicate              100.0%  (5/5)
    missing_referring_provider   100.0%  (2/2)
    missing_therapy_modifier     100.0%  (5/5)
    mue_exceeded                 100.0%  (3/3)
    ncci_ptp_no59                 66.7%  (2/3)
    none                          33.3%  (1/3)
    timely_filing                 57.1%  (4/7)
```

The hypothesis holds: **4 of the 6 failures are parks**, and `timely_filing` is
the weakest family at 57.1%. Six of ten families are perfect. Eliminating the
parks alone would put this run at 95.2%.

## And the run is therefore NOT being stopped

At 85.7% it is **passing** the 85% exit criterion, with about three points of
margin. Stopping a passing run to chase a diagnosed-but-unproven improvement
would spend the 42 cases already bought, spend more on re-validating the
change, and leave less budget for `md` — while risking a prompt edit that makes
something else worse. The margin is thin enough to say plainly: if the
remaining 98 cases run harder than the first 42, this can still finish below
the bar, and that outcome would be reported as it lands.

The remedy stays written down and unapplied. It belongs in the failure
analysis, not in a mid-run prompt edit.


---

## Correction: the NY state-floor reading of `MOH2-000055` was wrong

The hypothesis above worked this case by hand and concluded that NY Ins. Law
§3224-a's 120-day floor made 116 days timely, so the CO-29 was contestable and
the answer was `appeal`.

The scorer disagrees. Post-fix, the system answered `timely_filing` /
`do_not_resubmit` — "no evidence of earlier submission in the artifacts; the
837 ISA date is the only filing date available" — and the scorer marked it
**correct**.

The flaw in the hand analysis: the subscriber's address is in Staten Island NY,
but a subscriber's *address* is not a policy's *situs*. Keystone Commercial
Health is a Philadelphia payer and the billing provider is in Wilmington DE;
nothing in the artifacts establishes that the policy was issued in New York, so
nothing establishes that the NY floor applies. The card's own framing —
"State floors override contracts" — presumes you know which state's law governs
the contract, and this case does not say.

**What survives, and what does not.** The specific claim about this case was
wrong. The general fix it motivated — check the reference library for a rule
that *determines* a fact before declaring the fact absent — was right, and this
case is evidence for it: the system stopped parking and got the case right,
just not for the reason predicted. It resolved on the simpler determinable
ground the card gives first, that CO-29 with no proof of timely filing is a
write-off.

Recorded rather than quietly deleted, because a diagnosis that measurement
contradicts is worth as much as one it confirms, and because the note above
would otherwise stand as a confident wrong answer in the record.
