# Case MOH2-000051

Patient THOMAS BROWN, DOB 1981-03-17, sex F, member ID QAM060915365. Payer: KEYSTONE COMMERCIAL HEALTH. Service date 2025-05-06.

## Adjudication outcome (835)
Claim PA26687760: status 4 (denied). Billed $140.97, paid $0, patient responsibility $140.97. Filing indicator CI (commercial insurance). Payer claim control 2514740598221, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2025-05-27.
Payer [PR]: KEYSTONE COMMERCIAL HEALTH; 1200 MARKET ST; PHILADELPHIA, PA, 191071200; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT953057979, originator 1165028491.
claim statement period start (232): 2025-05-06.
Outpatient adjudication remarks (MOA): N30 (patient ineligible for this service).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 | $78.86 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $78.86 |  |
| 2 | 97530-GP | 1 | $62.11 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $62.11 |  |

Line item control numbers (REF 6R): PA26687760L1, PA26687760L2.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: THOMAS BROWN; MI (member ID) QAM060915365; rendering provider [82]: JOSEPH ANDERSON; XX (NPI) 1260849754.

## Claim as billed (837P)
Claim PA26687760, total charge $140.97, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M1712 (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 UN | $78.86 | 2025-05-06 | 1 | PA26687760L1 |
| 2 | 97530-GP | 1 UN | $62.11 | 2025-05-06 | 1 | PA26687760L2 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: KEYSTONE COMMERCIAL HEALTH; 46 (ETIN) 1650284917
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: THOMAS BROWN; MI (member ID) QAM060915365; 3714 WILLOW ST; TRENTON, NJ, 08611
- payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917
- referring provider [DN]: GRETA LINDQVIST; XX (NPI) 1205658765
- rendering provider [82]: JOSEPH ANDERSON; XX (NPI) 1260849754
- Submission reference TRC83246745, dated 2025-05-11 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2025-05-06.
Inquiry parties: payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: THOMAS BROWN; MI (member ID) QAM060915365.
Subject DOB 1981-03-17, sex F.

Response:
- benefit: 6 (inactive), coverage level IND, service type 30 (health benefit plan coverage), plan: KEYSTONE COMMERCIAL HEALTH EPO
- plan date (291): 2025-05-06
- eligibility begin (356): 2024-01-01
- eligibility end (357): 2025-04-30
Response parties: payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: THOMAS BROWN; MI (member ID) QAM060915365.
Subject DOB 1981-03-17, sex F.
Eligibility exchange reference ELG53637008, dated 2025-06-01 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2025-05-11, action code WQ, amount $140.97.
D9 (clearinghouse claim number): TRC83246745.
Trace (2 (referenced transaction trace)): TRC83246745.
received date (050): 2025-05-11.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: THOMAS BROWN; MI (member ID) QAM060915365.
Acknowledgment reference ACK83246745, dated 2025-05-11 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2025-05-06. Dx: Unilateral primary osteoarthritis left knee. 97110 (30 min): therapeutic exercise for strength and ROM. 97530 (14 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 44. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1650284917, interchange 243748486 date 250601 time 0800 version 00501 usage P; group HS control 243748486 date 20250601 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1650284917 to receiver [ZZ] 1601336180, interchange 506137536 date 250601 time 0800 version 00501 usage P; group HB control 506137536 date 20250601 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 14
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1650284917, interchange 988278377 date 250511 time 0800 version 00501 usage P; group HC control 988278377 date 20250511 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 126331801 date 250511 time 0800 version 00501 usage P; group HN control 126331801 date 20250511 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1650284917 to receiver [ZZ] 1601336180, interchange 953057979 date 250527 time 0800 version 00501 usage P; group HP control 953057979 date 20250527 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 27
