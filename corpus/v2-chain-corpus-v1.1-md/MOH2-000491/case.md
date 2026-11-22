# Case MOH2-000491

Patient SAMUEL TAYLOR, DOB 1950-10-18, sex F, member ID DFZ611155838. Payer: LIBERTY BELL HEALTH PLANS. Service date 2026-06-24.

## Adjudication outcome (835)
Claim PA28347600: status 4 (denied). Billed $203.4, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2621515898835, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-08-03.
Payer [PR]: LIBERTY BELL HEALTH PLANS; 1650 ARCH ST; PHILADELPHIA, PA, 191032097; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT393251745, originator 1135091827.
claim statement period start (232): 2026-06-24.
Outpatient adjudication remarks (MOA): MA04 (secondary payment cannot be considered without primary payer identity).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 | $80.41 | $0 | CO-22 (Contractual Obligation: care may be covered by another payer per coordination of benefits) $80.41 |  |
| 2 | 97140-GP | 2 | $86.49 | $0 | CO-22 (Contractual Obligation: care may be covered by another payer per coordination of benefits) $86.49 |  |
| 3 | 97140-GP | 1 | $36.5 | $0 | CO-22 (Contractual Obligation: care may be covered by another payer per coordination of benefits) $36.5 |  |

Line item control numbers (REF 6R): PA28347600L1, PA28347600L2, PA28347600L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: SAMUEL TAYLOR; MI (member ID) DFZ611155838; rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273.

## Claim as billed (837P)
Claim PA28347600, total charge $203.4, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M1712 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 UN | $80.41 | 2026-06-24 | 1 | PA28347600L1 |
| 2 | 97140-GP | 2 UN | $86.49 | 2026-06-24 | 1 | PA28347600L2 |
| 3 | 97140-GP | 1 UN | $36.5 | 2026-06-24 | 1 | PA28347600L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: LIBERTY BELL HEALTH PLANS; 46 (ETIN) 1350918273
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: SAMUEL TAYLOR; MI (member ID) DFZ611155838; 272 FRANKLIN ST; STATEN ISLAND, NY, 10320
- payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273
- referring provider [DN]: OMAR DELGADO; XX (NPI) 1094074058
- rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273
- Submission reference TRC94027929, dated 2026-07-14 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-06-24.
Inquiry parties: payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: SAMUEL TAYLOR; MI (member ID) DFZ611155838.
Subject DOB 1950-10-18, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: LIBERTY BELL HEALTH PLANS EPO
- benefit: R (other or additional payer), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-06-24
- eligibility begin (356): 2024-01-01
- eligibility begin (356): 2024-01-01
- payer message: PLAN IS PRIMARY PAYER FOR THIS MEMBER
Response parties: payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: SAMUEL TAYLOR; MI (member ID) DFZ611155838; payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352.
Subject DOB 1950-10-18, sex F.
Eligibility exchange reference ELG60091605, dated 2026-08-09 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-07-15, action code WQ, amount $203.4.
D9 (clearinghouse claim number): TRC94027929.
Trace (2 (referenced transaction trace)): TRC94027929.
received date (050): 2026-07-15.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: SAMUEL TAYLOR; MI (member ID) DFZ611155838.
Acknowledgment reference ACK94027929, dated 2026-07-15 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-06-24. Dx: Unilateral primary osteoarthritis left knee. 97110 (30 min): therapeutic exercise for strength and ROM. 97140 (29 min): manual therapy (soft tissue and joint mobilization). 97140 (15 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 74. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1350918273, interchange 850951630 date 260809 time 0800 version 00501 usage P; group HS control 850951630 date 20260809 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1350918273 to receiver [ZZ] 1110692305, interchange 313618619 date 260809 time 0800 version 00501 usage P; group HB control 313618619 date 20260809 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 17
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1350918273, interchange 885845203 date 260714 time 0800 version 00501 usage P; group HC control 885845203 date 20260714 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 486393480 date 260715 time 0800 version 00501 usage P; group HN control 486393480 date 20260715 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1350918273 to receiver [ZZ] 1110692305, interchange 393251745 date 260803 time 0800 version 00501 usage P; group HP control 393251745 date 20260803 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
