# Case MOH2-000647

Patient MARY PEREZ, DOB 1997-04-18, sex M, member ID YRC248453180. Payer: LIBERTY BELL HEALTH PLANS. Service date 2024-07-09.

## Adjudication outcome (835)
Claim PA27914477: status 1 (processed as primary, paid). Billed $333.7, paid $23.25, patient responsibility $5.81. Filing indicator CI (commercial insurance). Payer claim control 2424796802852, POS 11 (office), frequency 1 (original claim).
Payment: $23.25 by CHK (check), handling I.
production date (405): 2024-09-03.
Payer [PR]: LIBERTY BELL HEALTH PLANS; 1650 ARCH ST; PHILADELPHIA, PA, 191032097; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT298650473, originator 1135091827.
claim statement period start (232): 2024-07-09.
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $47.54 | $23.25 allowed (B6) $29.06 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $18.48; PR-2 (Patient Responsibility: coinsurance amount) $5.81 |  |
| 2 | 97116-GP | 7 | $286.16 | $0 | CO-151 (Contractual Obligation: information does not support this many/frequency of services) $286.16 | HE N362 (the number of days or units exceeds the acceptable maximum) |

Line item control numbers (REF 6R): PA27914477L1, PA27914477L2.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: MARY PEREZ; MI (member ID) YRC248453180; rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142.

## Claim as billed (837P)
Claim PA27914477, total charge $333.7, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: S43401D (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $47.54 | 2024-07-09 | 1 | PA27914477L1 |
| 2 | 97116-GP | 7 UN | $286.16 | 2024-07-09 | 1 | PA27914477L2 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: LIBERTY BELL HEALTH PLANS; 46 (ETIN) 1350918273
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: MARY PEREZ; MI (member ID) YRC248453180; 8923 FRANKLIN ST; WILMINGTON, DE, 19806
- payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273
- referring provider [DN]: MARCUS WEBB; XX (NPI) 1583494452
- rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142
- Submission reference TRC32482857, dated 2024-07-29 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2024-07-09.
Inquiry parties: payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: MARY PEREZ; MI (member ID) YRC248453180.
Subject DOB 1997-04-18, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: LIBERTY BELL HEALTH PLANS POS
- plan date (291): 2024-07-09
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: MARY PEREZ; MI (member ID) YRC248453180.
Subject DOB 1997-04-18, sex M.
Eligibility exchange reference ELG94328334, dated 2024-09-07 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2024-07-30, action code WQ, amount $333.7.
D9 (clearinghouse claim number): TRC32482857.
Trace (2 (referenced transaction trace)): TRC32482857.
received date (050): 2024-07-30.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: MARY PEREZ; MI (member ID) YRC248453180.
Acknowledgment reference ACK32482857, dated 2024-07-30 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2024-07-09. Dx: Unspecified sprain of right shoulder joint subsequent encounter. 97110 (14 min): therapeutic exercise for strength and ROM. 97116 (15 min): gait training with assistive device progression. Total timed minutes: 29. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1350918273, interchange 194975644 date 240907 time 0800 version 00501 usage P; group HS control 194975644 date 20240907 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1350918273 to receiver [ZZ] 1801579548, interchange 945117476 date 240907 time 0800 version 00501 usage P; group HB control 945117476 date 20240907 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1350918273, interchange 507205092 date 240729 time 0800 version 00501 usage P; group HC control 507205092 date 20240729 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 215365236 date 240730 time 0800 version 00501 usage P; group HN control 215365236 date 20240730 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1350918273 to receiver [ZZ] 1801579548, interchange 298650473 date 240903 time 0800 version 00501 usage P; group HP control 298650473 date 20240903 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 29
