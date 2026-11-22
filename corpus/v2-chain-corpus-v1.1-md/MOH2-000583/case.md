# Case MOH2-000583

Patient MARY TAYLOR, DOB 1937-12-06, sex M, member ID 1DU2TA8DX80. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-01-19.

## Adjudication outcome (835)
Claim PA21251763: status 4 (denied). Billed $175.72, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2609339242981, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-04-03.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT227150648, originator 1184634935.
claim statement period start (232): 2026-01-19.
Outpatient adjudication remarks (MOA): N111 (no appeal right except duplicate claim/service issue).
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $41.64 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $41.64 |  |
| 2 | 97140-GP | 1 | $37.44 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $37.44 |  |
| 3 | 97530-GP | 2 | $96.64 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $96.64 |  |

Line item control numbers (REF 6R): PA21251763L1, PA21251763L2, PA21251763L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: MARY TAYLOR; MI (member ID) 1DU2TA8DX80; rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142.

## Claim as billed (837P)
Claim PA21251763, total charge $175.72, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25511 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $41.64 | 2026-01-19 | 1 | PA21251763L1 |
| 2 | 97140-GP | 1 UN | $37.44 | 2026-01-19 | 1 | PA21251763L2 |
| 3 | 97530-GP | 2 UN | $96.64 | 2026-01-19 | 1 | PA21251763L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: MARY TAYLOR; MI (member ID) 1DU2TA8DX80; 9486 FRANKLIN LN; TRENTON, NJ, 08603
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: FATIMA AL-RASHID; XX (NPI) 1333183066
- rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142
- Submission reference TRC94899237, dated 2026-03-09 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-01-19.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: MARY TAYLOR; MI (member ID) 1DU2TA8DX80.
Subject DOB 1937-12-06, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-01-19
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: MARY TAYLOR; MI (member ID) 1DU2TA8DX80.
Subject DOB 1937-12-06, sex M.
Eligibility exchange reference ELG98732377, dated 2026-04-08 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-03-09, action code WQ, amount $175.72.
D9 (clearinghouse claim number): TRC94899237.
Trace (2 (referenced transaction trace)): TRC94899237.
received date (050): 2026-03-09.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: MARY TAYLOR; MI (member ID) 1DU2TA8DX80.
Acknowledgment reference ACK94899237, dated 2026-03-09 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-01-19. Dx: Pain in right shoulder. 97110 (15 min): therapeutic exercise for strength and ROM. 97140 (14 min): manual therapy (soft tissue and joint mobilization). 97530 (31 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 60. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1846349352, interchange 786042129 date 260408 time 0800 version 00501 usage P; group HS control 786042129 date 20260408 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1801579548, interchange 406173558 date 260408 time 0800 version 00501 usage P; group HB control 406173558 date 20260408 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1846349352, interchange 183505425 date 260309 time 0800 version 00501 usage P; group HC control 183505425 date 20260309 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 388836049 date 260309 time 0800 version 00501 usage P; group HN control 388836049 date 20260309 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1801579548, interchange 227150648 date 260403 time 0800 version 00501 usage P; group HP control 227150648 date 20260403 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
