# Case MOH2-000386

Patient BARBARA GARCIA, DOB 1964-06-20, sex F, member ID QEM676287307. Payer: ATLANTIC SHORE ASSURANCE. Service date 2025-10-08.

## Adjudication outcome (835)
Claim PA25306547: status 4 (denied). Billed $184.7, paid $0, patient responsibility $184.7. Filing indicator CI (commercial insurance). Payer claim control 2531315366113, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2025-11-09.
Payer [PR]: ATLANTIC SHORE ASSURANCE; 3499 ROUTE 9 N; FREEHOLD, NJ, 077283100; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT182752644, originator 1125037465.
claim statement period start (232): 2025-10-08.
Outpatient adjudication remarks (MOA): N30 (patient ineligible for this service).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $44.29 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $44.29 |  |
| 2 | 97110-GP | 2 | $93.01 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $93.01 |  |
| 3 | 97110-GP | 1 | $47.4 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $47.4 |  |

Line item control numbers (REF 6R): PA25306547L1, PA25306547L2, PA25306547L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: BARBARA GARCIA; MI (member ID) QEM676287307; rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737.

## Claim as billed (837P)
Claim PA25306547, total charge $184.7, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25561 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $44.29 | 2025-10-08 | 1 | PA25306547L1 |
| 2 | 97110-GP | 2 UN | $93.01 | 2025-10-08 | 1 | PA25306547L2 |
| 3 | 97110-GP | 1 UN | $47.4 | 2025-10-08 | 1 | PA25306547L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: ATLANTIC SHORE ASSURANCE; 46 (ETIN) 1250374659
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: BARBARA GARCIA; MI (member ID) QEM676287307; 6210 WILLOW LN; STATEN ISLAND, NY, 10346
- payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659
- referring provider [DN]: SARAH CHEN; XX (NPI) 1410042904
- rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737
- Submission reference TRC17154117, dated 2025-10-22 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2025-10-08.
Inquiry parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: BARBARA GARCIA; MI (member ID) QEM676287307.
Subject DOB 1964-06-20, sex F.

Response:
- benefit: 6 (inactive), coverage level IND, service type 30 (health benefit plan coverage), plan: ATLANTIC SHORE ASSURANCE PPO
- plan date (291): 2025-10-08
- eligibility begin (356): 2024-01-01
- eligibility end (357): 2025-09-30
Response parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: BARBARA GARCIA; MI (member ID) QEM676287307.
Subject DOB 1964-06-20, sex F.
Eligibility exchange reference ELG31895460, dated 2025-11-16 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2025-10-23, action code WQ, amount $184.7.
D9 (clearinghouse claim number): TRC17154117.
Trace (2 (referenced transaction trace)): TRC17154117.
received date (050): 2025-10-23.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: BARBARA GARCIA; MI (member ID) QEM676287307.
Acknowledgment reference ACK17154117, dated 2025-10-23 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2025-10-08. Dx: Pain in right knee. 97110 (14 min): therapeutic exercise for strength and ROM. 97110 (31 min): therapeutic exercise for strength and ROM. 97110 (16 min): therapeutic exercise for strength and ROM. Total timed minutes: 61. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1250374659, interchange 749537861 date 251116 time 0800 version 00501 usage P; group HS control 749537861 date 20251116 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1250374659 to receiver [ZZ] 1601336180, interchange 881957410 date 251116 time 0800 version 00501 usage P; group HB control 881957410 date 20251116 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 14
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1250374659, interchange 704032660 date 251022 time 0800 version 00501 usage P; group HC control 704032660 date 20251022 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 832231791 date 251023 time 0800 version 00501 usage P; group HN control 832231791 date 20251023 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1250374659 to receiver [ZZ] 1601336180, interchange 182752644 date 251109 time 0800 version 00501 usage P; group HP control 182752644 date 20251109 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
