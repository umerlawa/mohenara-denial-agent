# Case MOH2-000331

Patient RUTH JACKSON, DOB 1975-12-14, sex M, member ID NLM830365357. Payer: ATLANTIC SHORE ASSURANCE. Service date 2026-10-06.

## Adjudication outcome (835)
Claim PA23846812: status 4 (denied). Billed $121, paid $0, patient responsibility $121. Filing indicator CI (commercial insurance). Payer claim control 2631034290789, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-11-06.
Payer [PR]: ATLANTIC SHORE ASSURANCE; 3499 ROUTE 9 N; FREEHOLD, NJ, 077283100; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT651951455, originator 1125037465.
claim statement period start (232): 2026-10-06.
Outpatient adjudication remarks (MOA): N30 (patient ineligible for this service).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97140-GP | 1 | $41.74 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $41.74 |  |
| 2 | 97140-GP | 2 | $79.26 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $79.26 |  |

Line item control numbers (REF 6R): PA23846812L1, PA23846812L2.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: RUTH JACKSON; MI (member ID) NLM830365357; rendering provider [82]: JOSEPH ANDERSON; XX (NPI) 1260849754.

## Claim as billed (837P)
Claim PA23846812, total charge $121, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25561 (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97140-GP | 1 UN | $41.74 | 2026-10-06 | 1 | PA23846812L1 |
| 2 | 97140-GP | 2 UN | $79.26 | 2026-10-06 | 1 | PA23846812L2 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: ATLANTIC SHORE ASSURANCE; 46 (ETIN) 1250374659
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: RUTH JACKSON; MI (member ID) NLM830365357; 1299 WILLOW RD; STATEN ISLAND, NY, 10350
- payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659
- referring provider [DN]: AISHA RAHMAN; XX (NPI) 1538183382
- rendering provider [82]: JOSEPH ANDERSON; XX (NPI) 1260849754
- Submission reference TRC51020761, dated 2026-10-09 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-10-06.
Inquiry parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: RUTH JACKSON; MI (member ID) NLM830365357.
Subject DOB 1975-12-14, sex M.

Response:
- benefit: 6 (inactive), coverage level IND, service type 30 (health benefit plan coverage), plan: ATLANTIC SHORE ASSURANCE PPO
- plan date (291): 2026-10-06
- eligibility begin (356): 2024-01-01
- eligibility end (357): 2026-09-30
Response parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: RUTH JACKSON; MI (member ID) NLM830365357.
Subject DOB 1975-12-14, sex M.
Eligibility exchange reference ELG97490975, dated 2026-11-10 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-10-10, action code WQ, amount $121.
D9 (clearinghouse claim number): TRC51020761.
Trace (2 (referenced transaction trace)): TRC51020761.
received date (050): 2026-10-10.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: RUTH JACKSON; MI (member ID) NLM830365357.
Acknowledgment reference ACK51020761, dated 2026-10-10 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-10-06. Dx: Pain in right knee. 97140 (16 min): manual therapy (soft tissue and joint mobilization). 97140 (30 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 46. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1250374659, interchange 440392519 date 261110 time 0800 version 00501 usage P; group HS control 440392519 date 20261110 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1250374659 to receiver [ZZ] 1601336180, interchange 242244682 date 261110 time 0800 version 00501 usage P; group HB control 242244682 date 20261110 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 14
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1250374659, interchange 318134987 date 261009 time 0800 version 00501 usage P; group HC control 318134987 date 20261009 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 270073471 date 261010 time 0800 version 00501 usage P; group HN control 270073471 date 20261010 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1250374659 to receiver [ZZ] 1601336180, interchange 651951455 date 261106 time 0800 version 00501 usage P; group HP control 651951455 date 20261106 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 27
