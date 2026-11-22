# Case MOH2-000738

Patient ELIZABETH MARTINEZ, DOB 1981-05-11, sex M, member ID EUG481148600. Payer: GARDEN STATE BENEFIT TRUST. Service date 2025-05-01.

## Adjudication outcome (835)
Claim PA24938004: status 4 (denied). Billed $217.61, paid $0, patient responsibility $217.61. Filing indicator CI (commercial insurance). Payer claim control 2516386535416, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2025-06-12.
Payer [PR]: GARDEN STATE BENEFIT TRUST; 210 RARITAN PLAZA; EDISON, NJ, 088373105; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820.
Trace (1 (current transaction trace)): EFT446204011, originator 1145082736.
claim statement period start (232): 2025-05-01.
Outpatient adjudication remarks (MOA): N30 (patient ineligible for this service).
Payee TJ (federal tax ID): 321822487.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97140-GP | 2 | $76.03 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $76.03 |  |
| 2 | 97140-GP | 2 | $90.91 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $90.91 |  |
| 3 | 97112-GP | 1 | $50.67 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $50.67 |  |

Line item control numbers (REF 6R): PA24938004L1, PA24938004L2, PA24938004L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: ELIZABETH MARTINEZ; MI (member ID) EUG481148600; rendering provider [82]: MICHAEL MARTINEZ; XX (NPI) 1850202042.

## Claim as billed (837P)
Claim PA24938004, total charge $217.61, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25511 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97140-GP | 2 UN | $76.03 | 2025-05-01 | 1 | PA24938004L1 |
| 2 | 97140-GP | 2 UN | $90.91 | 2025-05-01 | 1 | PA24938004L2 |
| 3 | 97112-GP | 1 UN | $50.67 | 2025-05-01 | 1 | PA24938004L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: GARDEN STATE BENEFIT TRUST; 46 (ETIN) 1450827364
- billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820; EI (employer ID/EIN) 321822487
- insured/subscriber [IL]: ELIZABETH MARTINEZ; MI (member ID) EUG481148600; 7589 MAPLE ST; TRENTON, NJ, 08604
- payer [PR]: GARDEN STATE BENEFIT TRUST; PI (payer ID) 1450827364
- referring provider [DN]: OMAR DELGADO; XX (NPI) 1094074058
- rendering provider [82]: MICHAEL MARTINEZ; XX (NPI) 1850202042
- Submission reference TRC97668782, dated 2025-05-12 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2025-05-01.
Inquiry parties: payer [PR]: GARDEN STATE BENEFIT TRUST; PI (payer ID) 1450827364; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: ELIZABETH MARTINEZ; MI (member ID) EUG481148600.
Subject DOB 1981-05-11, sex M.

Response:
- benefit: 6 (inactive), coverage level IND, service type 30 (health benefit plan coverage), plan: GARDEN STATE BENEFIT TRUST HMO
- plan date (291): 2025-05-01
- eligibility begin (356): 2024-01-01
- eligibility end (357): 2025-04-30
Response parties: payer [PR]: GARDEN STATE BENEFIT TRUST; PI (payer ID) 1450827364; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: ELIZABETH MARTINEZ; MI (member ID) EUG481148600.
Subject DOB 1981-05-11, sex M.
Eligibility exchange reference ELG32328866, dated 2025-06-15 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2025-05-14, action code WQ, amount $217.61.
D9 (clearinghouse claim number): TRC97668782.
Trace (2 (referenced transaction trace)): TRC97668782.
received date (050): 2025-05-14.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; patient [QC]: ELIZABETH MARTINEZ; MI (member ID) EUG481148600.
Acknowledgment reference ACK97668782, dated 2025-05-14 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2025-05-01. Dx: Pain in right shoulder. 97140 (30 min): manual therapy (soft tissue and joint mobilization). 97140 (30 min): manual therapy (soft tissue and joint mobilization). 97112 (16 min): neuromuscular re-education of movement and balance. Total timed minutes: 76. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1353206904 to receiver [ZZ] 1450827364, interchange 676815478 date 250615 time 0800 version 00501 usage P; group HS control 676815478 date 20250615 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1450827364 to receiver [ZZ] 1353206904, interchange 798408379 date 250615 time 0800 version 00501 usage P; group HB control 798408379 date 20250615 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 14
- claim_837p: sender [ZZ] 321822487 to receiver [ZZ] 1450827364, interchange 482491252 date 250512 time 0800 version 00501 usage P; group HC control 482491252 date 20250512 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 321822487, interchange 567567893 date 250514 time 0800 version 00501 usage P; group HN control 567567893 date 20250514 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1450827364 to receiver [ZZ] 1353206904, interchange 446204011 date 250612 time 0800 version 00501 usage P; group HP control 446204011 date 20250612 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
