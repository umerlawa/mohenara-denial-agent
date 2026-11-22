# Case MOH2-000070

Patient SAMUEL THOMAS, DOB 1937-12-10, sex M, member ID 8UD9CM3FQ31. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-05-24.

## Adjudication outcome (835)
Claim PA27626581: status 4 (denied). Billed $190.81, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2621070519135, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-07-29.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820.
Trace (1 (current transaction trace)): EFT964672817, originator 1184634935.
claim statement period start (232): 2026-05-24.
Outpatient adjudication remarks (MOA): N111 (no appeal right except duplicate claim/service issue).
Payee TJ (federal tax ID): 321822487.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 | $93.7 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $93.7 |  |
| 2 | 97140-GP | 1 | $49.18 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $49.18 |  |
| 3 | 97110-GP | 1 | $47.93 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $47.93 |  |

Line item control numbers (REF 6R): PA27626581L1, PA27626581L2, PA27626581L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: SAMUEL THOMAS; MI (member ID) 8UD9CM3FQ31; rendering provider [82]: THOMAS PEREZ; XX (NPI) 1981894162.

## Claim as billed (837P)
Claim PA27626581, total charge $190.81, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M48061 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 UN | $93.7 | 2026-05-24 | 1 | PA27626581L1 |
| 2 | 97140-GP | 1 UN | $49.18 | 2026-05-24 | 1 | PA27626581L2 |
| 3 | 97110-GP | 1 UN | $47.93 | 2026-05-24 | 1 | PA27626581L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820; EI (employer ID/EIN) 321822487
- insured/subscriber [IL]: SAMUEL THOMAS; MI (member ID) 8UD9CM3FQ31; 6434 CHESTNUT AVE; PHILADELPHIA, PA, 19193
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: PRIYA NAIR; XX (NPI) 1903307855
- rendering provider [82]: THOMAS PEREZ; XX (NPI) 1981894162
- Submission reference TRC45435754, dated 2026-07-05 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-05-24.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: SAMUEL THOMAS; MI (member ID) 8UD9CM3FQ31.
Subject DOB 1937-12-10, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-05-24
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: SAMUEL THOMAS; MI (member ID) 8UD9CM3FQ31.
Subject DOB 1937-12-10, sex M.
Eligibility exchange reference ELG50271700, dated 2026-08-01 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-07-05, action code WQ, amount $190.81.
D9 (clearinghouse claim number): TRC45435754.
Trace (2 (referenced transaction trace)): TRC45435754.
received date (050): 2026-07-05.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; patient [QC]: SAMUEL THOMAS; MI (member ID) 8UD9CM3FQ31.
Acknowledgment reference ACK45435754, dated 2026-07-05 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-05-24. Dx: Spinal stenosis lumbar region without neurogenic claudication. 97110 (30 min): therapeutic exercise for strength and ROM. 97140 (15 min): manual therapy (soft tissue and joint mobilization). 97110 (15 min): therapeutic exercise for strength and ROM. Total timed minutes: 60. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1353206904 to receiver [ZZ] 1846349352, interchange 411085563 date 260801 time 0800 version 00501 usage P; group HS control 411085563 date 20260801 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1353206904, interchange 130231166 date 260801 time 0800 version 00501 usage P; group HB control 130231166 date 20260801 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 321822487 to receiver [ZZ] 1846349352, interchange 905847405 date 260705 time 0800 version 00501 usage P; group HC control 905847405 date 20260705 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 321822487, interchange 983823982 date 260705 time 0800 version 00501 usage P; group HN control 983823982 date 20260705 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1353206904, interchange 964672817 date 260729 time 0800 version 00501 usage P; group HP control 964672817 date 20260729 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
