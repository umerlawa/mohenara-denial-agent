# Case MOH2-000328

Patient HELEN WILLIAMS, DOB 1955-01-17, sex M, member ID H949153864. Payer: KEYSTONE SENIOR COMPLETE HMO. Service date 2024-03-21.

## Adjudication outcome (835)
Claim PA25296013: status 4 (denied). Billed $106.4, paid $0, patient responsibility . Filing indicator HM (HMO). Payer claim control 2412309959637, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2024-05-02.
Payer [PR]: KEYSTONE SENIOR COMPLETE HMO; 35 PENN CENTER BLVD; PHILADELPHIA, PA, 191031800; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT648663377, originator 1165038291.
claim statement period start (232): 2024-03-21.
Outpatient adjudication remarks (MOA): M77 (missing/incomplete/invalid place of service).
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97530-GO | 1 | $57.08 | $0 | CO-5 (Contractual Obligation: procedure code/type of bill is inconsistent with the place of service) $57.08 |  |
| 2 | 97535-GO | 1 | $49.32 | $0 | CO-5 (Contractual Obligation: procedure code/type of bill is inconsistent with the place of service) $49.32 |  |

Line item control numbers (REF 6R): PA25296013L1, PA25296013L2.
Modifiers on remit lines: GO (under OT plan of care).
Remit claim parties: patient [QC]: HELEN WILLIAMS; MI (member ID) H949153864; rendering provider [82]: DOROTHY LOPEZ; XX (NPI) 1390221007.

## Claim as billed (837P)
Claim PA25296013, total charge $106.4, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25511 (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing HM (HMO).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97530-GO | 1 UN | $57.08 | 2024-03-21 | 1 | PA25296013L1 |
| 2 | 97535-GO | 1 UN | $49.32 | 2024-03-21 | 1 | PA25296013L2 |

Modifiers on claim: GO (under OT plan of care).

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: KEYSTONE SENIOR COMPLETE HMO; 46 (ETIN) 1650382917
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: HELEN WILLIAMS; MI (member ID) H949153864; 7432 OAK ST; TRENTON, NJ, 08685
- payer [PR]: KEYSTONE SENIOR COMPLETE HMO; PI (payer ID) 1650382917
- referring provider [DN]: FATIMA AL-RASHID; XX (NPI) 1333183066
- rendering provider [82]: DOROTHY LOPEZ; XX (NPI) 1390221007
- Submission reference TRC34319475, dated 2024-03-25 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2024-03-21.
Inquiry parties: payer [PR]: KEYSTONE SENIOR COMPLETE HMO; PI (payer ID) 1650382917; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: HELEN WILLIAMS; MI (member ID) H949153864.
Subject DOB 1955-01-17, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: KEYSTONE SENIOR COMPLETE HMO HMO
- plan date (291): 2024-03-21
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: KEYSTONE SENIOR COMPLETE HMO; PI (payer ID) 1650382917; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: HELEN WILLIAMS; MI (member ID) H949153864.
Subject DOB 1955-01-17, sex M.
Eligibility exchange reference ELG38482877, dated 2024-05-06 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2024-03-25, action code WQ, amount $106.4.
D9 (clearinghouse claim number): TRC34319475.
Trace (2 (referenced transaction trace)): TRC34319475.
received date (050): 2024-03-25.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: HELEN WILLIAMS; MI (member ID) H949153864.
Acknowledgment reference ACK34319475, dated 2024-03-25 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

OT treatment note 2024-03-21. Dx: Pain in right shoulder. 97530 (14 min): therapeutic activities (dynamic functional tasks). 97535 (15 min): self-care/home management training. Total timed minutes: 29. Encounter completed by live interactive video with the patient at their residence; documented consent for telehealth services. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1650382917, interchange 104540972 date 240506 time 0800 version 00501 usage P; group HS control 104540972 date 20240506 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1650382917 to receiver [ZZ] 1801579548, interchange 586191629 date 240506 time 0800 version 00501 usage P; group HB control 586191629 date 20240506 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1650382917, interchange 381587206 date 240325 time 0800 version 00501 usage P; group HC control 381587206 date 20240325 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 959171936 date 240325 time 0800 version 00501 usage P; group HN control 959171936 date 20240325 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1650382917 to receiver [ZZ] 1801579548, interchange 648663377 date 240502 time 0800 version 00501 usage P; group HP control 648663377 date 20240502 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 27
