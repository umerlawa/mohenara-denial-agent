# Case MOH2-000369

Patient CHARLES JACKSON, DOB 1941-03-21, sex M, member ID 1ER2YR8UK79. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-01-28.

## Adjudication outcome (835)
Claim PA28654159: status 4 (denied). Billed $247.78, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2607274456446, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-03-13.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT159902570, originator 1184634935.
claim statement period start (232): 2026-01-28.
Outpatient adjudication remarks (MOA): N286 (missing/incomplete/invalid referring provider primary identifier).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 | $77.93 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $77.93 |  |
| 2 | 97140-GP | 1 | $46.37 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $46.37 |  |
| 3 | 97530-GP | 2 | $123.48 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $123.48 |  |

Line item control numbers (REF 6R): PA28654159L1, PA28654159L2, PA28654159L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: CHARLES JACKSON; MI (member ID) 1ER2YR8UK79; rendering provider [82]: NANCY LEWIS; XX (NPI) 1913425846.

## Claim as billed (837P)
Claim PA28654159, total charge $247.78, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 UN | $77.93 | 2026-01-28 | 1 | PA28654159L1 |
| 2 | 97140-GP | 1 UN | $46.37 | 2026-01-28 | 1 | PA28654159L2 |
| 3 | 97530-GP | 2 UN | $123.48 | 2026-01-28 | 1 | PA28654159L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: CHARLES JACKSON; MI (member ID) 1ER2YR8UK79; 7320 CHESTNUT LN; STATEN ISLAND, NY, 10361
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- rendering provider [82]: NANCY LEWIS; XX (NPI) 1913425846
- Submission reference TRC70034319, dated 2026-02-07 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-01-28.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: CHARLES JACKSON; MI (member ID) 1ER2YR8UK79.
Subject DOB 1941-03-21, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-01-28
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: CHARLES JACKSON; MI (member ID) 1ER2YR8UK79.
Subject DOB 1941-03-21, sex M.
Eligibility exchange reference ELG23867100, dated 2026-03-19 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-02-08, action code WQ, amount $247.78.
D9 (clearinghouse claim number): TRC70034319.
Trace (2 (referenced transaction trace)): TRC70034319.
received date (050): 2026-02-08.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: CHARLES JACKSON; MI (member ID) 1ER2YR8UK79.
Acknowledgment reference ACK70034319, dated 2026-02-08 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-01-28. Dx: Aftercare following joint replacement surgery. 97110 (30 min): therapeutic exercise for strength and ROM. 97140 (16 min): manual therapy (soft tissue and joint mobilization). 97530 (29 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 75. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 100408108 date 260319 time 0800 version 00501 usage P; group HS control 100408108 date 20260319 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 311034566 date 260319 time 0800 version 00501 usage P; group HB control 311034566 date 20260319 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 358646327 date 260207 time 0800 version 00501 usage P; group HC control 358646327 date 20260207 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 33
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 705675341 date 260208 time 0800 version 00501 usage P; group HN control 705675341 date 20260208 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 159902570 date 260313 time 0800 version 00501 usage P; group HP control 159902570 date 20260313 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
