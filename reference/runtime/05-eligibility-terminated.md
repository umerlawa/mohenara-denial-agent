# Terminated coverage (CARC 27 / N30)

**co27** = `co27-terminated-coverage-liability.md`; bare **§** = `cob-and-eligibility.md`.

**Recognise:** CARC **27** "expenses incurred after coverage terminated" with MOA **N30**, which sets no liability. On the **271 for the DOS**: `EB*6` plus `DTP*357` before the DOS, `DTP*291` = DOS; no `DTP*357` = open-ended active coverage (§7.4). **Then the claim filing indicator**, on 835 and 837P: `MB` Medicare Part B, `CI` commercial, `HM` HMO. Corpus: **`PR-27` ×8 / `CO-27` ×5**, all `CI` (CORPUS-CODES.md).

**Disposition:** **payer type gates the group code; the group code gates the rest.** On a **Medicare FFS** remit (`MB`, MAC payer) the group code is dispositive — CMS permits billing a beneficiary only on **PR**. On a **commercial** remit (`CI`) it is only the payer's *assertion*: the binding instrument is the participation agreement's hold-harmless clause, which reaches **members for covered services** — and coverage that ended before the DOS puts the patient outside it. `CO-27` is then no automatic write-off but a defensible mis-selection. `HM`/MA: not FFS — contract governs. Medicaid: state rule (co27).

**Do not:** conclude `bill_patient` from CARC 27 alone, or `do_not_resubmit` from `CO` alone off Medicare FFS. **CARC 27 from a commercial primary on a Medicare-secondary claim means Medicare may still pay — `resubmit_other_payer`, never the patient** (co27; FCSO MSP ORM). `OA-27` asserts no liability: never `bill_patient` (§8.1). `EB*6` is not "uninsured" — one payer, one date; an `AAA` means the *inquiry* failed and grounds nothing (§7.3, §7.5). The 271 is **one-directional**: the factual predicate for self-pay, but no payment guarantee and no detrimental-reliance protection (co27).

| condition, as the artifacts show it | next_action | source |
|---|---|---|
| `MB`: `CO-27` → `do_not_resubmit`; `PR-27` + 271 inactive for the DOS → `bill_patient`, overrides cleared | PR is the only billable group code there | co27; CMS MLN ICN905367 |
| 271 `EB*R`, or any payer effective on/before the DOS; commercial primary with Medicare secondary | `resubmit_other_payer` — patient billing premature in every line of business | co27; FCSO MSP ORM; §5 |
| `CI`, `EB*6` + `357` before DOS, no successor: `PR-27` → `bill_patient`; `CO-27` → `bill_patient` too, once overrides clear | hold-harmless reaches members only; no automatic write-off (Uncertain) | co27; BCBSNC 835 guide |
| ACA/exchange grace period | DOS month 1 — do not bill, issuer must pay; months 2–3 — may bill the member | 45 CFR 156.270 |
| Payer's record contradicts the denial: `EB*1` for the DOS, `357` on/after it, or retro-termination past the state's window (6/12/18 months) | `appeal`, quoting the 271's exchange reference and date | co27; CT OLR 2007-R-0205; §7.4, §8.3 |
| Medicaid | state rule: FL may bill if the patient was told beforehand; NY may not after the provider verified; never on provider error | co27; 42 CFR 447.15; FL 59G-1.050; NY MU 2014-02 |

| override — any one blocks `bill_patient` | disposition | source |
|---|---|---|
| Retroactive Medicaid eligibility (**3 months** pre-application) | bill Medicaid; refund if collected | 42 USC 1396a(a)(34); 42 CFR 435.915 |
| Medicaid-enrolled provider, covered service | payment in full | 42 CFR 447.15 |
| Patient is **QMB** | no Medicare cost sharing billable | 42 USC 1396a(n)(3)(B) |
| DOS inside an ACA grace period the issuer **pended** | termination not final | 45 CFR 156.270 |
| **Rescission** not termination — barred absent fraud; non-payment carved out | contest it | 45 CFR 147.128 |
| Hold-harmless / eligibility-verification clause covering this patient | write off | §8.2 |
| Successor payer active for the DOS, or payer reversed (`CR`)/reinstated | bill that payer; refund if collected | §5, §9 |

Uncertain: **no primary source reachable here answers the literal commercial question** — may a provider bill the patient over a commercial `CO-27`. Those rows are reasoned from contract structure, not a cited holding; practice: confirm with the payer first. Every regulatory row is a `pointer` (§11).
