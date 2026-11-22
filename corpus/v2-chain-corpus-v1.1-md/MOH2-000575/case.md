# Case MOH2-000575

Patient MARY TAYLOR, DOB 1937-12-06, sex M, member ID 1DU2TA8DX80. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-07-23.

## Adjudication outcome (835)
Claim PA25919524: status 1 (processed as primary, paid). Billed $82.47, paid $14.43, patient responsibility $3.61. Filing indicator MB (Medicare Part B). Payer claim control 2622856563515, POS 11 (office), frequency 1 (original claim).
Payment: $14.43 by CHK (check), handling I.
production date (405): 2026-08-16.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT233687500, originator 1184634935.
claim statement period start (232): 2026-07-23.
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97530-GP | 1 | $55.88 | $0 | CO-236 (Contractual Obligation: procedure/modifier combination not compatible per coding guidelines, bundled) $55.88 | HE N20 (service not payable with other service rendered on the same date) |
| 2 | 97150-GP | 1 | $26.59 | $14.43 allowed (B6) $18.04 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $8.55; PR-2 (Patient Responsibility: coinsurance amount) $3.61 |  |

Line item control numbers (REF 6R): PA25919524L1, PA25919524L2.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: MARY TAYLOR; MI (member ID) 1DU2TA8DX80; rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142.

## Claim as billed (837P)
Claim PA25919524, total charge $82.47, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25511 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97530-GP | 1 UN | $55.88 | 2026-07-23 | 1 | PA25919524L1 |
| 2 | 97150-GP | 1 UN | $26.59 | 2026-07-23 | 1 | PA25919524L2 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: MARY TAYLOR; MI (member ID) 1DU2TA8DX80; 9486 FRANKLIN LN; TRENTON, NJ, 08603
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: FATIMA AL-RASHID; XX (NPI) 1333183066
- rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142
- Submission reference TRC83857097, dated 2026-07-30 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-07-23.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: MARY TAYLOR; MI (member ID) 1DU2TA8DX80.
Subject DOB 1937-12-06, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-07-23
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: MARY TAYLOR; MI (member ID) 1DU2TA8DX80.
Subject DOB 1937-12-06, sex M.
Eligibility exchange reference ELG50259472, dated 2026-08-18 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-07-31, action code WQ, amount $82.47.
D9 (clearinghouse claim number): TRC83857097.
Trace (2 (referenced transaction trace)): TRC83857097.
received date (050): 2026-07-31.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: MARY TAYLOR; MI (member ID) 1DU2TA8DX80.
Acknowledgment reference ACK83857097, dated 2026-07-31 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-07-23. Dx: Pain in right shoulder. 97530 (16 min): therapeutic activities (dynamic functional tasks). 97150 (untimed, 1 unit): group therapeutic procedure. Total timed minutes: 16. 97530 was rendered as an independent service from 97150 — separate start/stop times were recorded and a different body region was treated. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1846349352, interchange 557325225 date 260818 time 0800 version 00501 usage P; group HS control 557325225 date 20260818 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1801579548, interchange 262656492 date 260818 time 0800 version 00501 usage P; group HB control 262656492 date 20260818 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1846349352, interchange 406207588 date 260730 time 0800 version 00501 usage P; group HC control 406207588 date 20260730 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 540074459 date 260731 time 0800 version 00501 usage P; group HN control 540074459 date 20260731 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1801579548, interchange 233687500 date 260816 time 0800 version 00501 usage P; group HP control 233687500 date 20260816 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 29
