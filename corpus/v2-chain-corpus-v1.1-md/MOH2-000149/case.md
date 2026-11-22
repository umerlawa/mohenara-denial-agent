# Case MOH2-000149

Patient MARY RODRIGUEZ, DOB 1940-12-16, sex M, member ID YJS021246875. Payer: KEYSTONE COMMERCIAL HEALTH. Service date 2026-02-14.

## Adjudication outcome (835)
Claim PA21343104: status 4 (denied). Billed $303.52, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2609285948954, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-04-02.
Payer [PR]: KEYSTONE COMMERCIAL HEALTH; 1200 MARKET ST; PHILADELPHIA, PA, 191071200; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT670428312, originator 1165028491.
claim statement period start (232): 2026-02-14.
Outpatient adjudication remarks (MOA): MA04 (secondary payment cannot be considered without primary payer identity).
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $38.98 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $38.98 |  |
| 2 | 97112-GP | 1 | $57.06 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $57.06 |  |
| 3 | 97140-GP | 1 | $39.98 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $39.98 |  |
| 4 | 97530-GP | 2 | $117.97 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $117.97 |  |
| 5 | 97535-GP | 1 | $49.53 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $49.53 |  |

Line item control numbers (REF 6R): PA21343104L1, PA21343104L2, PA21343104L3, PA21343104L4, PA21343104L5.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: MARY RODRIGUEZ; MI (member ID) YJS021246875; rendering provider [82]: DOROTHY LOPEZ; XX (NPI) 1390221007.

## Claim as billed (837P)
Claim PA21343104, total charge $303.52, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $38.98 | 2026-02-14 | 1 | PA21343104L1 |
| 2 | 97112-GP | 1 UN | $57.06 | 2026-02-14 | 1 | PA21343104L2 |
| 3 | 97140-GP | 1 UN | $39.98 | 2026-02-14 | 1 | PA21343104L3 |
| 4 | 97530-GP | 2 UN | $117.97 | 2026-02-14 | 1 | PA21343104L4 |
| 5 | 97535-GP | 1 UN | $49.53 | 2026-02-14 | 1 | PA21343104L5 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: KEYSTONE COMMERCIAL HEALTH; 46 (ETIN) 1650284917
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: MARY RODRIGUEZ; MI (member ID) YJS021246875; 2115 FRANKLIN ST; PHILADELPHIA, PA, 19180
- payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917
- referring provider [DN]: OMAR DELGADO; XX (NPI) 1094074058
- rendering provider [82]: DOROTHY LOPEZ; XX (NPI) 1390221007
- Submission reference TRC62196010, dated 2026-02-23 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-02-14.
Inquiry parties: payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: MARY RODRIGUEZ; MI (member ID) YJS021246875.
Subject DOB 1940-12-16, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: KEYSTONE COMMERCIAL HEALTH EPO
- benefit: R (other or additional payer), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-02-14
- eligibility begin (356): 2024-01-01
- eligibility begin (356): 2024-01-01
- payer message: PLAN IS PRIMARY PAYER FOR THIS MEMBER
Response parties: payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: MARY RODRIGUEZ; MI (member ID) YJS021246875; payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352.
Subject DOB 1940-12-16, sex M.
Eligibility exchange reference ELG57319760, dated 2026-04-07 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-02-23, action code WQ, amount $303.52.
D9 (clearinghouse claim number): TRC62196010.
Trace (2 (referenced transaction trace)): TRC62196010.
received date (050): 2026-02-23.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: MARY RODRIGUEZ; MI (member ID) YJS021246875.
Acknowledgment reference ACK62196010, dated 2026-02-23 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-02-14. Dx: Aftercare following joint replacement surgery. 97110 (16 min): therapeutic exercise for strength and ROM. 97112 (14 min): neuromuscular re-education of movement and balance. 97140 (15 min): manual therapy (soft tissue and joint mobilization). 97530 (31 min): therapeutic activities (dynamic functional tasks). 97535 (14 min): self-care/home management training. Total timed minutes: 90. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1650284917, interchange 483788510 date 260407 time 0800 version 00501 usage P; group HS control 483788510 date 20260407 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1650284917 to receiver [ZZ] 1801579548, interchange 796666380 date 260407 time 0800 version 00501 usage P; group HB control 796666380 date 20260407 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 17
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1650284917, interchange 932016052 date 260223 time 0800 version 00501 usage P; group HC control 932016052 date 20260223 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 42
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 173760608 date 260223 time 0800 version 00501 usage P; group HN control 173760608 date 20260223 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1650284917 to receiver [ZZ] 1801579548, interchange 670428312 date 260402 time 0800 version 00501 usage P; group HP control 670428312 date 20260402 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 39
