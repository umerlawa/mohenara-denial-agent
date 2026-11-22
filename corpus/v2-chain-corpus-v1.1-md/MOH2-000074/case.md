# Case MOH2-000074

Patient FRANK THOMPSON, DOB 1953-04-10, sex M, member ID 6P70MR0VF07. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-06-06.

## Adjudication outcome (835)
Claim PA28911883: status 4 (denied). Billed $145.65, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2620336527563, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-07-22.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT918441461, originator 1184634935.
claim statement period start (232): 2026-06-06.
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97530 | 1 | $57.74 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $57.74 | HE N822 (missing procedure modifier(s)) |
| 2 | 97110 | 1 | $49.62 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $49.62 | HE N822 (missing procedure modifier(s)) |
| 3 | 97140 | 1 | $38.29 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $38.29 | HE N822 (missing procedure modifier(s)) |

Line item control numbers (REF 6R): PA28911883L1, PA28911883L2, PA28911883L3.
Remit claim parties: patient [QC]: FRANK THOMPSON; MI (member ID) 6P70MR0VF07; rendering provider [82]: WEI LEWIS; XX (NPI) 1986021803.

## Claim as billed (837P)
Claim PA28911883, total charge $145.65, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M48061 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97530 | 1 UN | $57.74 | 2026-06-06 | 1 | PA28911883L1 |
| 2 | 97110 | 1 UN | $49.62 | 2026-06-06 | 1 | PA28911883L2 |
| 3 | 97140 | 1 UN | $38.29 | 2026-06-06 | 1 | PA28911883L3 |

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: FRANK THOMPSON; MI (member ID) 6P70MR0VF07; 1707 OAK AVE; TRENTON, NJ, 08668
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: ELENA VASQUEZ; XX (NPI) 1863431679
- rendering provider [82]: WEI LEWIS; XX (NPI) 1986021803
- Submission reference TRC53921373, dated 2026-06-23 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-06-06.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: FRANK THOMPSON; MI (member ID) 6P70MR0VF07.
Subject DOB 1953-04-10, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-06-06
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: FRANK THOMPSON; MI (member ID) 6P70MR0VF07.
Subject DOB 1953-04-10, sex M.
Eligibility exchange reference ELG84216519, dated 2026-07-27 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-06-25, action code WQ, amount $145.65.
D9 (clearinghouse claim number): TRC53921373.
Trace (2 (referenced transaction trace)): TRC53921373.
received date (050): 2026-06-25.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: FRANK THOMPSON; MI (member ID) 6P70MR0VF07.
Acknowledgment reference ACK53921373, dated 2026-06-25 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-06-06. Dx: Spinal stenosis lumbar region without neurogenic claudication. 97530 (14 min): therapeutic activities (dynamic functional tasks). 97110 (15 min): therapeutic exercise for strength and ROM. 97140 (15 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 44. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1846349352, interchange 924868559 date 260727 time 0800 version 00501 usage P; group HS control 924868559 date 20260727 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 172452452 date 260727 time 0800 version 00501 usage P; group HB control 172452452 date 20260727 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1846349352, interchange 675095252 date 260623 time 0800 version 00501 usage P; group HC control 675095252 date 20260623 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 896077166 date 260625 time 0800 version 00501 usage P; group HN control 896077166 date 20260625 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 918441461 date 260722 time 0800 version 00501 usage P; group HP control 918441461 date 20260722 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 33
