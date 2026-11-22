# Case MOH2-000455

Patient HELEN WHITE, DOB 1947-06-21, sex F, member ID 2YA2VF1FQ73. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-06-26.

## Adjudication outcome (835)
Claim PA25160479: status 1 (processed as primary, paid). Billed $101.25, paid $14.43, patient responsibility $3.61. Filing indicator MB (Medicare Part B). Payer claim control 2620215155834, POS 11 (office), frequency 1 (original claim).
Payment: $14.43 by CHK (check), handling I.
production date (405): 2026-07-21.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT185914349, originator 1184634935.
claim statement period start (232): 2026-06-26.
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97150-GP-KX | 1 | $23.73 | $14.43 allowed (B6) $18.04 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $5.69; PR-2 (Patient Responsibility: coinsurance amount) $3.61 |  |
| 2 | 97110-GP-KX | 2 | $77.52 | $0 | CO-236 (Contractual Obligation: procedure/modifier combination not compatible per coding guidelines, bundled) $77.52 | HE N20 (service not payable with other service rendered on the same date) |

Line item control numbers (REF 6R): PA25160479L1, PA25160479L2.
Modifiers on remit lines: GP (under PT plan of care), KX.
Remit claim parties: patient [QC]: HELEN WHITE; MI (member ID) 2YA2VF1FQ73; rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273.

## Claim as billed (837P)
Claim PA25160479, total charge $101.25, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25561 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97150-GP-KX | 1 UN | $23.73 | 2026-06-26 | 1 | PA25160479L1 |
| 2 | 97110-GP-KX | 2 UN | $77.52 | 2026-06-26 | 1 | PA25160479L2 |

Modifiers on claim: GP (under PT plan of care), KX.

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: HELEN WHITE; MI (member ID) 2YA2VF1FQ73; 7609 CHESTNUT RD; PHILADELPHIA, PA, 19132
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: OMAR DELGADO; XX (NPI) 1094074058
- rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273
- Submission reference TRC85545736, dated 2026-07-02 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-06-26.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: HELEN WHITE; MI (member ID) 2YA2VF1FQ73.
Subject DOB 1947-06-21, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-06-26
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: HELEN WHITE; MI (member ID) 2YA2VF1FQ73.
Subject DOB 1947-06-21, sex F.
Eligibility exchange reference ELG50222166, dated 2026-07-28 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-07-03, action code WQ, amount $101.25.
D9 (clearinghouse claim number): TRC85545736.
Trace (2 (referenced transaction trace)): TRC85545736.
received date (050): 2026-07-03.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: HELEN WHITE; MI (member ID) 2YA2VF1FQ73.
Acknowledgment reference ACK85545736, dated 2026-07-03 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-06-26. Dx: Pain in right knee. 97150 (untimed, 1 unit): group therapeutic procedure. 97110 (31 min): therapeutic exercise for strength and ROM. Total timed minutes: 31. 97110 was performed in a separate 15-minute session from 97150, directed at a distinct body region with a distinct goal; services were not integral to one another. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 194609299 date 260728 time 0800 version 00501 usage P; group HS control 194609299 date 20260728 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 889951798 date 260728 time 0800 version 00501 usage P; group HB control 889951798 date 20260728 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 188956697 date 260702 time 0800 version 00501 usage P; group HC control 188956697 date 20260702 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 129845882 date 260703 time 0800 version 00501 usage P; group HN control 129845882 date 20260703 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 185914349 date 260721 time 0800 version 00501 usage P; group HP control 185914349 date 20260721 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 29
