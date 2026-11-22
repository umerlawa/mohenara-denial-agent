# Case MOH2-000452

Patient LINDA RAMIREZ, DOB 1950-10-18, sex M, member ID 7GC9QV7NJ56. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-02-08.

## Adjudication outcome (835)
Claim PA25247540: status 4 (denied). Billed $156.17, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2609641504752, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-04-06.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT400956971, originator 1184634935.
claim statement period start (232): 2026-02-08.
Outpatient adjudication remarks (MOA): N286 (missing/incomplete/invalid referring provider primary identifier).
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 | $76.7 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $76.7 |  |
| 2 | 97112-GP | 1 | $42.63 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $42.63 |  |
| 3 | 97140-GP | 1 | $36.84 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $36.84 |  |

Line item control numbers (REF 6R): PA25247540L1, PA25247540L2, PA25247540L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: LINDA RAMIREZ; MI (member ID) 7GC9QV7NJ56; rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142.

## Claim as billed (837P)
Claim PA25247540, total charge $156.17, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: S43401D (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 UN | $76.7 | 2026-02-08 | 1 | PA25247540L1 |
| 2 | 97112-GP | 1 UN | $42.63 | 2026-02-08 | 1 | PA25247540L2 |
| 3 | 97140-GP | 1 UN | $36.84 | 2026-02-08 | 1 | PA25247540L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: LINDA RAMIREZ; MI (member ID) 7GC9QV7NJ56; 4042 LINCOLN AVE; TRENTON, NJ, 08652
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142
- Submission reference TRC30254364, dated 2026-02-26 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-02-08.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: LINDA RAMIREZ; MI (member ID) 7GC9QV7NJ56.
Subject DOB 1950-10-18, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-02-08
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: LINDA RAMIREZ; MI (member ID) 7GC9QV7NJ56.
Subject DOB 1950-10-18, sex M.
Eligibility exchange reference ELG57967691, dated 2026-04-07 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-02-26, action code WQ, amount $156.17.
D9 (clearinghouse claim number): TRC30254364.
Trace (2 (referenced transaction trace)): TRC30254364.
received date (050): 2026-02-26.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: LINDA RAMIREZ; MI (member ID) 7GC9QV7NJ56.
Acknowledgment reference ACK30254364, dated 2026-02-26 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-02-08. Dx: Unspecified sprain of right shoulder joint subsequent encounter. 97110 (31 min): therapeutic exercise for strength and ROM. 97112 (14 min): neuromuscular re-education of movement and balance. 97140 (15 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 60. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1846349352, interchange 627612715 date 260407 time 0800 version 00501 usage P; group HS control 627612715 date 20260407 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1801579548, interchange 260808382 date 260407 time 0800 version 00501 usage P; group HB control 260808382 date 20260407 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1846349352, interchange 171802542 date 260226 time 0800 version 00501 usage P; group HC control 171802542 date 20260226 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 33
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 545986933 date 260226 time 0800 version 00501 usage P; group HN control 545986933 date 20260226 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1801579548, interchange 400956971 date 260406 time 0800 version 00501 usage P; group HP control 400956971 date 20260406 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
