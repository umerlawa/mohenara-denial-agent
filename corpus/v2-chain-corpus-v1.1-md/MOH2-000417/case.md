# Case MOH2-000417

Patient JOHN LOPEZ, DOB 1941-03-05, sex M, member ID 9WV3UR4MG99. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-06-07.

## Adjudication outcome (835)
Claim PA23533020: status 1 (processed as primary, paid). Billed $118.39, paid $36.61, patient responsibility $9.15. Filing indicator MB (Medicare Part B). Payer claim control 2619094734790, POS 11 (office), frequency 1 (original claim).
Payment: $36.61 by CHK (check), handling I.
production date (405): 2026-07-09.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT404305803, originator 1184634935.
claim statement period start (232): 2026-06-07.
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $48.6 | $0 | CO-236 (Contractual Obligation: procedure/modifier combination not compatible per coding guidelines, bundled) $48.6 | HE N20 (service not payable with other service rendered on the same date) |
| 2 | 97140-GP-59 | 1 | $40.87 | $22.18 allowed (B6) $27.72 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $13.15; PR-2 (Patient Responsibility: coinsurance amount) $5.54 |  |
| 3 | 97150-GP | 1 | $28.92 | $14.43 allowed (B6) $18.04 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $10.88; PR-2 (Patient Responsibility: coinsurance amount) $3.61 |  |

Line item control numbers (REF 6R): PA23533020L1, PA23533020L2, PA23533020L3.
Modifiers on remit lines: 59 (distinct procedural service), GP (under PT plan of care).
Remit claim parties: patient [QC]: JOHN LOPEZ; MI (member ID) 9WV3UR4MG99; rendering provider [82]: NANCY LEWIS; XX (NPI) 1913425846.

## Claim as billed (837P)
Claim PA23533020, total charge $118.39, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: S335XXD (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $48.6 | 2026-06-07 | 1 | PA23533020L1 |
| 2 | 97140-GP-59 | 1 UN | $40.87 | 2026-06-07 | 1 | PA23533020L2 |
| 3 | 97150-GP | 1 UN | $28.92 | 2026-06-07 | 1 | PA23533020L3 |

Modifiers on claim: 59 (distinct procedural service), GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: JOHN LOPEZ; MI (member ID) 9WV3UR4MG99; 1707 MAPLE RD; WILMINGTON, DE, 19801
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: MARCUS WEBB; XX (NPI) 1583494452
- rendering provider [82]: NANCY LEWIS; XX (NPI) 1913425846
- Submission reference TRC71522283, dated 2026-06-21 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-06-07.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: JOHN LOPEZ; MI (member ID) 9WV3UR4MG99.
Subject DOB 1941-03-05, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-06-07
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: JOHN LOPEZ; MI (member ID) 9WV3UR4MG99.
Subject DOB 1941-03-05, sex M.
Eligibility exchange reference ELG77709164, dated 2026-07-10 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-06-21, action code WQ, amount $118.39.
D9 (clearinghouse claim number): TRC71522283.
Trace (2 (referenced transaction trace)): TRC71522283.
received date (050): 2026-06-21.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: JOHN LOPEZ; MI (member ID) 9WV3UR4MG99.
Acknowledgment reference ACK71522283, dated 2026-06-21 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-06-07. Dx: Sprain of ligaments of lumbar spine subsequent encounter. 97110 (16 min): therapeutic exercise for strength and ROM. 97140 (15 min): manual therapy (soft tissue and joint mobilization). 97150 (untimed, 1 unit): group therapeutic procedure. Total timed minutes: 31. 97110 and 97150 were furnished as separate and distinct services: different session times, different anatomic regions, independent treatment goals. Documentation supports separate services: 97140 occupied a discrete timed interval apart from 97150 and addressed a different region and impairment. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 566510380 date 260710 time 0800 version 00501 usage P; group HS control 566510380 date 20260710 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 414729131 date 260710 time 0800 version 00501 usage P; group HB control 414729131 date 20260710 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 190552007 date 260621 time 0800 version 00501 usage P; group HC control 190552007 date 20260621 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 785386723 date 260621 time 0800 version 00501 usage P; group HN control 785386723 date 20260621 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 404305803 date 260709 time 0800 version 00501 usage P; group HP control 404305803 date 20260709 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 35
