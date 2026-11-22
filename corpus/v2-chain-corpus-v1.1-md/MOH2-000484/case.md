# Case MOH2-000484

Patient GEORGE WILSON, DOB 1943-10-25, sex M, member ID TMM680692773. Payer: GARDEN STATE BENEFIT TRUST. Service date 2026-02-03.

## Adjudication outcome (835)
Claim PA24904247: status 4 (denied). Billed $150.9, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2606273807016, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-03-03.
Payer [PR]: GARDEN STATE BENEFIT TRUST; 210 RARITAN PLAZA; EDISON, NJ, 088373105; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT567206796, originator 1145082736.
claim statement period start (232): 2026-02-03.
Outpatient adjudication remarks (MOA): MA04 (secondary payment cannot be considered without primary payer identity).
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $43.27 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $43.27 |  |
| 2 | 97140-GP | 1 | $46.38 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $46.38 |  |
| 3 | 97530-GP | 1 | $61.25 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $61.25 |  |

Line item control numbers (REF 6R): PA24904247L1, PA24904247L2, PA24904247L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: GEORGE WILSON; MI (member ID) TMM680692773; rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142.

## Claim as billed (837P)
Claim PA24904247, total charge $150.9, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M48061 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $43.27 | 2026-02-03 | 1 | PA24904247L1 |
| 2 | 97140-GP | 1 UN | $46.38 | 2026-02-03 | 1 | PA24904247L2 |
| 3 | 97530-GP | 1 UN | $61.25 | 2026-02-03 | 1 | PA24904247L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: GARDEN STATE BENEFIT TRUST; 46 (ETIN) 1450827364
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: GEORGE WILSON; MI (member ID) TMM680692773; 8660 WILLOW ST; PHILADELPHIA, PA, 19133
- payer [PR]: GARDEN STATE BENEFIT TRUST; PI (payer ID) 1450827364
- referring provider [DN]: THOMAS BERGSTROM; XX (NPI) 1179655839
- rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142
- Submission reference TRC63534149, dated 2026-02-16 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-02-03.
Inquiry parties: payer [PR]: GARDEN STATE BENEFIT TRUST; PI (payer ID) 1450827364; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: GEORGE WILSON; MI (member ID) TMM680692773.
Subject DOB 1943-10-25, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: GARDEN STATE BENEFIT TRUST HMO
- benefit: R (other or additional payer), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-02-03
- eligibility begin (356): 2024-01-01
- eligibility begin (356): 2024-01-01
- payer message: PLAN IS PRIMARY PAYER FOR THIS MEMBER
Response parties: payer [PR]: GARDEN STATE BENEFIT TRUST; PI (payer ID) 1450827364; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: GEORGE WILSON; MI (member ID) TMM680692773; payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352.
Subject DOB 1943-10-25, sex M.
Eligibility exchange reference ELG63645526, dated 2026-03-10 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-02-18, action code WQ, amount $150.9.
D9 (clearinghouse claim number): TRC63534149.
Trace (2 (referenced transaction trace)): TRC63534149.
received date (050): 2026-02-18.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: GEORGE WILSON; MI (member ID) TMM680692773.
Acknowledgment reference ACK63534149, dated 2026-02-18 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-02-03. Dx: Spinal stenosis lumbar region without neurogenic claudication. 97110 (15 min): therapeutic exercise for strength and ROM. 97140 (14 min): manual therapy (soft tissue and joint mobilization). 97530 (16 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 45. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1450827364, interchange 438880491 date 260310 time 0800 version 00501 usage P; group HS control 438880491 date 20260310 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1450827364 to receiver [ZZ] 1801579548, interchange 619977943 date 260310 time 0800 version 00501 usage P; group HB control 619977943 date 20260310 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 17
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1450827364, interchange 426425544 date 260216 time 0800 version 00501 usage P; group HC control 426425544 date 20260216 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 228948027 date 260218 time 0800 version 00501 usage P; group HN control 228948027 date 20260218 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1450827364 to receiver [ZZ] 1801579548, interchange 567206796 date 260303 time 0800 version 00501 usage P; group HP control 567206796 date 20260303 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
