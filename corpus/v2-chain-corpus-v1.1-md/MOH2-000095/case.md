# Case MOH2-000095

Patient PATRICIA MILLER, DOB 1950-03-24, sex F, member ID 7GP3F90DU84. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-02-01.

## Adjudication outcome (835)
Claim PA25093497: status 4 (denied). Billed $259.32, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2609377281953, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-04-03.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT634938786, originator 1184634935.
claim statement period start (232): 2026-02-01.
Outpatient adjudication remarks (MOA): N111 (no appeal right except duplicate claim/service issue).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 | $98.72 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $98.72 |  |
| 2 | 97112-GP | 2 | $114.2 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $114.2 |  |
| 3 | 97140-GP | 1 | $46.4 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $46.4 |  |

Line item control numbers (REF 6R): PA25093497L1, PA25093497L2, PA25093497L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: PATRICIA MILLER; MI (member ID) 7GP3F90DU84; rendering provider [82]: NANCY LEWIS; XX (NPI) 1913425846.

## Claim as billed (837P)
Claim PA25093497, total charge $259.32, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25561 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 UN | $98.72 | 2026-02-01 | 1 | PA25093497L1 |
| 2 | 97112-GP | 2 UN | $114.2 | 2026-02-01 | 1 | PA25093497L2 |
| 3 | 97140-GP | 1 UN | $46.4 | 2026-02-01 | 1 | PA25093497L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: PATRICIA MILLER; MI (member ID) 7GP3F90DU84; 3617 OAK ST; STATEN ISLAND, NY, 10392
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: OMAR DELGADO; XX (NPI) 1094074058
- rendering provider [82]: NANCY LEWIS; XX (NPI) 1913425846
- Submission reference TRC39717833, dated 2026-03-17 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-02-01.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: PATRICIA MILLER; MI (member ID) 7GP3F90DU84.
Subject DOB 1950-03-24, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-02-01
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: PATRICIA MILLER; MI (member ID) 7GP3F90DU84.
Subject DOB 1950-03-24, sex F.
Eligibility exchange reference ELG66024290, dated 2026-04-08 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-03-17, action code WQ, amount $259.32.
D9 (clearinghouse claim number): TRC39717833.
Trace (2 (referenced transaction trace)): TRC39717833.
received date (050): 2026-03-17.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: PATRICIA MILLER; MI (member ID) 7GP3F90DU84.
Acknowledgment reference ACK39717833, dated 2026-03-17 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-02-01. Dx: Pain in right knee. 97110 (30 min): therapeutic exercise for strength and ROM. 97112 (30 min): neuromuscular re-education of movement and balance. 97140 (14 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 74. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 818913687 date 260408 time 0800 version 00501 usage P; group HS control 818913687 date 20260408 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 200574053 date 260408 time 0800 version 00501 usage P; group HB control 200574053 date 20260408 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 383271492 date 260317 time 0800 version 00501 usage P; group HC control 383271492 date 20260317 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 173593062 date 260317 time 0800 version 00501 usage P; group HN control 173593062 date 20260317 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 634938786 date 260403 time 0800 version 00501 usage P; group HP control 634938786 date 20260403 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
