# Case MOH2-000566

Patient ROBERT WILSON, DOB 1979-12-16, sex F, member ID MAP727498881. Payer: ATLANTIC SHORE ASSURANCE. Service date 2025-06-17.

## Adjudication outcome (835)
Claim PA22359018: status 4 (denied). Billed $268.94, paid $0, patient responsibility $268.94. Filing indicator CI (commercial insurance). Payer claim control 2519449475025, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2025-07-13.
Payer [PR]: ATLANTIC SHORE ASSURANCE; 3499 ROUTE 9 N; FREEHOLD, NJ, 077283100; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT768525806, originator 1125037465.
claim statement period start (232): 2025-06-17.
Outpatient adjudication remarks (MOA): N30 (patient ineligible for this service).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 | $98.4 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $98.4 |  |
| 2 | 97110-GP | 2 | $90.16 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $90.16 |  |
| 3 | 97110-GP | 2 | $80.38 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $80.38 |  |

Line item control numbers (REF 6R): PA22359018L1, PA22359018L2, PA22359018L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: ROBERT WILSON; MI (member ID) MAP727498881; rendering provider [82]: WEI LEWIS; XX (NPI) 1986021803.

## Claim as billed (837P)
Claim PA22359018, total charge $268.94, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25511 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 UN | $98.4 | 2025-06-17 | 1 | PA22359018L1 |
| 2 | 97110-GP | 2 UN | $90.16 | 2025-06-17 | 1 | PA22359018L2 |
| 3 | 97110-GP | 2 UN | $80.38 | 2025-06-17 | 1 | PA22359018L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: ATLANTIC SHORE ASSURANCE; 46 (ETIN) 1250374659
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: ROBERT WILSON; MI (member ID) MAP727498881; 8008 CHESTNUT ST; TRENTON, NJ, 08618
- payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659
- referring provider [DN]: SARAH CHEN; XX (NPI) 1410042904
- rendering provider [82]: WEI LEWIS; XX (NPI) 1986021803
- Submission reference TRC41945870, dated 2025-06-26 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2025-06-17.
Inquiry parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: ROBERT WILSON; MI (member ID) MAP727498881.
Subject DOB 1979-12-16, sex F.

Response:
- benefit: 6 (inactive), coverage level IND, service type 30 (health benefit plan coverage), plan: ATLANTIC SHORE ASSURANCE PPO
- plan date (291): 2025-06-17
- eligibility begin (356): 2024-01-01
- eligibility end (357): 2025-05-31
Response parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: ROBERT WILSON; MI (member ID) MAP727498881.
Subject DOB 1979-12-16, sex F.
Eligibility exchange reference ELG18877407, dated 2025-07-16 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2025-06-26, action code WQ, amount $268.94.
D9 (clearinghouse claim number): TRC41945870.
Trace (2 (referenced transaction trace)): TRC41945870.
received date (050): 2025-06-26.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: ROBERT WILSON; MI (member ID) MAP727498881.
Acknowledgment reference ACK41945870, dated 2025-06-26 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2025-06-17. Dx: Pain in right shoulder. 97110 (30 min): therapeutic exercise for strength and ROM. 97110 (30 min): therapeutic exercise for strength and ROM. 97110 (29 min): therapeutic exercise for strength and ROM. Total timed minutes: 89. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1250374659, interchange 884710877 date 250716 time 0800 version 00501 usage P; group HS control 884710877 date 20250716 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1250374659 to receiver [ZZ] 1601336180, interchange 906653327 date 250716 time 0800 version 00501 usage P; group HB control 906653327 date 20250716 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 14
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1250374659, interchange 657123597 date 250626 time 0800 version 00501 usage P; group HC control 657123597 date 20250626 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 440715704 date 250626 time 0800 version 00501 usage P; group HN control 440715704 date 20250626 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1250374659 to receiver [ZZ] 1601336180, interchange 768525806 date 250713 time 0800 version 00501 usage P; group HP control 768525806 date 20250713 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
