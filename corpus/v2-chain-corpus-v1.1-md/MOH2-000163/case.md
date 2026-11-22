# Case MOH2-000163

Patient JOSEPH ROBINSON, DOB 1950-07-01, sex F, member ID 5W14NV2JF32. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-02-05.

## Adjudication outcome (835)
Claim PA23679919: status 1 (processed as primary, paid). Billed $456.65, paid $67.6, patient responsibility $16.9. Filing indicator MB (Medicare Part B). Payer claim control 2608202939516, POS 11 (office), frequency 1 (original claim).
Payment: $67.6 by CHK (check), handling I.
production date (405): 2026-03-23.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT852212068, originator 1184634935.
claim statement period start (232): 2026-02-05.
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $41.59 | $23.25 allowed (B6) $29.06 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $12.53; PR-2 (Patient Responsibility: coinsurance amount) $5.81 |  |
| 2 | 97112-GP | 6 | $323.64 | $0 | CO-151 (Contractual Obligation: information does not support this many/frequency of services) $323.64 | HE N362 (the number of days or units exceeds the acceptable maximum) |
| 3 | 97140-GP | 2 | $91.42 | $44.35 allowed (B6) $55.44 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $35.98; PR-2 (Patient Responsibility: coinsurance amount) $11.09 |  |

Line item control numbers (REF 6R): PA23679919L1, PA23679919L2, PA23679919L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: JOSEPH ROBINSON; MI (member ID) 5W14NV2JF32; rendering provider [82]: NANCY LEWIS; XX (NPI) 1913425846.

## Claim as billed (837P)
Claim PA23679919, total charge $456.65, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25561 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $41.59 | 2026-02-05 | 1 | PA23679919L1 |
| 2 | 97112-GP | 6 UN | $323.64 | 2026-02-05 | 1 | PA23679919L2 |
| 3 | 97140-GP | 2 UN | $91.42 | 2026-02-05 | 1 | PA23679919L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: JOSEPH ROBINSON; MI (member ID) 5W14NV2JF32; 5045 LINCOLN ST; WILMINGTON, DE, 19818
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: MARCUS WEBB; XX (NPI) 1583494452
- rendering provider [82]: NANCY LEWIS; XX (NPI) 1913425846
- Submission reference TRC55422821, dated 2026-02-12 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-02-05.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: JOSEPH ROBINSON; MI (member ID) 5W14NV2JF32.
Subject DOB 1950-07-01, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-02-05
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: JOSEPH ROBINSON; MI (member ID) 5W14NV2JF32.
Subject DOB 1950-07-01, sex F.
Eligibility exchange reference ELG31961041, dated 2026-03-28 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-02-12, action code WQ, amount $456.65.
D9 (clearinghouse claim number): TRC55422821.
Trace (2 (referenced transaction trace)): TRC55422821.
received date (050): 2026-02-12.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: JOSEPH ROBINSON; MI (member ID) 5W14NV2JF32.
Acknowledgment reference ACK55422821, dated 2026-02-12 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-02-05. Dx: Pain in right knee. 97110 (14 min): therapeutic exercise for strength and ROM. 97112 (16 min): neuromuscular re-education of movement and balance. 97140 (30 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 60. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 327531588 date 260328 time 0800 version 00501 usage P; group HS control 327531588 date 20260328 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 674769027 date 260328 time 0800 version 00501 usage P; group HB control 674769027 date 20260328 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 208666350 date 260212 time 0800 version 00501 usage P; group HC control 208666350 date 20260212 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 227826958 date 260212 time 0800 version 00501 usage P; group HN control 227826958 date 20260212 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 852212068 date 260323 time 0800 version 00501 usage P; group HP control 852212068 date 20260323 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 35
