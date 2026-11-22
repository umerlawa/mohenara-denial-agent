# Case MOH2-000518

Patient BARBARA MOORE, DOB 1953-01-01, sex M, member ID 2J53RE5TK28. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-07-06.

## Adjudication outcome (835)
Claim PA22256038: status 4 (denied). Billed $118.09, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2624239904082, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-08-30.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT935355979, originator 1184634935.
claim statement period start (232): 2026-07-06.
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97140 | 1 | $38.75 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $38.75 | HE N822 (missing procedure modifier(s)) |
| 2 | 97110 | 1 | $39.9 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $39.9 | HE N822 (missing procedure modifier(s)) |
| 3 | 97116 | 1 | $39.44 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $39.44 | HE N822 (missing procedure modifier(s)) |

Line item control numbers (REF 6R): PA22256038L1, PA22256038L2, PA22256038L3.
Remit claim parties: patient [QC]: BARBARA MOORE; MI (member ID) 2J53RE5TK28; rendering provider [82]: MARY CLARK; XX (NPI) 1992501921.

## Claim as billed (837P)
Claim PA22256038, total charge $118.09, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M48061 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97140 | 1 UN | $38.75 | 2026-07-06 | 1 | PA22256038L1 |
| 2 | 97110 | 1 UN | $39.9 | 2026-07-06 | 1 | PA22256038L2 |
| 3 | 97116 | 1 UN | $39.44 | 2026-07-06 | 1 | PA22256038L3 |

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: BARBARA MOORE; MI (member ID) 2J53RE5TK28; 9678 WILLOW ST; WILMINGTON, DE, 19813
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: AISHA RAHMAN; XX (NPI) 1538183382
- rendering provider [82]: MARY CLARK; XX (NPI) 1992501921
- Submission reference TRC39840847, dated 2026-07-23 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-07-06.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: BARBARA MOORE; MI (member ID) 2J53RE5TK28.
Subject DOB 1953-01-01, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-07-06
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: BARBARA MOORE; MI (member ID) 2J53RE5TK28.
Subject DOB 1953-01-01, sex M.
Eligibility exchange reference ELG36964356, dated 2026-09-04 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-07-24, action code WQ, amount $118.09.
D9 (clearinghouse claim number): TRC39840847.
Trace (2 (referenced transaction trace)): TRC39840847.
received date (050): 2026-07-24.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: BARBARA MOORE; MI (member ID) 2J53RE5TK28.
Acknowledgment reference ACK39840847, dated 2026-07-24 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-07-06. Dx: Spinal stenosis lumbar region without neurogenic claudication. 97140 (14 min): manual therapy (soft tissue and joint mobilization). 97110 (14 min): therapeutic exercise for strength and ROM. 97116 (16 min): gait training with assistive device progression. Total timed minutes: 44. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 476710756 date 260904 time 0800 version 00501 usage P; group HS control 476710756 date 20260904 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 475215771 date 260904 time 0800 version 00501 usage P; group HB control 475215771 date 20260904 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 108835434 date 260723 time 0800 version 00501 usage P; group HC control 108835434 date 20260723 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 926728545 date 260724 time 0800 version 00501 usage P; group HN control 926728545 date 20260724 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 935355979 date 260830 time 0800 version 00501 usage P; group HP control 935355979 date 20260830 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 33
