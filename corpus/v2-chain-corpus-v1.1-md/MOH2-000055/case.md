# Case MOH2-000055

Patient CHARLES DAVIS, DOB 1987-10-26, sex M, member ID NYV256412758. Payer: KEYSTONE COMMERCIAL HEALTH. Service date 2025-04-16.

## Adjudication outcome (835)
Claim PA26855960: status 4 (denied). Billed $213.75, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2523925096885, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2025-08-27.
Payer [PR]: KEYSTONE COMMERCIAL HEALTH; 1200 MARKET ST; PHILADELPHIA, PA, 191071200; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT796254301, originator 1165028491.
claim statement period start (232): 2025-04-16.
Outpatient adjudication remarks (MOA): N211 (you may not appeal this decision).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97112-GP | 1 | $52.44 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $52.44 |  |
| 2 | 97530-GP | 2 | $111.69 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $111.69 |  |
| 3 | 97116-GP | 1 | $49.62 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $49.62 |  |

Line item control numbers (REF 6R): PA26855960L1, PA26855960L2, PA26855960L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: CHARLES DAVIS; MI (member ID) NYV256412758; rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273.

## Claim as billed (837P)
Claim PA26855960, total charge $213.75, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97112-GP | 1 UN | $52.44 | 2025-04-16 | 1 | PA26855960L1 |
| 2 | 97530-GP | 2 UN | $111.69 | 2025-04-16 | 1 | PA26855960L2 |
| 3 | 97116-GP | 1 UN | $49.62 | 2025-04-16 | 1 | PA26855960L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: KEYSTONE COMMERCIAL HEALTH; 46 (ETIN) 1650284917
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: CHARLES DAVIS; MI (member ID) NYV256412758; 2217 CHESTNUT RD; STATEN ISLAND, NY, 10332
- payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917
- referring provider [DN]: OMAR DELGADO; XX (NPI) 1094074058
- rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273
- Submission reference TRC73615608, dated 2025-08-10 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2025-04-16.
Inquiry parties: payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: CHARLES DAVIS; MI (member ID) NYV256412758.
Subject DOB 1987-10-26, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: KEYSTONE COMMERCIAL HEALTH HMO
- plan date (291): 2025-04-16
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: CHARLES DAVIS; MI (member ID) NYV256412758.
Subject DOB 1987-10-26, sex M.
Eligibility exchange reference ELG21815414, dated 2025-09-02 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
No 277CA acknowledgment is present for this case.

## Chart note (verbatim)

PT treatment note 2025-04-16. Dx: Aftercare following joint replacement surgery. 97112 (14 min): neuromuscular re-education of movement and balance. 97530 (30 min): therapeutic activities (dynamic functional tasks). 97116 (16 min): gait training with assistive device progression. Total timed minutes: 60. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1650284917, interchange 803531059 date 250902 time 0800 version 00501 usage P; group HS control 803531059 date 20250902 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1650284917 to receiver [ZZ] 1110692305, interchange 594166409 date 250902 time 0800 version 00501 usage P; group HB control 594166409 date 20250902 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1650284917, interchange 522917417 date 250810 time 0800 version 00501 usage P; group HC control 522917417 date 20250810 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- remit_835: sender [ZZ] 1650284917 to receiver [ZZ] 1110692305, interchange 796254301 date 250827 time 0800 version 00501 usage P; group HP control 796254301 date 20250827 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
