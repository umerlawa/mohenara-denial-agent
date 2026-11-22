# Case MOH2-000216

Patient JOSEPH ROBINSON, DOB 1950-07-01, sex F, member ID 5W14NV2JF32. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-07-01.

## Adjudication outcome (835)
Claim PA27944342: status 1 (processed as primary, paid). Billed $188.78, paid $90.85, patient responsibility $22.71. Filing indicator MB (Medicare Part B). Payer claim control 2621639500956, POS 11 (office), frequency 1 (original claim).
Payment: $90.85 by CHK (check), handling I.
production date (405): 2026-08-04.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT341363973, originator 1184634935.
claim statement period start (232): 2026-07-01.
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP-KX | 2 | $89.02 | $46.5 allowed (B6) $58.12 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $30.9; PR-2 (Patient Responsibility: coinsurance amount) $11.62 |  |
| 2 | 97140-GP-KX | 2 | $99.76 | $44.35 allowed (B6) $55.44 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $44.32; PR-2 (Patient Responsibility: coinsurance amount) $11.09 |  |

Line item control numbers (REF 6R): PA27944342L1, PA27944342L2.
Modifiers on remit lines: GP (under PT plan of care), KX.
Remit claim parties: patient [QC]: JOSEPH ROBINSON; MI (member ID) 5W14NV2JF32; rendering provider [82]: NANCY LEWIS; XX (NPI) 1913425846.

## Claim as billed (837P)
Claim PA27944342, total charge $188.78, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25561 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP-KX | 2 UN | $89.02 | 2026-07-01 | 1 | PA27944342L1 |
| 2 | 97140-GP-KX | 2 UN | $99.76 | 2026-07-01 | 1 | PA27944342L2 |

Modifiers on claim: GP (under PT plan of care), KX.

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: JOSEPH ROBINSON; MI (member ID) 5W14NV2JF32; 5045 LINCOLN ST; WILMINGTON, DE, 19818
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: MARCUS WEBB; XX (NPI) 1583494452
- rendering provider [82]: NANCY LEWIS; XX (NPI) 1913425846
- Submission reference TRC57416056, dated 2026-07-18 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-07-01.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: JOSEPH ROBINSON; MI (member ID) 5W14NV2JF32.
Subject DOB 1950-07-01, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-07-01
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: JOSEPH ROBINSON; MI (member ID) 5W14NV2JF32.
Subject DOB 1950-07-01, sex F.
Eligibility exchange reference ELG61537086, dated 2026-08-05 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-07-18, action code WQ, amount $188.78.
D9 (clearinghouse claim number): TRC57416056.
Trace (2 (referenced transaction trace)): TRC57416056.
received date (050): 2026-07-18.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: JOSEPH ROBINSON; MI (member ID) 5W14NV2JF32.
Acknowledgment reference ACK57416056, dated 2026-07-18 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-07-01. Dx: Pain in right knee. 97110 (31 min): therapeutic exercise for strength and ROM. 97140 (31 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 62. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 626484607 date 260805 time 0800 version 00501 usage P; group HS control 626484607 date 20260805 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 751980701 date 260805 time 0800 version 00501 usage P; group HB control 751980701 date 20260805 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 933227125 date 260718 time 0800 version 00501 usage P; group HC control 933227125 date 20260718 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 655952816 date 260718 time 0800 version 00501 usage P; group HN control 655952816 date 20260718 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 341363973 date 260804 time 0800 version 00501 usage P; group HP control 341363973 date 20260804 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 30
