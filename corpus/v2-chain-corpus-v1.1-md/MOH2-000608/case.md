# Case MOH2-000608

Patient MARIA RODRIGUEZ, DOB 1955-10-10, sex M, member ID 5E10X77QK02. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-06-28.

## Adjudication outcome (835)
Claim PA27348327: status 1 (processed as primary, paid). Billed $120.18, paid $14.43, patient responsibility $3.61. Filing indicator MB (Medicare Part B). Payer claim control 2623180843992, POS 11 (office), frequency 1 (original claim).
Payment: $14.43 by CHK (check), handling I.
production date (405): 2026-08-19.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820.
Trace (1 (current transaction trace)): EFT106976942, originator 1184634935.
claim statement period start (232): 2026-06-28.
Payee TJ (federal tax ID): 321822487.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP-KX | 2 | $88.7 | $0 | CO-236 (Contractual Obligation: procedure/modifier combination not compatible per coding guidelines, bundled) $88.7 | HE N20 (service not payable with other service rendered on the same date) |
| 2 | 97150-GP-KX | 1 | $31.48 | $14.43 allowed (B6) $18.04 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $13.44; PR-2 (Patient Responsibility: coinsurance amount) $3.61 |  |

Line item control numbers (REF 6R): PA27348327L1, PA27348327L2.
Modifiers on remit lines: GP (under PT plan of care), KX.
Remit claim parties: patient [QC]: MARIA RODRIGUEZ; MI (member ID) 5E10X77QK02; rendering provider [82]: JOHN CLARK; XX (NPI) 1878226791.

## Claim as billed (837P)
Claim PA27348327, total charge $120.18, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP-KX | 2 UN | $88.7 | 2026-06-28 | 1 | PA27348327L1 |
| 2 | 97150-GP-KX | 1 UN | $31.48 | 2026-06-28 | 1 | PA27348327L2 |

Modifiers on claim: GP (under PT plan of care), KX.

Parties on claim:
- submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820; EI (employer ID/EIN) 321822487
- insured/subscriber [IL]: MARIA RODRIGUEZ; MI (member ID) 5E10X77QK02; 2473 WILLOW ST; TRENTON, NJ, 08690
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: AISHA RAHMAN; XX (NPI) 1538183382
- rendering provider [82]: JOHN CLARK; XX (NPI) 1878226791
- Submission reference TRC72761776, dated 2026-07-17 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-06-28.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: MARIA RODRIGUEZ; MI (member ID) 5E10X77QK02.
Subject DOB 1955-10-10, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-06-28
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: MARIA RODRIGUEZ; MI (member ID) 5E10X77QK02.
Subject DOB 1955-10-10, sex M.
Eligibility exchange reference ELG27970825, dated 2026-08-20 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-07-17, action code WQ, amount $120.18.
D9 (clearinghouse claim number): TRC72761776.
Trace (2 (referenced transaction trace)): TRC72761776.
received date (050): 2026-07-17.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; patient [QC]: MARIA RODRIGUEZ; MI (member ID) 5E10X77QK02.
Acknowledgment reference ACK72761776, dated 2026-07-17 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-06-28. Dx: Aftercare following joint replacement surgery. 97110 (30 min): therapeutic exercise for strength and ROM. 97150 (untimed, 1 unit): group therapeutic procedure. Total timed minutes: 30. Documentation supports separate services: 97110 occupied a discrete timed interval apart from 97150 and addressed a different region and impairment. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1353206904 to receiver [ZZ] 1846349352, interchange 158781322 date 260820 time 0800 version 00501 usage P; group HS control 158781322 date 20260820 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1353206904, interchange 574208736 date 260820 time 0800 version 00501 usage P; group HB control 574208736 date 20260820 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 321822487 to receiver [ZZ] 1846349352, interchange 541758084 date 260717 time 0800 version 00501 usage P; group HC control 541758084 date 20260717 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 321822487, interchange 285887409 date 260717 time 0800 version 00501 usage P; group HN control 285887409 date 20260717 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1353206904, interchange 106976942 date 260819 time 0800 version 00501 usage P; group HP control 106976942 date 20260819 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 29
