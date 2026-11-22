# Case MOH2-000490

Patient RICHARD JOHNSON, DOB 1955-10-23, sex M, member ID JFY961779237. Payer: LIBERTY BELL HEALTH PLANS. Service date 2026-01-29.

## Adjudication outcome (835)
Claim PA28830819: status 4 (denied). Billed $173.49, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2606299108316, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-03-03.
Payer [PR]: LIBERTY BELL HEALTH PLANS; 1650 ARCH ST; PHILADELPHIA, PA, 191032097; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT635407506, originator 1135091827.
claim statement period start (232): 2026-01-29.
Outpatient adjudication remarks (MOA): MA04 (secondary payment cannot be considered without primary payer identity).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $38.87 | $0 | CO-22 (Contractual Obligation: care may be covered by another payer per coordination of benefits) $38.87 |  |
| 2 | 97140-GP | 1 | $43.39 | $0 | CO-22 (Contractual Obligation: care may be covered by another payer per coordination of benefits) $43.39 |  |
| 3 | 97530-GP | 2 | $91.23 | $0 | CO-22 (Contractual Obligation: care may be covered by another payer per coordination of benefits) $91.23 |  |

Line item control numbers (REF 6R): PA28830819L1, PA28830819L2, PA28830819L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: RICHARD JOHNSON; MI (member ID) JFY961779237; rendering provider [82]: MARY CLARK; XX (NPI) 1992501921.

## Claim as billed (837P)
Claim PA28830819, total charge $173.49, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25512 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $38.87 | 2026-01-29 | 1 | PA28830819L1 |
| 2 | 97140-GP | 1 UN | $43.39 | 2026-01-29 | 1 | PA28830819L2 |
| 3 | 97530-GP | 2 UN | $91.23 | 2026-01-29 | 1 | PA28830819L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: LIBERTY BELL HEALTH PLANS; 46 (ETIN) 1350918273
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: RICHARD JOHNSON; MI (member ID) JFY961779237; 277 MAPLE RD; PHILADELPHIA, PA, 19168
- payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273
- referring provider [DN]: THOMAS BERGSTROM; XX (NPI) 1179655839
- rendering provider [82]: MARY CLARK; XX (NPI) 1992501921
- Submission reference TRC77903716, dated 2026-02-14 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-01-29.
Inquiry parties: payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: RICHARD JOHNSON; MI (member ID) JFY961779237.
Subject DOB 1955-10-23, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: LIBERTY BELL HEALTH PLANS PPO
- benefit: R (other or additional payer), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-01-29
- eligibility begin (356): 2024-01-01
- eligibility begin (356): 2024-01-01
- payer message: PLAN IS PRIMARY PAYER FOR THIS MEMBER
Response parties: payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: RICHARD JOHNSON; MI (member ID) JFY961779237; payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352.
Subject DOB 1955-10-23, sex M.
Eligibility exchange reference ELG31652538, dated 2026-03-10 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-02-16, action code WQ, amount $173.49.
D9 (clearinghouse claim number): TRC77903716.
Trace (2 (referenced transaction trace)): TRC77903716.
received date (050): 2026-02-16.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: RICHARD JOHNSON; MI (member ID) JFY961779237.
Acknowledgment reference ACK77903716, dated 2026-02-16 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-01-29. Dx: Pain in left shoulder. 97110 (15 min): therapeutic exercise for strength and ROM. 97140 (14 min): manual therapy (soft tissue and joint mobilization). 97530 (30 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 59. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1350918273, interchange 672665378 date 260310 time 0800 version 00501 usage P; group HS control 672665378 date 20260310 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1350918273 to receiver [ZZ] 1110692305, interchange 879885418 date 260310 time 0800 version 00501 usage P; group HB control 879885418 date 20260310 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 17
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1350918273, interchange 432957299 date 260214 time 0800 version 00501 usage P; group HC control 432957299 date 20260214 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 207775503 date 260216 time 0800 version 00501 usage P; group HN control 207775503 date 20260216 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1350918273 to receiver [ZZ] 1110692305, interchange 635407506 date 260303 time 0800 version 00501 usage P; group HP control 635407506 date 20260303 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
