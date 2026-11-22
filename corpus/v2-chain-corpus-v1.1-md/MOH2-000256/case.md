# Case MOH2-000256

Patient RUTH JACKSON, DOB 1975-12-14, sex M, member ID NLM830365357. Payer: ATLANTIC SHORE ASSURANCE. Service date 2026-01-14.

## Adjudication outcome (835)
Claim PA27247297: status 4 (denied). Billed $95.4, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2605438995746, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-02-23.
Payer [PR]: ATLANTIC SHORE ASSURANCE; 3499 ROUTE 9 N; FREEHOLD, NJ, 077283100; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT996448781, originator 1125037465.
claim statement period start (232): 2026-01-14.
Outpatient adjudication remarks (MOA): M77 (missing/incomplete/invalid place of service).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $39.14 | $0 | CO-5 (Contractual Obligation: procedure code/type of bill is inconsistent with the place of service) $39.14 |  |
| 2 | 97112-GP | 1 | $56.26 | $0 | CO-5 (Contractual Obligation: procedure code/type of bill is inconsistent with the place of service) $56.26 |  |

Line item control numbers (REF 6R): PA27247297L1, PA27247297L2.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: RUTH JACKSON; MI (member ID) NLM830365357; rendering provider [82]: JOSEPH ANDERSON; XX (NPI) 1260849754.

## Claim as billed (837P)
Claim PA27247297, total charge $95.4, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25561 (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $39.14 | 2026-01-14 | 1 | PA27247297L1 |
| 2 | 97112-GP | 1 UN | $56.26 | 2026-01-14 | 1 | PA27247297L2 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: ATLANTIC SHORE ASSURANCE; 46 (ETIN) 1250374659
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: RUTH JACKSON; MI (member ID) NLM830365357; 1299 WILLOW RD; STATEN ISLAND, NY, 10350
- payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659
- referring provider [DN]: AISHA RAHMAN; XX (NPI) 1538183382
- rendering provider [82]: JOSEPH ANDERSON; XX (NPI) 1260849754
- Submission reference TRC11289426, dated 2026-01-29 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-01-14.
Inquiry parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: RUTH JACKSON; MI (member ID) NLM830365357.
Subject DOB 1975-12-14, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: ATLANTIC SHORE ASSURANCE PPO
- plan date (291): 2026-01-14
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: RUTH JACKSON; MI (member ID) NLM830365357.
Subject DOB 1975-12-14, sex M.
Eligibility exchange reference ELG45258138, dated 2026-02-24 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-01-30, action code WQ, amount $95.4.
D9 (clearinghouse claim number): TRC11289426.
Trace (2 (referenced transaction trace)): TRC11289426.
received date (050): 2026-01-30.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: RUTH JACKSON; MI (member ID) NLM830365357.
Acknowledgment reference ACK11289426, dated 2026-01-30 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-01-14. Dx: Pain in right knee. 97110 (14 min): therapeutic exercise for strength and ROM. 97112 (15 min): neuromuscular re-education of movement and balance. Total timed minutes: 29. Visit conducted via synchronous audio-video telehealth with the patient at home; consent for telehealth documented. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1250374659, interchange 378755331 date 260224 time 0800 version 00501 usage P; group HS control 378755331 date 20260224 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1250374659 to receiver [ZZ] 1601336180, interchange 153708999 date 260224 time 0800 version 00501 usage P; group HB control 153708999 date 20260224 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1250374659, interchange 678862921 date 260129 time 0800 version 00501 usage P; group HC control 678862921 date 20260129 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 686474020 date 260130 time 0800 version 00501 usage P; group HN control 686474020 date 20260130 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1250374659 to receiver [ZZ] 1601336180, interchange 996448781 date 260223 time 0800 version 00501 usage P; group HP control 996448781 date 20260223 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 27
