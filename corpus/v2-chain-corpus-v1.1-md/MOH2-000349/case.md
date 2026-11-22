# Case MOH2-000349

Patient THOMAS CLARK, DOB 1941-03-27, sex M, member ID 5JY1CU1XQ76. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-01-25.

## Adjudication outcome (835)
Claim PA22167290: status 4 (denied). Billed $181.39, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2610265742779, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-04-12.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT398250943, originator 1184634935.
claim statement period start (232): 2026-01-25.
Outpatient adjudication remarks (MOA): N111 (no appeal right except duplicate claim/service issue).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 | $81.44 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $81.44 |  |
| 2 | 97140-GP | 1 | $44.01 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $44.01 |  |
| 3 | 97530-GP | 1 | $55.94 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $55.94 |  |

Line item control numbers (REF 6R): PA22167290L1, PA22167290L2, PA22167290L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: THOMAS CLARK; MI (member ID) 5JY1CU1XQ76; rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737.

## Claim as billed (837P)
Claim PA22167290, total charge $181.39, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 UN | $81.44 | 2026-01-25 | 1 | PA22167290L1 |
| 2 | 97140-GP | 1 UN | $44.01 | 2026-01-25 | 1 | PA22167290L2 |
| 3 | 97530-GP | 1 UN | $55.94 | 2026-01-25 | 1 | PA22167290L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: THOMAS CLARK; MI (member ID) 5JY1CU1XQ76; 5403 LINCOLN ST; WILMINGTON, DE, 19806
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: MARCUS WEBB; XX (NPI) 1583494452
- rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737
- Submission reference TRC31377608, dated 2026-03-15 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-01-25.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: THOMAS CLARK; MI (member ID) 5JY1CU1XQ76.
Subject DOB 1941-03-27, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-01-25
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: THOMAS CLARK; MI (member ID) 5JY1CU1XQ76.
Subject DOB 1941-03-27, sex M.
Eligibility exchange reference ELG27418873, dated 2026-04-16 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-03-16, action code WQ, amount $181.39.
D9 (clearinghouse claim number): TRC31377608.
Trace (2 (referenced transaction trace)): TRC31377608.
received date (050): 2026-03-16.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: THOMAS CLARK; MI (member ID) 5JY1CU1XQ76.
Acknowledgment reference ACK31377608, dated 2026-03-16 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-01-25. Dx: Aftercare following joint replacement surgery. 97110 (30 min): therapeutic exercise for strength and ROM. 97140 (15 min): manual therapy (soft tissue and joint mobilization). 97530 (15 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 60. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1846349352, interchange 149066160 date 260416 time 0800 version 00501 usage P; group HS control 149066160 date 20260416 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 568456708 date 260416 time 0800 version 00501 usage P; group HB control 568456708 date 20260416 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1846349352, interchange 894710435 date 260315 time 0800 version 00501 usage P; group HC control 894710435 date 20260315 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 163533216 date 260316 time 0800 version 00501 usage P; group HN control 163533216 date 20260316 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 398250943 date 260412 time 0800 version 00501 usage P; group HP control 398250943 date 20260412 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
