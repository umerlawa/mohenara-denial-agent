# Case MOH2-000427

Patient JOHN LOPEZ, DOB 1941-03-05, sex M, member ID 9WV3UR4MG99. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-06-03.

## Adjudication outcome (835)
Claim PA29685819: status 4 (denied). Billed $132.54, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2620218145401, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-07-21.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT535020482, originator 1184634935.
claim statement period start (232): 2026-06-03.
Outpatient adjudication remarks (MOA): N286 (missing/incomplete/invalid referring provider primary identifier).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $38.05 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $38.05 |  |
| 2 | 97110-GP | 1 | $43.25 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $43.25 |  |
| 3 | 97110-GP | 1 | $51.24 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $51.24 |  |

Line item control numbers (REF 6R): PA29685819L1, PA29685819L2, PA29685819L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: JOHN LOPEZ; MI (member ID) 9WV3UR4MG99; rendering provider [82]: NANCY LEWIS; XX (NPI) 1913425846.

## Claim as billed (837P)
Claim PA29685819, total charge $132.54, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: S335XXD (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $38.05 | 2026-06-03 | 1 | PA29685819L1 |
| 2 | 97110-GP | 1 UN | $43.25 | 2026-06-03 | 1 | PA29685819L2 |
| 3 | 97110-GP | 1 UN | $51.24 | 2026-06-03 | 1 | PA29685819L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: JOHN LOPEZ; MI (member ID) 9WV3UR4MG99; 1707 MAPLE RD; WILMINGTON, DE, 19801
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- rendering provider [82]: NANCY LEWIS; XX (NPI) 1913425846
- Submission reference TRC96317479, dated 2026-06-18 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-06-03.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: JOHN LOPEZ; MI (member ID) 9WV3UR4MG99.
Subject DOB 1941-03-05, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-06-03
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: JOHN LOPEZ; MI (member ID) 9WV3UR4MG99.
Subject DOB 1941-03-05, sex M.
Eligibility exchange reference ELG44271847, dated 2026-07-26 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-06-18, action code WQ, amount $132.54.
D9 (clearinghouse claim number): TRC96317479.
Trace (2 (referenced transaction trace)): TRC96317479.
received date (050): 2026-06-18.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: JOHN LOPEZ; MI (member ID) 9WV3UR4MG99.
Acknowledgment reference ACK96317479, dated 2026-06-18 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-06-03. Dx: Sprain of ligaments of lumbar spine subsequent encounter. 97110 (15 min): therapeutic exercise for strength and ROM. 97110 (15 min): therapeutic exercise for strength and ROM. 97110 (16 min): therapeutic exercise for strength and ROM. Total timed minutes: 46. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 441904040 date 260726 time 0800 version 00501 usage P; group HS control 441904040 date 20260726 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 189176596 date 260726 time 0800 version 00501 usage P; group HB control 189176596 date 20260726 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 924577627 date 260618 time 0800 version 00501 usage P; group HC control 924577627 date 20260618 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 33
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 823718399 date 260618 time 0800 version 00501 usage P; group HN control 823718399 date 20260618 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 535020482 date 260721 time 0800 version 00501 usage P; group HP control 535020482 date 20260721 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
