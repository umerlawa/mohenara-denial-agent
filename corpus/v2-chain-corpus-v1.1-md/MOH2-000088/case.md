# Case MOH2-000088

Patient JOSEPH ROBINSON, DOB 1950-07-01, sex F, member ID 5W14NV2JF32. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-06-16.

## Adjudication outcome (835)
Claim PA24354783: status 4 (denied). Billed $227.08, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2620240786728, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-07-21.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT237977893, originator 1184634935.
claim statement period start (232): 2026-06-16.
Outpatient adjudication remarks (MOA): N435 (exceeds number/frequency approved or allowed within time period).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 | $75.96 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $75.96 |  |
| 2 | 97112-GP | 1 | $54.92 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $54.92 |  |
| 3 | 97112-GP | 2 | $96.2 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $96.2 |  |

Line item control numbers (REF 6R): PA24354783L1, PA24354783L2, PA24354783L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: JOSEPH ROBINSON; MI (member ID) 5W14NV2JF32; rendering provider [82]: NANCY LEWIS; XX (NPI) 1913425846.

## Claim as billed (837P)
Claim PA24354783, total charge $227.08, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25561 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 UN | $75.96 | 2026-06-16 | 1 | PA24354783L1 |
| 2 | 97112-GP | 1 UN | $54.92 | 2026-06-16 | 1 | PA24354783L2 |
| 3 | 97112-GP | 2 UN | $96.2 | 2026-06-16 | 1 | PA24354783L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: JOSEPH ROBINSON; MI (member ID) 5W14NV2JF32; 5045 LINCOLN ST; WILMINGTON, DE, 19818
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: MARCUS WEBB; XX (NPI) 1583494452
- rendering provider [82]: NANCY LEWIS; XX (NPI) 1913425846
- Submission reference TRC85424706, dated 2026-06-21 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-06-16.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: JOSEPH ROBINSON; MI (member ID) 5W14NV2JF32.
Subject DOB 1950-07-01, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-06-16
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: JOSEPH ROBINSON; MI (member ID) 5W14NV2JF32.
Subject DOB 1950-07-01, sex F.
Eligibility exchange reference ELG73328719, dated 2026-07-28 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-06-22, action code WQ, amount $227.08.
D9 (clearinghouse claim number): TRC85424706.
Trace (2 (referenced transaction trace)): TRC85424706.
received date (050): 2026-06-22.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: JOSEPH ROBINSON; MI (member ID) 5W14NV2JF32.
Acknowledgment reference ACK85424706, dated 2026-06-22 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-06-16. Dx: Pain in right knee. 97110 (31 min): therapeutic exercise for strength and ROM. 97112 (14 min): neuromuscular re-education of movement and balance. 97112 (30 min): neuromuscular re-education of movement and balance. Total timed minutes: 75. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 933469802 date 260728 time 0800 version 00501 usage P; group HS control 933469802 date 20260728 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 866108463 date 260728 time 0800 version 00501 usage P; group HB control 866108463 date 20260728 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 182855366 date 260621 time 0800 version 00501 usage P; group HC control 182855366 date 20260621 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 738569800 date 260622 time 0800 version 00501 usage P; group HN control 738569800 date 20260622 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 237977893 date 260721 time 0800 version 00501 usage P; group HP control 237977893 date 20260721 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
