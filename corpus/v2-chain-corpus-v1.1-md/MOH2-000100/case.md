# Case MOH2-000100

Patient CHARLES JACKSON, DOB 1941-03-21, sex M, member ID 1ER2YR8UK79. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-06-25.

## Adjudication outcome (835)
Claim PA24411807: status 4 (denied). Billed $207.4, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2622092164956, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-08-08.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT784925092, originator 1184634935.
claim statement period start (232): 2026-06-25.
Outpatient adjudication remarks (MOA): N435 (exceeds number/frequency approved or allowed within time period).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97530-GP | 1 | $58.13 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $58.13 |  |
| 2 | 97112-GP | 2 | $107.59 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $107.59 |  |
| 3 | 97140-GP | 1 | $41.68 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $41.68 |  |

Line item control numbers (REF 6R): PA24411807L1, PA24411807L2, PA24411807L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: CHARLES JACKSON; MI (member ID) 1ER2YR8UK79; rendering provider [82]: NANCY LEWIS; XX (NPI) 1913425846.

## Claim as billed (837P)
Claim PA24411807, total charge $207.4, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97530-GP | 1 UN | $58.13 | 2026-06-25 | 1 | PA24411807L1 |
| 2 | 97112-GP | 2 UN | $107.59 | 2026-06-25 | 1 | PA24411807L2 |
| 3 | 97140-GP | 1 UN | $41.68 | 2026-06-25 | 1 | PA24411807L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: CHARLES JACKSON; MI (member ID) 1ER2YR8UK79; 7320 CHESTNUT LN; STATEN ISLAND, NY, 10361
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: SARAH CHEN; XX (NPI) 1410042904
- rendering provider [82]: NANCY LEWIS; XX (NPI) 1913425846
- Submission reference TRC44864489, dated 2026-07-09 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-06-25.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: CHARLES JACKSON; MI (member ID) 1ER2YR8UK79.
Subject DOB 1941-03-21, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-06-25
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: CHARLES JACKSON; MI (member ID) 1ER2YR8UK79.
Subject DOB 1941-03-21, sex M.
Eligibility exchange reference ELG91103113, dated 2026-08-13 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-07-09, action code WQ, amount $207.4.
D9 (clearinghouse claim number): TRC44864489.
Trace (2 (referenced transaction trace)): TRC44864489.
received date (050): 2026-07-09.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: CHARLES JACKSON; MI (member ID) 1ER2YR8UK79.
Acknowledgment reference ACK44864489, dated 2026-07-09 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-06-25. Dx: Aftercare following joint replacement surgery. 97530 (16 min): therapeutic activities (dynamic functional tasks). 97112 (29 min): neuromuscular re-education of movement and balance. 97140 (15 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 60. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 114820437 date 260813 time 0800 version 00501 usage P; group HS control 114820437 date 20260813 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 691535910 date 260813 time 0800 version 00501 usage P; group HB control 691535910 date 20260813 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 418600853 date 260709 time 0800 version 00501 usage P; group HC control 418600853 date 20260709 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 309265361 date 260709 time 0800 version 00501 usage P; group HN control 309265361 date 20260709 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 784925092 date 260808 time 0800 version 00501 usage P; group HP control 784925092 date 20260808 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
