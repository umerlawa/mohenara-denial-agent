# Case MOH2-000007

Patient MARIA RODRIGUEZ, DOB 1955-10-10, sex M, member ID BDS257046369. Payer: GARDEN STATE BENEFIT TRUST. Service date 2026-02-22.

## Adjudication outcome (835)
Claim PA27666512: status 4 (denied). Billed $240.04, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2609154073637, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-04-01.
Payer [PR]: GARDEN STATE BENEFIT TRUST; 210 RARITAN PLAZA; EDISON, NJ, 088373105; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820.
Trace (1 (current transaction trace)): EFT224948352, originator 1145082736.
claim statement period start (232): 2026-02-22.
Outpatient adjudication remarks (MOA): MA04 (secondary payment cannot be considered without primary payer identity).
Payee TJ (federal tax ID): 321822487.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 | $86.07 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $86.07 |  |
| 2 | 97140-GP | 1 | $43.36 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $43.36 |  |
| 3 | 97530-GP | 1 | $62.19 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $62.19 |  |
| 4 | 97112-GP | 1 | $48.42 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $48.42 |  |

Line item control numbers (REF 6R): PA27666512L1, PA27666512L2, PA27666512L3, PA27666512L4.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: MARIA RODRIGUEZ; MI (member ID) BDS257046369; rendering provider [82]: JOHN CLARK; XX (NPI) 1878226791.

## Claim as billed (837P)
Claim PA27666512, total charge $240.04, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 UN | $86.07 | 2026-02-22 | 1 | PA27666512L1 |
| 2 | 97140-GP | 1 UN | $43.36 | 2026-02-22 | 1 | PA27666512L2 |
| 3 | 97530-GP | 1 UN | $62.19 | 2026-02-22 | 1 | PA27666512L3 |
| 4 | 97112-GP | 1 UN | $48.42 | 2026-02-22 | 1 | PA27666512L4 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: GARDEN STATE BENEFIT TRUST; 46 (ETIN) 1450827364
- billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820; EI (employer ID/EIN) 321822487
- insured/subscriber [IL]: MARIA RODRIGUEZ; MI (member ID) BDS257046369; 2473 WILLOW ST; TRENTON, NJ, 08690
- payer [PR]: GARDEN STATE BENEFIT TRUST; PI (payer ID) 1450827364
- referring provider [DN]: AISHA RAHMAN; XX (NPI) 1538183382
- rendering provider [82]: JOHN CLARK; XX (NPI) 1878226791
- Submission reference TRC57882754, dated 2026-03-06 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-02-22.
Inquiry parties: payer [PR]: GARDEN STATE BENEFIT TRUST; PI (payer ID) 1450827364; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: MARIA RODRIGUEZ; MI (member ID) BDS257046369.
Subject DOB 1955-10-10, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: GARDEN STATE BENEFIT TRUST EPO
- benefit: R (other or additional payer), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-02-22
- eligibility begin (356): 2024-01-01
- eligibility begin (356): 2024-01-01
- payer message: PLAN IS PRIMARY PAYER FOR THIS MEMBER
Response parties: payer [PR]: GARDEN STATE BENEFIT TRUST; PI (payer ID) 1450827364; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: MARIA RODRIGUEZ; MI (member ID) BDS257046369; payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352.
Subject DOB 1955-10-10, sex M.
Eligibility exchange reference ELG71592703, dated 2026-04-04 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-03-06, action code WQ, amount $240.04.
D9 (clearinghouse claim number): TRC57882754.
Trace (2 (referenced transaction trace)): TRC57882754.
received date (050): 2026-03-06.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; patient [QC]: MARIA RODRIGUEZ; MI (member ID) BDS257046369.
Acknowledgment reference ACK57882754, dated 2026-03-06 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-02-22. Dx: Aftercare following joint replacement surgery. 97110 (30 min): therapeutic exercise for strength and ROM. 97140 (16 min): manual therapy (soft tissue and joint mobilization). 97530 (14 min): therapeutic activities (dynamic functional tasks). 97112 (15 min): neuromuscular re-education of movement and balance. Total timed minutes: 75. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1353206904 to receiver [ZZ] 1450827364, interchange 420133344 date 260404 time 0800 version 00501 usage P; group HS control 420133344 date 20260404 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1450827364 to receiver [ZZ] 1353206904, interchange 995100902 date 260404 time 0800 version 00501 usage P; group HB control 995100902 date 20260404 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 17
- claim_837p: sender [ZZ] 321822487 to receiver [ZZ] 1450827364, interchange 184409156 date 260306 time 0800 version 00501 usage P; group HC control 184409156 date 20260306 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 38
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 321822487, interchange 815309518 date 260306 time 0800 version 00501 usage P; group HN control 815309518 date 20260306 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1450827364 to receiver [ZZ] 1353206904, interchange 224948352 date 260401 time 0800 version 00501 usage P; group HP control 224948352 date 20260401 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 35
