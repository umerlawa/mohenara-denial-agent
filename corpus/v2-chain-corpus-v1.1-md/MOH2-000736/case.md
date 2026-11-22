# Case MOH2-000736

Patient JESSICA JACKSON, DOB 1943-09-23, sex F, member ID 7QQ3T84RA44. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-07-10.

## Adjudication outcome (835)
Claim PA29813186: status 1 (processed as primary, paid). Billed $74.32, paid $14.43, patient responsibility $3.61. Filing indicator MB (Medicare Part B). Payer claim control 2621952449325, POS 11 (office), frequency 1 (original claim).
Payment: $14.43 by CHK (check), handling I.
production date (405): 2026-08-07.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820.
Trace (1 (current transaction trace)): EFT610850713, originator 1184634935.
claim statement period start (232): 2026-07-10.
Payee TJ (federal tax ID): 321822487.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $42.25 | $0 | CO-236 (Contractual Obligation: procedure/modifier combination not compatible per coding guidelines, bundled) $42.25 | HE N20 (service not payable with other service rendered on the same date) |
| 2 | 97150-GP | 1 | $32.07 | $14.43 allowed (B6) $18.04 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $14.03; PR-2 (Patient Responsibility: coinsurance amount) $3.61 |  |

Line item control numbers (REF 6R): PA29813186L1, PA29813186L2.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: JESSICA JACKSON; MI (member ID) 7QQ3T84RA44; rendering provider [82]: THOMAS PEREZ; XX (NPI) 1981894162.

## Claim as billed (837P)
Claim PA29813186, total charge $74.32, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: S93401D (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $42.25 | 2026-07-10 | 1 | PA29813186L1 |
| 2 | 97150-GP | 1 UN | $32.07 | 2026-07-10 | 1 | PA29813186L2 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820; EI (employer ID/EIN) 321822487
- insured/subscriber [IL]: JESSICA JACKSON; MI (member ID) 7QQ3T84RA44; 9325 MAPLE LN; STATEN ISLAND, NY, 10335
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: SARAH CHEN; XX (NPI) 1410042904
- rendering provider [82]: THOMAS PEREZ; XX (NPI) 1981894162
- Submission reference TRC98908936, dated 2026-07-20 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-07-10.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: JESSICA JACKSON; MI (member ID) 7QQ3T84RA44.
Subject DOB 1943-09-23, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-07-10
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: JESSICA JACKSON; MI (member ID) 7QQ3T84RA44.
Subject DOB 1943-09-23, sex F.
Eligibility exchange reference ELG56058311, dated 2026-08-08 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-07-21, action code WQ, amount $74.32.
D9 (clearinghouse claim number): TRC98908936.
Trace (2 (referenced transaction trace)): TRC98908936.
received date (050): 2026-07-21.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; patient [QC]: JESSICA JACKSON; MI (member ID) 7QQ3T84RA44.
Acknowledgment reference ACK98908936, dated 2026-07-21 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-07-10. Dx: Sprain of unspecified ligament of right ankle subsequent encounter. 97110 (16 min): therapeutic exercise for strength and ROM. 97150 (untimed, 1 unit): group therapeutic procedure. Total timed minutes: 16. Separate-session log: 97110 performed apart from 97150 with its own timed interval, distinct target region, and its own documented goal. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1353206904 to receiver [ZZ] 1846349352, interchange 721878175 date 260808 time 0800 version 00501 usage P; group HS control 721878175 date 20260808 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1353206904, interchange 306958570 date 260808 time 0800 version 00501 usage P; group HB control 306958570 date 20260808 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 321822487 to receiver [ZZ] 1846349352, interchange 121341806 date 260720 time 0800 version 00501 usage P; group HC control 121341806 date 20260720 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 321822487, interchange 871591488 date 260721 time 0800 version 00501 usage P; group HN control 871591488 date 20260721 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1353206904, interchange 610850713 date 260807 time 0800 version 00501 usage P; group HP control 610850713 date 20260807 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 29
