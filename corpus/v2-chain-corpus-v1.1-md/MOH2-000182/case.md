# Case MOH2-000182

Patient MICHAEL HARRIS, DOB 1958-01-26, sex M, member ID SMT679684921. Payer: ATLANTIC SHORE ASSURANCE. Service date 2026-01-21.

## Adjudication outcome (835)
Claim PA28834520: status 4 (denied). Billed $137.14, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2607343406904, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-03-14.
Payer [PR]: ATLANTIC SHORE ASSURANCE; 3499 ROUTE 9 N; FREEHOLD, NJ, 077283100; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT520298679, originator 1125037465.
claim statement period start (232): 2026-01-21.
Outpatient adjudication remarks (MOA): MA04 (secondary payment cannot be considered without primary payer identity).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $43.32 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $43.32 |  |
| 2 | 97140-GP | 1 | $42.87 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $42.87 |  |
| 3 | 97530-GP | 1 | $50.95 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $50.95 |  |

Line item control numbers (REF 6R): PA28834520L1, PA28834520L2, PA28834520L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: MICHAEL HARRIS; MI (member ID) SMT679684921; rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737.

## Claim as billed (837P)
Claim PA28834520, total charge $137.14, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: S335XXD (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $43.32 | 2026-01-21 | 1 | PA28834520L1 |
| 2 | 97140-GP | 1 UN | $42.87 | 2026-01-21 | 1 | PA28834520L2 |
| 3 | 97530-GP | 1 UN | $50.95 | 2026-01-21 | 1 | PA28834520L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: ATLANTIC SHORE ASSURANCE; 46 (ETIN) 1250374659
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: MICHAEL HARRIS; MI (member ID) SMT679684921; 9218 MAPLE LN; PHILADELPHIA, PA, 19156
- payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659
- referring provider [DN]: GRETA LINDQVIST; XX (NPI) 1205658765
- rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737
- Submission reference TRC20653089, dated 2026-02-03 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-01-21.
Inquiry parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: MICHAEL HARRIS; MI (member ID) SMT679684921.
Subject DOB 1958-01-26, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: ATLANTIC SHORE ASSURANCE POS
- benefit: R (other or additional payer), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-01-21
- eligibility begin (356): 2024-01-01
- eligibility begin (356): 2024-01-01
- payer message: PLAN IS PRIMARY PAYER FOR THIS MEMBER
Response parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: MICHAEL HARRIS; MI (member ID) SMT679684921; payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352.
Subject DOB 1958-01-26, sex M.
Eligibility exchange reference ELG78289993, dated 2026-03-20 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-02-04, action code WQ, amount $137.14.
D9 (clearinghouse claim number): TRC20653089.
Trace (2 (referenced transaction trace)): TRC20653089.
received date (050): 2026-02-04.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: MICHAEL HARRIS; MI (member ID) SMT679684921.
Acknowledgment reference ACK20653089, dated 2026-02-04 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-01-21. Dx: Sprain of ligaments of lumbar spine subsequent encounter. 97110 (14 min): therapeutic exercise for strength and ROM. 97140 (15 min): manual therapy (soft tissue and joint mobilization). 97530 (14 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 43. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1250374659, interchange 887822612 date 260320 time 0800 version 00501 usage P; group HS control 887822612 date 20260320 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1250374659 to receiver [ZZ] 1601336180, interchange 858026767 date 260320 time 0800 version 00501 usage P; group HB control 858026767 date 20260320 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 17
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1250374659, interchange 796291536 date 260203 time 0800 version 00501 usage P; group HC control 796291536 date 20260203 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 726216245 date 260204 time 0800 version 00501 usage P; group HN control 726216245 date 20260204 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1250374659 to receiver [ZZ] 1601336180, interchange 520298679 date 260314 time 0800 version 00501 usage P; group HP control 520298679 date 20260314 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
