# Case MOH2-000026

Patient CHARLES JACKSON, DOB 1941-03-21, sex M, member ID AUB396990887. Payer: DELAWARE VALLEY MUTUAL. Service date 2026-02-13.

## Adjudication outcome (835)
Claim PA26408061: status 4 (denied). Billed $250.44, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2607967498154, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-03-20.
Payer [PR]: DELAWARE VALLEY MUTUAL; 900 SHIPLEY RD; WILMINGTON, DE, 198033012; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT881322953, originator 1155019382.
claim statement period start (232): 2026-02-13.
Outpatient adjudication remarks (MOA): MA04 (secondary payment cannot be considered without primary payer identity).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $52.03 | $0 | CO-22 (Contractual Obligation: care may be covered by another payer per coordination of benefits) $52.03 |  |
| 2 | 97140-GP | 1 | $49.49 | $0 | CO-22 (Contractual Obligation: care may be covered by another payer per coordination of benefits) $49.49 |  |
| 3 | 97530-GP | 2 | $103.41 | $0 | CO-22 (Contractual Obligation: care may be covered by another payer per coordination of benefits) $103.41 |  |
| 4 | 97112-GP | 1 | $45.51 | $0 | CO-22 (Contractual Obligation: care may be covered by another payer per coordination of benefits) $45.51 |  |

Line item control numbers (REF 6R): PA26408061L1, PA26408061L2, PA26408061L3, PA26408061L4.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: CHARLES JACKSON; MI (member ID) AUB396990887; rendering provider [82]: NANCY LEWIS; XX (NPI) 1913425846.

## Claim as billed (837P)
Claim PA26408061, total charge $250.44, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $52.03 | 2026-02-13 | 1 | PA26408061L1 |
| 2 | 97140-GP | 1 UN | $49.49 | 2026-02-13 | 1 | PA26408061L2 |
| 3 | 97530-GP | 2 UN | $103.41 | 2026-02-13 | 1 | PA26408061L3 |
| 4 | 97112-GP | 1 UN | $45.51 | 2026-02-13 | 1 | PA26408061L4 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: DELAWARE VALLEY MUTUAL; 46 (ETIN) 1550193826
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: CHARLES JACKSON; MI (member ID) AUB396990887; 7320 CHESTNUT LN; STATEN ISLAND, NY, 10361
- payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826
- referring provider [DN]: SARAH CHEN; XX (NPI) 1410042904
- rendering provider [82]: NANCY LEWIS; XX (NPI) 1913425846
- Submission reference TRC17452067, dated 2026-02-25 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-02-13.
Inquiry parties: payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: CHARLES JACKSON; MI (member ID) AUB396990887.
Subject DOB 1941-03-21, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: DELAWARE VALLEY MUTUAL HMO
- benefit: R (other or additional payer), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-02-13
- eligibility begin (356): 2024-01-01
- eligibility begin (356): 2024-01-01
- payer message: PLAN IS PRIMARY PAYER FOR THIS MEMBER
Response parties: payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: CHARLES JACKSON; MI (member ID) AUB396990887; payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352.
Subject DOB 1941-03-21, sex M.
Eligibility exchange reference ELG15090921, dated 2026-03-21 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-02-26, action code WQ, amount $250.44.
D9 (clearinghouse claim number): TRC17452067.
Trace (2 (referenced transaction trace)): TRC17452067.
received date (050): 2026-02-26.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: CHARLES JACKSON; MI (member ID) AUB396990887.
Acknowledgment reference ACK17452067, dated 2026-02-26 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-02-13. Dx: Aftercare following joint replacement surgery. 97110 (14 min): therapeutic exercise for strength and ROM. 97140 (14 min): manual therapy (soft tissue and joint mobilization). 97530 (29 min): therapeutic activities (dynamic functional tasks). 97112 (15 min): neuromuscular re-education of movement and balance. Total timed minutes: 72. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1550193826, interchange 922097040 date 260321 time 0800 version 00501 usage P; group HS control 922097040 date 20260321 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1550193826 to receiver [ZZ] 1110692305, interchange 870231264 date 260321 time 0800 version 00501 usage P; group HB control 870231264 date 20260321 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 17
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1550193826, interchange 886274611 date 260225 time 0800 version 00501 usage P; group HC control 886274611 date 20260225 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 38
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 168244756 date 260226 time 0800 version 00501 usage P; group HN control 168244756 date 20260226 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1550193826 to receiver [ZZ] 1110692305, interchange 881322953 date 260320 time 0800 version 00501 usage P; group HP control 881322953 date 20260320 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 35
