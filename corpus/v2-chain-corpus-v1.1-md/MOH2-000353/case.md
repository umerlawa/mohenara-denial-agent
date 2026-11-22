# Case MOH2-000353

Patient SAMUEL TAYLOR, DOB 1950-10-18, sex F, member ID 3AE3VM3DM49. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-07-14.

## Adjudication outcome (835)
Claim PA27443719: status 4 (denied). Billed $134.33, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2623200712580, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-08-20.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT886063656, originator 1184634935.
claim statement period start (232): 2026-07-14.
Outpatient adjudication remarks (MOA): N435 (exceeds number/frequency approved or allowed within time period).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97530-GP | 1 | $48 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $48 |  |
| 2 | 97110-GP | 2 | $86.33 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $86.33 |  |

Line item control numbers (REF 6R): PA27443719L1, PA27443719L2.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: SAMUEL TAYLOR; MI (member ID) 3AE3VM3DM49; rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273.

## Claim as billed (837P)
Claim PA27443719, total charge $134.33, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M1712 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97530-GP | 1 UN | $48 | 2026-07-14 | 1 | PA27443719L1 |
| 2 | 97110-GP | 2 UN | $86.33 | 2026-07-14 | 1 | PA27443719L2 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: SAMUEL TAYLOR; MI (member ID) 3AE3VM3DM49; 272 FRANKLIN ST; STATEN ISLAND, NY, 10320
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: OMAR DELGADO; XX (NPI) 1094074058
- rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273
- Submission reference TRC39992587, dated 2026-07-30 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-07-14.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: SAMUEL TAYLOR; MI (member ID) 3AE3VM3DM49.
Subject DOB 1950-10-18, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-07-14
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: SAMUEL TAYLOR; MI (member ID) 3AE3VM3DM49.
Subject DOB 1950-10-18, sex F.
Eligibility exchange reference ELG15612804, dated 2026-08-27 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-07-31, action code WQ, amount $134.33.
D9 (clearinghouse claim number): TRC39992587.
Trace (2 (referenced transaction trace)): TRC39992587.
received date (050): 2026-07-31.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: SAMUEL TAYLOR; MI (member ID) 3AE3VM3DM49.
Acknowledgment reference ACK39992587, dated 2026-07-31 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-07-14. Dx: Unilateral primary osteoarthritis left knee. 97530 (16 min): therapeutic activities (dynamic functional tasks). 97110 (30 min): therapeutic exercise for strength and ROM. Total timed minutes: 46. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 744344665 date 260827 time 0800 version 00501 usage P; group HS control 744344665 date 20260827 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 178619241 date 260827 time 0800 version 00501 usage P; group HB control 178619241 date 20260827 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 214731274 date 260730 time 0800 version 00501 usage P; group HC control 214731274 date 20260730 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 872188126 date 260731 time 0800 version 00501 usage P; group HN control 872188126 date 20260731 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 886063656 date 260820 time 0800 version 00501 usage P; group HP control 886063656 date 20260820 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 27
