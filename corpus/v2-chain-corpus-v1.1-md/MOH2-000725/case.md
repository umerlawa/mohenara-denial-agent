# Case MOH2-000725

Patient FRANK SANCHEZ, DOB 1953-12-25, sex M, member ID 7AH8PX8YQ18. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-01-30.

## Adjudication outcome (835)
Claim PA25028311: status 4 (denied). Billed $191.71, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2607501796009, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-03-16.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT461215864, originator 1184634935.
claim statement period start (232): 2026-01-30.
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110 | 1 | $50.44 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $50.44 | HE N822 (missing procedure modifier(s)) |
| 2 | 97140 | 1 | $38.92 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $38.92 | HE N822 (missing procedure modifier(s)) |
| 3 | 97530 | 2 | $102.35 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $102.35 | HE N822 (missing procedure modifier(s)) |

Line item control numbers (REF 6R): PA25028311L1, PA25028311L2, PA25028311L3.
Remit claim parties: patient [QC]: FRANK SANCHEZ; MI (member ID) 7AH8PX8YQ18; rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273.

## Claim as billed (837P)
Claim PA25028311, total charge $191.71, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: S43401D (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110 | 1 UN | $50.44 | 2026-01-30 | 1 | PA25028311L1 |
| 2 | 97140 | 1 UN | $38.92 | 2026-01-30 | 1 | PA25028311L2 |
| 3 | 97530 | 2 UN | $102.35 | 2026-01-30 | 1 | PA25028311L3 |

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: FRANK SANCHEZ; MI (member ID) 7AH8PX8YQ18; 2614 LINCOLN AVE; TRENTON, NJ, 08615
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: GRETA LINDQVIST; XX (NPI) 1205658765
- rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273
- Submission reference TRC74241297, dated 2026-02-14 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-01-30.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: FRANK SANCHEZ; MI (member ID) 7AH8PX8YQ18.
Subject DOB 1953-12-25, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-01-30
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: FRANK SANCHEZ; MI (member ID) 7AH8PX8YQ18.
Subject DOB 1953-12-25, sex M.
Eligibility exchange reference ELG29768917, dated 2026-03-19 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-02-14, action code WQ, amount $191.71.
D9 (clearinghouse claim number): TRC74241297.
Trace (2 (referenced transaction trace)): TRC74241297.
received date (050): 2026-02-14.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: FRANK SANCHEZ; MI (member ID) 7AH8PX8YQ18.
Acknowledgment reference ACK74241297, dated 2026-02-14 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-01-30. Dx: Unspecified sprain of right shoulder joint subsequent encounter. 97110 (15 min): therapeutic exercise for strength and ROM. 97140 (15 min): manual therapy (soft tissue and joint mobilization). 97530 (30 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 60. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 377961134 date 260319 time 0800 version 00501 usage P; group HS control 377961134 date 20260319 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 568324157 date 260319 time 0800 version 00501 usage P; group HB control 568324157 date 20260319 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 922057211 date 260214 time 0800 version 00501 usage P; group HC control 922057211 date 20260214 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 210072597 date 260214 time 0800 version 00501 usage P; group HN control 210072597 date 20260214 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 461215864 date 260316 time 0800 version 00501 usage P; group HP control 461215864 date 20260316 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 33
