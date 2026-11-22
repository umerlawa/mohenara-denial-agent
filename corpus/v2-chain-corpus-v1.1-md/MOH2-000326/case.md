# Case MOH2-000326

Patient FRANK HERNANDEZ, DOB 1952-05-26, sex F, member ID 7ED2RR9DC45. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-05-15.

## Adjudication outcome (835)
Claim PA29266338: status 1 (processed as primary, paid). Billed $66.93, paid $14.43, patient responsibility $3.61. Filing indicator MB (Medicare Part B). Payer claim control 2616965943206, POS 11 (office), frequency 1 (original claim).
Payment: $14.43 by CHK (check), handling I.
production date (405): 2026-06-18.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820.
Trace (1 (current transaction trace)): EFT697259496, originator 1184634935.
claim statement period start (232): 2026-05-15.
Payee TJ (federal tax ID): 321822487.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97150-GP | 1 | $28.48 | $14.43 allowed (B6) $18.04 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $10.44; PR-2 (Patient Responsibility: coinsurance amount) $3.61 |  |
| 2 | 97110-GP | 1 | $38.45 | $0 | CO-236 (Contractual Obligation: procedure/modifier combination not compatible per coding guidelines, bundled) $38.45 | HE N20 (service not payable with other service rendered on the same date) |

Line item control numbers (REF 6R): PA29266338L1, PA29266338L2.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: FRANK HERNANDEZ; MI (member ID) 7ED2RR9DC45; rendering provider [82]: THOMAS PEREZ; XX (NPI) 1981894162.

## Claim as billed (837P)
Claim PA29266338, total charge $66.93, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25511 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97150-GP | 1 UN | $28.48 | 2026-05-15 | 1 | PA29266338L1 |
| 2 | 97110-GP | 1 UN | $38.45 | 2026-05-15 | 1 | PA29266338L2 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820; EI (employer ID/EIN) 321822487
- insured/subscriber [IL]: FRANK HERNANDEZ; MI (member ID) 7ED2RR9DC45; 8860 MAPLE LN; WILMINGTON, DE, 19898
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: FATIMA AL-RASHID; XX (NPI) 1333183066
- rendering provider [82]: THOMAS PEREZ; XX (NPI) 1981894162
- Submission reference TRC58099503, dated 2026-05-28 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-05-15.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: FRANK HERNANDEZ; MI (member ID) 7ED2RR9DC45.
Subject DOB 1952-05-26, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-05-15
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: FRANK HERNANDEZ; MI (member ID) 7ED2RR9DC45.
Subject DOB 1952-05-26, sex F.
Eligibility exchange reference ELG92506086, dated 2026-06-24 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-05-29, action code WQ, amount $66.93.
D9 (clearinghouse claim number): TRC58099503.
Trace (2 (referenced transaction trace)): TRC58099503.
received date (050): 2026-05-29.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; patient [QC]: FRANK HERNANDEZ; MI (member ID) 7ED2RR9DC45.
Acknowledgment reference ACK58099503, dated 2026-05-29 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-05-15. Dx: Pain in right shoulder. 97150 (untimed, 1 unit): group therapeutic procedure. 97110 (16 min): therapeutic exercise for strength and ROM. Total timed minutes: 16. Documentation supports separate services: 97110 occupied a discrete timed interval apart from 97150 and addressed a different region and impairment. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1353206904 to receiver [ZZ] 1846349352, interchange 986284870 date 260624 time 0800 version 00501 usage P; group HS control 986284870 date 20260624 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1353206904, interchange 208245776 date 260624 time 0800 version 00501 usage P; group HB control 208245776 date 20260624 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 321822487 to receiver [ZZ] 1846349352, interchange 688878042 date 260528 time 0800 version 00501 usage P; group HC control 688878042 date 20260528 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 321822487, interchange 381537499 date 260529 time 0800 version 00501 usage P; group HN control 381537499 date 20260529 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1353206904, interchange 697259496 date 260618 time 0800 version 00501 usage P; group HP control 697259496 date 20260618 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 29
