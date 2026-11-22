# Case MOH2-000706

Patient JESSICA HARRIS, DOB 1997-12-11, sex F, member ID SXA354348278. Payer: KEYSTONE COMMERCIAL HEALTH. Service date 2025-05-30.

## Adjudication outcome (835)
Claim PA23301405: status 4 (denied). Billed $196.86, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2530682548488, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2025-11-02.
Payer [PR]: KEYSTONE COMMERCIAL HEALTH; 1200 MARKET ST; PHILADELPHIA, PA, 191071200; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820.
Trace (1 (current transaction trace)): EFT431573863, originator 1165028491.
claim statement period start (232): 2025-05-30.
Outpatient adjudication remarks (MOA): N211 (you may not appeal this decision).
Payee TJ (federal tax ID): 321822487.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 | $88.37 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $88.37 |  |
| 2 | 97110-GP | 1 | $47.59 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $47.59 |  |
| 3 | 97530-GP | 1 | $60.9 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $60.9 |  |

Line item control numbers (REF 6R): PA23301405L1, PA23301405L2, PA23301405L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: JESSICA HARRIS; MI (member ID) SXA354348278; rendering provider [82]: MICHAEL MARTINEZ; XX (NPI) 1850202042.

## Claim as billed (837P)
Claim PA23301405, total charge $196.86, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M542 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 UN | $88.37 | 2025-05-30 | 1 | PA23301405L1 |
| 2 | 97110-GP | 1 UN | $47.59 | 2025-05-30 | 1 | PA23301405L2 |
| 3 | 97530-GP | 1 UN | $60.9 | 2025-05-30 | 1 | PA23301405L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: KEYSTONE COMMERCIAL HEALTH; 46 (ETIN) 1650284917
- billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820; EI (employer ID/EIN) 321822487
- insured/subscriber [IL]: JESSICA HARRIS; MI (member ID) SXA354348278; 6774 MAPLE LN; WILMINGTON, DE, 19814
- payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917
- referring provider [DN]: SARAH CHEN; XX (NPI) 1410042904
- rendering provider [82]: MICHAEL MARTINEZ; XX (NPI) 1850202042
- Submission reference TRC86827483, dated 2025-10-14 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2025-05-30.
Inquiry parties: payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: JESSICA HARRIS; MI (member ID) SXA354348278.
Subject DOB 1997-12-11, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: KEYSTONE COMMERCIAL HEALTH EPO
- plan date (291): 2025-05-30
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: JESSICA HARRIS; MI (member ID) SXA354348278.
Subject DOB 1997-12-11, sex F.
Eligibility exchange reference ELG55928402, dated 2025-11-07 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
No 277CA acknowledgment is present for this case.

## Chart note (verbatim)

PT treatment note 2025-05-30. Dx: Cervicalgia. 97110 (30 min): therapeutic exercise for strength and ROM. 97110 (14 min): therapeutic exercise for strength and ROM. 97530 (16 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 60. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1353206904 to receiver [ZZ] 1650284917, interchange 116802627 date 251107 time 0800 version 00501 usage P; group HS control 116802627 date 20251107 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1650284917 to receiver [ZZ] 1353206904, interchange 885183404 date 251107 time 0800 version 00501 usage P; group HB control 885183404 date 20251107 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 321822487 to receiver [ZZ] 1650284917, interchange 580592484 date 251014 time 0800 version 00501 usage P; group HC control 580592484 date 20251014 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- remit_835: sender [ZZ] 1650284917 to receiver [ZZ] 1353206904, interchange 431573863 date 251102 time 0800 version 00501 usage P; group HP control 431573863 date 20251102 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
