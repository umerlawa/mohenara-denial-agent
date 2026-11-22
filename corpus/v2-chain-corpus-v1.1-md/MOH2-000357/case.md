# Case MOH2-000357

Patient MICHAEL WHITE, DOB 1955-04-09, sex F, member ID 4EM6NG3EA62. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-06-19.

## Adjudication outcome (835)
Claim PA25570248: status 1 (processed as primary, paid). Billed $95.84, paid $49.43, patient responsibility $12.36. Filing indicator MB (Medicare Part B). Payer claim control 2621359037224, POS 11 (office), frequency 1 (original claim).
Payment: $49.43 by CHK (check), handling I.
production date (405): 2026-08-01.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT244403800, originator 1184634935.
claim statement period start (232): 2026-06-19.
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97116-GP-KX | 1 | $42.95 | $23.25 allowed (B6) $29.06 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $13.89; PR-2 (Patient Responsibility: coinsurance amount) $5.81 |  |
| 2 | 97112-GP-KX | 1 | $52.89 | $26.18 allowed (B6) $32.73 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $20.16; PR-2 (Patient Responsibility: coinsurance amount) $6.55 |  |

Line item control numbers (REF 6R): PA25570248L1, PA25570248L2.
Modifiers on remit lines: GP (under PT plan of care), KX.
Remit claim parties: patient [QC]: MICHAEL WHITE; MI (member ID) 4EM6NG3EA62; rendering provider [82]: DOROTHY LOPEZ; XX (NPI) 1390221007.

## Claim as billed (837P)
Claim PA25570248, total charge $95.84, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M1712 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97116-GP-KX | 1 UN | $42.95 | 2026-06-19 | 1 | PA25570248L1 |
| 2 | 97112-GP-KX | 1 UN | $52.89 | 2026-06-19 | 1 | PA25570248L2 |

Modifiers on claim: GP (under PT plan of care), KX.

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: MICHAEL WHITE; MI (member ID) 4EM6NG3EA62; 1069 LINCOLN LN; WILMINGTON, DE, 19855
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: GRETA LINDQVIST; XX (NPI) 1205658765
- rendering provider [82]: DOROTHY LOPEZ; XX (NPI) 1390221007
- Submission reference TRC42144133, dated 2026-06-24 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-06-19.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: MICHAEL WHITE; MI (member ID) 4EM6NG3EA62.
Subject DOB 1955-04-09, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-06-19
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: MICHAEL WHITE; MI (member ID) 4EM6NG3EA62.
Subject DOB 1955-04-09, sex F.
Eligibility exchange reference ELG86640866, dated 2026-08-07 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-06-26, action code WQ, amount $95.84.
D9 (clearinghouse claim number): TRC42144133.
Trace (2 (referenced transaction trace)): TRC42144133.
received date (050): 2026-06-26.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: MICHAEL WHITE; MI (member ID) 4EM6NG3EA62.
Acknowledgment reference ACK42144133, dated 2026-06-26 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-06-19. Dx: Unilateral primary osteoarthritis left knee. 97116 (15 min): gait training with assistive device progression. 97112 (15 min): neuromuscular re-education of movement and balance. Total timed minutes: 30. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1846349352, interchange 451571059 date 260807 time 0800 version 00501 usage P; group HS control 451571059 date 20260807 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1801579548, interchange 552049746 date 260807 time 0800 version 00501 usage P; group HB control 552049746 date 20260807 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1846349352, interchange 783696060 date 260624 time 0800 version 00501 usage P; group HC control 783696060 date 20260624 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 407327004 date 260626 time 0800 version 00501 usage P; group HN control 407327004 date 20260626 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1801579548, interchange 244403800 date 260801 time 0800 version 00501 usage P; group HP control 244403800 date 20260801 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 30
