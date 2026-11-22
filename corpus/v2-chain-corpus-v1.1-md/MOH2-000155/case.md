# Case MOH2-000155

Patient JESSICA GARCIA, DOB 1983-02-05, sex F, member ID YAW396438474. Payer: ATLANTIC SHORE ASSURANCE. Service date 2026-06-12.

## Adjudication outcome (835)
Claim PA22637322: status 4 (denied). Billed $82.5, paid $0, patient responsibility $82.5. Filing indicator CI (commercial insurance). Payer claim control 2620188847686, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-07-20.
Payer [PR]: ATLANTIC SHORE ASSURANCE; 3499 ROUTE 9 N; FREEHOLD, NJ, 077283100; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT555982387, originator 1125037465.
claim statement period start (232): 2026-06-12.
Outpatient adjudication remarks (MOA): N30 (patient ineligible for this service).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97140-GP | 1 | $43.73 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $43.73 |  |
| 2 | 97140-GP | 1 | $38.77 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $38.77 |  |

Line item control numbers (REF 6R): PA22637322L1, PA22637322L2.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: JESSICA GARCIA; MI (member ID) YAW396438474; rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737.

## Claim as billed (837P)
Claim PA22637322, total charge $82.5, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97140-GP | 1 UN | $43.73 | 2026-06-12 | 1 | PA22637322L1 |
| 2 | 97140-GP | 1 UN | $38.77 | 2026-06-12 | 1 | PA22637322L2 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: ATLANTIC SHORE ASSURANCE; 46 (ETIN) 1250374659
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: JESSICA GARCIA; MI (member ID) YAW396438474; 6598 FRANKLIN ST; STATEN ISLAND, NY, 10356
- payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659
- referring provider [DN]: FATIMA AL-RASHID; XX (NPI) 1333183066
- rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737
- Submission reference TRC42557464, dated 2026-06-17 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-06-12.
Inquiry parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: JESSICA GARCIA; MI (member ID) YAW396438474.
Subject DOB 1983-02-05, sex F.

Response:
- benefit: 6 (inactive), coverage level IND, service type 30 (health benefit plan coverage), plan: ATLANTIC SHORE ASSURANCE EPO
- plan date (291): 2026-06-12
- eligibility begin (356): 2024-01-01
- eligibility end (357): 2026-05-31
Response parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: JESSICA GARCIA; MI (member ID) YAW396438474.
Subject DOB 1983-02-05, sex F.
Eligibility exchange reference ELG94511610, dated 2026-07-22 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-06-18, action code WQ, amount $82.5.
D9 (clearinghouse claim number): TRC42557464.
Trace (2 (referenced transaction trace)): TRC42557464.
received date (050): 2026-06-18.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: JESSICA GARCIA; MI (member ID) YAW396438474.
Acknowledgment reference ACK42557464, dated 2026-06-18 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-06-12. Dx: Aftercare following joint replacement surgery. 97140 (15 min): manual therapy (soft tissue and joint mobilization). 97140 (16 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 31. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1250374659, interchange 133620040 date 260722 time 0800 version 00501 usage P; group HS control 133620040 date 20260722 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1250374659 to receiver [ZZ] 1601336180, interchange 806640703 date 260722 time 0800 version 00501 usage P; group HB control 806640703 date 20260722 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 14
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1250374659, interchange 616219017 date 260617 time 0800 version 00501 usage P; group HC control 616219017 date 20260617 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 472843650 date 260618 time 0800 version 00501 usage P; group HN control 472843650 date 20260618 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1250374659 to receiver [ZZ] 1601336180, interchange 555982387 date 260720 time 0800 version 00501 usage P; group HP control 555982387 date 20260720 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 27
