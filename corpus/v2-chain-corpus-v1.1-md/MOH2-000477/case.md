# Case MOH2-000477

Patient SUSAN HARRIS, DOB 1984-01-09, sex F, member ID LCW593288174. Payer: DELAWARE VALLEY MUTUAL. Service date 2025-02-19.

## Adjudication outcome (835)
Claim PA29292675: status 1 (processed as primary, paid). Billed $150.57, paid $75.62, patient responsibility $18.9. Filing indicator CI (commercial insurance). Payer claim control 2506961196993, POS 11 (office), frequency 1 (original claim).
Payment: $75.62 by CHK (check), handling I.
production date (405): 2025-03-10.
Payer [PR]: DELAWARE VALLEY MUTUAL; 900 SHIPLEY RD; WILMINGTON, DE, 198033012; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT297518869, originator 1155019382.
claim statement period start (232): 2025-02-19.
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $38.62 | $23.25 allowed (B6) $29.06 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $9.56; PR-2 (Patient Responsibility: coinsurance amount) $5.81 |  |
| 2 | 97112-GP | 2 | $111.95 | $52.37 allowed (B6) $65.46 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $46.49; PR-2 (Patient Responsibility: coinsurance amount) $13.09 |  |

Line item control numbers (REF 6R): PA29292675L1, PA29292675L2.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: SUSAN HARRIS; MI (member ID) LCW593288174; rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273.

## Claim as billed (837P)
Claim PA29292675, total charge $150.57, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $38.62 | 2025-02-19 | 1 | PA29292675L1 |
| 2 | 97112-GP | 2 UN | $111.95 | 2025-02-19 | 1 | PA29292675L2 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: DELAWARE VALLEY MUTUAL; 46 (ETIN) 1550193826
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: SUSAN HARRIS; MI (member ID) LCW593288174; 1018 FRANKLIN ST; TRENTON, NJ, 08680
- payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826
- referring provider [DN]: DANIEL OKAFOR; XX (NPI) 1230067602
- rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273
- Submission reference TRC82275021, dated 2025-02-23 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2025-02-19.
Inquiry parties: payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: SUSAN HARRIS; MI (member ID) LCW593288174.
Subject DOB 1984-01-09, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: DELAWARE VALLEY MUTUAL EPO
- plan date (291): 2025-02-19
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: SUSAN HARRIS; MI (member ID) LCW593288174.
Subject DOB 1984-01-09, sex F.
Eligibility exchange reference ELG48521116, dated 2025-03-11 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2025-02-23, action code WQ, amount $150.57.
D9 (clearinghouse claim number): TRC82275021.
Trace (2 (referenced transaction trace)): TRC82275021.
received date (050): 2025-02-23.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: SUSAN HARRIS; MI (member ID) LCW593288174.
Acknowledgment reference ACK82275021, dated 2025-02-23 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2025-02-19. Dx: Aftercare following joint replacement surgery. 97110 (16 min): therapeutic exercise for strength and ROM. 97112 (31 min): neuromuscular re-education of movement and balance. Total timed minutes: 47. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1550193826, interchange 859130266 date 250311 time 0800 version 00501 usage P; group HS control 859130266 date 20250311 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1550193826 to receiver [ZZ] 1110692305, interchange 985162449 date 250311 time 0800 version 00501 usage P; group HB control 985162449 date 20250311 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1550193826, interchange 429739807 date 250223 time 0800 version 00501 usage P; group HC control 429739807 date 20250223 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 674353713 date 250223 time 0800 version 00501 usage P; group HN control 674353713 date 20250223 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1550193826 to receiver [ZZ] 1110692305, interchange 297518869 date 250310 time 0800 version 00501 usage P; group HP control 297518869 date 20250310 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 30
