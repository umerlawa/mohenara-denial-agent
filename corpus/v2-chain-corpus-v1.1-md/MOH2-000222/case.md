# Case MOH2-000222

Patient BARBARA MOORE, DOB 1982-01-23, sex F, member ID ZRW491768858. Payer: LIBERTY BELL HEALTH PLANS. Service date 2026-09-26.

## Adjudication outcome (835)
Claim PA25099545: status 4 (denied). Billed $185.62, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2631309282439, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-11-09.
Payer [PR]: LIBERTY BELL HEALTH PLANS; 1650 ARCH ST; PHILADELPHIA, PA, 191032097; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820.
Trace (1 (current transaction trace)): EFT790079082, originator 1135091827.
claim statement period start (232): 2026-09-26.
Payee TJ (federal tax ID): 321822487.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97140 | 1 | $42.83 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $42.83 | HE N822 (missing procedure modifier(s)) |
| 2 | 97110 | 1 | $49.36 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $49.36 | HE N822 (missing procedure modifier(s)) |
| 3 | 97112 | 2 | $93.43 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $93.43 | HE N822 (missing procedure modifier(s)) |

Line item control numbers (REF 6R): PA25099545L1, PA25099545L2, PA25099545L3.
Remit claim parties: patient [QC]: BARBARA MOORE; MI (member ID) ZRW491768858; rendering provider [82]: JOHN CLARK; XX (NPI) 1878226791.

## Claim as billed (837P)
Claim PA25099545, total charge $185.62, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: S335XXD (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97140 | 1 UN | $42.83 | 2026-09-26 | 1 | PA25099545L1 |
| 2 | 97110 | 1 UN | $49.36 | 2026-09-26 | 1 | PA25099545L2 |
| 3 | 97112 | 2 UN | $93.43 | 2026-09-26 | 1 | PA25099545L3 |

Parties on claim:
- submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: LIBERTY BELL HEALTH PLANS; 46 (ETIN) 1350918273
- billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820; EI (employer ID/EIN) 321822487
- insured/subscriber [IL]: BARBARA MOORE; MI (member ID) ZRW491768858; 7339 LINCOLN LN; STATEN ISLAND, NY, 10331
- payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273
- referring provider [DN]: THOMAS BERGSTROM; XX (NPI) 1179655839
- rendering provider [82]: JOHN CLARK; XX (NPI) 1878226791
- Submission reference TRC25388545, dated 2026-10-15 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-09-26.
Inquiry parties: payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: BARBARA MOORE; MI (member ID) ZRW491768858.
Subject DOB 1982-01-23, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: LIBERTY BELL HEALTH PLANS EPO
- plan date (291): 2026-09-26
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: LIBERTY BELL HEALTH PLANS; PI (payer ID) 1350918273; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: BARBARA MOORE; MI (member ID) ZRW491768858.
Subject DOB 1982-01-23, sex F.
Eligibility exchange reference ELG69084783, dated 2026-11-10 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-10-15, action code WQ, amount $185.62.
D9 (clearinghouse claim number): TRC25388545.
Trace (2 (referenced transaction trace)): TRC25388545.
received date (050): 2026-10-15.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; patient [QC]: BARBARA MOORE; MI (member ID) ZRW491768858.
Acknowledgment reference ACK25388545, dated 2026-10-15 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-09-26. Dx: Sprain of ligaments of lumbar spine subsequent encounter. 97140 (15 min): manual therapy (soft tissue and joint mobilization). 97110 (14 min): therapeutic exercise for strength and ROM. 97112 (30 min): neuromuscular re-education of movement and balance. Total timed minutes: 59. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1353206904 to receiver [ZZ] 1350918273, interchange 744283629 date 261110 time 0800 version 00501 usage P; group HS control 744283629 date 20261110 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1350918273 to receiver [ZZ] 1353206904, interchange 171662568 date 261110 time 0800 version 00501 usage P; group HB control 171662568 date 20261110 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 321822487 to receiver [ZZ] 1350918273, interchange 393992078 date 261015 time 0800 version 00501 usage P; group HC control 393992078 date 20261015 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 321822487, interchange 720265106 date 261015 time 0800 version 00501 usage P; group HN control 720265106 date 20261015 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1350918273 to receiver [ZZ] 1353206904, interchange 790079082 date 261109 time 0800 version 00501 usage P; group HP control 790079082 date 20261109 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 33
