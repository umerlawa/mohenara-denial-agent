# Case MOH2-000525

Patient KAREN SMITH, DOB 1953-04-17, sex M, member ID QVV207439567. Payer: ATLANTIC SHORE ASSURANCE. Service date 2026-01-12.

## Adjudication outcome (835)
Claim PA28727426: status 4 (denied). Billed $378.73, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2604613373082, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-02-15.
Payer [PR]: ATLANTIC SHORE ASSURANCE; 3499 ROUTE 9 N; FREEHOLD, NJ, 077283100; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT419813114, originator 1125037465.
claim statement period start (232): 2026-01-12.
Outpatient adjudication remarks (MOA): MA04 (secondary payment cannot be considered without primary payer identity).
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 | $79.73 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $79.73 |  |
| 2 | 97140-GP | 2 | $96.44 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $96.44 |  |
| 3 | 97530-GP | 2 | $109.78 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $109.78 |  |
| 4 | 97112-GP | 2 | $92.78 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $92.78 |  |

Line item control numbers (REF 6R): PA28727426L1, PA28727426L2, PA28727426L3, PA28727426L4.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: KAREN SMITH; MI (member ID) QVV207439567; rendering provider [82]: RUTH TAYLOR; XX (NPI) 1780053473.

## Claim as billed (837P)
Claim PA28727426, total charge $378.73, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: S335XXD (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 UN | $79.73 | 2026-01-12 | 1 | PA28727426L1 |
| 2 | 97140-GP | 2 UN | $96.44 | 2026-01-12 | 1 | PA28727426L2 |
| 3 | 97530-GP | 2 UN | $109.78 | 2026-01-12 | 1 | PA28727426L3 |
| 4 | 97112-GP | 2 UN | $92.78 | 2026-01-12 | 1 | PA28727426L4 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: ATLANTIC SHORE ASSURANCE; 46 (ETIN) 1250374659
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: KAREN SMITH; MI (member ID) QVV207439567; 2162 FRANKLIN LN; TRENTON, NJ, 08687
- payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659
- referring provider [DN]: PRIYA NAIR; XX (NPI) 1903307855
- rendering provider [82]: RUTH TAYLOR; XX (NPI) 1780053473
- Submission reference TRC50548214, dated 2026-01-25 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-01-12.
Inquiry parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: KAREN SMITH; MI (member ID) QVV207439567.
Subject DOB 1953-04-17, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: ATLANTIC SHORE ASSURANCE PPO
- benefit: R (other or additional payer), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-01-12
- eligibility begin (356): 2024-01-01
- eligibility begin (356): 2024-01-01
- payer message: PLAN IS PRIMARY PAYER FOR THIS MEMBER
Response parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: KAREN SMITH; MI (member ID) QVV207439567; payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352.
Subject DOB 1953-04-17, sex M.
Eligibility exchange reference ELG41333041, dated 2026-02-16 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-01-26, action code WQ, amount $378.73.
D9 (clearinghouse claim number): TRC50548214.
Trace (2 (referenced transaction trace)): TRC50548214.
received date (050): 2026-01-26.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: KAREN SMITH; MI (member ID) QVV207439567.
Acknowledgment reference ACK50548214, dated 2026-01-26 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-01-12. Dx: Sprain of ligaments of lumbar spine subsequent encounter. 97110 (31 min): therapeutic exercise for strength and ROM. 97140 (31 min): manual therapy (soft tissue and joint mobilization). 97530 (29 min): therapeutic activities (dynamic functional tasks). 97112 (29 min): neuromuscular re-education of movement and balance. Total timed minutes: 120. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1250374659, interchange 164777019 date 260216 time 0800 version 00501 usage P; group HS control 164777019 date 20260216 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1250374659 to receiver [ZZ] 1801579548, interchange 659738345 date 260216 time 0800 version 00501 usage P; group HB control 659738345 date 20260216 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 17
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1250374659, interchange 577923069 date 260125 time 0800 version 00501 usage P; group HC control 577923069 date 20260125 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 38
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 880288012 date 260126 time 0800 version 00501 usage P; group HN control 880288012 date 20260126 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1250374659 to receiver [ZZ] 1801579548, interchange 419813114 date 260215 time 0800 version 00501 usage P; group HP control 419813114 date 20260215 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 35
