# Case MOH2-000141

Patient PATRICIA ROBINSON, DOB 1945-07-02, sex F, member ID 4CG5NV6EQ35. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-06-05.

## Adjudication outcome (835)
Claim PA23348661: status 1 (processed as primary, paid). Billed $113.05, paid $28.06, patient responsibility $7.01. Filing indicator MB (Medicare Part B). Payer claim control 2618948087851, POS 11 (office), frequency 1 (original claim).
Payment: $28.06 by CHK (check), handling I.
production date (405): 2026-07-08.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT468816067, originator 1184634935.
claim statement period start (232): 2026-06-05.
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97750-GP-KX | 1 | $60.62 | $0 | CO-236 (Contractual Obligation: procedure/modifier combination not compatible per coding guidelines, bundled) $60.62 | HE N20 (service not payable with other service rendered on the same date) |
| 2 | 97530-GP-KX | 1 | $52.43 | $28.06 allowed (B6) $35.07 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $17.36; PR-2 (Patient Responsibility: coinsurance amount) $7.01 |  |

Line item control numbers (REF 6R): PA23348661L1, PA23348661L2.
Modifiers on remit lines: GP (under PT plan of care), KX.
Remit claim parties: patient [QC]: PATRICIA ROBINSON; MI (member ID) 4CG5NV6EQ35; rendering provider [82]: WEI LEWIS; XX (NPI) 1986021803.

## Claim as billed (837P)
Claim PA23348661, total charge $113.05, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M1712 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97750-GP-KX | 1 UN | $60.62 | 2026-06-05 | 1 | PA23348661L1 |
| 2 | 97530-GP-KX | 1 UN | $52.43 | 2026-06-05 | 1 | PA23348661L2 |

Modifiers on claim: GP (under PT plan of care), KX.

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: PATRICIA ROBINSON; MI (member ID) 4CG5NV6EQ35; 1399 LINCOLN RD; WILMINGTON, DE, 19862
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: MARCUS WEBB; XX (NPI) 1583494452
- rendering provider [82]: WEI LEWIS; XX (NPI) 1986021803
- Submission reference TRC80381841, dated 2026-06-10 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-06-05.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: PATRICIA ROBINSON; MI (member ID) 4CG5NV6EQ35.
Subject DOB 1945-07-02, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-06-05
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: PATRICIA ROBINSON; MI (member ID) 4CG5NV6EQ35.
Subject DOB 1945-07-02, sex F.
Eligibility exchange reference ELG84177111, dated 2026-07-11 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-06-11, action code WQ, amount $113.05.
D9 (clearinghouse claim number): TRC80381841.
Trace (2 (referenced transaction trace)): TRC80381841.
received date (050): 2026-06-11.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: PATRICIA ROBINSON; MI (member ID) 4CG5NV6EQ35.
Acknowledgment reference ACK80381841, dated 2026-06-11 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-06-05. Dx: Unilateral primary osteoarthritis left knee. 97750 (15 min): physical performance test with written report. 97530 (14 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 29. 97750 was rendered as an independent service from 97530 — separate start/stop times were recorded and a different body region was treated. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1846349352, interchange 976424636 date 260711 time 0800 version 00501 usage P; group HS control 976424636 date 20260711 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 353338768 date 260711 time 0800 version 00501 usage P; group HB control 353338768 date 20260711 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1846349352, interchange 996283758 date 260610 time 0800 version 00501 usage P; group HC control 996283758 date 20260610 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 942213144 date 260611 time 0800 version 00501 usage P; group HN control 942213144 date 20260611 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 468816067 date 260708 time 0800 version 00501 usage P; group HP control 468816067 date 20260708 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 29
