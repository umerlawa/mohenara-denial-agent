# Case MOH2-000399

Patient CARLOS WILSON, DOB 1970-03-05, sex F, member ID KLU968297324. Payer: ATLANTIC SHORE ASSURANCE. Service date 2026-08-09.

## Adjudication outcome (835)
Claim PA24343577: status 1 (processed as primary, paid). Billed $73.39, paid $14.43, patient responsibility $3.61. Filing indicator CI (commercial insurance). Payer claim control 2625468496258, POS 11 (office), frequency 1 (original claim).
Payment: $14.43 by CHK (check), handling I.
production date (405): 2026-09-11.
Payer [PR]: ATLANTIC SHORE ASSURANCE; 3499 ROUTE 9 N; FREEHOLD, NJ, 077283100; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT498277652, originator 1125037465.
claim statement period start (232): 2026-08-09.
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97150-GP | 1 | $28.64 | $14.43 allowed (B6) $18.04 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $10.6; PR-2 (Patient Responsibility: coinsurance amount) $3.61 |  |
| 2 | 97140-GP | 1 | $44.75 | $0 | CO-97 (Contractual Obligation: payment included in the allowance for another service, bundled) $44.75 | HE M80 (not covered when performed with same-day service) |

Line item control numbers (REF 6R): PA24343577L1, PA24343577L2.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: CARLOS WILSON; MI (member ID) KLU968297324; rendering provider [82]: MARY CLARK; XX (NPI) 1992501921.

## Claim as billed (837P)
Claim PA24343577, total charge $73.39, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97150-GP | 1 UN | $28.64 | 2026-08-09 | 1 | PA24343577L1 |
| 2 | 97140-GP | 1 UN | $44.75 | 2026-08-09 | 1 | PA24343577L2 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: ATLANTIC SHORE ASSURANCE; 46 (ETIN) 1250374659
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: CARLOS WILSON; MI (member ID) KLU968297324; 8812 CHESTNUT AVE; STATEN ISLAND, NY, 10329
- payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659
- referring provider [DN]: MARCUS WEBB; XX (NPI) 1583494452
- rendering provider [82]: MARY CLARK; XX (NPI) 1992501921
- Submission reference TRC90367663, dated 2026-08-13 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-08-09.
Inquiry parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: CARLOS WILSON; MI (member ID) KLU968297324.
Subject DOB 1970-03-05, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: ATLANTIC SHORE ASSURANCE HMO
- plan date (291): 2026-08-09
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: CARLOS WILSON; MI (member ID) KLU968297324.
Subject DOB 1970-03-05, sex F.
Eligibility exchange reference ELG60831089, dated 2026-09-14 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-08-13, action code WQ, amount $73.39.
D9 (clearinghouse claim number): TRC90367663.
Trace (2 (referenced transaction trace)): TRC90367663.
received date (050): 2026-08-13.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: CARLOS WILSON; MI (member ID) KLU968297324.
Acknowledgment reference ACK90367663, dated 2026-08-13 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-08-09. Dx: Aftercare following joint replacement surgery. 97150 (untimed, 1 unit): group therapeutic procedure. 97140 (14 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 14. 97140 was performed in a separate 15-minute session from 97150, directed at a distinct body region with a distinct goal; services were not integral to one another. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1250374659, interchange 834922303 date 260914 time 0800 version 00501 usage P; group HS control 834922303 date 20260914 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1250374659 to receiver [ZZ] 1110692305, interchange 757424547 date 260914 time 0800 version 00501 usage P; group HB control 757424547 date 20260914 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1250374659, interchange 996516565 date 260813 time 0800 version 00501 usage P; group HC control 996516565 date 20260813 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 137862595 date 260813 time 0800 version 00501 usage P; group HN control 137862595 date 20260813 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1250374659 to receiver [ZZ] 1110692305, interchange 498277652 date 260911 time 0800 version 00501 usage P; group HP control 498277652 date 20260911 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 29
