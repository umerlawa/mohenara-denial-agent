# Case MOH2-000633

Patient SUSAN HARRIS, DOB 1984-01-09, sex F, member ID LCW593288174. Payer: DELAWARE VALLEY MUTUAL. Service date 2025-09-29.

## Adjudication outcome (835)
Claim PA26606939: status 1 (processed as primary, paid). Billed $261.23, paid $14.43, patient responsibility $3.61. Filing indicator CI (commercial insurance). Payer claim control 2531817516445, POS 11 (office), frequency 1 (original claim).
Payment: $14.43 by CHK (check), handling I.
production date (405): 2025-11-14.
Payer [PR]: DELAWARE VALLEY MUTUAL; 900 SHIPLEY RD; WILMINGTON, DE, 198033012; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT958445279, originator 1155019382.
claim statement period start (232): 2025-09-29.
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97530-GP | 2 | $120.22 | $0 | CO-97 (Contractual Obligation: payment included in the allowance for another service, bundled) $120.22 | HE N20 (service not payable with other service rendered on the same date) |
| 2 | 97150-GP | 1 | $29.43 | $14.43 allowed (B6) $18.04 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $11.39; PR-2 (Patient Responsibility: coinsurance amount) $3.61 |  |
| 3 | 97530-GP | 2 | $111.58 | $0 | CO-97 (Contractual Obligation: payment included in the allowance for another service, bundled) $111.58 | HE N20 (service not payable with other service rendered on the same date) |

Line item control numbers (REF 6R): PA26606939L1, PA26606939L2, PA26606939L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: SUSAN HARRIS; MI (member ID) LCW593288174; rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273.

## Claim as billed (837P)
Claim PA26606939, total charge $261.23, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97530-GP | 2 UN | $120.22 | 2025-09-29 | 1 | PA26606939L1 |
| 2 | 97150-GP | 1 UN | $29.43 | 2025-09-29 | 1 | PA26606939L2 |
| 3 | 97530-GP | 2 UN | $111.58 | 2025-09-29 | 1 | PA26606939L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: DELAWARE VALLEY MUTUAL; 46 (ETIN) 1550193826
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: SUSAN HARRIS; MI (member ID) LCW593288174; 1018 FRANKLIN ST; TRENTON, NJ, 08680
- payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826
- referring provider [DN]: DANIEL OKAFOR; XX (NPI) 1230067602
- rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273
- Submission reference TRC90816569, dated 2025-10-19 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2025-09-29.
Inquiry parties: payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: SUSAN HARRIS; MI (member ID) LCW593288174.
Subject DOB 1984-01-09, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: DELAWARE VALLEY MUTUAL EPO
- plan date (291): 2025-09-29
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: SUSAN HARRIS; MI (member ID) LCW593288174.
Subject DOB 1984-01-09, sex F.
Eligibility exchange reference ELG39950998, dated 2025-11-15 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2025-10-21, action code WQ, amount $261.23.
D9 (clearinghouse claim number): TRC90816569.
Trace (2 (referenced transaction trace)): TRC90816569.
received date (050): 2025-10-21.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: SUSAN HARRIS; MI (member ID) LCW593288174.
Acknowledgment reference ACK90816569, dated 2025-10-21 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2025-09-29. Dx: Aftercare following joint replacement surgery. 97530 (30 min): therapeutic activities (dynamic functional tasks). 97150 (untimed, 1 unit): group therapeutic procedure. 97530 (29 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 59. 97530 was delivered in its own treatment block after a rest break, targeting a different body region than 97150 and addressing a separate functional goal. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1550193826, interchange 260237799 date 251115 time 0800 version 00501 usage P; group HS control 260237799 date 20251115 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1550193826 to receiver [ZZ] 1110692305, interchange 306166796 date 251115 time 0800 version 00501 usage P; group HB control 306166796 date 20251115 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1550193826, interchange 991458237 date 251019 time 0800 version 00501 usage P; group HC control 991458237 date 20251019 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 531730834 date 251021 time 0800 version 00501 usage P; group HN control 531730834 date 20251021 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1550193826 to receiver [ZZ] 1110692305, interchange 958445279 date 251114 time 0800 version 00501 usage P; group HP control 958445279 date 20251114 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 34
