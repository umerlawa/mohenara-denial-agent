# Case MOH2-000143

Patient MARY PEREZ, DOB 1997-04-18, sex M, member ID YRC248453180. Payer: LIBERTY BELL HEALTH PLANS. Service date 2024-07-13.

## Adjudication outcome (835)
Claim PA25485217: status 4 (denied). Billed $156.05, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2510639922761, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2025-04-16.
Payer [PR]: LIBERTY BELL HEALTH PLANS; 1650 ARCH ST; PHILADELPHIA, PA, 191032097; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT474553686, originator 1135091827.
claim statement period start (232): 2024-07-13.
Outpatient adjudication remarks (MOA): N211 (you may not appeal this decision).
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97140-GP | 2 | $79.68 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $79.68 |  |
| 2 | 97140-GP | 1 | $36.82 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $36.82 |  |
| 3 | 97140-GP | 1 | $39.55 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $39.55 |  |

Line item control numbers (REF 6R): PA25485217L1, PA25485217L2, PA25485217L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: MARY PEREZ; MI (member ID) YRC248453180; rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142.

## Claim as billed (837P)
Claim PA25485217, total charge $156.05, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: S43401D (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97140-GP | 2 UN | $79.68 | 2024-07-13 | 1 | PA25485217L1 |
| 2 | 97140-GP | 1 UN | $36.82 | 2024-07-13 | 1 | PA25485217L2 |
| 3 | 97140-GP | 1 UN | $39.55 | 2024-07-13 | 1 | PA25485217L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: LIBERTY BELL HEALTH PLANS; 46 (ETIN) 1350918273
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: MARY PEREZ; MI (member ID) YRC248453180; 8923 FRANKLIN ST; WILMINGTON, DE, 19806
- payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273
- referring provider [DN]: MARCUS WEBB; XX (NPI) 1583494452
- rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142
- Submission reference TRC59398832, dated 2025-03-30 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2024-07-13.
Inquiry parties: payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: MARY PEREZ; MI (member ID) YRC248453180.
Subject DOB 1997-04-18, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: LIBERTY BELL HEALTH PLANS POS
- plan date (291): 2024-07-13
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: MARY PEREZ; MI (member ID) YRC248453180.
Subject DOB 1997-04-18, sex M.
Eligibility exchange reference ELG34726988, dated 2025-04-20 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2024-07-18, action code WQ, amount $156.05.
D9 (clearinghouse claim number): TRC59398832.
Trace (2 (referenced transaction trace)): TRC59398832.
received date (050): 2024-07-18.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: MARY PEREZ; MI (member ID) YRC248453180.
Acknowledgment reference ACK59398832, dated 2024-07-18 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2024-07-13. Dx: Unspecified sprain of right shoulder joint subsequent encounter. 97140 (29 min): manual therapy (soft tissue and joint mobilization). 97140 (16 min): manual therapy (soft tissue and joint mobilization). 97140 (16 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 61. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1350918273, interchange 833642865 date 250420 time 0800 version 00501 usage P; group HS control 833642865 date 20250420 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1350918273 to receiver [ZZ] 1801579548, interchange 138379974 date 250420 time 0800 version 00501 usage P; group HB control 138379974 date 20250420 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1350918273, interchange 148634661 date 250330 time 0800 version 00501 usage P; group HC control 148634661 date 20250330 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 672310343 date 240718 time 0800 version 00501 usage P; group HN control 672310343 date 20240718 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1350918273 to receiver [ZZ] 1801579548, interchange 474553686 date 250416 time 0800 version 00501 usage P; group HP control 474553686 date 20250416 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
