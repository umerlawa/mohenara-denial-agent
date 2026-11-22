# Case MOH2-000523

Patient KAREN LEWIS, DOB 1969-10-02, sex F, member ID PPB161431266. Payer: ATLANTIC SHORE ASSURANCE. Service date 2025-06-17.

## Adjudication outcome (835)
Claim PA22684944: status 4 (denied). Billed $137.29, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2521209205333, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2025-07-31.
Payer [PR]: ATLANTIC SHORE ASSURANCE; 3499 ROUTE 9 N; FREEHOLD, NJ, 077283100; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT333224421, originator 1125037465.
claim statement period start (232): 2025-06-17.
Outpatient adjudication remarks (MOA): M77 (missing/incomplete/invalid place of service).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $40.9 | $0 | CO-5 (Contractual Obligation: procedure code/type of bill is inconsistent with the place of service) $40.9 |  |
| 2 | 97110-GP | 1 | $43.48 | $0 | CO-5 (Contractual Obligation: procedure code/type of bill is inconsistent with the place of service) $43.48 |  |
| 3 | 97530-GP | 1 | $52.91 | $0 | CO-5 (Contractual Obligation: procedure code/type of bill is inconsistent with the place of service) $52.91 |  |

Line item control numbers (REF 6R): PA22684944L1, PA22684944L2, PA22684944L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: KAREN LEWIS; MI (member ID) PPB161431266; rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737.

## Claim as billed (837P)
Claim PA22684944, total charge $137.29, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25512 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $40.9 | 2025-06-17 | 1 | PA22684944L1 |
| 2 | 97110-GP | 1 UN | $43.48 | 2025-06-17 | 1 | PA22684944L2 |
| 3 | 97530-GP | 1 UN | $52.91 | 2025-06-17 | 1 | PA22684944L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: ATLANTIC SHORE ASSURANCE; 46 (ETIN) 1250374659
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: KAREN LEWIS; MI (member ID) PPB161431266; 7162 LINCOLN LN; PHILADELPHIA, PA, 19167
- payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659
- referring provider [DN]: ROBERT KIMURA; XX (NPI) 1609960205
- rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737
- Submission reference TRC24177483, dated 2025-06-24 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2025-06-17.
Inquiry parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: KAREN LEWIS; MI (member ID) PPB161431266.
Subject DOB 1969-10-02, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: ATLANTIC SHORE ASSURANCE POS
- plan date (291): 2025-06-17
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: KAREN LEWIS; MI (member ID) PPB161431266.
Subject DOB 1969-10-02, sex F.
Eligibility exchange reference ELG98724756, dated 2025-08-05 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2025-06-24, action code WQ, amount $137.29.
D9 (clearinghouse claim number): TRC24177483.
Trace (2 (referenced transaction trace)): TRC24177483.
received date (050): 2025-06-24.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: KAREN LEWIS; MI (member ID) PPB161431266.
Acknowledgment reference ACK24177483, dated 2025-06-24 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2025-06-17. Dx: Pain in left shoulder. 97110 (16 min): therapeutic exercise for strength and ROM. 97110 (15 min): therapeutic exercise for strength and ROM. 97530 (16 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 47. This was a virtual visit over synchronous video with the patient in their home; telehealth consent obtained and documented. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1250374659, interchange 958062902 date 250805 time 0800 version 00501 usage P; group HS control 958062902 date 20250805 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1250374659 to receiver [ZZ] 1601336180, interchange 725768669 date 250805 time 0800 version 00501 usage P; group HB control 725768669 date 20250805 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1250374659, interchange 737286639 date 250624 time 0800 version 00501 usage P; group HC control 737286639 date 20250624 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 988810743 date 250624 time 0800 version 00501 usage P; group HN control 988810743 date 20250624 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1250374659 to receiver [ZZ] 1601336180, interchange 333224421 date 250731 time 0800 version 00501 usage P; group HP control 333224421 date 20250731 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
