# Case MOH2-000400

Patient JAMES GONZALEZ, DOB 1941-04-24, sex M, member ID 6AN7D82UC08. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-02-09.

## Adjudication outcome (835)
Claim PA23936565: status 4 (denied). Billed $140.46, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2609412696255, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-04-04.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT980659389, originator 1184634935.
claim statement period start (232): 2026-02-09.
Outpatient adjudication remarks (MOA): N111 (no appeal right except duplicate claim/service issue).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $46.36 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $46.36 |  |
| 2 | 97140-GP | 1 | $43.29 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $43.29 |  |
| 3 | 97530-GP | 1 | $50.81 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $50.81 |  |

Line item control numbers (REF 6R): PA23936565L1, PA23936565L2, PA23936565L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: JAMES GONZALEZ; MI (member ID) 6AN7D82UC08; rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737.

## Claim as billed (837P)
Claim PA23936565, total charge $140.46, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: S43401D (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $46.36 | 2026-02-09 | 1 | PA23936565L1 |
| 2 | 97140-GP | 1 UN | $43.29 | 2026-02-09 | 1 | PA23936565L2 |
| 3 | 97530-GP | 1 UN | $50.81 | 2026-02-09 | 1 | PA23936565L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: JAMES GONZALEZ; MI (member ID) 6AN7D82UC08; 3233 LINCOLN ST; TRENTON, NJ, 08600
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: FATIMA AL-RASHID; XX (NPI) 1333183066
- rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737
- Submission reference TRC82301661, dated 2026-03-17 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-02-09.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: JAMES GONZALEZ; MI (member ID) 6AN7D82UC08.
Subject DOB 1941-04-24, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-02-09
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: JAMES GONZALEZ; MI (member ID) 6AN7D82UC08.
Subject DOB 1941-04-24, sex M.
Eligibility exchange reference ELG81392727, dated 2026-04-10 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-03-18, action code WQ, amount $140.46.
D9 (clearinghouse claim number): TRC82301661.
Trace (2 (referenced transaction trace)): TRC82301661.
received date (050): 2026-03-18.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: JAMES GONZALEZ; MI (member ID) 6AN7D82UC08.
Acknowledgment reference ACK82301661, dated 2026-03-18 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-02-09. Dx: Unspecified sprain of right shoulder joint subsequent encounter. 97110 (16 min): therapeutic exercise for strength and ROM. 97140 (16 min): manual therapy (soft tissue and joint mobilization). 97530 (15 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 47. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1846349352, interchange 320424266 date 260410 time 0800 version 00501 usage P; group HS control 320424266 date 20260410 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 616598000 date 260410 time 0800 version 00501 usage P; group HB control 616598000 date 20260410 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1846349352, interchange 380726550 date 260317 time 0800 version 00501 usage P; group HC control 380726550 date 20260317 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 729950728 date 260318 time 0800 version 00501 usage P; group HN control 729950728 date 20260318 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 980659389 date 260404 time 0800 version 00501 usage P; group HP control 980659389 date 20260404 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
