# Case MOH2-000291

Patient MARY JOHNSON, DOB 1952-06-17, sex M, member ID 2G92AM5RW23. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-06-02.

## Adjudication outcome (835)
Claim PA29548083: status 1 (processed as primary, paid). Billed $254.28, paid $81.22, patient responsibility $20.31. Filing indicator MB (Medicare Part B). Payer claim control 2619006974251, POS 11 (office), frequency 1 (original claim).
Payment: $81.22 by CHK (check), handling I.
production date (405): 2026-07-09.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT238727901, originator 1184634935.
claim statement period start (232): 2026-06-02.
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP-KX | 1 | $48.43 | $0 | CO-236 (Contractual Obligation: procedure/modifier combination not compatible per coding guidelines, bundled) $48.43 | HE N20 (service not payable with other service rendered on the same date) |
| 2 | 97760-GP-KX | 1 | $67.36 | $36.87 allowed (B6) $46.09 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $21.27; PR-2 (Patient Responsibility: coinsurance amount) $9.22 |  |
| 3 | 97110-GP-KX | 1 | $38.73 | $0 | CO-236 (Contractual Obligation: procedure/modifier combination not compatible per coding guidelines, bundled) $38.73 | HE N20 (service not payable with other service rendered on the same date) |
| 4 | 97140-GP-59-KX | 2 | $99.76 | $44.35 allowed (B6) $55.44 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $44.32; PR-2 (Patient Responsibility: coinsurance amount) $11.09 |  |

Line item control numbers (REF 6R): PA29548083L1, PA29548083L2, PA29548083L3, PA29548083L4.
Modifiers on remit lines: 59 (distinct procedural service), GP (under PT plan of care), KX.
Remit claim parties: patient [QC]: MARY JOHNSON; MI (member ID) 2G92AM5RW23; rendering provider [82]: WEI LEWIS; XX (NPI) 1986021803.

## Claim as billed (837P)
Claim PA29548083, total charge $254.28, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: S93401D (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP-KX | 1 UN | $48.43 | 2026-06-02 | 1 | PA29548083L1 |
| 2 | 97760-GP-KX | 1 UN | $67.36 | 2026-06-02 | 1 | PA29548083L2 |
| 3 | 97110-GP-KX | 1 UN | $38.73 | 2026-06-02 | 1 | PA29548083L3 |
| 4 | 97140-GP-59-KX | 2 UN | $99.76 | 2026-06-02 | 1 | PA29548083L4 |

Modifiers on claim: 59 (distinct procedural service), GP (under PT plan of care), KX.

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: MARY JOHNSON; MI (member ID) 2G92AM5RW23; 9000 CHESTNUT AVE; TRENTON, NJ, 08641
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: GRETA LINDQVIST; XX (NPI) 1205658765
- rendering provider [82]: WEI LEWIS; XX (NPI) 1986021803
- Submission reference TRC53623212, dated 2026-06-05 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-06-02.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: MARY JOHNSON; MI (member ID) 2G92AM5RW23.
Subject DOB 1952-06-17, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-06-02
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: MARY JOHNSON; MI (member ID) 2G92AM5RW23.
Subject DOB 1952-06-17, sex M.
Eligibility exchange reference ELG75168088, dated 2026-07-15 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-06-07, action code WQ, amount $254.28.
D9 (clearinghouse claim number): TRC53623212.
Trace (2 (referenced transaction trace)): TRC53623212.
received date (050): 2026-06-07.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: MARY JOHNSON; MI (member ID) 2G92AM5RW23.
Acknowledgment reference ACK53623212, dated 2026-06-07 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-06-02. Dx: Sprain of unspecified ligament of right ankle subsequent encounter. 97110 (16 min): therapeutic exercise for strength and ROM. 97760 (16 min): orthotic management and training, initial encounter. 97110 (14 min): therapeutic exercise for strength and ROM. 97140 (31 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 77. 97110 was performed in a separate 15-minute session from 97760, directed at a distinct body region with a distinct goal; services were not integral to one another. 97140 was rendered as an independent service from 97760 — separate start/stop times were recorded and a different body region was treated. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1846349352, interchange 590968386 date 260715 time 0800 version 00501 usage P; group HS control 590968386 date 20260715 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 209784150 date 260715 time 0800 version 00501 usage P; group HB control 209784150 date 20260715 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1846349352, interchange 128883655 date 260605 time 0800 version 00501 usage P; group HC control 128883655 date 20260605 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 38
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 255562914 date 260607 time 0800 version 00501 usage P; group HN control 255562914 date 20260607 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 238727901 date 260709 time 0800 version 00501 usage P; group HP control 238727901 date 20260709 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 40
