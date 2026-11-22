# Case MOH2-000730

Patient THOMAS HARRIS, DOB 1954-02-25, sex M, member ID 7AM6NJ4QA31. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-05-31.

## Adjudication outcome (835)
Claim PA26055779: status 4 (denied). Billed $183.23, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2619498043798, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-07-13.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310.
Trace (1 (current transaction trace)): EFT277906701, originator 1184634935.
claim statement period start (232): 2026-05-31.
Outpatient adjudication remarks (MOA): N435 (exceeds number/frequency approved or allowed within time period).
Payee TJ (federal tax ID): 261118724.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 | $93.68 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $93.68 |  |
| 2 | 97110-GP | 1 | $41.88 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $41.88 |  |
| 3 | 97140-GP | 1 | $47.67 | $0 | CO-119 (Contractual Obligation: benefit maximum for this time period has been reached) $47.67 |  |

Line item control numbers (REF 6R): PA26055779L1, PA26055779L2, PA26055779L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: THOMAS HARRIS; MI (member ID) 7AM6NJ4QA31; rendering provider [82]: JOSEPH ANDERSON; XX (NPI) 1260849754.

## Claim as billed (837P)
Claim PA26055779, total charge $183.23, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25511 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 UN | $93.68 | 2026-05-31 | 1 | PA26055779L1 |
| 2 | 97110-GP | 1 UN | $41.88 | 2026-05-31 | 1 | PA26055779L2 |
| 3 | 97140-GP | 1 UN | $47.67 | 2026-05-31 | 1 | PA26055779L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; 455 GERMANTOWN PIKE; NORRISTOWN, PA, 194013310; EI (employer ID/EIN) 261118724
- insured/subscriber [IL]: THOMAS HARRIS; MI (member ID) 7AM6NJ4QA31; 7202 WILLOW RD; TRENTON, NJ, 08651
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: PRIYA NAIR; XX (NPI) 1903307855
- rendering provider [82]: JOSEPH ANDERSON; XX (NPI) 1260849754
- Submission reference TRC22658394, dated 2026-06-18 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-05-31.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: THOMAS HARRIS; MI (member ID) 7AM6NJ4QA31.
Subject DOB 1954-02-25, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-05-31
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; insured/subscriber [IL]: THOMAS HARRIS; MI (member ID) 7AM6NJ4QA31.
Subject DOB 1954-02-25, sex M.
Eligibility exchange reference ELG96771580, dated 2026-07-15 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-06-18, action code WQ, amount $183.23.
D9 (clearinghouse claim number): TRC22658394.
Trace (2 (referenced transaction trace)): TRC22658394.
received date (050): 2026-06-18.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: SCHUYLKILL PHYSICAL THERAPY GROUP; 46 (ETIN) 261118724; billing provider [85]: SCHUYLKILL PHYSICAL THERAPY GROUP; XX (NPI) 1601336180; patient [QC]: THOMAS HARRIS; MI (member ID) 7AM6NJ4QA31.
Acknowledgment reference ACK22658394, dated 2026-06-18 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-05-31. Dx: Pain in right shoulder. 97110 (31 min): therapeutic exercise for strength and ROM. 97110 (15 min): therapeutic exercise for strength and ROM. 97140 (16 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 62. Patient at prior level of function; today's treatment repeated the standing maintenance protocol with no progression or new findings.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1601336180 to receiver [ZZ] 1846349352, interchange 181272943 date 260715 time 0800 version 00501 usage P; group HS control 181272943 date 20260715 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 988631397 date 260715 time 0800 version 00501 usage P; group HB control 988631397 date 20260715 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 261118724 to receiver [ZZ] 1846349352, interchange 116438781 date 260618 time 0800 version 00501 usage P; group HC control 116438781 date 20260618 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 261118724, interchange 389772085 date 260618 time 0800 version 00501 usage P; group HN control 389772085 date 20260618 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1601336180, interchange 277906701 date 260713 time 0800 version 00501 usage P; group HP control 277906701 date 20260713 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
