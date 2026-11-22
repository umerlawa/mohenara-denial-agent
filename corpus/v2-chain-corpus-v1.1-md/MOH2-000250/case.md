# Case MOH2-000250

Patient CHARLES DAVIS, DOB 1987-10-26, sex M, member ID NYV256412758. Payer: KEYSTONE COMMERCIAL HEALTH. Service date 2025-05-07.

## Adjudication outcome (835)
Claim PA22743925: status 4 (denied). Billed $137.52, paid $0, patient responsibility $137.52. Filing indicator CI (commercial insurance). Payer claim control 2516400013097, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2025-06-13.
Payer [PR]: KEYSTONE COMMERCIAL HEALTH; 1200 MARKET ST; PHILADELPHIA, PA, 191071200; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT710212843, originator 1165028491.
claim statement period start (232): 2025-05-07.
Outpatient adjudication remarks (MOA): N30 (patient ineligible for this service).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 | $83.96 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $83.96 |  |
| 2 | 97112-GP | 1 | $53.56 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $53.56 |  |

Line item control numbers (REF 6R): PA22743925L1, PA22743925L2.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: CHARLES DAVIS; MI (member ID) NYV256412758; rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273.

## Claim as billed (837P)
Claim PA22743925, total charge $137.52, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 UN | $83.96 | 2025-05-07 | 1 | PA22743925L1 |
| 2 | 97112-GP | 1 UN | $53.56 | 2025-05-07 | 1 | PA22743925L2 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: KEYSTONE COMMERCIAL HEALTH; 46 (ETIN) 1650284917
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: CHARLES DAVIS; MI (member ID) NYV256412758; 2217 CHESTNUT RD; STATEN ISLAND, NY, 10332
- payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917
- referring provider [DN]: OMAR DELGADO; XX (NPI) 1094074058
- rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273
- Submission reference TRC88878356, dated 2025-05-10 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2025-05-07.
Inquiry parties: payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: CHARLES DAVIS; MI (member ID) NYV256412758.
Subject DOB 1987-10-26, sex M.

Response:
- benefit: 6 (inactive), coverage level IND, service type 30 (health benefit plan coverage), plan: KEYSTONE COMMERCIAL HEALTH HMO
- plan date (291): 2025-05-07
- eligibility begin (356): 2024-01-01
- eligibility end (357): 2025-04-30
Response parties: payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: CHARLES DAVIS; MI (member ID) NYV256412758.
Subject DOB 1987-10-26, sex M.
Eligibility exchange reference ELG13592171, dated 2025-06-16 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2025-05-11, action code WQ, amount $137.52.
D9 (clearinghouse claim number): TRC88878356.
Trace (2 (referenced transaction trace)): TRC88878356.
received date (050): 2025-05-11.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: CHARLES DAVIS; MI (member ID) NYV256412758.
Acknowledgment reference ACK88878356, dated 2025-05-11 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2025-05-07. Dx: Aftercare following joint replacement surgery. 97110 (30 min): therapeutic exercise for strength and ROM. 97112 (15 min): neuromuscular re-education of movement and balance. Total timed minutes: 45. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1650284917, interchange 242857299 date 250616 time 0800 version 00501 usage P; group HS control 242857299 date 20250616 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1650284917 to receiver [ZZ] 1110692305, interchange 331895120 date 250616 time 0800 version 00501 usage P; group HB control 331895120 date 20250616 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 14
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1650284917, interchange 825258603 date 250510 time 0800 version 00501 usage P; group HC control 825258603 date 20250510 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 958100683 date 250511 time 0800 version 00501 usage P; group HN control 958100683 date 20250511 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1650284917 to receiver [ZZ] 1110692305, interchange 710212843 date 250613 time 0800 version 00501 usage P; group HP control 710212843 date 20250613 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 27
