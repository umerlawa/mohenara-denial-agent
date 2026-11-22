# Case MOH2-000720

Patient SUSAN HARRIS, DOB 1984-01-09, sex F, member ID LCW593288174. Payer: DELAWARE VALLEY MUTUAL. Service date 2025-09-24.

## Adjudication outcome (835)
Claim PA24881310: status 1 (processed as primary, paid). Billed $105.67, paid $51.31, patient responsibility $12.82. Filing indicator CI (commercial insurance). Payer claim control 2530798243990, POS 11 (office), frequency 1 (original claim).
Payment: $51.31 by CHK (check), handling I.
production date (405): 2025-11-03.
Payer [PR]: DELAWARE VALLEY MUTUAL; 900 SHIPLEY RD; WILMINGTON, DE, 198033012; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT343772035, originator 1155019382.
claim statement period start (232): 2025-09-24.
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $51.47 | $23.25 allowed (B6) $29.06 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $22.41; PR-2 (Patient Responsibility: coinsurance amount) $5.81 |  |
| 2 | 97530-GP | 1 | $54.2 | $28.06 allowed (B6) $35.07 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $19.13; PR-2 (Patient Responsibility: coinsurance amount) $7.01 |  |

Line item control numbers (REF 6R): PA24881310L1, PA24881310L2.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: SUSAN HARRIS; MI (member ID) LCW593288174; rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273.

## Claim as billed (837P)
Claim PA24881310, total charge $105.67, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $51.47 | 2025-09-24 | 1 | PA24881310L1 |
| 2 | 97530-GP | 1 UN | $54.2 | 2025-09-24 | 1 | PA24881310L2 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: DELAWARE VALLEY MUTUAL; 46 (ETIN) 1550193826
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: SUSAN HARRIS; MI (member ID) LCW593288174; 1018 FRANKLIN ST; TRENTON, NJ, 08680
- payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826
- referring provider [DN]: DANIEL OKAFOR; XX (NPI) 1230067602
- rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273
- Submission reference TRC66242699, dated 2025-10-10 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2025-09-24.
Inquiry parties: payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: SUSAN HARRIS; MI (member ID) LCW593288174.
Subject DOB 1984-01-09, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: DELAWARE VALLEY MUTUAL EPO
- plan date (291): 2025-09-24
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: SUSAN HARRIS; MI (member ID) LCW593288174.
Subject DOB 1984-01-09, sex F.
Eligibility exchange reference ELG22821171, dated 2025-11-08 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2025-10-11, action code WQ, amount $105.67.
D9 (clearinghouse claim number): TRC66242699.
Trace (2 (referenced transaction trace)): TRC66242699.
received date (050): 2025-10-11.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: SUSAN HARRIS; MI (member ID) LCW593288174.
Acknowledgment reference ACK66242699, dated 2025-10-11 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2025-09-24. Dx: Aftercare following joint replacement surgery. 97110 (14 min): therapeutic exercise for strength and ROM. 97530 (14 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 28. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1550193826, interchange 788126624 date 251108 time 0800 version 00501 usage P; group HS control 788126624 date 20251108 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1550193826 to receiver [ZZ] 1110692305, interchange 448980596 date 251108 time 0800 version 00501 usage P; group HB control 448980596 date 20251108 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1550193826, interchange 984460857 date 251010 time 0800 version 00501 usage P; group HC control 984460857 date 20251010 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 550778061 date 251011 time 0800 version 00501 usage P; group HN control 550778061 date 20251011 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1550193826 to receiver [ZZ] 1110692305, interchange 343772035 date 251103 time 0800 version 00501 usage P; group HP control 343772035 date 20251103 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 30
