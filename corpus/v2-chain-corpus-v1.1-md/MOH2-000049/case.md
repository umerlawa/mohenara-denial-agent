# Case MOH2-000049

Patient BARBARA MILLER, DOB 1955-06-19, sex F, member ID 3E92WK0EW22. Payer: NOVITAS SOLUTIONS MEDICARE PART B. Service date 2024-08-02.

## Adjudication outcome (835)
Claim PA23895716: status 1 (processed as primary, paid). Billed $516.84, paid $25.92, patient responsibility $6.48. Filing indicator MB (Medicare Part B). Payer claim control 2426104003803, POS 11 (office), frequency 1 (original claim).
Payment: $25.92 by CHK (check), handling I.
production date (405): 2024-09-17.
Payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PO BOX 3113; MECHANICSBURG, PA, 170553113; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT677143402, originator 1184634935.
claim statement period start (232): 2024-08-02.
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97535-GO | 1 | $44.03 | $25.92 allowed (B6) $32.4 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $11.63; PR-2 (Patient Responsibility: coinsurance amount) $6.48 |  |
| 2 | 97530-GO | 9 | $472.81 | $0 | CO-151 (Contractual Obligation: information does not support this many/frequency of services) $472.81 | HE N362 (the number of days or units exceeds the acceptable maximum) |

Line item control numbers (REF 6R): PA23895716L1, PA23895716L2.
Modifiers on remit lines: GO (under OT plan of care).
Remit claim parties: patient [QC]: BARBARA MILLER; MI (member ID) 3E92WK0EW22; rendering provider [82]: MARY CLARK; XX (NPI) 1992501921.

## Claim as billed (837P)
Claim PA23895716, total charge $516.84, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: G5601 (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing MB (Medicare Part B).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97535-GO | 1 UN | $44.03 | 2024-08-02 | 1 | PA23895716L1 |
| 2 | 97530-GO | 9 UN | $472.81 | 2024-08-02 | 1 | PA23895716L2 |

Modifiers on claim: GO (under OT plan of care).

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: NOVITAS SOLUTIONS MEDICARE PART B; 46 (ETIN) 1846349352
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: BARBARA MILLER; MI (member ID) 3E92WK0EW22; 2084 FRANKLIN RD; WILMINGTON, DE, 19878
- payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352
- referring provider [DN]: DANIEL OKAFOR; XX (NPI) 1230067602
- rendering provider [82]: MARY CLARK; XX (NPI) 1992501921
- Submission reference TRC66506499, dated 2024-08-16 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2024-08-02.
Inquiry parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: BARBARA MILLER; MI (member ID) 3E92WK0EW22.
Subject DOB 1955-06-19, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: NOVITAS SOLUTIONS MEDICARE PART B FFS
- plan date (291): 2024-08-02
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: NOVITAS SOLUTIONS MEDICARE PART B; PI (payer ID) 1846349352; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: BARBARA MILLER; MI (member ID) 3E92WK0EW22.
Subject DOB 1955-06-19, sex F.
Eligibility exchange reference ELG73739117, dated 2024-09-19 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2024-08-16, action code WQ, amount $516.84.
D9 (clearinghouse claim number): TRC66506499.
Trace (2 (referenced transaction trace)): TRC66506499.
received date (050): 2024-08-16.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: BARBARA MILLER; MI (member ID) 3E92WK0EW22.
Acknowledgment reference ACK66506499, dated 2024-08-16 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

OT treatment note 2024-08-02. Dx: Carpal tunnel syndrome right upper limb. 97535 (14 min): self-care/home management training. 97530 (29 min): therapeutic activities (dynamic functional tasks). Total timed minutes: 43. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1846349352, interchange 130376720 date 240919 time 0800 version 00501 usage P; group HS control 130376720 date 20240919 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 655329506 date 240919 time 0800 version 00501 usage P; group HB control 655329506 date 20240919 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1846349352, interchange 505552726 date 240816 time 0800 version 00501 usage P; group HC control 505552726 date 20240816 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 284356329 date 240816 time 0800 version 00501 usage P; group HN control 284356329 date 20240816 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1846349352 to receiver [ZZ] 1110692305, interchange 677143402 date 240917 time 0800 version 00501 usage P; group HP control 677143402 date 20240917 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 29
