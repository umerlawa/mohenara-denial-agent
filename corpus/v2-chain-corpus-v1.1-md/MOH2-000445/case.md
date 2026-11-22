# Case MOH2-000445

Patient HELEN WILLIAMS, DOB 1955-01-17, sex M, member ID H949153864. Payer: KEYSTONE SENIOR COMPLETE HMO. Service date 2024-03-18.

## Adjudication outcome (835)
Claim PA22997817: status 1 (processed as primary, paid). Billed $338.88, paid $99.66, patient responsibility $24.92. Filing indicator HM (HMO). Payer claim control 2410944753472, POS 11 (office), frequency 1 (original claim).
Payment: $99.66 by CHK (check), handling I.
production date (405): 2024-04-18.
Payer [PR]: KEYSTONE SENIOR COMPLETE HMO; 35 PENN CENTER BLVD; PHILADELPHIA, PA, 191031800; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT758664817, originator 1165038291.
claim statement period start (232): 2024-03-18.
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GO | 2 | $95.53 | $0 | CO-236 (Contractual Obligation: procedure/modifier combination not compatible per coding guidelines, bundled) $95.53 | HE N20 (service not payable with other service rendered on the same date) |
| 2 | 97760-GO | 2 | $157.66 | $73.74 allowed (B6) $92.18 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $65.48; PR-2 (Patient Responsibility: coinsurance amount) $18.44 |  |
| 3 | 97110-GO | 1 | $40.86 | $0 | CO-236 (Contractual Obligation: procedure/modifier combination not compatible per coding guidelines, bundled) $40.86 | HE N20 (service not payable with other service rendered on the same date) |
| 4 | 97535-GO | 1 | $44.83 | $25.92 allowed (B6) $32.4 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $12.43; PR-2 (Patient Responsibility: coinsurance amount) $6.48 |  |

Line item control numbers (REF 6R): PA22997817L1, PA22997817L2, PA22997817L3, PA22997817L4.
Modifiers on remit lines: GO (under OT plan of care).
Remit claim parties: patient [QC]: HELEN WILLIAMS; MI (member ID) H949153864; rendering provider [82]: DOROTHY LOPEZ; XX (NPI) 1390221007.

## Claim as billed (837P)
Claim PA22997817, total charge $338.88, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25511 (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing HM (HMO).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GO | 2 UN | $95.53 | 2024-03-18 | 1 | PA22997817L1 |
| 2 | 97760-GO | 2 UN | $157.66 | 2024-03-18 | 1 | PA22997817L2 |
| 3 | 97110-GO | 1 UN | $40.86 | 2024-03-18 | 1 | PA22997817L3 |
| 4 | 97535-GO | 1 UN | $44.83 | 2024-03-18 | 1 | PA22997817L4 |

Modifiers on claim: GO (under OT plan of care).

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: KEYSTONE SENIOR COMPLETE HMO; 46 (ETIN) 1650382917
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: HELEN WILLIAMS; MI (member ID) H949153864; 7432 OAK ST; TRENTON, NJ, 08685
- payer [PR]: KEYSTONE SENIOR COMPLETE HMO; PI (payer ID) 1650382917
- referring provider [DN]: FATIMA AL-RASHID; XX (NPI) 1333183066
- rendering provider [82]: DOROTHY LOPEZ; XX (NPI) 1390221007
- Submission reference TRC71251570, dated 2024-04-02 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2024-03-18.
Inquiry parties: payer [PR]: KEYSTONE SENIOR COMPLETE HMO; PI (payer ID) 1650382917; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: HELEN WILLIAMS; MI (member ID) H949153864.
Subject DOB 1955-01-17, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: KEYSTONE SENIOR COMPLETE HMO HMO
- plan date (291): 2024-03-18
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: KEYSTONE SENIOR COMPLETE HMO; PI (payer ID) 1650382917; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: HELEN WILLIAMS; MI (member ID) H949153864.
Subject DOB 1955-01-17, sex M.
Eligibility exchange reference ELG57512136, dated 2024-04-21 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2024-04-04, action code WQ, amount $338.88.
D9 (clearinghouse claim number): TRC71251570.
Trace (2 (referenced transaction trace)): TRC71251570.
received date (050): 2024-04-04.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: HELEN WILLIAMS; MI (member ID) H949153864.
Acknowledgment reference ACK71251570, dated 2024-04-04 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

OT treatment note 2024-03-18. Dx: Pain in right shoulder. 97110 (30 min): therapeutic exercise for strength and ROM. 97760 (30 min): orthotic management and training, initial encounter. 97110 (14 min): therapeutic exercise for strength and ROM. 97535 (16 min): self-care/home management training. Total timed minutes: 90. 97110 was performed in a separate 15-minute session from 97760, directed at a distinct body region with a distinct goal; services were not integral to one another. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1650382917, interchange 502317816 date 240421 time 0800 version 00501 usage P; group HS control 502317816 date 20240421 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1650382917 to receiver [ZZ] 1801579548, interchange 451441421 date 240421 time 0800 version 00501 usage P; group HB control 451441421 date 20240421 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1650382917, interchange 159196478 date 240402 time 0800 version 00501 usage P; group HC control 159196478 date 20240402 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 38
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 115604408 date 240404 time 0800 version 00501 usage P; group HN control 115604408 date 20240404 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1650382917 to receiver [ZZ] 1801579548, interchange 758664817 date 240418 time 0800 version 00501 usage P; group HP control 758664817 date 20240418 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 40
