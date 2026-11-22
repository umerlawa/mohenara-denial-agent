# Case MOH2-000522

Patient JESSICA HARRIS, DOB 1997-12-11, sex F, member ID SXA354348278. Payer: KEYSTONE COMMERCIAL HEALTH. Service date 2025-06-07.

## Adjudication outcome (835)
Claim PA24836086: status 4 (denied). Billed $189.79, paid $0, patient responsibility $189.79. Filing indicator CI (commercial insurance). Payer claim control 2520196868011, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2025-07-20.
Payer [PR]: KEYSTONE COMMERCIAL HEALTH; 1200 MARKET ST; PHILADELPHIA, PA, 191071200; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820.
Trace (1 (current transaction trace)): EFT688733446, originator 1165028491.
claim statement period start (232): 2025-06-07.
Outpatient adjudication remarks (MOA): N30 (patient ineligible for this service).
Payee TJ (federal tax ID): 321822487.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 | $77.16 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $77.16 |  |
| 2 | 97530-GP | 1 | $62.3 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $62.3 |  |
| 3 | 97110-GP | 1 | $50.33 | $0 | PR-27 (Patient Responsibility: expenses incurred after coverage terminated) $50.33 |  |

Line item control numbers (REF 6R): PA24836086L1, PA24836086L2, PA24836086L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: JESSICA HARRIS; MI (member ID) SXA354348278; rendering provider [82]: MICHAEL MARTINEZ; XX (NPI) 1850202042.

## Claim as billed (837P)
Claim PA24836086, total charge $189.79, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M542 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 UN | $77.16 | 2025-06-07 | 1 | PA24836086L1 |
| 2 | 97530-GP | 1 UN | $62.3 | 2025-06-07 | 1 | PA24836086L2 |
| 3 | 97110-GP | 1 UN | $50.33 | 2025-06-07 | 1 | PA24836086L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: KEYSTONE COMMERCIAL HEALTH; 46 (ETIN) 1650284917
- billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; 820 HARBOR VIEW BLVD; TRENTON, NJ, 086100820; EI (employer ID/EIN) 321822487
- insured/subscriber [IL]: JESSICA HARRIS; MI (member ID) SXA354348278; 6774 MAPLE LN; WILMINGTON, DE, 19814
- payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917
- referring provider [DN]: SARAH CHEN; XX (NPI) 1410042904
- rendering provider [82]: MICHAEL MARTINEZ; XX (NPI) 1850202042
- Submission reference TRC80610085, dated 2025-06-18 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2025-06-07.
Inquiry parties: payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: JESSICA HARRIS; MI (member ID) SXA354348278.
Subject DOB 1997-12-11, sex F.

Response:
- benefit: 6 (inactive), coverage level IND, service type 30 (health benefit plan coverage), plan: KEYSTONE COMMERCIAL HEALTH EPO
- plan date (291): 2025-06-07
- eligibility begin (356): 2024-01-01
- eligibility end (357): 2025-05-31
Response parties: payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917; provider [1P]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; insured/subscriber [IL]: JESSICA HARRIS; MI (member ID) SXA354348278.
Subject DOB 1997-12-11, sex F.
Eligibility exchange reference ELG98828578, dated 2025-07-26 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2025-06-18, action code WQ, amount $189.79.
D9 (clearinghouse claim number): TRC80610085.
Trace (2 (referenced transaction trace)): TRC80610085.
received date (050): 2025-06-18.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: RIVERBEND OUTPATIENT THERAPY LLC; 46 (ETIN) 321822487; billing provider [85]: RIVERBEND OUTPATIENT THERAPY LLC; XX (NPI) 1353206904; patient [QC]: JESSICA HARRIS; MI (member ID) SXA354348278.
Acknowledgment reference ACK80610085, dated 2025-06-18 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2025-06-07. Dx: Cervicalgia. 97110 (31 min): therapeutic exercise for strength and ROM. 97530 (15 min): therapeutic activities (dynamic functional tasks). 97110 (16 min): therapeutic exercise for strength and ROM. Total timed minutes: 62. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1353206904 to receiver [ZZ] 1650284917, interchange 534655299 date 250726 time 0800 version 00501 usage P; group HS control 534655299 date 20250726 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1650284917 to receiver [ZZ] 1353206904, interchange 778544970 date 250726 time 0800 version 00501 usage P; group HB control 778544970 date 20250726 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 14
- claim_837p: sender [ZZ] 321822487 to receiver [ZZ] 1650284917, interchange 210601102 date 250618 time 0800 version 00501 usage P; group HC control 210601102 date 20250618 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 321822487, interchange 864726087 date 250618 time 0800 version 00501 usage P; group HN control 864726087 date 20250618 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1650284917 to receiver [ZZ] 1353206904, interchange 688733446 date 250720 time 0800 version 00501 usage P; group HP control 688733446 date 20250720 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
