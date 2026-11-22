# Case MOH2-000188

Patient JESSICA JACKSON, DOB 1943-09-23, sex F, member ID 7QQ3T84RA44. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-07-17.

## Adjudication outcome (835)
Claim PA28429677: status 4 (denied). Billed $173.6, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2623355825946, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-08-21.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820.
Trace (1 (current transaction trace)): EFT792998203, originator 1184634935.
claim statement period start (232): 2026-07-17.
Payee TJ (federal tax ID): 321822487.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97140 | 1 | $45.05 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $45.05 | HE N822 (missing procedure modifier(s)) |
| 2 | 97110 | 1 | $37.85 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $37.85 | HE N822 (missing procedure modifier(s)) |
| 3 | 97112 | 2 | $90.7 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $90.7 | HE N822 (missing procedure modifier(s)) |

Line item control numbers (REF 6R): PA28429677L1, PA28429677L2, PA28429677L3.
Remit claim parties: patient [QC]: JESSICA JACKSON; MI (member ID) 7QQ3T84RA44; rendering provider [82]: THOMAS PEREZ; XX (NPI) 1981894162.

## Claim as billed (837P)
Claim PA28429677, total charge $173.6, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: S93401D (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97140 | 1 UN | $45.05 | 2026-07-17 | 1 | PA28429677L1 |
| 2 | 97110 | 1 UN | $37.85 | 2026-07-17 | 1 | PA28429677L2 |
| 3 | 97112 | 2 UN | $90.7 | 2026-07-17 | 1 | PA28429677L3 |

Parties on claim:
- submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820; EI (employer ID/EIN) 321822487
- insured/subscriber [IL]: JESSICA JACKSON; MI (member ID) 7QQ3T84RA44; 9325 MAPLE LN; STATEN ISLAND, NY, 10335
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: SARAH CHEN; XX (NPI) 1410042904
- rendering provider [82]: THOMAS PEREZ; XX (NPI) 1981894162
- Submission reference TRC55085240, dated 2026-07-25 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-07-17.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: JESSICA JACKSON; MI (member ID) 7QQ3T84RA44.
Subject DOB 1943-09-23, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-07-17
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: JESSICA JACKSON; MI (member ID) 7QQ3T84RA44.
Subject DOB 1943-09-23, sex F.
Eligibility exchange reference ELG41019749, dated 2026-08-24 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-07-27, action code WQ, amount $173.6.
D9 (clearinghouse claim number): TRC55085240.
Trace (2 (referenced transaction trace)): TRC55085240.
received date (050): 2026-07-27.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; patient [QC]: JESSICA JACKSON; MI (member ID) 7QQ3T84RA44.
Acknowledgment reference ACK55085240, dated 2026-07-27 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-07-17. Dx: Sprain of unspecified ligament of right ankle subsequent encounter. 97140 (16 min): manual therapy (soft tissue and joint mobilization). 97110 (14 min): therapeutic exercise for strength and ROM. 97112 (29 min): neuromuscular re-education of movement and balance. Total timed minutes: 59. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1353206904 to receiver [ZZ] 1846349352, interchange 354813110 date 260824 time 0800 version 00501 usage P; group HS control 354813110 date 20260824 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1353206904, interchange 419516325 date 260824 time 0800 version 00501 usage P; group HB control 419516325 date 20260824 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 321822487 to receiver [ZZ] 1846349352, interchange 424289702 date 260725 time 0800 version 00501 usage P; group HC control 424289702 date 20260725 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 321822487, interchange 606387767 date 260727 time 0800 version 00501 usage P; group HN control 606387767 date 20260727 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1353206904, interchange 792998203 date 260821 time 0800 version 00501 usage P; group HP control 792998203 date 20260821 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 33
