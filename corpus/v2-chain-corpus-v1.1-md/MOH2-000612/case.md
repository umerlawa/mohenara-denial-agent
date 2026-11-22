# Case MOH2-000612

Patient CHARLES MOORE, DOB 1953-09-12, sex F, member ID 8UR2AN9RD05. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-07-20.

## Adjudication outcome (835)
Claim PA25851339: status 4 (denied). Billed $220.86, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2625180081827, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-09-08.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT947128298, originator 1184634935.
claim statement period start (232): 2026-07-20.
Outpatient adjudication remarks (MOA): N286 (missing/incomplete/invalid referring provider primary identifier).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP-KX | 2 | $78.35 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $78.35 |  |
| 2 | 97116-GP-KX | 1 | $42.22 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $42.22 |  |
| 3 | 97110-GP-KX | 2 | $100.29 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $100.29 |  |

Line item control numbers (REF 6R): PA25851339L1, PA25851339L2, PA25851339L3.
Modifiers on remit lines: GP (under PT plan of care), KX.
Remit claim parties: patient [QC]: CHARLES MOORE; MI (member ID) 8UR2AN9RD05; rendering provider [82]: MARY CLARK; XX (NPI) 1992501921.

## Claim as billed (837P)
Claim PA25851339, total charge $220.86, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP-KX | 2 UN | $78.35 | 2026-07-20 | 1 | PA25851339L1 |
| 2 | 97116-GP-KX | 1 UN | $42.22 | 2026-07-20 | 1 | PA25851339L2 |
| 3 | 97110-GP-KX | 2 UN | $100.29 | 2026-07-20 | 1 | PA25851339L3 |

Modifiers on claim: GP (under PT plan of care), KX.

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: CHARLES MOORE; MI (member ID) 8UR2AN9RD05; 649 CHESTNUT RD; PHILADELPHIA, PA, 19195
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- rendering provider [82]: MARY CLARK; XX (NPI) 1992501921
- Submission reference TRC45590268, dated 2026-08-03 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-07-20.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: CHARLES MOORE; MI (member ID) 8UR2AN9RD05.
Subject DOB 1953-09-12, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-07-20
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: CHARLES MOORE; MI (member ID) 8UR2AN9RD05.
Subject DOB 1953-09-12, sex F.
Eligibility exchange reference ELG40262478, dated 2026-09-11 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-08-05, action code WQ, amount $220.86.
D9 (clearinghouse claim number): TRC45590268.
Trace (2 (referenced transaction trace)): TRC45590268.
received date (050): 2026-08-05.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: CHARLES MOORE; MI (member ID) 8UR2AN9RD05.
Acknowledgment reference ACK45590268, dated 2026-08-05 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-07-20. Dx: Aftercare following joint replacement surgery. 97110 (29 min): therapeutic exercise for strength and ROM. 97116 (14 min): gait training with assistive device progression. 97110 (30 min): therapeutic exercise for strength and ROM. Total timed minutes: 73. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 888060726 date 260911 time 0800 version 00501 usage P; group HS control 888060726 date 20260911 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 649352849 date 260911 time 0800 version 00501 usage P; group HB control 649352849 date 20260911 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 921486660 date 260803 time 0800 version 00501 usage P; group HC control 921486660 date 20260803 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 33
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 933755802 date 260805 time 0800 version 00501 usage P; group HN control 933755802 date 20260805 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 947128298 date 260908 time 0800 version 00501 usage P; group HP control 947128298 date 20260908 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
