# Case MOH2-000502

Patient ELIZABETH WILSON, DOB 1951-03-02, sex F, member ID 4EP8T60UC91. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-01-09.

## Adjudication outcome (835)
Claim PA23702885: status 4 (denied). Billed $133.6, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2605798646511, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-02-26.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT837568056, originator 1184634935.
claim statement period start (232): 2026-01-09.
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110 | 1 | $41.14 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $41.14 | HE N822 (missing procedure modifier(s)) |
| 2 | 97140 | 1 | $39.05 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $39.05 | HE N822 (missing procedure modifier(s)) |
| 3 | 97530 | 1 | $53.41 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $53.41 | HE N822 (missing procedure modifier(s)) |

Line item control numbers (REF 6R): PA23702885L1, PA23702885L2, PA23702885L3.
Remit claim parties: patient [QC]: ELIZABETH WILSON; MI (member ID) 4EP8T60UC91; rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737.

## Claim as billed (837P)
Claim PA23702885, total charge $133.6, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25512 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110 | 1 UN | $41.14 | 2026-01-09 | 1 | PA23702885L1 |
| 2 | 97140 | 1 UN | $39.05 | 2026-01-09 | 1 | PA23702885L2 |
| 3 | 97530 | 1 UN | $53.41 | 2026-01-09 | 1 | PA23702885L3 |

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: ELIZABETH WILSON; MI (member ID) 4EP8T60UC91; 8206 CHESTNUT ST; TRENTON, NJ, 08638
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: GRETA LINDQVIST; XX (NPI) 1205658765
- rendering provider [82]: SAMUEL RODRIGUEZ; XX (NPI) 1462872737
- Submission reference TRC74614407, dated 2026-01-24 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-01-09.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: ELIZABETH WILSON; MI (member ID) 4EP8T60UC91.
Subject DOB 1951-03-02, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-01-09
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: ELIZABETH WILSON; MI (member ID) 4EP8T60UC91.
Subject DOB 1951-03-02, sex F.
Eligibility exchange reference ELG44636573, dated 2026-03-01 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-01-24, action code WQ, amount $133.6.
D9 (clearinghouse claim number): TRC74614407.
Trace (2 (referenced transaction trace)): TRC74614407.
received date (050): 2026-01-24.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: ELIZABETH WILSON; MI (member ID) 4EP8T60UC91.
Acknowledgment reference ACK74614407, dated 2026-01-24 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-01-09. Dx: Pain in left shoulder. 97110 (16 min): therapeutic exercise for strength and ROM. 97140 (15 min): manual therapy (soft tissue and joint mobilization). 97530 (14 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 45. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1846349352, interchange 617640351 date 260301 time 0800 version 00501 usage P; group HS control 617640351 date 20260301 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 195168934 date 260301 time 0800 version 00501 usage P; group HB control 195168934 date 20260301 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1846349352, interchange 806492729 date 260124 time 0800 version 00501 usage P; group HC control 806492729 date 20260124 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 989834360 date 260124 time 0800 version 00501 usage P; group HN control 989834360 date 20260124 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 837568056 date 260226 time 0800 version 00501 usage P; group HP control 837568056 date 20260226 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 33
