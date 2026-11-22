# Case MOH2-000087

Patient RICHARD LOPEZ, DOB 1955-08-08, sex M, member ID KSF583282882. Payer: KEYSTONE COMMERCIAL HEALTH. Service date 2026-01-05.

## Adjudication outcome (835)
Claim PA25096142: status 4 (denied). Billed $146.15, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2605044123904, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-02-19.
Payer [PR]: KEYSTONE COMMERCIAL HEALTH; 1200 MARKET ST; PHILADELPHIA, PA, 191071200; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT960716139, originator 1165028491.
claim statement period start (232): 2026-01-05.
Outpatient adjudication remarks (MOA): MA04 (secondary payment cannot be considered without primary payer identity).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $47.45 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $47.45 |  |
| 2 | 97140-GP | 1 | $45.49 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $45.49 |  |
| 3 | 97530-GP | 1 | $53.21 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $53.21 |  |

Line item control numbers (REF 6R): PA25096142L1, PA25096142L2, PA25096142L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: RICHARD LOPEZ; MI (member ID) KSF583282882; rendering provider [82]: MARY CLARK; XX (NPI) 1992501921.

## Claim as billed (837P)
Claim PA25096142, total charge $146.15, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $47.45 | 2026-01-05 | 1 | PA25096142L1 |
| 2 | 97140-GP | 1 UN | $45.49 | 2026-01-05 | 1 | PA25096142L2 |
| 3 | 97530-GP | 1 UN | $53.21 | 2026-01-05 | 1 | PA25096142L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: KEYSTONE COMMERCIAL HEALTH; 46 (ETIN) 1650284917
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: RICHARD LOPEZ; MI (member ID) KSF583282882; 9081 CHESTNUT RD; TRENTON, NJ, 08677
- payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917
- referring provider [DN]: MARCUS WEBB; XX (NPI) 1583494452
- rendering provider [82]: MARY CLARK; XX (NPI) 1992501921
- Submission reference TRC19714515, dated 2026-01-18 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-01-05.
Inquiry parties: payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: RICHARD LOPEZ; MI (member ID) KSF583282882.
Subject DOB 1955-08-08, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: KEYSTONE COMMERCIAL HEALTH HMO
- benefit: R (other or additional payer), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-01-05
- eligibility begin (356): 2024-01-01
- eligibility begin (356): 2024-01-01
- payer message: PLAN IS PRIMARY PAYER FOR THIS MEMBER
Response parties: payer [PR]: KEYSTONE COMMERCIAL HEALTH; PI (payer ID) 1650284917; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: RICHARD LOPEZ; MI (member ID) KSF583282882; payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352.
Subject DOB 1955-08-08, sex M.
Eligibility exchange reference ELG41377020, dated 2026-02-20 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-01-18, action code WQ, amount $146.15.
D9 (clearinghouse claim number): TRC19714515.
Trace (2 (referenced transaction trace)): TRC19714515.
received date (050): 2026-01-18.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: RICHARD LOPEZ; MI (member ID) KSF583282882.
Acknowledgment reference ACK19714515, dated 2026-01-18 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-01-05. Dx: Aftercare following joint replacement surgery. 97110 (16 min): therapeutic exercise for strength and ROM. 97140 (14 min): manual therapy (soft tissue and joint mobilization). 97530 (14 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 44. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1650284917, interchange 605204680 date 260220 time 0800 version 00501 usage P; group HS control 605204680 date 20260220 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1650284917 to receiver [ZZ] 1110692305, interchange 573076593 date 260220 time 0800 version 00501 usage P; group HB control 573076593 date 20260220 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 17
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1650284917, interchange 667547872 date 260118 time 0800 version 00501 usage P; group HC control 667547872 date 20260118 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 836130417 date 260118 time 0800 version 00501 usage P; group HN control 836130417 date 20260118 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1650284917 to receiver [ZZ] 1110692305, interchange 960716139 date 260219 time 0800 version 00501 usage P; group HP control 960716139 date 20260219 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
