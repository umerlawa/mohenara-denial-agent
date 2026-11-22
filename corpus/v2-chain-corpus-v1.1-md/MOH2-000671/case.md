# Case MOH2-000671

Patient SAMUEL LOPEZ, DOB 1965-11-13, sex F, member ID MTA297421990. Payer: DELAWARE VALLEY MUTUAL. Service date 2026-05-30.

## Adjudication outcome (835)
Claim PA24692219: status 1 (processed as primary, paid). Billed $502.77, paid $46.5, patient responsibility $11.62. Filing indicator CI (commercial insurance). Payer claim control 2620395972464, POS 11 (office), frequency 1 (original claim).
Payment: $46.5 by CHK (check), handling I.
production date (405): 2026-07-22.
Payer [PR]: DELAWARE VALLEY MUTUAL; 900 SHIPLEY RD; WILMINGTON, DE, 198033012; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT217213375, originator 1155019382.
claim statement period start (232): 2026-05-30.
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 | $43.04 | $23.25 allowed (B6) $29.06 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $13.98; PR-2 (Patient Responsibility: coinsurance amount) $5.81 |  |
| 2 | 97110-GP | 1 | $46.99 | $23.25 allowed (B6) $29.06 | CO-45 (Contractual Obligation: charge exceeds fee schedule/maximum allowable, contractual) $17.93; PR-2 (Patient Responsibility: coinsurance amount) $5.81 |  |
| 3 | 97140-GP | 9 | $412.74 | $0 | CO-151 (Contractual Obligation: information does not support this many/frequency of services) $412.74 | HE N362 (the number of days or units exceeds the acceptable maximum) |

Line item control numbers (REF 6R): PA24692219L1, PA24692219L2, PA24692219L3.
Modifiers on remit lines: GP (under PT plan of care).
Remit claim parties: patient [QC]: SAMUEL LOPEZ; MI (member ID) MTA297421990; rendering provider [82]: DOROTHY LOPEZ; XX (NPI) 1390221007.

## Claim as billed (837P)
Claim PA24692219, total charge $502.77, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M1712 (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110-GP | 1 UN | $43.04 | 2026-05-30 | 1 | PA24692219L1 |
| 2 | 97110-GP | 1 UN | $46.99 | 2026-05-30 | 1 | PA24692219L2 |
| 3 | 97140-GP | 9 UN | $412.74 | 2026-05-30 | 1 | PA24692219L3 |

Modifiers on claim: GP (under PT plan of care).

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: DELAWARE VALLEY MUTUAL; 46 (ETIN) 1550193826
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: SAMUEL LOPEZ; MI (member ID) MTA297421990; 1544 LINCOLN ST; STATEN ISLAND, NY, 10368
- payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826
- referring provider [DN]: THOMAS BERGSTROM; XX (NPI) 1179655839
- rendering provider [82]: DOROTHY LOPEZ; XX (NPI) 1390221007
- Submission reference TRC59613783, dated 2026-06-17 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-05-30.
Inquiry parties: payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: SAMUEL LOPEZ; MI (member ID) MTA297421990.
Subject DOB 1965-11-13, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: DELAWARE VALLEY MUTUAL EPO
- plan date (291): 2026-05-30
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: SAMUEL LOPEZ; MI (member ID) MTA297421990.
Subject DOB 1965-11-13, sex F.
Eligibility exchange reference ELG82166452, dated 2026-07-25 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-06-19, action code WQ, amount $502.77.
D9 (clearinghouse claim number): TRC59613783.
Trace (2 (referenced transaction trace)): TRC59613783.
received date (050): 2026-06-19.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: SAMUEL LOPEZ; MI (member ID) MTA297421990.
Acknowledgment reference ACK59613783, dated 2026-06-19 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-05-30. Dx: Unilateral primary osteoarthritis left knee. 97110 (15 min): therapeutic exercise for strength and ROM. 97110 (15 min): therapeutic exercise for strength and ROM. 97140 (16 min): manual therapy (soft tissue and joint mobilization). Total timed minutes: 46. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1550193826, interchange 769466487 date 260725 time 0800 version 00501 usage P; group HS control 769466487 date 20260725 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1550193826 to receiver [ZZ] 1801579548, interchange 397405679 date 260725 time 0800 version 00501 usage P; group HB control 397405679 date 20260725 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1550193826, interchange 898191646 date 260617 time 0800 version 00501 usage P; group HC control 898191646 date 20260617 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 34
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 442072413 date 260619 time 0800 version 00501 usage P; group HN control 442072413 date 20260619 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1550193826 to receiver [ZZ] 1801579548, interchange 217213375 date 260722 time 0800 version 00501 usage P; group HP control 217213375 date 20260722 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 35
