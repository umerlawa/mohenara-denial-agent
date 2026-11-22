# Case MOH2-000224

Patient MARY PEREZ, DOB 1997-04-18, sex M, member ID YRC248453180. Payer: LIBERTY BELL HEALTH PLANS. Service date 2024-07-07.

## Adjudication outcome (835)
Claim PA26359384: status 1 (processed as primary, paid). Billed $173.18, paid $92.72, patient responsibility $23.17. Filing indicator CI (commercial insurance). Payer claim control 2422374918960, POS 11 (office), frequency 1 (original claim).
Payment: $92.72 by CHK (check), handling I.
production date (405): 2024-08-10.
Payer [PR]: LIBERTY BELL HEALTH PLANS; 1650 ARCH ST; PHILADELPHIA, PA, 191032097; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT913941793, originator 1135091827.
claim statement period start (232): 2024-07-07.
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97112-GP | 1 | $50.73 | $26.18 allowed (B6) $32.73 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $18; PR-2 (Patient Responsibility: coinsurance amount) $6.55 |  |
| 2 | 97140-GP | 1 | $37.47 | $22.18 allowed (B6) $27.72 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $9.75; PR-2 (Patient Responsibility: coinsurance amount) $5.54 |  |
| 3 | 97140-GP | 1 | $46.38 | $22.18 allowed (B6) $27.72 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $18.66; PR-2 (Patient Responsibility: coinsurance amount) $5.54 |  |
| 4 | 97140-GP | 1 | $38.6 | $22.18 allowed (B6) $27.72 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $10.88; PR-2 (Patient Responsibility: coinsurance amount) $5.54 |  |

Line item control numbers (REF 6R): PA26359384L1, PA26359384L2, PA26359384L3, PA26359384L4.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: MARY PEREZ; MI (member ID) YRC248453180; rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142.

## Claim as billed (837P)
Claim PA26359384, total charge $173.18, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: S43401D (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97112-GP | 1 UN | $50.73 | 2024-07-07 | 1 | PA26359384L1 |
| 2 | 97140-GP | 1 UN | $37.47 | 2024-07-07 | 1 | PA26359384L2 |
| 3 | 97140-GP | 1 UN | $46.38 | 2024-07-07 | 1 | PA26359384L3 |
| 4 | 97140-GP | 1 UN | $38.6 | 2024-07-07 | 1 | PA26359384L4 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: LIBERTY BELL HEALTH PLANS; 46 (ETIN) 1350918273
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: MARY PEREZ; MI (member ID) YRC248453180; 8923 FRANKLIN ST; WILMINGTON, DE, 19806
- payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273
- referring provider [DN]: MARCUS WEBB; XX (NPI) 1583494452
- rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142
- Submission reference TRC28481958, dated 2024-07-25 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2024-07-07.
Inquiry parties: payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: MARY PEREZ; MI (member ID) YRC248453180.
Subject DOB 1997-04-18, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: LIBERTY BELL HEALTH PLANS POS
- plan date (291): 2024-07-07
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: MARY PEREZ; MI (member ID) YRC248453180.
Subject DOB 1997-04-18, sex M.
Eligibility exchange reference ELG95617343, dated 2024-08-13 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2024-07-25, action code WQ, amount $173.18.
D9 (clearinghouse claim number): TRC28481958.
Trace (2 (referenced transaction trace)): TRC28481958.
received date (050): 2024-07-25.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: MARY PEREZ; MI (member ID) YRC248453180.
Acknowledgment reference ACK28481958, dated 2024-07-25 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2024-07-07. Dx: Unspecified sprain of right shoulder joint subsequent encounter. 97112 (15 min): neuromuscular re-education of movement and balance. 97140 (15 min): manual therapy (soft tissue and joint mobilization). 97140 (16 min): manual therapy (soft tissue and joint mobilization). 97140 (14 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 60. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1350918273, interchange 881713770 date 240813 time 0800 version 00501 usage P; group HS control 881713770 date 20240813 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1350918273 to receiver [ZZ] 1801579548, interchange 382739407 date 240813 time 0800 version 00501 usage P; group HB control 382739407 date 20240813 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1350918273, interchange 909995120 date 240725 time 0800 version 00501 usage P; group HC control 909995120 date 20240725 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 38
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 565514886 date 240725 time 0800 version 00501 usage P; group HN control 565514886 date 20240725 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1350918273 to receiver [ZZ] 1801579548, interchange 913941793 date 240810 time 0800 version 00501 usage P; group HP control 913941793 date 20240810 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 42
