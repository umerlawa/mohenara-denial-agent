# Case MOH2-000145

Patient JOSEPH ROBINSON, DOB 1950-07-01, sex F, member ID 5W14NV2JF32. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-06-04.

## Adjudication outcome (835)
Claim PA24275221: status 4 (denied). Billed $225.55, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2617727971604, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-06-26.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT635194589, originator 1184634935.
claim statement period start (232): 2026-06-04.
Outpatient adjudication remarks (MOA): N286 (missing/incomplete/invalid referring provider primary identifier).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97116-GP | 1 | $44.1 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $44.1 |  |
| 2 | 97530-GP | 2 | $103.07 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $103.07 |  |
| 3 | 97110-GP | 2 | $78.38 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $78.38 |  |

Line item control numbers (REF 6R): PA24275221L1, PA24275221L2, PA24275221L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: JOSEPH ROBINSON; MI (member ID) 5W14NV2JF32; rendering provider [82]: NANCY LEWIS; XX (NPI) 1913425846.

## Claim as billed (837P)
Claim PA24275221, total charge $225.55, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25561 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97116-GP | 1 UN | $44.1 | 2026-06-04 | 1 | PA24275221L1 |
| 2 | 97530-GP | 2 UN | $103.07 | 2026-06-04 | 1 | PA24275221L2 |
| 3 | 97110-GP | 2 UN | $78.38 | 2026-06-04 | 1 | PA24275221L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: JOSEPH ROBINSON; MI (member ID) 5W14NV2JF32; 5045 LINCOLN ST; WILMINGTON, DE, 19818
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- rendering provider [82]: NANCY LEWIS; XX (NPI) 1913425846
- Submission reference TRC36964790, dated 2026-06-12 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-06-04.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: JOSEPH ROBINSON; MI (member ID) 5W14NV2JF32.
Subject DOB 1950-07-01, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-06-04
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: JOSEPH ROBINSON; MI (member ID) 5W14NV2JF32.
Subject DOB 1950-07-01, sex F.
Eligibility exchange reference ELG53111783, dated 2026-06-30 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-06-13, action code WQ, amount $225.55.
D9 (clearinghouse claim number): TRC36964790.
Trace (2 (referenced transaction trace)): TRC36964790.
received date (050): 2026-06-13.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: JOSEPH ROBINSON; MI (member ID) 5W14NV2JF32.
Acknowledgment reference ACK36964790, dated 2026-06-13 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-06-04. Dx: Pain in right knee. 97116 (15 min): gait training with assistive device progression. 97530 (31 min): therapeutic activities (dynamic functional tasks). 97110 (31 min): therapeutic exercise for strength and ROM. Total timed minutes: 77. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 426793511 date 260630 time 0800 version 00501 usage P; group HS control 426793511 date 20260630 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 796006380 date 260630 time 0800 version 00501 usage P; group HB control 796006380 date 20260630 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 837673220 date 260612 time 0800 version 00501 usage P; group HC control 837673220 date 20260612 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 33
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 806653895 date 260613 time 0800 version 00501 usage P; group HN control 806653895 date 20260613 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 635194589 date 260626 time 0800 version 00501 usage P; group HP control 635194589 date 20260626 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
