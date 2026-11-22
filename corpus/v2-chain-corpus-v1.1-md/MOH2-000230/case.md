# Case MOH2-000230

Patient JOHN SMITH, DOB 1943-04-09, sex M, member ID 7A22FM4GH98. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-06-03.

## Adjudication outcome (835)
Claim PA23329559: status 1 (processed as primary, paid). Billed $471.66, paid $52.36, patient responsibility $13.1. Filing indicator MB (Medicare Part B). Payer claim control 2620096143661, POS 11 (office), frequency 1 (original claim).
Payment: $52.36 by CHK (check), handling I.
production date (405): 2026-07-19.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT675780561, originator 1184634935.
claim statement period start (232): 2026-06-03.
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 9 | $360.94 | $0 | CO-151 (Contractual Obligation: information does not support this many/frequency of services) $360.94 | HE N362 (the number of days or units exceeds the acceptable maximum) |
| 2 | 97112-GP | 1 | $55.35 | $26.18 allowed (B6) $32.73 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $22.62; PR-2 (Patient Responsibility: coinsurance amount) $6.55 |  |
| 3 | 97112-GP | 1 | $55.37 | $26.18 allowed (B6) $32.73 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $22.64; PR-2 (Patient Responsibility: coinsurance amount) $6.55 |  |

Line item control numbers (REF 6R): PA23329559L1, PA23329559L2, PA23329559L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: JOHN SMITH; MI (member ID) 7A22FM4GH98; rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737.

## Claim as billed (837P)
Claim PA23329559, total charge $471.66, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M1711 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 9 UN | $360.94 | 2026-06-03 | 1 | PA23329559L1 |
| 2 | 97112-GP | 1 UN | $55.35 | 2026-06-03 | 1 | PA23329559L2 |
| 3 | 97112-GP | 1 UN | $55.37 | 2026-06-03 | 1 | PA23329559L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: JOHN SMITH; MI (member ID) 7A22FM4GH98; 5478 FRANKLIN AVE; STATEN ISLAND, NY, 10356
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: SARAH CHEN; XX (NPI) 1410042904
- rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737
- Submission reference TRC37609909, dated 2026-06-15 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-06-03.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: JOHN SMITH; MI (member ID) 7A22FM4GH98.
Subject DOB 1943-04-09, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-06-03
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: JOHN SMITH; MI (member ID) 7A22FM4GH98.
Subject DOB 1943-04-09, sex M.
Eligibility exchange reference ELG87933748, dated 2026-07-22 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-06-15, action code WQ, amount $471.66.
D9 (clearinghouse claim number): TRC37609909.
Trace (2 (referenced transaction trace)): TRC37609909.
received date (050): 2026-06-15.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: JOHN SMITH; MI (member ID) 7A22FM4GH98.
Acknowledgment reference ACK37609909, dated 2026-06-15 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-06-03. Dx: Unilateral primary osteoarthritis right knee. 97110 (30 min): therapeutic exercise for strength and ROM. 97112 (16 min): neuromuscular re-education of movement and balance. 97112 (16 min): neuromuscular re-education of movement and balance. Total timed minutes: 62. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1846349352, interchange 548286145 date 260722 time 0800 version 00501 usage P; group HS control 548286145 date 20260722 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 619503625 date 260722 time 0800 version 00501 usage P; group HB control 619503625 date 20260722 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1846349352, interchange 561046548 date 260615 time 0800 version 00501 usage P; group HC control 561046548 date 20260615 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 789019711 date 260615 time 0800 version 00501 usage P; group HN control 789019711 date 20260615 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 675780561 date 260719 time 0800 version 00501 usage P; group HP control 675780561 date 20260719 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 35
