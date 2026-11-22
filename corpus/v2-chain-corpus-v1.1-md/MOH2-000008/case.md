# Case MOH2-000008

Patient JESSICA GARCIA, DOB 1983-02-05, sex F, member ID YAW396438474. Payer: ATLANTIC SHORE ASSURANCE. Service date 2026-05-24.

## Adjudication outcome (835)
Claim PA27416586: status 1 (processed as primary, paid). Billed $125.09, paid $67.61, patient responsibility $16.89. Filing indicator CI (commercial insurance). Payer claim control 2617804169015, POS 11 (office), frequency 1 (original claim).
Payment: $67.61 by CHK (check), handling I.
production date (405): 2026-06-27.
Payer [PR]: ATLANTIC SHORE ASSURANCE; 3499 ROUTE 9 N; FREEHOLD, NJ, 077283100; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT696018726, originator 1125037465.
claim statement period start (232): 2026-05-24.
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $39.48 | $23.25 allowed (B6) $29.06 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $10.42; PR-2 (Patient Responsibility: coinsurance amount) $5.81 |  |
| 2 | 97140-GP | 1 | $44.08 | $22.18 allowed (B6) $27.72 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $16.36; PR-2 (Patient Responsibility: coinsurance amount) $5.54 |  |
| 3 | 97140-GP | 1 | $41.53 | $22.18 allowed (B6) $27.72 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $13.81; PR-2 (Patient Responsibility: coinsurance amount) $5.54 |  |

Line item control numbers (REF 6R): PA27416586L1, PA27416586L2, PA27416586L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: JESSICA GARCIA; MI (member ID) YAW396438474; rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737.

## Claim as billed (837P)
Claim PA27416586, total charge $125.09, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $39.48 | 2026-05-24 | 1 | PA27416586L1 |
| 2 | 97140-GP | 1 UN | $44.08 | 2026-05-24 | 1 | PA27416586L2 |
| 3 | 97140-GP | 1 UN | $41.53 | 2026-05-24 | 1 | PA27416586L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: ATLANTIC SHORE ASSURANCE; 46 (ETIN) 1250374659
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: JESSICA GARCIA; MI (member ID) YAW396438474; 6598 FRANKLIN ST; STATEN ISLAND, NY, 10356
- payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659
- referring provider [DN]: FATIMA AL-RASHID; XX (NPI) 1333183066
- rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737
- Submission reference TRC77327725, dated 2026-06-03 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-05-24.
Inquiry parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: JESSICA GARCIA; MI (member ID) YAW396438474.
Subject DOB 1983-02-05, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: ATLANTIC SHORE ASSURANCE EPO
- plan date (291): 2026-05-24
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: JESSICA GARCIA; MI (member ID) YAW396438474.
Subject DOB 1983-02-05, sex F.
Eligibility exchange reference ELG99009621, dated 2026-07-01 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-06-03, action code WQ, amount $125.09.
D9 (clearinghouse claim number): TRC77327725.
Trace (2 (referenced transaction trace)): TRC77327725.
received date (050): 2026-06-03.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: JESSICA GARCIA; MI (member ID) YAW396438474.
Acknowledgment reference ACK77327725, dated 2026-06-03 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-05-24. Dx: Aftercare following joint replacement surgery. 97110 (15 min): therapeutic exercise for strength and ROM. 97140 (16 min): manual therapy (soft tissue and joint mobilization). 97140 (16 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 47. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1250374659, interchange 835624461 date 260701 time 0800 version 00501 usage P; group HS control 835624461 date 20260701 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1250374659 to receiver [ZZ] 1601336180, interchange 908317951 date 260701 time 0800 version 00501 usage P; group HB control 908317951 date 20260701 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1250374659, interchange 957460182 date 260603 time 0800 version 00501 usage P; group HC control 957460182 date 20260603 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 129731904 date 260603 time 0800 version 00501 usage P; group HN control 129731904 date 20260603 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1250374659 to receiver [ZZ] 1601336180, interchange 696018726 date 260627 time 0800 version 00501 usage P; group HP control 696018726 date 20260627 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 36
