# Case MOH2-000211

Patient JESSICA MOORE, DOB 1941-08-18, sex M, member ID JQF393075469. Payer: DELAWARE VALLEY MUTUAL. Service date 2026-01-15.

## Adjudication outcome (835)
Claim PA22736857: status 4 (denied). Billed $337.08, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2605395044939, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-02-22.
Payer [PR]: DELAWARE VALLEY MUTUAL; 900 SHIPLEY RD; WILMINGTON, DE, 198033012; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820.
Trace (1 (current transaction trace)): EFT863670589, originator 1155019382.
claim statement period start (232): 2026-01-15.
Outpatient adjudication remarks (MOA): MA04 (secondary payment cannot be considered without primary payer identity).
Payee TJ (federal tax ID): 321822487.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 | $78.58 | $0 | CO-22 (Contractual Obligation: care may be covered by another payer per coordination of benefits) $78.58 |  |
| 2 | 97140-GP | 1 | $47.07 | $0 | CO-22 (Contractual Obligation: care may be covered by another payer per coordination of benefits) $47.07 |  |
| 3 | 97530-GP | 2 | $94.54 | $0 | CO-22 (Contractual Obligation: care may be covered by another payer per coordination of benefits) $94.54 |  |
| 4 | 97112-GP | 2 | $116.89 | $0 | CO-22 (Contractual Obligation: care may be covered by another payer per coordination of benefits) $116.89 |  |

Line item control numbers (REF 6R): PA22736857L1, PA22736857L2, PA22736857L3, PA22736857L4.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: JESSICA MOORE; MI (member ID) JQF393075469; rendering provider [82]: THOMAS PEREZ; XX (NPI) 1981894162.

## Claim as billed (837P)
Claim PA22736857, total charge $337.08, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M542 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 UN | $78.58 | 2026-01-15 | 1 | PA22736857L1 |
| 2 | 97140-GP | 1 UN | $47.07 | 2026-01-15 | 1 | PA22736857L2 |
| 3 | 97530-GP | 2 UN | $94.54 | 2026-01-15 | 1 | PA22736857L3 |
| 4 | 97112-GP | 2 UN | $116.89 | 2026-01-15 | 1 | PA22736857L4 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: DELAWARE VALLEY MUTUAL; 46 (ETIN) 1550193826
- billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820; EI (employer ID/EIN) 321822487
- insured/subscriber [IL]: JESSICA MOORE; MI (member ID) JQF393075469; 5363 WILLOW AVE; WILMINGTON, DE, 19883
- payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826
- referring provider [DN]: GRETA LINDQVIST; XX (NPI) 1205658765
- rendering provider [82]: THOMAS PEREZ; XX (NPI) 1981894162
- Submission reference TRC25964010, dated 2026-01-21 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-01-15.
Inquiry parties: payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: JESSICA MOORE; MI (member ID) JQF393075469.
Subject DOB 1941-08-18, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: DELAWARE VALLEY MUTUAL POS
- benefit: R (other or additional payer), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-01-15
- eligibility begin (356): 2024-01-01
- eligibility begin (356): 2024-01-01
- payer message: PLAN IS PRIMARY PAYER FOR THIS MEMBER
Response parties: payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: JESSICA MOORE; MI (member ID) JQF393075469; payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352.
Subject DOB 1941-08-18, sex M.
Eligibility exchange reference ELG31944765, dated 2026-03-01 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-01-21, action code WQ, amount $337.08.
D9 (clearinghouse claim number): TRC25964010.
Trace (2 (referenced transaction trace)): TRC25964010.
received date (050): 2026-01-21.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; patient [QC]: JESSICA MOORE; MI (member ID) JQF393075469.
Acknowledgment reference ACK25964010, dated 2026-01-21 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-01-15. Dx: Cervicalgia. 97110 (30 min): therapeutic exercise for strength and ROM. 97140 (15 min): manual therapy (soft tissue and joint mobilization). 97530 (31 min): therapeutic activities (dynamic functional tasks). 97112 (30 min): neuromuscular re-education of movement and balance. Total timed minutes: 106. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1353206904 to receiver [ZZ] 1550193826, interchange 932744673 date 260301 time 0800 version 00501 usage P; group HS control 932744673 date 20260301 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1550193826 to receiver [ZZ] 1353206904, interchange 309230907 date 260301 time 0800 version 00501 usage P; group HB control 309230907 date 20260301 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 17
- claim_837p: sender [ZZ] 321822487 to receiver [ZZ] 1550193826, interchange 611739820 date 260121 time 0800 version 00501 usage P; group HC control 611739820 date 20260121 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 38
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 321822487, interchange 417040648 date 260121 time 0800 version 00501 usage P; group HN control 417040648 date 20260121 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1550193826 to receiver [ZZ] 1353206904, interchange 863670589 date 260222 time 0800 version 00501 usage P; group HP control 863670589 date 20260222 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 35
