# Case MOH2-000064

Patient MARY MARTIN, DOB 1947-07-24, sex M, member ID 8CU2PF4WT73. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2024-01-21.

## Adjudication outcome (835)
Claim PA23537435: status 4 (denied). Billed $101.24, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2405808713476, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2024-02-27.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT727178042, originator 1184634935.
claim statement period start (232): 2024-01-21.
Outpatient adjudication remarks (MOA): M77 (missing/incomplete/invalid place of service).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $47.97 | $0 | CO-5 (Contractual Obligation: procedure code/type of bill is inconsistent with the place of service) $47.97 |  |
| 2 | 97112-GP | 1 | $53.27 | $0 | CO-5 (Contractual Obligation: procedure code/type of bill is inconsistent with the place of service) $53.27 |  |

Line item control numbers (REF 6R): PA23537435L1, PA23537435L2.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: MARY MARTIN; MI (member ID) 8CU2PF4WT73; rendering provider [82]: MARY CLARK; XX (NPI) 1992501921.

## Claim as billed (837P)
Claim PA23537435, total charge $101.24, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: S335XXD (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $47.97 | 2024-01-21 | 1 | PA23537435L1 |
| 2 | 97112-GP | 1 UN | $53.27 | 2024-01-21 | 1 | PA23537435L2 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: MARY MARTIN; MI (member ID) 8CU2PF4WT73; 8315 LINCOLN AVE; STATEN ISLAND, NY, 10378
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: AISHA RAHMAN; XX (NPI) 1538183382
- rendering provider [82]: MARY CLARK; XX (NPI) 1992501921
- Submission reference TRC83067910, dated 2024-01-31 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2024-01-21.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: MARY MARTIN; MI (member ID) 8CU2PF4WT73.
Subject DOB 1947-07-24, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2024-01-21
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: MARY MARTIN; MI (member ID) 8CU2PF4WT73.
Subject DOB 1947-07-24, sex M.
Eligibility exchange reference ELG59851296, dated 2024-02-29 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2024-01-31, action code WQ, amount $101.24.
D9 (clearinghouse claim number): TRC83067910.
Trace (2 (referenced transaction trace)): TRC83067910.
received date (050): 2024-01-31.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: MARY MARTIN; MI (member ID) 8CU2PF4WT73.
Acknowledgment reference ACK83067910, dated 2024-01-31 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2024-01-21. Dx: Sprain of ligaments of lumbar spine subsequent encounter. 97110 (15 min): therapeutic exercise for strength and ROM. 97112 (16 min): neuromuscular re-education of movement and balance. Total timed minutes: 31. Care delivered remotely via two-way real-time audio-video; patient located at home, consent for virtual care recorded. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 544828516 date 240229 time 0800 version 00501 usage P; group HS control 544828516 date 20240229 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 553563559 date 240229 time 0800 version 00501 usage P; group HB control 553563559 date 20240229 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 764619844 date 240131 time 0800 version 00501 usage P; group HC control 764619844 date 20240131 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 529036515 date 240131 time 0800 version 00501 usage P; group HN control 529036515 date 20240131 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 727178042 date 240227 time 0800 version 00501 usage P; group HP control 727178042 date 20240227 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 27
