# Case MOH2-000196

Patient RICHARD JOHNSON, DOB 1955-10-23, sex M, member ID 3EX5CX0KA19. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-08-03.

## Adjudication outcome (835)
Claim PA22217438: status 4 (denied). Billed $134.57, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2624277521626, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-08-30.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT714917197, originator 1184634935.
claim statement period start (232): 2026-08-03.
Outpatient adjudication remarks (MOA): M77 (missing/incomplete/invalid place of service).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP-KX | 1 | $47.41 | $0 | CO-5 (Contractual Obligation: procedure code/type of bill is inconsistent with the place of service) $47.41 |  |
| 2 | 97112-GP-KX | 1 | $46.61 | $0 | CO-5 (Contractual Obligation: procedure code/type of bill is inconsistent with the place of service) $46.61 |  |
| 3 | 97110-GP-KX | 1 | $40.55 | $0 | CO-5 (Contractual Obligation: procedure code/type of bill is inconsistent with the place of service) $40.55 |  |

Line item control numbers (REF 6R): PA22217438L1, PA22217438L2, PA22217438L3.
Modifiers on remit lines: GP (under PT plan of care), KX.
Remit claim parties: patient [QC]: RICHARD JOHNSON; MI (member ID) 3EX5CX0KA19; rendering provider [82]: MARY CLARK; XX (NPI) 1992501921.

## Claim as billed (837P)
Claim PA22217438, total charge $134.57, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25512 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP-KX | 1 UN | $47.41 | 2026-08-03 | 1 | PA22217438L1 |
| 2 | 97112-GP-KX | 1 UN | $46.61 | 2026-08-03 | 1 | PA22217438L2 |
| 3 | 97110-GP-KX | 1 UN | $40.55 | 2026-08-03 | 1 | PA22217438L3 |

Modifiers on claim: GP (under PT plan of care), KX.

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: RICHARD JOHNSON; MI (member ID) 3EX5CX0KA19; 277 MAPLE RD; PHILADELPHIA, PA, 19168
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: THOMAS BERGSTROM; XX (NPI) 1179655839
- rendering provider [82]: MARY CLARK; XX (NPI) 1992501921
- Submission reference TRC34582996, dated 2026-08-14 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-08-03.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: RICHARD JOHNSON; MI (member ID) 3EX5CX0KA19.
Subject DOB 1955-10-23, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-08-03
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: RICHARD JOHNSON; MI (member ID) 3EX5CX0KA19.
Subject DOB 1955-10-23, sex M.
Eligibility exchange reference ELG75813696, dated 2026-09-06 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-08-15, action code WQ, amount $134.57.
D9 (clearinghouse claim number): TRC34582996.
Trace (2 (referenced transaction trace)): TRC34582996.
received date (050): 2026-08-15.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: RICHARD JOHNSON; MI (member ID) 3EX5CX0KA19.
Acknowledgment reference ACK34582996, dated 2026-08-15 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-08-03. Dx: Pain in left shoulder. 97110 (15 min): therapeutic exercise for strength and ROM. 97112 (16 min): neuromuscular re-education of movement and balance. 97110 (15 min): therapeutic exercise for strength and ROM. Total timed minutes: 46. Encounter completed by live interactive video with the patient at their residence; documented consent for telehealth services. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 383161526 date 260906 time 0800 version 00501 usage P; group HS control 383161526 date 20260906 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 173004255 date 260906 time 0800 version 00501 usage P; group HB control 173004255 date 20260906 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 947149768 date 260814 time 0800 version 00501 usage P; group HC control 947149768 date 20260814 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 559426051 date 260815 time 0800 version 00501 usage P; group HN control 559426051 date 20260815 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 714917197 date 260830 time 0800 version 00501 usage P; group HP control 714917197 date 20260830 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
