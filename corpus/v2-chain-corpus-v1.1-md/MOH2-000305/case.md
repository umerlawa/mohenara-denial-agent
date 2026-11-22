# Case MOH2-000305

Patient RICHARD THOMAS, DOB 1951-02-01, sex M, member ID 4D85TG6JX14. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-06-11.

## Adjudication outcome (835)
Claim PA27899538: status 4 (denied). Billed $137.25, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2618269243151, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-07-01.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT578815919, originator 1184634935.
claim statement period start (232): 2026-06-11.
Outpatient adjudication remarks (MOA): N435 (exceeds number/frequency approved or allowed within time period).
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $48.61 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $48.61 |  |
| 2 | 97110-GP | 1 | $47.18 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $47.18 |  |
| 3 | 97110-GP | 1 | $41.46 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $41.46 |  |

Line item control numbers (REF 6R): PA27899538L1, PA27899538L2, PA27899538L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: RICHARD THOMAS; MI (member ID) 4D85TG6JX14; rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142.

## Claim as billed (837P)
Claim PA27899538, total charge $137.25, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M48061 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $48.61 | 2026-06-11 | 1 | PA27899538L1 |
| 2 | 97110-GP | 1 UN | $47.18 | 2026-06-11 | 1 | PA27899538L2 |
| 3 | 97110-GP | 1 UN | $41.46 | 2026-06-11 | 1 | PA27899538L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: RICHARD THOMAS; MI (member ID) 4D85TG6JX14; 3186 MAPLE LN; PHILADELPHIA, PA, 19147
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: DAVID GOLDSTEIN; XX (NPI) 1996029234
- rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142
- Submission reference TRC81541007, dated 2026-06-15 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-06-11.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: RICHARD THOMAS; MI (member ID) 4D85TG6JX14.
Subject DOB 1951-02-01, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-06-11
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: RICHARD THOMAS; MI (member ID) 4D85TG6JX14.
Subject DOB 1951-02-01, sex M.
Eligibility exchange reference ELG35658035, dated 2026-07-03 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-06-15, action code WQ, amount $137.25.
D9 (clearinghouse claim number): TRC81541007.
Trace (2 (referenced transaction trace)): TRC81541007.
received date (050): 2026-06-15.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: RICHARD THOMAS; MI (member ID) 4D85TG6JX14.
Acknowledgment reference ACK81541007, dated 2026-06-15 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-06-11. Dx: Spinal stenosis lumbar region without neurogenic claudication. 97110 (15 min): therapeutic exercise for strength and ROM. 97110 (14 min): therapeutic exercise for strength and ROM. 97110 (15 min): therapeutic exercise for strength and ROM. Total timed minutes: 44. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1846349352, interchange 394025346 date 260703 time 0800 version 00501 usage P; group HS control 394025346 date 20260703 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1801579548, interchange 177835703 date 260703 time 0800 version 00501 usage P; group HB control 177835703 date 20260703 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1846349352, interchange 781822863 date 260615 time 0800 version 00501 usage P; group HC control 781822863 date 20260615 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 233550131 date 260615 time 0800 version 00501 usage P; group HN control 233550131 date 20260615 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1801579548, interchange 578815919 date 260701 time 0800 version 00501 usage P; group HP control 578815919 date 20260701 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
