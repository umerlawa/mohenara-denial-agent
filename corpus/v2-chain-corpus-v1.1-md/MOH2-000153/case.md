# Case MOH2-000153

Patient PATRICIA THOMPSON, DOB 1984-04-04, sex M, member ID BVU866469049. Payer: KEYSTONE COMMERCIAL HEALTH. Service date 2025-01-29.

## Adjudication outcome (835)
Claim PA27438668: status 4 (denied). Billed $116.52, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2517075059535, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2025-06-19.
Payer [PR]: KEYSTONE COMMERCIAL HEALTH; 1200 MARKET ST; PHILADELPHIA, PA, 191071200; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT972869637, originator 1165028491.
claim statement period start (232): 2025-01-29.
Outpatient adjudication remarks (MOA): N211 (you may not appeal this decision).
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $42.33 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $42.33 |  |
| 2 | 97140-GP | 2 | $74.19 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $74.19 |  |

Line item control numbers (REF 6R): PA27438668L1, PA27438668L2.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: PATRICIA THOMPSON; MI (member ID) BVU866469049; rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142.

## Claim as billed (837P)
Claim PA27438668, total charge $116.52, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M542 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $42.33 | 2025-01-29 | 1 | PA27438668L1 |
| 2 | 97140-GP | 2 UN | $74.19 | 2025-01-29 | 1 | PA27438668L2 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: KEYSTONE COMMERCIAL HEALTH; 46 (ETIN) 1650284917
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: PATRICIA THOMPSON; MI (member ID) BVU866469049; 2649 CHESTNUT LN; TRENTON, NJ, 08625
- payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917
- referring provider [DN]: DAVID GOLDSTEIN; XX (NPI) 1996029234
- rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142
- Submission reference TRC16862806, dated 2025-06-03 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2025-01-29.
Inquiry parties: payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: PATRICIA THOMPSON; MI (member ID) BVU866469049.
Subject DOB 1984-04-04, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: KEYSTONE COMMERCIAL HEALTH POS
- plan date (291): 2025-01-29
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: PATRICIA THOMPSON; MI (member ID) BVU866469049.
Subject DOB 1984-04-04, sex M.
Eligibility exchange reference ELG26482339, dated 2025-06-26 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2025-02-10, action code WQ, amount $116.52.
D9 (clearinghouse claim number): TRC16862806.
Trace (2 (referenced transaction trace)): TRC16862806.
received date (050): 2025-02-10.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: PATRICIA THOMPSON; MI (member ID) BVU866469049.
Acknowledgment reference ACK16862806, dated 2025-02-10 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2025-01-29. Dx: Cervicalgia. 97110 (15 min): therapeutic exercise for strength and ROM. 97140 (30 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 45. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1650284917, interchange 335739220 date 250626 time 0800 version 00501 usage P; group HS control 335739220 date 20250626 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1650284917 to receiver [ZZ] 1801579548, interchange 382129489 date 250626 time 0800 version 00501 usage P; group HB control 382129489 date 20250626 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1650284917, interchange 586915599 date 250603 time 0800 version 00501 usage P; group HC control 586915599 date 20250603 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 992120957 date 250210 time 0800 version 00501 usage P; group HN control 992120957 date 20250210 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1650284917 to receiver [ZZ] 1801579548, interchange 972869637 date 250619 time 0800 version 00501 usage P; group HP control 972869637 date 20250619 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 27
