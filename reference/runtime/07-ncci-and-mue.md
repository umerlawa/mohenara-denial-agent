# NCCI PTP edits and MUE (two separate families)

PTP = "these two codes were billed together": a code **PAIR** problem, keyed on **CCMI**, bypassed only by 59/XE/XS/XP/XU or an anatomic modifier. MUE = "too many units of one code": a **UNITS** problem, keyed on **MAI 1/2/3**. Never apply a CCMI rule to a units problem or an MAI rule to a code pair.

## (a) ncci_ptp_no59 — bypass modifier needed and absent

**Recognise:** a service line denied **`CO-236`**. MACs "shall assign **CARC 236 with Group Code CO and MSN 16.8** for claims that fail the PTP edits" (ncci-ptp-carc-236.md §1–§2; CMS Transmittal 4188 / CR 10852; Pub 100-04 ch.23 §20.9).

**Key routing on 236, never on N20.** No primary text instructs any RARC on PTP denials, and the MAC page documenting N20 pairs it with CARC **234** (DME). N20 corroborates same-date bundling only; no partner code, no CCMI. Do **not** present "CO-236 + N20" as a joint signature — 236 alone is still PTP (ncci-ptp-carc-236.md §3). Corpus: every 236 line also carries N20 — observation, not rule (§5b).

**Read the line:** the 236 line is the **Column Two** code, definitionally; Column One is payable. If Column One was denied, re-diagnose (ncci-ptp-and-mue.md §2). The 835 carries **neither the partner code nor the CCMI**; look the pair up in the PTP edit file for the **DOS quarter**, else `awaiting_human` — do not guess (ncci-ptp-carc-236.md §5, §8 rows 3–4).

**Disposition:** `correct_and_resubmit` only when **CCMI = 1** *and* the record documents a separate encounter, anatomic site, or specimen. Append the **most specific** modifier — anatomic (RT/LT, FA/F1–F9, TA/T1–T9, E1–E4, LC/LD/RC/LM/RI) first, then XE/XS/XP/XU, **59 only if no other modifier describes the service** — to the **Column Two** line (ncci-ptp-and-mue.md §§4–6; ncci-ptp-carc-236.md §6). Vehicle: **Medicare Part B FFS → clerical-error reopening** (modifier changes are reopening-eligible), never a new original `1` (a resend draws a duplicate denial); **commercial → corrected `7` + `REF*F8`** (ncci-ptp-carc-236.md §7; resubmission-and-frequency-codes.md §6, §7b).

**Do not:** CCMI **0**, or any §6 disqualifier (same site **and** same encounter; only rationale is different diagnoses or different descriptors; same session/same incision; distinctness undocumented) → `do_not_resubmit`, write off. Never solicit a retroactive modifier or addendum. Never `bill_patient`: this is a **coding denial, not medical necessity**; an ABN does not shift liability (§11). `CO-97` and `B15` are not PTP signatures — diagnose first (ncci-ptp-carc-236.md §4).

| condition | action | source |
|---|---|---|
| CCMI **9**, or no edit for the pair in the DOS-quarter file | `appeal` — challenge **applicability of the edit**, not the modifier | ncci-ptp-and-mue.md §3, §12 row 3 |
| Denied line **already** carried 59/XE/XS/XP/XU | Not a missing-modifier case; diagnose why the bypass failed | ncci-ptp-carc-236.md §8 row 9 |

## (b) mue_exceeded — units above the MUE

**Recognise:** **`CO-151` + `N362`** ("units of service exceeds our acceptable maximum"), MSN 15.6, MA01; the **entire claim line** for that HCPCS is denied. One code, units too high, **no pair, no CCMI** (ncci-ptp-and-mue.md §10; CMS R1421OTN / MM8853; CORPUS-CODES.md). CMS instructs this pairing.

| MAI | edit | action |
|---|---|---|
| **1** | claim-line edit; each line judged alone | `correct_and_resubmit` — split legitimately distinct units across lines with 59/XE/XP/XS/XU, 76, 77, 91 or anatomic. `appeal` only if the single line's units were genuinely correct |
| **2** | absolute per-day policy edit; excess "impossible" | `correct_and_resubmit` if the units were a keying/conversion error; otherwise `do_not_resubmit` — the excess is not payable |
| **3** | per-day clinical-benchmark edit | `appeal` with records: units actually furnished, correctly coded, medically necessary, in that order |

(ncci-ptp-and-mue.md §§8–9; CMS Medicare NCCI MUEs)

**Do not:** never split lines on **MAI 2 or 3** — they sum every line with that code on that DOS, so a modifier rebill denies again. Some Medicare MUEs are confidential: never assert a value you cannot see, argue documented units. Never `bill_patient` (group CO; ABN does not help).

Uncertain: 236's wording comes from CMS/MAC reproductions, not the X12 list. Whether commercial/MA plans send 236 is unestablished (2 MA corpus cases). A workers'-comp 236 may run off a **state** fee schedule, not the CMS NCCI file. MAI 2 is practically, not provably, unappealable.
