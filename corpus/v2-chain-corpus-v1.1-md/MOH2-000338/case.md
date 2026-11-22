# Case MOH2-000338

Patient ELIZABETH MARTINEZ, DOB 1981-05-11, sex M, member ID EUG481148600. Payer: GARDEN STATE BENEFIT TRUST. Service date 2025-01-25.

## Adjudication outcome (835)
Claim PA24217192: status 4 (denied). Billed $220.65, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2525334545635, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2025-09-10.
Payer [PR]: GARDEN STATE BENEFIT TRUST; 210 RARITAN PLAZA; EDISON, NJ, 088373105; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820.
Trace (1 (current transaction trace)): EFT252879642, originator 1145082736.
claim statement period start (232): 2025-01-25.
Outpatient adjudication remarks (MOA): N211 (you may not appeal this decision).
Payee TJ (federal tax ID): 321822487.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 | $83.95 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $83.95 |  |
| 2 | 97140-GP | 1 | $41.35 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $41.35 |  |
| 3 | 97530-GP | 2 | $95.35 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $95.35 |  |

Line item control numbers (REF 6R): PA24217192L1, PA24217192L2, PA24217192L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: ELIZABETH MARTINEZ; MI (member ID) EUG481148600; rendering provider [82]: MICHAEL MARTINEZ; XX (NPI) 1850202042.

## Claim as billed (837P)
Claim PA24217192, total charge $220.65, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25511 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 UN | $83.95 | 2025-01-25 | 1 | PA24217192L1 |
| 2 | 97140-GP | 1 UN | $41.35 | 2025-01-25 | 1 | PA24217192L2 |
| 3 | 97530-GP | 2 UN | $95.35 | 2025-01-25 | 1 | PA24217192L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: GARDEN STATE BENEFIT TRUST; 46 (ETIN) 1450827364
- billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820; EI (employer ID/EIN) 321822487
- insured/subscriber [IL]: ELIZABETH MARTINEZ; MI (member ID) EUG481148600; 7589 MAPLE ST; TRENTON, NJ, 08604
- payer [PR]: GARDEN STATE BENEFIT TRUST; PI (payer ID) 1450827364
- referring provider [DN]: OMAR DELGADO; XX (NPI) 1094074058
- rendering provider [82]: MICHAEL MARTINEZ; XX (NPI) 1850202042
- Submission reference TRC95085471, dated 2025-08-19 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2025-01-25.
Inquiry parties: payer [PR]: GARDEN STATE BENEFIT TRUST; PI (payer ID) 1450827364; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: ELIZABETH MARTINEZ; MI (member ID) EUG481148600.
Subject DOB 1981-05-11, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: GARDEN STATE BENEFIT TRUST HMO
- plan date (291): 2025-01-25
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: GARDEN STATE BENEFIT TRUST; PI (payer ID) 1450827364; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: ELIZABETH MARTINEZ; MI (member ID) EUG481148600.
Subject DOB 1981-05-11, sex M.
Eligibility exchange reference ELG81047777, dated 2025-09-11 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2025-02-06, action code WQ, amount $220.65.
D9 (clearinghouse claim number): TRC95085471.
Trace (2 (referenced transaction trace)): TRC95085471.
received date (050): 2025-02-06.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; patient [QC]: ELIZABETH MARTINEZ; MI (member ID) EUG481148600.
Acknowledgment reference ACK95085471, dated 2025-02-06 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2025-01-25. Dx: Pain in right shoulder. 97110 (31 min): therapeutic exercise for strength and ROM. 97140 (16 min): manual therapy (soft tissue and joint mobilization). 97530 (29 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 76. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1353206904 to receiver [ZZ] 1450827364, interchange 363215353 date 250911 time 0800 version 00501 usage P; group HS control 363215353 date 20250911 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1450827364 to receiver [ZZ] 1353206904, interchange 887551662 date 250911 time 0800 version 00501 usage P; group HB control 887551662 date 20250911 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 321822487 to receiver [ZZ] 1450827364, interchange 574304232 date 250819 time 0800 version 00501 usage P; group HC control 574304232 date 20250819 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 321822487, interchange 609638524 date 250206 time 0800 version 00501 usage P; group HN control 609638524 date 20250206 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1450827364 to receiver [ZZ] 1353206904, interchange 252879642 date 250910 time 0800 version 00501 usage P; group HP control 252879642 date 20250910 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
