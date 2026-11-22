# Case MOH2-000018

Patient CHARLES DAVIS, DOB 1987-10-26, sex M, member ID NYV256412758. Payer: KEYSTONE COMMERCIAL HEALTH. Service date 2025-02-13.

## Adjudication outcome (835)
Claim PA29340131: status 4 (denied). Billed $199.74, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2518830022949, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2025-07-07.
Payer [PR]: KEYSTONE COMMERCIAL HEALTH; 1200 MARKET ST; PHILADELPHIA, PA, 191071200; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT310523155, originator 1165028491.
claim statement period start (232): 2025-02-13.
Outpatient adjudication remarks (MOA): N211 (you may not appeal this decision).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 | $85.09 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $85.09 |  |
| 2 | 97112-GP | 2 | $114.65 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $114.65 |  |

Line item control numbers (REF 6R): PA29340131L1, PA29340131L2.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: CHARLES DAVIS; MI (member ID) NYV256412758; rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273.

## Claim as billed (837P)
Claim PA29340131, total charge $199.74, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 UN | $85.09 | 2025-02-13 | 1 | PA29340131L1 |
| 2 | 97112-GP | 2 UN | $114.65 | 2025-02-13 | 1 | PA29340131L2 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: KEYSTONE COMMERCIAL HEALTH; 46 (ETIN) 1650284917
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: CHARLES DAVIS; MI (member ID) NYV256412758; 2217 CHESTNUT RD; STATEN ISLAND, NY, 10332
- payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917
- referring provider [DN]: OMAR DELGADO; XX (NPI) 1094074058
- rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273
- Submission reference TRC50089111, dated 2025-06-15 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2025-02-13.
Inquiry parties: payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: CHARLES DAVIS; MI (member ID) NYV256412758.
Subject DOB 1987-10-26, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: KEYSTONE COMMERCIAL HEALTH HMO
- plan date (291): 2025-02-13
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: CHARLES DAVIS; MI (member ID) NYV256412758.
Subject DOB 1987-10-26, sex M.
Eligibility exchange reference ELG24818209, dated 2025-07-10 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2025-02-24, action code WQ, amount $199.74.
D9 (clearinghouse claim number): TRC50089111.
Trace (2 (referenced transaction trace)): TRC50089111.
received date (050): 2025-02-24.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: CHARLES DAVIS; MI (member ID) NYV256412758.
Acknowledgment reference ACK50089111, dated 2025-02-24 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2025-02-13. Dx: Aftercare following joint replacement surgery. 97110 (31 min): therapeutic exercise for strength and ROM. 97112 (30 min): neuromuscular re-education of movement and balance. Total timed minutes: 61. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1650284917, interchange 142578472 date 250710 time 0800 version 00501 usage P; group HS control 142578472 date 20250710 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1650284917 to receiver [ZZ] 1110692305, interchange 817193582 date 250710 time 0800 version 00501 usage P; group HB control 817193582 date 20250710 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1650284917, interchange 583501595 date 250615 time 0800 version 00501 usage P; group HC control 583501595 date 20250615 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 279219615 date 250224 time 0800 version 00501 usage P; group HN control 279219615 date 20250224 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1650284917 to receiver [ZZ] 1110692305, interchange 310523155 date 250707 time 0800 version 00501 usage P; group HP control 310523155 date 20250707 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 27
