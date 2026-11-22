# Case MOH2-000139

Patient MICHAEL LEE, DOB 1985-04-16, sex F, member ID DYA865312039. Payer: LIBERTY BELL HEALTH PLANS. Service date 2025-01-30.

## Adjudication outcome (835)
Claim PA25314364: status 4 (denied). Billed $88.52, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2531223677909, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2025-11-08.
Payer [PR]: LIBERTY BELL HEALTH PLANS; 1650 ARCH ST; PHILADELPHIA, PA, 191032097; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820.
Trace (1 (current transaction trace)): EFT972253498, originator 1135091827.
claim statement period start (232): 2025-01-30.
Outpatient adjudication remarks (MOA): N211 (you may not appeal this decision).
Payee TJ (federal tax ID): 321822487.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $37.98 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $37.98 |  |
| 2 | 97112-GP | 1 | $50.54 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $50.54 |  |

Line item control numbers (REF 6R): PA25314364L1, PA25314364L2.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: MICHAEL LEE; MI (member ID) DYA865312039; rendering provider [82]: MICHAEL MARTINEZ; XX (NPI) 1850202042.

## Claim as billed (837P)
Claim PA25314364, total charge $88.52, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25562 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $37.98 | 2025-01-30 | 1 | PA25314364L1 |
| 2 | 97112-GP | 1 UN | $50.54 | 2025-01-30 | 1 | PA25314364L2 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: LIBERTY BELL HEALTH PLANS; 46 (ETIN) 1350918273
- billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820; EI (employer ID/EIN) 321822487
- insured/subscriber [IL]: MICHAEL LEE; MI (member ID) DYA865312039; 4492 FRANKLIN ST; TRENTON, NJ, 08661
- payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273
- referring provider [DN]: MARCUS WEBB; XX (NPI) 1583494452
- rendering provider [82]: MICHAEL MARTINEZ; XX (NPI) 1850202042
- Submission reference TRC12150848, dated 2025-10-12 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2025-01-30.
Inquiry parties: payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: MICHAEL LEE; MI (member ID) DYA865312039.
Subject DOB 1985-04-16, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: LIBERTY BELL HEALTH PLANS POS
- plan date (291): 2025-01-30
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: MICHAEL LEE; MI (member ID) DYA865312039.
Subject DOB 1985-04-16, sex F.
Eligibility exchange reference ELG33466357, dated 2025-11-12 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2025-02-16, action code WQ, amount $88.52.
D9 (clearinghouse claim number): TRC12150848.
Trace (2 (referenced transaction trace)): TRC12150848.
received date (050): 2025-02-16.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; patient [QC]: MICHAEL LEE; MI (member ID) DYA865312039.
Acknowledgment reference ACK12150848, dated 2025-02-16 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2025-01-30. Dx: Pain in left knee. 97110 (16 min): therapeutic exercise for strength and ROM. 97112 (15 min): neuromuscular re-education of movement and balance. Total timed minutes: 31. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1353206904 to receiver [ZZ] 1350918273, interchange 853743952 date 251112 time 0800 version 00501 usage P; group HS control 853743952 date 20251112 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1350918273 to receiver [ZZ] 1353206904, interchange 668353216 date 251112 time 0800 version 00501 usage P; group HB control 668353216 date 20251112 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 321822487 to receiver [ZZ] 1350918273, interchange 955119501 date 251012 time 0800 version 00501 usage P; group HC control 955119501 date 20251012 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 321822487, interchange 160639815 date 250216 time 0800 version 00501 usage P; group HN control 160639815 date 20250216 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1350918273 to receiver [ZZ] 1353206904, interchange 972253498 date 251108 time 0800 version 00501 usage P; group HP control 972253498 date 20251108 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 27
