# Case MOH2-000693

Patient CARLOS WILSON, DOB 1970-03-05, sex F, member ID KLU968297324. Payer: ATLANTIC SHORE ASSURANCE. Service date 2026-08-27.

## Adjudication outcome (835)
Claim PA29744378: status 1 (processed as primary, paid). Billed $162.28, paid $80.16, patient responsibility $20.04. Filing indicator CI (commercial insurance). Payer claim control 2629384591362, POS 11 (office), frequency 1 (original claim).
Payment: $80.16 by CHK (check), handling I.
production date (405): 2026-10-20.
Payer [PR]: ATLANTIC SHORE ASSURANCE; 3499 ROUTE 9 N; FREEHOLD, NJ, 077283100; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT667657325, originator 1125037465.
claim statement period start (232): 2026-08-27.
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97535-GP | 1 | $50.83 | $25.92 allowed (B6) $32.4 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $18.43; PR-2 (Patient Responsibility: coinsurance amount) $6.48 |  |
| 2 | 97530-GP | 1 | $56.01 | $28.06 allowed (B6) $35.07 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $20.94; PR-2 (Patient Responsibility: coinsurance amount) $7.01 |  |
| 3 | 97112-GP | 1 | $55.44 | $26.18 allowed (B6) $32.73 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $22.71; PR-2 (Patient Responsibility: coinsurance amount) $6.55 |  |

Line item control numbers (REF 6R): PA29744378L1, PA29744378L2, PA29744378L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: CARLOS WILSON; MI (member ID) KLU968297324; rendering provider [82]: MARY CLARK; XX (NPI) 1992501921.

## Claim as billed (837P)
Claim PA29744378, total charge $162.28, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97535-GP | 1 UN | $50.83 | 2026-08-27 | 1 | PA29744378L1 |
| 2 | 97530-GP | 1 UN | $56.01 | 2026-08-27 | 1 | PA29744378L2 |
| 3 | 97112-GP | 1 UN | $55.44 | 2026-08-27 | 1 | PA29744378L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: ATLANTIC SHORE ASSURANCE; 46 (ETIN) 1250374659
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: CARLOS WILSON; MI (member ID) KLU968297324; 8812 CHESTNUT AVE; STATEN ISLAND, NY, 10329
- payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659
- referring provider [DN]: MARCUS WEBB; XX (NPI) 1583494452
- rendering provider [82]: MARY CLARK; XX (NPI) 1992501921
- Submission reference TRC70812140, dated 2026-09-15 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-08-27.
Inquiry parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: CARLOS WILSON; MI (member ID) KLU968297324.
Subject DOB 1970-03-05, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: ATLANTIC SHORE ASSURANCE HMO
- plan date (291): 2026-08-27
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: CARLOS WILSON; MI (member ID) KLU968297324.
Subject DOB 1970-03-05, sex F.
Eligibility exchange reference ELG31283286, dated 2026-10-24 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-09-16, action code WQ, amount $162.28.
D9 (clearinghouse claim number): TRC70812140.
Trace (2 (referenced transaction trace)): TRC70812140.
received date (050): 2026-09-16.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: CARLOS WILSON; MI (member ID) KLU968297324.
Acknowledgment reference ACK70812140, dated 2026-09-16 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-08-27. Dx: Aftercare following joint replacement surgery. 97535 (14 min): self-care/home management training. 97530 (15 min): therapeutic activities (dynamic functional tasks). 97112 (16 min): neuromuscular re-education of movement and balance. Total timed minutes: 45. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1250374659, interchange 686167774 date 261024 time 0800 version 00501 usage P; group HS control 686167774 date 20261024 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1250374659 to receiver [ZZ] 1110692305, interchange 183455582 date 261024 time 0800 version 00501 usage P; group HB control 183455582 date 20261024 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1250374659, interchange 998357913 date 260915 time 0800 version 00501 usage P; group HC control 998357913 date 20260915 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 261117391 date 260916 time 0800 version 00501 usage P; group HN control 261117391 date 20260916 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1250374659 to receiver [ZZ] 1110692305, interchange 667657325 date 261020 time 0800 version 00501 usage P; group HP control 667657325 date 20261020 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 36
