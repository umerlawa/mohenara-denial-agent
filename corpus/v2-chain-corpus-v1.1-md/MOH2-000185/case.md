# Case MOH2-000185

Patient MARY PEREZ, DOB 1997-04-18, sex M, member ID YRC248453180. Payer: LIBERTY BELL HEALTH PLANS. Service date 2024-06-26.

## Adjudication outcome (835)
Claim PA26166941: status 4 (denied). Billed $127.36, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2508061484566, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2025-03-21.
Payer [PR]: LIBERTY BELL HEALTH PLANS; 1650 ARCH ST; PHILADELPHIA, PA, 191032097; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT167301305, originator 1135091827.
claim statement period start (232): 2024-06-26.
Outpatient adjudication remarks (MOA): N211 (you may not appeal this decision).
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97150-GP | 1 | $30.55 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $30.55 |  |
| 2 | 97530-GP-59 | 2 | $96.81 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $96.81 |  |

Line item control numbers (REF 6R): PA26166941L1, PA26166941L2.
Modifiers on remit lines: 59 (distinct procedural service), GP (under PT plan of care).
Remit claim parties: patient [QC]: MARY PEREZ; MI (member ID) YRC248453180; rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142.

## Claim as billed (837P)
Claim PA26166941, total charge $127.36, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: S43401D (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97150-GP | 1 UN | $30.55 | 2024-06-26 | 1 | PA26166941L1 |
| 2 | 97530-GP-59 | 2 UN | $96.81 | 2024-06-26 | 1 | PA26166941L2 |

Modifiers on claim: 59 (distinct procedural service), GP (under PT plan of care).

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: LIBERTY BELL HEALTH PLANS; 46 (ETIN) 1350918273
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: MARY PEREZ; MI (member ID) YRC248453180; 8923 FRANKLIN ST; WILMINGTON, DE, 19806
- payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273
- referring provider [DN]: MARCUS WEBB; XX (NPI) 1583494452
- rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142
- Submission reference TRC63961869, dated 2025-03-05 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2024-06-26.
Inquiry parties: payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: MARY PEREZ; MI (member ID) YRC248453180.
Subject DOB 1997-04-18, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: LIBERTY BELL HEALTH PLANS POS
- plan date (291): 2024-06-26
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: MARY PEREZ; MI (member ID) YRC248453180.
Subject DOB 1997-04-18, sex M.
Eligibility exchange reference ELG51488018, dated 2025-03-25 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2024-07-14, action code WQ, amount $127.36.
D9 (clearinghouse claim number): TRC63961869.
Trace (2 (referenced transaction trace)): TRC63961869.
received date (050): 2024-07-14.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: MARY PEREZ; MI (member ID) YRC248453180.
Acknowledgment reference ACK63961869, dated 2024-07-14 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2024-06-26. Dx: Unspecified sprain of right shoulder joint subsequent encounter. 97150 (untimed, 1 unit): group therapeutic procedure. 97530 (29 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 29. 97530 was rendered as an independent service from 97150 — separate start/stop times were recorded and a different body region was treated. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1350918273, interchange 659267278 date 250325 time 0800 version 00501 usage P; group HS control 659267278 date 20250325 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1350918273 to receiver [ZZ] 1801579548, interchange 854645753 date 250325 time 0800 version 00501 usage P; group HB control 854645753 date 20250325 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1350918273, interchange 407491791 date 250305 time 0800 version 00501 usage P; group HC control 407491791 date 20250305 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 975029731 date 240714 time 0800 version 00501 usage P; group HN control 975029731 date 20240714 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1350918273 to receiver [ZZ] 1801579548, interchange 167301305 date 250321 time 0800 version 00501 usage P; group HP control 167301305 date 20250321 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 27
