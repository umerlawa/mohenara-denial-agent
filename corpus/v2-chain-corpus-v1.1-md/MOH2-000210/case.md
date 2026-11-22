# Case MOH2-000210

Patient CARLOS THOMPSON, DOB 1947-03-03, sex F, member ID 5GG1A51TJ34. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-06-15.

## Adjudication outcome (835)
Claim PA27118122: status 4 (denied). Billed $179.78, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2619202822254, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-07-11.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT846413234, originator 1184634935.
claim statement period start (232): 2026-06-15.
Outpatient adjudication remarks (MOA): N435 (exceeds number/frequency approved or allowed within time period).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 | $89.07 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $89.07 |  |
| 2 | 97140-GP | 1 | $47.39 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $47.39 |  |
| 3 | 97140-GP | 1 | $43.32 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $43.32 |  |

Line item control numbers (REF 6R): PA27118122L1, PA27118122L2, PA27118122L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: CARLOS THOMPSON; MI (member ID) 5GG1A51TJ34; rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273.

## Claim as billed (837P)
Claim PA27118122, total charge $179.78, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M48061 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 UN | $89.07 | 2026-06-15 | 1 | PA27118122L1 |
| 2 | 97140-GP | 1 UN | $47.39 | 2026-06-15 | 1 | PA27118122L2 |
| 3 | 97140-GP | 1 UN | $43.32 | 2026-06-15 | 1 | PA27118122L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: CARLOS THOMPSON; MI (member ID) 5GG1A51TJ34; 7943 CHESTNUT RD; PHILADELPHIA, PA, 19164
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: SARAH CHEN; XX (NPI) 1410042904
- rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273
- Submission reference TRC58734685, dated 2026-06-25 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-06-15.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: CARLOS THOMPSON; MI (member ID) 5GG1A51TJ34.
Subject DOB 1947-03-03, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-06-15
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: CARLOS THOMPSON; MI (member ID) 5GG1A51TJ34.
Subject DOB 1947-03-03, sex F.
Eligibility exchange reference ELG29992057, dated 2026-07-16 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-06-26, action code WQ, amount $179.78.
D9 (clearinghouse claim number): TRC58734685.
Trace (2 (referenced transaction trace)): TRC58734685.
received date (050): 2026-06-26.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: CARLOS THOMPSON; MI (member ID) 5GG1A51TJ34.
Acknowledgment reference ACK58734685, dated 2026-06-26 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-06-15. Dx: Spinal stenosis lumbar region without neurogenic claudication. 97110 (31 min): therapeutic exercise for strength and ROM. 97140 (16 min): manual therapy (soft tissue and joint mobilization). 97140 (14 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 61. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 930252928 date 260716 time 0800 version 00501 usage P; group HS control 930252928 date 20260716 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 959977011 date 260716 time 0800 version 00501 usage P; group HB control 959977011 date 20260716 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 971977054 date 260625 time 0800 version 00501 usage P; group HC control 971977054 date 20260625 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 685142469 date 260626 time 0800 version 00501 usage P; group HN control 685142469 date 20260626 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 846413234 date 260711 time 0800 version 00501 usage P; group HP control 846413234 date 20260711 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
