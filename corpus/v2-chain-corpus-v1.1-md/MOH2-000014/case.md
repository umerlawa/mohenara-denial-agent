# Case MOH2-000014

Patient HELEN WILLIAMS, DOB 1955-01-17, sex M, member ID H949153864. Payer: KEYSTONE SENIOR COMPLETE HMO. Service date 2024-02-16.

## Adjudication outcome (835)
Claim PA27381031: status 4 (denied). Billed $199.39, paid $0, patient responsibility . Filing indicator HM (HMO). Payer claim control 2409404221242, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2024-04-03.
Payer [PR]: KEYSTONE SENIOR COMPLETE HMO; 35 PENN CENTER BLVD; PHILADELPHIA, PA, 191031800; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT196182583, originator 1165038291.
claim statement period start (232): 2024-02-16.
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110 | 2 | $101.83 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $101.83 | HE N822 (missing procedure modifier(s)) |
| 2 | 97140 | 1 | $45.49 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $45.49 | HE N822 (missing procedure modifier(s)) |
| 3 | 97530 | 1 | $52.07 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $52.07 | HE N822 (missing procedure modifier(s)) |

Line item control numbers (REF 6R): PA27381031L1, PA27381031L2, PA27381031L3.
Remit claim parties: patient [QC]: HELEN WILLIAMS; MI (member ID) H949153864; rendering provider [82]: DOROTHY LOPEZ; XX (NPI) 1390221007.

## Claim as billed (837P)
Claim PA27381031, total charge $199.39, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25511 (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing HM (HMO).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110 | 2 UN | $101.83 | 2024-02-16 | 1 | PA27381031L1 |
| 2 | 97140 | 1 UN | $45.49 | 2024-02-16 | 1 | PA27381031L2 |
| 3 | 97530 | 1 UN | $52.07 | 2024-02-16 | 1 | PA27381031L3 |

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: KEYSTONE SENIOR COMPLETE HMO; 46 (ETIN) 1650382917
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: HELEN WILLIAMS; MI (member ID) H949153864; 7432 OAK ST; TRENTON, NJ, 08685
- payer [PR]: KEYSTONE SENIOR COMPLETE HMO; PI (payer ID) 1650382917
- referring provider [DN]: FATIMA AL-RASHID; XX (NPI) 1333183066
- rendering provider [82]: DOROTHY LOPEZ; XX (NPI) 1390221007
- Submission reference TRC51622456, dated 2024-02-28 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2024-02-16.
Inquiry parties: payer [PR]: KEYSTONE SENIOR COMPLETE HMO; PI (payer ID) 1650382917; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: HELEN WILLIAMS; MI (member ID) H949153864.
Subject DOB 1955-01-17, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: KEYSTONE SENIOR COMPLETE HMO HMO
- plan date (291): 2024-02-16
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: KEYSTONE SENIOR COMPLETE HMO; PI (payer ID) 1650382917; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: HELEN WILLIAMS; MI (member ID) H949153864.
Subject DOB 1955-01-17, sex M.
Eligibility exchange reference ELG47229864, dated 2024-04-09 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2024-02-28, action code WQ, amount $199.39.
D9 (clearinghouse claim number): TRC51622456.
Trace (2 (referenced transaction trace)): TRC51622456.
received date (050): 2024-02-28.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: HELEN WILLIAMS; MI (member ID) H949153864.
Acknowledgment reference ACK51622456, dated 2024-02-28 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2024-02-16. Dx: Pain in right shoulder. 97110 (30 min): therapeutic exercise for strength and ROM. 97140 (15 min): manual therapy (soft tissue and joint mobilization). 97530 (14 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 59. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1650382917, interchange 795909677 date 240409 time 0800 version 00501 usage P; group HS control 795909677 date 20240409 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1650382917 to receiver [ZZ] 1801579548, interchange 996422859 date 240409 time 0800 version 00501 usage P; group HB control 996422859 date 20240409 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1650382917, interchange 266330159 date 240228 time 0800 version 00501 usage P; group HC control 266330159 date 20240228 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 623218923 date 240228 time 0800 version 00501 usage P; group HN control 623218923 date 20240228 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1650382917 to receiver [ZZ] 1801579548, interchange 196182583 date 240403 time 0800 version 00501 usage P; group HP control 196182583 date 20240403 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 33
