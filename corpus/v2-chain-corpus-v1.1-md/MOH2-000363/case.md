# Case MOH2-000363

Patient ROBERT WILSON, DOB 1979-12-16, sex F, member ID MAP727498881. Payer: ATLANTIC SHORE ASSURANCE. Service date 2025-06-15.

## Adjudication outcome (835)
Claim PA28660182: status 4 (denied). Billed $125.86, paid $0, patient responsibility $125.86. Filing indicator CI (commercial insurance). Payer claim control 2519628110612, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2025-07-15.
Payer [PR]: ATLANTIC SHORE ASSURANCE; 3499 ROUTE 9 N; FREEHOLD, NJ, 077283100; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT704082146, originator 1125037465.
claim statement period start (232): 2025-06-15.
Outpatient adjudication remarks (MOA): N30 (patient ineligible for this service).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97112-GP | 1 | $44.26 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $44.26 |  |
| 2 | 97110-GP | 1 | $38.26 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $38.26 |  |
| 3 | 97140-GP | 1 | $43.34 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $43.34 |  |

Line item control numbers (REF 6R): PA28660182L1, PA28660182L2, PA28660182L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: ROBERT WILSON; MI (member ID) MAP727498881; rendering provider [82]: WEI LEWIS; XX (NPI) 1986021803.

## Claim as billed (837P)
Claim PA28660182, total charge $125.86, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25511 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97112-GP | 1 UN | $44.26 | 2025-06-15 | 1 | PA28660182L1 |
| 2 | 97110-GP | 1 UN | $38.26 | 2025-06-15 | 1 | PA28660182L2 |
| 3 | 97140-GP | 1 UN | $43.34 | 2025-06-15 | 1 | PA28660182L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: ATLANTIC SHORE ASSURANCE; 46 (ETIN) 1250374659
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: ROBERT WILSON; MI (member ID) MAP727498881; 8008 CHESTNUT ST; TRENTON, NJ, 08618
- payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659
- referring provider [DN]: SARAH CHEN; XX (NPI) 1410042904
- rendering provider [82]: WEI LEWIS; XX (NPI) 1986021803
- Submission reference TRC89680162, dated 2025-06-25 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2025-06-15.
Inquiry parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: ROBERT WILSON; MI (member ID) MAP727498881.
Subject DOB 1979-12-16, sex F.

Response:
- benefit: 6 (inactive), coverage level IND, service type 30 (health benefit plan coverage), plan: ATLANTIC SHORE ASSURANCE PPO
- plan date (291): 2025-06-15
- eligibility begin (356): 2024-01-01
- eligibility end (357): 2025-05-31
Response parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: ROBERT WILSON; MI (member ID) MAP727498881.
Subject DOB 1979-12-16, sex F.
Eligibility exchange reference ELG67419450, dated 2025-07-21 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2025-06-27, action code WQ, amount $125.86.
D9 (clearinghouse claim number): TRC89680162.
Trace (2 (referenced transaction trace)): TRC89680162.
received date (050): 2025-06-27.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: ROBERT WILSON; MI (member ID) MAP727498881.
Acknowledgment reference ACK89680162, dated 2025-06-27 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2025-06-15. Dx: Pain in right shoulder. 97112 (15 min): neuromuscular re-education of movement and balance. 97110 (16 min): therapeutic exercise for strength and ROM. 97140 (16 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 47. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1250374659, interchange 329270811 date 250721 time 0800 version 00501 usage P; group HS control 329270811 date 20250721 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1250374659 to receiver [ZZ] 1601336180, interchange 622100467 date 250721 time 0800 version 00501 usage P; group HB control 622100467 date 20250721 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 14
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1250374659, interchange 571975475 date 250625 time 0800 version 00501 usage P; group HC control 571975475 date 20250625 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 655138973 date 250627 time 0800 version 00501 usage P; group HN control 655138973 date 20250627 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1250374659 to receiver [ZZ] 1601336180, interchange 704082146 date 250715 time 0800 version 00501 usage P; group HP control 704082146 date 20250715 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
