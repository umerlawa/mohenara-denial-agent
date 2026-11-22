# Case MOH2-000379

Patient SAMUEL THOMAS, DOB 1937-12-10, sex M, member ID 8UD9CM3FQ31. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-05-19.

## Adjudication outcome (835)
Claim PA27903332: status 1 (processed as primary, paid). Billed $73.29, paid $14.43, patient responsibility $3.61. Filing indicator MB (Medicare Part B). Payer claim control 2618196827413, POS 11 (office), frequency 1 (original claim).
Payment: $14.43 by CHK (check), handling I.
production date (405): 2026-06-30.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820.
Trace (1 (current transaction trace)): EFT911533556, originator 1184634935.
claim statement period start (232): 2026-05-19.
Payee TJ (federal tax ID): 321822487.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97150-GP | 1 | $31.29 | $14.43 allowed (B6) $18.04 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $13.25; PR-2 (Patient Responsibility: coinsurance amount) $3.61 |  |
| 2 | 97110-GP | 1 | $42 | $0 | CO-236 (Contractual Obligation: procedure/modifier combination not compatible per coding guidelines, bundled) $42 | HE N20 (service not payable with other service rendered on the same date) |

Line item control numbers (REF 6R): PA27903332L1, PA27903332L2.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: SAMUEL THOMAS; MI (member ID) 8UD9CM3FQ31; rendering provider [82]: THOMAS PEREZ; XX (NPI) 1981894162.

## Claim as billed (837P)
Claim PA27903332, total charge $73.29, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M48061 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97150-GP | 1 UN | $31.29 | 2026-05-19 | 1 | PA27903332L1 |
| 2 | 97110-GP | 1 UN | $42 | 2026-05-19 | 1 | PA27903332L2 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820; EI (employer ID/EIN) 321822487
- insured/subscriber [IL]: SAMUEL THOMAS; MI (member ID) 8UD9CM3FQ31; 6434 CHESTNUT AVE; PHILADELPHIA, PA, 19193
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: PRIYA NAIR; XX (NPI) 1903307855
- rendering provider [82]: THOMAS PEREZ; XX (NPI) 1981894162
- Submission reference TRC30084338, dated 2026-05-23 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-05-19.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: SAMUEL THOMAS; MI (member ID) 8UD9CM3FQ31.
Subject DOB 1937-12-10, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-05-19
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: SAMUEL THOMAS; MI (member ID) 8UD9CM3FQ31.
Subject DOB 1937-12-10, sex M.
Eligibility exchange reference ELG37673418, dated 2026-07-01 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-05-25, action code WQ, amount $73.29.
D9 (clearinghouse claim number): TRC30084338.
Trace (2 (referenced transaction trace)): TRC30084338.
received date (050): 2026-05-25.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; patient [QC]: SAMUEL THOMAS; MI (member ID) 8UD9CM3FQ31.
Acknowledgment reference ACK30084338, dated 2026-05-25 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-05-19. Dx: Spinal stenosis lumbar region without neurogenic claudication. 97150 (untimed, 1 unit): group therapeutic procedure. 97110 (15 min): therapeutic exercise for strength and ROM. Total timed minutes: 15. 97110 was performed in a separate 15-minute session from 97150, directed at a distinct body region with a distinct goal; services were not integral to one another. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1353206904 to receiver [ZZ] 1846349352, interchange 997044306 date 260701 time 0800 version 00501 usage P; group HS control 997044306 date 20260701 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1353206904, interchange 533673369 date 260701 time 0800 version 00501 usage P; group HB control 533673369 date 20260701 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 321822487 to receiver [ZZ] 1846349352, interchange 323863757 date 260523 time 0800 version 00501 usage P; group HC control 323863757 date 20260523 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 321822487, interchange 465541860 date 260525 time 0800 version 00501 usage P; group HN control 465541860 date 20260525 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1353206904, interchange 911533556 date 260630 time 0800 version 00501 usage P; group HP control 911533556 date 20260630 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 29
