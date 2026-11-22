# Case MOH2-000295

Patient CARLOS WILSON, DOB 1970-03-05, sex F, member ID KLU968297324. Payer: ATLANTIC SHORE ASSURANCE. Service date 2026-09-05.

## Adjudication outcome (835)
Claim PA21954243: status 4 (denied). Billed $202.66, paid $0, patient responsibility $202.66. Filing indicator CI (commercial insurance). Payer claim control 2628501976212, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-10-12.
Payer [PR]: ATLANTIC SHORE ASSURANCE; 3499 ROUTE 9 N; FREEHOLD, NJ, 077283100; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT294761475, originator 1125037465.
claim statement period start (232): 2026-09-05.
Outpatient adjudication remarks (MOA): N30 (patient ineligible for this service).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97112-GP | 1 | $53.4 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $53.4 |  |
| 2 | 97140-GP | 2 | $76.48 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $76.48 |  |
| 3 | 97140-GP | 2 | $72.78 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $72.78 |  |

Line item control numbers (REF 6R): PA21954243L1, PA21954243L2, PA21954243L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: CARLOS WILSON; MI (member ID) KLU968297324; rendering provider [82]: MARY CLARK; XX (NPI) 1992501921.

## Claim as billed (837P)
Claim PA21954243, total charge $202.66, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97112-GP | 1 UN | $53.4 | 2026-09-05 | 1 | PA21954243L1 |
| 2 | 97140-GP | 2 UN | $76.48 | 2026-09-05 | 1 | PA21954243L2 |
| 3 | 97140-GP | 2 UN | $72.78 | 2026-09-05 | 1 | PA21954243L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: ATLANTIC SHORE ASSURANCE; 46 (ETIN) 1250374659
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: CARLOS WILSON; MI (member ID) KLU968297324; 8812 CHESTNUT AVE; STATEN ISLAND, NY, 10329
- payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659
- referring provider [DN]: MARCUS WEBB; XX (NPI) 1583494452
- rendering provider [82]: MARY CLARK; XX (NPI) 1992501921
- Submission reference TRC31979690, dated 2026-09-18 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-09-05.
Inquiry parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: CARLOS WILSON; MI (member ID) KLU968297324.
Subject DOB 1970-03-05, sex F.

Response:
- benefit: 6 (inactive), coverage level IND, service type 30 (health benefit plan coverage), plan: ATLANTIC SHORE ASSURANCE HMO
- plan date (291): 2026-09-05
- eligibility begin (356): 2024-01-01
- eligibility end (357): 2026-08-31
Response parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: CARLOS WILSON; MI (member ID) KLU968297324.
Subject DOB 1970-03-05, sex F.
Eligibility exchange reference ELG69359011, dated 2026-10-13 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-09-20, action code WQ, amount $202.66.
D9 (clearinghouse claim number): TRC31979690.
Trace (2 (referenced transaction trace)): TRC31979690.
received date (050): 2026-09-20.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: CARLOS WILSON; MI (member ID) KLU968297324.
Acknowledgment reference ACK31979690, dated 2026-09-20 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-09-05. Dx: Aftercare following joint replacement surgery. 97112 (14 min): neuromuscular re-education of movement and balance. 97140 (31 min): manual therapy (soft tissue and joint mobilization). 97140 (30 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 75. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1250374659, interchange 846685952 date 261013 time 0800 version 00501 usage P; group HS control 846685952 date 20261013 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1250374659 to receiver [ZZ] 1110692305, interchange 321978499 date 261013 time 0800 version 00501 usage P; group HB control 321978499 date 20261013 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 14
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1250374659, interchange 164655804 date 260918 time 0800 version 00501 usage P; group HC control 164655804 date 20260918 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 138384594 date 260920 time 0800 version 00501 usage P; group HN control 138384594 date 20260920 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1250374659 to receiver [ZZ] 1110692305, interchange 294761475 date 261012 time 0800 version 00501 usage P; group HP control 294761475 date 20261012 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
