# Case MOH2-000552

Patient BARBARA MOORE, DOB 1982-01-23, sex F, member ID ZRW491768858. Payer: LIBERTY BELL HEALTH PLANS. Service date 2026-10-14.

## Adjudication outcome (835)
Claim PA25613822: status 4 (denied). Billed $107.92, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2631777315829, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-11-13.
Payer [PR]: LIBERTY BELL HEALTH PLANS; 1650 ARCH ST; PHILADELPHIA, PA, 191032097; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820.
Trace (1 (current transaction trace)): EFT318657300, originator 1135091827.
claim statement period start (232): 2026-10-14.
Outpatient adjudication remarks (MOA): N30 (patient ineligible for this service).
Payee TJ (federal tax ID): 321822487.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP-59 | 1 | $43.64 | $0 | CO-27 (Contractual Obligation: expenses incurred after coverage terminated) $43.64 |  |
| 2 | 97140-GP-59 | 1 | $40.47 | $0 | CO-27 (Contractual Obligation: expenses incurred after coverage terminated) $40.47 |  |
| 3 | 97150-GP | 1 | $23.81 | $0 | CO-27 (Contractual Obligation: expenses incurred after coverage terminated) $23.81 |  |

Line item control numbers (REF 6R): PA25613822L1, PA25613822L2, PA25613822L3.
Modifiers on remit lines: 59 (distinct procedural service), GP (under PT plan of care).
Remit claim parties: patient [QC]: BARBARA MOORE; MI (member ID) ZRW491768858; rendering provider [82]: JOHN CLARK; XX (NPI) 1878226791.

## Claim as billed (837P)
Claim PA25613822, total charge $107.92, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: S335XXD (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP-59 | 1 UN | $43.64 | 2026-10-14 | 1 | PA25613822L1 |
| 2 | 97140-GP-59 | 1 UN | $40.47 | 2026-10-14 | 1 | PA25613822L2 |
| 3 | 97150-GP | 1 UN | $23.81 | 2026-10-14 | 1 | PA25613822L3 |

Modifiers on claim: 59 (distinct procedural service), GP (under PT plan of care).

Parties on claim:
- submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: LIBERTY BELL HEALTH PLANS; 46 (ETIN) 1350918273
- billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820; EI (employer ID/EIN) 321822487
- insured/subscriber [IL]: BARBARA MOORE; MI (member ID) ZRW491768858; 7339 LINCOLN LN; STATEN ISLAND, NY, 10331
- payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273
- referring provider [DN]: THOMAS BERGSTROM; XX (NPI) 1179655839
- rendering provider [82]: JOHN CLARK; XX (NPI) 1878226791
- Submission reference TRC83013454, dated 2026-10-22 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-10-14.
Inquiry parties: payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: BARBARA MOORE; MI (member ID) ZRW491768858.
Subject DOB 1982-01-23, sex F.

Response:
- benefit: 6 (inactive), coverage level IND, service type 30 (health benefit plan coverage), plan: LIBERTY BELL HEALTH PLANS EPO
- plan date (291): 2026-10-14
- eligibility begin (356): 2024-01-01
- eligibility end (357): 2026-09-30
Response parties: payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: BARBARA MOORE; MI (member ID) ZRW491768858.
Subject DOB 1982-01-23, sex F.
Eligibility exchange reference ELG93415182, dated 2026-11-20 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-10-23, action code WQ, amount $107.92.
D9 (clearinghouse claim number): TRC83013454.
Trace (2 (referenced transaction trace)): TRC83013454.
received date (050): 2026-10-23.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; patient [QC]: BARBARA MOORE; MI (member ID) ZRW491768858.
Acknowledgment reference ACK83013454, dated 2026-10-23 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-10-14. Dx: Sprain of ligaments of lumbar spine subsequent encounter. 97110 (14 min): therapeutic exercise for strength and ROM. 97140 (15 min): manual therapy (soft tissue and joint mobilization). 97150 (untimed, 1 unit): group therapeutic procedure. Total timed minutes: 29. 97110 was carried out during a later, clearly demarcated portion of the visit than 97150, on a different body region, for an unrelated goal. 97140 was rendered as an independent service from 97150 — separate start/stop times were recorded and a different body region was treated. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1353206904 to receiver [ZZ] 1350918273, interchange 269225425 date 261120 time 0800 version 00501 usage P; group HS control 269225425 date 20261120 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1350918273 to receiver [ZZ] 1353206904, interchange 534288557 date 261120 time 0800 version 00501 usage P; group HB control 534288557 date 20261120 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 14
- claim_837p: sender [ZZ] 321822487 to receiver [ZZ] 1350918273, interchange 631284117 date 261022 time 0800 version 00501 usage P; group HC control 631284117 date 20261022 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 321822487, interchange 134492678 date 261023 time 0800 version 00501 usage P; group HN control 134492678 date 20261023 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1350918273 to receiver [ZZ] 1353206904, interchange 318657300 date 261113 time 0800 version 00501 usage P; group HP control 318657300 date 20261113 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
