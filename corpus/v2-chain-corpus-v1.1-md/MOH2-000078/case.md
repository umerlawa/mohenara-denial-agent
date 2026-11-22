# Case MOH2-000078

Patient SAMUEL TAYLOR, DOB 1950-10-18, sex F, member ID DFZ611155838. Payer: LIBERTY BELL HEALTH PLANS. Service date 2026-03-03.

## Adjudication outcome (835)
Claim PA23181154: status 4 (denied). Billed $227.37, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2610791312209, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-04-17.
Payer [PR]: LIBERTY BELL HEALTH PLANS; 1650 ARCH ST; PHILADELPHIA, PA, 191032097; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT720283468, originator 1135091827.
claim statement period start (232): 2026-03-03.
Outpatient adjudication remarks (MOA): MA04 (secondary payment cannot be considered without primary payer identity).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $46.98 | $0 | CO-22 (Contractual Obligation: care may be covered by another payer per coordination of benefits) $46.98 |  |
| 2 | 97112-GP | 2 | $87.61 | $0 | CO-22 (Contractual Obligation: care may be covered by another payer per coordination of benefits) $87.61 |  |
| 3 | 97140-GP | 2 | $92.78 | $0 | CO-22 (Contractual Obligation: care may be covered by another payer per coordination of benefits) $92.78 |  |

Line item control numbers (REF 6R): PA23181154L1, PA23181154L2, PA23181154L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: SAMUEL TAYLOR; MI (member ID) DFZ611155838; rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273.

## Claim as billed (837P)
Claim PA23181154, total charge $227.37, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M1712 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $46.98 | 2026-03-03 | 1 | PA23181154L1 |
| 2 | 97112-GP | 2 UN | $87.61 | 2026-03-03 | 1 | PA23181154L2 |
| 3 | 97140-GP | 2 UN | $92.78 | 2026-03-03 | 1 | PA23181154L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: LIBERTY BELL HEALTH PLANS; 46 (ETIN) 1350918273
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: SAMUEL TAYLOR; MI (member ID) DFZ611155838; 272 FRANKLIN ST; STATEN ISLAND, NY, 10320
- payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273
- referring provider [DN]: OMAR DELGADO; XX (NPI) 1094074058
- rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273
- Submission reference TRC40997545, dated 2026-03-17 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-03-03.
Inquiry parties: payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: SAMUEL TAYLOR; MI (member ID) DFZ611155838.
Subject DOB 1950-10-18, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: LIBERTY BELL HEALTH PLANS EPO
- benefit: R (other or additional payer), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-03-03
- eligibility begin (356): 2024-01-01
- eligibility begin (356): 2024-01-01
- payer message: PLAN IS PRIMARY PAYER FOR THIS MEMBER
Response parties: payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: SAMUEL TAYLOR; MI (member ID) DFZ611155838; payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352.
Subject DOB 1950-10-18, sex F.
Eligibility exchange reference ELG64980726, dated 2026-04-22 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-03-18, action code WQ, amount $227.37.
D9 (clearinghouse claim number): TRC40997545.
Trace (2 (referenced transaction trace)): TRC40997545.
received date (050): 2026-03-18.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: SAMUEL TAYLOR; MI (member ID) DFZ611155838.
Acknowledgment reference ACK40997545, dated 2026-03-18 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-03-03. Dx: Unilateral primary osteoarthritis left knee. 97110 (14 min): therapeutic exercise for strength and ROM. 97112 (30 min): neuromuscular re-education of movement and balance. 97140 (29 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 73. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1350918273, interchange 757819420 date 260422 time 0800 version 00501 usage P; group HS control 757819420 date 20260422 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1350918273 to receiver [ZZ] 1110692305, interchange 851485811 date 260422 time 0800 version 00501 usage P; group HB control 851485811 date 20260422 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 17
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1350918273, interchange 791373965 date 260317 time 0800 version 00501 usage P; group HC control 791373965 date 20260317 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 819677087 date 260318 time 0800 version 00501 usage P; group HN control 819677087 date 20260318 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1350918273 to receiver [ZZ] 1110692305, interchange 720283468 date 260417 time 0800 version 00501 usage P; group HP control 720283468 date 20260417 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
