# Case MOH2-000223

Patient FRANK THOMPSON, DOB 1953-04-10, sex M, member ID 6P70MR0VF07. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-07-01.

## Adjudication outcome (835)
Claim PA22483417: status 4 (denied). Billed $204.26, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2622161325163, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-08-09.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT412901148, originator 1184634935.
claim statement period start (232): 2026-07-01.
Outpatient adjudication remarks (MOA): N435 (exceeds number/frequency approved or allowed within time period).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97112-GP | 2 | $116.2 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $116.2 |  |
| 2 | 97530-GP | 1 | $46.84 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $46.84 |  |
| 3 | 97140-GP | 1 | $41.22 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $41.22 |  |

Line item control numbers (REF 6R): PA22483417L1, PA22483417L2, PA22483417L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: FRANK THOMPSON; MI (member ID) 6P70MR0VF07; rendering provider [82]: WEI LEWIS; XX (NPI) 1986021803.

## Claim as billed (837P)
Claim PA22483417, total charge $204.26, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M48061 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97112-GP | 2 UN | $116.2 | 2026-07-01 | 1 | PA22483417L1 |
| 2 | 97530-GP | 1 UN | $46.84 | 2026-07-01 | 1 | PA22483417L2 |
| 3 | 97140-GP | 1 UN | $41.22 | 2026-07-01 | 1 | PA22483417L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: FRANK THOMPSON; MI (member ID) 6P70MR0VF07; 1707 OAK AVE; TRENTON, NJ, 08668
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: ELENA VASQUEZ; XX (NPI) 1863431679
- rendering provider [82]: WEI LEWIS; XX (NPI) 1986021803
- Submission reference TRC40735098, dated 2026-07-21 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-07-01.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: FRANK THOMPSON; MI (member ID) 6P70MR0VF07.
Subject DOB 1953-04-10, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-07-01
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: FRANK THOMPSON; MI (member ID) 6P70MR0VF07.
Subject DOB 1953-04-10, sex M.
Eligibility exchange reference ELG62692466, dated 2026-08-10 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-07-21, action code WQ, amount $204.26.
D9 (clearinghouse claim number): TRC40735098.
Trace (2 (referenced transaction trace)): TRC40735098.
received date (050): 2026-07-21.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: FRANK THOMPSON; MI (member ID) 6P70MR0VF07.
Acknowledgment reference ACK40735098, dated 2026-07-21 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-07-01. Dx: Spinal stenosis lumbar region without neurogenic claudication. 97112 (29 min): neuromuscular re-education of movement and balance. 97530 (15 min): therapeutic activities (dynamic functional tasks). 97140 (16 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 60. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1846349352, interchange 896034999 date 260810 time 0800 version 00501 usage P; group HS control 896034999 date 20260810 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 617219331 date 260810 time 0800 version 00501 usage P; group HB control 617219331 date 20260810 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1846349352, interchange 921385862 date 260721 time 0800 version 00501 usage P; group HC control 921385862 date 20260721 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 677467014 date 260721 time 0800 version 00501 usage P; group HN control 677467014 date 20260721 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 412901148 date 260809 time 0800 version 00501 usage P; group HP control 412901148 date 20260809 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
