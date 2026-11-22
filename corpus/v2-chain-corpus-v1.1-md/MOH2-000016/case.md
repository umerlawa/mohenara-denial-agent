# Case MOH2-000016

Patient JOHN SMITH, DOB 1943-04-09, sex M, member ID 7A22FM4GH98. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-02-22.

## Adjudication outcome (835)
Claim PA25509241: status 1 (processed as primary, paid). Billed $803.83, paid $153.91, patient responsibility $38.47. Filing indicator MB (Medicare Part B). Payer claim control 2609114464683, POS 11 (office), frequency 1 (original claim).
Payment: $153.91 by CHK (check), handling I.
production date (405): 2026-04-01.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT830399574, originator 1184634935.
claim statement period start (232): 2026-02-22.
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $43.93 | $23.25 allowed (B6) $29.06 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $14.87; PR-2 (Patient Responsibility: coinsurance amount) $5.81 |  |
| 2 | 97112-GP | 2 | $93.29 | $52.37 allowed (B6) $65.46 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $27.83; PR-2 (Patient Responsibility: coinsurance amount) $13.09 |  |
| 3 | 97140-GP | 1 | $45.77 | $22.18 allowed (B6) $27.72 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $18.05; PR-2 (Patient Responsibility: coinsurance amount) $5.54 |  |
| 4 | 97530-GP | 2 | $104.17 | $56.11 allowed (B6) $70.14 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $34.03; PR-2 (Patient Responsibility: coinsurance amount) $14.03 |  |
| 5 | 97535-GP | 11 | $516.67 | $0 | CO-151 (Contractual Obligation: information does not support this many/frequency of services) $516.67 | HE N362 (the number of days or units exceeds the acceptable maximum) |

Line item control numbers (REF 6R): PA25509241L1, PA25509241L2, PA25509241L3, PA25509241L4, PA25509241L5.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: JOHN SMITH; MI (member ID) 7A22FM4GH98; rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737.

## Claim as billed (837P)
Claim PA25509241, total charge $803.83, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M1711 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $43.93 | 2026-02-22 | 1 | PA25509241L1 |
| 2 | 97112-GP | 2 UN | $93.29 | 2026-02-22 | 1 | PA25509241L2 |
| 3 | 97140-GP | 1 UN | $45.77 | 2026-02-22 | 1 | PA25509241L3 |
| 4 | 97530-GP | 2 UN | $104.17 | 2026-02-22 | 1 | PA25509241L4 |
| 5 | 97535-GP | 11 UN | $516.67 | 2026-02-22 | 1 | PA25509241L5 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: JOHN SMITH; MI (member ID) 7A22FM4GH98; 5478 FRANKLIN AVE; STATEN ISLAND, NY, 10356
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: SARAH CHEN; XX (NPI) 1410042904
- rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737
- Submission reference TRC51088857, dated 2026-03-14 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-02-22.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: JOHN SMITH; MI (member ID) 7A22FM4GH98.
Subject DOB 1943-04-09, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-02-22
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: JOHN SMITH; MI (member ID) 7A22FM4GH98.
Subject DOB 1943-04-09, sex M.
Eligibility exchange reference ELG76946113, dated 2026-04-08 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-03-16, action code WQ, amount $803.83.
D9 (clearinghouse claim number): TRC51088857.
Trace (2 (referenced transaction trace)): TRC51088857.
received date (050): 2026-03-16.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: JOHN SMITH; MI (member ID) 7A22FM4GH98.
Acknowledgment reference ACK51088857, dated 2026-03-16 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-02-22. Dx: Unilateral primary osteoarthritis right knee. 97110 (14 min): therapeutic exercise for strength and ROM. 97112 (31 min): neuromuscular re-education of movement and balance. 97140 (15 min): manual therapy (soft tissue and joint mobilization). 97530 (30 min): therapeutic activities (dynamic functional tasks). 97535 (14 min): self-care/home management training. Total timed minutes: 104. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1846349352, interchange 300094455 date 260408 time 0800 version 00501 usage P; group HS control 300094455 date 20260408 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 589343363 date 260408 time 0800 version 00501 usage P; group HB control 589343363 date 20260408 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1846349352, interchange 200408753 date 260314 time 0800 version 00501 usage P; group HC control 200408753 date 20260314 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 42
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 981405703 date 260316 time 0800 version 00501 usage P; group HN control 981405703 date 20260316 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 830399574 date 260401 time 0800 version 00501 usage P; group HP control 830399574 date 20260401 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 47
