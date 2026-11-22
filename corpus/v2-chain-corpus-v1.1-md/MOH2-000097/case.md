# Case MOH2-000097

Patient KAREN LEWIS, DOB 1969-10-02, sex F, member ID PPB161431266. Payer: ATLANTIC SHORE ASSURANCE. Service date 2025-07-08.

## Adjudication outcome (835)
Claim PA28187579: status 4 (denied). Billed $173.83, paid $0, patient responsibility $173.83. Filing indicator CI (commercial insurance). Payer claim control 2522797493587, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2025-08-15.
Payer [PR]: ATLANTIC SHORE ASSURANCE; 3499 ROUTE 9 N; FREEHOLD, NJ, 077283100; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT224779314, originator 1125037465.
claim statement period start (232): 2025-07-08.
Outpatient adjudication remarks (MOA): N30 (patient ineligible for this service).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $45.93 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $45.93 |  |
| 2 | 97140-GP | 2 | $84.27 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $84.27 |  |
| 3 | 97140-GP | 1 | $43.63 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $43.63 |  |

Line item control numbers (REF 6R): PA28187579L1, PA28187579L2, PA28187579L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: KAREN LEWIS; MI (member ID) PPB161431266; rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737.

## Claim as billed (837P)
Claim PA28187579, total charge $173.83, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25512 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $45.93 | 2025-07-08 | 1 | PA28187579L1 |
| 2 | 97140-GP | 2 UN | $84.27 | 2025-07-08 | 1 | PA28187579L2 |
| 3 | 97140-GP | 1 UN | $43.63 | 2025-07-08 | 1 | PA28187579L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: ATLANTIC SHORE ASSURANCE; 46 (ETIN) 1250374659
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: KAREN LEWIS; MI (member ID) PPB161431266; 7162 LINCOLN LN; PHILADELPHIA, PA, 19167
- payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659
- referring provider [DN]: ROBERT KIMURA; XX (NPI) 1609960205
- rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737
- Submission reference TRC70522255, dated 2025-07-28 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2025-07-08.
Inquiry parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: KAREN LEWIS; MI (member ID) PPB161431266.
Subject DOB 1969-10-02, sex F.

Response:
- benefit: 6 (inactive), coverage level IND, service type 30 (health benefit plan coverage), plan: ATLANTIC SHORE ASSURANCE POS
- plan date (291): 2025-07-08
- eligibility begin (356): 2024-01-01
- eligibility end (357): 2025-06-30
Response parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: KAREN LEWIS; MI (member ID) PPB161431266.
Subject DOB 1969-10-02, sex F.
Eligibility exchange reference ELG60110152, dated 2025-08-21 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2025-07-29, action code WQ, amount $173.83.
D9 (clearinghouse claim number): TRC70522255.
Trace (2 (referenced transaction trace)): TRC70522255.
received date (050): 2025-07-29.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: KAREN LEWIS; MI (member ID) PPB161431266.
Acknowledgment reference ACK70522255, dated 2025-07-29 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2025-07-08. Dx: Pain in left shoulder. 97110 (14 min): therapeutic exercise for strength and ROM. 97140 (29 min): manual therapy (soft tissue and joint mobilization). 97140 (15 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 58. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1250374659, interchange 910695650 date 250821 time 0800 version 00501 usage P; group HS control 910695650 date 20250821 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1250374659 to receiver [ZZ] 1601336180, interchange 326911240 date 250821 time 0800 version 00501 usage P; group HB control 326911240 date 20250821 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 14
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1250374659, interchange 423686167 date 250728 time 0800 version 00501 usage P; group HC control 423686167 date 20250728 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 797534729 date 250729 time 0800 version 00501 usage P; group HN control 797534729 date 20250729 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1250374659 to receiver [ZZ] 1601336180, interchange 224779314 date 250815 time 0800 version 00501 usage P; group HP control 224779314 date 20250815 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
