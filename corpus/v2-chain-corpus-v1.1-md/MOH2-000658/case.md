# Case MOH2-000658

Patient FRANK JONES, DOB 1943-05-06, sex M, member ID 5YG0EQ3QU82. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-03-03.

## Adjudication outcome (835)
Claim PA23778771: status 4 (denied). Billed $188.41, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2609520225336, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-04-05.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT474887238, originator 1184634935.
claim statement period start (232): 2026-03-03.
Outpatient adjudication remarks (MOA): N286 (missing/incomplete/invalid referring provider primary identifier).
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $38.84 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $38.84 |  |
| 2 | 97112-GP | 1 | $51.96 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $51.96 |  |
| 3 | 97140-GP | 2 | $97.61 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $97.61 |  |

Line item control numbers (REF 6R): PA23778771L1, PA23778771L2, PA23778771L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: FRANK JONES; MI (member ID) 5YG0EQ3QU82; rendering provider [82]: DOROTHY LOPEZ; XX (NPI) 1390221007.

## Claim as billed (837P)
Claim PA23778771, total charge $188.41, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25511 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $38.84 | 2026-03-03 | 1 | PA23778771L1 |
| 2 | 97112-GP | 1 UN | $51.96 | 2026-03-03 | 1 | PA23778771L2 |
| 3 | 97140-GP | 2 UN | $97.61 | 2026-03-03 | 1 | PA23778771L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: FRANK JONES; MI (member ID) 5YG0EQ3QU82; 4526 FRANKLIN AVE; STATEN ISLAND, NY, 10370
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- rendering provider [82]: DOROTHY LOPEZ; XX (NPI) 1390221007
- Submission reference TRC76007668, dated 2026-03-10 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-03-03.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: FRANK JONES; MI (member ID) 5YG0EQ3QU82.
Subject DOB 1943-05-06, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-03-03
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: FRANK JONES; MI (member ID) 5YG0EQ3QU82.
Subject DOB 1943-05-06, sex M.
Eligibility exchange reference ELG13771453, dated 2026-04-07 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-03-11, action code WQ, amount $188.41.
D9 (clearinghouse claim number): TRC76007668.
Trace (2 (referenced transaction trace)): TRC76007668.
received date (050): 2026-03-11.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: FRANK JONES; MI (member ID) 5YG0EQ3QU82.
Acknowledgment reference ACK76007668, dated 2026-03-11 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-03-03. Dx: Pain in right shoulder. 97110 (15 min): therapeutic exercise for strength and ROM. 97112 (16 min): neuromuscular re-education of movement and balance. 97140 (29 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 60. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1846349352, interchange 611753948 date 260407 time 0800 version 00501 usage P; group HS control 611753948 date 20260407 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1801579548, interchange 239563942 date 260407 time 0800 version 00501 usage P; group HB control 239563942 date 20260407 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1846349352, interchange 409540274 date 260310 time 0800 version 00501 usage P; group HC control 409540274 date 20260310 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 33
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 170703694 date 260311 time 0800 version 00501 usage P; group HN control 170703694 date 20260311 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1801579548, interchange 474887238 date 260405 time 0800 version 00501 usage P; group HP control 474887238 date 20260405 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
