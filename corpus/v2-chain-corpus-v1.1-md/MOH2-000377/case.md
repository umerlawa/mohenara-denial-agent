# Case MOH2-000377

Patient THOMAS CLARK, DOB 1941-03-27, sex M, member ID 5JY1CU1XQ76. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-07-04.

## Adjudication outcome (835)
Claim PA25460031: status 4 (denied). Billed $128.56, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2623452481071, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-08-22.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT555967565, originator 1184634935.
claim statement period start (232): 2026-07-04.
Outpatient adjudication remarks (MOA): N435 (exceeds number/frequency approved or allowed within time period).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $38.96 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $38.96 |  |
| 2 | 97110-GP | 1 | $49.54 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $49.54 |  |
| 3 | 97110-GP | 1 | $40.06 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $40.06 |  |

Line item control numbers (REF 6R): PA25460031L1, PA25460031L2, PA25460031L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: THOMAS CLARK; MI (member ID) 5JY1CU1XQ76; rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737.

## Claim as billed (837P)
Claim PA25460031, total charge $128.56, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $38.96 | 2026-07-04 | 1 | PA25460031L1 |
| 2 | 97110-GP | 1 UN | $49.54 | 2026-07-04 | 1 | PA25460031L2 |
| 3 | 97110-GP | 1 UN | $40.06 | 2026-07-04 | 1 | PA25460031L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: THOMAS CLARK; MI (member ID) 5JY1CU1XQ76; 5403 LINCOLN ST; WILMINGTON, DE, 19806
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: MARCUS WEBB; XX (NPI) 1583494452
- rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737
- Submission reference TRC18968732, dated 2026-07-23 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-07-04.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: THOMAS CLARK; MI (member ID) 5JY1CU1XQ76.
Subject DOB 1941-03-27, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-07-04
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: THOMAS CLARK; MI (member ID) 5JY1CU1XQ76.
Subject DOB 1941-03-27, sex M.
Eligibility exchange reference ELG30441594, dated 2026-08-24 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-07-24, action code WQ, amount $128.56.
D9 (clearinghouse claim number): TRC18968732.
Trace (2 (referenced transaction trace)): TRC18968732.
received date (050): 2026-07-24.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: THOMAS CLARK; MI (member ID) 5JY1CU1XQ76.
Acknowledgment reference ACK18968732, dated 2026-07-24 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-07-04. Dx: Aftercare following joint replacement surgery. 97110 (14 min): therapeutic exercise for strength and ROM. 97110 (15 min): therapeutic exercise for strength and ROM. 97110 (14 min): therapeutic exercise for strength and ROM. Total timed minutes: 43. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1846349352, interchange 511087197 date 260824 time 0800 version 00501 usage P; group HS control 511087197 date 20260824 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 975944560 date 260824 time 0800 version 00501 usage P; group HB control 975944560 date 20260824 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1846349352, interchange 981973024 date 260723 time 0800 version 00501 usage P; group HC control 981973024 date 20260723 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 571637057 date 260724 time 0800 version 00501 usage P; group HN control 571637057 date 20260724 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 555967565 date 260822 time 0800 version 00501 usage P; group HP control 555967565 date 20260822 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
