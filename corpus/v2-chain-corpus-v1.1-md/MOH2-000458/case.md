# Case MOH2-000458

Patient BARBARA GARCIA, DOB 1964-06-20, sex F, member ID QEM676287307. Payer: ATLANTIC SHORE ASSURANCE. Service date 2025-09-13.

## Adjudication outcome (835)
Claim PA21438216: status 4 (denied). Billed $166.75, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2530463955145, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2025-10-31.
Payer [PR]: ATLANTIC SHORE ASSURANCE; 3499 ROUTE 9 N; FREEHOLD, NJ, 077283100; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT950611646, originator 1125037465.
claim statement period start (232): 2025-09-13.
Outpatient adjudication remarks (MOA): M77 (missing/incomplete/invalid place of service).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $44.47 | $0 | CO-5 (Contractual Obligation: procedure code/type of bill is inconsistent with the place of service) $44.47 |  |
| 2 | 97110-GP | 1 | $42.51 | $0 | CO-5 (Contractual Obligation: procedure code/type of bill is inconsistent with the place of service) $42.51 |  |
| 3 | 97110-GP | 2 | $79.77 | $0 | CO-5 (Contractual Obligation: procedure code/type of bill is inconsistent with the place of service) $79.77 |  |

Line item control numbers (REF 6R): PA21438216L1, PA21438216L2, PA21438216L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: BARBARA GARCIA; MI (member ID) QEM676287307; rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737.

## Claim as billed (837P)
Claim PA21438216, total charge $166.75, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25561 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $44.47 | 2025-09-13 | 1 | PA21438216L1 |
| 2 | 97110-GP | 1 UN | $42.51 | 2025-09-13 | 1 | PA21438216L2 |
| 3 | 97110-GP | 2 UN | $79.77 | 2025-09-13 | 1 | PA21438216L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: ATLANTIC SHORE ASSURANCE; 46 (ETIN) 1250374659
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: BARBARA GARCIA; MI (member ID) QEM676287307; 6210 WILLOW LN; STATEN ISLAND, NY, 10346
- payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659
- referring provider [DN]: SARAH CHEN; XX (NPI) 1410042904
- rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737
- Submission reference TRC58340533, dated 2025-10-03 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2025-09-13.
Inquiry parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: BARBARA GARCIA; MI (member ID) QEM676287307.
Subject DOB 1964-06-20, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: ATLANTIC SHORE ASSURANCE PPO
- plan date (291): 2025-09-13
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: BARBARA GARCIA; MI (member ID) QEM676287307.
Subject DOB 1964-06-20, sex F.
Eligibility exchange reference ELG23768510, dated 2025-11-03 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2025-10-05, action code WQ, amount $166.75.
D9 (clearinghouse claim number): TRC58340533.
Trace (2 (referenced transaction trace)): TRC58340533.
received date (050): 2025-10-05.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: BARBARA GARCIA; MI (member ID) QEM676287307.
Acknowledgment reference ACK58340533, dated 2025-10-05 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2025-09-13. Dx: Pain in right knee. 97110 (15 min): therapeutic exercise for strength and ROM. 97110 (14 min): therapeutic exercise for strength and ROM. 97110 (31 min): therapeutic exercise for strength and ROM. Total timed minutes: 60. Telehealth encounter (synchronous audio/video); patient participated from home and verbal consent was documented. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1250374659, interchange 508637217 date 251103 time 0800 version 00501 usage P; group HS control 508637217 date 20251103 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1250374659 to receiver [ZZ] 1601336180, interchange 959715970 date 251103 time 0800 version 00501 usage P; group HB control 959715970 date 20251103 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1250374659, interchange 852373762 date 251003 time 0800 version 00501 usage P; group HC control 852373762 date 20251003 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 591541394 date 251005 time 0800 version 00501 usage P; group HN control 591541394 date 20251005 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1250374659 to receiver [ZZ] 1601336180, interchange 950611646 date 251031 time 0800 version 00501 usage P; group HP control 950611646 date 20251031 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
