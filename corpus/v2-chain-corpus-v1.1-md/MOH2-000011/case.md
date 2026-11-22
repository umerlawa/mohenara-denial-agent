# Case MOH2-000011

Patient RICHARD LOPEZ, DOB 1955-08-08, sex M, member ID KSF583282882. Payer: KEYSTONE COMMERCIAL HEALTH. Service date 2026-01-25.

## Adjudication outcome (835)
Claim PA29796850: status 4 (denied). Billed $226.17, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2608045324532, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-03-21.
Payer [PR]: KEYSTONE COMMERCIAL HEALTH; 1200 MARKET ST; PHILADELPHIA, PA, 191071200; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT122682149, originator 1165028491.
claim statement period start (232): 2026-01-25.
Outpatient adjudication remarks (MOA): MA04 (secondary payment cannot be considered without primary payer identity).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 | $76.63 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $76.63 |  |
| 2 | 97112-GP | 2 | $110.93 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $110.93 |  |
| 3 | 97140-GP | 1 | $38.61 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $38.61 |  |

Line item control numbers (REF 6R): PA29796850L1, PA29796850L2, PA29796850L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: RICHARD LOPEZ; MI (member ID) KSF583282882; rendering provider [82]: MARY CLARK; XX (NPI) 1992501921.

## Claim as billed (837P)
Claim PA29796850, total charge $226.17, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 UN | $76.63 | 2026-01-25 | 1 | PA29796850L1 |
| 2 | 97112-GP | 2 UN | $110.93 | 2026-01-25 | 1 | PA29796850L2 |
| 3 | 97140-GP | 1 UN | $38.61 | 2026-01-25 | 1 | PA29796850L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: KEYSTONE COMMERCIAL HEALTH; 46 (ETIN) 1650284917
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: RICHARD LOPEZ; MI (member ID) KSF583282882; 9081 CHESTNUT RD; TRENTON, NJ, 08677
- payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917
- referring provider [DN]: MARCUS WEBB; XX (NPI) 1583494452
- rendering provider [82]: MARY CLARK; XX (NPI) 1992501921
- Submission reference TRC98725775, dated 2026-02-13 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-01-25.
Inquiry parties: payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: RICHARD LOPEZ; MI (member ID) KSF583282882.
Subject DOB 1955-08-08, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: KEYSTONE COMMERCIAL HEALTH HMO
- benefit: R (other or additional payer), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-01-25
- eligibility begin (356): 2024-01-01
- eligibility begin (356): 2024-01-01
- payer message: PLAN IS PRIMARY PAYER FOR THIS MEMBER
Response parties: payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: RICHARD LOPEZ; MI (member ID) KSF583282882; payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352.
Subject DOB 1955-08-08, sex M.
Eligibility exchange reference ELG88689579, dated 2026-03-22 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-02-14, action code WQ, amount $226.17.
D9 (clearinghouse claim number): TRC98725775.
Trace (2 (referenced transaction trace)): TRC98725775.
received date (050): 2026-02-14.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: RICHARD LOPEZ; MI (member ID) KSF583282882.
Acknowledgment reference ACK98725775, dated 2026-02-14 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-01-25. Dx: Aftercare following joint replacement surgery. 97110 (31 min): therapeutic exercise for strength and ROM. 97112 (31 min): neuromuscular re-education of movement and balance. 97140 (14 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 76. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1650284917, interchange 625223058 date 260322 time 0800 version 00501 usage P; group HS control 625223058 date 20260322 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1650284917 to receiver [ZZ] 1110692305, interchange 606088486 date 260322 time 0800 version 00501 usage P; group HB control 606088486 date 20260322 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 17
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1650284917, interchange 246619664 date 260213 time 0800 version 00501 usage P; group HC control 246619664 date 20260213 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 203842046 date 260214 time 0800 version 00501 usage P; group HN control 203842046 date 20260214 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1650284917 to receiver [ZZ] 1110692305, interchange 122682149 date 260321 time 0800 version 00501 usage P; group HP control 122682149 date 20260321 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
