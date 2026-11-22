# Case MOH2-000114

Patient FRANK THOMPSON, DOB 1953-04-10, sex M, member ID 6P70MR0VF07. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-06-26.

## Adjudication outcome (835)
Claim PA21184933: status 4 (denied). Billed $130, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2624712696686, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-09-04.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT217175189, originator 1184634935.
claim statement period start (232): 2026-06-26.
Outpatient adjudication remarks (MOA): N111 (no appeal right except duplicate claim/service issue).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97140-GP-KX | 1 | $44.46 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $44.46 |  |
| 2 | 97112-GP-KX | 2 | $85.54 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $85.54 |  |

Line item control numbers (REF 6R): PA21184933L1, PA21184933L2.
Modifiers on remit lines: GP (under PT plan of care), KX.
Remit claim parties: patient [QC]: FRANK THOMPSON; MI (member ID) 6P70MR0VF07; rendering provider [82]: WEI LEWIS; XX (NPI) 1986021803.

## Claim as billed (837P)
Claim PA21184933, total charge $130, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M48061 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97140-GP-KX | 1 UN | $44.46 | 2026-06-26 | 1 | PA21184933L1 |
| 2 | 97112-GP-KX | 2 UN | $85.54 | 2026-06-26 | 1 | PA21184933L2 |

Modifiers on claim: GP (under PT plan of care), KX.

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: FRANK THOMPSON; MI (member ID) 6P70MR0VF07; 1707 OAK AVE; TRENTON, NJ, 08668
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: ELENA VASQUEZ; XX (NPI) 1863431679
- rendering provider [82]: WEI LEWIS; XX (NPI) 1986021803
- Submission reference TRC68510856, dated 2026-08-19 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-06-26.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: FRANK THOMPSON; MI (member ID) 6P70MR0VF07.
Subject DOB 1953-04-10, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-06-26
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: FRANK THOMPSON; MI (member ID) 6P70MR0VF07.
Subject DOB 1953-04-10, sex M.
Eligibility exchange reference ELG51726543, dated 2026-09-09 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-08-20, action code WQ, amount $130.
D9 (clearinghouse claim number): TRC68510856.
Trace (2 (referenced transaction trace)): TRC68510856.
received date (050): 2026-08-20.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: FRANK THOMPSON; MI (member ID) 6P70MR0VF07.
Acknowledgment reference ACK68510856, dated 2026-08-20 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-06-26. Dx: Spinal stenosis lumbar region without neurogenic claudication. 97140 (14 min): manual therapy (soft tissue and joint mobilization). 97112 (30 min): neuromuscular re-education of movement and balance. Total timed minutes: 44. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1846349352, interchange 297401854 date 260909 time 0800 version 00501 usage P; group HS control 297401854 date 20260909 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 491472438 date 260909 time 0800 version 00501 usage P; group HB control 491472438 date 20260909 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1846349352, interchange 224016954 date 260819 time 0800 version 00501 usage P; group HC control 224016954 date 20260819 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 138767446 date 260820 time 0800 version 00501 usage P; group HN control 138767446 date 20260820 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 217175189 date 260904 time 0800 version 00501 usage P; group HP control 217175189 date 20260904 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 27
