# Case MOH2-000450

Patient THOMAS BROWN, DOB 1981-03-17, sex F, member ID QAM060915365. Payer: KEYSTONE COMMERCIAL HEALTH. Service date 2025-05-10.

## Adjudication outcome (835)
Claim PA26744338: status 4 (denied). Billed $236.41, paid $0, patient responsibility $236.41. Filing indicator CI (commercial insurance). Payer claim control 2516707125494, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2025-06-16.
Payer [PR]: KEYSTONE COMMERCIAL HEALTH; 1200 MARKET ST; PHILADELPHIA, PA, 191071200; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT732388974, originator 1165028491.
claim statement period start (232): 2025-05-10.
Outpatient adjudication remarks (MOA): N30 (patient ineligible for this service).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $39.26 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $39.26 |  |
| 2 | 97530-GP | 1 | $49.75 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $49.75 |  |
| 3 | 97530-GP | 1 | $55.26 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $55.26 |  |
| 4 | 97530-GP | 1 | $46.98 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $46.98 |  |
| 5 | 97110-GP | 1 | $45.16 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $45.16 |  |

Line item control numbers (REF 6R): PA26744338L1, PA26744338L2, PA26744338L3, PA26744338L4, PA26744338L5.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: THOMAS BROWN; MI (member ID) QAM060915365; rendering provider [82]: JOSEPH ANDERSON; XX (NPI) 1260849754.

## Claim as billed (837P)
Claim PA26744338, total charge $236.41, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M1712 (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $39.26 | 2025-05-10 | 1 | PA26744338L1 |
| 2 | 97530-GP | 1 UN | $49.75 | 2025-05-10 | 1 | PA26744338L2 |
| 3 | 97530-GP | 1 UN | $55.26 | 2025-05-10 | 1 | PA26744338L3 |
| 4 | 97530-GP | 1 UN | $46.98 | 2025-05-10 | 1 | PA26744338L4 |
| 5 | 97110-GP | 1 UN | $45.16 | 2025-05-10 | 1 | PA26744338L5 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: KEYSTONE COMMERCIAL HEALTH; 46 (ETIN) 1650284917
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: THOMAS BROWN; MI (member ID) QAM060915365; 3714 WILLOW ST; TRENTON, NJ, 08611
- payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917
- referring provider [DN]: GRETA LINDQVIST; XX (NPI) 1205658765
- rendering provider [82]: JOSEPH ANDERSON; XX (NPI) 1260849754
- Submission reference TRC67762880, dated 2025-05-23 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2025-05-10.
Inquiry parties: payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: THOMAS BROWN; MI (member ID) QAM060915365.
Subject DOB 1981-03-17, sex F.

Response:
- benefit: 6 (inactive), coverage level IND, service type 30 (health benefit plan coverage), plan: KEYSTONE COMMERCIAL HEALTH EPO
- plan date (291): 2025-05-10
- eligibility begin (356): 2024-01-01
- eligibility end (357): 2025-04-30
Response parties: payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: THOMAS BROWN; MI (member ID) QAM060915365.
Subject DOB 1981-03-17, sex F.
Eligibility exchange reference ELG31987768, dated 2025-06-17 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2025-05-25, action code WQ, amount $236.41.
D9 (clearinghouse claim number): TRC67762880.
Trace (2 (referenced transaction trace)): TRC67762880.
received date (050): 2025-05-25.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: THOMAS BROWN; MI (member ID) QAM060915365.
Acknowledgment reference ACK67762880, dated 2025-05-25 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2025-05-10. Dx: Unilateral primary osteoarthritis left knee. 97110 (14 min): therapeutic exercise for strength and ROM. 97530 (15 min): therapeutic activities (dynamic functional tasks). 97530 (15 min): therapeutic activities (dynamic functional tasks). 97530 (16 min): therapeutic activities (dynamic functional tasks). 97110 (14 min): therapeutic exercise for strength and ROM. Total timed minutes: 74. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1650284917, interchange 126930129 date 250617 time 0800 version 00501 usage P; group HS control 126930129 date 20250617 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1650284917 to receiver [ZZ] 1601336180, interchange 990759456 date 250617 time 0800 version 00501 usage P; group HB control 990759456 date 20250617 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 14
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1650284917, interchange 754208661 date 250523 time 0800 version 00501 usage P; group HC control 754208661 date 20250523 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 42
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 612491689 date 250525 time 0800 version 00501 usage P; group HN control 612491689 date 20250525 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1650284917 to receiver [ZZ] 1601336180, interchange 732388974 date 250616 time 0800 version 00501 usage P; group HP control 732388974 date 20250616 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 39
