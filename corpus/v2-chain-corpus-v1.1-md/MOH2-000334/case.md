# Case MOH2-000334

Patient KAREN LEWIS, DOB 1969-10-02, sex F, member ID PPB161431266. Payer: ATLANTIC SHORE ASSURANCE. Service date 2025-06-21.

## Adjudication outcome (835)
Claim PA24499972: status 4 (denied). Billed $90.94, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2624805819725, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-09-05.
Payer [PR]: ATLANTIC SHORE ASSURANCE; 3499 ROUTE 9 N; FREEHOLD, NJ, 077283100; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT195179239, originator 1125037465.
claim statement period start (232): 2025-06-21.
Outpatient adjudication remarks (MOA): N211 (you may not appeal this decision).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $46.34 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $46.34 |  |
| 2 | 97110-GP | 1 | $44.6 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $44.6 |  |

Line item control numbers (REF 6R): PA24499972L1, PA24499972L2.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: KAREN LEWIS; MI (member ID) PPB161431266; rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737.

## Claim as billed (837P)
Claim PA24499972, total charge $90.94, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25512 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $46.34 | 2025-06-21 | 1 | PA24499972L1 |
| 2 | 97110-GP | 1 UN | $44.6 | 2025-06-21 | 1 | PA24499972L2 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: ATLANTIC SHORE ASSURANCE; 46 (ETIN) 1250374659
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: KAREN LEWIS; MI (member ID) PPB161431266; 7162 LINCOLN LN; PHILADELPHIA, PA, 19167
- payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659
- referring provider [DN]: ROBERT KIMURA; XX (NPI) 1609960205
- rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737
- Submission reference TRC86768843, dated 2026-08-13 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2025-06-21.
Inquiry parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: KAREN LEWIS; MI (member ID) PPB161431266.
Subject DOB 1969-10-02, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: ATLANTIC SHORE ASSURANCE POS
- plan date (291): 2025-06-21
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: KAREN LEWIS; MI (member ID) PPB161431266.
Subject DOB 1969-10-02, sex F.
Eligibility exchange reference ELG13735306, dated 2026-09-11 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2025-07-10, action code WQ, amount $90.94.
D9 (clearinghouse claim number): TRC86768843.
Trace (2 (referenced transaction trace)): TRC86768843.
received date (050): 2025-07-10.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: KAREN LEWIS; MI (member ID) PPB161431266.
Acknowledgment reference ACK86768843, dated 2025-07-10 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2025-06-21. Dx: Pain in left shoulder. 97110 (16 min): therapeutic exercise for strength and ROM. 97110 (15 min): therapeutic exercise for strength and ROM. Total timed minutes: 31. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1250374659, interchange 389054046 date 260911 time 0800 version 00501 usage P; group HS control 389054046 date 20260911 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1250374659 to receiver [ZZ] 1601336180, interchange 426855759 date 260911 time 0800 version 00501 usage P; group HB control 426855759 date 20260911 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1250374659, interchange 229820328 date 260813 time 0800 version 00501 usage P; group HC control 229820328 date 20260813 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 118472824 date 250710 time 0800 version 00501 usage P; group HN control 118472824 date 20250710 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1250374659 to receiver [ZZ] 1601336180, interchange 195179239 date 260905 time 0800 version 00501 usage P; group HP control 195179239 date 20260905 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 27
