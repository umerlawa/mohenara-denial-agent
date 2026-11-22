# Case MOH2-000044

Patient JESSICA JACKSON, DOB 1943-09-23, sex F, member ID 7QQ3T84RA44. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-07-20.

## Adjudication outcome (835)
Claim PA25765894: status 1 (processed as primary, paid). Billed $73.25, paid $14.43, patient responsibility $3.61. Filing indicator MB (Medicare Part B). Payer claim control 2622719599483, POS 11 (office), frequency 1 (original claim).
Payment: $14.43 by CHK (check), handling I.
production date (405): 2026-08-15.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820.
Trace (1 (current transaction trace)): EFT656277143, originator 1184634935.
claim statement period start (232): 2026-07-20.
Payee TJ (federal tax ID): 321822487.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97112-GP | 1 | $44.24 | $0 | CO-236 (Contractual Obligation: procedure/modifier combination not compatible per coding guidelines, bundled) $44.24 | HE N20 (service not payable with other service rendered on the same date) |
| 2 | 97150-GP | 1 | $29.01 | $14.43 allowed (B6) $18.04 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $10.97; PR-2 (Patient Responsibility: coinsurance amount) $3.61 |  |

Line item control numbers (REF 6R): PA25765894L1, PA25765894L2.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: JESSICA JACKSON; MI (member ID) 7QQ3T84RA44; rendering provider [82]: THOMAS PEREZ; XX (NPI) 1981894162.

## Claim as billed (837P)
Claim PA25765894, total charge $73.25, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: S93401D (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97112-GP | 1 UN | $44.24 | 2026-07-20 | 1 | PA25765894L1 |
| 2 | 97150-GP | 1 UN | $29.01 | 2026-07-20 | 1 | PA25765894L2 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820; EI (employer ID/EIN) 321822487
- insured/subscriber [IL]: JESSICA JACKSON; MI (member ID) 7QQ3T84RA44; 9325 MAPLE LN; STATEN ISLAND, NY, 10335
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: SARAH CHEN; XX (NPI) 1410042904
- rendering provider [82]: THOMAS PEREZ; XX (NPI) 1981894162
- Submission reference TRC93902412, dated 2026-07-28 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-07-20.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: JESSICA JACKSON; MI (member ID) 7QQ3T84RA44.
Subject DOB 1943-09-23, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-07-20
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: JESSICA JACKSON; MI (member ID) 7QQ3T84RA44.
Subject DOB 1943-09-23, sex F.
Eligibility exchange reference ELG72560685, dated 2026-08-22 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-07-29, action code WQ, amount $73.25.
D9 (clearinghouse claim number): TRC93902412.
Trace (2 (referenced transaction trace)): TRC93902412.
received date (050): 2026-07-29.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; patient [QC]: JESSICA JACKSON; MI (member ID) 7QQ3T84RA44.
Acknowledgment reference ACK93902412, dated 2026-07-29 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-07-20. Dx: Sprain of unspecified ligament of right ankle subsequent encounter. 97112 (16 min): neuromuscular re-education of movement and balance. 97150 (untimed, 1 unit): group therapeutic procedure. Total timed minutes: 16. The 97112 intervention was distinct from 97150: performed sequentially in separate timed segments and directed at different anatomic sites. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1353206904 to receiver [ZZ] 1846349352, interchange 349717483 date 260822 time 0800 version 00501 usage P; group HS control 349717483 date 20260822 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1353206904, interchange 383537569 date 260822 time 0800 version 00501 usage P; group HB control 383537569 date 20260822 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 321822487 to receiver [ZZ] 1846349352, interchange 916421927 date 260728 time 0800 version 00501 usage P; group HC control 916421927 date 20260728 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 321822487, interchange 440211481 date 260729 time 0800 version 00501 usage P; group HN control 440211481 date 20260729 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1353206904, interchange 656277143 date 260815 time 0800 version 00501 usage P; group HP control 656277143 date 20260815 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 29
