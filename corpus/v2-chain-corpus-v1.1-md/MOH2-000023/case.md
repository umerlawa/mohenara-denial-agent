# Case MOH2-000023

Patient THOMAS HARRIS, DOB 1954-02-25, sex M, member ID 7AM6NJ4QA31. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-01-14.

## Adjudication outcome (835)
Claim PA29538424: status 4 (denied). Billed $173.21, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2606792332848, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-03-08.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT249920632, originator 1184634935.
claim statement period start (232): 2026-01-14.
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110 | 1 | $40.19 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $40.19 | HE N822 (missing procedure modifier(s)) |
| 2 | 97112 | 1 | $51.12 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $51.12 | HE N822 (missing procedure modifier(s)) |
| 3 | 97140 | 2 | $81.9 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $81.9 | HE N822 (missing procedure modifier(s)) |

Line item control numbers (REF 6R): PA29538424L1, PA29538424L2, PA29538424L3.
Remit claim parties: patient [QC]: THOMAS HARRIS; MI (member ID) 7AM6NJ4QA31; rendering provider [82]: JOSEPH ANDERSON; XX (NPI) 1260849754.

## Claim as billed (837P)
Claim PA29538424, total charge $173.21, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25511 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110 | 1 UN | $40.19 | 2026-01-14 | 1 | PA29538424L1 |
| 2 | 97112 | 1 UN | $51.12 | 2026-01-14 | 1 | PA29538424L2 |
| 3 | 97140 | 2 UN | $81.9 | 2026-01-14 | 1 | PA29538424L3 |

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: THOMAS HARRIS; MI (member ID) 7AM6NJ4QA31; 7202 WILLOW RD; TRENTON, NJ, 08651
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: PRIYA NAIR; XX (NPI) 1903307855
- rendering provider [82]: JOSEPH ANDERSON; XX (NPI) 1260849754
- Submission reference TRC59867447, dated 2026-02-02 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-01-14.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: THOMAS HARRIS; MI (member ID) 7AM6NJ4QA31.
Subject DOB 1954-02-25, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-01-14
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: THOMAS HARRIS; MI (member ID) 7AM6NJ4QA31.
Subject DOB 1954-02-25, sex M.
Eligibility exchange reference ELG94464716, dated 2026-03-10 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-02-03, action code WQ, amount $173.21.
D9 (clearinghouse claim number): TRC59867447.
Trace (2 (referenced transaction trace)): TRC59867447.
received date (050): 2026-02-03.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: THOMAS HARRIS; MI (member ID) 7AM6NJ4QA31.
Acknowledgment reference ACK59867447, dated 2026-02-03 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-01-14. Dx: Pain in right shoulder. 97110 (14 min): therapeutic exercise for strength and ROM. 97112 (16 min): neuromuscular re-education of movement and balance. 97140 (30 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 60. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1846349352, interchange 426680048 date 260310 time 0800 version 00501 usage P; group HS control 426680048 date 20260310 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 398387110 date 260310 time 0800 version 00501 usage P; group HB control 398387110 date 20260310 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1846349352, interchange 793025507 date 260202 time 0800 version 00501 usage P; group HC control 793025507 date 20260202 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 323595632 date 260203 time 0800 version 00501 usage P; group HN control 323595632 date 20260203 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 249920632 date 260308 time 0800 version 00501 usage P; group HP control 249920632 date 20260308 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 33
