# Case MOH2-000732

Patient CARLOS WILSON, DOB 1970-03-05, sex F, member ID KLU968297324. Payer: ATLANTIC SHORE ASSURANCE. Service date 2026-09-07.

## Adjudication outcome (835)
Claim PA28196649: status 4 (denied). Billed $178.64, paid $0, patient responsibility $178.64. Filing indicator CI (commercial insurance). Payer claim control 2629325450887, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-10-20.
Payer [PR]: ATLANTIC SHORE ASSURANCE; 3499 ROUTE 9 N; FREEHOLD, NJ, 077283100; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT465647462, originator 1125037465.
claim statement period start (232): 2026-09-07.
Outpatient adjudication remarks (MOA): N30 (patient ineligible for this service).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97140-GP | 1 | $36.76 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $36.76 |  |
| 2 | 97112-GP | 2 | $92.15 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $92.15 |  |
| 3 | 97110-GP | 1 | $49.73 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $49.73 |  |

Line item control numbers (REF 6R): PA28196649L1, PA28196649L2, PA28196649L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: CARLOS WILSON; MI (member ID) KLU968297324; rendering provider [82]: MARY CLARK; XX (NPI) 1992501921.

## Claim as billed (837P)
Claim PA28196649, total charge $178.64, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97140-GP | 1 UN | $36.76 | 2026-09-07 | 1 | PA28196649L1 |
| 2 | 97112-GP | 2 UN | $92.15 | 2026-09-07 | 1 | PA28196649L2 |
| 3 | 97110-GP | 1 UN | $49.73 | 2026-09-07 | 1 | PA28196649L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: ATLANTIC SHORE ASSURANCE; 46 (ETIN) 1250374659
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: CARLOS WILSON; MI (member ID) KLU968297324; 8812 CHESTNUT AVE; STATEN ISLAND, NY, 10329
- payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659
- referring provider [DN]: MARCUS WEBB; XX (NPI) 1583494452
- rendering provider [82]: MARY CLARK; XX (NPI) 1992501921
- Submission reference TRC47051064, dated 2026-09-16 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-09-07.
Inquiry parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: CARLOS WILSON; MI (member ID) KLU968297324.
Subject DOB 1970-03-05, sex F.

Response:
- benefit: 6 (inactive), coverage level IND, service type 30 (health benefit plan coverage), plan: ATLANTIC SHORE ASSURANCE HMO
- plan date (291): 2026-09-07
- eligibility begin (356): 2024-01-01
- eligibility end (357): 2026-08-31
Response parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: CARLOS WILSON; MI (member ID) KLU968297324.
Subject DOB 1970-03-05, sex F.
Eligibility exchange reference ELG82009728, dated 2026-10-25 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-09-18, action code WQ, amount $178.64.
D9 (clearinghouse claim number): TRC47051064.
Trace (2 (referenced transaction trace)): TRC47051064.
received date (050): 2026-09-18.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: CARLOS WILSON; MI (member ID) KLU968297324.
Acknowledgment reference ACK47051064, dated 2026-09-18 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-09-07. Dx: Aftercare following joint replacement surgery. 97140 (14 min): manual therapy (soft tissue and joint mobilization). 97112 (29 min): neuromuscular re-education of movement and balance. 97110 (16 min): therapeutic exercise for strength and ROM. Total timed minutes: 59. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1250374659, interchange 964607416 date 261025 time 0800 version 00501 usage P; group HS control 964607416 date 20261025 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1250374659 to receiver [ZZ] 1110692305, interchange 760326118 date 261025 time 0800 version 00501 usage P; group HB control 760326118 date 20261025 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 14
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1250374659, interchange 155077812 date 260916 time 0800 version 00501 usage P; group HC control 155077812 date 20260916 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 986217203 date 260918 time 0800 version 00501 usage P; group HN control 986217203 date 20260918 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1250374659 to receiver [ZZ] 1110692305, interchange 465647462 date 261020 time 0800 version 00501 usage P; group HP control 465647462 date 20261020 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
