# Case MOH2-000187

Patient JOHN LOPEZ, DOB 1941-03-05, sex M, member ID 9WV3UR4MG99. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-06-23.

## Adjudication outcome (835)
Claim PA26154675: status 4 (denied). Billed $138.07, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2626166488912, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-09-18.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT540658068, originator 1184634935.
claim statement period start (232): 2026-06-23.
Outpatient adjudication remarks (MOA): N111 (no appeal right except duplicate claim/service issue).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP-KX | 1 | $49.22 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $49.22 |  |
| 2 | 97110-GP-KX | 1 | $48.11 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $48.11 |  |
| 3 | 97140-GP-KX | 1 | $40.74 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $40.74 |  |

Line item control numbers (REF 6R): PA26154675L1, PA26154675L2, PA26154675L3.
Modifiers on remit lines: GP (under PT plan of care), KX.
Remit claim parties: patient [QC]: JOHN LOPEZ; MI (member ID) 9WV3UR4MG99; rendering provider [82]: NANCY LEWIS; XX (NPI) 1913425846.

## Claim as billed (837P)
Claim PA26154675, total charge $138.07, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: S335XXD (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP-KX | 1 UN | $49.22 | 2026-06-23 | 1 | PA26154675L1 |
| 2 | 97110-GP-KX | 1 UN | $48.11 | 2026-06-23 | 1 | PA26154675L2 |
| 3 | 97140-GP-KX | 1 UN | $40.74 | 2026-06-23 | 1 | PA26154675L3 |

Modifiers on claim: GP (under PT plan of care), KX.

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: JOHN LOPEZ; MI (member ID) 9WV3UR4MG99; 1707 MAPLE RD; WILMINGTON, DE, 19801
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: MARCUS WEBB; XX (NPI) 1583494452
- rendering provider [82]: NANCY LEWIS; XX (NPI) 1913425846
- Submission reference TRC77263798, dated 2026-08-24 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-06-23.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: JOHN LOPEZ; MI (member ID) 9WV3UR4MG99.
Subject DOB 1941-03-05, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-06-23
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: JOHN LOPEZ; MI (member ID) 9WV3UR4MG99.
Subject DOB 1941-03-05, sex M.
Eligibility exchange reference ELG99783003, dated 2026-09-25 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-08-25, action code WQ, amount $138.07.
D9 (clearinghouse claim number): TRC77263798.
Trace (2 (referenced transaction trace)): TRC77263798.
received date (050): 2026-08-25.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: JOHN LOPEZ; MI (member ID) 9WV3UR4MG99.
Acknowledgment reference ACK77263798, dated 2026-08-25 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-06-23. Dx: Sprain of ligaments of lumbar spine subsequent encounter. 97110 (15 min): therapeutic exercise for strength and ROM. 97110 (16 min): therapeutic exercise for strength and ROM. 97140 (15 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 46. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 439083054 date 260925 time 0800 version 00501 usage P; group HS control 439083054 date 20260925 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 352347902 date 260925 time 0800 version 00501 usage P; group HB control 352347902 date 20260925 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 998123896 date 260824 time 0800 version 00501 usage P; group HC control 998123896 date 20260824 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 820957140 date 260825 time 0800 version 00501 usage P; group HN control 820957140 date 20260825 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 540658068 date 260918 time 0800 version 00501 usage P; group HP control 540658068 date 20260918 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
