# Case MOH2-000180

Patient JAMES GONZALEZ, DOB 1941-04-24, sex M, member ID 6AN7D82UC08. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-03-06.

## Adjudication outcome (835)
Claim PA23749998: status 4 (denied). Billed $149.72, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2613267759366, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-05-12.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT839977034, originator 1184634935.
claim statement period start (232): 2026-03-06.
Outpatient adjudication remarks (MOA): N111 (no appeal right except duplicate claim/service issue).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $47.29 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $47.29 |  |
| 2 | 97112-GP | 1 | $57.9 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $57.9 |  |
| 3 | 97140-GP | 1 | $44.53 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $44.53 |  |

Line item control numbers (REF 6R): PA23749998L1, PA23749998L2, PA23749998L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: JAMES GONZALEZ; MI (member ID) 6AN7D82UC08; rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737.

## Claim as billed (837P)
Claim PA23749998, total charge $149.72, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: S43401D (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $47.29 | 2026-03-06 | 1 | PA23749998L1 |
| 2 | 97112-GP | 1 UN | $57.9 | 2026-03-06 | 1 | PA23749998L2 |
| 3 | 97140-GP | 1 UN | $44.53 | 2026-03-06 | 1 | PA23749998L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: JAMES GONZALEZ; MI (member ID) 6AN7D82UC08; 3233 LINCOLN ST; TRENTON, NJ, 08600
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: FATIMA AL-RASHID; XX (NPI) 1333183066
- rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737
- Submission reference TRC89305690, dated 2026-04-27 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-03-06.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: JAMES GONZALEZ; MI (member ID) 6AN7D82UC08.
Subject DOB 1941-04-24, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-03-06
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: JAMES GONZALEZ; MI (member ID) 6AN7D82UC08.
Subject DOB 1941-04-24, sex M.
Eligibility exchange reference ELG34265221, dated 2026-05-17 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-04-29, action code WQ, amount $149.72.
D9 (clearinghouse claim number): TRC89305690.
Trace (2 (referenced transaction trace)): TRC89305690.
received date (050): 2026-04-29.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: JAMES GONZALEZ; MI (member ID) 6AN7D82UC08.
Acknowledgment reference ACK89305690, dated 2026-04-29 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-03-06. Dx: Unspecified sprain of right shoulder joint subsequent encounter. 97110 (16 min): therapeutic exercise for strength and ROM. 97112 (15 min): neuromuscular re-education of movement and balance. 97140 (16 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 47. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1846349352, interchange 366134957 date 260517 time 0800 version 00501 usage P; group HS control 366134957 date 20260517 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 518949036 date 260517 time 0800 version 00501 usage P; group HB control 518949036 date 20260517 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1846349352, interchange 483297940 date 260427 time 0800 version 00501 usage P; group HC control 483297940 date 20260427 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 524427041 date 260429 time 0800 version 00501 usage P; group HN control 524427041 date 20260429 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 839977034 date 260512 time 0800 version 00501 usage P; group HP control 839977034 date 20260512 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
