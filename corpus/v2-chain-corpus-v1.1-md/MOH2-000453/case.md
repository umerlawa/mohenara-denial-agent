# Case MOH2-000453

Patient MARIA RODRIGUEZ, DOB 1955-10-10, sex M, member ID BDS257046369. Payer: GARDEN STATE BENEFIT TRUST. Service date 2026-01-12.

## Adjudication outcome (835)
Claim PA23810680: status 4 (denied). Billed $140.2, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2606231318252, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-03-03.
Payer [PR]: GARDEN STATE BENEFIT TRUST; 210 RARITAN PLAZA; EDISON, NJ, 088373105; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820.
Trace (1 (current transaction trace)): EFT913859277, originator 1145082736.
claim statement period start (232): 2026-01-12.
Outpatient adjudication remarks (MOA): MA04 (secondary payment cannot be considered without primary payer identity).
Payee TJ (federal tax ID): 321822487.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $51.12 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $51.12 |  |
| 2 | 97112-GP | 1 | $50.68 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $50.68 |  |
| 3 | 97140-GP | 1 | $38.4 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $38.4 |  |

Line item control numbers (REF 6R): PA23810680L1, PA23810680L2, PA23810680L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: MARIA RODRIGUEZ; MI (member ID) BDS257046369; rendering provider [82]: JOHN CLARK; XX (NPI) 1878226791.

## Claim as billed (837P)
Claim PA23810680, total charge $140.2, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $51.12 | 2026-01-12 | 1 | PA23810680L1 |
| 2 | 97112-GP | 1 UN | $50.68 | 2026-01-12 | 1 | PA23810680L2 |
| 3 | 97140-GP | 1 UN | $38.4 | 2026-01-12 | 1 | PA23810680L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: GARDEN STATE BENEFIT TRUST; 46 (ETIN) 1450827364
- billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820; EI (employer ID/EIN) 321822487
- insured/subscriber [IL]: MARIA RODRIGUEZ; MI (member ID) BDS257046369; 2473 WILLOW ST; TRENTON, NJ, 08690
- payer [PR]: GARDEN STATE BENEFIT TRUST; PI (payer ID) 1450827364
- referring provider [DN]: AISHA RAHMAN; XX (NPI) 1538183382
- rendering provider [82]: JOHN CLARK; XX (NPI) 1878226791
- Submission reference TRC66012307, dated 2026-01-24 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-01-12.
Inquiry parties: payer [PR]: GARDEN STATE BENEFIT TRUST; PI (payer ID) 1450827364; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: MARIA RODRIGUEZ; MI (member ID) BDS257046369.
Subject DOB 1955-10-10, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: GARDEN STATE BENEFIT TRUST EPO
- benefit: R (other or additional payer), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-01-12
- eligibility begin (356): 2024-01-01
- eligibility begin (356): 2024-01-01
- payer message: PLAN IS PRIMARY PAYER FOR THIS MEMBER
Response parties: payer [PR]: GARDEN STATE BENEFIT TRUST; PI (payer ID) 1450827364; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: MARIA RODRIGUEZ; MI (member ID) BDS257046369; payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352.
Subject DOB 1955-10-10, sex M.
Eligibility exchange reference ELG30539939, dated 2026-03-10 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-01-24, action code WQ, amount $140.2.
D9 (clearinghouse claim number): TRC66012307.
Trace (2 (referenced transaction trace)): TRC66012307.
received date (050): 2026-01-24.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; patient [QC]: MARIA RODRIGUEZ; MI (member ID) BDS257046369.
Acknowledgment reference ACK66012307, dated 2026-01-24 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-01-12. Dx: Aftercare following joint replacement surgery. 97110 (15 min): therapeutic exercise for strength and ROM. 97112 (14 min): neuromuscular re-education of movement and balance. 97140 (15 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 44. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1353206904 to receiver [ZZ] 1450827364, interchange 919605317 date 260310 time 0800 version 00501 usage P; group HS control 919605317 date 20260310 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1450827364 to receiver [ZZ] 1353206904, interchange 432716841 date 260310 time 0800 version 00501 usage P; group HB control 432716841 date 20260310 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 17
- claim_837p: sender [ZZ] 321822487 to receiver [ZZ] 1450827364, interchange 515974574 date 260124 time 0800 version 00501 usage P; group HC control 515974574 date 20260124 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 321822487, interchange 480417406 date 260124 time 0800 version 00501 usage P; group HN control 480417406 date 20260124 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1450827364 to receiver [ZZ] 1353206904, interchange 913859277 date 260303 time 0800 version 00501 usage P; group HP control 913859277 date 20260303 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
