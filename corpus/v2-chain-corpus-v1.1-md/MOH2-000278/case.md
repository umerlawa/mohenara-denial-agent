# Case MOH2-000278

Patient SAMUEL LOPEZ, DOB 1965-11-13, sex F, member ID MTA297421990. Payer: DELAWARE VALLEY MUTUAL. Service date 2026-06-05.

## Adjudication outcome (835)
Claim PA23422920: status 4 (denied). Billed $186.87, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2620828192714, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-07-27.
Payer [PR]: DELAWARE VALLEY MUTUAL; 900 SHIPLEY RD; WILMINGTON, DE, 198033012; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT549050382, originator 1155019382.
claim statement period start (232): 2026-06-05.
Outpatient adjudication remarks (MOA): N30 (patient ineligible for this service).
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $52.03 | $0 | CO-27 (Contractual Obligation: expenses incurred after coverage terminated) $52.03 |  |
| 2 | 97140-GP | 2 | $83.84 | $0 | CO-27 (Contractual Obligation: expenses incurred after coverage terminated) $83.84 |  |
| 3 | 97530-GP | 1 | $51 | $0 | CO-27 (Contractual Obligation: expenses incurred after coverage terminated) $51 |  |

Line item control numbers (REF 6R): PA23422920L1, PA23422920L2, PA23422920L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: SAMUEL LOPEZ; MI (member ID) MTA297421990; rendering provider [82]: DOROTHY LOPEZ; XX (NPI) 1390221007.

## Claim as billed (837P)
Claim PA23422920, total charge $186.87, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M1712 (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $52.03 | 2026-06-05 | 1 | PA23422920L1 |
| 2 | 97140-GP | 2 UN | $83.84 | 2026-06-05 | 1 | PA23422920L2 |
| 3 | 97530-GP | 1 UN | $51 | 2026-06-05 | 1 | PA23422920L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: DELAWARE VALLEY MUTUAL; 46 (ETIN) 1550193826
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: SAMUEL LOPEZ; MI (member ID) MTA297421990; 1544 LINCOLN ST; STATEN ISLAND, NY, 10368
- payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826
- referring provider [DN]: THOMAS BERGSTROM; XX (NPI) 1179655839
- rendering provider [82]: DOROTHY LOPEZ; XX (NPI) 1390221007
- Submission reference TRC72603366, dated 2026-06-17 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-06-05.
Inquiry parties: payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: SAMUEL LOPEZ; MI (member ID) MTA297421990.
Subject DOB 1965-11-13, sex F.

Response:
- benefit: 6 (inactive), coverage level IND, service type 30 (health benefit plan coverage), plan: DELAWARE VALLEY MUTUAL EPO
- plan date (291): 2026-06-05
- eligibility begin (356): 2024-01-01
- eligibility end (357): 2026-05-31
Response parties: payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: SAMUEL LOPEZ; MI (member ID) MTA297421990.
Subject DOB 1965-11-13, sex F.
Eligibility exchange reference ELG84732319, dated 2026-08-01 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-06-18, action code WQ, amount $186.87.
D9 (clearinghouse claim number): TRC72603366.
Trace (2 (referenced transaction trace)): TRC72603366.
received date (050): 2026-06-18.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: SAMUEL LOPEZ; MI (member ID) MTA297421990.
Acknowledgment reference ACK72603366, dated 2026-06-18 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-06-05. Dx: Unilateral primary osteoarthritis left knee. 97110 (15 min): therapeutic exercise for strength and ROM. 97140 (30 min): manual therapy (soft tissue and joint mobilization). 97530 (14 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 59. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1550193826, interchange 121678009 date 260801 time 0800 version 00501 usage P; group HS control 121678009 date 20260801 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1550193826 to receiver [ZZ] 1801579548, interchange 196270896 date 260801 time 0800 version 00501 usage P; group HB control 196270896 date 20260801 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 14
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1550193826, interchange 741799471 date 260617 time 0800 version 00501 usage P; group HC control 741799471 date 20260617 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 887191456 date 260618 time 0800 version 00501 usage P; group HN control 887191456 date 20260618 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1550193826 to receiver [ZZ] 1801579548, interchange 549050382 date 260727 time 0800 version 00501 usage P; group HP control 549050382 date 20260727 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
