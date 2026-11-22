# Case MOH2-000698

Patient RICHARD WILLIAMS, DOB 1966-06-08, sex F, member ID YTT780931716. Payer: DELAWARE VALLEY MUTUAL. Service date 2026-01-23.

## Adjudication outcome (835)
Claim PA25101145: status 4 (denied). Billed $137.18, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2604495957864, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-02-13.
Payer [PR]: DELAWARE VALLEY MUTUAL; 900 SHIPLEY RD; WILMINGTON, DE, 198033012; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT342142947, originator 1155019382.
claim statement period start (232): 2026-01-23.
Outpatient adjudication remarks (MOA): M77 (missing/incomplete/invalid place of service).
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 | $87.29 | $0 | CO-5 (Contractual Obligation: procedure code/type of bill is inconsistent with the place of service) $87.29 |  |
| 2 | 97112-GP | 1 | $49.89 | $0 | CO-5 (Contractual Obligation: procedure code/type of bill is inconsistent with the place of service) $49.89 |  |

Line item control numbers (REF 6R): PA25101145L1, PA25101145L2.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: RICHARD WILLIAMS; MI (member ID) YTT780931716; rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142.

## Claim as billed (837P)
Claim PA25101145, total charge $137.18, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25562 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 UN | $87.29 | 2026-01-23 | 1 | PA25101145L1 |
| 2 | 97112-GP | 1 UN | $49.89 | 2026-01-23 | 1 | PA25101145L2 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: DELAWARE VALLEY MUTUAL; 46 (ETIN) 1550193826
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: RICHARD WILLIAMS; MI (member ID) YTT780931716; 2005 CHESTNUT RD; PHILADELPHIA, PA, 19136
- payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826
- referring provider [DN]: DANIEL OKAFOR; XX (NPI) 1230067602
- rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142
- Submission reference TRC18864145, dated 2026-01-28 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-01-23.
Inquiry parties: payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: RICHARD WILLIAMS; MI (member ID) YTT780931716.
Subject DOB 1966-06-08, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: DELAWARE VALLEY MUTUAL POS
- plan date (291): 2026-01-23
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: RICHARD WILLIAMS; MI (member ID) YTT780931716.
Subject DOB 1966-06-08, sex F.
Eligibility exchange reference ELG51872913, dated 2026-02-17 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-01-28, action code WQ, amount $137.18.
D9 (clearinghouse claim number): TRC18864145.
Trace (2 (referenced transaction trace)): TRC18864145.
received date (050): 2026-01-28.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: RICHARD WILLIAMS; MI (member ID) YTT780931716.
Acknowledgment reference ACK18864145, dated 2026-01-28 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-01-23. Dx: Pain in left knee. 97110 (31 min): therapeutic exercise for strength and ROM. 97112 (15 min): neuromuscular re-education of movement and balance. Total timed minutes: 46. Telehealth encounter (synchronous audio/video); patient participated from home and verbal consent was documented. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1550193826, interchange 437086030 date 260217 time 0800 version 00501 usage P; group HS control 437086030 date 20260217 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1550193826 to receiver [ZZ] 1801579548, interchange 787849481 date 260217 time 0800 version 00501 usage P; group HB control 787849481 date 20260217 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1550193826, interchange 359141203 date 260128 time 0800 version 00501 usage P; group HC control 359141203 date 20260128 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 398731611 date 260128 time 0800 version 00501 usage P; group HN control 398731611 date 20260128 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1550193826 to receiver [ZZ] 1801579548, interchange 342142947 date 260213 time 0800 version 00501 usage P; group HP control 342142947 date 20260213 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 27
