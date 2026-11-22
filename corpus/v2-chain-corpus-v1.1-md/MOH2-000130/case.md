# Case MOH2-000130

Patient HELEN WILLIAMS, DOB 1955-01-17, sex M, member ID H949153864. Payer: KEYSTONE SENIOR COMPLETE HMO. Service date 2024-01-21.

## Adjudication outcome (835)
Claim PA26119573: status 4 (denied). Billed $141.61, paid $0, patient responsibility . Filing indicator HM (HMO). Payer claim control 2509200554038, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2025-04-02.
Payer [PR]: KEYSTONE SENIOR COMPLETE HMO; 35 PENN CENTER BLVD; PHILADELPHIA, PA, 191031800; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT755450118, originator 1165038291.
claim statement period start (232): 2024-01-21.
Outpatient adjudication remarks (MOA): N211 (you may not appeal this decision).
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 | $98.34 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $98.34 |  |
| 2 | 97112-GP | 1 | $43.27 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $43.27 |  |

Line item control numbers (REF 6R): PA26119573L1, PA26119573L2.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: HELEN WILLIAMS; MI (member ID) H949153864; rendering provider [82]: DOROTHY LOPEZ; XX (NPI) 1390221007.

## Claim as billed (837P)
Claim PA26119573, total charge $141.61, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25511 (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing HM (HMO).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 UN | $98.34 | 2024-01-21 | 1 | PA26119573L1 |
| 2 | 97112-GP | 1 UN | $43.27 | 2024-01-21 | 1 | PA26119573L2 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: KEYSTONE SENIOR COMPLETE HMO; 46 (ETIN) 1650382917
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: HELEN WILLIAMS; MI (member ID) H949153864; 7432 OAK ST; TRENTON, NJ, 08685
- payer [PR]: KEYSTONE SENIOR COMPLETE HMO; PI (payer ID) 1650382917
- referring provider [DN]: FATIMA AL-RASHID; XX (NPI) 1333183066
- rendering provider [82]: DOROTHY LOPEZ; XX (NPI) 1390221007
- Submission reference TRC14477087, dated 2025-03-18 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2024-01-21.
Inquiry parties: payer [PR]: KEYSTONE SENIOR COMPLETE HMO; PI (payer ID) 1650382917; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: HELEN WILLIAMS; MI (member ID) H949153864.
Subject DOB 1955-01-17, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: KEYSTONE SENIOR COMPLETE HMO HMO
- plan date (291): 2024-01-21
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: KEYSTONE SENIOR COMPLETE HMO; PI (payer ID) 1650382917; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: HELEN WILLIAMS; MI (member ID) H949153864.
Subject DOB 1955-01-17, sex M.
Eligibility exchange reference ELG74413189, dated 2025-04-04 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2024-02-07, action code WQ, amount $141.61.
D9 (clearinghouse claim number): TRC14477087.
Trace (2 (referenced transaction trace)): TRC14477087.
received date (050): 2024-02-07.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: HELEN WILLIAMS; MI (member ID) H949153864.
Acknowledgment reference ACK14477087, dated 2024-02-07 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2024-01-21. Dx: Pain in right shoulder. 97110 (31 min): therapeutic exercise for strength and ROM. 97112 (14 min): neuromuscular re-education of movement and balance. Total timed minutes: 45. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1650382917, interchange 718942811 date 250404 time 0800 version 00501 usage P; group HS control 718942811 date 20250404 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1650382917 to receiver [ZZ] 1801579548, interchange 245868440 date 250404 time 0800 version 00501 usage P; group HB control 245868440 date 20250404 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1650382917, interchange 840946948 date 250318 time 0800 version 00501 usage P; group HC control 840946948 date 20250318 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 457323303 date 240207 time 0800 version 00501 usage P; group HN control 457323303 date 20240207 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1650382917 to receiver [ZZ] 1801579548, interchange 755450118 date 250402 time 0800 version 00501 usage P; group HP control 755450118 date 20250402 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 27
