# Case MOH2-000173

Patient RICHARD JOHNSON, DOB 1955-10-23, sex M, member ID 3EX5CX0KA19. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-07-02.

## Adjudication outcome (835)
Claim PA24670387: status 4 (denied). Billed $141.64, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2621831051373, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-08-06.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT545362702, originator 1184634935.
claim statement period start (232): 2026-07-02.
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110 | 1 | $43.69 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $43.69 | HE N822 (missing procedure modifier(s)) |
| 2 | 97112 | 2 | $97.95 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $97.95 | HE N822 (missing procedure modifier(s)) |

Line item control numbers (REF 6R): PA24670387L1, PA24670387L2.
Remit claim parties: patient [QC]: RICHARD JOHNSON; MI (member ID) 3EX5CX0KA19; rendering provider [82]: MARY CLARK; XX (NPI) 1992501921.

## Claim as billed (837P)
Claim PA24670387, total charge $141.64, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25512 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110 | 1 UN | $43.69 | 2026-07-02 | 1 | PA24670387L1 |
| 2 | 97112 | 2 UN | $97.95 | 2026-07-02 | 1 | PA24670387L2 |

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: RICHARD JOHNSON; MI (member ID) 3EX5CX0KA19; 277 MAPLE RD; PHILADELPHIA, PA, 19168
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: THOMAS BERGSTROM; XX (NPI) 1179655839
- rendering provider [82]: MARY CLARK; XX (NPI) 1992501921
- Submission reference TRC39001809, dated 2026-07-18 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-07-02.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: RICHARD JOHNSON; MI (member ID) 3EX5CX0KA19.
Subject DOB 1955-10-23, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-07-02
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: RICHARD JOHNSON; MI (member ID) 3EX5CX0KA19.
Subject DOB 1955-10-23, sex M.
Eligibility exchange reference ELG24217868, dated 2026-08-07 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-07-18, action code WQ, amount $141.64.
D9 (clearinghouse claim number): TRC39001809.
Trace (2 (referenced transaction trace)): TRC39001809.
received date (050): 2026-07-18.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: RICHARD JOHNSON; MI (member ID) 3EX5CX0KA19.
Acknowledgment reference ACK39001809, dated 2026-07-18 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-07-02. Dx: Pain in left shoulder. 97110 (15 min): therapeutic exercise for strength and ROM. 97112 (30 min): neuromuscular re-education of movement and balance. Total timed minutes: 45. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 520281000 date 260807 time 0800 version 00501 usage P; group HS control 520281000 date 20260807 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 106872395 date 260807 time 0800 version 00501 usage P; group HB control 106872395 date 20260807 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 608561911 date 260718 time 0800 version 00501 usage P; group HC control 608561911 date 20260718 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 650199502 date 260718 time 0800 version 00501 usage P; group HN control 650199502 date 20260718 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 545362702 date 260806 time 0800 version 00501 usage P; group HP control 545362702 date 20260806 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 28
