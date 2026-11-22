# Case MOH2-000558

Patient THOMAS CLARK, DOB 1941-03-27, sex M, member ID 5JY1CU1XQ76. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-07-19.

## Adjudication outcome (835)
Claim PA27576028: status 4 (denied). Billed $139.25, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2623737310079, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-08-25.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT155286470, originator 1184634935.
claim statement period start (232): 2026-07-19.
Outpatient adjudication remarks (MOA): N286 (missing/incomplete/invalid referring provider primary identifier).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97112-GP-KX | 1 | $48.57 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $48.57 |  |
| 2 | 97140-GP-KX | 1 | $46.27 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $46.27 |  |
| 3 | 97140-GP-KX | 1 | $44.41 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $44.41 |  |

Line item control numbers (REF 6R): PA27576028L1, PA27576028L2, PA27576028L3.
Modifiers on remit lines: GP (under PT plan of care), KX.
Remit claim parties: patient [QC]: THOMAS CLARK; MI (member ID) 5JY1CU1XQ76; rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737.

## Claim as billed (837P)
Claim PA27576028, total charge $139.25, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97112-GP-KX | 1 UN | $48.57 | 2026-07-19 | 1 | PA27576028L1 |
| 2 | 97140-GP-KX | 1 UN | $46.27 | 2026-07-19 | 1 | PA27576028L2 |
| 3 | 97140-GP-KX | 1 UN | $44.41 | 2026-07-19 | 1 | PA27576028L3 |

Modifiers on claim: GP (under PT plan of care), KX.

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: THOMAS CLARK; MI (member ID) 5JY1CU1XQ76; 5403 LINCOLN ST; WILMINGTON, DE, 19806
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737
- Submission reference TRC83693286, dated 2026-08-06 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-07-19.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: THOMAS CLARK; MI (member ID) 5JY1CU1XQ76.
Subject DOB 1941-03-27, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-07-19
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: THOMAS CLARK; MI (member ID) 5JY1CU1XQ76.
Subject DOB 1941-03-27, sex M.
Eligibility exchange reference ELG98301934, dated 2026-08-26 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-08-08, action code WQ, amount $139.25.
D9 (clearinghouse claim number): TRC83693286.
Trace (2 (referenced transaction trace)): TRC83693286.
received date (050): 2026-08-08.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: THOMAS CLARK; MI (member ID) 5JY1CU1XQ76.
Acknowledgment reference ACK83693286, dated 2026-08-08 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-07-19. Dx: Aftercare following joint replacement surgery. 97112 (15 min): neuromuscular re-education of movement and balance. 97140 (14 min): manual therapy (soft tissue and joint mobilization). 97140 (14 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 43. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1846349352, interchange 831726181 date 260826 time 0800 version 00501 usage P; group HS control 831726181 date 20260826 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 393379775 date 260826 time 0800 version 00501 usage P; group HB control 393379775 date 20260826 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1846349352, interchange 949755858 date 260806 time 0800 version 00501 usage P; group HC control 949755858 date 20260806 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 33
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 338509976 date 260808 time 0800 version 00501 usage P; group HN control 338509976 date 20260808 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 155286470 date 260825 time 0800 version 00501 usage P; group HP control 155286470 date 20260825 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
