# Case MOH2-000351

Patient FRANK JONES, DOB 1943-05-06, sex M, member ID KUL147221914. Payer: KEYSTONE COMMERCIAL HEALTH. Service date 2026-02-06.

## Adjudication outcome (835)
Claim PA21752863: status 4 (denied). Billed $126.55, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2608456224615, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-03-25.
Payer [PR]: KEYSTONE COMMERCIAL HEALTH; 1200 MARKET ST; PHILADELPHIA, PA, 191071200; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT453998439, originator 1165028491.
claim statement period start (232): 2026-02-06.
Outpatient adjudication remarks (MOA): MA04 (secondary payment cannot be considered without primary payer identity).
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $39.06 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $39.06 |  |
| 2 | 97112-GP | 1 | $45.35 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $45.35 |  |
| 3 | 97140-GP | 1 | $42.14 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $42.14 |  |

Line item control numbers (REF 6R): PA21752863L1, PA21752863L2, PA21752863L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: FRANK JONES; MI (member ID) KUL147221914; rendering provider [82]: DOROTHY LOPEZ; XX (NPI) 1390221007.

## Claim as billed (837P)
Claim PA21752863, total charge $126.55, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25511 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $39.06 | 2026-02-06 | 1 | PA21752863L1 |
| 2 | 97112-GP | 1 UN | $45.35 | 2026-02-06 | 1 | PA21752863L2 |
| 3 | 97140-GP | 1 UN | $42.14 | 2026-02-06 | 1 | PA21752863L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: KEYSTONE COMMERCIAL HEALTH; 46 (ETIN) 1650284917
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: FRANK JONES; MI (member ID) KUL147221914; 4526 FRANKLIN AVE; STATEN ISLAND, NY, 10370
- payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917
- referring provider [DN]: ELENA VASQUEZ; XX (NPI) 1863431679
- rendering provider [82]: DOROTHY LOPEZ; XX (NPI) 1390221007
- Submission reference TRC64552398, dated 2026-02-13 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-02-06.
Inquiry parties: payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: FRANK JONES; MI (member ID) KUL147221914.
Subject DOB 1943-05-06, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: KEYSTONE COMMERCIAL HEALTH HMO
- benefit: R (other or additional payer), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-02-06
- eligibility begin (356): 2024-01-01
- eligibility begin (356): 2024-01-01
- payer message: PLAN IS PRIMARY PAYER FOR THIS MEMBER
Response parties: payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: FRANK JONES; MI (member ID) KUL147221914; payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352.
Subject DOB 1943-05-06, sex M.
Eligibility exchange reference ELG93404378, dated 2026-03-26 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-02-15, action code WQ, amount $126.55.
D9 (clearinghouse claim number): TRC64552398.
Trace (2 (referenced transaction trace)): TRC64552398.
received date (050): 2026-02-15.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: FRANK JONES; MI (member ID) KUL147221914.
Acknowledgment reference ACK64552398, dated 2026-02-15 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-02-06. Dx: Pain in right shoulder. 97110 (14 min): therapeutic exercise for strength and ROM. 97112 (15 min): neuromuscular re-education of movement and balance. 97140 (14 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 43. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1650284917, interchange 925581801 date 260326 time 0800 version 00501 usage P; group HS control 925581801 date 20260326 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1650284917 to receiver [ZZ] 1801579548, interchange 202633919 date 260326 time 0800 version 00501 usage P; group HB control 202633919 date 20260326 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 17
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1650284917, interchange 351229316 date 260213 time 0800 version 00501 usage P; group HC control 351229316 date 20260213 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 679143517 date 260215 time 0800 version 00501 usage P; group HN control 679143517 date 20260215 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1650284917 to receiver [ZZ] 1801579548, interchange 453998439 date 260325 time 0800 version 00501 usage P; group HP control 453998439 date 20260325 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
