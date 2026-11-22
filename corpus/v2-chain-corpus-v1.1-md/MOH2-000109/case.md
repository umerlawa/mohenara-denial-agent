# Case MOH2-000109

Patient DAVID MARTIN, DOB 1953-06-16, sex F, member ID 7UE7JR2CE34. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-06-25.

## Adjudication outcome (835)
Claim PA25961494: status 1 (processed as primary, paid). Billed $78.97, paid $14.43, patient responsibility $3.61. Filing indicator MB (Medicare Part B). Payer claim control 2621813456406, POS 11 (office), frequency 1 (original claim).
Payment: $14.43 by CHK (check), handling I.
production date (405): 2026-08-06.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT503263942, originator 1184634935.
claim statement period start (232): 2026-06-25.
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $49.32 | $0 | CO-236 (Contractual Obligation: procedure/modifier combination not compatible per coding guidelines, bundled) $49.32 | HE N20 (service not payable with other service rendered on the same date) |
| 2 | 97150-GP | 1 | $29.65 | $14.43 allowed (B6) $18.04 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $11.61; PR-2 (Patient Responsibility: coinsurance amount) $3.61 |  |

Line item control numbers (REF 6R): PA25961494L1, PA25961494L2.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: DAVID MARTIN; MI (member ID) 7UE7JR2CE34; rendering provider [82]: JOSEPH ANDERSON; XX (NPI) 1260849754.

## Claim as billed (837P)
Claim PA25961494, total charge $78.97, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M1712 (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $49.32 | 2026-06-25 | 1 | PA25961494L1 |
| 2 | 97150-GP | 1 UN | $29.65 | 2026-06-25 | 1 | PA25961494L2 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: DAVID MARTIN; MI (member ID) 7UE7JR2CE34; 4138 MAPLE AVE; WILMINGTON, DE, 19809
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: ELENA VASQUEZ; XX (NPI) 1863431679
- rendering provider [82]: JOSEPH ANDERSON; XX (NPI) 1260849754
- Submission reference TRC14523887, dated 2026-07-07 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-06-25.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: DAVID MARTIN; MI (member ID) 7UE7JR2CE34.
Subject DOB 1953-06-16, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-06-25
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: DAVID MARTIN; MI (member ID) 7UE7JR2CE34.
Subject DOB 1953-06-16, sex F.
Eligibility exchange reference ELG60789967, dated 2026-08-08 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-07-09, action code WQ, amount $78.97.
D9 (clearinghouse claim number): TRC14523887.
Trace (2 (referenced transaction trace)): TRC14523887.
received date (050): 2026-07-09.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: DAVID MARTIN; MI (member ID) 7UE7JR2CE34.
Acknowledgment reference ACK14523887, dated 2026-07-09 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-06-25. Dx: Unilateral primary osteoarthritis left knee. 97110 (16 min): therapeutic exercise for strength and ROM. 97150 (untimed, 1 unit): group therapeutic procedure. Total timed minutes: 16. 97110 was performed in a separate 15-minute session from 97150, directed at a distinct body region with a distinct goal; services were not integral to one another. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1846349352, interchange 974245179 date 260808 time 0800 version 00501 usage P; group HS control 974245179 date 20260808 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 692082810 date 260808 time 0800 version 00501 usage P; group HB control 692082810 date 20260808 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1846349352, interchange 251968050 date 260707 time 0800 version 00501 usage P; group HC control 251968050 date 20260707 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 242874650 date 260709 time 0800 version 00501 usage P; group HN control 242874650 date 20260709 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 503263942 date 260806 time 0800 version 00501 usage P; group HP control 503263942 date 20260806 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 29
