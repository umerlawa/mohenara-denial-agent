# Case MOH2-000571

Patient PATRICIA THOMPSON, DOB 1984-04-04, sex M, member ID BVU866469049. Payer: KEYSTONE COMMERCIAL HEALTH. Service date 2025-07-02.

## Adjudication outcome (835)
Claim PA23846228: status 4 (denied). Billed $276.99, paid $0, patient responsibility $276.99. Filing indicator CI (commercial insurance). Payer claim control 2523555475933, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2025-08-23.
Payer [PR]: KEYSTONE COMMERCIAL HEALTH; 1200 MARKET ST; PHILADELPHIA, PA, 191071200; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT473350873, originator 1165028491.
claim statement period start (232): 2025-07-02.
Outpatient adjudication remarks (MOA): N30 (patient ineligible for this service).
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97530-GP | 2 | $123.41 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $123.41 |  |
| 2 | 97112-GP | 2 | $103.92 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $103.92 |  |
| 3 | 97140-GP | 1 | $49.66 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $49.66 |  |

Line item control numbers (REF 6R): PA23846228L1, PA23846228L2, PA23846228L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: PATRICIA THOMPSON; MI (member ID) BVU866469049; rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142.

## Claim as billed (837P)
Claim PA23846228, total charge $276.99, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M542 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97530-GP | 2 UN | $123.41 | 2025-07-02 | 1 | PA23846228L1 |
| 2 | 97112-GP | 2 UN | $103.92 | 2025-07-02 | 1 | PA23846228L2 |
| 3 | 97140-GP | 1 UN | $49.66 | 2025-07-02 | 1 | PA23846228L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: KEYSTONE COMMERCIAL HEALTH; 46 (ETIN) 1650284917
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: PATRICIA THOMPSON; MI (member ID) BVU866469049; 2649 CHESTNUT LN; TRENTON, NJ, 08625
- payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917
- referring provider [DN]: DAVID GOLDSTEIN; XX (NPI) 1996029234
- rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142
- Submission reference TRC52838816, dated 2025-07-22 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2025-07-02.
Inquiry parties: payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: PATRICIA THOMPSON; MI (member ID) BVU866469049.
Subject DOB 1984-04-04, sex M.

Response:
- benefit: 6 (inactive), coverage level IND, service type 30 (health benefit plan coverage), plan: KEYSTONE COMMERCIAL HEALTH POS
- plan date (291): 2025-07-02
- eligibility begin (356): 2024-01-01
- eligibility end (357): 2025-06-30
Response parties: payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: PATRICIA THOMPSON; MI (member ID) BVU866469049.
Subject DOB 1984-04-04, sex M.
Eligibility exchange reference ELG15823397, dated 2025-08-27 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2025-07-22, action code WQ, amount $276.99.
D9 (clearinghouse claim number): TRC52838816.
Trace (2 (referenced transaction trace)): TRC52838816.
received date (050): 2025-07-22.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: PATRICIA THOMPSON; MI (member ID) BVU866469049.
Acknowledgment reference ACK52838816, dated 2025-07-22 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2025-07-02. Dx: Cervicalgia. 97530 (30 min): therapeutic activities (dynamic functional tasks). 97112 (31 min): neuromuscular re-education of movement and balance. 97140 (16 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 77. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1650284917, interchange 802533001 date 250827 time 0800 version 00501 usage P; group HS control 802533001 date 20250827 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1650284917 to receiver [ZZ] 1801579548, interchange 669320415 date 250827 time 0800 version 00501 usage P; group HB control 669320415 date 20250827 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 14
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1650284917, interchange 830347378 date 250722 time 0800 version 00501 usage P; group HC control 830347378 date 20250722 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 271673797 date 250722 time 0800 version 00501 usage P; group HN control 271673797 date 20250722 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1650284917 to receiver [ZZ] 1801579548, interchange 473350873 date 250823 time 0800 version 00501 usage P; group HP control 473350873 date 20250823 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
