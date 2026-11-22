# Case MOH2-000554

Patient THOMAS BROWN, DOB 1981-03-17, sex F, member ID QAM060915365. Payer: KEYSTONE COMMERCIAL HEALTH. Service date 2025-04-24.

## Adjudication outcome (835)
Claim PA26838484: status 1 (processed as primary, paid). Billed $226.66, paid $118.92, patient responsibility $29.71. Filing indicator CI (commercial insurance). Payer claim control 2516286564849, POS 11 (office), frequency 1 (original claim).
Payment: $118.92 by CHK (check), handling I.
production date (405): 2025-06-11.
Payer [PR]: KEYSTONE COMMERCIAL HEALTH; 1200 MARKET ST; PHILADELPHIA, PA, 191071200; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT102824707, originator 1165028491.
claim statement period start (232): 2025-04-24.
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 | $87.38 | $46.5 allowed (B6) $58.12 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $29.26; PR-2 (Patient Responsibility: coinsurance amount) $11.62 |  |
| 2 | 97530-GP | 1 | $53.23 | $28.06 allowed (B6) $35.07 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $18.16; PR-2 (Patient Responsibility: coinsurance amount) $7.01 |  |
| 3 | 97140-GP | 1 | $46.77 | $22.18 allowed (B6) $27.72 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $19.05; PR-2 (Patient Responsibility: coinsurance amount) $5.54 |  |
| 4 | 97140-GP | 1 | $39.28 | $22.18 allowed (B6) $27.72 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $11.56; PR-2 (Patient Responsibility: coinsurance amount) $5.54 |  |

Line item control numbers (REF 6R): PA26838484L1, PA26838484L2, PA26838484L3, PA26838484L4.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: THOMAS BROWN; MI (member ID) QAM060915365; rendering provider [82]: JOSEPH ANDERSON; XX (NPI) 1260849754.

## Claim as billed (837P)
Claim PA26838484, total charge $226.66, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M1712 (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 UN | $87.38 | 2025-04-24 | 1 | PA26838484L1 |
| 2 | 97530-GP | 1 UN | $53.23 | 2025-04-24 | 1 | PA26838484L2 |
| 3 | 97140-GP | 1 UN | $46.77 | 2025-04-24 | 1 | PA26838484L3 |
| 4 | 97140-GP | 1 UN | $39.28 | 2025-04-24 | 1 | PA26838484L4 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: KEYSTONE COMMERCIAL HEALTH; 46 (ETIN) 1650284917
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: THOMAS BROWN; MI (member ID) QAM060915365; 3714 WILLOW ST; TRENTON, NJ, 08611
- payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917
- referring provider [DN]: GRETA LINDQVIST; XX (NPI) 1205658765
- rendering provider [82]: JOSEPH ANDERSON; XX (NPI) 1260849754
- Submission reference TRC61407128, dated 2025-05-04 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2025-04-24.
Inquiry parties: payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: THOMAS BROWN; MI (member ID) QAM060915365.
Subject DOB 1981-03-17, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: KEYSTONE COMMERCIAL HEALTH EPO
- plan date (291): 2025-04-24
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: THOMAS BROWN; MI (member ID) QAM060915365.
Subject DOB 1981-03-17, sex F.
Eligibility exchange reference ELG61737224, dated 2025-06-18 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2025-05-04, action code WQ, amount $226.66.
D9 (clearinghouse claim number): TRC61407128.
Trace (2 (referenced transaction trace)): TRC61407128.
received date (050): 2025-05-04.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: THOMAS BROWN; MI (member ID) QAM060915365.
Acknowledgment reference ACK61407128, dated 2025-05-04 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2025-04-24. Dx: Unilateral primary osteoarthritis left knee. 97110 (30 min): therapeutic exercise for strength and ROM. 97530 (16 min): therapeutic activities (dynamic functional tasks). 97140 (16 min): manual therapy (soft tissue and joint mobilization). 97140 (14 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 76. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1650284917, interchange 652575579 date 250618 time 0800 version 00501 usage P; group HS control 652575579 date 20250618 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1650284917 to receiver [ZZ] 1601336180, interchange 224382679 date 250618 time 0800 version 00501 usage P; group HB control 224382679 date 20250618 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1650284917, interchange 169544720 date 250504 time 0800 version 00501 usage P; group HC control 169544720 date 20250504 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 38
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 974694353 date 250504 time 0800 version 00501 usage P; group HN control 974694353 date 20250504 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1650284917 to receiver [ZZ] 1601336180, interchange 102824707 date 250611 time 0800 version 00501 usage P; group HP control 102824707 date 20250611 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 42
