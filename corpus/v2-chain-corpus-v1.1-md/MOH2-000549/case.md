# Case MOH2-000549

Patient DOROTHY THOMPSON, DOB 1945-11-22, sex F, member ID 6U95WJ6UD98. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-08-16.

## Adjudication outcome (835)
Claim PA21835651: status 1 (processed as primary, paid). Billed $74.09, paid $14.43, patient responsibility $3.61. Filing indicator MB (Medicare Part B). Payer claim control 2626687738844, POS 11 (office), frequency 1 (original claim).
Payment: $14.43 by CHK (check), handling I.
production date (405): 2026-09-23.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820.
Trace (1 (current transaction trace)): EFT996279888, originator 1184634935.
claim statement period start (232): 2026-08-16.
Payee TJ (federal tax ID): 321822487.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97150-GP-KX | 1 | $25.32 | $14.43 allowed (B6) $18.04 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $7.28; PR-2 (Patient Responsibility: coinsurance amount) $3.61 |  |
| 2 | 97112-GP-KX | 1 | $48.77 | $0 | CO-236 (Contractual Obligation: procedure/modifier combination not compatible per coding guidelines, bundled) $48.77 | HE N20 (service not payable with other service rendered on the same date) |

Line item control numbers (REF 6R): PA21835651L1, PA21835651L2.
Modifiers on remit lines: GP (under PT plan of care), KX.
Remit claim parties: patient [QC]: DOROTHY THOMPSON; MI (member ID) 6U95WJ6UD98; rendering provider [82]: MICHAEL MARTINEZ; XX (NPI) 1850202042.

## Claim as billed (837P)
Claim PA21835651, total charge $74.09, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M5450 (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97150-GP-KX | 1 UN | $25.32 | 2026-08-16 | 1 | PA21835651L1 |
| 2 | 97112-GP-KX | 1 UN | $48.77 | 2026-08-16 | 1 | PA21835651L2 |

Modifiers on claim: GP (under PT plan of care), KX.

Parties on claim:
- submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820; EI (employer ID/EIN) 321822487
- insured/subscriber [IL]: DOROTHY THOMPSON; MI (member ID) 6U95WJ6UD98; 7878 MAPLE ST; STATEN ISLAND, NY, 10329
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: DAVID GOLDSTEIN; XX (NPI) 1996029234
- rendering provider [82]: MICHAEL MARTINEZ; XX (NPI) 1850202042
- Submission reference TRC78330384, dated 2026-08-19 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-08-16.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: DOROTHY THOMPSON; MI (member ID) 6U95WJ6UD98.
Subject DOB 1945-11-22, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-08-16
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: DOROTHY THOMPSON; MI (member ID) 6U95WJ6UD98.
Subject DOB 1945-11-22, sex F.
Eligibility exchange reference ELG15937792, dated 2026-09-30 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-08-20, action code WQ, amount $74.09.
D9 (clearinghouse claim number): TRC78330384.
Trace (2 (referenced transaction trace)): TRC78330384.
received date (050): 2026-08-20.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; patient [QC]: DOROTHY THOMPSON; MI (member ID) 6U95WJ6UD98.
Acknowledgment reference ACK78330384, dated 2026-08-20 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-08-16. Dx: Low back pain unspecified. 97150 (untimed, 1 unit): group therapeutic procedure. 97112 (14 min): neuromuscular re-education of movement and balance. Total timed minutes: 14. 97112 was integral to the 97150 intervention this visit — same region, same goal, one continuous session. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1353206904 to receiver [ZZ] 1846349352, interchange 597665226 date 260930 time 0800 version 00501 usage P; group HS control 597665226 date 20260930 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1353206904, interchange 899779053 date 260930 time 0800 version 00501 usage P; group HB control 899779053 date 20260930 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 321822487 to receiver [ZZ] 1846349352, interchange 750626321 date 260819 time 0800 version 00501 usage P; group HC control 750626321 date 20260819 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 321822487, interchange 916778950 date 260820 time 0800 version 00501 usage P; group HN control 916778950 date 20260820 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1353206904, interchange 996279888 date 260923 time 0800 version 00501 usage P; group HP control 996279888 date 20260923 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 29
