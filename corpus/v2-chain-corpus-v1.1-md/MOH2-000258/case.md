# Case MOH2-000258

Patient FRANK HERNANDEZ, DOB 1952-05-26, sex F, member ID 7ED2RR9DC45. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-06-06.

## Adjudication outcome (835)
Claim PA22078319: status 4 (denied). Billed $113.27, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2619987309177, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-07-18.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820.
Trace (1 (current transaction trace)): EFT877046840, originator 1184634935.
claim statement period start (232): 2026-06-06.
Outpatient adjudication remarks (MOA): N435 (exceeds number/frequency approved or allowed within time period).
Payee TJ (federal tax ID): 321822487.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97140-GP | 2 | $73.4 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $73.4 |  |
| 2 | 97140-GP | 1 | $39.87 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $39.87 |  |

Line item control numbers (REF 6R): PA22078319L1, PA22078319L2.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: FRANK HERNANDEZ; MI (member ID) 7ED2RR9DC45; rendering provider [82]: THOMAS PEREZ; XX (NPI) 1981894162.

## Claim as billed (837P)
Claim PA22078319, total charge $113.27, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25511 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97140-GP | 2 UN | $73.4 | 2026-06-06 | 1 | PA22078319L1 |
| 2 | 97140-GP | 1 UN | $39.87 | 2026-06-06 | 1 | PA22078319L2 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820; EI (employer ID/EIN) 321822487
- insured/subscriber [IL]: FRANK HERNANDEZ; MI (member ID) 7ED2RR9DC45; 8860 MAPLE LN; WILMINGTON, DE, 19898
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: FATIMA AL-RASHID; XX (NPI) 1333183066
- rendering provider [82]: THOMAS PEREZ; XX (NPI) 1981894162
- Submission reference TRC22127526, dated 2026-06-14 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-06-06.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: FRANK HERNANDEZ; MI (member ID) 7ED2RR9DC45.
Subject DOB 1952-05-26, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-06-06
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: FRANK HERNANDEZ; MI (member ID) 7ED2RR9DC45.
Subject DOB 1952-05-26, sex F.
Eligibility exchange reference ELG16571217, dated 2026-07-25 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-06-15, action code WQ, amount $113.27.
D9 (clearinghouse claim number): TRC22127526.
Trace (2 (referenced transaction trace)): TRC22127526.
received date (050): 2026-06-15.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; patient [QC]: FRANK HERNANDEZ; MI (member ID) 7ED2RR9DC45.
Acknowledgment reference ACK22127526, dated 2026-06-15 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-06-06. Dx: Pain in right shoulder. 97140 (30 min): manual therapy (soft tissue and joint mobilization). 97140 (14 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 44. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1353206904 to receiver [ZZ] 1846349352, interchange 343414974 date 260725 time 0800 version 00501 usage P; group HS control 343414974 date 20260725 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1353206904, interchange 254385093 date 260725 time 0800 version 00501 usage P; group HB control 254385093 date 20260725 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 321822487 to receiver [ZZ] 1846349352, interchange 928233901 date 260614 time 0800 version 00501 usage P; group HC control 928233901 date 20260614 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 321822487, interchange 546804260 date 260615 time 0800 version 00501 usage P; group HN control 546804260 date 20260615 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1353206904, interchange 877046840 date 260718 time 0800 version 00501 usage P; group HP control 877046840 date 20260718 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 27
