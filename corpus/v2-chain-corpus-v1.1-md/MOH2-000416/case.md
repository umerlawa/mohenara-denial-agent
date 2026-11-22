# Case MOH2-000416

Patient RICHARD LOPEZ, DOB 1955-08-08, sex M, member ID 7VQ0E29HW92. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-05-31.

## Adjudication outcome (835)
Claim PA24696449: status 4 (denied). Billed $201.27, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2622493901871, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-08-12.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT396404449, originator 1184634935.
claim statement period start (232): 2026-05-31.
Outpatient adjudication remarks (MOA): N111 (no appeal right except duplicate claim/service issue).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97140-GP-KX | 1 | $37.85 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $37.85 |  |
| 2 | 97112-GP-KX | 2 | $116.59 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $116.59 |  |
| 3 | 97116-GP-KX | 1 | $46.83 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $46.83 |  |

Line item control numbers (REF 6R): PA24696449L1, PA24696449L2, PA24696449L3.
Modifiers on remit lines: GP (under PT plan of care), KX.
Remit claim parties: patient [QC]: RICHARD LOPEZ; MI (member ID) 7VQ0E29HW92; rendering provider [82]: MARY CLARK; XX (NPI) 1992501921.

## Claim as billed (837P)
Claim PA24696449, total charge $201.27, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97140-GP-KX | 1 UN | $37.85 | 2026-05-31 | 1 | PA24696449L1 |
| 2 | 97112-GP-KX | 2 UN | $116.59 | 2026-05-31 | 1 | PA24696449L2 |
| 3 | 97116-GP-KX | 1 UN | $46.83 | 2026-05-31 | 1 | PA24696449L3 |

Modifiers on claim: GP (under PT plan of care), KX.

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: RICHARD LOPEZ; MI (member ID) 7VQ0E29HW92; 9081 CHESTNUT RD; TRENTON, NJ, 08677
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: MARCUS WEBB; XX (NPI) 1583494452
- rendering provider [82]: MARY CLARK; XX (NPI) 1992501921
- Submission reference TRC99359660, dated 2026-07-16 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-05-31.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: RICHARD LOPEZ; MI (member ID) 7VQ0E29HW92.
Subject DOB 1955-08-08, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-05-31
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: RICHARD LOPEZ; MI (member ID) 7VQ0E29HW92.
Subject DOB 1955-08-08, sex M.
Eligibility exchange reference ELG11298583, dated 2026-08-18 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-07-18, action code WQ, amount $201.27.
D9 (clearinghouse claim number): TRC99359660.
Trace (2 (referenced transaction trace)): TRC99359660.
received date (050): 2026-07-18.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: RICHARD LOPEZ; MI (member ID) 7VQ0E29HW92.
Acknowledgment reference ACK99359660, dated 2026-07-18 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-05-31. Dx: Aftercare following joint replacement surgery. 97140 (14 min): manual therapy (soft tissue and joint mobilization). 97112 (31 min): neuromuscular re-education of movement and balance. 97116 (14 min): gait training with assistive device progression. Total timed minutes: 59. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 350306941 date 260818 time 0800 version 00501 usage P; group HS control 350306941 date 20260818 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 745669435 date 260818 time 0800 version 00501 usage P; group HB control 745669435 date 20260818 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 497237707 date 260716 time 0800 version 00501 usage P; group HC control 497237707 date 20260716 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 913180490 date 260718 time 0800 version 00501 usage P; group HN control 913180490 date 20260718 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 396404449 date 260812 time 0800 version 00501 usage P; group HP control 396404449 date 20260812 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
