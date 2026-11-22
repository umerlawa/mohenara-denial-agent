# Case MOH2-000075

Patient JESSICA LEE, DOB 1947-12-16, sex M, member ID 7XC1QJ4QX54. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-07-18.

## Adjudication outcome (835)
Claim PA22458405: status 1 (processed as primary, paid). Billed $69.15, paid $14.43, patient responsibility $3.61. Filing indicator MB (Medicare Part B). Payer claim control 2623530508850, POS 11 (office), frequency 1 (original claim).
Payment: $14.43 by CHK (check), handling I.
production date (405): 2026-08-23.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820.
Trace (1 (current transaction trace)): EFT235990220, originator 1184634935.
claim statement period start (232): 2026-07-18.
Payee TJ (federal tax ID): 321822487.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97140-GP-KX | 1 | $38.51 | $0 | CO-236 (Contractual Obligation: procedure/modifier combination not compatible per coding guidelines, bundled) $38.51 | HE N20 (service not payable with other service rendered on the same date) |
| 2 | 97150-GP-KX | 1 | $30.64 | $14.43 allowed (B6) $18.04 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $12.6; PR-2 (Patient Responsibility: coinsurance amount) $3.61 |  |

Line item control numbers (REF 6R): PA22458405L1, PA22458405L2.
Modifiers on remit lines: GP (under PT plan of care), KX.
Remit claim parties: patient [QC]: JESSICA LEE; MI (member ID) 7XC1QJ4QX54; rendering provider [82]: MICHAEL MARTINEZ; XX (NPI) 1850202042.

## Claim as billed (837P)
Claim PA22458405, total charge $69.15, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97140-GP-KX | 1 UN | $38.51 | 2026-07-18 | 1 | PA22458405L1 |
| 2 | 97150-GP-KX | 1 UN | $30.64 | 2026-07-18 | 1 | PA22458405L2 |

Modifiers on claim: GP (under PT plan of care), KX.

Parties on claim:
- submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820; EI (employer ID/EIN) 321822487
- insured/subscriber [IL]: JESSICA LEE; MI (member ID) 7XC1QJ4QX54; 5399 MAPLE RD; PHILADELPHIA, PA, 19147
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: ROBERT KIMURA; XX (NPI) 1609960205
- rendering provider [82]: MICHAEL MARTINEZ; XX (NPI) 1850202042
- Submission reference TRC20371232, dated 2026-07-27 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-07-18.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: JESSICA LEE; MI (member ID) 7XC1QJ4QX54.
Subject DOB 1947-12-16, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-07-18
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: JESSICA LEE; MI (member ID) 7XC1QJ4QX54.
Subject DOB 1947-12-16, sex M.
Eligibility exchange reference ELG77937890, dated 2026-08-25 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-07-28, action code WQ, amount $69.15.
D9 (clearinghouse claim number): TRC20371232.
Trace (2 (referenced transaction trace)): TRC20371232.
received date (050): 2026-07-28.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; patient [QC]: JESSICA LEE; MI (member ID) 7XC1QJ4QX54.
Acknowledgment reference ACK20371232, dated 2026-07-28 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-07-18. Dx: Aftercare following joint replacement surgery. 97140 (16 min): manual therapy (soft tissue and joint mobilization). 97150 (untimed, 1 unit): group therapeutic procedure. Total timed minutes: 16. 97140 was performed in a separate 15-minute session from 97150, directed at a distinct body region with a distinct goal; services were not integral to one another. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1353206904 to receiver [ZZ] 1846349352, interchange 536599089 date 260825 time 0800 version 00501 usage P; group HS control 536599089 date 20260825 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1353206904, interchange 663097450 date 260825 time 0800 version 00501 usage P; group HB control 663097450 date 20260825 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 321822487 to receiver [ZZ] 1846349352, interchange 719332292 date 260727 time 0800 version 00501 usage P; group HC control 719332292 date 20260727 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 321822487, interchange 823633754 date 260728 time 0800 version 00501 usage P; group HN control 823633754 date 20260728 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1353206904, interchange 235990220 date 260823 time 0800 version 00501 usage P; group HP control 235990220 date 20260823 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 29
