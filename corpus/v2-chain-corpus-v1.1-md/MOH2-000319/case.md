# Case MOH2-000319

Patient RICHARD THOMAS, DOB 1951-02-01, sex M, member ID 4D85TG6JX14. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-06-09.

## Adjudication outcome (835)
Claim PA22053120: status 4 (denied). Billed $212.1, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2621479147662, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-08-02.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT830905386, originator 1184634935.
claim statement period start (232): 2026-06-09.
Outpatient adjudication remarks (MOA): N435 (exceeds number/frequency approved or allowed within time period).
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97530-GP | 2 | $118.07 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $118.07 |  |
| 2 | 97112-GP | 1 | $50.74 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $50.74 |  |
| 3 | 97140-GP | 1 | $43.29 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $43.29 |  |

Line item control numbers (REF 6R): PA22053120L1, PA22053120L2, PA22053120L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: RICHARD THOMAS; MI (member ID) 4D85TG6JX14; rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142.

## Claim as billed (837P)
Claim PA22053120, total charge $212.1, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M48061 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97530-GP | 2 UN | $118.07 | 2026-06-09 | 1 | PA22053120L1 |
| 2 | 97112-GP | 1 UN | $50.74 | 2026-06-09 | 1 | PA22053120L2 |
| 3 | 97140-GP | 1 UN | $43.29 | 2026-06-09 | 1 | PA22053120L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: RICHARD THOMAS; MI (member ID) 4D85TG6JX14; 3186 MAPLE LN; PHILADELPHIA, PA, 19147
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: DAVID GOLDSTEIN; XX (NPI) 1996029234
- rendering provider [82]: RICHARD THOMAS; XX (NPI) 1580714142
- Submission reference TRC13173723, dated 2026-06-29 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-06-09.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: RICHARD THOMAS; MI (member ID) 4D85TG6JX14.
Subject DOB 1951-02-01, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-06-09
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: RICHARD THOMAS; MI (member ID) 4D85TG6JX14.
Subject DOB 1951-02-01, sex M.
Eligibility exchange reference ELG89458334, dated 2026-08-03 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-06-30, action code WQ, amount $212.1.
D9 (clearinghouse claim number): TRC13173723.
Trace (2 (referenced transaction trace)): TRC13173723.
received date (050): 2026-06-30.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: RICHARD THOMAS; MI (member ID) 4D85TG6JX14.
Acknowledgment reference ACK13173723, dated 2026-06-30 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-06-09. Dx: Spinal stenosis lumbar region without neurogenic claudication. 97530 (29 min): therapeutic activities (dynamic functional tasks). 97112 (15 min): neuromuscular re-education of movement and balance. 97140 (14 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 58. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1846349352, interchange 344300239 date 260803 time 0800 version 00501 usage P; group HS control 344300239 date 20260803 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1801579548, interchange 501690783 date 260803 time 0800 version 00501 usage P; group HB control 501690783 date 20260803 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1846349352, interchange 980157875 date 260629 time 0800 version 00501 usage P; group HC control 980157875 date 20260629 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 214661541 date 260630 time 0800 version 00501 usage P; group HN control 214661541 date 20260630 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1801579548, interchange 830905386 date 260802 time 0800 version 00501 usage P; group HP control 830905386 date 20260802 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
