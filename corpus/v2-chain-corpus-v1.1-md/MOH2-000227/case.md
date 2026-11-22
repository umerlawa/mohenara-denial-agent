# Case MOH2-000227

Patient SAMUEL THOMAS, DOB 1937-12-10, sex M, member ID 8UD9CM3FQ31. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-05-14.

## Adjudication outcome (835)
Claim PA26628515: status 1 (processed as primary, paid). Billed $200.12, paid $42.49, patient responsibility $10.62. Filing indicator MB (Medicare Part B). Payer claim control 2617222258253, POS 11 (office), frequency 1 (original claim).
Payment: $42.49 by CHK (check), handling I.
production date (405): 2026-06-21.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820.
Trace (1 (current transaction trace)): EFT788465219, originator 1184634935.
claim statement period start (232): 2026-05-14.
Payee TJ (federal tax ID): 321822487.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 | $85.74 | $0 | CO-236 (Contractual Obligation: procedure/modifier combination not compatible per coding guidelines, bundled) $85.74 | HE N20 (service not payable with other service rendered on the same date) |
| 2 | 97150-GP | 1 | $30.54 | $14.43 allowed (B6) $18.04 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $12.5; PR-2 (Patient Responsibility: coinsurance amount) $3.61 |  |
| 3 | 97110-GP | 1 | $37.99 | $0 | CO-236 (Contractual Obligation: procedure/modifier combination not compatible per coding guidelines, bundled) $37.99 | HE N20 (service not payable with other service rendered on the same date) |
| 4 | 97530-GP-59 | 1 | $45.85 | $28.06 allowed (B6) $35.07 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $10.78; PR-2 (Patient Responsibility: coinsurance amount) $7.01 |  |

Line item control numbers (REF 6R): PA26628515L1, PA26628515L2, PA26628515L3, PA26628515L4.
Modifiers on remit lines: 59 (distinct procedural service), GP (under PT plan of care).
Remit claim parties: patient [QC]: SAMUEL THOMAS; MI (member ID) 8UD9CM3FQ31; rendering provider [82]: THOMAS PEREZ; XX (NPI) 1981894162.

## Claim as billed (837P)
Claim PA26628515, total charge $200.12, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M48061 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 UN | $85.74 | 2026-05-14 | 1 | PA26628515L1 |
| 2 | 97150-GP | 1 UN | $30.54 | 2026-05-14 | 1 | PA26628515L2 |
| 3 | 97110-GP | 1 UN | $37.99 | 2026-05-14 | 1 | PA26628515L3 |
| 4 | 97530-GP-59 | 1 UN | $45.85 | 2026-05-14 | 1 | PA26628515L4 |

Modifiers on claim: 59 (distinct procedural service), GP (under PT plan of care).

Parties on claim:
- submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820; EI (employer ID/EIN) 321822487
- insured/subscriber [IL]: SAMUEL THOMAS; MI (member ID) 8UD9CM3FQ31; 6434 CHESTNUT AVE; PHILADELPHIA, PA, 19193
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: PRIYA NAIR; XX (NPI) 1903307855
- rendering provider [82]: THOMAS PEREZ; XX (NPI) 1981894162
- Submission reference TRC45062977, dated 2026-06-01 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-05-14.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: SAMUEL THOMAS; MI (member ID) 8UD9CM3FQ31.
Subject DOB 1937-12-10, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-05-14
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: SAMUEL THOMAS; MI (member ID) 8UD9CM3FQ31.
Subject DOB 1937-12-10, sex M.
Eligibility exchange reference ELG79774557, dated 2026-06-26 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-06-02, action code WQ, amount $200.12.
D9 (clearinghouse claim number): TRC45062977.
Trace (2 (referenced transaction trace)): TRC45062977.
received date (050): 2026-06-02.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; patient [QC]: SAMUEL THOMAS; MI (member ID) 8UD9CM3FQ31.
Acknowledgment reference ACK45062977, dated 2026-06-02 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-05-14. Dx: Spinal stenosis lumbar region without neurogenic claudication. 97110 (31 min): therapeutic exercise for strength and ROM. 97150 (untimed, 1 unit): group therapeutic procedure. 97110 (14 min): therapeutic exercise for strength and ROM. 97530 (15 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 60. Separate-session log: 97110 performed apart from 97150 with its own timed interval, distinct target region, and its own documented goal. Documentation supports separate services: 97530 occupied a discrete timed interval apart from 97150 and addressed a different region and impairment. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1353206904 to receiver [ZZ] 1846349352, interchange 258631242 date 260626 time 0800 version 00501 usage P; group HS control 258631242 date 20260626 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1353206904, interchange 189711013 date 260626 time 0800 version 00501 usage P; group HB control 189711013 date 20260626 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 321822487 to receiver [ZZ] 1846349352, interchange 622719581 date 260601 time 0800 version 00501 usage P; group HC control 622719581 date 20260601 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 38
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 321822487, interchange 464098944 date 260602 time 0800 version 00501 usage P; group HN control 464098944 date 20260602 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1353206904, interchange 788465219 date 260621 time 0800 version 00501 usage P; group HP control 788465219 date 20260621 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 40
