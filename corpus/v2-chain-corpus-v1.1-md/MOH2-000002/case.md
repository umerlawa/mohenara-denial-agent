# Case MOH2-000002

Patient RICHARD WILLIAMS, DOB 1966-06-08, sex F, member ID YTT780931716. Payer: DELAWARE VALLEY MUTUAL. Service date 2026-06-11.

## Adjudication outcome (835)
Claim PA24228780: status 4 (denied). Billed $187.53, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2618694259766, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-07-05.
Payer [PR]: DELAWARE VALLEY MUTUAL; 900 SHIPLEY RD; WILMINGTON, DE, 198033012; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT447825085, originator 1155019382.
claim statement period start (232): 2026-06-11.
Outpatient adjudication remarks (MOA): N30 (patient ineligible for this service).
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97530-GP | 1 | $57.07 | $0 | CO-27 (Contractual Obligation: expenses incurred after coverage terminated) $57.07 |  |
| 2 | 97530-GP | 1 | $49.38 | $0 | CO-27 (Contractual Obligation: expenses incurred after coverage terminated) $49.38 |  |
| 3 | 97140-GP | 2 | $81.08 | $0 | CO-27 (Contractual Obligation: expenses incurred after coverage terminated) $81.08 |  |

Line item control numbers (REF 6R): PA24228780L1, PA24228780L2, PA24228780L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: RICHARD WILLIAMS; MI (member ID) YTT780931716; rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142.

## Claim as billed (837P)
Claim PA24228780, total charge $187.53, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25562 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97530-GP | 1 UN | $57.07 | 2026-06-11 | 1 | PA24228780L1 |
| 2 | 97530-GP | 1 UN | $49.38 | 2026-06-11 | 1 | PA24228780L2 |
| 3 | 97140-GP | 2 UN | $81.08 | 2026-06-11 | 1 | PA24228780L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: DELAWARE VALLEY MUTUAL; 46 (ETIN) 1550193826
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: RICHARD WILLIAMS; MI (member ID) YTT780931716; 2005 CHESTNUT RD; PHILADELPHIA, PA, 19136
- payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826
- referring provider [DN]: DANIEL OKAFOR; XX (NPI) 1230067602
- rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142
- Submission reference TRC71730515, dated 2026-06-21 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-06-11.
Inquiry parties: payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: RICHARD WILLIAMS; MI (member ID) YTT780931716.
Subject DOB 1966-06-08, sex F.

Response:
- benefit: 6 (inactive), coverage level IND, service type 30 (health benefit plan coverage), plan: DELAWARE VALLEY MUTUAL POS
- plan date (291): 2026-06-11
- eligibility begin (356): 2024-01-01
- eligibility end (357): 2026-05-31
Response parties: payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: RICHARD WILLIAMS; MI (member ID) YTT780931716.
Subject DOB 1966-06-08, sex F.
Eligibility exchange reference ELG52444131, dated 2026-07-08 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-06-21, action code WQ, amount $187.53.
D9 (clearinghouse claim number): TRC71730515.
Trace (2 (referenced transaction trace)): TRC71730515.
received date (050): 2026-06-21.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: RICHARD WILLIAMS; MI (member ID) YTT780931716.
Acknowledgment reference ACK71730515, dated 2026-06-21 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-06-11. Dx: Pain in left knee. 97530 (16 min): therapeutic activities (dynamic functional tasks). 97530 (16 min): therapeutic activities (dynamic functional tasks). 97140 (29 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 61. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1550193826, interchange 592671540 date 260708 time 0800 version 00501 usage P; group HS control 592671540 date 20260708 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1550193826 to receiver [ZZ] 1801579548, interchange 274778698 date 260708 time 0800 version 00501 usage P; group HB control 274778698 date 20260708 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 14
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1550193826, interchange 247528526 date 260621 time 0800 version 00501 usage P; group HC control 247528526 date 20260621 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 778349724 date 260621 time 0800 version 00501 usage P; group HN control 778349724 date 20260621 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1550193826 to receiver [ZZ] 1801579548, interchange 447825085 date 260705 time 0800 version 00501 usage P; group HP control 447825085 date 20260705 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
