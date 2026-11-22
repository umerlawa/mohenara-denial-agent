# Case MOH2-000268

Patient THOMAS CLARK, DOB 1941-03-27, sex M, member ID 5JY1CU1XQ76. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-06-12.

## Adjudication outcome (835)
Claim PA24117975: status 1 (processed as primary, paid). Billed $177, paid $42.49, patient responsibility $10.62. Filing indicator MB (Medicare Part B). Payer claim control 2618946830169, POS 11 (office), frequency 1 (original claim).
Payment: $42.49 by CHK (check), handling I.
production date (405): 2026-07-08.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT738781449, originator 1184634935.
claim statement period start (232): 2026-06-12.
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97530-GP-59 | 1 | $56.14 | $28.06 allowed (B6) $35.07 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $21.07; PR-2 (Patient Responsibility: coinsurance amount) $7.01 |  |
| 2 | 97150-GP | 1 | $30.41 | $14.43 allowed (B6) $18.04 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $12.37; PR-2 (Patient Responsibility: coinsurance amount) $3.61 |  |
| 3 | 97140-GP | 2 | $90.45 | $0 | CO-236 (Contractual Obligation: procedure/modifier combination not compatible per coding guidelines, bundled) $90.45 | HE N20 (service not payable with other service rendered on the same date) |

Line item control numbers (REF 6R): PA24117975L1, PA24117975L2, PA24117975L3.
Modifiers on remit lines: 59 (distinct procedural service), GP (under PT plan of care).
Remit claim parties: patient [QC]: THOMAS CLARK; MI (member ID) 5JY1CU1XQ76; rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737.

## Claim as billed (837P)
Claim PA24117975, total charge $177, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97530-GP-59 | 1 UN | $56.14 | 2026-06-12 | 1 | PA24117975L1 |
| 2 | 97150-GP | 1 UN | $30.41 | 2026-06-12 | 1 | PA24117975L2 |
| 3 | 97140-GP | 2 UN | $90.45 | 2026-06-12 | 1 | PA24117975L3 |

Modifiers on claim: 59 (distinct procedural service), GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: THOMAS CLARK; MI (member ID) 5JY1CU1XQ76; 5403 LINCOLN ST; WILMINGTON, DE, 19806
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: MARCUS WEBB; XX (NPI) 1583494452
- rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737
- Submission reference TRC37400023, dated 2026-06-15 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-06-12.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: THOMAS CLARK; MI (member ID) 5JY1CU1XQ76.
Subject DOB 1941-03-27, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-06-12
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: THOMAS CLARK; MI (member ID) 5JY1CU1XQ76.
Subject DOB 1941-03-27, sex M.
Eligibility exchange reference ELG18980290, dated 2026-07-13 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-06-17, action code WQ, amount $177.
D9 (clearinghouse claim number): TRC37400023.
Trace (2 (referenced transaction trace)): TRC37400023.
received date (050): 2026-06-17.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: THOMAS CLARK; MI (member ID) 5JY1CU1XQ76.
Acknowledgment reference ACK37400023, dated 2026-06-17 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-06-12. Dx: Aftercare following joint replacement surgery. 97530 (14 min): therapeutic activities (dynamic functional tasks). 97150 (untimed, 1 unit): group therapeutic procedure. 97140 (29 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 43. Documentation supports separate services: 97140 occupied a discrete timed interval apart from 97150 and addressed a different region and impairment. 97530 and 97150 were furnished as separate and distinct services: different session times, different anatomic regions, independent treatment goals. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1846349352, interchange 432358316 date 260713 time 0800 version 00501 usage P; group HS control 432358316 date 20260713 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 898673473 date 260713 time 0800 version 00501 usage P; group HB control 898673473 date 20260713 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1846349352, interchange 925279694 date 260615 time 0800 version 00501 usage P; group HC control 925279694 date 20260615 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 154759850 date 260617 time 0800 version 00501 usage P; group HN control 154759850 date 20260617 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 738781449 date 260708 time 0800 version 00501 usage P; group HP control 738781449 date 20260708 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 35
