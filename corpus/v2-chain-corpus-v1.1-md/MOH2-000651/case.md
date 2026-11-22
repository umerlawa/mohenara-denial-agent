# Case MOH2-000651

Patient RICHARD LOPEZ, DOB 1955-08-08, sex M, member ID 7VQ0E29HW92. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-01-13.

## Adjudication outcome (835)
Claim PA27280812: status 4 (denied). Billed $273.54, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2605724676806, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-02-26.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT830085968, originator 1184634935.
claim statement period start (232): 2026-01-13.
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110 | 2 | $79.69 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $79.69 | HE N822 (missing procedure modifier(s)) |
| 2 | 97112 | 2 | $111.81 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $111.81 | HE N822 (missing procedure modifier(s)) |
| 3 | 97140 | 2 | $82.04 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $82.04 | HE N822 (missing procedure modifier(s)) |

Line item control numbers (REF 6R): PA27280812L1, PA27280812L2, PA27280812L3.
Remit claim parties: patient [QC]: RICHARD LOPEZ; MI (member ID) 7VQ0E29HW92; rendering provider [82]: MARY CLARK; XX (NPI) 1992501921.

## Claim as billed (837P)
Claim PA27280812, total charge $273.54, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110 | 2 UN | $79.69 | 2026-01-13 | 1 | PA27280812L1 |
| 2 | 97112 | 2 UN | $111.81 | 2026-01-13 | 1 | PA27280812L2 |
| 3 | 97140 | 2 UN | $82.04 | 2026-01-13 | 1 | PA27280812L3 |

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: RICHARD LOPEZ; MI (member ID) 7VQ0E29HW92; 9081 CHESTNUT RD; TRENTON, NJ, 08677
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: MARCUS WEBB; XX (NPI) 1583494452
- rendering provider [82]: MARY CLARK; XX (NPI) 1992501921
- Submission reference TRC34830756, dated 2026-01-29 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-01-13.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: RICHARD LOPEZ; MI (member ID) 7VQ0E29HW92.
Subject DOB 1955-08-08, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-01-13
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: RICHARD LOPEZ; MI (member ID) 7VQ0E29HW92.
Subject DOB 1955-08-08, sex M.
Eligibility exchange reference ELG36603376, dated 2026-03-04 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-01-31, action code WQ, amount $273.54.
D9 (clearinghouse claim number): TRC34830756.
Trace (2 (referenced transaction trace)): TRC34830756.
received date (050): 2026-01-31.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: RICHARD LOPEZ; MI (member ID) 7VQ0E29HW92.
Acknowledgment reference ACK34830756, dated 2026-01-31 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-01-13. Dx: Aftercare following joint replacement surgery. 97110 (30 min): therapeutic exercise for strength and ROM. 97112 (31 min): neuromuscular re-education of movement and balance. 97140 (31 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 92. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 229374515 date 260304 time 0800 version 00501 usage P; group HS control 229374515 date 20260304 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 484642449 date 260304 time 0800 version 00501 usage P; group HB control 484642449 date 20260304 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 931435856 date 260129 time 0800 version 00501 usage P; group HC control 931435856 date 20260129 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 255496299 date 260131 time 0800 version 00501 usage P; group HN control 255496299 date 20260131 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 830085968 date 260226 time 0800 version 00501 usage P; group HP control 830085968 date 20260226 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 33
