# Case MOH2-000178

Patient THOMAS BROWN, DOB 1981-03-17, sex F, member ID QAM060915365. Payer: KEYSTONE COMMERCIAL HEALTH. Service date 2025-04-20.

## Adjudication outcome (835)
Claim PA23604163: status 4 (denied). Billed $134.27, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2528187020105, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2025-10-08.
Payer [PR]: KEYSTONE COMMERCIAL HEALTH; 1200 MARKET ST; PHILADELPHIA, PA, 191071200; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT575944941, originator 1165028491.
claim statement period start (232): 2025-04-20.
Outpatient adjudication remarks (MOA): N211 (you may not appeal this decision).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $48.74 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $48.74 |  |
| 2 | 97112-GP | 1 | $46.58 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $46.58 |  |
| 3 | 97110-GP | 1 | $38.95 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $38.95 |  |

Line item control numbers (REF 6R): PA23604163L1, PA23604163L2, PA23604163L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: THOMAS BROWN; MI (member ID) QAM060915365; rendering provider [82]: JOSEPH ANDERSON; XX (NPI) 1260849754.

## Claim as billed (837P)
Claim PA23604163, total charge $134.27, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M1712 (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $48.74 | 2025-04-20 | 1 | PA23604163L1 |
| 2 | 97112-GP | 1 UN | $46.58 | 2025-04-20 | 1 | PA23604163L2 |
| 3 | 97110-GP | 1 UN | $38.95 | 2025-04-20 | 1 | PA23604163L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: KEYSTONE COMMERCIAL HEALTH; 46 (ETIN) 1650284917
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: THOMAS BROWN; MI (member ID) QAM060915365; 3714 WILLOW ST; TRENTON, NJ, 08611
- payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917
- referring provider [DN]: GRETA LINDQVIST; XX (NPI) 1205658765
- rendering provider [82]: JOSEPH ANDERSON; XX (NPI) 1260849754
- Submission reference TRC45153295, dated 2025-09-19 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2025-04-20.
Inquiry parties: payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: THOMAS BROWN; MI (member ID) QAM060915365.
Subject DOB 1981-03-17, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: KEYSTONE COMMERCIAL HEALTH EPO
- plan date (291): 2025-04-20
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: THOMAS BROWN; MI (member ID) QAM060915365.
Subject DOB 1981-03-17, sex F.
Eligibility exchange reference ELG16247299, dated 2025-10-10 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2025-05-02, action code WQ, amount $134.27.
D9 (clearinghouse claim number): TRC45153295.
Trace (2 (referenced transaction trace)): TRC45153295.
received date (050): 2025-05-02.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: THOMAS BROWN; MI (member ID) QAM060915365.
Acknowledgment reference ACK45153295, dated 2025-05-02 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2025-04-20. Dx: Unilateral primary osteoarthritis left knee. 97110 (14 min): therapeutic exercise for strength and ROM. 97112 (15 min): neuromuscular re-education of movement and balance. 97110 (15 min): therapeutic exercise for strength and ROM. Total timed minutes: 44. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1650284917, interchange 683426054 date 251010 time 0800 version 00501 usage P; group HS control 683426054 date 20251010 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1650284917 to receiver [ZZ] 1601336180, interchange 474377470 date 251010 time 0800 version 00501 usage P; group HB control 474377470 date 20251010 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1650284917, interchange 523146953 date 250919 time 0800 version 00501 usage P; group HC control 523146953 date 20250919 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 682123711 date 250502 time 0800 version 00501 usage P; group HN control 682123711 date 20250502 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1650284917 to receiver [ZZ] 1601336180, interchange 575944941 date 251008 time 0800 version 00501 usage P; group HP control 575944941 date 20251008 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
