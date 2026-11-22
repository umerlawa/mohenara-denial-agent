# Case MOH2-000688

Patient BARBARA LEE, DOB 1982-03-23, sex F, member ID JYH092021893. Payer: GARDEN STATE BENEFIT TRUST. Service date 2026-08-06.

## Adjudication outcome (835)
Claim PA29382903: status 1 (processed as primary, paid). Billed $158.17, paid $74.56, patient responsibility $18.63. Filing indicator CI (commercial insurance). Payer claim control 2625083393779, POS 11 (office), frequency 1 (original claim).
Payment: $74.56 by CHK (check), handling I.
production date (405): 2026-09-07.
Payer [PR]: GARDEN STATE BENEFIT TRUST; 210 RARITAN PLAZA; EDISON, NJ, 088373105; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820.
Trace (1 (current transaction trace)): EFT978523404, originator 1145082736.
claim statement period start (232): 2026-08-06.
Payee TJ (federal tax ID): 321822487.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97530-GP | 1 | $58.81 | $28.06 allowed (B6) $35.07 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $23.74; PR-2 (Patient Responsibility: coinsurance amount) $7.01 |  |
| 2 | 97110-GP | 1 | $48.53 | $23.25 allowed (B6) $29.06 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $19.47; PR-2 (Patient Responsibility: coinsurance amount) $5.81 |  |
| 3 | 97110-GP | 1 | $50.83 | $23.25 allowed (B6) $29.06 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $21.77; PR-2 (Patient Responsibility: coinsurance amount) $5.81 |  |

Line item control numbers (REF 6R): PA29382903L1, PA29382903L2, PA29382903L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: BARBARA LEE; MI (member ID) JYH092021893; rendering provider [82]: JOHN CLARK; XX (NPI) 1878226791.

## Claim as billed (837P)
Claim PA29382903, total charge $158.17, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M5450 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97530-GP | 1 UN | $58.81 | 2026-08-06 | 1 | PA29382903L1 |
| 2 | 97110-GP | 1 UN | $48.53 | 2026-08-06 | 1 | PA29382903L2 |
| 3 | 97110-GP | 1 UN | $50.83 | 2026-08-06 | 1 | PA29382903L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: GARDEN STATE BENEFIT TRUST; 46 (ETIN) 1450827364
- billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820; EI (employer ID/EIN) 321822487
- insured/subscriber [IL]: BARBARA LEE; MI (member ID) JYH092021893; 7392 CHESTNUT RD; PHILADELPHIA, PA, 19114
- payer [PR]: GARDEN STATE BENEFIT TRUST; PI (payer ID) 1450827364
- referring provider [DN]: SARAH CHEN; XX (NPI) 1410042904
- rendering provider [82]: JOHN CLARK; XX (NPI) 1878226791
- Submission reference TRC99422071, dated 2026-08-23 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-08-06.
Inquiry parties: payer [PR]: GARDEN STATE BENEFIT TRUST; PI (payer ID) 1450827364; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: BARBARA LEE; MI (member ID) JYH092021893.
Subject DOB 1982-03-23, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: GARDEN STATE BENEFIT TRUST PPO
- plan date (291): 2026-08-06
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: GARDEN STATE BENEFIT TRUST; PI (payer ID) 1450827364; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: BARBARA LEE; MI (member ID) JYH092021893.
Subject DOB 1982-03-23, sex F.
Eligibility exchange reference ELG75390986, dated 2026-09-10 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-08-24, action code WQ, amount $158.17.
D9 (clearinghouse claim number): TRC99422071.
Trace (2 (referenced transaction trace)): TRC99422071.
received date (050): 2026-08-24.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; patient [QC]: BARBARA LEE; MI (member ID) JYH092021893.
Acknowledgment reference ACK99422071, dated 2026-08-24 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-08-06. Dx: Low back pain unspecified. 97530 (15 min): therapeutic activities (dynamic functional tasks). 97110 (15 min): therapeutic exercise for strength and ROM. 97110 (16 min): therapeutic exercise for strength and ROM. Total timed minutes: 46. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1353206904 to receiver [ZZ] 1450827364, interchange 999329469 date 260910 time 0800 version 00501 usage P; group HS control 999329469 date 20260910 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1450827364 to receiver [ZZ] 1353206904, interchange 288429890 date 260910 time 0800 version 00501 usage P; group HB control 288429890 date 20260910 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 321822487 to receiver [ZZ] 1450827364, interchange 531632189 date 260823 time 0800 version 00501 usage P; group HC control 531632189 date 20260823 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 321822487, interchange 146508881 date 260824 time 0800 version 00501 usage P; group HN control 146508881 date 20260824 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1450827364 to receiver [ZZ] 1353206904, interchange 978523404 date 260907 time 0800 version 00501 usage P; group HP control 978523404 date 20260907 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 36
