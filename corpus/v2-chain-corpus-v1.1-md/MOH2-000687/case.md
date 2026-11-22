# Case MOH2-000687

Patient SUSAN HARRIS, DOB 1984-01-09, sex F, member ID LCW593288174. Payer: DELAWARE VALLEY MUTUAL. Service date 2025-01-20.

## Adjudication outcome (835)
Claim PA27568939: status 4 (denied). Billed $173.26, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2515612725445, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2025-06-05.
Payer [PR]: DELAWARE VALLEY MUTUAL; 900 SHIPLEY RD; WILMINGTON, DE, 198033012; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT828767837, originator 1155019382.
claim statement period start (232): 2025-01-20.
Outpatient adjudication remarks (MOA): N211 (you may not appeal this decision).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $39.27 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $39.27 |  |
| 2 | 97140-GP | 1 | $41.83 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $41.83 |  |
| 3 | 97530-GP | 2 | $92.16 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $92.16 |  |

Line item control numbers (REF 6R): PA27568939L1, PA27568939L2, PA27568939L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: SUSAN HARRIS; MI (member ID) LCW593288174; rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273.

## Claim as billed (837P)
Claim PA27568939, total charge $173.26, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $39.27 | 2025-01-20 | 1 | PA27568939L1 |
| 2 | 97140-GP | 1 UN | $41.83 | 2025-01-20 | 1 | PA27568939L2 |
| 3 | 97530-GP | 2 UN | $92.16 | 2025-01-20 | 1 | PA27568939L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: DELAWARE VALLEY MUTUAL; 46 (ETIN) 1550193826
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: SUSAN HARRIS; MI (member ID) LCW593288174; 1018 FRANKLIN ST; TRENTON, NJ, 08680
- payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826
- referring provider [DN]: DANIEL OKAFOR; XX (NPI) 1230067602
- rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273
- Submission reference TRC85297429, dated 2025-05-07 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2025-01-20.
Inquiry parties: payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: SUSAN HARRIS; MI (member ID) LCW593288174.
Subject DOB 1984-01-09, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: DELAWARE VALLEY MUTUAL EPO
- plan date (291): 2025-01-20
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: SUSAN HARRIS; MI (member ID) LCW593288174.
Subject DOB 1984-01-09, sex F.
Eligibility exchange reference ELG39275793, dated 2025-06-06 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2025-02-05, action code WQ, amount $173.26.
D9 (clearinghouse claim number): TRC85297429.
Trace (2 (referenced transaction trace)): TRC85297429.
received date (050): 2025-02-05.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: SUSAN HARRIS; MI (member ID) LCW593288174.
Acknowledgment reference ACK85297429, dated 2025-02-05 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2025-01-20. Dx: Aftercare following joint replacement surgery. 97110 (15 min): therapeutic exercise for strength and ROM. 97140 (14 min): manual therapy (soft tissue and joint mobilization). 97530 (29 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 58. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1550193826, interchange 652673096 date 250606 time 0800 version 00501 usage P; group HS control 652673096 date 20250606 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1550193826 to receiver [ZZ] 1110692305, interchange 258643333 date 250606 time 0800 version 00501 usage P; group HB control 258643333 date 20250606 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1550193826, interchange 860400531 date 250507 time 0800 version 00501 usage P; group HC control 860400531 date 20250507 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 923159287 date 250205 time 0800 version 00501 usage P; group HN control 923159287 date 20250205 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1550193826 to receiver [ZZ] 1110692305, interchange 828767837 date 250605 time 0800 version 00501 usage P; group HP control 828767837 date 20250605 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
