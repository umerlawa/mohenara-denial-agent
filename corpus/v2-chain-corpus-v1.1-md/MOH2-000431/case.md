# Case MOH2-000431

Patient CARLOS WILSON, DOB 1970-03-05, sex F, member ID KLU968297324. Payer: ATLANTIC SHORE ASSURANCE. Service date 2026-01-25.

## Adjudication outcome (835)
Claim PA26588660: status 4 (denied). Billed $135.23, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2712282777374, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2027-05-02.
Payer [PR]: ATLANTIC SHORE ASSURANCE; 3499 ROUTE 9 N; FREEHOLD, NJ, 077283100; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT591879432, originator 1125037465.
claim statement period start (232): 2026-01-25.
Outpatient adjudication remarks (MOA): N211 (you may not appeal this decision).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 | $90.37 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $90.37 |  |
| 2 | 97112-GP | 1 | $44.86 | $0 | CO-29 (Contractual Obligation: the time limit for filing has expired) $44.86 |  |

Line item control numbers (REF 6R): PA26588660L1, PA26588660L2.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: CARLOS WILSON; MI (member ID) KLU968297324; rendering provider [82]: MARY CLARK; XX (NPI) 1992501921.

## Claim as billed (837P)
Claim PA26588660, total charge $135.23, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: Z471 (principal, ABK), R269 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 2 UN | $90.37 | 2026-01-25 | 1 | PA26588660L1 |
| 2 | 97112-GP | 1 UN | $44.86 | 2026-01-25 | 1 | PA26588660L2 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: ATLANTIC SHORE ASSURANCE; 46 (ETIN) 1250374659
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: CARLOS WILSON; MI (member ID) KLU968297324; 8812 CHESTNUT AVE; STATEN ISLAND, NY, 10329
- payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659
- referring provider [DN]: MARCUS WEBB; XX (NPI) 1583494452
- rendering provider [82]: MARY CLARK; XX (NPI) 1992501921
- Submission reference TRC76401758, dated 2027-04-05 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-01-25.
Inquiry parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: CARLOS WILSON; MI (member ID) KLU968297324.
Subject DOB 1970-03-05, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: ATLANTIC SHORE ASSURANCE HMO
- plan date (291): 2026-01-25
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: ATLANTIC SHORE ASSURANCE; PI (payer ID) 1250374659; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: CARLOS WILSON; MI (member ID) KLU968297324.
Subject DOB 1970-03-05, sex F.
Eligibility exchange reference ELG21798732, dated 2027-05-09 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2027-04-07, action code WQ, amount $135.23.
D9 (clearinghouse claim number): TRC76401758.
Trace (2 (referenced transaction trace)): TRC76401758.
received date (050): 2027-04-07.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: CARLOS WILSON; MI (member ID) KLU968297324.
Acknowledgment reference ACK76401758, dated 2027-04-07 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-01-25. Dx: Aftercare following joint replacement surgery. 97110 (31 min): therapeutic exercise for strength and ROM. 97112 (14 min): neuromuscular re-education of movement and balance. Total timed minutes: 45. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1250374659, interchange 949691016 date 270509 time 0800 version 00501 usage P; group HS control 949691016 date 20270509 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1250374659 to receiver [ZZ] 1110692305, interchange 871024559 date 270509 time 0800 version 00501 usage P; group HB control 871024559 date 20270509 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1250374659, interchange 460232600 date 270405 time 0800 version 00501 usage P; group HC control 460232600 date 20270405 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 464611739 date 270407 time 0800 version 00501 usage P; group HN control 464611739 date 20270407 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1250374659 to receiver [ZZ] 1110692305, interchange 591879432 date 270502 time 0800 version 00501 usage P; group HP control 591879432 date 20270502 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 27
