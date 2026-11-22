# Case MOH2-000127

Patient PATRICIA THOMPSON, DOB 1984-04-04, sex M, member ID BVU866469049. Payer: KEYSTONE COMMERCIAL HEALTH. Service date 2025-07-12.

## Adjudication outcome (835)
Claim PA23709796: status 4 (denied). Billed $138.54, paid $0, patient responsibility $138.54. Filing indicator CI (commercial insurance). Payer claim control 2521732151058, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2025-08-05.
Payer [PR]: KEYSTONE COMMERCIAL HEALTH; 1200 MARKET ST; PHILADELPHIA, PA, 191071200; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT451971232, originator 1165028491.
claim statement period start (232): 2025-07-12.
Outpatient adjudication remarks (MOA): N30 (patient ineligible for this service).
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $46.17 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $46.17 |  |
| 2 | 97112-GP | 1 | $46.66 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $46.66 |  |
| 3 | 97110-GP | 1 | $45.71 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $45.71 |  |

Line item control numbers (REF 6R): PA23709796L1, PA23709796L2, PA23709796L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: PATRICIA THOMPSON; MI (member ID) BVU866469049; rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142.

## Claim as billed (837P)
Claim PA23709796, total charge $138.54, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M542 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $46.17 | 2025-07-12 | 1 | PA23709796L1 |
| 2 | 97112-GP | 1 UN | $46.66 | 2025-07-12 | 1 | PA23709796L2 |
| 3 | 97110-GP | 1 UN | $45.71 | 2025-07-12 | 1 | PA23709796L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: KEYSTONE COMMERCIAL HEALTH; 46 (ETIN) 1650284917
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: PATRICIA THOMPSON; MI (member ID) BVU866469049; 2649 CHESTNUT LN; TRENTON, NJ, 08625
- payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917
- referring provider [DN]: DAVID GOLDSTEIN; XX (NPI) 1996029234
- rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142
- Submission reference TRC24953463, dated 2025-07-16 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2025-07-12.
Inquiry parties: payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: PATRICIA THOMPSON; MI (member ID) BVU866469049.
Subject DOB 1984-04-04, sex M.

Response:
- benefit: 6 (inactive), coverage level IND, service type 30 (health benefit plan coverage), plan: KEYSTONE COMMERCIAL HEALTH POS
- plan date (291): 2025-07-12
- eligibility begin (356): 2024-01-01
- eligibility end (357): 2025-06-30
Response parties: payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: PATRICIA THOMPSON; MI (member ID) BVU866469049.
Subject DOB 1984-04-04, sex M.
Eligibility exchange reference ELG28068485, dated 2025-08-10 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2025-07-18, action code WQ, amount $138.54.
D9 (clearinghouse claim number): TRC24953463.
Trace (2 (referenced transaction trace)): TRC24953463.
received date (050): 2025-07-18.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: PATRICIA THOMPSON; MI (member ID) BVU866469049.
Acknowledgment reference ACK24953463, dated 2025-07-18 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2025-07-12. Dx: Cervicalgia. 97110 (16 min): therapeutic exercise for strength and ROM. 97112 (15 min): neuromuscular re-education of movement and balance. 97110 (14 min): therapeutic exercise for strength and ROM. Total timed minutes: 45. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1650284917, interchange 868400863 date 250810 time 0800 version 00501 usage P; group HS control 868400863 date 20250810 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1650284917 to receiver [ZZ] 1801579548, interchange 828073170 date 250810 time 0800 version 00501 usage P; group HB control 828073170 date 20250810 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 14
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1650284917, interchange 922808419 date 250716 time 0800 version 00501 usage P; group HC control 922808419 date 20250716 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 165244593 date 250718 time 0800 version 00501 usage P; group HN control 165244593 date 20250718 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1650284917 to receiver [ZZ] 1801579548, interchange 451971232 date 250805 time 0800 version 00501 usage P; group HP control 451971232 date 20250805 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
