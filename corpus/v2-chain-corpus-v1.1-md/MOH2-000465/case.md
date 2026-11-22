# Case MOH2-000465

Patient MARIA RODRIGUEZ, DOB 1955-10-10, sex M, member ID 5E10X77QK02. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-06-04.

## Adjudication outcome (835)
Claim PA28677128: status 4 (denied). Billed $175.9, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2618358355124, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-07-02.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820.
Trace (1 (current transaction trace)): EFT400868104, originator 1184634935.
claim statement period start (232): 2026-06-04.
Outpatient adjudication remarks (MOA): N286 (missing/incomplete/invalid referring provider primary identifier).
Payee TJ (federal tax ID): 321822487.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $50.76 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $50.76 |  |
| 2 | 97140-GP | 1 | $38.46 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $38.46 |  |
| 3 | 97140-GP | 2 | $86.68 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $86.68 |  |

Line item control numbers (REF 6R): PA28677128L1, PA28677128L2, PA28677128L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: MARIA RODRIGUEZ; MI (member ID) 5E10X77QK02; rendering provider [82]: JOHN CLARK; XX (NPI) 1878226791.

## Claim as billed (837P)
Claim PA28677128, total charge $175.9, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $50.76 | 2026-06-04 | 1 | PA28677128L1 |
| 2 | 97140-GP | 1 UN | $38.46 | 2026-06-04 | 1 | PA28677128L2 |
| 3 | 97140-GP | 2 UN | $86.68 | 2026-06-04 | 1 | PA28677128L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820; EI (employer ID/EIN) 321822487
- insured/subscriber [IL]: MARIA RODRIGUEZ; MI (member ID) 5E10X77QK02; 2473 WILLOW ST; TRENTON, NJ, 08690
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- rendering provider [82]: JOHN CLARK; XX (NPI) 1878226791
- Submission reference TRC12162372, dated 2026-06-14 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-06-04.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: MARIA RODRIGUEZ; MI (member ID) 5E10X77QK02.
Subject DOB 1955-10-10, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-06-04
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: MARIA RODRIGUEZ; MI (member ID) 5E10X77QK02.
Subject DOB 1955-10-10, sex M.
Eligibility exchange reference ELG15536949, dated 2026-07-08 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-06-14, action code WQ, amount $175.9.
D9 (clearinghouse claim number): TRC12162372.
Trace (2 (referenced transaction trace)): TRC12162372.
received date (050): 2026-06-14.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; patient [QC]: MARIA RODRIGUEZ; MI (member ID) 5E10X77QK02.
Acknowledgment reference ACK12162372, dated 2026-06-14 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-06-04. Dx: Aftercare following joint replacement surgery. 97110 (15 min): therapeutic exercise for strength and ROM. 97140 (15 min): manual therapy (soft tissue and joint mobilization). 97140 (29 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 59. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1353206904 to receiver [ZZ] 1846349352, interchange 852826602 date 260708 time 0800 version 00501 usage P; group HS control 852826602 date 20260708 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1353206904, interchange 830102893 date 260708 time 0800 version 00501 usage P; group HB control 830102893 date 20260708 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 321822487 to receiver [ZZ] 1846349352, interchange 325479233 date 260614 time 0800 version 00501 usage P; group HC control 325479233 date 20260614 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 33
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 321822487, interchange 939552446 date 260614 time 0800 version 00501 usage P; group HN control 939552446 date 20260614 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1353206904, interchange 400868104 date 260702 time 0800 version 00501 usage P; group HP control 400868104 date 20260702 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
