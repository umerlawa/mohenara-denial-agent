# Case MOH2-000298

Patient MICHAEL LEE, DOB 1985-04-16, sex F, member ID DYA865312039. Payer: LIBERTY BELL HEALTH PLANS. Service date 2025-09-11.

## Adjudication outcome (835)
Claim PA22192436: status 4 (denied). Billed $211.07, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2529990892149, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2025-10-26.
Payer [PR]: LIBERTY BELL HEALTH PLANS; 1650 ARCH ST; PHILADELPHIA, PA, 191032097; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820.
Trace (1 (current transaction trace)): EFT903062915, originator 1135091827.
claim statement period start (232): 2025-09-11.
Outpatient adjudication remarks (MOA): N30 (patient ineligible for this service).
Payee TJ (federal tax ID): 321822487.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP-59 | 2 | $80.33 | $0 | CO-27 (Contractual Obligation: expenses incurred after coverage terminated) $80.33 |  |
| 2 | 97110-GP-59 | 2 | $98.31 | $0 | CO-27 (Contractual Obligation: expenses incurred after coverage terminated) $98.31 |  |
| 3 | 97150-GP | 1 | $32.43 | $0 | CO-27 (Contractual Obligation: expenses incurred after coverage terminated) $32.43 |  |

Line item control numbers (REF 6R): PA22192436L1, PA22192436L2, PA22192436L3.
Modifiers on remit lines: 59 (distinct procedural service), GP (under PT plan of care).
Remit claim parties: patient [QC]: MICHAEL LEE; MI (member ID) DYA865312039; rendering provider [82]: MICHAEL MARTINEZ; XX (NPI) 1850202042.

## Claim as billed (837P)
Claim PA22192436, total charge $211.07, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25562 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP-59 | 2 UN | $80.33 | 2025-09-11 | 1 | PA22192436L1 |
| 2 | 97110-GP-59 | 2 UN | $98.31 | 2025-09-11 | 1 | PA22192436L2 |
| 3 | 97150-GP | 1 UN | $32.43 | 2025-09-11 | 1 | PA22192436L3 |

Modifiers on claim: 59 (distinct procedural service), GP (under PT plan of care).

Parties on claim:
- submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: LIBERTY BELL HEALTH PLANS; 46 (ETIN) 1350918273
- billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820; EI (employer ID/EIN) 321822487
- insured/subscriber [IL]: MICHAEL LEE; MI (member ID) DYA865312039; 4492 FRANKLIN ST; TRENTON, NJ, 08661
- payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273
- referring provider [DN]: MARCUS WEBB; XX (NPI) 1583494452
- rendering provider [82]: MICHAEL MARTINEZ; XX (NPI) 1850202042
- Submission reference TRC42495951, dated 2025-09-28 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2025-09-11.
Inquiry parties: payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: MICHAEL LEE; MI (member ID) DYA865312039.
Subject DOB 1985-04-16, sex F.

Response:
- benefit: 6 (inactive), coverage level IND, service type 30 (health benefit plan coverage), plan: LIBERTY BELL HEALTH PLANS POS
- plan date (291): 2025-09-11
- eligibility begin (356): 2024-01-01
- eligibility end (357): 2025-08-31
Response parties: payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: MICHAEL LEE; MI (member ID) DYA865312039.
Subject DOB 1985-04-16, sex F.
Eligibility exchange reference ELG84022850, dated 2025-10-29 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2025-09-29, action code WQ, amount $211.07.
D9 (clearinghouse claim number): TRC42495951.
Trace (2 (referenced transaction trace)): TRC42495951.
received date (050): 2025-09-29.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; patient [QC]: MICHAEL LEE; MI (member ID) DYA865312039.
Acknowledgment reference ACK42495951, dated 2025-09-29 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2025-09-11. Dx: Pain in left knee. 97110 (30 min): therapeutic exercise for strength and ROM. 97110 (29 min): therapeutic exercise for strength and ROM. 97150 (untimed, 1 unit): group therapeutic procedure. Total timed minutes: 59. 97110 and 97150 were furnished as separate and distinct services: different session times, different anatomic regions, independent treatment goals. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1353206904 to receiver [ZZ] 1350918273, interchange 549882396 date 251029 time 0800 version 00501 usage P; group HS control 549882396 date 20251029 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1350918273 to receiver [ZZ] 1353206904, interchange 609954986 date 251029 time 0800 version 00501 usage P; group HB control 609954986 date 20251029 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 14
- claim_837p: sender [ZZ] 321822487 to receiver [ZZ] 1350918273, interchange 621422516 date 250928 time 0800 version 00501 usage P; group HC control 621422516 date 20250928 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 321822487, interchange 256034700 date 250929 time 0800 version 00501 usage P; group HN control 256034700 date 20250929 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1350918273 to receiver [ZZ] 1353206904, interchange 903062915 date 251026 time 0800 version 00501 usage P; group HP control 903062915 date 20251026 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
