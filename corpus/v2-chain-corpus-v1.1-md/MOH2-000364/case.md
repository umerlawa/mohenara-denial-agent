# Case MOH2-000364

Patient MARY JOHNSON, DOB 1952-06-17, sex M, member ID 2G92AM5RW23. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-05-23.

## Adjudication outcome (835)
Claim PA28821530: status 1 (processed as primary, paid). Billed $83.05, paid $45.43, patient responsibility $11.35. Filing indicator MB (Medicare Part B). Payer claim control 2616358008810, POS 11 (office), frequency 1 (original claim).
Payment: $45.43 by CHK (check), handling I.
production date (405): 2026-06-12.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT834213501, originator 1184634935.
claim statement period start (232): 2026-05-23.
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97116-GP | 1 | $39.49 | $23.25 allowed (B6) $29.06 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $10.43; PR-2 (Patient Responsibility: coinsurance amount) $5.81 |  |
| 2 | 97140-GP | 1 | $43.56 | $22.18 allowed (B6) $27.72 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $15.84; PR-2 (Patient Responsibility: coinsurance amount) $5.54 |  |

Line item control numbers (REF 6R): PA28821530L1, PA28821530L2.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: MARY JOHNSON; MI (member ID) 2G92AM5RW23; rendering provider [82]: WEI LEWIS; XX (NPI) 1986021803.

## Claim as billed (837P)
Claim PA28821530, total charge $83.05, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: S93401D (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97116-GP | 1 UN | $39.49 | 2026-05-23 | 1 | PA28821530L1 |
| 2 | 97140-GP | 1 UN | $43.56 | 2026-05-23 | 1 | PA28821530L2 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: MARY JOHNSON; MI (member ID) 2G92AM5RW23; 9000 CHESTNUT AVE; TRENTON, NJ, 08641
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: GRETA LINDQVIST; XX (NPI) 1205658765
- rendering provider [82]: WEI LEWIS; XX (NPI) 1986021803
- Submission reference TRC69499975, dated 2026-05-26 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-05-23.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: MARY JOHNSON; MI (member ID) 2G92AM5RW23.
Subject DOB 1952-06-17, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-05-23
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: MARY JOHNSON; MI (member ID) 2G92AM5RW23.
Subject DOB 1952-06-17, sex M.
Eligibility exchange reference ELG34194223, dated 2026-06-19 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-05-26, action code WQ, amount $83.05.
D9 (clearinghouse claim number): TRC69499975.
Trace (2 (referenced transaction trace)): TRC69499975.
received date (050): 2026-05-26.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: MARY JOHNSON; MI (member ID) 2G92AM5RW23.
Acknowledgment reference ACK69499975, dated 2026-05-26 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-05-23. Dx: Sprain of unspecified ligament of right ankle subsequent encounter. 97116 (15 min): gait training with assistive device progression. 97140 (14 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 29. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1846349352, interchange 350216999 date 260619 time 0800 version 00501 usage P; group HS control 350216999 date 20260619 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 484825976 date 260619 time 0800 version 00501 usage P; group HB control 484825976 date 20260619 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1846349352, interchange 727855708 date 260526 time 0800 version 00501 usage P; group HC control 727855708 date 20260526 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 154971436 date 260526 time 0800 version 00501 usage P; group HN control 154971436 date 20260526 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 834213501 date 260612 time 0800 version 00501 usage P; group HP control 834213501 date 20260612 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 30
