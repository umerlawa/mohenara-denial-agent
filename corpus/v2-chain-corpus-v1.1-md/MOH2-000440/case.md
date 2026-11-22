# Case MOH2-000440

Patient SAMUEL TAYLOR, DOB 1950-10-18, sex F, member ID 3AE3VM3DM49. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-07-06.

## Adjudication outcome (835)
Claim PA28254325: status 4 (denied). Billed $162.61, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2621104073364, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-07-30.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT332915013, originator 1184634935.
claim statement period start (232): 2026-07-06.
Outpatient adjudication remarks (MOA): M77 (missing/incomplete/invalid place of service).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 | $79.71 | $0 | CO-5 (Contractual Obligation: procedure code/type of bill is inconsistent with the place of service) $79.71 |  |
| 2 | 97110-GP | 2 | $82.9 | $0 | CO-5 (Contractual Obligation: procedure code/type of bill is inconsistent with the place of service) $82.9 |  |

Line item control numbers (REF 6R): PA28254325L1, PA28254325L2.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: SAMUEL TAYLOR; MI (member ID) 3AE3VM3DM49; rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273.

## Claim as billed (837P)
Claim PA28254325, total charge $162.61, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M1712 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 UN | $79.71 | 2026-07-06 | 1 | PA28254325L1 |
| 2 | 97110-GP | 2 UN | $82.9 | 2026-07-06 | 1 | PA28254325L2 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: SAMUEL TAYLOR; MI (member ID) 3AE3VM3DM49; 272 FRANKLIN ST; STATEN ISLAND, NY, 10320
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: OMAR DELGADO; XX (NPI) 1094074058
- rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273
- Submission reference TRC50552556, dated 2026-07-09 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-07-06.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: SAMUEL TAYLOR; MI (member ID) 3AE3VM3DM49.
Subject DOB 1950-10-18, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-07-06
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: SAMUEL TAYLOR; MI (member ID) 3AE3VM3DM49.
Subject DOB 1950-10-18, sex F.
Eligibility exchange reference ELG57230196, dated 2026-07-31 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-07-10, action code WQ, amount $162.61.
D9 (clearinghouse claim number): TRC50552556.
Trace (2 (referenced transaction trace)): TRC50552556.
received date (050): 2026-07-10.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: SAMUEL TAYLOR; MI (member ID) 3AE3VM3DM49.
Acknowledgment reference ACK50552556, dated 2026-07-10 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-07-06. Dx: Unilateral primary osteoarthritis left knee. 97110 (31 min): therapeutic exercise for strength and ROM. 97110 (30 min): therapeutic exercise for strength and ROM. Total timed minutes: 61. Encounter completed by live interactive video with the patient at their residence; documented consent for telehealth services. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 289352948 date 260731 time 0800 version 00501 usage P; group HS control 289352948 date 20260731 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 478819493 date 260731 time 0800 version 00501 usage P; group HB control 478819493 date 20260731 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 285792944 date 260709 time 0800 version 00501 usage P; group HC control 285792944 date 20260709 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 331590045 date 260710 time 0800 version 00501 usage P; group HN control 331590045 date 20260710 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 332915013 date 260730 time 0800 version 00501 usage P; group HP control 332915013 date 20260730 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 27
