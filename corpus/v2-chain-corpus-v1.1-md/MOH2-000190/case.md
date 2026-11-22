# Case MOH2-000190

Patient HELEN WILLIAMS, DOB 1955-01-17, sex M, member ID H949153864. Payer: KEYSTONE SENIOR COMPLETE HMO. Service date 2024-03-24.

## Adjudication outcome (835)
Claim PA26987636: status 1 (processed as primary, paid). Billed $275.89, paid $107.14, patient responsibility $26.79. Filing indicator HM (HMO). Payer claim control 2413158982256, POS 11 (office), frequency 1 (original claim).
Payment: $107.14 by CHK (check), handling I.
production date (405): 2024-05-10.
Payer [PR]: KEYSTONE SENIOR COMPLETE HMO; 35 PENN CENTER BLVD; PHILADELPHIA, PA, 191031800; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT189654654, originator 1165038291.
claim statement period start (232): 2024-03-24.
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97760-GO | 1 | $81.52 | $36.87 allowed (B6) $46.09 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $35.43; PR-2 (Patient Responsibility: coinsurance amount) $9.22 |  |
| 2 | 97112-GO | 1 | $46.51 | $0 | CO-236 (Contractual Obligation: procedure/modifier combination not compatible per coding guidelines, bundled) $46.51 | HE N20 (service not payable with other service rendered on the same date) |
| 3 | 97140-GO-59 | 2 | $98.97 | $44.35 allowed (B6) $55.44 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $43.53; PR-2 (Patient Responsibility: coinsurance amount) $11.09 |  |
| 4 | 97535-GO | 1 | $48.89 | $25.92 allowed (B6) $32.4 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $16.49; PR-2 (Patient Responsibility: coinsurance amount) $6.48 |  |

Line item control numbers (REF 6R): PA26987636L1, PA26987636L2, PA26987636L3, PA26987636L4.
Modifiers on remit lines: 59 (distinct procedural service), GO (under OT plan of care).
Remit claim parties: patient [QC]: HELEN WILLIAMS; MI (member ID) H949153864; rendering provider [82]: DOROTHY LOPEZ; XX (NPI) 1390221007.

## Claim as billed (837P)
Claim PA26987636, total charge $275.89, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M25511 (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing HM (HMO).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97760-GO | 1 UN | $81.52 | 2024-03-24 | 1 | PA26987636L1 |
| 2 | 97112-GO | 1 UN | $46.51 | 2024-03-24 | 1 | PA26987636L2 |
| 3 | 97140-GO-59 | 2 UN | $98.97 | 2024-03-24 | 1 | PA26987636L3 |
| 4 | 97535-GO | 1 UN | $48.89 | 2024-03-24 | 1 | PA26987636L4 |

Modifiers on claim: 59 (distinct procedural service), GO (under OT plan of care).

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: KEYSTONE SENIOR COMPLETE HMO; 46 (ETIN) 1650382917
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: HELEN WILLIAMS; MI (member ID) H949153864; 7432 OAK ST; TRENTON, NJ, 08685
- payer [PR]: KEYSTONE SENIOR COMPLETE HMO; PI (payer ID) 1650382917
- referring provider [DN]: FATIMA AL-RASHID; XX (NPI) 1333183066
- rendering provider [82]: DOROTHY LOPEZ; XX (NPI) 1390221007
- Submission reference TRC70670326, dated 2024-04-09 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2024-03-24.
Inquiry parties: payer [PR]: KEYSTONE SENIOR COMPLETE HMO; PI (payer ID) 1650382917; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: HELEN WILLIAMS; MI (member ID) H949153864.
Subject DOB 1955-01-17, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: KEYSTONE SENIOR COMPLETE HMO HMO
- plan date (291): 2024-03-24
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: KEYSTONE SENIOR COMPLETE HMO; PI (payer ID) 1650382917; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: HELEN WILLIAMS; MI (member ID) H949153864.
Subject DOB 1955-01-17, sex M.
Eligibility exchange reference ELG39636737, dated 2024-05-15 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2024-04-09, action code WQ, amount $275.89.
D9 (clearinghouse claim number): TRC70670326.
Trace (2 (referenced transaction trace)): TRC70670326.
received date (050): 2024-04-09.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: HELEN WILLIAMS; MI (member ID) H949153864.
Acknowledgment reference ACK70670326, dated 2024-04-09 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

OT treatment note 2024-03-24. Dx: Pain in right shoulder. 97760 (14 min): orthotic management and training, initial encounter. 97112 (16 min): neuromuscular re-education of movement and balance. 97140 (29 min): manual therapy (soft tissue and joint mobilization). 97535 (15 min): self-care/home management training. Total timed minutes: 74. 97112 ran concurrently with the 97760 work on the identical body region; the note documents one unbroken treatment interval with shared goals. 97140 was rendered as an independent service from 97760 — separate start/stop times were recorded and a different body region was treated. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1650382917, interchange 714777896 date 240515 time 0800 version 00501 usage P; group HS control 714777896 date 20240515 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1650382917 to receiver [ZZ] 1801579548, interchange 109762681 date 240515 time 0800 version 00501 usage P; group HB control 109762681 date 20240515 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1650382917, interchange 124456783 date 240409 time 0800 version 00501 usage P; group HC control 124456783 date 20240409 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 38
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 231248217 date 240409 time 0800 version 00501 usage P; group HN control 231248217 date 20240409 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1650382917 to receiver [ZZ] 1801579548, interchange 189654654 date 240510 time 0800 version 00501 usage P; group HP control 189654654 date 20240510 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 41
