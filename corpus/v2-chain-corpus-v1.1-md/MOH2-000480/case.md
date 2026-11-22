# Case MOH2-000480

Patient JAMES GONZALEZ, DOB 1941-04-24, sex M, member ID 6AN7D82UC08. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-03-09.

## Adjudication outcome (835)
Claim PA29084751: status 4 (denied). Billed $182.75, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2610755377910, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-04-17.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT274265280, originator 1184634935.
claim statement period start (232): 2026-03-09.
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110 | 1 | $45.71 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $45.71 | HE N822 (missing procedure modifier(s)) |
| 2 | 97112 | 2 | $98.66 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $98.66 | HE N822 (missing procedure modifier(s)) |
| 3 | 97140 | 1 | $38.38 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $38.38 | HE N822 (missing procedure modifier(s)) |

Line item control numbers (REF 6R): PA29084751L1, PA29084751L2, PA29084751L3.
Remit claim parties: patient [QC]: JAMES GONZALEZ; MI (member ID) 6AN7D82UC08; rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737.

## Claim as billed (837P)
Claim PA29084751, total charge $182.75, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: S43401D (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110 | 1 UN | $45.71 | 2026-03-09 | 1 | PA29084751L1 |
| 2 | 97112 | 2 UN | $98.66 | 2026-03-09 | 1 | PA29084751L2 |
| 3 | 97140 | 1 UN | $38.38 | 2026-03-09 | 1 | PA29084751L3 |

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: JAMES GONZALEZ; MI (member ID) 6AN7D82UC08; 3233 LINCOLN ST; TRENTON, NJ, 08600
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: FATIMA AL-RASHID; XX (NPI) 1333183066
- rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737
- Submission reference TRC20288100, dated 2026-03-28 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-03-09.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: JAMES GONZALEZ; MI (member ID) 6AN7D82UC08.
Subject DOB 1941-04-24, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-03-09
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: JAMES GONZALEZ; MI (member ID) 6AN7D82UC08.
Subject DOB 1941-04-24, sex M.
Eligibility exchange reference ELG60768707, dated 2026-04-23 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-03-28, action code WQ, amount $182.75.
D9 (clearinghouse claim number): TRC20288100.
Trace (2 (referenced transaction trace)): TRC20288100.
received date (050): 2026-03-28.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: JAMES GONZALEZ; MI (member ID) 6AN7D82UC08.
Acknowledgment reference ACK20288100, dated 2026-03-28 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-03-09. Dx: Unspecified sprain of right shoulder joint subsequent encounter. 97110 (15 min): therapeutic exercise for strength and ROM. 97112 (29 min): neuromuscular re-education of movement and balance. 97140 (16 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 60. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1846349352, interchange 425797462 date 260423 time 0800 version 00501 usage P; group HS control 425797462 date 20260423 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 817399619 date 260423 time 0800 version 00501 usage P; group HB control 817399619 date 20260423 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1846349352, interchange 393262238 date 260328 time 0800 version 00501 usage P; group HC control 393262238 date 20260328 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 727439192 date 260328 time 0800 version 00501 usage P; group HN control 727439192 date 20260328 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 274265280 date 260417 time 0800 version 00501 usage P; group HP control 274265280 date 20260417 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 33
