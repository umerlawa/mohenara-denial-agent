# Case MOH2-000103

Patient HELEN WILSON, DOB 1973-01-25, sex F, member ID NUQ114921162. Payer: DELAWARE VALLEY MUTUAL. Service date 2026-10-04.

## Adjudication outcome (835)
Claim PA27014104: status 4 (denied). Billed $133.39, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2630976521959, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-11-05.
Payer [PR]: DELAWARE VALLEY MUTUAL; 900 SHIPLEY RD; WILMINGTON, DE, 198033012; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT282387932, originator 1155019382.
claim statement period start (232): 2026-10-04.
Outpatient adjudication remarks (MOA): N30 (patient ineligible for this service).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97140-GP | 1 | $38.39 | $0 | CO-27 (Contractual Obligation: expenses incurred after coverage terminated) $38.39 |  |
| 2 | 97112-GP | 1 | $56.75 | $0 | CO-27 (Contractual Obligation: expenses incurred after coverage terminated) $56.75 |  |
| 3 | 97110-GP | 1 | $38.25 | $0 | CO-27 (Contractual Obligation: expenses incurred after coverage terminated) $38.25 |  |

Line item control numbers (REF 6R): PA27014104L1, PA27014104L2, PA27014104L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: HELEN WILSON; MI (member ID) NUQ114921162; rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737.

## Claim as billed (837P)
Claim PA27014104, total charge $133.39, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M1712 (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97140-GP | 1 UN | $38.39 | 2026-10-04 | 1 | PA27014104L1 |
| 2 | 97112-GP | 1 UN | $56.75 | 2026-10-04 | 1 | PA27014104L2 |
| 3 | 97110-GP | 1 UN | $38.25 | 2026-10-04 | 1 | PA27014104L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: DELAWARE VALLEY MUTUAL; 46 (ETIN) 1550193826
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: HELEN WILSON; MI (member ID) NUQ114921162; 7732 WILLOW ST; STATEN ISLAND, NY, 10307
- payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826
- referring provider [DN]: GRETA LINDQVIST; XX (NPI) 1205658765
- rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737
- Submission reference TRC68863437, dated 2026-10-17 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-10-04.
Inquiry parties: payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: HELEN WILSON; MI (member ID) NUQ114921162.
Subject DOB 1973-01-25, sex F.

Response:
- benefit: 6 (inactive), coverage level IND, service type 30 (health benefit plan coverage), plan: DELAWARE VALLEY MUTUAL HMO
- plan date (291): 2026-10-04
- eligibility begin (356): 2024-01-01
- eligibility end (357): 2026-09-30
Response parties: payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: HELEN WILSON; MI (member ID) NUQ114921162.
Subject DOB 1973-01-25, sex F.
Eligibility exchange reference ELG54573988, dated 2026-11-08 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-10-19, action code WQ, amount $133.39.
D9 (clearinghouse claim number): TRC68863437.
Trace (2 (referenced transaction trace)): TRC68863437.
received date (050): 2026-10-19.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: HELEN WILSON; MI (member ID) NUQ114921162.
Acknowledgment reference ACK68863437, dated 2026-10-19 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-10-04. Dx: Unilateral primary osteoarthritis left knee. 97140 (14 min): manual therapy (soft tissue and joint mobilization). 97112 (16 min): neuromuscular re-education of movement and balance. 97110 (15 min): therapeutic exercise for strength and ROM. Total timed minutes: 45. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1550193826, interchange 347175114 date 261108 time 0800 version 00501 usage P; group HS control 347175114 date 20261108 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1550193826 to receiver [ZZ] 1601336180, interchange 923206029 date 261108 time 0800 version 00501 usage P; group HB control 923206029 date 20261108 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 14
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1550193826, interchange 846348951 date 261017 time 0800 version 00501 usage P; group HC control 846348951 date 20261017 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 681583701 date 261019 time 0800 version 00501 usage P; group HN control 681583701 date 20261019 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1550193826 to receiver [ZZ] 1601336180, interchange 282387932 date 261105 time 0800 version 00501 usage P; group HP control 282387932 date 20261105 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
