# Case MOH2-000311

Patient BARBARA MOORE, DOB 1953-01-01, sex M, member ID 2J53RE5TK28. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-08-04.

## Adjudication outcome (835)
Claim PA23072118: status 4 (denied). Billed $197.73, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2625523353331, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-09-12.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT597501100, originator 1184634935.
claim statement period start (232): 2026-08-04.
Outpatient adjudication remarks (MOA): N435 (exceeds number/frequency approved or allowed within time period).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97530-GP | 2 | $102.45 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $102.45 |  |
| 2 | 97535-GP | 1 | $45.9 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $45.9 |  |
| 3 | 97112-GP | 1 | $49.38 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $49.38 |  |

Line item control numbers (REF 6R): PA23072118L1, PA23072118L2, PA23072118L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: BARBARA MOORE; MI (member ID) 2J53RE5TK28; rendering provider [82]: MARY CLARK; XX (NPI) 1992501921.

## Claim as billed (837P)
Claim PA23072118, total charge $197.73, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M48061 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97530-GP | 2 UN | $102.45 | 2026-08-04 | 1 | PA23072118L1 |
| 2 | 97535-GP | 1 UN | $45.9 | 2026-08-04 | 1 | PA23072118L2 |
| 3 | 97112-GP | 1 UN | $49.38 | 2026-08-04 | 1 | PA23072118L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: BARBARA MOORE; MI (member ID) 2J53RE5TK28; 9678 WILLOW ST; WILMINGTON, DE, 19813
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: AISHA RAHMAN; XX (NPI) 1538183382
- rendering provider [82]: MARY CLARK; XX (NPI) 1992501921
- Submission reference TRC54988095, dated 2026-08-08 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-08-04.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: BARBARA MOORE; MI (member ID) 2J53RE5TK28.
Subject DOB 1953-01-01, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-08-04
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: BARBARA MOORE; MI (member ID) 2J53RE5TK28.
Subject DOB 1953-01-01, sex M.
Eligibility exchange reference ELG20140643, dated 2026-09-14 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-08-08, action code WQ, amount $197.73.
D9 (clearinghouse claim number): TRC54988095.
Trace (2 (referenced transaction trace)): TRC54988095.
received date (050): 2026-08-08.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: BARBARA MOORE; MI (member ID) 2J53RE5TK28.
Acknowledgment reference ACK54988095, dated 2026-08-08 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-08-04. Dx: Spinal stenosis lumbar region without neurogenic claudication. 97530 (30 min): therapeutic activities (dynamic functional tasks). 97535 (16 min): self-care/home management training. 97112 (16 min): neuromuscular re-education of movement and balance. Total timed minutes: 62. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 176881462 date 260914 time 0800 version 00501 usage P; group HS control 176881462 date 20260914 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 626106064 date 260914 time 0800 version 00501 usage P; group HB control 626106064 date 20260914 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 421550405 date 260808 time 0800 version 00501 usage P; group HC control 421550405 date 20260808 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 370160921 date 260808 time 0800 version 00501 usage P; group HN control 370160921 date 20260808 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 597501100 date 260912 time 0800 version 00501 usage P; group HP control 597501100 date 20260912 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
