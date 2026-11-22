# Case MOH2-000508

Patient JAMES GONZALEZ, DOB 1941-04-24, sex M, member ID 6AN7D82UC08. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-06-20.

## Adjudication outcome (835)
Claim PA25239145: status 4 (denied). Billed $144.5, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2622272840923, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-08-10.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT915170253, originator 1184634935.
claim statement period start (232): 2026-06-20.
Outpatient adjudication remarks (MOA): N435 (exceeds number/frequency approved or allowed within time period).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97112-GP | 1 | $57.8 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $57.8 |  |
| 2 | 97140-GP | 1 | $45.06 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $45.06 |  |
| 3 | 97140-GP | 1 | $41.64 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $41.64 |  |

Line item control numbers (REF 6R): PA25239145L1, PA25239145L2, PA25239145L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: JAMES GONZALEZ; MI (member ID) 6AN7D82UC08; rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737.

## Claim as billed (837P)
Claim PA25239145, total charge $144.5, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: S43401D (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97112-GP | 1 UN | $57.8 | 2026-06-20 | 1 | PA25239145L1 |
| 2 | 97140-GP | 1 UN | $45.06 | 2026-06-20 | 1 | PA25239145L2 |
| 3 | 97140-GP | 1 UN | $41.64 | 2026-06-20 | 1 | PA25239145L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: JAMES GONZALEZ; MI (member ID) 6AN7D82UC08; 3233 LINCOLN ST; TRENTON, NJ, 08600
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: FATIMA AL-RASHID; XX (NPI) 1333183066
- rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737
- Submission reference TRC29305071, dated 2026-07-06 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-06-20.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: JAMES GONZALEZ; MI (member ID) 6AN7D82UC08.
Subject DOB 1941-04-24, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-06-20
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: JAMES GONZALEZ; MI (member ID) 6AN7D82UC08.
Subject DOB 1941-04-24, sex M.
Eligibility exchange reference ELG32275247, dated 2026-08-12 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-07-07, action code WQ, amount $144.5.
D9 (clearinghouse claim number): TRC29305071.
Trace (2 (referenced transaction trace)): TRC29305071.
received date (050): 2026-07-07.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: JAMES GONZALEZ; MI (member ID) 6AN7D82UC08.
Acknowledgment reference ACK29305071, dated 2026-07-07 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-06-20. Dx: Unspecified sprain of right shoulder joint subsequent encounter. 97112 (14 min): neuromuscular re-education of movement and balance. 97140 (16 min): manual therapy (soft tissue and joint mobilization). 97140 (15 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 45. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1846349352, interchange 829385900 date 260812 time 0800 version 00501 usage P; group HS control 829385900 date 20260812 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 707420896 date 260812 time 0800 version 00501 usage P; group HB control 707420896 date 20260812 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1846349352, interchange 607191445 date 260706 time 0800 version 00501 usage P; group HC control 607191445 date 20260706 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 355444704 date 260707 time 0800 version 00501 usage P; group HN control 355444704 date 20260707 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 915170253 date 260810 time 0800 version 00501 usage P; group HP control 915170253 date 20260810 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
