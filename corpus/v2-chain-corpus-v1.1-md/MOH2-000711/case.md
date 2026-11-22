# Case MOH2-000711

Patient THOMAS CLARK, DOB 1941-03-27, sex M, member ID 5JY1CU1XQ76. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-07-08.

## Adjudication outcome (835)
Claim PA22388223: status 4 (denied). Billed $147.16, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2622720095805, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-08-15.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT684824565, originator 1184634935.
claim statement period start (232): 2026-07-08.
Outpatient adjudication remarks (MOA): N435 (exceeds number/frequency approved or allowed within time period).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97140-GP | 1 | $48.39 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $48.39 |  |
| 2 | 97530-GP | 1 | $56.18 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $56.18 |  |
| 3 | 97110-GP | 1 | $42.59 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $42.59 |  |

Line item control numbers (REF 6R): PA22388223L1, PA22388223L2, PA22388223L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: THOMAS CLARK; MI (member ID) 5JY1CU1XQ76; rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737.

## Claim as billed (837P)
Claim PA22388223, total charge $147.16, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97140-GP | 1 UN | $48.39 | 2026-07-08 | 1 | PA22388223L1 |
| 2 | 97530-GP | 1 UN | $56.18 | 2026-07-08 | 1 | PA22388223L2 |
| 3 | 97110-GP | 1 UN | $42.59 | 2026-07-08 | 1 | PA22388223L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: THOMAS CLARK; MI (member ID) 5JY1CU1XQ76; 5403 LINCOLN ST; WILMINGTON, DE, 19806
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: MARCUS WEBB; XX (NPI) 1583494452
- rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737
- Submission reference TRC88951518, dated 2026-07-18 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-07-08.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: THOMAS CLARK; MI (member ID) 5JY1CU1XQ76.
Subject DOB 1941-03-27, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-07-08
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: THOMAS CLARK; MI (member ID) 5JY1CU1XQ76.
Subject DOB 1941-03-27, sex M.
Eligibility exchange reference ELG12699351, dated 2026-08-17 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-07-18, action code WQ, amount $147.16.
D9 (clearinghouse claim number): TRC88951518.
Trace (2 (referenced transaction trace)): TRC88951518.
received date (050): 2026-07-18.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: THOMAS CLARK; MI (member ID) 5JY1CU1XQ76.
Acknowledgment reference ACK88951518, dated 2026-07-18 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-07-08. Dx: Aftercare following joint replacement surgery. 97140 (16 min): manual therapy (soft tissue and joint mobilization). 97530 (14 min): therapeutic activities (dynamic functional tasks). 97110 (15 min): therapeutic exercise for strength and ROM. Total timed minutes: 45. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1846349352, interchange 583757940 date 260817 time 0800 version 00501 usage P; group HS control 583757940 date 20260817 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 175624638 date 260817 time 0800 version 00501 usage P; group HB control 175624638 date 20260817 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1846349352, interchange 114021693 date 260718 time 0800 version 00501 usage P; group HC control 114021693 date 20260718 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 215558968 date 260718 time 0800 version 00501 usage P; group HN control 215558968 date 20260718 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 684824565 date 260815 time 0800 version 00501 usage P; group HP control 684824565 date 20260815 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
