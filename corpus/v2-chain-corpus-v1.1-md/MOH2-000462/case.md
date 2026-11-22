# Case MOH2-000462

Patient ELIZABETH MARTINEZ, DOB 1981-05-11, sex M, member ID EUG481148600. Payer: GARDEN STATE BENEFIT TRUST. Service date 2025-05-04.

## Adjudication outcome (835)
Claim PA26312128: status 4 (denied). Billed $71.08, paid $0, patient responsibility $71.08. Filing indicator CI (commercial insurance). Payer claim control 2514927291170, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2025-05-29.
Payer [PR]: GARDEN STATE BENEFIT TRUST; 210 RARITAN PLAZA; EDISON, NJ, 088373105; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820.
Trace (1 (current transaction trace)): EFT860466625, originator 1145082736.
claim statement period start (232): 2025-05-04.
Outpatient adjudication remarks (MOA): N30 (patient ineligible for this service).
Payee TJ (federal tax ID): 321822487.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97140-GP-59 | 1 | $46.15 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $46.15 |  |
| 2 | 97150-GP | 1 | $24.93 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $24.93 |  |

Line item control numbers (REF 6R): PA26312128L1, PA26312128L2.
Modifiers on remit lines: 59 (distinct procedural service), GP (under PT plan of care).
Remit claim parties: patient [QC]: ELIZABETH MARTINEZ; MI (member ID) EUG481148600; rendering provider [82]: MICHAEL MARTINEZ; XX (NPI) 1850202042.

## Claim as billed (837P)
Claim PA26312128, total charge $71.08, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25511 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97140-GP-59 | 1 UN | $46.15 | 2025-05-04 | 1 | PA26312128L1 |
| 2 | 97150-GP | 1 UN | $24.93 | 2025-05-04 | 1 | PA26312128L2 |

Modifiers on claim: 59 (distinct procedural service), GP (under PT plan of care).

Parties on claim:
- submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: GARDEN STATE BENEFIT TRUST; 46 (ETIN) 1450827364
- billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820; EI (employer ID/EIN) 321822487
- insured/subscriber [IL]: ELIZABETH MARTINEZ; MI (member ID) EUG481148600; 7589 MAPLE ST; TRENTON, NJ, 08604
- payer [PR]: GARDEN STATE BENEFIT TRUST; PI (payer ID) 1450827364
- referring provider [DN]: OMAR DELGADO; XX (NPI) 1094074058
- rendering provider [82]: MICHAEL MARTINEZ; XX (NPI) 1850202042
- Submission reference TRC70059751, dated 2025-05-10 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2025-05-04.
Inquiry parties: payer [PR]: GARDEN STATE BENEFIT TRUST; PI (payer ID) 1450827364; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: ELIZABETH MARTINEZ; MI (member ID) EUG481148600.
Subject DOB 1981-05-11, sex M.

Response:
- benefit: 6 (inactive), coverage level IND, service type 30 (health benefit plan coverage), plan: GARDEN STATE BENEFIT TRUST HMO
- plan date (291): 2025-05-04
- eligibility begin (356): 2024-01-01
- eligibility end (357): 2025-04-30
Response parties: payer [PR]: GARDEN STATE BENEFIT TRUST; PI (payer ID) 1450827364; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: ELIZABETH MARTINEZ; MI (member ID) EUG481148600.
Subject DOB 1981-05-11, sex M.
Eligibility exchange reference ELG37347291, dated 2025-06-02 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2025-05-10, action code WQ, amount $71.08.
D9 (clearinghouse claim number): TRC70059751.
Trace (2 (referenced transaction trace)): TRC70059751.
received date (050): 2025-05-10.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; patient [QC]: ELIZABETH MARTINEZ; MI (member ID) EUG481148600.
Acknowledgment reference ACK70059751, dated 2025-05-10 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2025-05-04. Dx: Pain in right shoulder. 97140 (16 min): manual therapy (soft tissue and joint mobilization). 97150 (untimed, 1 unit): group therapeutic procedure. Total timed minutes: 16. 97140 was performed in a separate 15-minute session from 97150, directed at a distinct body region with a distinct goal; services were not integral to one another. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1353206904 to receiver [ZZ] 1450827364, interchange 995995125 date 250602 time 0800 version 00501 usage P; group HS control 995995125 date 20250602 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1450827364 to receiver [ZZ] 1353206904, interchange 545678366 date 250602 time 0800 version 00501 usage P; group HB control 545678366 date 20250602 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 14
- claim_837p: sender [ZZ] 321822487 to receiver [ZZ] 1450827364, interchange 688835303 date 250510 time 0800 version 00501 usage P; group HC control 688835303 date 20250510 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 321822487, interchange 354154377 date 250510 time 0800 version 00501 usage P; group HN control 354154377 date 20250510 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1450827364 to receiver [ZZ] 1353206904, interchange 860466625 date 250529 time 0800 version 00501 usage P; group HP control 860466625 date 20250529 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 27
