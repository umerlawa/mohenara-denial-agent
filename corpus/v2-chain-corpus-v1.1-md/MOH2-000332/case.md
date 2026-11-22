# Case MOH2-000332

Patient JESSICA HARRIS, DOB 1957-08-08, sex M, member ID VMC906648227. Payer: GARDEN STATE BENEFIT TRUST. Service date 2026-01-13.

## Adjudication outcome (835)
Claim PA23605431: status 4 (denied). Billed $237.38, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2605064685818, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-02-19.
Payer [PR]: GARDEN STATE BENEFIT TRUST; 210 RARITAN PLAZA; EDISON, NJ, 088373105; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT629940139, originator 1145082736.
claim statement period start (232): 2026-01-13.
Outpatient adjudication remarks (MOA): MA04 (secondary payment cannot be considered without primary payer identity).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 | $94.94 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $94.94 |  |
| 2 | 97112-GP | 2 | $94.01 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $94.01 |  |
| 3 | 97140-GP | 1 | $48.43 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $48.43 |  |

Line item control numbers (REF 6R): PA23605431L1, PA23605431L2, PA23605431L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: JESSICA HARRIS; MI (member ID) VMC906648227; rendering provider [82]: MARY CLARK; XX (NPI) 1992501921.

## Claim as billed (837P)
Claim PA23605431, total charge $237.38, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 UN | $94.94 | 2026-01-13 | 1 | PA23605431L1 |
| 2 | 97112-GP | 2 UN | $94.01 | 2026-01-13 | 1 | PA23605431L2 |
| 3 | 97140-GP | 1 UN | $48.43 | 2026-01-13 | 1 | PA23605431L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: GARDEN STATE BENEFIT TRUST; 46 (ETIN) 1450827364
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: JESSICA HARRIS; MI (member ID) VMC906648227; 9631 OAK ST; TRENTON, NJ, 08668
- payer [PR]: GARDEN STATE BENEFIT TRUST; PI (payer ID) 1450827364
- referring provider [DN]: DANIEL OKAFOR; XX (NPI) 1230067602
- rendering provider [82]: MARY CLARK; XX (NPI) 1992501921
- Submission reference TRC67588079, dated 2026-01-16 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-01-13.
Inquiry parties: payer [PR]: GARDEN STATE BENEFIT TRUST; PI (payer ID) 1450827364; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: JESSICA HARRIS; MI (member ID) VMC906648227.
Subject DOB 1957-08-08, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: GARDEN STATE BENEFIT TRUST POS
- benefit: R (other or additional payer), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-01-13
- eligibility begin (356): 2024-01-01
- eligibility begin (356): 2024-01-01
- payer message: PLAN IS PRIMARY PAYER FOR THIS MEMBER
Response parties: payer [PR]: GARDEN STATE BENEFIT TRUST; PI (payer ID) 1450827364; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: JESSICA HARRIS; MI (member ID) VMC906648227; payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352.
Subject DOB 1957-08-08, sex M.
Eligibility exchange reference ELG36146968, dated 2026-02-25 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-01-16, action code WQ, amount $237.38.
D9 (clearinghouse claim number): TRC67588079.
Trace (2 (referenced transaction trace)): TRC67588079.
received date (050): 2026-01-16.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: JESSICA HARRIS; MI (member ID) VMC906648227.
Acknowledgment reference ACK67588079, dated 2026-01-16 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-01-13. Dx: Aftercare following joint replacement surgery. 97110 (29 min): therapeutic exercise for strength and ROM. 97112 (30 min): neuromuscular re-education of movement and balance. 97140 (15 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 74. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1450827364, interchange 643345570 date 260225 time 0800 version 00501 usage P; group HS control 643345570 date 20260225 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1450827364 to receiver [ZZ] 1110692305, interchange 435282535 date 260225 time 0800 version 00501 usage P; group HB control 435282535 date 20260225 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 17
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1450827364, interchange 660229699 date 260116 time 0800 version 00501 usage P; group HC control 660229699 date 20260116 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 400311540 date 260116 time 0800 version 00501 usage P; group HN control 400311540 date 20260116 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1450827364 to receiver [ZZ] 1110692305, interchange 629940139 date 260219 time 0800 version 00501 usage P; group HP control 629940139 date 20260219 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
