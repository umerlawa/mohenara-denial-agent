# Case MOH2-000422

Patient PATRICIA ROBINSON, DOB 1945-07-02, sex F, member ID 4CG5NV6EQ35. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-05-02.

## Adjudication outcome (835)
Claim PA21015414: status 4 (denied). Billed $196.17, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2621094156657, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-07-29.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT837996374, originator 1184634935.
claim statement period start (232): 2026-05-02.
Outpatient adjudication remarks (MOA): N111 (no appeal right except duplicate claim/service issue).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97112-GP | 1 | $49.47 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $49.47 |  |
| 2 | 97140-GP | 2 | $96.54 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $96.54 |  |
| 3 | 97530-GP | 1 | $50.16 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $50.16 |  |

Line item control numbers (REF 6R): PA21015414L1, PA21015414L2, PA21015414L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: PATRICIA ROBINSON; MI (member ID) 4CG5NV6EQ35; rendering provider [82]: WEI LEWIS; XX (NPI) 1986021803.

## Claim as billed (837P)
Claim PA21015414, total charge $196.17, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M1712 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97112-GP | 1 UN | $49.47 | 2026-05-02 | 1 | PA21015414L1 |
| 2 | 97140-GP | 2 UN | $96.54 | 2026-05-02 | 1 | PA21015414L2 |
| 3 | 97530-GP | 1 UN | $50.16 | 2026-05-02 | 1 | PA21015414L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: PATRICIA ROBINSON; MI (member ID) 4CG5NV6EQ35; 1399 LINCOLN RD; WILMINGTON, DE, 19862
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: MARCUS WEBB; XX (NPI) 1583494452
- rendering provider [82]: WEI LEWIS; XX (NPI) 1986021803
- Submission reference TRC38394975, dated 2026-07-02 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-05-02.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: PATRICIA ROBINSON; MI (member ID) 4CG5NV6EQ35.
Subject DOB 1945-07-02, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-05-02
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: PATRICIA ROBINSON; MI (member ID) 4CG5NV6EQ35.
Subject DOB 1945-07-02, sex F.
Eligibility exchange reference ELG55968814, dated 2026-07-30 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-07-02, action code WQ, amount $196.17.
D9 (clearinghouse claim number): TRC38394975.
Trace (2 (referenced transaction trace)): TRC38394975.
received date (050): 2026-07-02.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: PATRICIA ROBINSON; MI (member ID) 4CG5NV6EQ35.
Acknowledgment reference ACK38394975, dated 2026-07-02 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-05-02. Dx: Unilateral primary osteoarthritis left knee. 97112 (14 min): neuromuscular re-education of movement and balance. 97140 (31 min): manual therapy (soft tissue and joint mobilization). 97530 (15 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 60. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1846349352, interchange 252747131 date 260730 time 0800 version 00501 usage P; group HS control 252747131 date 20260730 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 847751379 date 260730 time 0800 version 00501 usage P; group HB control 847751379 date 20260730 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1846349352, interchange 282718396 date 260702 time 0800 version 00501 usage P; group HC control 282718396 date 20260702 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 181045412 date 260702 time 0800 version 00501 usage P; group HN control 181045412 date 20260702 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 837996374 date 260729 time 0800 version 00501 usage P; group HP control 837996374 date 20260729 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
