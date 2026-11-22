# Case MOH2-000441

Patient BARBARA MARTIN, DOB 1957-12-14, sex M, member ID 6C24R57XX43. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-02-19.

## Adjudication outcome (835)
Claim PA24980623: status 4 (denied). Billed $189.68, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2610383773597, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-04-13.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT290684167, originator 1184634935.
claim statement period start (232): 2026-02-19.
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110 | 1 | $51.34 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $51.34 | HE N822 (missing procedure modifier(s)) |
| 2 | 97140 | 2 | $91.8 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $91.8 | HE N822 (missing procedure modifier(s)) |
| 3 | 97530 | 1 | $46.54 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $46.54 | HE N822 (missing procedure modifier(s)) |

Line item control numbers (REF 6R): PA24980623L1, PA24980623L2, PA24980623L3.
Remit claim parties: patient [QC]: BARBARA MARTIN; MI (member ID) 6C24R57XX43; rendering provider [82]: MARY CLARK; XX (NPI) 1992501921.

## Claim as billed (837P)
Claim PA24980623, total charge $189.68, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110 | 1 UN | $51.34 | 2026-02-19 | 1 | PA24980623L1 |
| 2 | 97140 | 2 UN | $91.8 | 2026-02-19 | 1 | PA24980623L2 |
| 3 | 97530 | 1 UN | $46.54 | 2026-02-19 | 1 | PA24980623L3 |

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: BARBARA MARTIN; MI (member ID) 6C24R57XX43; 2190 OAK ST; WILMINGTON, DE, 19851
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: GRETA LINDQVIST; XX (NPI) 1205658765
- rendering provider [82]: MARY CLARK; XX (NPI) 1992501921
- Submission reference TRC69585817, dated 2026-03-04 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-02-19.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: BARBARA MARTIN; MI (member ID) 6C24R57XX43.
Subject DOB 1957-12-14, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-02-19
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: BARBARA MARTIN; MI (member ID) 6C24R57XX43.
Subject DOB 1957-12-14, sex M.
Eligibility exchange reference ELG61196925, dated 2026-04-16 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-03-06, action code WQ, amount $189.68.
D9 (clearinghouse claim number): TRC69585817.
Trace (2 (referenced transaction trace)): TRC69585817.
received date (050): 2026-03-06.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: BARBARA MARTIN; MI (member ID) 6C24R57XX43.
Acknowledgment reference ACK69585817, dated 2026-03-06 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-02-19. Dx: Aftercare following joint replacement surgery. 97110 (16 min): therapeutic exercise for strength and ROM. 97140 (30 min): manual therapy (soft tissue and joint mobilization). 97530 (16 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 62. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 361902012 date 260416 time 0800 version 00501 usage P; group HS control 361902012 date 20260416 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 334415820 date 260416 time 0800 version 00501 usage P; group HB control 334415820 date 20260416 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 970739966 date 260304 time 0800 version 00501 usage P; group HC control 970739966 date 20260304 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 146058804 date 260306 time 0800 version 00501 usage P; group HN control 146058804 date 20260306 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 290684167 date 260413 time 0800 version 00501 usage P; group HP control 290684167 date 20260413 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 33
