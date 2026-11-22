# Case MOH2-000624

Patient KAREN SMITH, DOB 1953-04-17, sex M, member ID QVV207439567. Payer: ATLANTIC SHORE ASSURANCE. Service date 2026-07-16.

## Adjudication outcome (835)
Claim PA23218186: status 4 (denied). Billed $231.49, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2622644876424, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-08-14.
Payer [PR]: ATLANTIC SHORE ASSURANCE; 3499 ROUTE 9 N; FREEHOLD, NJ, 077283100; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT145183606, originator 1125037465.
claim statement period start (232): 2026-07-16.
Outpatient adjudication remarks (MOA): MA04 (secondary payment cannot be considered without primary payer identity).
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97112-GP | 1 | $50.12 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $50.12 |  |
| 2 | 97530-GP | 2 | $125.27 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $125.27 |  |
| 3 | 97530-GP | 1 | $56.1 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $56.1 |  |

Line item control numbers (REF 6R): PA23218186L1, PA23218186L2, PA23218186L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: KAREN SMITH; MI (member ID) QVV207439567; rendering provider [82]: RUTH TAYLOR; XX (NPI) 1780053473.

## Claim as billed (837P)
Claim PA23218186, total charge $231.49, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: S335XXD (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97112-GP | 1 UN | $50.12 | 2026-07-16 | 1 | PA23218186L1 |
| 2 | 97530-GP | 2 UN | $125.27 | 2026-07-16 | 1 | PA23218186L2 |
| 3 | 97530-GP | 1 UN | $56.1 | 2026-07-16 | 1 | PA23218186L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: ATLANTIC SHORE ASSURANCE; 46 (ETIN) 1250374659
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: KAREN SMITH; MI (member ID) QVV207439567; 2162 FRANKLIN LN; TRENTON, NJ, 08687
- payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659
- referring provider [DN]: PRIYA NAIR; XX (NPI) 1903307855
- rendering provider [82]: RUTH TAYLOR; XX (NPI) 1780053473
- Submission reference TRC53824930, dated 2026-07-23 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-07-16.
Inquiry parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: KAREN SMITH; MI (member ID) QVV207439567.
Subject DOB 1953-04-17, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: ATLANTIC SHORE ASSURANCE PPO
- benefit: R (other or additional payer), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-07-16
- eligibility begin (356): 2024-01-01
- eligibility begin (356): 2024-01-01
- payer message: PLAN IS PRIMARY PAYER FOR THIS MEMBER
Response parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: KAREN SMITH; MI (member ID) QVV207439567; payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352.
Subject DOB 1953-04-17, sex M.
Eligibility exchange reference ELG42040308, dated 2026-08-15 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-07-23, action code WQ, amount $231.49.
D9 (clearinghouse claim number): TRC53824930.
Trace (2 (referenced transaction trace)): TRC53824930.
received date (050): 2026-07-23.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: KAREN SMITH; MI (member ID) QVV207439567.
Acknowledgment reference ACK53824930, dated 2026-07-23 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-07-16. Dx: Sprain of ligaments of lumbar spine subsequent encounter. 97112 (14 min): neuromuscular re-education of movement and balance. 97530 (31 min): therapeutic activities (dynamic functional tasks). 97530 (14 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 59. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1250374659, interchange 556663316 date 260815 time 0800 version 00501 usage P; group HS control 556663316 date 20260815 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1250374659 to receiver [ZZ] 1801579548, interchange 527180333 date 260815 time 0800 version 00501 usage P; group HB control 527180333 date 20260815 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 17
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1250374659, interchange 171288647 date 260723 time 0800 version 00501 usage P; group HC control 171288647 date 20260723 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 243530199 date 260723 time 0800 version 00501 usage P; group HN control 243530199 date 20260723 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1250374659 to receiver [ZZ] 1801579548, interchange 145183606 date 260814 time 0800 version 00501 usage P; group HP control 145183606 date 20260814 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
