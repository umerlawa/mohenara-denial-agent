# Case MOH2-000166

Patient MARY JOHNSON, DOB 1952-06-17, sex M, member ID 2G92AM5RW23. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-01-19.

## Adjudication outcome (835)
Claim PA26461680: status 4 (denied). Billed $190.78, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2609185534064, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-04-01.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT594371979, originator 1184634935.
claim statement period start (232): 2026-01-19.
Outpatient adjudication remarks (MOA): N111 (no appeal right except duplicate claim/service issue).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $45.47 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $45.47 |  |
| 2 | 97140-GP | 2 | $91.66 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $91.66 |  |
| 3 | 97530-GP | 1 | $53.65 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $53.65 |  |

Line item control numbers (REF 6R): PA26461680L1, PA26461680L2, PA26461680L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: MARY JOHNSON; MI (member ID) 2G92AM5RW23; rendering provider [82]: WEI LEWIS; XX (NPI) 1986021803.

## Claim as billed (837P)
Claim PA26461680, total charge $190.78, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: S93401D (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $45.47 | 2026-01-19 | 1 | PA26461680L1 |
| 2 | 97140-GP | 2 UN | $91.66 | 2026-01-19 | 1 | PA26461680L2 |
| 3 | 97530-GP | 1 UN | $53.65 | 2026-01-19 | 1 | PA26461680L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: MARY JOHNSON; MI (member ID) 2G92AM5RW23; 9000 CHESTNUT AVE; TRENTON, NJ, 08641
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: GRETA LINDQVIST; XX (NPI) 1205658765
- rendering provider [82]: WEI LEWIS; XX (NPI) 1986021803
- Submission reference TRC61112787, dated 2026-03-17 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-01-19.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: MARY JOHNSON; MI (member ID) 2G92AM5RW23.
Subject DOB 1952-06-17, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-01-19
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: MARY JOHNSON; MI (member ID) 2G92AM5RW23.
Subject DOB 1952-06-17, sex M.
Eligibility exchange reference ELG91607363, dated 2026-04-08 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-03-17, action code WQ, amount $190.78.
D9 (clearinghouse claim number): TRC61112787.
Trace (2 (referenced transaction trace)): TRC61112787.
received date (050): 2026-03-17.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: MARY JOHNSON; MI (member ID) 2G92AM5RW23.
Acknowledgment reference ACK61112787, dated 2026-03-17 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-01-19. Dx: Sprain of unspecified ligament of right ankle subsequent encounter. 97110 (14 min): therapeutic exercise for strength and ROM. 97140 (30 min): manual therapy (soft tissue and joint mobilization). 97530 (16 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 60. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1846349352, interchange 338248872 date 260408 time 0800 version 00501 usage P; group HS control 338248872 date 20260408 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 847409792 date 260408 time 0800 version 00501 usage P; group HB control 847409792 date 20260408 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1846349352, interchange 155727277 date 260317 time 0800 version 00501 usage P; group HC control 155727277 date 20260317 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 709804150 date 260317 time 0800 version 00501 usage P; group HN control 709804150 date 20260317 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 594371979 date 260401 time 0800 version 00501 usage P; group HP control 594371979 date 20260401 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
