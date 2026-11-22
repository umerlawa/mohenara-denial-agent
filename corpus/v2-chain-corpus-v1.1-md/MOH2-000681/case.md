# Case MOH2-000681

Patient SAMUEL TAYLOR, DOB 1950-10-18, sex F, member ID 3AE3VM3DM49. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-06-14.

## Adjudication outcome (835)
Claim PA27524200: status 1 (processed as primary, paid). Billed $70.58, paid $14.43, patient responsibility $3.61. Filing indicator MB (Medicare Part B). Payer claim control 2620142199387, POS 11 (office), frequency 1 (original claim).
Payment: $14.43 by CHK (check), handling I.
production date (405): 2026-07-20.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT452280169, originator 1184634935.
claim statement period start (232): 2026-06-14.
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97150-GP | 1 | $27.5 | $14.43 allowed (B6) $18.04 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $9.46; PR-2 (Patient Responsibility: coinsurance amount) $3.61 |  |
| 2 | 97110-GP | 1 | $43.08 | $0 | CO-236 (Contractual Obligation: procedure/modifier combination not compatible per coding guidelines, bundled) $43.08 | HE N20 (service not payable with other service rendered on the same date) |

Line item control numbers (REF 6R): PA27524200L1, PA27524200L2.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: SAMUEL TAYLOR; MI (member ID) 3AE3VM3DM49; rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273.

## Claim as billed (837P)
Claim PA27524200, total charge $70.58, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M1712 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97150-GP | 1 UN | $27.5 | 2026-06-14 | 1 | PA27524200L1 |
| 2 | 97110-GP | 1 UN | $43.08 | 2026-06-14 | 1 | PA27524200L2 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: SAMUEL TAYLOR; MI (member ID) 3AE3VM3DM49; 272 FRANKLIN ST; STATEN ISLAND, NY, 10320
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: OMAR DELGADO; XX (NPI) 1094074058
- rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273
- Submission reference TRC87007516, dated 2026-07-03 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-06-14.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: SAMUEL TAYLOR; MI (member ID) 3AE3VM3DM49.
Subject DOB 1950-10-18, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-06-14
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: SAMUEL TAYLOR; MI (member ID) 3AE3VM3DM49.
Subject DOB 1950-10-18, sex F.
Eligibility exchange reference ELG37771467, dated 2026-07-24 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-07-03, action code WQ, amount $70.58.
D9 (clearinghouse claim number): TRC87007516.
Trace (2 (referenced transaction trace)): TRC87007516.
received date (050): 2026-07-03.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: SAMUEL TAYLOR; MI (member ID) 3AE3VM3DM49.
Acknowledgment reference ACK87007516, dated 2026-07-03 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-06-14. Dx: Unilateral primary osteoarthritis left knee. 97150 (untimed, 1 unit): group therapeutic procedure. 97110 (16 min): therapeutic exercise for strength and ROM. Total timed minutes: 16. 97110 was carried out during a later, clearly demarcated portion of the visit than 97150, on a different body region, for an unrelated goal. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 796704508 date 260724 time 0800 version 00501 usage P; group HS control 796704508 date 20260724 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 129469116 date 260724 time 0800 version 00501 usage P; group HB control 129469116 date 20260724 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 394082968 date 260703 time 0800 version 00501 usage P; group HC control 394082968 date 20260703 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 843308046 date 260703 time 0800 version 00501 usage P; group HN control 843308046 date 20260703 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 452280169 date 260720 time 0800 version 00501 usage P; group HP control 452280169 date 20260720 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 29
