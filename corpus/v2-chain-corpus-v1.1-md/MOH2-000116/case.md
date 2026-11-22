# Case MOH2-000116

Patient JESSICA LEE, DOB 1947-12-16, sex M, member ID 7XC1QJ4QX54. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-07-27.

## Adjudication outcome (835)
Claim PA24460688: status 4 (denied). Billed $126.09, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2627695771104, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-10-03.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820.
Trace (1 (current transaction trace)): EFT436346035, originator 1184634935.
claim statement period start (232): 2026-07-27.
Outpatient adjudication remarks (MOA): N111 (no appeal right except duplicate claim/service issue).
Payee TJ (federal tax ID): 321822487.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97140-GP-KX | 2 | $76.68 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $76.68 |  |
| 2 | 97110-GP-KX | 1 | $49.41 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $49.41 |  |

Line item control numbers (REF 6R): PA24460688L1, PA24460688L2.
Modifiers on remit lines: GP (under PT plan of care), KX.
Remit claim parties: patient [QC]: JESSICA LEE; MI (member ID) 7XC1QJ4QX54; rendering provider [82]: MICHAEL MARTINEZ; XX (NPI) 1850202042.

## Claim as billed (837P)
Claim PA24460688, total charge $126.09, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97140-GP-KX | 2 UN | $76.68 | 2026-07-27 | 1 | PA24460688L1 |
| 2 | 97110-GP-KX | 1 UN | $49.41 | 2026-07-27 | 1 | PA24460688L2 |

Modifiers on claim: GP (under PT plan of care), KX.

Parties on claim:
- submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820; EI (employer ID/EIN) 321822487
- insured/subscriber [IL]: JESSICA LEE; MI (member ID) 7XC1QJ4QX54; 5399 MAPLE RD; PHILADELPHIA, PA, 19147
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: ROBERT KIMURA; XX (NPI) 1609960205
- rendering provider [82]: MICHAEL MARTINEZ; XX (NPI) 1850202042
- Submission reference TRC14391543, dated 2026-09-13 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-07-27.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: JESSICA LEE; MI (member ID) 7XC1QJ4QX54.
Subject DOB 1947-12-16, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-07-27
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: JESSICA LEE; MI (member ID) 7XC1QJ4QX54.
Subject DOB 1947-12-16, sex M.
Eligibility exchange reference ELG11764714, dated 2026-10-05 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-09-14, action code WQ, amount $126.09.
D9 (clearinghouse claim number): TRC14391543.
Trace (2 (referenced transaction trace)): TRC14391543.
received date (050): 2026-09-14.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; patient [QC]: JESSICA LEE; MI (member ID) 7XC1QJ4QX54.
Acknowledgment reference ACK14391543, dated 2026-09-14 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-07-27. Dx: Aftercare following joint replacement surgery. 97140 (31 min): manual therapy (soft tissue and joint mobilization). 97110 (14 min): therapeutic exercise for strength and ROM. Total timed minutes: 45. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1353206904 to receiver [ZZ] 1846349352, interchange 789871106 date 261005 time 0800 version 00501 usage P; group HS control 789871106 date 20261005 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1353206904, interchange 102070663 date 261005 time 0800 version 00501 usage P; group HB control 102070663 date 20261005 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 321822487 to receiver [ZZ] 1846349352, interchange 784843757 date 260913 time 0800 version 00501 usage P; group HC control 784843757 date 20260913 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 321822487, interchange 129839508 date 260914 time 0800 version 00501 usage P; group HN control 129839508 date 20260914 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1353206904, interchange 436346035 date 261003 time 0800 version 00501 usage P; group HP control 436346035 date 20261003 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 27
