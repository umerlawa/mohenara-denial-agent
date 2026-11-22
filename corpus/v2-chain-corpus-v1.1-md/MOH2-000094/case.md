# Case MOH2-000094

Patient PATRICIA ROBINSON, DOB 1945-07-02, sex F, member ID 4CG5NV6EQ35. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-05-31.

## Adjudication outcome (835)
Claim PA24886236: status 1 (processed as primary, paid). Billed $66.75, paid $14.43, patient responsibility $3.61. Filing indicator MB (Medicare Part B). Payer claim control 2618420886234, POS 11 (office), frequency 1 (original claim).
Payment: $14.43 by CHK (check), handling I.
production date (405): 2026-07-03.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT544609795, originator 1184634935.
claim statement period start (232): 2026-05-31.
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP-KX | 1 | $40.18 | $0 | CO-236 (Contractual Obligation: procedure/modifier combination not compatible per coding guidelines, bundled) $40.18 | HE N20 (service not payable with other service rendered on the same date) |
| 2 | 97150-GP-KX | 1 | $26.57 | $14.43 allowed (B6) $18.04 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $8.53; PR-2 (Patient Responsibility: coinsurance amount) $3.61 |  |

Line item control numbers (REF 6R): PA24886236L1, PA24886236L2.
Modifiers on remit lines: GP (under PT plan of care), KX.
Remit claim parties: patient [QC]: PATRICIA ROBINSON; MI (member ID) 4CG5NV6EQ35; rendering provider [82]: WEI LEWIS; XX (NPI) 1986021803.

## Claim as billed (837P)
Claim PA24886236, total charge $66.75, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M1712 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP-KX | 1 UN | $40.18 | 2026-05-31 | 1 | PA24886236L1 |
| 2 | 97150-GP-KX | 1 UN | $26.57 | 2026-05-31 | 1 | PA24886236L2 |

Modifiers on claim: GP (under PT plan of care), KX.

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: PATRICIA ROBINSON; MI (member ID) 4CG5NV6EQ35; 1399 LINCOLN RD; WILMINGTON, DE, 19862
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: MARCUS WEBB; XX (NPI) 1583494452
- rendering provider [82]: WEI LEWIS; XX (NPI) 1986021803
- Submission reference TRC40910595, dated 2026-06-19 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-05-31.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: PATRICIA ROBINSON; MI (member ID) 4CG5NV6EQ35.
Subject DOB 1945-07-02, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-05-31
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: PATRICIA ROBINSON; MI (member ID) 4CG5NV6EQ35.
Subject DOB 1945-07-02, sex F.
Eligibility exchange reference ELG23168476, dated 2026-07-07 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-06-20, action code WQ, amount $66.75.
D9 (clearinghouse claim number): TRC40910595.
Trace (2 (referenced transaction trace)): TRC40910595.
received date (050): 2026-06-20.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: PATRICIA ROBINSON; MI (member ID) 4CG5NV6EQ35.
Acknowledgment reference ACK40910595, dated 2026-06-20 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-05-31. Dx: Unilateral primary osteoarthritis left knee. 97110 (15 min): therapeutic exercise for strength and ROM. 97150 (untimed, 1 unit): group therapeutic procedure. Total timed minutes: 15. 97110 was rendered as an independent service from 97150 — separate start/stop times were recorded and a different body region was treated. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1846349352, interchange 495476498 date 260707 time 0800 version 00501 usage P; group HS control 495476498 date 20260707 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 246007649 date 260707 time 0800 version 00501 usage P; group HB control 246007649 date 20260707 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1846349352, interchange 111357671 date 260619 time 0800 version 00501 usage P; group HC control 111357671 date 20260619 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 653362181 date 260620 time 0800 version 00501 usage P; group HN control 653362181 date 20260620 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 544609795 date 260703 time 0800 version 00501 usage P; group HP control 544609795 date 20260703 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 29
