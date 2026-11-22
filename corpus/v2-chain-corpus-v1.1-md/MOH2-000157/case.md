# Case MOH2-000157

Patient CARLOS THOMPSON, DOB 1947-03-03, sex F, member ID 5GG1A51TJ34. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2026-02-17.

## Adjudication outcome (835)
Claim PA26347566: status 4 (denied). Billed $183.57, paid $0, patient responsibility . Filing indicator MB (Medicare Part B). Payer claim control 2608211185313, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-03-23.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT364468424, originator 1184634935.
claim statement period start (232): 2026-02-17.
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110 | 1 | $39.86 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $39.86 | HE N822 (missing procedure modifier(s)) |
| 2 | 97140 | 1 | $43.48 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $43.48 | HE N822 (missing procedure modifier(s)) |
| 3 | 97530 | 2 | $100.23 | $0 | CO-4 (Contractual Obligation: procedure code is inconsistent with the modifier used) $100.23 | HE N822 (missing procedure modifier(s)) |

Line item control numbers (REF 6R): PA26347566L1, PA26347566L2, PA26347566L3.
Remit claim parties: patient [QC]: CARLOS THOMPSON; MI (member ID) 5GG1A51TJ34; rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273.

## Claim as billed (837P)
Claim PA26347566, total charge $183.57, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M48061 (principal, ABK).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110 | 1 UN | $39.86 | 2026-02-17 | 1 | PA26347566L1 |
| 2 | 97140 | 1 UN | $43.48 | 2026-02-17 | 1 | PA26347566L2 |
| 3 | 97530 | 2 UN | $100.23 | 2026-02-17 | 1 | PA26347566L3 |

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: CARLOS THOMPSON; MI (member ID) 5GG1A51TJ34; 7943 CHESTNUT RD; PHILADELPHIA, PA, 19164
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: SARAH CHEN; XX (NPI) 1410042904
- rendering provider [82]: DAVID MILLER; XX (NPI) 1067541273
- Submission reference TRC72688940, dated 2026-03-07 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-02-17.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: CARLOS THOMPSON; MI (member ID) 5GG1A51TJ34.
Subject DOB 1947-03-03, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2026-02-17
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: CARLOS THOMPSON; MI (member ID) 5GG1A51TJ34.
Subject DOB 1947-03-03, sex F.
Eligibility exchange reference ELG18250639, dated 2026-03-24 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-03-09, action code WQ, amount $183.57.
D9 (clearinghouse claim number): TRC72688940.
Trace (2 (referenced transaction trace)): TRC72688940.
received date (050): 2026-03-09.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: CARLOS THOMPSON; MI (member ID) 5GG1A51TJ34.
Acknowledgment reference ACK72688940, dated 2026-03-09 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-02-17. Dx: Spinal stenosis lumbar region without neurogenic claudication. 97110 (14 min): therapeutic exercise for strength and ROM. 97140 (14 min): manual therapy (soft tissue and joint mobilization). 97530 (30 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 58. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 524986258 date 260324 time 0800 version 00501 usage P; group HS control 524986258 date 20260324 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 798068552 date 260324 time 0800 version 00501 usage P; group HB control 798068552 date 20260324 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 371162032 date 260307 time 0800 version 00501 usage P; group HC control 371162032 date 20260307 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 736708492 date 260309 time 0800 version 00501 usage P; group HN control 736708492 date 20260309 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 364468424 date 260323 time 0800 version 00501 usage P; group HP control 364468424 date 20260323 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 33
