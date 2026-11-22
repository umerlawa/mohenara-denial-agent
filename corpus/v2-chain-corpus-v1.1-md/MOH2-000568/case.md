# Case MOH2-000568

Patient ELIZABETH WILSON, DOB 1951-03-02, sex F, member ID 4EP8T60UC91. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-01-12.

## Adjudication outcome (835)
Claim PA29179078: status 4 (denied). Billed $187.69, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2605632180847, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-02-25.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT952744388, originator 1184634935.
claim statement period start (232): 2026-01-12.
Outpatient adjudication remarks (MOA): N286 (missing/incomplete/invalid referring provider primary identifier).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $42.56 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $42.56 |  |
| 2 | 97140-GP | 2 | $92.17 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $92.17 |  |
| 3 | 97530-GP | 1 | $52.96 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $52.96 |  |

Line item control numbers (REF 6R): PA29179078L1, PA29179078L2, PA29179078L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: ELIZABETH WILSON; MI (member ID) 4EP8T60UC91; rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737.

## Claim as billed (837P)
Claim PA29179078, total charge $187.69, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25512 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $42.56 | 2026-01-12 | 1 | PA29179078L1 |
| 2 | 97140-GP | 2 UN | $92.17 | 2026-01-12 | 1 | PA29179078L2 |
| 3 | 97530-GP | 1 UN | $52.96 | 2026-01-12 | 1 | PA29179078L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: ELIZABETH WILSON; MI (member ID) 4EP8T60UC91; 8206 CHESTNUT ST; TRENTON, NJ, 08638
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737
- Submission reference TRC30747566, dated 2026-01-31 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-01-12.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: ELIZABETH WILSON; MI (member ID) 4EP8T60UC91.
Subject DOB 1951-03-02, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-01-12
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: ELIZABETH WILSON; MI (member ID) 4EP8T60UC91.
Subject DOB 1951-03-02, sex F.
Eligibility exchange reference ELG61975290, dated 2026-02-27 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-02-01, action code WQ, amount $187.69.
D9 (clearinghouse claim number): TRC30747566.
Trace (2 (referenced transaction trace)): TRC30747566.
received date (050): 2026-02-01.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: ELIZABETH WILSON; MI (member ID) 4EP8T60UC91.
Acknowledgment reference ACK30747566, dated 2026-02-01 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-01-12. Dx: Pain in left shoulder. 97110 (14 min): therapeutic exercise for strength and ROM. 97140 (30 min): manual therapy (soft tissue and joint mobilization). 97530 (15 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 59. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1846349352, interchange 425017585 date 260227 time 0800 version 00501 usage P; group HS control 425017585 date 20260227 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 362775787 date 260227 time 0800 version 00501 usage P; group HB control 362775787 date 20260227 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1846349352, interchange 556330227 date 260131 time 0800 version 00501 usage P; group HC control 556330227 date 20260131 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 33
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 604070364 date 260201 time 0800 version 00501 usage P; group HN control 604070364 date 20260201 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 952744388 date 260225 time 0800 version 00501 usage P; group HP control 952744388 date 20260225 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
