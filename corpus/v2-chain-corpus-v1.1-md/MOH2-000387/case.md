# Case MOH2-000387

Patient JOHN SMITH, DOB 1943-04-09, sex M, member ID 7A22FM4GH98. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-07-05.

## Adjudication outcome (835)
Claim PA26672725: status 1 (processed as primary, paid). Billed $79.59, paid $14.43, patient responsibility $3.61. Filing indicator MB (Medicare Part B). Payer claim control 2624287104256, POS 11 (office), frequency 1 (original claim).
Payment: $14.43 by CHK (check), handling I.
production date (405): 2026-08-30.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT399783212, originator 1184634935.
claim statement period start (232): 2026-07-05.
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97150-GP-KX | 1 | $24.63 | $14.43 allowed (B6) $18.04 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $6.59; PR-2 (Patient Responsibility: coinsurance amount) $3.61 |  |
| 2 | 97112-GP-KX | 1 | $54.96 | $0 | CO-236 (Contractual Obligation: procedure/modifier combination not compatible per coding guidelines, bundled) $54.96 | HE N20 (service not payable with other service rendered on the same date) |

Line item control numbers (REF 6R): PA26672725L1, PA26672725L2.
Modifiers on remit lines: GP (under PT plan of care), KX.
Remit claim parties: patient [QC]: JOHN SMITH; MI (member ID) 7A22FM4GH98; rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737.

## Claim as billed (837P)
Claim PA26672725, total charge $79.59, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M1711 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97150-GP-KX | 1 UN | $24.63 | 2026-07-05 | 1 | PA26672725L1 |
| 2 | 97112-GP-KX | 1 UN | $54.96 | 2026-07-05 | 1 | PA26672725L2 |

Modifiers on claim: GP (under PT plan of care), KX.

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: JOHN SMITH; MI (member ID) 7A22FM4GH98; 5478 FRANKLIN AVE; STATEN ISLAND, NY, 10356
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: SARAH CHEN; XX (NPI) 1410042904
- rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737
- Submission reference TRC24068306, dated 2026-07-25 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-07-05.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: JOHN SMITH; MI (member ID) 7A22FM4GH98.
Subject DOB 1943-04-09, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-07-05
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: JOHN SMITH; MI (member ID) 7A22FM4GH98.
Subject DOB 1943-04-09, sex M.
Eligibility exchange reference ELG76829368, dated 2026-09-06 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-07-26, action code WQ, amount $79.59.
D9 (clearinghouse claim number): TRC24068306.
Trace (2 (referenced transaction trace)): TRC24068306.
received date (050): 2026-07-26.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: JOHN SMITH; MI (member ID) 7A22FM4GH98.
Acknowledgment reference ACK24068306, dated 2026-07-26 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-07-05. Dx: Unilateral primary osteoarthritis right knee. 97150 (untimed, 1 unit): group therapeutic procedure. 97112 (16 min): neuromuscular re-education of movement and balance. Total timed minutes: 16. Documentation supports separate services: 97112 occupied a discrete timed interval apart from 97150 and addressed a different region and impairment. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1846349352, interchange 777152929 date 260906 time 0800 version 00501 usage P; group HS control 777152929 date 20260906 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 396510327 date 260906 time 0800 version 00501 usage P; group HB control 396510327 date 20260906 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1846349352, interchange 440548061 date 260725 time 0800 version 00501 usage P; group HC control 440548061 date 20260725 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 704828727 date 260726 time 0800 version 00501 usage P; group HN control 704828727 date 20260726 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 399783212 date 260830 time 0800 version 00501 usage P; group HP control 399783212 date 20260830 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 29
