# Case MOH2-000415

Patient ELIZABETH WILSON, DOB 1951-03-02, sex F, member ID 4EP8T60UC91. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-06-07.

## Adjudication outcome (835)
Claim PA25330829: status 4 (denied). Billed $130.07, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2621171018657, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-07-30.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT437187828, originator 1184634935.
claim statement period start (232): 2026-06-07.
Outpatient adjudication remarks (MOA): N435 (exceeds number/frequency approved or allowed within time period).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $39.96 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $39.96 |  |
| 2 | 97112-GP | 1 | $43.63 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $43.63 |  |
| 3 | 97140-GP | 1 | $46.48 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $46.48 |  |

Line item control numbers (REF 6R): PA25330829L1, PA25330829L2, PA25330829L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: ELIZABETH WILSON; MI (member ID) 4EP8T60UC91; rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737.

## Claim as billed (837P)
Claim PA25330829, total charge $130.07, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25512 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $39.96 | 2026-06-07 | 1 | PA25330829L1 |
| 2 | 97112-GP | 1 UN | $43.63 | 2026-06-07 | 1 | PA25330829L2 |
| 3 | 97140-GP | 1 UN | $46.48 | 2026-06-07 | 1 | PA25330829L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: ELIZABETH WILSON; MI (member ID) 4EP8T60UC91; 8206 CHESTNUT ST; TRENTON, NJ, 08638
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: GRETA LINDQVIST; XX (NPI) 1205658765
- rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737
- Submission reference TRC75667035, dated 2026-06-24 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-06-07.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: ELIZABETH WILSON; MI (member ID) 4EP8T60UC91.
Subject DOB 1951-03-02, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-06-07
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: ELIZABETH WILSON; MI (member ID) 4EP8T60UC91.
Subject DOB 1951-03-02, sex F.
Eligibility exchange reference ELG81758797, dated 2026-08-01 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-06-24, action code WQ, amount $130.07.
D9 (clearinghouse claim number): TRC75667035.
Trace (2 (referenced transaction trace)): TRC75667035.
received date (050): 2026-06-24.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: ELIZABETH WILSON; MI (member ID) 4EP8T60UC91.
Acknowledgment reference ACK75667035, dated 2026-06-24 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-06-07. Dx: Pain in left shoulder. 97110 (16 min): therapeutic exercise for strength and ROM. 97112 (15 min): neuromuscular re-education of movement and balance. 97140 (16 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 47. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1846349352, interchange 909042275 date 260801 time 0800 version 00501 usage P; group HS control 909042275 date 20260801 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 112199302 date 260801 time 0800 version 00501 usage P; group HB control 112199302 date 20260801 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1846349352, interchange 826619668 date 260624 time 0800 version 00501 usage P; group HC control 826619668 date 20260624 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 543979367 date 260624 time 0800 version 00501 usage P; group HN control 543979367 date 20260624 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 437187828 date 260730 time 0800 version 00501 usage P; group HP control 437187828 date 20260730 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
