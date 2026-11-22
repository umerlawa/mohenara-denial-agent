# Case MOH2-000430

Patient BARBARA LEE, DOB 1982-03-23, sex F, member ID JYH092021893. Payer: GARDEN STATE BENEFIT TRUST. Service date 2026-08-16.

## Adjudication outcome (835)
Claim PA25893537: status 1 (processed as primary, paid). Billed $136.69, paid $72.42, patient responsibility $18.09. Filing indicator CI (commercial insurance). Payer claim control 2626717370400, POS 11 (office), frequency 1 (original claim).
Payment: $72.42 by CHK (check), handling I.
production date (405): 2026-09-24.
Payer [PR]: GARDEN STATE BENEFIT TRUST; 210 RARITAN PLAZA; EDISON, NJ, 088373105; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820.
Trace (1 (current transaction trace)): EFT962204212, originator 1145082736.
claim statement period start (232): 2026-08-16.
Payee TJ (federal tax ID): 321822487.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97530-GP | 1 | $46.23 | $28.06 allowed (B6) $35.07 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $11.16; PR-2 (Patient Responsibility: coinsurance amount) $7.01 |  |
| 2 | 97140-GP | 1 | $45.43 | $22.18 allowed (B6) $27.72 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $17.71; PR-2 (Patient Responsibility: coinsurance amount) $5.54 |  |
| 3 | 97140-GP | 1 | $45.03 | $22.18 allowed (B6) $27.72 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $17.31; PR-2 (Patient Responsibility: coinsurance amount) $5.54 |  |

Line item control numbers (REF 6R): PA25893537L1, PA25893537L2, PA25893537L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: BARBARA LEE; MI (member ID) JYH092021893; rendering provider [82]: JOHN CLARK; XX (NPI) 1878226791.

## Claim as billed (837P)
Claim PA25893537, total charge $136.69, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M5450 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97530-GP | 1 UN | $46.23 | 2026-08-16 | 1 | PA25893537L1 |
| 2 | 97140-GP | 1 UN | $45.43 | 2026-08-16 | 1 | PA25893537L2 |
| 3 | 97140-GP | 1 UN | $45.03 | 2026-08-16 | 1 | PA25893537L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: GARDEN STATE BENEFIT TRUST; 46 (ETIN) 1450827364
- billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820; EI (employer ID/EIN) 321822487
- insured/subscriber [IL]: BARBARA LEE; MI (member ID) JYH092021893; 7392 CHESTNUT RD; PHILADELPHIA, PA, 19114
- payer [PR]: GARDEN STATE BENEFIT TRUST; PI (payer ID) 1450827364
- referring provider [DN]: SARAH CHEN; XX (NPI) 1410042904
- rendering provider [82]: JOHN CLARK; XX (NPI) 1878226791
- Submission reference TRC88776240, dated 2026-08-30 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-08-16.
Inquiry parties: payer [PR]: GARDEN STATE BENEFIT TRUST; PI (payer ID) 1450827364; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: BARBARA LEE; MI (member ID) JYH092021893.
Subject DOB 1982-03-23, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: GARDEN STATE BENEFIT TRUST PPO
- plan date (291): 2026-08-16
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: GARDEN STATE BENEFIT TRUST; PI (payer ID) 1450827364; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: BARBARA LEE; MI (member ID) JYH092021893.
Subject DOB 1982-03-23, sex F.
Eligibility exchange reference ELG36872208, dated 2026-09-28 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-08-31, action code WQ, amount $136.69.
D9 (clearinghouse claim number): TRC88776240.
Trace (2 (referenced transaction trace)): TRC88776240.
received date (050): 2026-08-31.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; patient [QC]: BARBARA LEE; MI (member ID) JYH092021893.
Acknowledgment reference ACK88776240, dated 2026-08-31 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-08-16. Dx: Low back pain unspecified. 97530 (16 min): therapeutic activities (dynamic functional tasks). 97140 (15 min): manual therapy (soft tissue and joint mobilization). 97140 (14 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 45. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1353206904 to receiver [ZZ] 1450827364, interchange 355677966 date 260928 time 0800 version 00501 usage P; group HS control 355677966 date 20260928 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1450827364 to receiver [ZZ] 1353206904, interchange 622815930 date 260928 time 0800 version 00501 usage P; group HB control 622815930 date 20260928 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 321822487 to receiver [ZZ] 1450827364, interchange 490516551 date 260830 time 0800 version 00501 usage P; group HC control 490516551 date 20260830 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 321822487, interchange 964582310 date 260831 time 0800 version 00501 usage P; group HN control 964582310 date 20260831 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1450827364 to receiver [ZZ] 1353206904, interchange 962204212 date 260924 time 0800 version 00501 usage P; group HP control 962204212 date 20260924 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 36
