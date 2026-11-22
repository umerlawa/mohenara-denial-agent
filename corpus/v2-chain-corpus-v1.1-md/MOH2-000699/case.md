# Case MOH2-000699

Patient BARBARA MARTIN, DOB 1957-12-14, sex M, member ID 6C24R57XX43. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-01-30.

## Adjudication outcome (835)
Claim PA27678637: status 1 (processed as primary, paid). Billed $413.6, paid $50.24, patient responsibility $12.55. Filing indicator MB (Medicare Part B). Payer claim control 2606016412349, POS 11 (office), frequency 1 (original claim).
Payment: $50.24 by CHK (check), handling I.
production date (405): 2026-03-01.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT968129251, originator 1184634935.
claim statement period start (232): 2026-01-30.
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 7 | $317.38 | $0 | CO-151 (Contractual Obligation: information does not support this many/frequency of services) $317.38 | HE N362 (the number of days or units exceeds the acceptable maximum) |
| 2 | 97140-GP | 1 | $43.57 | $22.18 allowed (B6) $27.72 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $15.85; PR-2 (Patient Responsibility: coinsurance amount) $5.54 |  |
| 3 | 97530-GP | 1 | $52.65 | $28.06 allowed (B6) $35.07 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $17.58; PR-2 (Patient Responsibility: coinsurance amount) $7.01 |  |

Line item control numbers (REF 6R): PA27678637L1, PA27678637L2, PA27678637L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: BARBARA MARTIN; MI (member ID) 6C24R57XX43; rendering provider [82]: MARY CLARK; XX (NPI) 1992501921.

## Claim as billed (837P)
Claim PA27678637, total charge $413.6, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 7 UN | $317.38 | 2026-01-30 | 1 | PA27678637L1 |
| 2 | 97140-GP | 1 UN | $43.57 | 2026-01-30 | 1 | PA27678637L2 |
| 3 | 97530-GP | 1 UN | $52.65 | 2026-01-30 | 1 | PA27678637L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: BARBARA MARTIN; MI (member ID) 6C24R57XX43; 2190 OAK ST; WILMINGTON, DE, 19851
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: GRETA LINDQVIST; XX (NPI) 1205658765
- rendering provider [82]: MARY CLARK; XX (NPI) 1992501921
- Submission reference TRC52773908, dated 2026-02-03 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-01-30.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: BARBARA MARTIN; MI (member ID) 6C24R57XX43.
Subject DOB 1957-12-14, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-01-30
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: BARBARA MARTIN; MI (member ID) 6C24R57XX43.
Subject DOB 1957-12-14, sex M.
Eligibility exchange reference ELG63062776, dated 2026-03-06 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-02-04, action code WQ, amount $413.6.
D9 (clearinghouse claim number): TRC52773908.
Trace (2 (referenced transaction trace)): TRC52773908.
received date (050): 2026-02-04.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: BARBARA MARTIN; MI (member ID) 6C24R57XX43.
Acknowledgment reference ACK52773908, dated 2026-02-04 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-01-30. Dx: Aftercare following joint replacement surgery. 97110 (14 min): therapeutic exercise for strength and ROM. 97140 (14 min): manual therapy (soft tissue and joint mobilization). 97530 (15 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 43. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 430568432 date 260306 time 0800 version 00501 usage P; group HS control 430568432 date 20260306 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 565622266 date 260306 time 0800 version 00501 usage P; group HB control 565622266 date 20260306 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 628538082 date 260203 time 0800 version 00501 usage P; group HC control 628538082 date 20260203 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 358711069 date 260204 time 0800 version 00501 usage P; group HN control 358711069 date 20260204 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 968129251 date 260301 time 0800 version 00501 usage P; group HP control 968129251 date 20260301 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 35
