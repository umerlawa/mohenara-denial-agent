# Case MOH2-000164

Patient GEORGE WILSON, DOB 1943-10-25, sex M, member ID 4Y63PU1WC13. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-06-17.

## Adjudication outcome (835)
Claim PA22033205: status 4 (denied). Billed $150.25, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2621185321534, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-07-30.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT527728899, originator 1184634935.
claim statement period start (232): 2026-06-17.
Outpatient adjudication remarks (MOA): M77 (missing/incomplete/invalid place of service).
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $48.25 | $0 | CO-5 (Contractual Obligation: procedure code/type of bill is inconsistent with the place of service) $48.25 |  |
| 2 | 97110-GP | 2 | $102 | $0 | CO-5 (Contractual Obligation: procedure code/type of bill is inconsistent with the place of service) $102 |  |

Line item control numbers (REF 6R): PA22033205L1, PA22033205L2.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: GEORGE WILSON; MI (member ID) 4Y63PU1WC13; rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142.

## Claim as billed (837P)
Claim PA22033205, total charge $150.25, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M48061 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $48.25 | 2026-06-17 | 1 | PA22033205L1 |
| 2 | 97110-GP | 2 UN | $102 | 2026-06-17 | 1 | PA22033205L2 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: GEORGE WILSON; MI (member ID) 4Y63PU1WC13; 8660 WILLOW ST; PHILADELPHIA, PA, 19133
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: THOMAS BERGSTROM; XX (NPI) 1179655839
- rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142
- Submission reference TRC18349385, dated 2026-07-03 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-06-17.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: GEORGE WILSON; MI (member ID) 4Y63PU1WC13.
Subject DOB 1943-10-25, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-06-17
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: GEORGE WILSON; MI (member ID) 4Y63PU1WC13.
Subject DOB 1943-10-25, sex M.
Eligibility exchange reference ELG56252529, dated 2026-08-01 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-07-04, action code WQ, amount $150.25.
D9 (clearinghouse claim number): TRC18349385.
Trace (2 (referenced transaction trace)): TRC18349385.
received date (050): 2026-07-04.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: GEORGE WILSON; MI (member ID) 4Y63PU1WC13.
Acknowledgment reference ACK18349385, dated 2026-07-04 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-06-17. Dx: Spinal stenosis lumbar region without neurogenic claudication. 97110 (15 min): therapeutic exercise for strength and ROM. 97110 (30 min): therapeutic exercise for strength and ROM. Total timed minutes: 45. Visit conducted via synchronous audio-video telehealth with the patient at home; consent for telehealth documented. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1846349352, interchange 479940546 date 260801 time 0800 version 00501 usage P; group HS control 479940546 date 20260801 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1801579548, interchange 828762974 date 260801 time 0800 version 00501 usage P; group HB control 828762974 date 20260801 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1846349352, interchange 188313583 date 260703 time 0800 version 00501 usage P; group HC control 188313583 date 20260703 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 344837221 date 260704 time 0800 version 00501 usage P; group HN control 344837221 date 20260704 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1801579548, interchange 527728899 date 260730 time 0800 version 00501 usage P; group HP control 527728899 date 20260730 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 27
