# Case MOH2-000043

Patient MARY TAYLOR, DOB 1937-12-06, sex M, member ID 1DU2TA8DX80. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-07-31.

## Adjudication outcome (835)
Claim PA21046784: status 4 (denied). Billed $178.46, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2625373216972, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-09-10.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT157641631, originator 1184634935.
claim statement period start (232): 2026-07-31.
Outpatient adjudication remarks (MOA): N435 (exceeds number/frequency approved or allowed within time period).
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $41.8 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $41.8 |  |
| 2 | 97110-GP | 2 | $87.35 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $87.35 |  |
| 3 | 97110-GP | 1 | $49.31 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $49.31 |  |

Line item control numbers (REF 6R): PA21046784L1, PA21046784L2, PA21046784L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: MARY TAYLOR; MI (member ID) 1DU2TA8DX80; rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142.

## Claim as billed (837P)
Claim PA21046784, total charge $178.46, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25511 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $41.8 | 2026-07-31 | 1 | PA21046784L1 |
| 2 | 97110-GP | 2 UN | $87.35 | 2026-07-31 | 1 | PA21046784L2 |
| 3 | 97110-GP | 1 UN | $49.31 | 2026-07-31 | 1 | PA21046784L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: MARY TAYLOR; MI (member ID) 1DU2TA8DX80; 9486 FRANKLIN LN; TRENTON, NJ, 08603
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: FATIMA AL-RASHID; XX (NPI) 1333183066
- rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142
- Submission reference TRC37133605, dated 2026-08-15 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-07-31.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: MARY TAYLOR; MI (member ID) 1DU2TA8DX80.
Subject DOB 1937-12-06, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-07-31
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: MARY TAYLOR; MI (member ID) 1DU2TA8DX80.
Subject DOB 1937-12-06, sex M.
Eligibility exchange reference ELG49122183, dated 2026-09-13 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-08-17, action code WQ, amount $178.46.
D9 (clearinghouse claim number): TRC37133605.
Trace (2 (referenced transaction trace)): TRC37133605.
received date (050): 2026-08-17.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: MARY TAYLOR; MI (member ID) 1DU2TA8DX80.
Acknowledgment reference ACK37133605, dated 2026-08-17 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-07-31. Dx: Pain in right shoulder. 97110 (14 min): therapeutic exercise for strength and ROM. 97110 (31 min): therapeutic exercise for strength and ROM. 97110 (16 min): therapeutic exercise for strength and ROM. Total timed minutes: 61. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1846349352, interchange 489058733 date 260913 time 0800 version 00501 usage P; group HS control 489058733 date 20260913 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1801579548, interchange 866678776 date 260913 time 0800 version 00501 usage P; group HB control 866678776 date 20260913 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1846349352, interchange 721115433 date 260815 time 0800 version 00501 usage P; group HC control 721115433 date 20260815 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 534162438 date 260817 time 0800 version 00501 usage P; group HN control 534162438 date 20260817 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1801579548, interchange 157641631 date 260910 time 0800 version 00501 usage P; group HP control 157641631 date 20260910 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
