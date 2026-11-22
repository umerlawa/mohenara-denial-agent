# Case MOH2-000220

Patient BARBARA MILLER, DOB 1955-06-19, sex F, member ID 3E92WK0EW22. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2024-07-19.

## Adjudication outcome (835)
Claim PA27526776: status 4 (denied). Billed $81.37, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2530544661308, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2025-11-01.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT856616516, originator 1184634935.
claim statement period start (232): 2024-07-19.
Outpatient adjudication remarks (MOA): N211 (you may not appeal this decision).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GO | 1 | $38.48 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $38.48 |  |
| 2 | 97535-GO | 1 | $42.89 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $42.89 |  |

Line item control numbers (REF 6R): PA27526776L1, PA27526776L2.
Modifiers on remit lines: GO (under OT plan of care).
Remit claim parties: patient [QC]: BARBARA MILLER; MI (member ID) 3E92WK0EW22; rendering provider [82]: MARY CLARK; XX (NPI) 1992501921.

## Claim as billed (837P)
Claim PA27526776, total charge $81.37, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: G5601 (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GO | 1 UN | $38.48 | 2024-07-19 | 1 | PA27526776L1 |
| 2 | 97535-GO | 1 UN | $42.89 | 2024-07-19 | 1 | PA27526776L2 |

Modifiers on claim: GO (under OT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: BARBARA MILLER; MI (member ID) 3E92WK0EW22; 2084 FRANKLIN RD; WILMINGTON, DE, 19878
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: DANIEL OKAFOR; XX (NPI) 1230067602
- rendering provider [82]: MARY CLARK; XX (NPI) 1992501921
- Submission reference TRC40749676, dated 2025-10-13 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2024-07-19.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: BARBARA MILLER; MI (member ID) 3E92WK0EW22.
Subject DOB 1955-06-19, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2024-07-19
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: BARBARA MILLER; MI (member ID) 3E92WK0EW22.
Subject DOB 1955-06-19, sex F.
Eligibility exchange reference ELG41716452, dated 2025-11-03 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2024-07-23, action code WQ, amount $81.37.
D9 (clearinghouse claim number): TRC40749676.
Trace (2 (referenced transaction trace)): TRC40749676.
received date (050): 2024-07-23.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: BARBARA MILLER; MI (member ID) 3E92WK0EW22.
Acknowledgment reference ACK40749676, dated 2024-07-23 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

OT treatment note 2024-07-19. Dx: Carpal tunnel syndrome right upper limb. 97110 (15 min): therapeutic exercise for strength and ROM. 97535 (14 min): self-care/home management training. Total timed minutes: 29. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 153672919 date 251103 time 0800 version 00501 usage P; group HS control 153672919 date 20251103 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 716138391 date 251103 time 0800 version 00501 usage P; group HB control 716138391 date 20251103 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 904035606 date 251013 time 0800 version 00501 usage P; group HC control 904035606 date 20251013 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 179093152 date 240723 time 0800 version 00501 usage P; group HN control 179093152 date 20240723 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 856616516 date 251101 time 0800 version 00501 usage P; group HP control 856616516 date 20251101 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 27
