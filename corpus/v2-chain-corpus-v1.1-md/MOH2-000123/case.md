# Case MOH2-000123

Patient MICHAEL MARTINEZ, DOB 1967-12-25, sex M, member ID HST615122592. Payer: DELAWARE VALLEY MUTUAL. Service date 2026-08-28.

## Adjudication outcome (835)
Claim PA23711000: status 1 (processed as primary, paid). Billed $86.09, paid $14.43, patient responsibility $3.61. Filing indicator CI (commercial insurance). Payer claim control 2627195464715, POS 11 (office), frequency 1 (original claim).
Payment: $14.43 by CHK (check), handling I.
production date (405): 2026-09-28.
Payer [PR]: DELAWARE VALLEY MUTUAL; 900 SHIPLEY RD; WILMINGTON, DE, 198033012; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT569445338, originator 1155019382.
claim statement period start (232): 2026-08-28.
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97112-GP | 1 | $55.43 | $0 | CO-97 (Contractual Obligation: payment included in the allowance for another service, bundled) $55.43 | HE N20 (service not payable with other service rendered on the same date) |
| 2 | 97150-GP | 1 | $30.66 | $14.43 allowed (B6) $18.04 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $12.62; PR-2 (Patient Responsibility: coinsurance amount) $3.61 |  |

Line item control numbers (REF 6R): PA23711000L1, PA23711000L2.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: MICHAEL MARTINEZ; MI (member ID) HST615122592; rendering provider [82]: MARY CLARK; XX (NPI) 1992501921.

## Claim as billed (837P)
Claim PA23711000, total charge $86.09, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M1712 (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97112-GP | 1 UN | $55.43 | 2026-08-28 | 1 | PA23711000L1 |
| 2 | 97150-GP | 1 UN | $30.66 | 2026-08-28 | 1 | PA23711000L2 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: DELAWARE VALLEY MUTUAL; 46 (ETIN) 1550193826
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: MICHAEL MARTINEZ; MI (member ID) HST615122592; 6806 CHESTNUT AVE; TRENTON, NJ, 08691
- payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826
- referring provider [DN]: THOMAS BERGSTROM; XX (NPI) 1179655839
- rendering provider [82]: MARY CLARK; XX (NPI) 1992501921
- Submission reference TRC12552008, dated 2026-09-08 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-08-28.
Inquiry parties: payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: MICHAEL MARTINEZ; MI (member ID) HST615122592.
Subject DOB 1967-12-25, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: DELAWARE VALLEY MUTUAL EPO
- plan date (291): 2026-08-28
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: MICHAEL MARTINEZ; MI (member ID) HST615122592.
Subject DOB 1967-12-25, sex M.
Eligibility exchange reference ELG29659891, dated 2026-10-01 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-09-09, action code WQ, amount $86.09.
D9 (clearinghouse claim number): TRC12552008.
Trace (2 (referenced transaction trace)): TRC12552008.
received date (050): 2026-09-09.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: MICHAEL MARTINEZ; MI (member ID) HST615122592.
Acknowledgment reference ACK12552008, dated 2026-09-09 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-08-28. Dx: Unilateral primary osteoarthritis left knee. 97112 (16 min): neuromuscular re-education of movement and balance. 97150 (untimed, 1 unit): group therapeutic procedure. Total timed minutes: 16. 97112 was performed in a separate 15-minute session from 97150, directed at a distinct body region with a distinct goal; services were not integral to one another. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1550193826, interchange 571275498 date 261001 time 0800 version 00501 usage P; group HS control 571275498 date 20261001 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1550193826 to receiver [ZZ] 1110692305, interchange 818530720 date 261001 time 0800 version 00501 usage P; group HB control 818530720 date 20261001 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1550193826, interchange 795488152 date 260908 time 0800 version 00501 usage P; group HC control 795488152 date 20260908 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 388815250 date 260909 time 0800 version 00501 usage P; group HN control 388815250 date 20260909 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1550193826 to receiver [ZZ] 1110692305, interchange 569445338 date 260928 time 0800 version 00501 usage P; group HP control 569445338 date 20260928 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 29
