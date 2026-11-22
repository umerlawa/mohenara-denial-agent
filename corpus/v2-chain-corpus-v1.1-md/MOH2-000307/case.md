# Case MOH2-000307

Patient FRANK JONES, DOB 1943-05-06, sex M, member ID 5YG0EQ3QU82. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-07-02.

## Adjudication outcome (835)
Claim PA22903615: status 1 (processed as primary, paid). Billed $133.58, paid $40.61, patient responsibility $10.16. Filing indicator MB (Medicare Part B). Payer claim control 2621843090784, POS 11 (office), frequency 1 (original claim).
Payment: $40.61 by CHK (check), handling I.
production date (405): 2026-08-06.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT293482547, originator 1184634935.
claim statement period start (232): 2026-07-02.
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97150-GP | 1 | $26.52 | $14.43 allowed (B6) $18.04 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $8.48; PR-2 (Patient Responsibility: coinsurance amount) $3.61 |  |
| 2 | 97112-GP-59 | 1 | $57.28 | $26.18 allowed (B6) $32.73 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $24.55; PR-2 (Patient Responsibility: coinsurance amount) $6.55 |  |
| 3 | 97110-GP | 1 | $49.78 | $0 | CO-236 (Contractual Obligation: procedure/modifier combination not compatible per coding guidelines, bundled) $49.78 | HE N20 (service not payable with other service rendered on the same date) |

Line item control numbers (REF 6R): PA22903615L1, PA22903615L2, PA22903615L3.
Modifiers on remit lines: 59 (distinct procedural service), GP (under PT plan of care).
Remit claim parties: patient [QC]: FRANK JONES; MI (member ID) 5YG0EQ3QU82; rendering provider [82]: DOROTHY LOPEZ; XX (NPI) 1390221007.

## Claim as billed (837P)
Claim PA22903615, total charge $133.58, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25511 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97150-GP | 1 UN | $26.52 | 2026-07-02 | 1 | PA22903615L1 |
| 2 | 97112-GP-59 | 1 UN | $57.28 | 2026-07-02 | 1 | PA22903615L2 |
| 3 | 97110-GP | 1 UN | $49.78 | 2026-07-02 | 1 | PA22903615L3 |

Modifiers on claim: 59 (distinct procedural service), GP (under PT plan of care).

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: FRANK JONES; MI (member ID) 5YG0EQ3QU82; 4526 FRANKLIN AVE; STATEN ISLAND, NY, 10370
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: ELENA VASQUEZ; XX (NPI) 1863431679
- rendering provider [82]: DOROTHY LOPEZ; XX (NPI) 1390221007
- Submission reference TRC23471359, dated 2026-07-08 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-07-02.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: FRANK JONES; MI (member ID) 5YG0EQ3QU82.
Subject DOB 1943-05-06, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-07-02
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: FRANK JONES; MI (member ID) 5YG0EQ3QU82.
Subject DOB 1943-05-06, sex M.
Eligibility exchange reference ELG56443530, dated 2026-08-07 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-07-10, action code WQ, amount $133.58.
D9 (clearinghouse claim number): TRC23471359.
Trace (2 (referenced transaction trace)): TRC23471359.
received date (050): 2026-07-10.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: FRANK JONES; MI (member ID) 5YG0EQ3QU82.
Acknowledgment reference ACK23471359, dated 2026-07-10 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-07-02. Dx: Pain in right shoulder. 97150 (untimed, 1 unit): group therapeutic procedure. 97112 (15 min): neuromuscular re-education of movement and balance. 97110 (16 min): therapeutic exercise for strength and ROM. Total timed minutes: 31. 97110 was performed in a separate 15-minute session from 97150, directed at a distinct body region with a distinct goal; services were not integral to one another. Documentation supports separate services: 97112 occupied a discrete timed interval apart from 97150 and addressed a different region and impairment. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1846349352, interchange 309364613 date 260807 time 0800 version 00501 usage P; group HS control 309364613 date 20260807 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1801579548, interchange 778207316 date 260807 time 0800 version 00501 usage P; group HB control 778207316 date 20260807 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1846349352, interchange 233365265 date 260708 time 0800 version 00501 usage P; group HC control 233365265 date 20260708 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 172973214 date 260710 time 0800 version 00501 usage P; group HN control 172973214 date 20260710 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1801579548, interchange 293482547 date 260806 time 0800 version 00501 usage P; group HP control 293482547 date 20260806 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 35
