# Case MOH2-000054

Patient HELEN WILLIAMS, DOB 1955-01-17, sex M, member ID H949153864. Payer: KEYSTONE SENIOR COMPLETE HMO. Service date 2024-04-01.

## Adjudication outcome (835)
Claim PA24357393: status 1 (processed as primary, paid). Billed $443.88, paid $51.84, patient responsibility $12.96. Filing indicator HM (HMO). Payer claim control 2412907570815, POS 11 (office), frequency 1 (original claim).
Payment: $51.84 by CHK (check), handling I.
production date (405): 2024-05-08.
Payer [PR]: KEYSTONE SENIOR COMPLETE HMO; 35 PENN CENTER BLVD; PHILADELPHIA, PA, 191031800; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT122615418, originator 1165038291.
claim statement period start (232): 2024-04-01.
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97535-GO | 1 | $46.35 | $25.92 allowed (B6) $32.4 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $13.95; PR-2 (Patient Responsibility: coinsurance amount) $6.48 |  |
| 2 | 97535-GO | 1 | $58.03 | $25.92 allowed (B6) $32.4 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $25.63; PR-2 (Patient Responsibility: coinsurance amount) $6.48 |  |
| 3 | 97110-GO | 7 | $339.5 | $0 | CO-151 (Contractual Obligation: information does not support this many/frequency of services) $339.5 | HE N362 (the number of days or units exceeds the acceptable maximum) |

Line item control numbers (REF 6R): PA24357393L1, PA24357393L2, PA24357393L3.
Modifiers on remit lines: GO (under OT plan of care).
Remit claim parties: patient [QC]: HELEN WILLIAMS; MI (member ID) H949153864; rendering provider [82]: DOROTHY LOPEZ; XX (NPI) 1390221007.

## Claim as billed (837P)
Claim PA24357393, total charge $443.88, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25511 (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing HM (HMO).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97535-GO | 1 UN | $46.35 | 2024-04-01 | 1 | PA24357393L1 |
| 2 | 97535-GO | 1 UN | $58.03 | 2024-04-01 | 1 | PA24357393L2 |
| 3 | 97110-GO | 7 UN | $339.5 | 2024-04-01 | 1 | PA24357393L3 |

Modifiers on claim: GO (under OT plan of care).

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: KEYSTONE SENIOR COMPLETE HMO; 46 (ETIN) 1650382917
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: HELEN WILLIAMS; MI (member ID) H949153864; 7432 OAK ST; TRENTON, NJ, 08685
- payer [PR]: KEYSTONE SENIOR COMPLETE HMO; PI (payer ID) 1650382917
- referring provider [DN]: FATIMA AL-RASHID; XX (NPI) 1333183066
- rendering provider [82]: DOROTHY LOPEZ; XX (NPI) 1390221007
- Submission reference TRC29810589, dated 2024-04-04 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2024-04-01.
Inquiry parties: payer [PR]: KEYSTONE SENIOR COMPLETE HMO; PI (payer ID) 1650382917; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: HELEN WILLIAMS; MI (member ID) H949153864.
Subject DOB 1955-01-17, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: KEYSTONE SENIOR COMPLETE HMO HMO
- plan date (291): 2024-04-01
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: KEYSTONE SENIOR COMPLETE HMO; PI (payer ID) 1650382917; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: HELEN WILLIAMS; MI (member ID) H949153864.
Subject DOB 1955-01-17, sex M.
Eligibility exchange reference ELG27398795, dated 2024-05-13 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2024-04-06, action code WQ, amount $443.88.
D9 (clearinghouse claim number): TRC29810589.
Trace (2 (referenced transaction trace)): TRC29810589.
received date (050): 2024-04-06.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: HELEN WILLIAMS; MI (member ID) H949153864.
Acknowledgment reference ACK29810589, dated 2024-04-06 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

OT treatment note 2024-04-01. Dx: Pain in right shoulder. 97535 (14 min): self-care/home management training. 97535 (15 min): self-care/home management training. 97110 (16 min): therapeutic exercise for strength and ROM. Total timed minutes: 45. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1650382917, interchange 376240932 date 240513 time 0800 version 00501 usage P; group HS control 376240932 date 20240513 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1650382917 to receiver [ZZ] 1801579548, interchange 789745675 date 240513 time 0800 version 00501 usage P; group HB control 789745675 date 20240513 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1650382917, interchange 589302737 date 240404 time 0800 version 00501 usage P; group HC control 589302737 date 20240404 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 751008200 date 240406 time 0800 version 00501 usage P; group HN control 751008200 date 20240406 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1650382917 to receiver [ZZ] 1801579548, interchange 122615418 date 240508 time 0800 version 00501 usage P; group HP control 122615418 date 20240508 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 35
