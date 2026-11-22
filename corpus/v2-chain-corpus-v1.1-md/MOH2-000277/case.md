# Case MOH2-000277

Patient ELIZABETH MARTINEZ, DOB 1981-05-11, sex M, member ID EUG481148600. Payer: GARDEN STATE BENEFIT TRUST. Service date 2025-01-30.

## Adjudication outcome (835)
Claim PA24574375: status 4 (denied). Billed $132.27, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2506963145679, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2025-03-10.
Payer [PR]: GARDEN STATE BENEFIT TRUST; 210 RARITAN PLAZA; EDISON, NJ, 088373105; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820.
Trace (1 (current transaction trace)): EFT792977982, originator 1145082736.
claim statement period start (232): 2025-01-30.
Outpatient adjudication remarks (MOA): N286 (missing/incomplete/invalid referring provider primary identifier).
Payee TJ (federal tax ID): 321822487.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $41.78 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $41.78 |  |
| 2 | 97140-GP | 1 | $43.68 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $43.68 |  |
| 3 | 97530-GP | 1 | $46.81 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $46.81 |  |

Line item control numbers (REF 6R): PA24574375L1, PA24574375L2, PA24574375L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: ELIZABETH MARTINEZ; MI (member ID) EUG481148600; rendering provider [82]: MICHAEL MARTINEZ; XX (NPI) 1850202042.

## Claim as billed (837P)
Claim PA24574375, total charge $132.27, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25511 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $41.78 | 2025-01-30 | 1 | PA24574375L1 |
| 2 | 97140-GP | 1 UN | $43.68 | 2025-01-30 | 1 | PA24574375L2 |
| 3 | 97530-GP | 1 UN | $46.81 | 2025-01-30 | 1 | PA24574375L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: GARDEN STATE BENEFIT TRUST; 46 (ETIN) 1450827364
- billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820; EI (employer ID/EIN) 321822487
- insured/subscriber [IL]: ELIZABETH MARTINEZ; MI (member ID) EUG481148600; 7589 MAPLE ST; TRENTON, NJ, 08604
- payer [PR]: GARDEN STATE BENEFIT TRUST; PI (payer ID) 1450827364
- rendering provider [82]: MICHAEL MARTINEZ; XX (NPI) 1850202042
- Submission reference TRC51623454, dated 2025-02-04 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2025-01-30.
Inquiry parties: payer [PR]: GARDEN STATE BENEFIT TRUST; PI (payer ID) 1450827364; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: ELIZABETH MARTINEZ; MI (member ID) EUG481148600.
Subject DOB 1981-05-11, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: GARDEN STATE BENEFIT TRUST HMO
- plan date (291): 2025-01-30
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: GARDEN STATE BENEFIT TRUST; PI (payer ID) 1450827364; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: ELIZABETH MARTINEZ; MI (member ID) EUG481148600.
Subject DOB 1981-05-11, sex M.
Eligibility exchange reference ELG93291033, dated 2025-03-16 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2025-02-05, action code WQ, amount $132.27.
D9 (clearinghouse claim number): TRC51623454.
Trace (2 (referenced transaction trace)): TRC51623454.
received date (050): 2025-02-05.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; patient [QC]: ELIZABETH MARTINEZ; MI (member ID) EUG481148600.
Acknowledgment reference ACK51623454, dated 2025-02-05 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2025-01-30. Dx: Pain in right shoulder. 97110 (15 min): therapeutic exercise for strength and ROM. 97140 (14 min): manual therapy (soft tissue and joint mobilization). 97530 (15 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 44. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1353206904 to receiver [ZZ] 1450827364, interchange 400914233 date 250316 time 0800 version 00501 usage P; group HS control 400914233 date 20250316 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1450827364 to receiver [ZZ] 1353206904, interchange 358093718 date 250316 time 0800 version 00501 usage P; group HB control 358093718 date 20250316 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 321822487 to receiver [ZZ] 1450827364, interchange 815622663 date 250204 time 0800 version 00501 usage P; group HC control 815622663 date 20250204 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 33
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 321822487, interchange 563623353 date 250205 time 0800 version 00501 usage P; group HN control 563623353 date 20250205 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1450827364 to receiver [ZZ] 1353206904, interchange 792977982 date 250310 time 0800 version 00501 usage P; group HP control 792977982 date 20250310 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
