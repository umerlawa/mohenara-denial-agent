# Case MOH2-000335

Patient CHARLES MOORE, DOB 1953-09-12, sex F, member ID 8UR2AN9RD05. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-07-25.

## Adjudication outcome (835)
Claim PA23763649: status 4 (denied). Billed $157.38, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2626021306028, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-09-17.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT316196357, originator 1184634935.
claim statement period start (232): 2026-07-25.
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97530-KX | 1 | $58.78 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $58.78 | HE N822 (missing procedure modifier(s)) |
| 2 | 97140-KX | 1 | $45.21 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $45.21 | HE N822 (missing procedure modifier(s)) |
| 3 | 97112-KX | 1 | $53.39 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $53.39 | HE N822 (missing procedure modifier(s)) |

Line item control numbers (REF 6R): PA23763649L1, PA23763649L2, PA23763649L3.
Modifiers on remit lines: KX.
Remit claim parties: patient [QC]: CHARLES MOORE; MI (member ID) 8UR2AN9RD05; rendering provider [82]: MARY CLARK; XX (NPI) 1992501921.

## Claim as billed (837P)
Claim PA23763649, total charge $157.38, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97530-KX | 1 UN | $58.78 | 2026-07-25 | 1 | PA23763649L1 |
| 2 | 97140-KX | 1 UN | $45.21 | 2026-07-25 | 1 | PA23763649L2 |
| 3 | 97112-KX | 1 UN | $53.39 | 2026-07-25 | 1 | PA23763649L3 |

Modifiers on claim: KX.

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: CHARLES MOORE; MI (member ID) 8UR2AN9RD05; 649 CHESTNUT RD; PHILADELPHIA, PA, 19195
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: ROBERT KIMURA; XX (NPI) 1609960205
- rendering provider [82]: MARY CLARK; XX (NPI) 1992501921
- Submission reference TRC70781770, dated 2026-08-11 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-07-25.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: CHARLES MOORE; MI (member ID) 8UR2AN9RD05.
Subject DOB 1953-09-12, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-07-25
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: CHARLES MOORE; MI (member ID) 8UR2AN9RD05.
Subject DOB 1953-09-12, sex F.
Eligibility exchange reference ELG94706991, dated 2026-09-18 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-08-12, action code WQ, amount $157.38.
D9 (clearinghouse claim number): TRC70781770.
Trace (2 (referenced transaction trace)): TRC70781770.
received date (050): 2026-08-12.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: CHARLES MOORE; MI (member ID) 8UR2AN9RD05.
Acknowledgment reference ACK70781770, dated 2026-08-12 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-07-25. Dx: Aftercare following joint replacement surgery. 97530 (16 min): therapeutic activities (dynamic functional tasks). 97140 (15 min): manual therapy (soft tissue and joint mobilization). 97112 (15 min): neuromuscular re-education of movement and balance. Total timed minutes: 46. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 163717172 date 260918 time 0800 version 00501 usage P; group HS control 163717172 date 20260918 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 625506201 date 260918 time 0800 version 00501 usage P; group HB control 625506201 date 20260918 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 896232743 date 260811 time 0800 version 00501 usage P; group HC control 896232743 date 20260811 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 746617279 date 260812 time 0800 version 00501 usage P; group HN control 746617279 date 20260812 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 316196357 date 260917 time 0800 version 00501 usage P; group HP control 316196357 date 20260917 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 33
