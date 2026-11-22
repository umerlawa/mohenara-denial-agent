# Case MOH2-000253

Patient GEORGE WILSON, DOB 1943-10-25, sex M, member ID 4Y63PU1WC13. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-01-27.

## Adjudication outcome (835)
Claim PA27215358: status 4 (denied). Billed $126.57, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2605807939578, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-02-27.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT293762270, originator 1184634935.
claim statement period start (232): 2026-01-27.
Outpatient adjudication remarks (MOA): N286 (missing/incomplete/invalid referring provider primary identifier).
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $38.8 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $38.8 |  |
| 2 | 97112-GP | 1 | $48.91 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $48.91 |  |
| 3 | 97140-GP | 1 | $38.86 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $38.86 |  |

Line item control numbers (REF 6R): PA27215358L1, PA27215358L2, PA27215358L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: GEORGE WILSON; MI (member ID) 4Y63PU1WC13; rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142.

## Claim as billed (837P)
Claim PA27215358, total charge $126.57, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M48061 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $38.8 | 2026-01-27 | 1 | PA27215358L1 |
| 2 | 97112-GP | 1 UN | $48.91 | 2026-01-27 | 1 | PA27215358L2 |
| 3 | 97140-GP | 1 UN | $38.86 | 2026-01-27 | 1 | PA27215358L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: GEORGE WILSON; MI (member ID) 4Y63PU1WC13; 8660 WILLOW ST; PHILADELPHIA, PA, 19133
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142
- Submission reference TRC42932728, dated 2026-02-02 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-01-27.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: GEORGE WILSON; MI (member ID) 4Y63PU1WC13.
Subject DOB 1943-10-25, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-01-27
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: GEORGE WILSON; MI (member ID) 4Y63PU1WC13.
Subject DOB 1943-10-25, sex M.
Eligibility exchange reference ELG38721186, dated 2026-03-05 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-02-03, action code WQ, amount $126.57.
D9 (clearinghouse claim number): TRC42932728.
Trace (2 (referenced transaction trace)): TRC42932728.
received date (050): 2026-02-03.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: GEORGE WILSON; MI (member ID) 4Y63PU1WC13.
Acknowledgment reference ACK42932728, dated 2026-02-03 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-01-27. Dx: Spinal stenosis lumbar region without neurogenic claudication. 97110 (16 min): therapeutic exercise for strength and ROM. 97112 (16 min): neuromuscular re-education of movement and balance. 97140 (15 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 47. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1846349352, interchange 567893873 date 260305 time 0800 version 00501 usage P; group HS control 567893873 date 20260305 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1801579548, interchange 373494612 date 260305 time 0800 version 00501 usage P; group HB control 373494612 date 20260305 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1846349352, interchange 754982939 date 260202 time 0800 version 00501 usage P; group HC control 754982939 date 20260202 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 33
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 379849888 date 260203 time 0800 version 00501 usage P; group HN control 379849888 date 20260203 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1801579548, interchange 293762270 date 260227 time 0800 version 00501 usage P; group HP control 293762270 date 20260227 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
