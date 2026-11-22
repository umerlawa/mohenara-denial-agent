# Case MOH2-000667

Patient JESSICA GARCIA, DOB 1983-02-05, sex F, member ID YAW396438474. Payer: ATLANTIC SHORE ASSURANCE. Service date 2026-05-30.

## Adjudication outcome (835)
Claim PA21377407: status 4 (denied). Billed $177.54, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2618655503942, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-07-05.
Payer [PR]: ATLANTIC SHORE ASSURANCE; 3499 ROUTE 9 N; FREEHOLD, NJ, 077283100; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT497234260, originator 1125037465.
claim statement period start (232): 2026-05-30.
Outpatient adjudication remarks (MOA): M77 (missing/incomplete/invalid place of service).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97112-GP | 1 | $55.96 | $0 | CO-5 (Contractual Obligation: procedure code/type of bill is inconsistent with the place of service) $55.96 |  |
| 2 | 97530-GP | 1 | $61.27 | $0 | CO-5 (Contractual Obligation: procedure code/type of bill is inconsistent with the place of service) $61.27 |  |
| 3 | 97530-GP | 1 | $60.31 | $0 | CO-5 (Contractual Obligation: procedure code/type of bill is inconsistent with the place of service) $60.31 |  |

Line item control numbers (REF 6R): PA21377407L1, PA21377407L2, PA21377407L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: JESSICA GARCIA; MI (member ID) YAW396438474; rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737.

## Claim as billed (837P)
Claim PA21377407, total charge $177.54, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97112-GP | 1 UN | $55.96 | 2026-05-30 | 1 | PA21377407L1 |
| 2 | 97530-GP | 1 UN | $61.27 | 2026-05-30 | 1 | PA21377407L2 |
| 3 | 97530-GP | 1 UN | $60.31 | 2026-05-30 | 1 | PA21377407L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: ATLANTIC SHORE ASSURANCE; 46 (ETIN) 1250374659
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: JESSICA GARCIA; MI (member ID) YAW396438474; 6598 FRANKLIN ST; STATEN ISLAND, NY, 10356
- payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659
- referring provider [DN]: FATIMA AL-RASHID; XX (NPI) 1333183066
- rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737
- Submission reference TRC59614696, dated 2026-06-03 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-05-30.
Inquiry parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: JESSICA GARCIA; MI (member ID) YAW396438474.
Subject DOB 1983-02-05, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: ATLANTIC SHORE ASSURANCE EPO
- plan date (291): 2026-05-30
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: JESSICA GARCIA; MI (member ID) YAW396438474.
Subject DOB 1983-02-05, sex F.
Eligibility exchange reference ELG43180067, dated 2026-07-11 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-06-04, action code WQ, amount $177.54.
D9 (clearinghouse claim number): TRC59614696.
Trace (2 (referenced transaction trace)): TRC59614696.
received date (050): 2026-06-04.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: JESSICA GARCIA; MI (member ID) YAW396438474.
Acknowledgment reference ACK59614696, dated 2026-06-04 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-05-30. Dx: Aftercare following joint replacement surgery. 97112 (15 min): neuromuscular re-education of movement and balance. 97530 (16 min): therapeutic activities (dynamic functional tasks). 97530 (15 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 46. Care delivered remotely via two-way real-time audio-video; patient located at home, consent for virtual care recorded. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1250374659, interchange 276848849 date 260711 time 0800 version 00501 usage P; group HS control 276848849 date 20260711 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1250374659 to receiver [ZZ] 1601336180, interchange 190362723 date 260711 time 0800 version 00501 usage P; group HB control 190362723 date 20260711 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1250374659, interchange 124719781 date 260603 time 0800 version 00501 usage P; group HC control 124719781 date 20260603 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 175341385 date 260604 time 0800 version 00501 usage P; group HN control 175341385 date 20260604 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1250374659 to receiver [ZZ] 1601336180, interchange 497234260 date 260705 time 0800 version 00501 usage P; group HP control 497234260 date 20260705 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
