# Case MOH2-000444

Patient SAMUEL LOPEZ, DOB 1965-11-13, sex F, member ID MTA297421990. Payer: DELAWARE VALLEY MUTUAL. Service date 2026-02-02.

## Adjudication outcome (835)
Claim PA28497427: status 4 (denied). Billed $92.65, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2605666295305, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-02-25.
Payer [PR]: DELAWARE VALLEY MUTUAL; 900 SHIPLEY RD; WILMINGTON, DE, 198033012; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205.
Trace (1 (current transaction trace)): EFT203489459, originator 1155019382.
claim statement period start (232): 2026-02-02.
Payee TJ (federal tax ID): 078865760.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97110 | 1 | $46.18 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $46.18 | HE N822 (missing procedure modifier(s)) |
| 2 | 97112 | 1 | $46.47 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $46.47 | HE N822 (missing procedure modifier(s)) |

Line item control numbers (REF 6R): PA28497427L1, PA28497427L2.
Remit claim parties: patient [QC]: SAMUEL LOPEZ; MI (member ID) MTA297421990; rendering provider [82]: DOROTHY LOPEZ; XX (NPI) 1390221007.

## Claim as billed (837P)
Claim PA28497427, total charge $92.65, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M1712 (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97110 | 1 UN | $46.18 | 2026-02-02 | 1 | PA28497427L1 |
| 2 | 97112 | 1 UN | $46.47 | 2026-02-02 | 1 | PA28497427L2 |

Parties on claim:
- submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: DELAWARE VALLEY MUTUAL; 46 (ETIN) 1550193826
- billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; 77 RIVER TERRACE; HOBOKEN, NJ, 070301205; EI (employer ID/EIN) 078865760
- insured/subscriber [IL]: SAMUEL LOPEZ; MI (member ID) MTA297421990; 1544 LINCOLN ST; STATEN ISLAND, NY, 10368
- payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826
- referring provider [DN]: THOMAS BERGSTROM; XX (NPI) 1179655839
- rendering provider [82]: DOROTHY LOPEZ; XX (NPI) 1390221007
- Submission reference TRC96526380, dated 2026-02-08 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-02-02.
Inquiry parties: payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: SAMUEL LOPEZ; MI (member ID) MTA297421990.
Subject DOB 1965-11-13, sex F.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: DELAWARE VALLEY MUTUAL EPO
- plan date (291): 2026-02-02
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826; provider [1P]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; insured/subscriber [IL]: SAMUEL LOPEZ; MI (member ID) MTA297421990.
Subject DOB 1965-11-13, sex F.
Eligibility exchange reference ELG13233212, dated 2026-03-01 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-02-09, action code WQ, amount $92.65.
D9 (clearinghouse claim number): TRC96526380.
Trace (2 (referenced transaction trace)): TRC96526380.
received date (050): 2026-02-09.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: HUDSON REHAB AND HAND CENTER; 46 (ETIN) 078865760; billing provider [85]: HUDSON REHAB AND HAND CENTER; XX (NPI) 1801579548; patient [QC]: SAMUEL LOPEZ; MI (member ID) MTA297421990.
Acknowledgment reference ACK96526380, dated 2026-02-09 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-02-02. Dx: Unilateral primary osteoarthritis left knee. 97110 (16 min): therapeutic exercise for strength and ROM. 97112 (16 min): neuromuscular re-education of movement and balance. Total timed minutes: 32. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1801579548 to receiver [ZZ] 1550193826, interchange 250924181 date 260301 time 0800 version 00501 usage P; group HS control 250924181 date 20260301 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1550193826 to receiver [ZZ] 1801579548, interchange 930655159 date 260301 time 0800 version 00501 usage P; group HB control 930655159 date 20260301 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 078865760 to receiver [ZZ] 1550193826, interchange 245951618 date 260208 time 0800 version 00501 usage P; group HC control 245951618 date 20260208 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 078865760, interchange 897952714 date 260209 time 0800 version 00501 usage P; group HN control 897952714 date 20260209 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1550193826 to receiver [ZZ] 1801579548, interchange 203489459 date 260225 time 0800 version 00501 usage P; group HP control 203489459 date 20260225 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 28
