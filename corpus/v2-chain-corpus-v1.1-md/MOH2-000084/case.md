# Case MOH2-000084

Patient MICHAEL LEE, DOB 1985-04-16, sex F, member ID DYA865312039. Payer: LIBERTY BELL HEALTH PLANS. Service date 2025-09-03.

## Adjudication outcome (835)
Claim PA25166764: status 4 (denied). Billed $183.91, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2529795870085, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2025-10-24.
Payer [PR]: LIBERTY BELL HEALTH PLANS; 1650 ARCH ST; PHILADELPHIA, PA, 191032097; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820.
Trace (1 (current transaction trace)): EFT932571494, originator 1135091827.
claim statement period start (232): 2025-09-03.
Outpatient adjudication remarks (MOA): N30 (patient ineligible for this service).
Payee TJ (federal tax ID): 321822487.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97140-GP | 1 | $46.57 | $0 | CO-27 (Contractual Obligation: expenses incurred after coverage terminated) $46.57 |  |
| 2 | 97140-GP | 2 | $87.35 | $0 | CO-27 (Contractual Obligation: expenses incurred after coverage terminated) $87.35 |  |
| 3 | 97530-GP | 1 | $49.99 | $0 | CO-27 (Contractual Obligation: expenses incurred after coverage terminated) $49.99 |  |

Line item control numbers (REF 6R): PA25166764L1, PA25166764L2, PA25166764L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: MICHAEL LEE; MI (member ID) DYA865312039; rendering provider [82]: MICHAEL MARTINEZ; XX (NPI) 1850202042.

## Claim as billed (837P)
Claim PA25166764, total charge $183.91, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25562 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97140-GP | 1 UN | $46.57 | 2025-09-03 | 1 | PA25166764L1 |
| 2 | 97140-GP | 2 UN | $87.35 | 2025-09-03 | 1 | PA25166764L2 |
| 3 | 97530-GP | 1 UN | $49.99 | 2025-09-03 | 1 | PA25166764L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: LIBERTY BELL HEALTH PLANS; 46 (ETIN) 1350918273
- billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820; EI (employer ID/EIN) 321822487
- insured/subscriber [IL]: MICHAEL LEE; MI (member ID) DYA865312039; 4492 FRANKLIN ST; TRENTON, NJ, 08661
- payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273
- referring provider [DN]: MARCUS WEBB; XX (NPI) 1583494452
- rendering provider [82]: MICHAEL MARTINEZ; XX (NPI) 1850202042
- Submission reference TRC78141011, dated 2025-09-18 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2025-09-03.
Inquiry parties: payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: MICHAEL LEE; MI (member ID) DYA865312039.
Subject DOB 1985-04-16, sex F.

Response:
- benefit: 6 (inactive), coverage level IND, service type 30 (health benefit plan coverage), plan: LIBERTY BELL HEALTH PLANS POS
- plan date (291): 2025-09-03
- eligibility begin (356): 2024-01-01
- eligibility end (357): 2025-08-31
Response parties: payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: MICHAEL LEE; MI (member ID) DYA865312039.
Subject DOB 1985-04-16, sex F.
Eligibility exchange reference ELG38426294, dated 2025-10-29 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2025-09-19, action code WQ, amount $183.91.
D9 (clearinghouse claim number): TRC78141011.
Trace (2 (referenced transaction trace)): TRC78141011.
received date (050): 2025-09-19.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; patient [QC]: MICHAEL LEE; MI (member ID) DYA865312039.
Acknowledgment reference ACK78141011, dated 2025-09-19 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2025-09-03. Dx: Pain in left knee. 97140 (14 min): manual therapy (soft tissue and joint mobilization). 97140 (31 min): manual therapy (soft tissue and joint mobilization). 97530 (16 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 61. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1353206904 to receiver [ZZ] 1350918273, interchange 257792330 date 251029 time 0800 version 00501 usage P; group HS control 257792330 date 20251029 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1350918273 to receiver [ZZ] 1353206904, interchange 939980115 date 251029 time 0800 version 00501 usage P; group HB control 939980115 date 20251029 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 14
- claim_837p: sender [ZZ] 321822487 to receiver [ZZ] 1350918273, interchange 752369628 date 250918 time 0800 version 00501 usage P; group HC control 752369628 date 20250918 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 321822487, interchange 392821708 date 250919 time 0800 version 00501 usage P; group HN control 392821708 date 20250919 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1350918273 to receiver [ZZ] 1353206904, interchange 932571494 date 251024 time 0800 version 00501 usage P; group HP control 932571494 date 20251024 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
