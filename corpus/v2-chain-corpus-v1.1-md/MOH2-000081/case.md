# Case MOH2-000081

Patient MARY PEREZ, DOB 1997-04-18, sex M, member ID YRC248453180. Payer: LIBERTY BELL HEALTH PLANS. Service date 2024-06-19.

## Adjudication outcome (835)
Claim PA23733599: status 1 (processed as primary, paid). Billed $255.24, paid $110.88, patient responsibility $27.72. Filing indicator CI (commercial insurance). Payer claim control 2419935721000, POS 11 (office), frequency 1 (original claim).
Payment: $110.88 by CHK (check), handling I.
production date (405): 2024-07-17.
Payer [PR]: LIBERTY BELL HEALTH PLANS; 1650 ARCH ST; PHILADELPHIA, PA, 191032097; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT494529441, originator 1135091827.
claim statement period start (232): 2024-06-19.
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97750-GP | 1 | $46.3 | $0 | CO-97 (Contractual Obligation: payment included in the allowance for another service, bundled) $46.3 | HE N20 (service not payable with other service rendered on the same date) |
| 2 | 97140-GP | 2 | $73.61 | $44.35 allowed (B6) $55.44 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $18.17; PR-2 (Patient Responsibility: coinsurance amount) $11.09 |  |
| 3 | 97140-GP | 2 | $94.71 | $44.35 allowed (B6) $55.44 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $39.27; PR-2 (Patient Responsibility: coinsurance amount) $11.09 |  |
| 4 | 97140-GP | 1 | $40.62 | $22.18 allowed (B6) $27.72 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $12.9; PR-2 (Patient Responsibility: coinsurance amount) $5.54 |  |

Line item control numbers (REF 6R): PA23733599L1, PA23733599L2, PA23733599L3, PA23733599L4.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: MARY PEREZ; MI (member ID) YRC248453180; rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142.

## Claim as billed (837P)
Claim PA23733599, total charge $255.24, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: S43401D (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97750-GP | 1 UN | $46.3 | 2024-06-19 | 1 | PA23733599L1 |
| 2 | 97140-GP | 2 UN | $73.61 | 2024-06-19 | 1 | PA23733599L2 |
| 3 | 97140-GP | 2 UN | $94.71 | 2024-06-19 | 1 | PA23733599L3 |
| 4 | 97140-GP | 1 UN | $40.62 | 2024-06-19 | 1 | PA23733599L4 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: LIBERTY BELL HEALTH PLANS; 46 (ETIN) 1350918273
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: MARY PEREZ; MI (member ID) YRC248453180; 8923 FRANKLIN ST; WILMINGTON, DE, 19806
- payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273
- referring provider [DN]: MARCUS WEBB; XX (NPI) 1583494452
- rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142
- Submission reference TRC38331033, dated 2024-06-26 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2024-06-19.
Inquiry parties: payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: MARY PEREZ; MI (member ID) YRC248453180.
Subject DOB 1997-04-18, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: LIBERTY BELL HEALTH PLANS POS
- plan date (291): 2024-06-19
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: MARY PEREZ; MI (member ID) YRC248453180.
Subject DOB 1997-04-18, sex M.
Eligibility exchange reference ELG39269810, dated 2024-07-19 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2024-06-26, action code WQ, amount $255.24.
D9 (clearinghouse claim number): TRC38331033.
Trace (2 (referenced transaction trace)): TRC38331033.
received date (050): 2024-06-26.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: MARY PEREZ; MI (member ID) YRC248453180.
Acknowledgment reference ACK38331033, dated 2024-06-26 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2024-06-19. Dx: Unspecified sprain of right shoulder joint subsequent encounter. 97750 (15 min): physical performance test with written report. 97140 (30 min): manual therapy (soft tissue and joint mobilization). 97140 (30 min): manual therapy (soft tissue and joint mobilization). 97140 (16 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 91. Separate-session log: 97750 performed apart from 97140 with its own timed interval, distinct target region, and its own documented goal. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1350918273, interchange 426405534 date 240719 time 0800 version 00501 usage P; group HS control 426405534 date 20240719 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1350918273 to receiver [ZZ] 1801579548, interchange 906587679 date 240719 time 0800 version 00501 usage P; group HB control 906587679 date 20240719 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1350918273, interchange 398037295 date 240626 time 0800 version 00501 usage P; group HC control 398037295 date 20240626 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 38
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 254995923 date 240626 time 0800 version 00501 usage P; group HN control 254995923 date 20240626 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1350918273 to receiver [ZZ] 1801579548, interchange 494529441 date 240717 time 0800 version 00501 usage P; group HP control 494529441 date 20240717 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 41
