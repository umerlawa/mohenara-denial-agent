# Case MOH2-000391

Patient CHARLES JACKSON, DOB 1941-03-21, sex M, member ID AUB396990887. Payer: DELAWARE VALLEY MUTUAL. Service date 2026-01-31.

## Adjudication outcome (835)
Claim PA22735091: status 4 (denied). Billed $241.92, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2607366031552, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-03-14.
Payer [PR]: DELAWARE VALLEY MUTUAL; 900 SHIPLEY RD; WILMINGTON, DE, 198033012; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT103703434, originator 1155019382.
claim statement period start (232): 2026-01-31.
Outpatient adjudication remarks (MOA): MA04 (secondary payment cannot be considered without primary payer identity).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $49.25 | $0 | CO-22 (Contractual Obligation: care may be covered by another payer per coordination of benefits) $49.25 |  |
| 2 | 97112-GP | 1 | $45.17 | $0 | CO-22 (Contractual Obligation: care may be covered by another payer per coordination of benefits) $45.17 |  |
| 3 | 97140-GP | 1 | $41.59 | $0 | CO-22 (Contractual Obligation: care may be covered by another payer per coordination of benefits) $41.59 |  |
| 4 | 97530-GP | 1 | $52.85 | $0 | CO-22 (Contractual Obligation: care may be covered by another payer per coordination of benefits) $52.85 |  |
| 5 | 97535-GP | 1 | $53.06 | $0 | CO-22 (Contractual Obligation: care may be covered by another payer per coordination of benefits) $53.06 |  |

Line item control numbers (REF 6R): PA22735091L1, PA22735091L2, PA22735091L3, PA22735091L4, PA22735091L5.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: CHARLES JACKSON; MI (member ID) AUB396990887; rendering provider [82]: NANCY LEWIS; XX (NPI) 1913425846.

## Claim as billed (837P)
Claim PA22735091, total charge $241.92, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $49.25 | 2026-01-31 | 1 | PA22735091L1 |
| 2 | 97112-GP | 1 UN | $45.17 | 2026-01-31 | 1 | PA22735091L2 |
| 3 | 97140-GP | 1 UN | $41.59 | 2026-01-31 | 1 | PA22735091L3 |
| 4 | 97530-GP | 1 UN | $52.85 | 2026-01-31 | 1 | PA22735091L4 |
| 5 | 97535-GP | 1 UN | $53.06 | 2026-01-31 | 1 | PA22735091L5 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: DELAWARE VALLEY MUTUAL; 46 (ETIN) 1550193826
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: CHARLES JACKSON; MI (member ID) AUB396990887; 7320 CHESTNUT LN; STATEN ISLAND, NY, 10361
- payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826
- referring provider [DN]: SARAH CHEN; XX (NPI) 1410042904
- rendering provider [82]: NANCY LEWIS; XX (NPI) 1913425846
- Submission reference TRC15340989, dated 2026-02-08 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-01-31.
Inquiry parties: payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: CHARLES JACKSON; MI (member ID) AUB396990887.
Subject DOB 1941-03-21, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: DELAWARE VALLEY MUTUAL HMO
- benefit: R (other or additional payer), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-01-31
- eligibility begin (356): 2024-01-01
- eligibility begin (356): 2024-01-01
- payer message: PLAN IS PRIMARY PAYER FOR THIS MEMBER
Response parties: payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: CHARLES JACKSON; MI (member ID) AUB396990887; payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352.
Subject DOB 1941-03-21, sex M.
Eligibility exchange reference ELG21893653, dated 2026-03-17 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-02-10, action code WQ, amount $241.92.
D9 (clearinghouse claim number): TRC15340989.
Trace (2 (referenced transaction trace)): TRC15340989.
received date (050): 2026-02-10.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: CHARLES JACKSON; MI (member ID) AUB396990887.
Acknowledgment reference ACK15340989, dated 2026-02-10 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-01-31. Dx: Aftercare following joint replacement surgery. 97110 (14 min): therapeutic exercise for strength and ROM. 97112 (15 min): neuromuscular re-education of movement and balance. 97140 (16 min): manual therapy (soft tissue and joint mobilization). 97530 (15 min): therapeutic activities (dynamic functional tasks). 97535 (15 min): self-care/home management training. Total timed minutes: 75. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1550193826, interchange 914986037 date 260317 time 0800 version 00501 usage P; group HS control 914986037 date 20260317 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1550193826 to receiver [ZZ] 1110692305, interchange 580568871 date 260317 time 0800 version 00501 usage P; group HB control 580568871 date 20260317 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 17
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1550193826, interchange 928072242 date 260208 time 0800 version 00501 usage P; group HC control 928072242 date 20260208 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 42
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 819097977 date 260210 time 0800 version 00501 usage P; group HN control 819097977 date 20260210 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1550193826 to receiver [ZZ] 1110692305, interchange 103703434 date 260314 time 0800 version 00501 usage P; group HP control 103703434 date 20260314 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 39
