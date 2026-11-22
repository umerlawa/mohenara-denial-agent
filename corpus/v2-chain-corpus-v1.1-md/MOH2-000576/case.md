# Case MOH2-000576

Patient SUSAN HARRIS, DOB 1984-01-09, sex F, member ID LCW593288174. Payer: DELAWARE VALLEY MUTUAL. Service date 2025-10-07.

## Adjudication outcome (835)
Claim PA26390375: status 4 (denied). Billed $131.4, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2531447020354, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2025-11-10.
Payer [PR]: DELAWARE VALLEY MUTUAL; 900 SHIPLEY RD; WILMINGTON, DE, 198033012; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT752323294, originator 1155019382.
claim statement period start (232): 2025-10-07.
Outpatient adjudication remarks (MOA): N30 (patient ineligible for this service).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97112-GP | 1 | $47.81 | $0 | CO-27 (Contractual Obligation: expenses incurred after coverage terminated) $47.81 |  |
| 2 | 97116-GP | 1 | $43.04 | $0 | CO-27 (Contractual Obligation: expenses incurred after coverage terminated) $43.04 |  |
| 3 | 97140-GP | 1 | $40.55 | $0 | CO-27 (Contractual Obligation: expenses incurred after coverage terminated) $40.55 |  |

Line item control numbers (REF 6R): PA26390375L1, PA26390375L2, PA26390375L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: SUSAN HARRIS; MI (member ID) LCW593288174; rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273.

## Claim as billed (837P)
Claim PA26390375, total charge $131.4, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97112-GP | 1 UN | $47.81 | 2025-10-07 | 1 | PA26390375L1 |
| 2 | 97116-GP | 1 UN | $43.04 | 2025-10-07 | 1 | PA26390375L2 |
| 3 | 97140-GP | 1 UN | $40.55 | 2025-10-07 | 1 | PA26390375L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: DELAWARE VALLEY MUTUAL; 46 (ETIN) 1550193826
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: SUSAN HARRIS; MI (member ID) LCW593288174; 1018 FRANKLIN ST; TRENTON, NJ, 08680
- payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826
- referring provider [DN]: DANIEL OKAFOR; XX (NPI) 1230067602
- rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273
- Submission reference TRC89662644, dated 2025-10-18 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2025-10-07.
Inquiry parties: payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: SUSAN HARRIS; MI (member ID) LCW593288174.
Subject DOB 1984-01-09, sex F.

Response:
- benefit: 6 (inactive), coverage level IND, service type 30 (health benefit plan coverage), plan: DELAWARE VALLEY MUTUAL EPO
- plan date (291): 2025-10-07
- eligibility begin (356): 2024-01-01
- eligibility end (357): 2025-09-30
Response parties: payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: SUSAN HARRIS; MI (member ID) LCW593288174.
Subject DOB 1984-01-09, sex F.
Eligibility exchange reference ELG77173284, dated 2025-11-12 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2025-10-20, action code WQ, amount $131.4.
D9 (clearinghouse claim number): TRC89662644.
Trace (2 (referenced transaction trace)): TRC89662644.
received date (050): 2025-10-20.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: SUSAN HARRIS; MI (member ID) LCW593288174.
Acknowledgment reference ACK89662644, dated 2025-10-20 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2025-10-07. Dx: Aftercare following joint replacement surgery. 97112 (14 min): neuromuscular re-education of movement and balance. 97116 (16 min): gait training with assistive device progression. 97140 (15 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 45. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1550193826, interchange 681643003 date 251112 time 0800 version 00501 usage P; group HS control 681643003 date 20251112 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1550193826 to receiver [ZZ] 1110692305, interchange 928137913 date 251112 time 0800 version 00501 usage P; group HB control 928137913 date 20251112 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 14
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1550193826, interchange 157771784 date 251018 time 0800 version 00501 usage P; group HC control 157771784 date 20251018 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 740823825 date 251020 time 0800 version 00501 usage P; group HN control 740823825 date 20251020 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1550193826 to receiver [ZZ] 1110692305, interchange 752323294 date 251110 time 0800 version 00501 usage P; group HP control 752323294 date 20251110 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
