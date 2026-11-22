# Case MOH2-000243

Patient MARY JOHNSON, DOB 1952-06-17, sex M, member ID 2G92AM5RW23. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-05-28.

## Adjudication outcome (835)
Claim PA23141101: status 4 (denied). Billed $84.25, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2617125417795, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-06-20.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT815582147, originator 1184634935.
claim statement period start (232): 2026-05-28.
Outpatient adjudication remarks (MOA): M77 (missing/incomplete/invalid place of service).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $45.05 | $0 | CO-5 (Contractual Obligation: procedure code/type of bill is inconsistent with the place of service) $45.05 |  |
| 2 | 97110-GP | 1 | $39.2 | $0 | CO-5 (Contractual Obligation: procedure code/type of bill is inconsistent with the place of service) $39.2 |  |

Line item control numbers (REF 6R): PA23141101L1, PA23141101L2.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: MARY JOHNSON; MI (member ID) 2G92AM5RW23; rendering provider [82]: WEI LEWIS; XX (NPI) 1986021803.

## Claim as billed (837P)
Claim PA23141101, total charge $84.25, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: S93401D (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $45.05 | 2026-05-28 | 1 | PA23141101L1 |
| 2 | 97110-GP | 1 UN | $39.2 | 2026-05-28 | 1 | PA23141101L2 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: MARY JOHNSON; MI (member ID) 2G92AM5RW23; 9000 CHESTNUT AVE; TRENTON, NJ, 08641
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: GRETA LINDQVIST; XX (NPI) 1205658765
- rendering provider [82]: WEI LEWIS; XX (NPI) 1986021803
- Submission reference TRC59783260, dated 2026-06-06 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-05-28.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: MARY JOHNSON; MI (member ID) 2G92AM5RW23.
Subject DOB 1952-06-17, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-05-28
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: MARY JOHNSON; MI (member ID) 2G92AM5RW23.
Subject DOB 1952-06-17, sex M.
Eligibility exchange reference ELG94196215, dated 2026-06-22 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-06-06, action code WQ, amount $84.25.
D9 (clearinghouse claim number): TRC59783260.
Trace (2 (referenced transaction trace)): TRC59783260.
received date (050): 2026-06-06.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: MARY JOHNSON; MI (member ID) 2G92AM5RW23.
Acknowledgment reference ACK59783260, dated 2026-06-06 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-05-28. Dx: Sprain of unspecified ligament of right ankle subsequent encounter. 97110 (15 min): therapeutic exercise for strength and ROM. 97110 (15 min): therapeutic exercise for strength and ROM. Total timed minutes: 30. Encounter completed by live interactive video with the patient at their residence; documented consent for telehealth services. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1846349352, interchange 885987707 date 260622 time 0800 version 00501 usage P; group HS control 885987707 date 20260622 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 310313860 date 260622 time 0800 version 00501 usage P; group HB control 310313860 date 20260622 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1846349352, interchange 420352256 date 260606 time 0800 version 00501 usage P; group HC control 420352256 date 20260606 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 361271751 date 260606 time 0800 version 00501 usage P; group HN control 361271751 date 20260606 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 815582147 date 260620 time 0800 version 00501 usage P; group HP control 815582147 date 20260620 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 27
