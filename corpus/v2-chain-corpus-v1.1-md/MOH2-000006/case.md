# Case MOH2-000006

Patient KAREN SMITH, DOB 1953-04-17, sex M, member ID 1WG1UG7KV90. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-08-09.

## Adjudication outcome (835)
Claim PA21318021: status 4 (denied). Billed $117.27, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2625075459382, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-09-07.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT569488026, originator 1184634935.
claim statement period start (232): 2026-08-09.
Outpatient adjudication remarks (MOA): N435 (exceeds number/frequency approved or allowed within time period).
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97140-GP | 2 | $79.35 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $79.35 |  |
| 2 | 97110-GP | 1 | $37.92 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $37.92 |  |

Line item control numbers (REF 6R): PA21318021L1, PA21318021L2.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: KAREN SMITH; MI (member ID) 1WG1UG7KV90; rendering provider [82]: RUTH TAYLOR; XX (NPI) 1780053473.

## Claim as billed (837P)
Claim PA21318021, total charge $117.27, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: S335XXD (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97140-GP | 2 UN | $79.35 | 2026-08-09 | 1 | PA21318021L1 |
| 2 | 97110-GP | 1 UN | $37.92 | 2026-08-09 | 1 | PA21318021L2 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: KAREN SMITH; MI (member ID) 1WG1UG7KV90; 2162 FRANKLIN LN; TRENTON, NJ, 08687
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: PRIYA NAIR; XX (NPI) 1903307855
- rendering provider [82]: RUTH TAYLOR; XX (NPI) 1780053473
- Submission reference TRC24475156, dated 2026-08-24 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-08-09.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: KAREN SMITH; MI (member ID) 1WG1UG7KV90.
Subject DOB 1953-04-17, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-08-09
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: KAREN SMITH; MI (member ID) 1WG1UG7KV90.
Subject DOB 1953-04-17, sex M.
Eligibility exchange reference ELG26891182, dated 2026-09-12 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-08-26, action code WQ, amount $117.27.
D9 (clearinghouse claim number): TRC24475156.
Trace (2 (referenced transaction trace)): TRC24475156.
received date (050): 2026-08-26.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: KAREN SMITH; MI (member ID) 1WG1UG7KV90.
Acknowledgment reference ACK24475156, dated 2026-08-26 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-08-09. Dx: Sprain of ligaments of lumbar spine subsequent encounter. 97140 (30 min): manual therapy (soft tissue and joint mobilization). 97110 (16 min): therapeutic exercise for strength and ROM. Total timed minutes: 46. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1846349352, interchange 609427339 date 260912 time 0800 version 00501 usage P; group HS control 609427339 date 20260912 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1801579548, interchange 976615392 date 260912 time 0800 version 00501 usage P; group HB control 976615392 date 20260912 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1846349352, interchange 713538807 date 260824 time 0800 version 00501 usage P; group HC control 713538807 date 20260824 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 791751188 date 260826 time 0800 version 00501 usage P; group HN control 791751188 date 20260826 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1801579548, interchange 569488026 date 260907 time 0800 version 00501 usage P; group HP control 569488026 date 20260907 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 27
