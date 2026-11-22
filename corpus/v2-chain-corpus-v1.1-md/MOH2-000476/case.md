# Case MOH2-000476

Patient ELIZABETH WHITE, DOB 1957-05-02, sex M, member ID 4UK9JP4RE04. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-06-06.

## Adjudication outcome (835)
Claim PA28765639: status 4 (denied). Billed $136.49, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2620993082610, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-07-28.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT494157710, originator 1184634935.
claim statement period start (232): 2026-06-06.
Outpatient adjudication remarks (MOA): M77 (missing/incomplete/invalid place of service).
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP-KX | 1 | $41.73 | $0 | CO-5 (Contractual Obligation: procedure code/type of bill is inconsistent with the place of service) $41.73 |  |
| 2 | 97110-GP-KX | 1 | $40.16 | $0 | CO-5 (Contractual Obligation: procedure code/type of bill is inconsistent with the place of service) $40.16 |  |
| 3 | 97530-GP-KX | 1 | $54.6 | $0 | CO-5 (Contractual Obligation: procedure code/type of bill is inconsistent with the place of service) $54.6 |  |

Line item control numbers (REF 6R): PA28765639L1, PA28765639L2, PA28765639L3.
Modifiers on remit lines: GP (under PT plan of care), KX.
Remit claim parties: patient [QC]: ELIZABETH WHITE; MI (member ID) 4UK9JP4RE04; rendering provider [82]: MARY CLARK; XX (NPI) 1992501921.

## Claim as billed (837P)
Claim PA28765639, total charge $136.49, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M1712 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP-KX | 1 UN | $41.73 | 2026-06-06 | 1 | PA28765639L1 |
| 2 | 97110-GP-KX | 1 UN | $40.16 | 2026-06-06 | 1 | PA28765639L2 |
| 3 | 97530-GP-KX | 1 UN | $54.6 | 2026-06-06 | 1 | PA28765639L3 |

Modifiers on claim: GP (under PT plan of care), KX.

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: ELIZABETH WHITE; MI (member ID) 4UK9JP4RE04; 9303 LINCOLN AVE; WILMINGTON, DE, 19859
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: ELENA VASQUEZ; XX (NPI) 1863431679
- rendering provider [82]: MARY CLARK; XX (NPI) 1992501921
- Submission reference TRC32856012, dated 2026-06-18 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-06-06.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: ELIZABETH WHITE; MI (member ID) 4UK9JP4RE04.
Subject DOB 1957-05-02, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-06-06
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: ELIZABETH WHITE; MI (member ID) 4UK9JP4RE04.
Subject DOB 1957-05-02, sex M.
Eligibility exchange reference ELG91274883, dated 2026-07-30 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-06-18, action code WQ, amount $136.49.
D9 (clearinghouse claim number): TRC32856012.
Trace (2 (referenced transaction trace)): TRC32856012.
received date (050): 2026-06-18.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: ELIZABETH WHITE; MI (member ID) 4UK9JP4RE04.
Acknowledgment reference ACK32856012, dated 2026-06-18 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-06-06. Dx: Unilateral primary osteoarthritis left knee. 97110 (14 min): therapeutic exercise for strength and ROM. 97110 (16 min): therapeutic exercise for strength and ROM. 97530 (15 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 45. Care delivered remotely via two-way real-time audio-video; patient located at home, consent for virtual care recorded. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 388254338 date 260730 time 0800 version 00501 usage P; group HS control 388254338 date 20260730 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 467738027 date 260730 time 0800 version 00501 usage P; group HB control 467738027 date 20260730 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 881378458 date 260618 time 0800 version 00501 usage P; group HC control 881378458 date 20260618 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 929033160 date 260618 time 0800 version 00501 usage P; group HN control 929033160 date 20260618 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 494157710 date 260728 time 0800 version 00501 usage P; group HP control 494157710 date 20260728 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 31
