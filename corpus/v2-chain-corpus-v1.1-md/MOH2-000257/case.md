# Case MOH2-000257

Patient RUTH CLARK, DOB 1942-12-20, sex F, member ID 1KT3WR8WA84. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-07-11.

## Adjudication outcome (835)
Claim PA27158682: status 4 (denied). Billed $171.34, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2622223463909, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-08-10.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT291522634, originator 1184634935.
claim statement period start (232): 2026-07-11.
Outpatient adjudication remarks (MOA): N435 (exceeds number/frequency approved or allowed within time period).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 | $91.15 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $91.15 |  |
| 2 | 97110-GP | 1 | $38.27 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $38.27 |  |
| 3 | 97140-GP | 1 | $41.92 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $41.92 |  |

Line item control numbers (REF 6R): PA27158682L1, PA27158682L2, PA27158682L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: RUTH CLARK; MI (member ID) 1KT3WR8WA84; rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737.

## Claim as billed (837P)
Claim PA27158682, total charge $171.34, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25512 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 UN | $91.15 | 2026-07-11 | 1 | PA27158682L1 |
| 2 | 97110-GP | 1 UN | $38.27 | 2026-07-11 | 1 | PA27158682L2 |
| 3 | 97140-GP | 1 UN | $41.92 | 2026-07-11 | 1 | PA27158682L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: RUTH CLARK; MI (member ID) 1KT3WR8WA84; 1059 CHESTNUT ST; STATEN ISLAND, NY, 10337
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: ROBERT KIMURA; XX (NPI) 1609960205
- rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737
- Submission reference TRC12237921, dated 2026-07-22 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-07-11.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: RUTH CLARK; MI (member ID) 1KT3WR8WA84.
Subject DOB 1942-12-20, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-07-11
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: RUTH CLARK; MI (member ID) 1KT3WR8WA84.
Subject DOB 1942-12-20, sex F.
Eligibility exchange reference ELG33156126, dated 2026-08-14 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-07-24, action code WQ, amount $171.34.
D9 (clearinghouse claim number): TRC12237921.
Trace (2 (referenced transaction trace)): TRC12237921.
received date (050): 2026-07-24.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: RUTH CLARK; MI (member ID) 1KT3WR8WA84.
Acknowledgment reference ACK12237921, dated 2026-07-24 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-07-11. Dx: Pain in left shoulder. 97110 (31 min): therapeutic exercise for strength and ROM. 97110 (16 min): therapeutic exercise for strength and ROM. 97140 (16 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 63. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1846349352, interchange 325978543 date 260814 time 0800 version 00501 usage P; group HS control 325978543 date 20260814 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 354054098 date 260814 time 0800 version 00501 usage P; group HB control 354054098 date 20260814 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1846349352, interchange 586663974 date 260722 time 0800 version 00501 usage P; group HC control 586663974 date 20260722 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 175620327 date 260724 time 0800 version 00501 usage P; group HN control 175620327 date 20260724 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 291522634 date 260810 time 0800 version 00501 usage P; group HP control 291522634 date 20260810 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
