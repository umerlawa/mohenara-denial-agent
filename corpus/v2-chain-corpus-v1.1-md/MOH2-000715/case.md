# Case MOH2-000715

Patient HELEN WILSON, DOB 1973-01-25, sex F, member ID NUQ114921162. Payer: DELAWARE VALLEY MUTUAL. Service date 2026-01-24.

## Adjudication outcome (835)
Claim PA22887535: status 4 (denied). Billed $78.94, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2607808483299, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-03-19.
Payer [PR]: DELAWARE VALLEY MUTUAL; 900 SHIPLEY RD; WILMINGTON, DE, 198033012; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT463963680, originator 1155019382.
claim statement period start (232): 2026-01-24.
Outpatient adjudication remarks (MOA): N111 (no appeal right except duplicate claim/service issue).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $39.66 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $39.66 |  |
| 2 | 97140-GP | 1 | $39.28 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $39.28 |  |

Line item control numbers (REF 6R): PA22887535L1, PA22887535L2.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: HELEN WILSON; MI (member ID) NUQ114921162; rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737.

## Claim as billed (837P)
Claim PA22887535, total charge $78.94, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M1712 (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $39.66 | 2026-01-24 | 1 | PA22887535L1 |
| 2 | 97140-GP | 1 UN | $39.28 | 2026-01-24 | 1 | PA22887535L2 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: DELAWARE VALLEY MUTUAL; 46 (ETIN) 1550193826
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: HELEN WILSON; MI (member ID) NUQ114921162; 7732 WILLOW ST; STATEN ISLAND, NY, 10307
- payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826
- referring provider [DN]: GRETA LINDQVIST; XX (NPI) 1205658765
- rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737
- Submission reference TRC98714053, dated 2026-03-03 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-01-24.
Inquiry parties: payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: HELEN WILSON; MI (member ID) NUQ114921162.
Subject DOB 1973-01-25, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: DELAWARE VALLEY MUTUAL HMO
- plan date (291): 2026-01-24
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: HELEN WILSON; MI (member ID) NUQ114921162.
Subject DOB 1973-01-25, sex F.
Eligibility exchange reference ELG13959346, dated 2026-03-23 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-03-05, action code WQ, amount $78.94.
D9 (clearinghouse claim number): TRC98714053.
Trace (2 (referenced transaction trace)): TRC98714053.
received date (050): 2026-03-05.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: HELEN WILSON; MI (member ID) NUQ114921162.
Acknowledgment reference ACK98714053, dated 2026-03-05 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-01-24. Dx: Unilateral primary osteoarthritis left knee. 97110 (16 min): therapeutic exercise for strength and ROM. 97140 (16 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 32. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1550193826, interchange 732532132 date 260323 time 0800 version 00501 usage P; group HS control 732532132 date 20260323 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1550193826 to receiver [ZZ] 1601336180, interchange 754032813 date 260323 time 0800 version 00501 usage P; group HB control 754032813 date 20260323 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1550193826, interchange 285373101 date 260303 time 0800 version 00501 usage P; group HC control 285373101 date 20260303 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 531699534 date 260305 time 0800 version 00501 usage P; group HN control 531699534 date 20260305 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1550193826 to receiver [ZZ] 1601336180, interchange 463963680 date 260319 time 0800 version 00501 usage P; group HP control 463963680 date 20260319 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 27
