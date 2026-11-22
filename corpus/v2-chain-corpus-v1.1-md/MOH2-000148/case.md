# Case MOH2-000148

Patient CHARLES DAVIS, DOB 1987-10-26, sex M, member ID NYV256412758. Payer: KEYSTONE COMMERCIAL HEALTH. Service date 2025-04-19.

## Adjudication outcome (835)
Claim PA28954129: status 4 (denied). Billed $220.84, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2523612883988, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2025-08-24.
Payer [PR]: KEYSTONE COMMERCIAL HEALTH; 1200 MARKET ST; PHILADELPHIA, PA, 191071200; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT277616900, originator 1165028491.
claim statement period start (232): 2025-04-19.
Outpatient adjudication remarks (MOA): N211 (you may not appeal this decision).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $44.93 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $44.93 |  |
| 2 | 97112-GP | 2 | $100.56 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $100.56 |  |
| 3 | 97140-GP | 1 | $37.52 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $37.52 |  |
| 4 | 97140-GP | 1 | $37.83 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $37.83 |  |

Line item control numbers (REF 6R): PA28954129L1, PA28954129L2, PA28954129L3, PA28954129L4.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: CHARLES DAVIS; MI (member ID) NYV256412758; rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273.

## Claim as billed (837P)
Claim PA28954129, total charge $220.84, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $44.93 | 2025-04-19 | 1 | PA28954129L1 |
| 2 | 97112-GP | 2 UN | $100.56 | 2025-04-19 | 1 | PA28954129L2 |
| 3 | 97140-GP | 1 UN | $37.52 | 2025-04-19 | 1 | PA28954129L3 |
| 4 | 97140-GP | 1 UN | $37.83 | 2025-04-19 | 1 | PA28954129L4 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: KEYSTONE COMMERCIAL HEALTH; 46 (ETIN) 1650284917
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: CHARLES DAVIS; MI (member ID) NYV256412758; 2217 CHESTNUT RD; STATEN ISLAND, NY, 10332
- payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917
- referring provider [DN]: OMAR DELGADO; XX (NPI) 1094074058
- rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273
- Submission reference TRC77065836, dated 2025-08-03 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2025-04-19.
Inquiry parties: payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: CHARLES DAVIS; MI (member ID) NYV256412758.
Subject DOB 1987-10-26, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: KEYSTONE COMMERCIAL HEALTH HMO
- plan date (291): 2025-04-19
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: CHARLES DAVIS; MI (member ID) NYV256412758.
Subject DOB 1987-10-26, sex M.
Eligibility exchange reference ELG67032149, dated 2025-08-25 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
No 277CA acknowledgment is present for this case.

## Chart note (verbatim)

PT treatment note 2025-04-19. Dx: Aftercare following joint replacement surgery. 97110 (14 min): therapeutic exercise for strength and ROM. 97112 (31 min): neuromuscular re-education of movement and balance. 97140 (16 min): manual therapy (soft tissue and joint mobilization). 97140 (16 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 77. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1650284917, interchange 532693094 date 250825 time 0800 version 00501 usage P; group HS control 532693094 date 20250825 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1650284917 to receiver [ZZ] 1110692305, interchange 890361894 date 250825 time 0800 version 00501 usage P; group HB control 890361894 date 20250825 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1650284917, interchange 331354643 date 250803 time 0800 version 00501 usage P; group HC control 331354643 date 20250803 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 38
- remit_835: sender [ZZ] 1650284917 to receiver [ZZ] 1110692305, interchange 277616900 date 250824 time 0800 version 00501 usage P; group HP control 277616900 date 20250824 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 35
