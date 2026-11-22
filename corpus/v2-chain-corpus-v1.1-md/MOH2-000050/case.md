# Case MOH2-000050

Patient GEORGE WILSON, DOB 1943-10-25, sex M, member ID 4Y63PU1WC13. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-01-21.

## Adjudication outcome (835)
Claim PA27401321: status 4 (denied). Billed $243.39, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2604514891085, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-02-14.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT197452251, originator 1184634935.
claim statement period start (232): 2026-01-21.
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110 | 2 | $100.1 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $100.1 | HE N822 (missing procedure modifier(s)) |
| 2 | 97140 | 2 | $90.16 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $90.16 | HE N822 (missing procedure modifier(s)) |
| 3 | 97530 | 1 | $53.13 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $53.13 | HE N822 (missing procedure modifier(s)) |

Line item control numbers (REF 6R): PA27401321L1, PA27401321L2, PA27401321L3.
Remit claim parties: patient [QC]: GEORGE WILSON; MI (member ID) 4Y63PU1WC13; rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142.

## Claim as billed (837P)
Claim PA27401321, total charge $243.39, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M48061 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110 | 2 UN | $100.1 | 2026-01-21 | 1 | PA27401321L1 |
| 2 | 97140 | 2 UN | $90.16 | 2026-01-21 | 1 | PA27401321L2 |
| 3 | 97530 | 1 UN | $53.13 | 2026-01-21 | 1 | PA27401321L3 |

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: GEORGE WILSON; MI (member ID) 4Y63PU1WC13; 8660 WILLOW ST; PHILADELPHIA, PA, 19133
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: THOMAS BERGSTROM; XX (NPI) 1179655839
- rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142
- Submission reference TRC64409756, dated 2026-01-31 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-01-21.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: GEORGE WILSON; MI (member ID) 4Y63PU1WC13.
Subject DOB 1943-10-25, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-01-21
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: GEORGE WILSON; MI (member ID) 4Y63PU1WC13.
Subject DOB 1943-10-25, sex M.
Eligibility exchange reference ELG63386278, dated 2026-02-16 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-01-31, action code WQ, amount $243.39.
D9 (clearinghouse claim number): TRC64409756.
Trace (2 (referenced transaction trace)): TRC64409756.
received date (050): 2026-01-31.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: GEORGE WILSON; MI (member ID) 4Y63PU1WC13.
Acknowledgment reference ACK64409756, dated 2026-01-31 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-01-21. Dx: Spinal stenosis lumbar region without neurogenic claudication. 97110 (31 min): therapeutic exercise for strength and ROM. 97140 (31 min): manual therapy (soft tissue and joint mobilization). 97530 (14 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 76. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1846349352, interchange 166415190 date 260216 time 0800 version 00501 usage P; group HS control 166415190 date 20260216 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1801579548, interchange 125153298 date 260216 time 0800 version 00501 usage P; group HB control 125153298 date 20260216 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1846349352, interchange 379544248 date 260131 time 0800 version 00501 usage P; group HC control 379544248 date 20260131 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 791221822 date 260131 time 0800 version 00501 usage P; group HN control 791221822 date 20260131 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1801579548, interchange 197452251 date 260214 time 0800 version 00501 usage P; group HP control 197452251 date 20260214 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 33
