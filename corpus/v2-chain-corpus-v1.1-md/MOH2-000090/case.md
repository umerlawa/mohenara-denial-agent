# Case MOH2-000090

Patient SAMUEL LOPEZ, DOB 1965-11-13, sex F, member ID MTA297421990. Payer: DELAWARE VALLEY MUTUAL. Service date 2026-05-23.

## Adjudication outcome (835)
Claim PA24241740: status 4 (denied). Billed $180.06, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2622849644497, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-08-16.
Payer [PR]: DELAWARE VALLEY MUTUAL; 900 SHIPLEY RD; WILMINGTON, DE, 198033012; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT552516654, originator 1155019382.
claim statement period start (232): 2026-05-23.
Outpatient adjudication remarks (MOA): N111 (no appeal right except duplicate claim/service issue).
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $49.4 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $49.4 |  |
| 2 | 97112-GP | 1 | $47.57 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $47.57 |  |
| 3 | 97140-GP | 2 | $83.09 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $83.09 |  |

Line item control numbers (REF 6R): PA24241740L1, PA24241740L2, PA24241740L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: SAMUEL LOPEZ; MI (member ID) MTA297421990; rendering provider [82]: DOROTHY LOPEZ; XX (NPI) 1390221007.

## Claim as billed (837P)
Claim PA24241740, total charge $180.06, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M1712 (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $49.4 | 2026-05-23 | 1 | PA24241740L1 |
| 2 | 97112-GP | 1 UN | $47.57 | 2026-05-23 | 1 | PA24241740L2 |
| 3 | 97140-GP | 2 UN | $83.09 | 2026-05-23 | 1 | PA24241740L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: DELAWARE VALLEY MUTUAL; 46 (ETIN) 1550193826
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: SAMUEL LOPEZ; MI (member ID) MTA297421990; 1544 LINCOLN ST; STATEN ISLAND, NY, 10368
- payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826
- referring provider [DN]: THOMAS BERGSTROM; XX (NPI) 1179655839
- rendering provider [82]: DOROTHY LOPEZ; XX (NPI) 1390221007
- Submission reference TRC86478052, dated 2026-07-24 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-05-23.
Inquiry parties: payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: SAMUEL LOPEZ; MI (member ID) MTA297421990.
Subject DOB 1965-11-13, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: DELAWARE VALLEY MUTUAL EPO
- plan date (291): 2026-05-23
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: SAMUEL LOPEZ; MI (member ID) MTA297421990.
Subject DOB 1965-11-13, sex F.
Eligibility exchange reference ELG33600783, dated 2026-08-19 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-07-24, action code WQ, amount $180.06.
D9 (clearinghouse claim number): TRC86478052.
Trace (2 (referenced transaction trace)): TRC86478052.
received date (050): 2026-07-24.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: SAMUEL LOPEZ; MI (member ID) MTA297421990.
Acknowledgment reference ACK86478052, dated 2026-07-24 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-05-23. Dx: Unilateral primary osteoarthritis left knee. 97110 (16 min): therapeutic exercise for strength and ROM. 97112 (15 min): neuromuscular re-education of movement and balance. 97140 (29 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 60. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1550193826, interchange 922587556 date 260819 time 0800 version 00501 usage P; group HS control 922587556 date 20260819 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1550193826 to receiver [ZZ] 1801579548, interchange 594532047 date 260819 time 0800 version 00501 usage P; group HB control 594532047 date 20260819 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1550193826, interchange 581097883 date 260724 time 0800 version 00501 usage P; group HC control 581097883 date 20260724 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 493568712 date 260724 time 0800 version 00501 usage P; group HN control 493568712 date 20260724 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1550193826 to receiver [ZZ] 1801579548, interchange 552516654 date 260816 time 0800 version 00501 usage P; group HP control 552516654 date 20260816 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
