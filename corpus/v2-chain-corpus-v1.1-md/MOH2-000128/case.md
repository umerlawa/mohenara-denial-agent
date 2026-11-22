# Case MOH2-000128

Patient MICHAEL HARRIS, DOB 1958-01-26, sex M, member ID 3KN4PT4QF96. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-02-22.

## Adjudication outcome (835)
Claim PA23903967: status 4 (denied). Billed $189.11, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2612281173087, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-05-02.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT327864337, originator 1184634935.
claim statement period start (232): 2026-02-22.
Outpatient adjudication remarks (MOA): N111 (no appeal right except duplicate claim/service issue).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 | $95.46 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $95.46 |  |
| 2 | 97140-GP | 1 | $44.45 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $44.45 |  |
| 3 | 97530-GP | 1 | $49.2 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $49.2 |  |

Line item control numbers (REF 6R): PA23903967L1, PA23903967L2, PA23903967L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: MICHAEL HARRIS; MI (member ID) 3KN4PT4QF96; rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737.

## Claim as billed (837P)
Claim PA23903967, total charge $189.11, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: S335XXD (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 UN | $95.46 | 2026-02-22 | 1 | PA23903967L1 |
| 2 | 97140-GP | 1 UN | $44.45 | 2026-02-22 | 1 | PA23903967L2 |
| 3 | 97530-GP | 1 UN | $49.2 | 2026-02-22 | 1 | PA23903967L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: MICHAEL HARRIS; MI (member ID) 3KN4PT4QF96; 9218 MAPLE LN; PHILADELPHIA, PA, 19156
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: GRETA LINDQVIST; XX (NPI) 1205658765
- rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737
- Submission reference TRC23251142, dated 2026-04-03 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-02-22.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: MICHAEL HARRIS; MI (member ID) 3KN4PT4QF96.
Subject DOB 1958-01-26, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-02-22
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: MICHAEL HARRIS; MI (member ID) 3KN4PT4QF96.
Subject DOB 1958-01-26, sex M.
Eligibility exchange reference ELG66278170, dated 2026-05-05 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-04-03, action code WQ, amount $189.11.
D9 (clearinghouse claim number): TRC23251142.
Trace (2 (referenced transaction trace)): TRC23251142.
received date (050): 2026-04-03.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: MICHAEL HARRIS; MI (member ID) 3KN4PT4QF96.
Acknowledgment reference ACK23251142, dated 2026-04-03 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-02-22. Dx: Sprain of ligaments of lumbar spine subsequent encounter. 97110 (29 min): therapeutic exercise for strength and ROM. 97140 (14 min): manual therapy (soft tissue and joint mobilization). 97530 (15 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 58. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1846349352, interchange 592773679 date 260505 time 0800 version 00501 usage P; group HS control 592773679 date 20260505 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 982910066 date 260505 time 0800 version 00501 usage P; group HB control 982910066 date 20260505 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1846349352, interchange 222208946 date 260403 time 0800 version 00501 usage P; group HC control 222208946 date 20260403 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 716473164 date 260403 time 0800 version 00501 usage P; group HN control 716473164 date 20260403 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 327864337 date 260502 time 0800 version 00501 usage P; group HP control 327864337 date 20260502 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
