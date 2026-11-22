# Case MOH2-000312

Patient PATRICIA ROBINSON, DOB 1945-07-02, sex F, member ID 4CG5NV6EQ35. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-01-15.

## Adjudication outcome (835)
Claim PA21473350: status 4 (denied). Billed $178.46, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2608278361911, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-03-23.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT258952787, originator 1184634935.
claim statement period start (232): 2026-01-15.
Outpatient adjudication remarks (MOA): N111 (no appeal right except duplicate claim/service issue).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 | $76.43 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $76.43 |  |
| 2 | 97140-GP | 1 | $48.11 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $48.11 |  |
| 3 | 97530-GP | 1 | $53.92 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $53.92 |  |

Line item control numbers (REF 6R): PA21473350L1, PA21473350L2, PA21473350L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: PATRICIA ROBINSON; MI (member ID) 4CG5NV6EQ35; rendering provider [82]: WEI LEWIS; XX (NPI) 1986021803.

## Claim as billed (837P)
Claim PA21473350, total charge $178.46, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M1712 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 UN | $76.43 | 2026-01-15 | 1 | PA21473350L1 |
| 2 | 97140-GP | 1 UN | $48.11 | 2026-01-15 | 1 | PA21473350L2 |
| 3 | 97530-GP | 1 UN | $53.92 | 2026-01-15 | 1 | PA21473350L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: PATRICIA ROBINSON; MI (member ID) 4CG5NV6EQ35; 1399 LINCOLN RD; WILMINGTON, DE, 19862
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: MARCUS WEBB; XX (NPI) 1583494452
- rendering provider [82]: WEI LEWIS; XX (NPI) 1986021803
- Submission reference TRC46190199, dated 2026-03-01 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-01-15.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: PATRICIA ROBINSON; MI (member ID) 4CG5NV6EQ35.
Subject DOB 1945-07-02, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-01-15
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: PATRICIA ROBINSON; MI (member ID) 4CG5NV6EQ35.
Subject DOB 1945-07-02, sex F.
Eligibility exchange reference ELG79742036, dated 2026-03-30 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-03-03, action code WQ, amount $178.46.
D9 (clearinghouse claim number): TRC46190199.
Trace (2 (referenced transaction trace)): TRC46190199.
received date (050): 2026-03-03.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: PATRICIA ROBINSON; MI (member ID) 4CG5NV6EQ35.
Acknowledgment reference ACK46190199, dated 2026-03-03 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-01-15. Dx: Unilateral primary osteoarthritis left knee. 97110 (29 min): therapeutic exercise for strength and ROM. 97140 (15 min): manual therapy (soft tissue and joint mobilization). 97530 (14 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 58. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1846349352, interchange 186545319 date 260330 time 0800 version 00501 usage P; group HS control 186545319 date 20260330 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 494490436 date 260330 time 0800 version 00501 usage P; group HB control 494490436 date 20260330 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1846349352, interchange 265029782 date 260301 time 0800 version 00501 usage P; group HC control 265029782 date 20260301 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 925716449 date 260303 time 0800 version 00501 usage P; group HN control 925716449 date 20260303 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 258952787 date 260323 time 0800 version 00501 usage P; group HP control 258952787 date 20260323 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
