# Case MOH2-000209

Patient JOHN LOPEZ, DOB 1941-03-05, sex M, member ID 9WV3UR4MG99. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-05-24.

## Adjudication outcome (835)
Claim PA25357253: status 4 (denied). Billed $238.65, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2618988637695, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-07-08.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT661157223, originator 1184634935.
claim statement period start (232): 2026-05-24.
Outpatient adjudication remarks (MOA): M77 (missing/incomplete/invalid place of service).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 | $97.01 | $0 | CO-5 (Contractual Obligation: procedure code/type of bill is inconsistent with the place of service) $97.01 |  |
| 2 | 97110-GP | 1 | $43.41 | $0 | CO-5 (Contractual Obligation: procedure code/type of bill is inconsistent with the place of service) $43.41 |  |
| 3 | 97110-GP | 2 | $98.23 | $0 | CO-5 (Contractual Obligation: procedure code/type of bill is inconsistent with the place of service) $98.23 |  |

Line item control numbers (REF 6R): PA25357253L1, PA25357253L2, PA25357253L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: JOHN LOPEZ; MI (member ID) 9WV3UR4MG99; rendering provider [82]: NANCY LEWIS; XX (NPI) 1913425846.

## Claim as billed (837P)
Claim PA25357253, total charge $238.65, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: S335XXD (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 UN | $97.01 | 2026-05-24 | 1 | PA25357253L1 |
| 2 | 97110-GP | 1 UN | $43.41 | 2026-05-24 | 1 | PA25357253L2 |
| 3 | 97110-GP | 2 UN | $98.23 | 2026-05-24 | 1 | PA25357253L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: JOHN LOPEZ; MI (member ID) 9WV3UR4MG99; 1707 MAPLE RD; WILMINGTON, DE, 19801
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: MARCUS WEBB; XX (NPI) 1583494452
- rendering provider [82]: NANCY LEWIS; XX (NPI) 1913425846
- Submission reference TRC77149466, dated 2026-05-30 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-05-24.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: JOHN LOPEZ; MI (member ID) 9WV3UR4MG99.
Subject DOB 1941-03-05, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-05-24
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: JOHN LOPEZ; MI (member ID) 9WV3UR4MG99.
Subject DOB 1941-03-05, sex M.
Eligibility exchange reference ELG91641170, dated 2026-07-09 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-05-30, action code WQ, amount $238.65.
D9 (clearinghouse claim number): TRC77149466.
Trace (2 (referenced transaction trace)): TRC77149466.
received date (050): 2026-05-30.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: JOHN LOPEZ; MI (member ID) 9WV3UR4MG99.
Acknowledgment reference ACK77149466, dated 2026-05-30 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-05-24. Dx: Sprain of ligaments of lumbar spine subsequent encounter. 97110 (30 min): therapeutic exercise for strength and ROM. 97110 (14 min): therapeutic exercise for strength and ROM. 97110 (31 min): therapeutic exercise for strength and ROM. Total timed minutes: 75. Care delivered remotely via two-way real-time audio-video; patient located at home, consent for virtual care recorded. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 116882340 date 260709 time 0800 version 00501 usage P; group HS control 116882340 date 20260709 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 890313915 date 260709 time 0800 version 00501 usage P; group HB control 890313915 date 20260709 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 363020513 date 260530 time 0800 version 00501 usage P; group HC control 363020513 date 20260530 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 560546732 date 260530 time 0800 version 00501 usage P; group HN control 560546732 date 20260530 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 661157223 date 260708 time 0800 version 00501 usage P; group HP control 661157223 date 20260708 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
