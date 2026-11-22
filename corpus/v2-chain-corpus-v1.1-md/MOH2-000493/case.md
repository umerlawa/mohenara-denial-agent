# Case MOH2-000493

Patient DAVID MARTIN, DOB 1953-06-16, sex F, member ID 7UE7JR2CE34. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-07-01.

## Adjudication outcome (835)
Claim PA28846907: status 4 (denied). Billed $145.66, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2620573268443, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-07-24.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT117524640, originator 1184634935.
claim statement period start (232): 2026-07-01.
Outpatient adjudication remarks (MOA): N435 (exceeds number/frequency approved or allowed within time period).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $52.12 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $52.12 |  |
| 2 | 97110-GP | 1 | $50.94 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $50.94 |  |
| 3 | 97140-GP | 1 | $42.6 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $42.6 |  |

Line item control numbers (REF 6R): PA28846907L1, PA28846907L2, PA28846907L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: DAVID MARTIN; MI (member ID) 7UE7JR2CE34; rendering provider [82]: JOSEPH ANDERSON; XX (NPI) 1260849754.

## Claim as billed (837P)
Claim PA28846907, total charge $145.66, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M1712 (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $52.12 | 2026-07-01 | 1 | PA28846907L1 |
| 2 | 97110-GP | 1 UN | $50.94 | 2026-07-01 | 1 | PA28846907L2 |
| 3 | 97140-GP | 1 UN | $42.6 | 2026-07-01 | 1 | PA28846907L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: DAVID MARTIN; MI (member ID) 7UE7JR2CE34; 4138 MAPLE AVE; WILMINGTON, DE, 19809
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: ELENA VASQUEZ; XX (NPI) 1863431679
- rendering provider [82]: JOSEPH ANDERSON; XX (NPI) 1260849754
- Submission reference TRC73171107, dated 2026-07-04 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-07-01.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: DAVID MARTIN; MI (member ID) 7UE7JR2CE34.
Subject DOB 1953-06-16, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-07-01
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: DAVID MARTIN; MI (member ID) 7UE7JR2CE34.
Subject DOB 1953-06-16, sex F.
Eligibility exchange reference ELG36775808, dated 2026-07-30 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-07-06, action code WQ, amount $145.66.
D9 (clearinghouse claim number): TRC73171107.
Trace (2 (referenced transaction trace)): TRC73171107.
received date (050): 2026-07-06.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: DAVID MARTIN; MI (member ID) 7UE7JR2CE34.
Acknowledgment reference ACK73171107, dated 2026-07-06 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-07-01. Dx: Unilateral primary osteoarthritis left knee. 97110 (14 min): therapeutic exercise for strength and ROM. 97110 (15 min): therapeutic exercise for strength and ROM. 97140 (14 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 43. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1846349352, interchange 878379112 date 260730 time 0800 version 00501 usage P; group HS control 878379112 date 20260730 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 311066400 date 260730 time 0800 version 00501 usage P; group HB control 311066400 date 20260730 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1846349352, interchange 936038821 date 260704 time 0800 version 00501 usage P; group HC control 936038821 date 20260704 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 130738351 date 260706 time 0800 version 00501 usage P; group HN control 130738351 date 20260706 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 117524640 date 260724 time 0800 version 00501 usage P; group HP control 117524640 date 20260724 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
