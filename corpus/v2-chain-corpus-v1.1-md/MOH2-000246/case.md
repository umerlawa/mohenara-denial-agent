# Case MOH2-000246

Patient MARY MARTIN, DOB 1947-07-24, sex M, member ID 8CU2PF4WT73. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2024-03-13.

## Adjudication outcome (835)
Claim PA29933438: status 4 (denied). Billed $166.01, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2517692597573, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2025-06-25.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT415690018, originator 1184634935.
claim statement period start (232): 2024-03-13.
Outpatient adjudication remarks (MOA): N211 (you may not appeal this decision).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97140-GP | 2 | $75.6 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $75.6 |  |
| 2 | 97140-GP | 1 | $41.76 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $41.76 |  |
| 3 | 97112-GP | 1 | $48.65 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $48.65 |  |

Line item control numbers (REF 6R): PA29933438L1, PA29933438L2, PA29933438L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: MARY MARTIN; MI (member ID) 8CU2PF4WT73; rendering provider [82]: MARY CLARK; XX (NPI) 1992501921.

## Claim as billed (837P)
Claim PA29933438, total charge $166.01, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: S335XXD (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97140-GP | 2 UN | $75.6 | 2024-03-13 | 1 | PA29933438L1 |
| 2 | 97140-GP | 1 UN | $41.76 | 2024-03-13 | 1 | PA29933438L2 |
| 3 | 97112-GP | 1 UN | $48.65 | 2024-03-13 | 1 | PA29933438L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: MARY MARTIN; MI (member ID) 8CU2PF4WT73; 8315 LINCOLN AVE; STATEN ISLAND, NY, 10378
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: AISHA RAHMAN; XX (NPI) 1538183382
- rendering provider [82]: MARY CLARK; XX (NPI) 1992501921
- Submission reference TRC67211678, dated 2025-06-08 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2024-03-13.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: MARY MARTIN; MI (member ID) 8CU2PF4WT73.
Subject DOB 1947-07-24, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2024-03-13
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: MARY MARTIN; MI (member ID) 8CU2PF4WT73.
Subject DOB 1947-07-24, sex M.
Eligibility exchange reference ELG12177022, dated 2025-07-01 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2024-03-28, action code WQ, amount $166.01.
D9 (clearinghouse claim number): TRC67211678.
Trace (2 (referenced transaction trace)): TRC67211678.
received date (050): 2024-03-28.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: MARY MARTIN; MI (member ID) 8CU2PF4WT73.
Acknowledgment reference ACK67211678, dated 2024-03-28 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2024-03-13. Dx: Sprain of ligaments of lumbar spine subsequent encounter. 97140 (29 min): manual therapy (soft tissue and joint mobilization). 97140 (15 min): manual therapy (soft tissue and joint mobilization). 97112 (14 min): neuromuscular re-education of movement and balance. Total timed minutes: 58. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 644500687 date 250701 time 0800 version 00501 usage P; group HS control 644500687 date 20250701 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 746031740 date 250701 time 0800 version 00501 usage P; group HB control 746031740 date 20250701 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 480901200 date 250608 time 0800 version 00501 usage P; group HC control 480901200 date 20250608 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 554264376 date 240328 time 0800 version 00501 usage P; group HN control 554264376 date 20240328 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 415690018 date 250625 time 0800 version 00501 usage P; group HP control 415690018 date 20250625 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
