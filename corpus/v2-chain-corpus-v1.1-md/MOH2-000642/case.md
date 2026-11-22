# Case MOH2-000642

Patient HELEN WHITE, DOB 1947-06-21, sex F, member ID 2YA2VF1FQ73. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-06-01.

## Adjudication outcome (835)
Claim PA21154776: status 4 (denied). Billed $220.8, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2617717136581, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-06-26.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT220065198, originator 1184634935.
claim statement period start (232): 2026-06-01.
Outpatient adjudication remarks (MOA): M77 (missing/incomplete/invalid place of service).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97112-GP | 2 | $112.29 | $0 | CO-5 (Contractual Obligation: procedure code/type of bill is inconsistent with the place of service) $112.29 |  |
| 2 | 97530-GP | 1 | $60.87 | $0 | CO-5 (Contractual Obligation: procedure code/type of bill is inconsistent with the place of service) $60.87 |  |
| 3 | 97530-GP | 1 | $47.64 | $0 | CO-5 (Contractual Obligation: procedure code/type of bill is inconsistent with the place of service) $47.64 |  |

Line item control numbers (REF 6R): PA21154776L1, PA21154776L2, PA21154776L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: HELEN WHITE; MI (member ID) 2YA2VF1FQ73; rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273.

## Claim as billed (837P)
Claim PA21154776, total charge $220.8, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25561 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97112-GP | 2 UN | $112.29 | 2026-06-01 | 1 | PA21154776L1 |
| 2 | 97530-GP | 1 UN | $60.87 | 2026-06-01 | 1 | PA21154776L2 |
| 3 | 97530-GP | 1 UN | $47.64 | 2026-06-01 | 1 | PA21154776L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: HELEN WHITE; MI (member ID) 2YA2VF1FQ73; 7609 CHESTNUT RD; PHILADELPHIA, PA, 19132
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: OMAR DELGADO; XX (NPI) 1094074058
- rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273
- Submission reference TRC38812172, dated 2026-06-08 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-06-01.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: HELEN WHITE; MI (member ID) 2YA2VF1FQ73.
Subject DOB 1947-06-21, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-06-01
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: HELEN WHITE; MI (member ID) 2YA2VF1FQ73.
Subject DOB 1947-06-21, sex F.
Eligibility exchange reference ELG23317278, dated 2026-07-01 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-06-08, action code WQ, amount $220.8.
D9 (clearinghouse claim number): TRC38812172.
Trace (2 (referenced transaction trace)): TRC38812172.
received date (050): 2026-06-08.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: HELEN WHITE; MI (member ID) 2YA2VF1FQ73.
Acknowledgment reference ACK38812172, dated 2026-06-08 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-06-01. Dx: Pain in right knee. 97112 (30 min): neuromuscular re-education of movement and balance. 97530 (16 min): therapeutic activities (dynamic functional tasks). 97530 (14 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 60. Session furnished by real-time interactive audio-video connection to the patient's residence; telehealth consent on file. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 782008228 date 260701 time 0800 version 00501 usage P; group HS control 782008228 date 20260701 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 163444111 date 260701 time 0800 version 00501 usage P; group HB control 163444111 date 20260701 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 417416300 date 260608 time 0800 version 00501 usage P; group HC control 417416300 date 20260608 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 602873357 date 260608 time 0800 version 00501 usage P; group HN control 602873357 date 20260608 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 220065198 date 260626 time 0800 version 00501 usage P; group HP control 220065198 date 20260626 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
