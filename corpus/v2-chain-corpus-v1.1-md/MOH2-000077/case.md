# Case MOH2-000077

Patient BARBARA MOORE, DOB 1953-01-01, sex M, member ID 2J53RE5TK28. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-02-20.

## Adjudication outcome (835)
Claim PA28132835: status 4 (denied). Billed $170.67, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2610363880845, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-04-13.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT260007559, originator 1184634935.
claim statement period start (232): 2026-02-20.
Outpatient adjudication remarks (MOA): N286 (missing/incomplete/invalid referring provider primary identifier).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $39.76 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $39.76 |  |
| 2 | 97140-GP | 1 | $37.13 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $37.13 |  |
| 3 | 97530-GP | 2 | $93.78 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $93.78 |  |

Line item control numbers (REF 6R): PA28132835L1, PA28132835L2, PA28132835L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: BARBARA MOORE; MI (member ID) 2J53RE5TK28; rendering provider [82]: MARY CLARK; XX (NPI) 1992501921.

## Claim as billed (837P)
Claim PA28132835, total charge $170.67, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M48061 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $39.76 | 2026-02-20 | 1 | PA28132835L1 |
| 2 | 97140-GP | 1 UN | $37.13 | 2026-02-20 | 1 | PA28132835L2 |
| 3 | 97530-GP | 2 UN | $93.78 | 2026-02-20 | 1 | PA28132835L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: BARBARA MOORE; MI (member ID) 2J53RE5TK28; 9678 WILLOW ST; WILMINGTON, DE, 19813
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- rendering provider [82]: MARY CLARK; XX (NPI) 1992501921
- Submission reference TRC82890611, dated 2026-03-06 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-02-20.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: BARBARA MOORE; MI (member ID) 2J53RE5TK28.
Subject DOB 1953-01-01, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-02-20
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: BARBARA MOORE; MI (member ID) 2J53RE5TK28.
Subject DOB 1953-01-01, sex M.
Eligibility exchange reference ELG56931239, dated 2026-04-18 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-03-07, action code WQ, amount $170.67.
D9 (clearinghouse claim number): TRC82890611.
Trace (2 (referenced transaction trace)): TRC82890611.
received date (050): 2026-03-07.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: BARBARA MOORE; MI (member ID) 2J53RE5TK28.
Acknowledgment reference ACK82890611, dated 2026-03-07 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-02-20. Dx: Spinal stenosis lumbar region without neurogenic claudication. 97110 (15 min): therapeutic exercise for strength and ROM. 97140 (14 min): manual therapy (soft tissue and joint mobilization). 97530 (31 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 60. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 334902194 date 260418 time 0800 version 00501 usage P; group HS control 334902194 date 20260418 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 684904680 date 260418 time 0800 version 00501 usage P; group HB control 684904680 date 20260418 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 907329265 date 260306 time 0800 version 00501 usage P; group HC control 907329265 date 20260306 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 33
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 496572838 date 260307 time 0800 version 00501 usage P; group HN control 496572838 date 20260307 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 260007559 date 260413 time 0800 version 00501 usage P; group HP control 260007559 date 20260413 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
