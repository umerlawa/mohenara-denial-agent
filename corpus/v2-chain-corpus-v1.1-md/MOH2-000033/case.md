# Case MOH2-000033

Patient BARBARA MARTIN, DOB 1957-12-14, sex M, member ID 6C24R57XX43. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-03-16.

## Adjudication outcome (835)
Claim PA28590356: status 4 (denied). Billed $143.16, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2612592606596, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-05-05.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT622216704, originator 1184634935.
claim statement period start (232): 2026-03-16.
Outpatient adjudication remarks (MOA): N286 (missing/incomplete/invalid referring provider primary identifier).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $43.34 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $43.34 |  |
| 2 | 97112-GP | 1 | $52.24 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $52.24 |  |
| 3 | 97140-GP | 1 | $47.58 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $47.58 |  |

Line item control numbers (REF 6R): PA28590356L1, PA28590356L2, PA28590356L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: BARBARA MARTIN; MI (member ID) 6C24R57XX43; rendering provider [82]: MARY CLARK; XX (NPI) 1992501921.

## Claim as billed (837P)
Claim PA28590356, total charge $143.16, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $43.34 | 2026-03-16 | 1 | PA28590356L1 |
| 2 | 97112-GP | 1 UN | $52.24 | 2026-03-16 | 1 | PA28590356L2 |
| 3 | 97140-GP | 1 UN | $47.58 | 2026-03-16 | 1 | PA28590356L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: BARBARA MARTIN; MI (member ID) 6C24R57XX43; 2190 OAK ST; WILMINGTON, DE, 19851
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- rendering provider [82]: MARY CLARK; XX (NPI) 1992501921
- Submission reference TRC48908714, dated 2026-04-01 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-03-16.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: BARBARA MARTIN; MI (member ID) 6C24R57XX43.
Subject DOB 1957-12-14, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-03-16
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: BARBARA MARTIN; MI (member ID) 6C24R57XX43.
Subject DOB 1957-12-14, sex M.
Eligibility exchange reference ELG41666062, dated 2026-05-08 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-04-03, action code WQ, amount $143.16.
D9 (clearinghouse claim number): TRC48908714.
Trace (2 (referenced transaction trace)): TRC48908714.
received date (050): 2026-04-03.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: BARBARA MARTIN; MI (member ID) 6C24R57XX43.
Acknowledgment reference ACK48908714, dated 2026-04-03 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-03-16. Dx: Aftercare following joint replacement surgery. 97110 (15 min): therapeutic exercise for strength and ROM. 97112 (16 min): neuromuscular re-education of movement and balance. 97140 (15 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 46. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 516492654 date 260508 time 0800 version 00501 usage P; group HS control 516492654 date 20260508 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 471511573 date 260508 time 0800 version 00501 usage P; group HB control 471511573 date 20260508 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 337355759 date 260401 time 0800 version 00501 usage P; group HC control 337355759 date 20260401 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 33
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 574291764 date 260403 time 0800 version 00501 usage P; group HN control 574291764 date 20260403 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 622216704 date 260505 time 0800 version 00501 usage P; group HP control 622216704 date 20260505 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
