# Case MOH2-000726

Patient JESSICA HARRIS, DOB 1957-08-08, sex M, member ID VMC906648227. Payer: GARDEN STATE BENEFIT TRUST. Service date 2026-01-16.

## Adjudication outcome (835)
Claim PA25516831: status 4 (denied). Billed $290.83, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2604065690428, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-02-09.
Payer [PR]: GARDEN STATE BENEFIT TRUST; 210 RARITAN PLAZA; EDISON, NJ, 088373105; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT784168911, originator 1145082736.
claim statement period start (232): 2026-01-16.
Outpatient adjudication remarks (MOA): MA04 (secondary payment cannot be considered without primary payer identity).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $47.51 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $47.51 |  |
| 2 | 97112-GP | 1 | $46.51 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $46.51 |  |
| 3 | 97140-GP | 2 | $88.52 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $88.52 |  |
| 4 | 97530-GP | 1 | $55.75 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $55.75 |  |
| 5 | 97535-GP | 1 | $52.54 | $0 | OA-22 (Other Adjustment: care may be covered by another payer per coordination of benefits) $52.54 |  |

Line item control numbers (REF 6R): PA25516831L1, PA25516831L2, PA25516831L3, PA25516831L4, PA25516831L5.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: JESSICA HARRIS; MI (member ID) VMC906648227; rendering provider [82]: MARY CLARK; XX (NPI) 1992501921.

## Claim as billed (837P)
Claim PA25516831, total charge $290.83, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $47.51 | 2026-01-16 | 1 | PA25516831L1 |
| 2 | 97112-GP | 1 UN | $46.51 | 2026-01-16 | 1 | PA25516831L2 |
| 3 | 97140-GP | 2 UN | $88.52 | 2026-01-16 | 1 | PA25516831L3 |
| 4 | 97530-GP | 1 UN | $55.75 | 2026-01-16 | 1 | PA25516831L4 |
| 5 | 97535-GP | 1 UN | $52.54 | 2026-01-16 | 1 | PA25516831L5 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: GARDEN STATE BENEFIT TRUST; 46 (ETIN) 1450827364
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: JESSICA HARRIS; MI (member ID) VMC906648227; 9631 OAK ST; TRENTON, NJ, 08668
- payer [PR]: GARDEN STATE BENEFIT TRUST; PI (payer ID) 1450827364
- referring provider [DN]: DANIEL OKAFOR; XX (NPI) 1230067602
- rendering provider [82]: MARY CLARK; XX (NPI) 1992501921
- Submission reference TRC27758856, dated 2026-01-19 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-01-16.
Inquiry parties: payer [PR]: GARDEN STATE BENEFIT TRUST; PI (payer ID) 1450827364; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: JESSICA HARRIS; MI (member ID) VMC906648227.
Subject DOB 1957-08-08, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: GARDEN STATE BENEFIT TRUST POS
- benefit: R (other or additional payer), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-01-16
- eligibility begin (356): 2024-01-01
- eligibility begin (356): 2024-01-01
- payer message: PLAN IS PRIMARY PAYER FOR THIS MEMBER
Response parties: payer [PR]: GARDEN STATE BENEFIT TRUST; PI (payer ID) 1450827364; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: JESSICA HARRIS; MI (member ID) VMC906648227; payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352.
Subject DOB 1957-08-08, sex M.
Eligibility exchange reference ELG13082661, dated 2026-02-10 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-01-19, action code WQ, amount $290.83.
D9 (clearinghouse claim number): TRC27758856.
Trace (2 (referenced transaction trace)): TRC27758856.
received date (050): 2026-01-19.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: JESSICA HARRIS; MI (member ID) VMC906648227.
Acknowledgment reference ACK27758856, dated 2026-01-19 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-01-16. Dx: Aftercare following joint replacement surgery. 97110 (14 min): therapeutic exercise for strength and ROM. 97112 (14 min): neuromuscular re-education of movement and balance. 97140 (31 min): manual therapy (soft tissue and joint mobilization). 97530 (14 min): therapeutic activities (dynamic functional tasks). 97535 (14 min): self-care/home management training. Total timed minutes: 87. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1450827364, interchange 985950416 date 260210 time 0800 version 00501 usage P; group HS control 985950416 date 20260210 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1450827364 to receiver [ZZ] 1110692305, interchange 871056108 date 260210 time 0800 version 00501 usage P; group HB control 871056108 date 20260210 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 17
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1450827364, interchange 180449088 date 260119 time 0800 version 00501 usage P; group HC control 180449088 date 20260119 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 42
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 681170747 date 260119 time 0800 version 00501 usage P; group HN control 681170747 date 20260119 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1450827364 to receiver [ZZ] 1110692305, interchange 784168911 date 260209 time 0800 version 00501 usage P; group HP control 784168911 date 20260209 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 39
