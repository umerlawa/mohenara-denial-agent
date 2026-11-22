# Case MOH2-000036

Patient RUTH JACKSON, DOB 1975-12-14, sex M, member ID NLM830365357. Payer: ATLANTIC SHORE ASSURANCE. Service date 2026-10-04.

## Adjudication outcome (835)
Claim PA29437822: status 4 (denied). Billed $137.96, paid $0, patient responsibility $137.96. Filing indicator CI (commercial insurance). Payer claim control 2629823655740, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-10-25.
Payer [PR]: ATLANTIC SHORE ASSURANCE; 3499 ROUTE 9 N; FREEHOLD, NJ, 077283100; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT606727205, originator 1125037465.
claim statement period start (232): 2026-10-04.
Outpatient adjudication remarks (MOA): N30 (patient ineligible for this service).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $44.29 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $44.29 |  |
| 2 | 97140-GP | 1 | $39.15 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $39.15 |  |
| 3 | 97112-GP | 1 | $54.52 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $54.52 |  |

Line item control numbers (REF 6R): PA29437822L1, PA29437822L2, PA29437822L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: RUTH JACKSON; MI (member ID) NLM830365357; rendering provider [82]: JOSEPH ANDERSON; XX (NPI) 1260849754.

## Claim as billed (837P)
Claim PA29437822, total charge $137.96, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25561 (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $44.29 | 2026-10-04 | 1 | PA29437822L1 |
| 2 | 97140-GP | 1 UN | $39.15 | 2026-10-04 | 1 | PA29437822L2 |
| 3 | 97112-GP | 1 UN | $54.52 | 2026-10-04 | 1 | PA29437822L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: ATLANTIC SHORE ASSURANCE; 46 (ETIN) 1250374659
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: RUTH JACKSON; MI (member ID) NLM830365357; 1299 WILLOW RD; STATEN ISLAND, NY, 10350
- payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659
- referring provider [DN]: AISHA RAHMAN; XX (NPI) 1538183382
- rendering provider [82]: JOSEPH ANDERSON; XX (NPI) 1260849754
- Submission reference TRC59685918, dated 2026-10-09 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-10-04.
Inquiry parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: RUTH JACKSON; MI (member ID) NLM830365357.
Subject DOB 1975-12-14, sex M.

Response:
- benefit: 6 (inactive), coverage level IND, service type 30 (health benefit plan coverage), plan: ATLANTIC SHORE ASSURANCE PPO
- plan date (291): 2026-10-04
- eligibility begin (356): 2024-01-01
- eligibility end (357): 2026-09-30
Response parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: RUTH JACKSON; MI (member ID) NLM830365357.
Subject DOB 1975-12-14, sex M.
Eligibility exchange reference ELG86601052, dated 2026-10-28 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-10-09, action code WQ, amount $137.96.
D9 (clearinghouse claim number): TRC59685918.
Trace (2 (referenced transaction trace)): TRC59685918.
received date (050): 2026-10-09.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: RUTH JACKSON; MI (member ID) NLM830365357.
Acknowledgment reference ACK59685918, dated 2026-10-09 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-10-04. Dx: Pain in right knee. 97110 (16 min): therapeutic exercise for strength and ROM. 97140 (16 min): manual therapy (soft tissue and joint mobilization). 97112 (16 min): neuromuscular re-education of movement and balance. Total timed minutes: 48. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1250374659, interchange 813830358 date 261028 time 0800 version 00501 usage P; group HS control 813830358 date 20261028 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1250374659 to receiver [ZZ] 1601336180, interchange 753729011 date 261028 time 0800 version 00501 usage P; group HB control 753729011 date 20261028 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 14
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1250374659, interchange 748240024 date 261009 time 0800 version 00501 usage P; group HC control 748240024 date 20261009 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 183958293 date 261009 time 0800 version 00501 usage P; group HN control 183958293 date 20261009 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1250374659 to receiver [ZZ] 1601336180, interchange 606727205 date 261025 time 0800 version 00501 usage P; group HP control 606727205 date 20261025 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
