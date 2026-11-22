# Case MOH2-000046

Patient JESSICA LEE, DOB 1947-12-16, sex M, member ID 7XC1QJ4QX54. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-06-27.

## Adjudication outcome (835)
Claim PA25733167: status 1 (processed as primary, paid). Billed $367.24, paid $23.25, patient responsibility $5.81. Filing indicator MB (Medicare Part B). Payer claim control 2622396119748, POS 11 (office), frequency 1 (original claim).
Payment: $23.25 by CHK (check), handling I.
production date (405): 2026-08-11.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820.
Trace (1 (current transaction trace)): EFT990316473, originator 1184634935.
claim statement period start (232): 2026-06-27.
Payee TJ (federal tax ID): 321822487.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $42.02 | $23.25 allowed (B6) $29.06 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $12.96; PR-2 (Patient Responsibility: coinsurance amount) $5.81 |  |
| 2 | 97140-GP | 7 | $325.22 | $0 | CO-151 (Contractual Obligation: information does not support this many/frequency of services) $325.22 | HE N362 (the number of days or units exceeds the acceptable maximum) |

Line item control numbers (REF 6R): PA25733167L1, PA25733167L2.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: JESSICA LEE; MI (member ID) 7XC1QJ4QX54; rendering provider [82]: MICHAEL MARTINEZ; XX (NPI) 1850202042.

## Claim as billed (837P)
Claim PA25733167, total charge $367.24, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $42.02 | 2026-06-27 | 1 | PA25733167L1 |
| 2 | 97140-GP | 7 UN | $325.22 | 2026-06-27 | 1 | PA25733167L2 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820; EI (employer ID/EIN) 321822487
- insured/subscriber [IL]: JESSICA LEE; MI (member ID) 7XC1QJ4QX54; 5399 MAPLE RD; PHILADELPHIA, PA, 19147
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: ROBERT KIMURA; XX (NPI) 1609960205
- rendering provider [82]: MICHAEL MARTINEZ; XX (NPI) 1850202042
- Submission reference TRC49521199, dated 2026-07-15 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-06-27.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: JESSICA LEE; MI (member ID) 7XC1QJ4QX54.
Subject DOB 1947-12-16, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-06-27
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: JESSICA LEE; MI (member ID) 7XC1QJ4QX54.
Subject DOB 1947-12-16, sex M.
Eligibility exchange reference ELG21003999, dated 2026-08-15 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-07-16, action code WQ, amount $367.24.
D9 (clearinghouse claim number): TRC49521199.
Trace (2 (referenced transaction trace)): TRC49521199.
received date (050): 2026-07-16.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; patient [QC]: JESSICA LEE; MI (member ID) 7XC1QJ4QX54.
Acknowledgment reference ACK49521199, dated 2026-07-16 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-06-27. Dx: Aftercare following joint replacement surgery. 97110 (14 min): therapeutic exercise for strength and ROM. 97140 (15 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 29. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1353206904 to receiver [ZZ] 1846349352, interchange 394737553 date 260815 time 0800 version 00501 usage P; group HS control 394737553 date 20260815 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1353206904, interchange 216338811 date 260815 time 0800 version 00501 usage P; group HB control 216338811 date 20260815 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 321822487 to receiver [ZZ] 1846349352, interchange 707824926 date 260715 time 0800 version 00501 usage P; group HC control 707824926 date 20260715 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 321822487, interchange 745143188 date 260716 time 0800 version 00501 usage P; group HN control 745143188 date 20260716 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1353206904, interchange 990316473 date 260811 time 0800 version 00501 usage P; group HP control 990316473 date 20260811 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 29
