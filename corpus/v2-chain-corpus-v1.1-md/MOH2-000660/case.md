# Case MOH2-000660

Patient HELEN WHITE, DOB 1947-06-21, sex F, member ID 2YA2VF1FQ73. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-06-06.

## Adjudication outcome (835)
Claim PA22175741: status 4 (denied). Billed $92.78, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2622504898885, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-08-13.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT522151539, originator 1184634935.
claim statement period start (232): 2026-06-06.
Outpatient adjudication remarks (MOA): N111 (no appeal right except duplicate claim/service issue).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97140-GP | 1 | $46.98 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $46.98 |  |
| 2 | 97110-GP | 1 | $45.8 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $45.8 |  |

Line item control numbers (REF 6R): PA22175741L1, PA22175741L2.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: HELEN WHITE; MI (member ID) 2YA2VF1FQ73; rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273.

## Claim as billed (837P)
Claim PA22175741, total charge $92.78, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25561 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97140-GP | 1 UN | $46.98 | 2026-06-06 | 1 | PA22175741L1 |
| 2 | 97110-GP | 1 UN | $45.8 | 2026-06-06 | 1 | PA22175741L2 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: HELEN WHITE; MI (member ID) 2YA2VF1FQ73; 7609 CHESTNUT RD; PHILADELPHIA, PA, 19132
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: OMAR DELGADO; XX (NPI) 1094074058
- rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273
- Submission reference TRC33667050, dated 2026-07-27 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-06-06.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: HELEN WHITE; MI (member ID) 2YA2VF1FQ73.
Subject DOB 1947-06-21, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-06-06
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: HELEN WHITE; MI (member ID) 2YA2VF1FQ73.
Subject DOB 1947-06-21, sex F.
Eligibility exchange reference ELG28455011, dated 2026-08-19 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-07-29, action code WQ, amount $92.78.
D9 (clearinghouse claim number): TRC33667050.
Trace (2 (referenced transaction trace)): TRC33667050.
received date (050): 2026-07-29.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: HELEN WHITE; MI (member ID) 2YA2VF1FQ73.
Acknowledgment reference ACK33667050, dated 2026-07-29 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-06-06. Dx: Pain in right knee. 97140 (15 min): manual therapy (soft tissue and joint mobilization). 97110 (14 min): therapeutic exercise for strength and ROM. Total timed minutes: 29. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 244507289 date 260819 time 0800 version 00501 usage P; group HS control 244507289 date 20260819 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 689011376 date 260819 time 0800 version 00501 usage P; group HB control 689011376 date 20260819 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 509238411 date 260727 time 0800 version 00501 usage P; group HC control 509238411 date 20260727 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 466051580 date 260729 time 0800 version 00501 usage P; group HN control 466051580 date 20260729 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 522151539 date 260813 time 0800 version 00501 usage P; group HP control 522151539 date 20260813 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 27
