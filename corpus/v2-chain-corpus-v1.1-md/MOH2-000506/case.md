# Case MOH2-000506

Patient KAREN SMITH, DOB 1953-04-17, sex M, member ID 1WG1UG7KV90. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-02-14.

## Adjudication outcome (835)
Claim PA25630385: status 4 (denied). Billed $232.43, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2607416506886, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-03-15.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT828231500, originator 1184634935.
claim statement period start (232): 2026-02-14.
Outpatient adjudication remarks (MOA): N286 (missing/incomplete/invalid referring provider primary identifier).
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 | $96.38 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $96.38 |  |
| 2 | 97140-GP | 2 | $87.83 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $87.83 |  |
| 3 | 97530-GP | 1 | $48.22 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $48.22 |  |

Line item control numbers (REF 6R): PA25630385L1, PA25630385L2, PA25630385L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: KAREN SMITH; MI (member ID) 1WG1UG7KV90; rendering provider [82]: RUTH TAYLOR; XX (NPI) 1780053473.

## Claim as billed (837P)
Claim PA25630385, total charge $232.43, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: S335XXD (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 UN | $96.38 | 2026-02-14 | 1 | PA25630385L1 |
| 2 | 97140-GP | 2 UN | $87.83 | 2026-02-14 | 1 | PA25630385L2 |
| 3 | 97530-GP | 1 UN | $48.22 | 2026-02-14 | 1 | PA25630385L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: KAREN SMITH; MI (member ID) 1WG1UG7KV90; 2162 FRANKLIN LN; TRENTON, NJ, 08687
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- rendering provider [82]: RUTH TAYLOR; XX (NPI) 1780053473
- Submission reference TRC81626889, dated 2026-02-20 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-02-14.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: KAREN SMITH; MI (member ID) 1WG1UG7KV90.
Subject DOB 1953-04-17, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-02-14
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: KAREN SMITH; MI (member ID) 1WG1UG7KV90.
Subject DOB 1953-04-17, sex M.
Eligibility exchange reference ELG94756233, dated 2026-03-20 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-02-20, action code WQ, amount $232.43.
D9 (clearinghouse claim number): TRC81626889.
Trace (2 (referenced transaction trace)): TRC81626889.
received date (050): 2026-02-20.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: KAREN SMITH; MI (member ID) 1WG1UG7KV90.
Acknowledgment reference ACK81626889, dated 2026-02-20 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-02-14. Dx: Sprain of ligaments of lumbar spine subsequent encounter. 97110 (29 min): therapeutic exercise for strength and ROM. 97140 (30 min): manual therapy (soft tissue and joint mobilization). 97530 (16 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 75. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1846349352, interchange 437479695 date 260320 time 0800 version 00501 usage P; group HS control 437479695 date 20260320 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1801579548, interchange 752050490 date 260320 time 0800 version 00501 usage P; group HB control 752050490 date 20260320 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1846349352, interchange 235820389 date 260220 time 0800 version 00501 usage P; group HC control 235820389 date 20260220 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 33
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 902059705 date 260220 time 0800 version 00501 usage P; group HN control 902059705 date 20260220 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1801579548, interchange 828231500 date 260315 time 0800 version 00501 usage P; group HP control 828231500 date 20260315 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
