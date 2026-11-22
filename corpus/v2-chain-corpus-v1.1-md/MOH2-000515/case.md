# Case MOH2-000515

Patient BARBARA MOORE, DOB 1953-01-01, sex M, member ID 2J53RE5TK28. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-08-02.

## Adjudication outcome (835)
Claim PA26661173: status 1 (processed as primary, paid). Billed $116.22, paid $14.43, patient responsibility $3.61. Filing indicator MB (Medicare Part B). Payer claim control 2624633788696, POS 11 (office), frequency 1 (original claim).
Payment: $14.43 by CHK (check), handling I.
production date (405): 2026-09-03.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT283224002, originator 1184634935.
claim statement period start (232): 2026-08-02.
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $42.42 | $0 | CO-236 (Contractual Obligation: procedure/modifier combination not compatible per coding guidelines, bundled) $42.42 | HE N20 (service not payable with other service rendered on the same date) |
| 2 | 97110-GP | 1 | $42.76 | $0 | CO-236 (Contractual Obligation: procedure/modifier combination not compatible per coding guidelines, bundled) $42.76 | HE N20 (service not payable with other service rendered on the same date) |
| 3 | 97150-GP | 1 | $31.04 | $14.43 allowed (B6) $18.04 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $13; PR-2 (Patient Responsibility: coinsurance amount) $3.61 |  |

Line item control numbers (REF 6R): PA26661173L1, PA26661173L2, PA26661173L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: BARBARA MOORE; MI (member ID) 2J53RE5TK28; rendering provider [82]: MARY CLARK; XX (NPI) 1992501921.

## Claim as billed (837P)
Claim PA26661173, total charge $116.22, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M48061 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $42.42 | 2026-08-02 | 1 | PA26661173L1 |
| 2 | 97110-GP | 1 UN | $42.76 | 2026-08-02 | 1 | PA26661173L2 |
| 3 | 97150-GP | 1 UN | $31.04 | 2026-08-02 | 1 | PA26661173L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: BARBARA MOORE; MI (member ID) 2J53RE5TK28; 9678 WILLOW ST; WILMINGTON, DE, 19813
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: AISHA RAHMAN; XX (NPI) 1538183382
- rendering provider [82]: MARY CLARK; XX (NPI) 1992501921
- Submission reference TRC86045764, dated 2026-08-08 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-08-02.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: BARBARA MOORE; MI (member ID) 2J53RE5TK28.
Subject DOB 1953-01-01, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-08-02
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: BARBARA MOORE; MI (member ID) 2J53RE5TK28.
Subject DOB 1953-01-01, sex M.
Eligibility exchange reference ELG11021412, dated 2026-09-05 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-08-10, action code WQ, amount $116.22.
D9 (clearinghouse claim number): TRC86045764.
Trace (2 (referenced transaction trace)): TRC86045764.
received date (050): 2026-08-10.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: BARBARA MOORE; MI (member ID) 2J53RE5TK28.
Acknowledgment reference ACK86045764, dated 2026-08-10 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-08-02. Dx: Spinal stenosis lumbar region without neurogenic claudication. 97110 (15 min): therapeutic exercise for strength and ROM. 97110 (15 min): therapeutic exercise for strength and ROM. 97150 (untimed, 1 unit): group therapeutic procedure. Total timed minutes: 30. The 97110 intervention was distinct from 97150: performed sequentially in separate timed segments and directed at different anatomic sites. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 694026981 date 260905 time 0800 version 00501 usage P; group HS control 694026981 date 20260905 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 311939991 date 260905 time 0800 version 00501 usage P; group HB control 311939991 date 20260905 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 837493695 date 260808 time 0800 version 00501 usage P; group HC control 837493695 date 20260808 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 991912339 date 260810 time 0800 version 00501 usage P; group HN control 991912339 date 20260810 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 283224002 date 260903 time 0800 version 00501 usage P; group HP control 283224002 date 20260903 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 34
