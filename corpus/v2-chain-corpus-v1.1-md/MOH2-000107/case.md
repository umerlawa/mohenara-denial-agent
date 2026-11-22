# Case MOH2-000107

Patient JESSICA HARRIS, DOB 1957-08-08, sex M, member ID 1A11H41WR17. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-06-30.

## Adjudication outcome (835)
Claim PA24143415: status 4 (denied). Billed $135.28, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2621000961251, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-07-29.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT219870591, originator 1184634935.
claim statement period start (232): 2026-06-30.
Outpatient adjudication remarks (MOA): N435 (exceeds number/frequency approved or allowed within time period).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $50.38 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $50.38 |  |
| 2 | 97110-GP | 1 | $38 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $38 |  |
| 3 | 97110-GP | 1 | $46.9 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $46.9 |  |

Line item control numbers (REF 6R): PA24143415L1, PA24143415L2, PA24143415L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: JESSICA HARRIS; MI (member ID) 1A11H41WR17; rendering provider [82]: MARY CLARK; XX (NPI) 1992501921.

## Claim as billed (837P)
Claim PA24143415, total charge $135.28, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $50.38 | 2026-06-30 | 1 | PA24143415L1 |
| 2 | 97110-GP | 1 UN | $38 | 2026-06-30 | 1 | PA24143415L2 |
| 3 | 97110-GP | 1 UN | $46.9 | 2026-06-30 | 1 | PA24143415L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: JESSICA HARRIS; MI (member ID) 1A11H41WR17; 9631 OAK ST; TRENTON, NJ, 08668
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: DANIEL OKAFOR; XX (NPI) 1230067602
- rendering provider [82]: MARY CLARK; XX (NPI) 1992501921
- Submission reference TRC30372883, dated 2026-07-03 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-06-30.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: JESSICA HARRIS; MI (member ID) 1A11H41WR17.
Subject DOB 1957-08-08, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-06-30
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: JESSICA HARRIS; MI (member ID) 1A11H41WR17.
Subject DOB 1957-08-08, sex M.
Eligibility exchange reference ELG29448015, dated 2026-08-04 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-07-03, action code WQ, amount $135.28.
D9 (clearinghouse claim number): TRC30372883.
Trace (2 (referenced transaction trace)): TRC30372883.
received date (050): 2026-07-03.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: JESSICA HARRIS; MI (member ID) 1A11H41WR17.
Acknowledgment reference ACK30372883, dated 2026-07-03 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-06-30. Dx: Aftercare following joint replacement surgery. 97110 (15 min): therapeutic exercise for strength and ROM. 97110 (14 min): therapeutic exercise for strength and ROM. 97110 (15 min): therapeutic exercise for strength and ROM. Total timed minutes: 44. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 765603108 date 260804 time 0800 version 00501 usage P; group HS control 765603108 date 20260804 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 859974727 date 260804 time 0800 version 00501 usage P; group HB control 859974727 date 20260804 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 917977317 date 260703 time 0800 version 00501 usage P; group HC control 917977317 date 20260703 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 974053068 date 260703 time 0800 version 00501 usage P; group HN control 974053068 date 20260703 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 219870591 date 260729 time 0800 version 00501 usage P; group HP control 219870591 date 20260729 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
