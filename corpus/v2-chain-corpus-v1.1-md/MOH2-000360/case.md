# Case MOH2-000360

Patient MICHAEL WHITE, DOB 1955-04-09, sex F, member ID 4EM6NG3EA62. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-06-14.

## Adjudication outcome (835)
Claim PA24561583: status 4 (denied). Billed $165.83, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2622354477779, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-08-11.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT228101955, originator 1184634935.
claim statement period start (232): 2026-06-14.
Outpatient adjudication remarks (MOA): N111 (no appeal right except duplicate claim/service issue).
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97530-GP-KX | 1 | $48.74 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $48.74 |  |
| 2 | 97110-GP-KX | 1 | $39.95 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $39.95 |  |
| 3 | 97140-GP-KX | 2 | $77.14 | $0 | OA-18 (Other Adjustment: exact duplicate claim/service) $77.14 |  |

Line item control numbers (REF 6R): PA24561583L1, PA24561583L2, PA24561583L3.
Modifiers on remit lines: GP (under PT plan of care), KX.
Remit claim parties: patient [QC]: MICHAEL WHITE; MI (member ID) 4EM6NG3EA62; rendering provider [82]: DOROTHY LOPEZ; XX (NPI) 1390221007.

## Claim as billed (837P)
Claim PA24561583, total charge $165.83, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M1712 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97530-GP-KX | 1 UN | $48.74 | 2026-06-14 | 1 | PA24561583L1 |
| 2 | 97110-GP-KX | 1 UN | $39.95 | 2026-06-14 | 1 | PA24561583L2 |
| 3 | 97140-GP-KX | 2 UN | $77.14 | 2026-06-14 | 1 | PA24561583L3 |

Modifiers on claim: GP (under PT plan of care), KX.

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: MICHAEL WHITE; MI (member ID) 4EM6NG3EA62; 1069 LINCOLN LN; WILMINGTON, DE, 19855
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: GRETA LINDQVIST; XX (NPI) 1205658765
- rendering provider [82]: DOROTHY LOPEZ; XX (NPI) 1390221007
- Submission reference TRC71706393, dated 2026-07-25 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-06-14.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: MICHAEL WHITE; MI (member ID) 4EM6NG3EA62.
Subject DOB 1955-04-09, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-06-14
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: MICHAEL WHITE; MI (member ID) 4EM6NG3EA62.
Subject DOB 1955-04-09, sex F.
Eligibility exchange reference ELG66846512, dated 2026-08-17 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-07-26, action code WQ, amount $165.83.
D9 (clearinghouse claim number): TRC71706393.
Trace (2 (referenced transaction trace)): TRC71706393.
received date (050): 2026-07-26.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: MICHAEL WHITE; MI (member ID) 4EM6NG3EA62.
Acknowledgment reference ACK71706393, dated 2026-07-26 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-06-14. Dx: Unilateral primary osteoarthritis left knee. 97530 (16 min): therapeutic activities (dynamic functional tasks). 97110 (16 min): therapeutic exercise for strength and ROM. 97140 (29 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 61. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1846349352, interchange 513689303 date 260817 time 0800 version 00501 usage P; group HS control 513689303 date 20260817 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1801579548, interchange 129158190 date 260817 time 0800 version 00501 usage P; group HB control 129158190 date 20260817 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1846349352, interchange 912903868 date 260725 time 0800 version 00501 usage P; group HC control 912903868 date 20260725 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 474225077 date 260726 time 0800 version 00501 usage P; group HN control 474225077 date 20260726 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1801579548, interchange 228101955 date 260811 time 0800 version 00501 usage P; group HP control 228101955 date 20260811 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
