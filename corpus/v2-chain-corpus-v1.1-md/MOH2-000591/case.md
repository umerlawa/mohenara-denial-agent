# Case MOH2-000591

Patient MARY RODRIGUEZ, DOB 1940-12-16, sex M, member ID YJS021246875. Payer: KEYSTONE COMMERCIAL HEALTH. Service date 2026-02-02.

## Adjudication outcome (835)
Claim PA24138655: status 4 (denied). Billed $306.11, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2607605212380, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-03-17.
Payer [PR]: KEYSTONE COMMERCIAL HEALTH; 1200 MARKET ST; PHILADELPHIA, PA, 191071200; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT711824891, originator 1165028491.
claim statement period start (232): 2026-02-02.
Outpatient adjudication remarks (MOA): MA04 (secondary payment cannot be considered without primary payer identity).
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $48.91 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $48.91 |  |
| 2 | 97112-GP | 1 | $58.74 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $58.74 |  |
| 3 | 97140-GP | 2 | $90.14 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $90.14 |  |
| 4 | 97530-GP | 1 | $51.4 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $51.4 |  |
| 5 | 97535-GP | 1 | $56.92 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $56.92 |  |

Line item control numbers (REF 6R): PA24138655L1, PA24138655L2, PA24138655L3, PA24138655L4, PA24138655L5.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: MARY RODRIGUEZ; MI (member ID) YJS021246875; rendering provider [82]: DOROTHY LOPEZ; XX (NPI) 1390221007.

## Claim as billed (837P)
Claim PA24138655, total charge $306.11, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $48.91 | 2026-02-02 | 1 | PA24138655L1 |
| 2 | 97112-GP | 1 UN | $58.74 | 2026-02-02 | 1 | PA24138655L2 |
| 3 | 97140-GP | 2 UN | $90.14 | 2026-02-02 | 1 | PA24138655L3 |
| 4 | 97530-GP | 1 UN | $51.4 | 2026-02-02 | 1 | PA24138655L4 |
| 5 | 97535-GP | 1 UN | $56.92 | 2026-02-02 | 1 | PA24138655L5 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: KEYSTONE COMMERCIAL HEALTH; 46 (ETIN) 1650284917
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: MARY RODRIGUEZ; MI (member ID) YJS021246875; 2115 FRANKLIN ST; PHILADELPHIA, PA, 19180
- payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917
- referring provider [DN]: OMAR DELGADO; XX (NPI) 1094074058
- rendering provider [82]: DOROTHY LOPEZ; XX (NPI) 1390221007
- Submission reference TRC70819523, dated 2026-02-14 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-02-02.
Inquiry parties: payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: MARY RODRIGUEZ; MI (member ID) YJS021246875.
Subject DOB 1940-12-16, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: KEYSTONE COMMERCIAL HEALTH EPO
- benefit: R (other or additional payer), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-02-02
- eligibility begin (356): 2024-01-01
- eligibility begin (356): 2024-01-01
- payer message: PLAN IS PRIMARY PAYER FOR THIS MEMBER
Response parties: payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: MARY RODRIGUEZ; MI (member ID) YJS021246875; payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352.
Subject DOB 1940-12-16, sex M.
Eligibility exchange reference ELG60840763, dated 2026-03-22 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-02-16, action code WQ, amount $306.11.
D9 (clearinghouse claim number): TRC70819523.
Trace (2 (referenced transaction trace)): TRC70819523.
received date (050): 2026-02-16.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: MARY RODRIGUEZ; MI (member ID) YJS021246875.
Acknowledgment reference ACK70819523, dated 2026-02-16 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-02-02. Dx: Aftercare following joint replacement surgery. 97110 (14 min): therapeutic exercise for strength and ROM. 97112 (16 min): neuromuscular re-education of movement and balance. 97140 (30 min): manual therapy (soft tissue and joint mobilization). 97530 (16 min): therapeutic activities (dynamic functional tasks). 97535 (16 min): self-care/home management training. Total timed minutes: 92. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1650284917, interchange 994122950 date 260322 time 0800 version 00501 usage P; group HS control 994122950 date 20260322 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1650284917 to receiver [ZZ] 1801579548, interchange 470338363 date 260322 time 0800 version 00501 usage P; group HB control 470338363 date 20260322 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 17
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1650284917, interchange 202910201 date 260214 time 0800 version 00501 usage P; group HC control 202910201 date 20260214 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 42
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 922699730 date 260216 time 0800 version 00501 usage P; group HN control 922699730 date 20260216 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1650284917 to receiver [ZZ] 1801579548, interchange 711824891 date 260317 time 0800 version 00501 usage P; group HP control 711824891 date 20260317 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 39
