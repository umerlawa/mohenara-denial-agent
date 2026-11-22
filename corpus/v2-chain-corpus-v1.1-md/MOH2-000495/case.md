# Case MOH2-000495

Patient BARBARA MILLER, DOB 1955-06-19, sex F, member ID 3E92WK0EW22. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2024-07-30.

## Adjudication outcome (835)
Claim PA27489831: status 4 (denied). Billed $220.69, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2526414543143, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2025-09-21.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT474165751, originator 1184634935.
claim statement period start (232): 2024-07-30.
Outpatient adjudication remarks (MOA): N211 (you may not appeal this decision).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97760-GO | 2 | $128.74 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $128.74 |  |
| 2 | 97110-GO-59 | 2 | $91.95 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $91.95 |  |

Line item control numbers (REF 6R): PA27489831L1, PA27489831L2.
Modifiers on remit lines: 59 (distinct procedural service), GO (under OT plan of care).
Remit claim parties: patient [QC]: BARBARA MILLER; MI (member ID) 3E92WK0EW22; rendering provider [82]: MARY CLARK; XX (NPI) 1992501921.

## Claim as billed (837P)
Claim PA27489831, total charge $220.69, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: G5601 (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97760-GO | 2 UN | $128.74 | 2024-07-30 | 1 | PA27489831L1 |
| 2 | 97110-GO-59 | 2 UN | $91.95 | 2024-07-30 | 1 | PA27489831L2 |

Modifiers on claim: 59 (distinct procedural service), GO (under OT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: BARBARA MILLER; MI (member ID) 3E92WK0EW22; 2084 FRANKLIN RD; WILMINGTON, DE, 19878
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: DANIEL OKAFOR; XX (NPI) 1230067602
- rendering provider [82]: MARY CLARK; XX (NPI) 1992501921
- Submission reference TRC10335960, dated 2025-09-05 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2024-07-30.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: BARBARA MILLER; MI (member ID) 3E92WK0EW22.
Subject DOB 1955-06-19, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2024-07-30
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: BARBARA MILLER; MI (member ID) 3E92WK0EW22.
Subject DOB 1955-06-19, sex F.
Eligibility exchange reference ELG24312851, dated 2025-09-25 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2025-09-07, action code WQ, amount $220.69.
D9 (clearinghouse claim number): TRC10335960.
Trace (2 (referenced transaction trace)): TRC10335960.
received date (050): 2025-09-07.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: BARBARA MILLER; MI (member ID) 3E92WK0EW22.
Acknowledgment reference ACK10335960, dated 2025-09-07 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

OT treatment note 2024-07-30. Dx: Carpal tunnel syndrome right upper limb. 97760 (31 min): orthotic management and training, initial encounter. 97110 (31 min): therapeutic exercise for strength and ROM. Total timed minutes: 62. The 97110 intervention was distinct from 97760: performed sequentially in separate timed segments and directed at different anatomic sites. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 400069970 date 250925 time 0800 version 00501 usage P; group HS control 400069970 date 20250925 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 979242977 date 250925 time 0800 version 00501 usage P; group HB control 979242977 date 20250925 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 593362700 date 250905 time 0800 version 00501 usage P; group HC control 593362700 date 20250905 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 276567795 date 250907 time 0800 version 00501 usage P; group HN control 276567795 date 20250907 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 474165751 date 250921 time 0800 version 00501 usage P; group HP control 474165751 date 20250921 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 27
