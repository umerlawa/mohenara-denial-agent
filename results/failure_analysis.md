# Failure analysis

Per-case diagnoses for the runs below. Every accuracy figure is copied from the scorer's own JSON report; nothing here recomputes one. Each wrong case is described in the system's own words, read off the prediction it wrote, because the brief requires failures to be diagnosed by reading what happened rather than by guessing at it.

## How to read a `awaiting_human` failure

A parked case scores as wrong: the label space has no value for "needs a fact nobody gave me". Some of those parks are genuine misses, where a rule in the reference library would have settled the question from what the artifacts already carry. Others are the system doing exactly what its cited authority tells it to do, on a question the corpus expects it to answer anyway.

The `ncci_ptp_no59` family is entirely the second kind, and it is the single largest known gap between what is reported here and what could be scored by guessing. See `results/notes/corpus-vs-guardrail.md` for the evidence on both sides and why the guardrail was chosen.

## `final-sonnet-4-6-low-edi`

us.anthropic.claude-sonnet-4-6 · effort `low` · format `edi` · 140 predictions against 140 labeled cases

| joint | root cause | next action |
|---:|---:|---:|
| **87.1%** | 89.3% | 87.1% |

### Why the wrong ones were wrong

| reason | n |
|---|---:|
| `awaiting_human` | 15 |
| `wrong_next_action` | 3 |

### Families that lost cases

| family | correct | total | accuracy |
|---|---:|---:|---:|
| `ncci_ptp_no59` | 2 | 14 | 14% |
| `timely_filing` | 11 | 14 | 79% |
| `mue_exceeded` | 11 | 13 | 85% |
| `exact_duplicate` | 12 | 13 | 92% |

### The 18 cases that answered and got it wrong

#### `MOH2-000055` — `wrong_next_action`

- **expected** `timely_filing` / `do_not_resubmit`
- **said** timely_filing / appeal
- **its explanation** CO-29 on all three lines. DOS 2025-04-16, 837P submitted 2025-08-10 = 116 days. NY state floor (subscriber in Staten Island NY) is 120 days; claim was filed within that floor.
- **evidence it cited**
  - `claim_837p.edi` ISA date 2025-08-10; DOS 2025-04-16 = 116 days elapsed; filing indicator CI
  - `remit_835.edi` CAS*CO*29 on all three SVC lines; MOA N211; payer CI commercial
  - `eligibility_271.edi` EB*1 active coverage, DTP*356 2024-01-01, no termination date — coverage confirmed active on DOS
  - `reference` NY state floor 120 days overrides contract terms; 116 days &lt; 120 days; proof of timely submission supports appeal
- **rationale** All three lines denied CO-29 (timely filing). DOS 2025-04-16; 837P ISA date 2025-08-10 = 116 days. Payer is commercial (CI), patient address Staten Island NY. NY Ins. Law §3224-a sets a 120-day floor. 116 days &lt; 120 days → claim was filed within the NY state floor. MOA N211 is a Medicare-only no-appeal marker; it carries no force on a CI remit. Appeal disputing the filing date.
- transcript: `final-sonnet-4-6-low-edi/transcripts/MOH2-000055.json`

#### `MOH2-000061` — `wrong_next_action`

- **expected** `exact_duplicate` / `do_not_resubmit`
- **said** exact_duplicate / correct_and_resubmit
- **its explanation** OA-18 on all four lines. 97140 billed on lines 1 and 3, 97110 on lines 2 and 4, same DOS, no modifier 76 distinguishing the repeat procedures. Chart note confirms two separate timed blocks of each code.
- **evidence it cited**
  - `remit_835.edi` CAS*OA*18 on all four SVC lines; CLP02=4 (denied); CLP07=2623576767957 confirms adjudication; MOA N111.
  - `claim_837p.edi` Lines 1 and 3 both bill 97140:GP:KX; lines 2 and 4 both bill 97110:GP:KX — same DOS 20260705 — no modifier 76 on repeat lines.
  - `chart_note.txt` Two separate 97140 blocks (15 min, 14 min) and two 97110 blocks (31 min, 16 min) documented on 2026-07-05 — services legitimately distinct.
- **rationale** All four lines denied OA-18 (exact duplicate). Claim adjudicated — CLP07 carries ICN 2623576767957. Chart note confirms two distinct timed blocks of 97140 (15 min, 14 min) and two of 97110 (31 min, 16 min) on the same DOS. Repeat CPTs were billed without modifier 76, triggering the duplicate edit. False duplicate: services legitimately rendered. Medicare Part B → clerical-error reopening to append modifier 76 to the repeat lines.
- transcript: `final-sonnet-4-6-low-edi/transcripts/MOH2-000061.json`

#### `MOH2-000075` — `awaiting_human`

- **expected** `ncci_ptp_no59` / `correct_and_resubmit`
- **said** parked: awaiting_human
- **its explanation** What is the CCMI (Column Two Most Intensive indicator) for the CPT 97140 / 97150 pair in the NCCI PTP edit file effective Q3 2026 (DOS 2026-07-18)?
- **rationale** Line 0 (97140) denied CO-236/N20 — confirmed NCCI PTP edit. Chart note documents a separate session and distinct body region, which could support a bypass modifier — but the CCMI for the 97140/97150 pair on the DOS-quarter PTP edit file determines whether a modifier is allowed (CCMI=1), disallowed (CCMI=0), or challengeable (CCMI=9). The 835 does not carry the CCMI; the reference requires a lookup before routing.
- transcript: `final-sonnet-4-6-low-edi/transcripts/MOH2-000075.json`

#### `MOH2-000094` — `awaiting_human`

- **expected** `ncci_ptp_no59` / `correct_and_resubmit`
- **said** parked: awaiting_human
- **its explanation** What is the Column Modifier Indicator (CCMI) for the 97110 (Column Two) / 97150 (Column One) pair in the NCCI PTP edit file effective for DOS 2026-05-31 (Q2 2026)?
- **rationale** Line 0 (97110) carries CO-236+N20 — a PTP bundling denial. The chart note documents a distinct service (separate start/stop, different body region), and the claim already carries GP+KX but no bypass modifier. Disposition hinges entirely on the CCMI for the 97110/97150 pair in the Q2 2026 NCCI edit file, which the 835 does not carry. The reference prohibits guessing this value.
- transcript: `final-sonnet-4-6-low-edi/transcripts/MOH2-000094.json`

#### `MOH2-000122` — `awaiting_human`

- **expected** `timely_filing` / `do_not_resubmit`
- **said** parked: awaiting_human
- **its explanation** What is Keystone Commercial Health's timely filing deadline for outpatient participating-provider claims — is it 90 days, 180 days, or some other limit per the provider agreement or Keystone's billing manual?
- **rationale** Both lines denied CO-29 (timely filing expired) with N211. DOS 2025-02-16; claim accepted by clearinghouse/payer 2025-06-09 — 113 days after DOS. Whether to appeal (submission was within window) or write off (genuinely late) turns entirely on Keystone Commercial Health's filing deadline, which is not in the reference library. NJ has no documented state floor in the reference files.
- transcript: `final-sonnet-4-6-low-edi/transcripts/MOH2-000122.json`

#### `MOH2-000148` — `wrong_next_action`

- **expected** `timely_filing` / `do_not_resubmit`
- **said** timely_filing / appeal
- **its explanation** CO-29 on all lines, but 837P reached payer 106 days after DOS. NY Ins. Law §3224-a floor is 120 days and overrides any shorter contract limit; denial issued in error.
- **evidence it cited**
  - `remit_835.edi` All four SVC lines carry CAS*CO*29; $0 paid; MOA N211 'you may not appeal this decision' (inapplicable once NY floor is invoked).
  - `claim_837p.edi` BHT submission date 20250803; DOS 20250419 — 106 days elapsed.
  - `claim_837p.edi` Subscriber (DAVIS CHARLES) address Staten Island, NY — NY law governs.
  - `reference` NY Ins. Law §3224-a sets 120-day state floor overriding shorter contract limits; 106 days is within that floor.
- **rationale** All four lines denied CO-29. DOS 2025-04-19, 837P submitted 2025-08-03 = 106 days. Subscriber address is Staten Island, NY. NY Ins. Law §3224-a sets a 120-day state floor that overrides any shorter contract limit. 106 days &lt; 120 days — claim was timely under NY law. Denial is improper; appeal with the clearinghouse acceptance report showing the Aug 3 submission date.
- transcript: `final-sonnet-4-6-low-edi/transcripts/MOH2-000148.json`

#### `MOH2-000233` — `awaiting_human`

- **expected** `ncci_ptp_no59` / `correct_and_resubmit`
- **said** parked: awaiting_human
- **its explanation** What is the CCMI (Column II Modifier Indicator) for the 97110/97150 pair in the CMS NCCI PTP edit table effective for DOS 2026-06-25?
- **rationale** Lines 0–2 (97110×3) are denied CO-236+N20 — NCCI PTP edit, 97110 bundled into 97150. The chart note documents a clearly demarcated separate encounter on a different body region for an unrelated goal, which could support a bypass modifier — but only if CCMI=1. The 835 carries neither the Column One/Two partner confirmation nor the CCMI. The PTP edit file for Q2 2026 must be consulted before any corrected claim or write-off decision is made.
- transcript: `final-sonnet-4-6-low-edi/transcripts/MOH2-000233.json`

#### `MOH2-000251` — `awaiting_human`

- **expected** `ncci_ptp_no59` / `correct_and_resubmit`
- **said** parked: awaiting_human
- **its explanation** What is the CCMI (modifier indicator) for the 97110 (Column 2) / 97150 (Column 1) pair in the CMS NCCI PTP edit table effective Q2 2026 (April 1 – June 30, 2026)?
- **rationale** Line 0 (97110) denied CO-236 + N20 — confirmed NCCI PTP edit. Reference 07 requires looking up the CCMI for the 97110/97150 pair in the Q2 2026 PTP edit file before routing. CCMI=1 allows a clerical-error reopening with a bypass modifier; CCMI=0 mandates write-off. The chart note supports distinctness but that only matters if CCMI=1. Cannot determine disposition without the CCMI.
- transcript: `final-sonnet-4-6-low-edi/transcripts/MOH2-000251.json`

#### `MOH2-000291` — `awaiting_human`

- **expected** `ncci_ptp_no59` / `correct_and_resubmit`
- **said** parked: awaiting_human
- **its explanation** In the CMS NCCI PTP edit file effective Q2 2026 (DOS 2026-06-02), what is the Column Indicator (CCMI) for the pair 97110 / 97760, and for 97110 / 97140?
- **rationale** Lines 0 and 2 (both 97110) are denied CO-236+N20 — confirmed NCCI PTP edits. The chart note documents distinctness for both sessions. Next action (correct_and_resubmit with modifier vs. do_not_resubmit vs. appeal) turns entirely on the CCMI for the affected pairs in the Q2 2026 PTP edit file, which the 835 does not carry. Reference 07 is explicit: look it up or park.
- transcript: `final-sonnet-4-6-low-edi/transcripts/MOH2-000291.json`

#### `MOH2-000309` — `awaiting_human`

- **expected** `mue_exceeded` / `correct_and_resubmit`
- **said** parked: awaiting_human
- **its explanation** What is the MAI (Medically Unlikely Edit Adjudication Indicator) for CPT 97530 in the CMS MUE table for DOS quarter Q1 2026?
- **rationale** Lines 0–1 (97110, 97140) paid with routine CO-45/PR-2 adjustments. Line 2 (97530, 7 units) was fully denied CO-151 + N362 — MUE exceeded. Chart note documents 31 minutes for 97530 (~2 billable units), so 7 units is a keying error. Next action is correct_and_resubmit for MAI 1 or 2, but appeal for MAI 3. MAI cannot be assumed.
- transcript: `final-sonnet-4-6-low-edi/transcripts/MOH2-000309.json`

#### `MOH2-000326` — `awaiting_human`

- **expected** `ncci_ptp_no59` / `correct_and_resubmit`
- **said** parked: awaiting_human
- **its explanation** What is the CCMI (Column Modifier Indicator) for the 97150 / 97110 code pair in the Q2 2026 (April–June) CMS NCCI PTP edit table?
- **rationale** Line 2 (97110:GP) denied CO-236 + N20 — confirmed NCCI PTP edit. Disposition turns entirely on CCMI for the 97150/97110 pair in the Q2 2026 PTP edit file: CCMI=1 → correct_and_resubmit with modifier; CCMI=0 → do_not_resubmit. The 835 carries neither the partner code nor the CCMI. Reference 07 is explicit: look it up or ask, never guess.
- transcript: `final-sonnet-4-6-low-edi/transcripts/MOH2-000326.json`

#### `MOH2-000445` — `awaiting_human`

- **expected** `ncci_ptp_no59` / `correct_and_resubmit`
- **said** parked: awaiting_human
- **its explanation** What is the CCMI (Column II modifier indicator) for the 97110 / 97760 PTP edit pair in the Q1 2024 (January 2024) CMS NCCI edit file?
- **rationale** Lines 0 and 2 (97110:GO) are denied CO-236+N20 — NCCI PTP edits. 97760:GO (line 1) is the Column One code and was paid. The chart note documents separate sessions and distinct body regions, but the bypass modifier decision turns on the CCMI for the 97110/97760 pair in the Q1 2024 PTP edit file. The 835 carries neither the partner code nor the CCMI; per reference 07 I cannot guess it.
- transcript: `final-sonnet-4-6-low-edi/transcripts/MOH2-000445.json`

#### `MOH2-000539` — `awaiting_human`

- **expected** `mue_exceeded` / `correct_and_resubmit`
- **said** parked: awaiting_human
- **its explanation** What is the MAI (Medically Unlikely Edit Adjudication Indicator) for CPT 97140 in the CMS MUE table effective for DOS 2026-06-24 (Q2 2026)?
- **rationale** Line 1 (97140 × 9 units) denied CO-151 + N362 — MUE exceeded. Lines 2–4 (97110) adjudicated normally with CO-45 write-off and PR-2 coinsurance. Chart note documents only 15 min (1 unit) of 97140, so units are wrong regardless. But the correction vehicle on Medicare Part B depends on the MAI for 97140: MAI 1/2 → correct-and-resubmit (clerical reopening); MAI 3 → appeal with records. MAI is not in any artifact or reference file.
- transcript: `final-sonnet-4-6-low-edi/transcripts/MOH2-000539.json`

#### `MOH2-000575` — `awaiting_human`

- **expected** `ncci_ptp_no59` / `correct_and_resubmit`
- **said** parked: awaiting_human
- **its explanation** What is the CCMI (Correct Coding Modifier Indicator) for CPT pair 97150 (Column 1) / 97530 (Column 2) in the CMS NCCI PTP edit file effective Q3 2026 (DOS 2026-07-23)?
- **rationale** Line 0 (97530:GP) denied CO-236+N20 — confirmed NCCI PTP edit. 97150 is Column One (paid); 97530 is Column Two (denied). Chart note documents separate service, separate start/stop, different body region. Next action depends entirely on CCMI for this pair in the Q3 2026 PTP edit file — cannot determine from the 835. Line 1 (97150) paid correctly; CO-45 write-off + PR-2 coinsurance routine.
- transcript: `final-sonnet-4-6-low-edi/transcripts/MOH2-000575.json`

#### `MOH2-000608` — `awaiting_human`

- **expected** `ncci_ptp_no59` / `correct_and_resubmit`
- **said** parked: awaiting_human
- **its explanation** What is the CCMI (Column Condition Modifier Indicator) for the 97110 / 97150 pair in the CMS NCCI PTP edit file effective for Q2 2026 (DOS 2026-06-28)?
- **rationale** Line 0 (97110) was denied CO-236 + N20 — a PTP edit. 97150 (line 1) paid normally. The CCMI for the 97110/97150 pair in the Q2 2026 NCCI edit file is not in the artifacts or reference library. CCMI determines the entire disposition: CCMI=1 allows a modifier fix; CCMI=0 requires write-off. Cannot proceed without it.
- transcript: `final-sonnet-4-6-low-edi/transcripts/MOH2-000608.json`

#### `MOH2-000649` — `awaiting_human`

- **expected** `ncci_ptp_no59` / `correct_and_resubmit`
- **said** parked: awaiting_human
- **its explanation** What is the CCMI (modifier indicator) for the CPT pair 97150 (Column One) / 97110 (Column Two) in the Q2 2026 CMS NCCI PTP edit table?
- **rationale** Line 3 (97110:GP, $41.35) was denied CO-236 + N20 — NCCI PTP edit. The chart note documents distinct services, but the 835 carries neither the partner code nor the CCMI. Per ref 07-ncci-and-mue.md, the CCMI must be looked up in the DOS-quarter PTP edit file before routing: CCMI=1 allows a modifier bypass (correct_and_resubmit with 59); CCMI=0 requires write-off.
- transcript: `final-sonnet-4-6-low-edi/transcripts/MOH2-000649.json`

#### `MOH2-000681` — `awaiting_human`

- **expected** `ncci_ptp_no59` / `correct_and_resubmit`
- **said** parked: awaiting_human
- **its explanation** What is the Column-Modifier-Indicator (CCMI) for the 97150 (Column One) / 97110 (Column Two) pair in the CMS NCCI PTP edit table effective for Q2 2026 (DOS 2026-06-14)?
- **rationale** Line 2 (97110:GP) is denied CO-236 + N20 — an NCCI PTP edit. The chart note documents a distinct, demarcated service on a different body region, supporting a modifier bypass — but disposition (correct_and_resubmit vs. do_not_resubmit vs. appeal) turns entirely on the CCMI for the 97150/97110 pair in the Q2 2026 PTP edit table, which no artifact carries. Reference 07 requires a lookup; guessing is prohibited.
- transcript: `final-sonnet-4-6-low-edi/transcripts/MOH2-000681.json`

#### `MOH2-000682` — `awaiting_human`

- **expected** `ncci_ptp_no59` / `correct_and_resubmit`
- **said** parked: awaiting_human
- **its explanation** What is the CCMI (Column-to-Column Modifier Indicator) for the 97110 PTP pair — 97110 vs 97112 and/or 97110 vs 97150 — in the CMS NCCI PTP edit file effective Q3 2026 (July 1, 2026)?
- **rationale** Lines 0 and 2 paid normally (CO-45 write-off + PR-2 coinsurance). Line 1 (97110) is denied CO-236 + N20 — NCCI PTP edit. 97110 has no bypass modifier; 97112 on line 0 already carries 59. The chart note documents a separate session for 97110. Whether a modifier can be appended turns entirely on the CCMI for the 97110 pair in the Q3 2026 PTP edit file — CCMI=1 → correct_and_resubmit (reopening + modifier); CCMI=0 → do_not_resubmit. The 835 carries neither the partner code nor the CCMI.
- transcript: `final-sonnet-4-6-low-edi/transcripts/MOH2-000682.json`

## `final-sonnet-4-6-low-md-dev25`

us.anthropic.claude-sonnet-4-6 · effort `low` · format `md` · 25 predictions against 25 labeled cases

| joint | root cause | next action |
|---:|---:|---:|
| **80.0%** | 92.0% | 80.0% |

### Why the wrong ones were wrong

| reason | n |
|---|---:|
| `wrong_next_action` | 3 |
| `awaiting_human` | 2 |

### Families that lost cases

| family | correct | total | accuracy |
|---|---:|---:|---:|
| `ncci_ptp_no59` | 0 | 2 | 0% |
| `cob_other_primary` | 1 | 3 | 33% |
| `exact_duplicate` | 2 | 3 | 67% |

### The 5 cases that answered and got it wrong

#### `MOH2-000061` — `wrong_next_action`

- **expected** `exact_duplicate` / `do_not_resubmit`
- **said** exact_duplicate / correct_and_resubmit
- **its explanation** Lines 3 and 4 repeat the same HCPCS/modifier combination as lines 1 and 2 on the same DOS without modifier 76 distinguishing them as repeat procedures. Payer matched provider/member/DOS/procedure and denied all four.
- **evidence it cited**
  - `remit_835.edi` All four lines denied OA-18; CLP07 = 2623576767957 confirms adjudication; MOA N111.
  - `claim_837p.edi` Lines 1 and 3 both 97140-GP-KX; lines 2 and 4 both 97110-GP-KX; same DOS 2026-07-05; no modifier 76.
  - `chart_note.txt` Two distinct 97140 timed blocks (15 min, 14 min) and two distinct 97110 blocks (31 min, 16 min) documented.
  - `reference` False duplicate → correct_and_resubmit corrected lines only; Part B: clerical-error reopening; modifier 76 is reopening-eligible.
- **rationale** All four lines carry OA-18. The claim was adjudicated (CLP07 = 2623576767957). Lines 1 and 3 are both 97140-GP-KX; lines 2 and 4 are both 97110-GP-KX on the same DOS with no distinguishing modifier. Chart note confirms two distinct timed blocks for each code. This is a false duplicate; the fix is a MAC clerical-error reopening to add modifier 76 to lines 3 and 4. Frequency 7 not accepted on Part B.
- transcript: `final-sonnet-4-6-low-md-dev25/transcripts/MOH2-000061.json`

#### `MOH2-000075` — `awaiting_human`

- **expected** `ncci_ptp_no59` / `correct_and_resubmit`
- **said** parked: awaiting_human
- **its explanation** What is the CCMI (Column 2/Column 1 Modifier Indicator) for the 97140/97150 pair in the CMS NCCI PTP edit table effective Q3 2026 (July 1, 2026)?
- **rationale** Line 1 (97140-GP-KX) denied CO-236 + N20 — NCCI PTP bundling against 97150. The chart note documents a separate session and distinct body region, which could support a bypass modifier if CCMI = 1. But the 835 carries neither the Column One partner code nor the CCMI indicator. Per reference 07-ncci-and-mue.md, the CCMI must be looked up in the PTP edit file for the DOS quarter before any action can be determined; guessing is prohibited.
- transcript: `final-sonnet-4-6-low-md-dev25/transcripts/MOH2-000075.json`

#### `MOH2-000079` — `wrong_next_action`

- **expected** `cob_other_primary` / `resubmit_other_payer`
- **said** cob_other_primary / correct_and_resubmit
- **its explanation** 835 carries CO-22 on both lines and claim-level MA04. 271 shows EB*R for Novitas Solutions Medicare Part B FFS on the DOS. Claim was submitted SBR responsibility P (primary) without Medicare adjudication data; Liberty Bell cannot process as secondary.
- **evidence it cited**
  - `remit_835.edi` CO-22 on lines 1 and 2; claim-level MOA MA04 ('secondary payment cannot be considered without primary payer identity')
  - `eligibility_271.edi` EB*R benefit for NOVITAS SOLUTIONS MEDICARE PART B FFS on plan date 2026-07-02 — another active payer on record
  - `claim_837p.edi` SBR payer responsibility P (primary) — claim billed to Liberty Bell as primary with no primary adjudication data attached
  - `reference` MA04: correct_and_resubmit to the same payer; populate primary SBR/AMT/CAS. Never resubmit_other_payer or appeal.
- **rationale** 271 confirms `EB*R` for Novitas Solutions Medicare Part B FFS — a second active payer. Liberty Bell fired CO-22 at both lines and MA04 at claim level. MA04 controls: this is a completeness defect (missing primary adjudication data), not a routing error. Per reference 06, MA04 = correct_and_resubmit to the same payer with the primary's SBR/AMT/CAS populated. File Medicare (Novitas) first; once that remit arrives, rebill Liberty Bell as secondary.
- transcript: `final-sonnet-4-6-low-md-dev25/transcripts/MOH2-000079.json`

#### `MOH2-000233` — `awaiting_human`

- **expected** `ncci_ptp_no59` / `correct_and_resubmit`
- **said** parked: awaiting_human
- **its explanation** What is the Column Modifier Indicator (CCMI) for the 97110/97150 PTP edit pair in the Q2 2026 (April 1, 2026) CMS NCCI table?
- **rationale** Lines 1–3 (97110-GP) denied CO-236/N20: NCCI PTP bundling with 97150-GP (paid, Column One). Chart note documents a distinct, demarcated session on a different body region for an unrelated goal — potential bypass. But the 835 carries neither the partner code nor the CCMI, and reference 07 requires the PTP edit file lookup before routing. CCMI=1 → correct-and-resubmit with modifier; CCMI=0 → write off. Cannot determine action without it.
- transcript: `final-sonnet-4-6-low-md-dev25/transcripts/MOH2-000233.json`

#### `MOH2-000490` — `wrong_next_action`

- **expected** `cob_other_primary` / `resubmit_other_payer`
- **said** cob_other_primary / appeal
- **its explanation** Liberty Bell denied CO-22 (another payer primary) with MOA MA04 (no primary payer identity), but their own 271 response for DOS 2026-01-29 states 'PLAN IS PRIMARY PAYER FOR THIS MEMBER' with active EB*1 coverage.
- **evidence it cited**
  - `remit_835.edi` All three service lines denied CO-22 ($173.49 total); claim-level MOA MA04 — Liberty Bell treating itself as secondary.
  - `eligibility_271.edi` EB*1 active coverage for Liberty Bell PPO on DOS 2026-01-29; payer message: 'PLAN IS PRIMARY PAYER FOR THIS MEMBER'.
  - `eligibility_271.edi` EB*R identifies Novitas Solutions Medicare Part B as other/additional payer — confirms Medicare exists but does not establish it as primary.
  - `reference` Per 06-cob-other-primary.md: when payer's own eligibility record contradicts the CO-22 denial, action is appeal citing the 271 exchange reference and date.
- **rationale** Liberty Bell denied all three lines CO-22 + MOA MA04, asserting another payer is primary. But Liberty Bell's own 271 response for the DOS (2026-01-29) carries EB*1 (active coverage) with the explicit payer message "PLAN IS PRIMARY PAYER FOR THIS MEMBER." The payer's records contradict the denial. Appeal with the 271 as the controlling evidence; do not bill Medicare first.
- transcript: `final-sonnet-4-6-low-md-dev25/transcripts/MOH2-000490.json`

## `final-opus-4-6-low-edi`

us.anthropic.claude-opus-4-6-v1 · effort `low` · format `edi` · 37 predictions against 140 labeled cases

| joint | root cause | next action |
|---:|---:|---:|
| **22.1%** | 25.0% | 22.1% |

### Why the wrong ones were wrong

| reason | n |
|---|---:|
| `missing_prediction` | 103 |
| `wrong_next_action` | 4 |
| `awaiting_human` | 2 |

### Families that lost cases

| family | correct | total | accuracy |
|---|---:|---:|---:|
| `ncci_ptp_no59` | 0 | 14 | 0% |
| `threshold_no_kx` | 0 | 14 | 0% |
| `none` | 2 | 20 | 10% |
| `missing_referring_provider` | 2 | 13 | 15% |
| `exact_duplicate` | 3 | 13 | 23% |
| `mue_exceeded` | 3 | 13 | 23% |
| `timely_filing` | 5 | 14 | 36% |
| `eligibility_terminated` | 5 | 13 | 38% |
| `missing_therapy_modifier` | 5 | 13 | 38% |
| `cob_other_primary` | 6 | 13 | 46% |

### 103 cases produced no prediction

These are not wrong answers. The run did not reach them, or the call failed after its retries. They count as wrong in the strict score above -- a missing answer is a missing answer -- but there is nothing to diagnose, because nothing was written.

`MOH2-000148`, `MOH2-000153`, `MOH2-000163`, `MOH2-000165`, `MOH2-000166`, `MOH2-000169`, `MOH2-000171`, `MOH2-000187`, `MOH2-000188`, `MOH2-000202`, `MOH2-000210`, `MOH2-000219`, `MOH2-000220`, `MOH2-000222`, `MOH2-000232`, `MOH2-000233`, `MOH2-000241`, `MOH2-000244`, `MOH2-000250`, `MOH2-000251`, `MOH2-000263`, `MOH2-000267`, `MOH2-000281`, `MOH2-000291`, `MOH2-000293`, `MOH2-000296`, `MOH2-000300`, `MOH2-000308`, `MOH2-000309`, `MOH2-000317`, `MOH2-000326`, `MOH2-000327`, `MOH2-000334`, `MOH2-000335`, `MOH2-000338`, `MOH2-000345`, `MOH2-000348`, `MOH2-000350`, `MOH2-000364`, `MOH2-000369` … and 63 more

### The 6 cases that answered and got it wrong

#### `MOH2-000075` — `awaiting_human`

- **expected** `ncci_ptp_no59` / `correct_and_resubmit`
- **said** parked: awaiting_human
- **its explanation** What is the CCMI (Column One/Column Two Correct Coding Indicator) for the 97150–97140 pair in the CMS NCCI PTP edit file for Q3 2026 (effective 2026-07-01)? It will be 0, 1, or 9.
- **rationale** Line 1 (97140) denied CO-236 = NCCI PTP edit, with 97150 as the Column One code (paid). The 835 carries neither the partner code nor the Column One/Column Two Indicator (CCMI). Per ncci-ptp-carc-236.md §5/§8, the CCMI for the 97150–97140 pair in the Q3 2026 PTP edit file determines whether a modifier bypass is permitted (CCMI=1) or the denial stands (CCMI=0). Cannot resolve without it.
- transcript: `final-opus-4-6-low-edi/transcripts/MOH2-000075.json`

#### `MOH2-000078` — `wrong_next_action`

- **expected** `cob_other_primary` / `resubmit_other_payer`
- **said** cob_other_primary / correct_and_resubmit
- **its explanation** Liberty Bell denied CO-22 + MA04 asserting another payer is primary, but their own 271 for the DOS shows EB*1 active and MSG 'PLAN IS PRIMARY PAYER FOR THIS MEMBER.' COB record in claims system contradicts eligibility system.
- **evidence it cited**
  - `remit_835.edi` All three lines denied CO-22 $0 paid; MOA*MA04 at claim level
  - `eligibility_271.edi` EB*1*IND*30 active coverage with Liberty Bell; MSG 'PLAN IS PRIMARY PAYER FOR THIS MEMBER'
  - `eligibility_271.edi` EB*R names Novitas Medicare Part B FFS as other payer, effective 2024-01-01
  - `claim_837p.edi` Claim billed with SBR*P (primary) to Liberty Bell, filing indicator CI
- **rationale** 835 shows CO-22 on all lines with MOA MA04. Per reference 06, MA04 is a completeness defect requiring resubmission to the same payer with primary adjudication data. However, the 271 from this same payer (Liberty Bell) shows EB*1 active coverage and MSG "PLAN IS PRIMARY PAYER FOR THIS MEMBER" — their eligibility system confirms they are primary, contradicting the CO-22 denial. The payer's COB record in claims adjudication is inconsistent with their own eligibility response. Remedy: correct the COB record with the payer, then resubmit.
- transcript: `final-opus-4-6-low-edi/transcripts/MOH2-000078.json`

#### `MOH2-000081` — `wrong_next_action`

- **expected** `ncci_ptp_no59` / `correct_and_resubmit`
- **said** ncci_ptp_no59 / appeal
- **its explanation** 97750 denied CO-97 (bundled into another service) with N20. Payer applied bundling edit against 97140. Chart documents separate session with distinct region and goal.
- **evidence it cited**
  - `remit_835.edi` Line 1 (97750:GP) paid $0, CAS*CO*97*46.30, remark N20 — bundled into another service
  - `chart_note.txt` Separate-session log: 97750 performed apart from 97140 with its own timed interval, distinct target region, and its own documented goal
  - `claim_837p.edi` Claim billed to commercial payer (SBR*P*18*******CI) — Liberty Bell Health Plans
  - `remit_835.edi` Lines 2-4 (97140:GP) paid with CO-45 contractual and PR-2 coinsurance — not denied
- **rationale** Line 1 (97750:GP) denied CO-97 + N20 — payer bundled it into 97140. Chart note documents 97750 performed in a separate timed interval with distinct target region and documented goal. Claim was billed correctly; the bundling determination is wrong. Commercial payer (CI), so appeal with clinical documentation of the separate session.
- transcript: `final-opus-4-6-low-edi/transcripts/MOH2-000081.json`

#### `MOH2-000094` — `awaiting_human`

- **expected** `ncci_ptp_no59` / `correct_and_resubmit`
- **said** parked: awaiting_human
- **its explanation** What is the Column One/Column Two Correct Coding Modifier Indicator (CCMI) for the 97150–97110 pair in the CMS NCCI PTP edit file for Q2 2026 (April–June)? Is it 0, 1, or 9?
- **rationale** Line 1 (97110:GP:KX) denied CO-236 + N20 = NCCI PTP edit. Column One (97150, paid) bundled Column Two (97110, denied). Chart note documents separate encounters/body regions supporting a modifier bypass, but the 835 carries neither the CCMI nor confirms the edit pair in the DOS-quarter PTP file. Reference 07 explicitly requires looking up the CCMI before routing — CCMI 1 allows correct_and_resubmit, CCMI 0 means do_not_resubmit. Cannot guess.
- transcript: `final-opus-4-6-low-edi/transcripts/MOH2-000094.json`

#### `MOH2-000140` — `wrong_next_action`

- **expected** `cob_other_primary` / `resubmit_other_payer`
- **said** cob_other_primary / correct_and_resubmit
- **its explanation** Claim billed to Liberty Bell as primary but Medicare Part B (Novitas) is the primary payer per the 271. CO-22 + MA04: primary adjudication data missing from the secondary claim.
- **evidence it cited**
  - `remit_835.edi` All three lines denied CAS*CO*22 with MOA MA04; CLP07=2605114385066
  - `eligibility_271.edi` EB*R*IND*30**NOVITAS SOLUTIONS MEDICARE PART B FFS with MSG 'PLAN IS PRIMARY PAYER FOR THIS MEMBER'
  - `claim_837p.edi` SBR*P*18*******CI — billed Liberty Bell as primary, commercial filing indicator
  - `reference` MA04 = correct_and_resubmit to same payer with primary's SBR/AMT/CAS; never resubmit_other_payer
- **rationale** 835 shows all lines denied CO-22 with MOA MA04. 271 confirms EB*R naming "NOVITAS SOLUTIONS MEDICARE PART B FFS" as primary payer for this member on the DOS. Claim was billed to Liberty Bell as primary (SBR*P, CI) without Medicare's adjudication data. MA04 = completeness defect: primary payer data missing. Per reference, correct_and_resubmit to same payer with primary's payment data; never resubmit_other_payer for MA04.
- transcript: `final-opus-4-6-low-edi/transcripts/MOH2-000140.json`

#### `MOH2-000162` — `wrong_next_action`

- **expected** `none` / `none`
- **said** none / bill_patient
- **its explanation** Claim paid correctly. CO-45 is the contractual write-off to the Medicare fee schedule; PR-2 is standard 20% coinsurance. No lines denied.
- **evidence it cited**
  - `remit_835.edi` CLP status code 1 (processed as primary), paid $145.09 of $293.81 billed
  - `remit_835.edi` All four lines carry CO-45 (fee schedule reduction) and PR-2 (coinsurance) — no denial CARCs
  - `remit_835.edi` PR-2 amounts total $36.27 matching CLP patient responsibility field
- **rationale** All four lines paid. CLP*PA25592574*1 = status "1" (processed as primary). Adjustments are CO-45 (contractual write-down to fee schedule) and PR-2 (20% coinsurance). No denial exists; this is routine Medicare adjudication with allowed amounts, contractual adjustments, and standard patient cost-sharing.
- transcript: `final-opus-4-6-low-edi/transcripts/MOH2-000162.json`

## Cases wrong in more than one run

A case that fails in every format is a reference or reasoning gap. A case that fails in only one is a rendering or parsing gap. Only the first kind is listed here.

- `MOH2-000061`
- `MOH2-000075`
- `MOH2-000094`
- `MOH2-000148`
- `MOH2-000233`
- `MOH2-000251`
- `MOH2-000291`
- `MOH2-000309`
- `MOH2-000326`
- `MOH2-000445`
- `MOH2-000490`
- `MOH2-000539`
- `MOH2-000575`
- `MOH2-000608`
- `MOH2-000649`
- `MOH2-000681`
- `MOH2-000682`
