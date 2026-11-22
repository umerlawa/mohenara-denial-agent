# Case MOH2-000600

Patient ELIZABETH WILSON, DOB 1951-03-02, sex F, member ID 4EP8T60UC91. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-05-19.

## Adjudication outcome (835)
Claim PA21183273: status 4 (denied). Billed $91.58, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2618087804994, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-06-29.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT371149738, originator 1184634935.
claim statement period start (232): 2026-05-19.
Outpatient adjudication remarks (MOA): N286 (missing/incomplete/invalid referring provider primary identifier).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97112-GP | 1 | $42.75 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $42.75 |  |
| 2 | 97110-GP | 1 | $48.83 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $48.83 |  |

Line item control numbers (REF 6R): PA21183273L1, PA21183273L2.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: ELIZABETH WILSON; MI (member ID) 4EP8T60UC91; rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737.

## Claim as billed (837P)
Claim PA21183273, total charge $91.58, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25512 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97112-GP | 1 UN | $42.75 | 2026-05-19 | 1 | PA21183273L1 |
| 2 | 97110-GP | 1 UN | $48.83 | 2026-05-19 | 1 | PA21183273L2 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: ELIZABETH WILSON; MI (member ID) 4EP8T60UC91; 8206 CHESTNUT ST; TRENTON, NJ, 08638
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737
- Submission reference TRC78109687, dated 2026-06-01 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-05-19.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: ELIZABETH WILSON; MI (member ID) 4EP8T60UC91.
Subject DOB 1951-03-02, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-05-19
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: ELIZABETH WILSON; MI (member ID) 4EP8T60UC91.
Subject DOB 1951-03-02, sex F.
Eligibility exchange reference ELG77910031, dated 2026-06-30 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-06-03, action code WQ, amount $91.58.
D9 (clearinghouse claim number): TRC78109687.
Trace (2 (referenced transaction trace)): TRC78109687.
received date (050): 2026-06-03.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: ELIZABETH WILSON; MI (member ID) 4EP8T60UC91.
Acknowledgment reference ACK78109687, dated 2026-06-03 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-05-19. Dx: Pain in left shoulder. 97112 (16 min): neuromuscular re-education of movement and balance. 97110 (15 min): therapeutic exercise for strength and ROM. Total timed minutes: 31. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1846349352, interchange 150183227 date 260630 time 0800 version 00501 usage P; group HS control 150183227 date 20260630 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 320684142 date 260630 time 0800 version 00501 usage P; group HB control 320684142 date 20260630 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1846349352, interchange 591460495 date 260601 time 0800 version 00501 usage P; group HC control 591460495 date 20260601 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 29
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 532996890 date 260603 time 0800 version 00501 usage P; group HN control 532996890 date 20260603 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 371149738 date 260629 time 0800 version 00501 usage P; group HP control 371149738 date 20260629 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 27
