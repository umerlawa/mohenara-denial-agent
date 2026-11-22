# Case MOH2-000146

Patient CHARLES MOORE, DOB 1953-09-12, sex F, member ID 8UR2AN9RD05. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-01-31.

## Adjudication outcome (835)
Claim PA28730672: status 4 (denied). Billed $234.71, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2610443768663, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-04-14.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT195636532, originator 1184634935.
claim statement period start (232): 2026-01-31.
Outpatient adjudication remarks (MOA): N111 (no appeal right except duplicate claim/service issue).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 | $83.68 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $83.68 |  |
| 2 | 97140-GP | 1 | $38.92 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $38.92 |  |
| 3 | 97530-GP | 2 | $112.11 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $112.11 |  |

Line item control numbers (REF 6R): PA28730672L1, PA28730672L2, PA28730672L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: CHARLES MOORE; MI (member ID) 8UR2AN9RD05; rendering provider [82]: MARY CLARK; XX (NPI) 1992501921.

## Claim as billed (837P)
Claim PA28730672, total charge $234.71, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 UN | $83.68 | 2026-01-31 | 1 | PA28730672L1 |
| 2 | 97140-GP | 1 UN | $38.92 | 2026-01-31 | 1 | PA28730672L2 |
| 3 | 97530-GP | 2 UN | $112.11 | 2026-01-31 | 1 | PA28730672L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: CHARLES MOORE; MI (member ID) 8UR2AN9RD05; 649 CHESTNUT RD; PHILADELPHIA, PA, 19195
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: ROBERT KIMURA; XX (NPI) 1609960205
- rendering provider [82]: MARY CLARK; XX (NPI) 1992501921
- Submission reference TRC41692668, dated 2026-03-30 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-01-31.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: CHARLES MOORE; MI (member ID) 8UR2AN9RD05.
Subject DOB 1953-09-12, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-01-31
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: CHARLES MOORE; MI (member ID) 8UR2AN9RD05.
Subject DOB 1953-09-12, sex F.
Eligibility exchange reference ELG25113152, dated 2026-04-21 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-03-31, action code WQ, amount $234.71.
D9 (clearinghouse claim number): TRC41692668.
Trace (2 (referenced transaction trace)): TRC41692668.
received date (050): 2026-03-31.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: CHARLES MOORE; MI (member ID) 8UR2AN9RD05.
Acknowledgment reference ACK41692668, dated 2026-03-31 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-01-31. Dx: Aftercare following joint replacement surgery. 97110 (29 min): therapeutic exercise for strength and ROM. 97140 (16 min): manual therapy (soft tissue and joint mobilization). 97530 (29 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 74. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 651319721 date 260421 time 0800 version 00501 usage P; group HS control 651319721 date 20260421 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 142380322 date 260421 time 0800 version 00501 usage P; group HB control 142380322 date 20260421 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 440792865 date 260330 time 0800 version 00501 usage P; group HC control 440792865 date 20260330 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 226923519 date 260331 time 0800 version 00501 usage P; group HN control 226923519 date 20260331 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 195636532 date 260414 time 0800 version 00501 usage P; group HP control 195636532 date 20260414 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
