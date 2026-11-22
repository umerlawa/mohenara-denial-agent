# Case MOH2-000063

Patient MICHAEL MARTINEZ, DOB 1967-12-25, sex M, member ID HST615122592. Payer: DELAWARE VALLEY MUTUAL. Service date 2026-08-19.

## Adjudication outcome (835)
Claim PA24685180: status 4 (denied). Billed $127, paid $0, patient responsibility . Filing indicator CI (commercial insurance). Payer claim control 2626505616209, POS 11 (office), frequency 1 (original claim).
Payment: $0 by NON (no payment), handling H.
production date (405): 2026-09-22.
Payer [PR]: DELAWARE VALLEY MUTUAL; 900 SHIPLEY RD; WILMINGTON, DE, 198033012; contact BL PROVIDER SERVICES TE 8005551234.
Payee [PE]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900.
Trace (1 (current transaction trace)): EFT900177217, originator 1155019382.
claim statement period start (232): 2026-08-19.
Payee TJ (federal tax ID): 794935003.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments | Remarks |
|---|---|---|---|---|---|---|
| 1 | 97140 | 1 | $48.78 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $48.78 | HE N822 (missing procedure modifier(s)) |
| 2 | 97110 | 2 | $78.22 | $0 | CO-16 (Contractual Obligation: claim/service lacks information or has submission/billing error) $78.22 | HE N822 (missing procedure modifier(s)) |

Line item control numbers (REF 6R): PA24685180L1, PA24685180L2.
Remit claim parties: patient [QC]: MICHAEL MARTINEZ; MI (member ID) HST615122592; rendering provider [82]: MARY CLARK; XX (NPI) 1992501921.

## Claim as billed (837P)
Claim PA24685180, total charge $127, POS 11 (office) (facility qualifier B), frequency 1 (original claim). Diagnosis: M1712 (principal, ABK), M6281 (additional, ABF).
Subscriber relationship code 18 (18 = self), payer responsibility P (P = primary), claim filing CI (commercial insurance).
Provider signature Y, assignment A, benefits assigned Y, release of info Y.

| # | Procedure | Units | Charge | Service date (DTP 472) | Dx ptr | Line control (REF 6R) |
|---|---|---|---|---|---|---|
| 1 | 97140 | 1 UN | $48.78 | 2026-08-19 | 1 | PA24685180L1 |
| 2 | 97110 | 2 UN | $78.22 | 2026-08-19 | 1 | PA24685180L2 |

Parties on claim:
- submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; contact IC BILLING OFFICE TE 8005550137
- receiver [40]: DELAWARE VALLEY MUTUAL; 46 (ETIN) 1550193826
- billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; 1400 CONCORD PIKE; WILMINGTON, DE, 198032900; EI (employer ID/EIN) 794935003
- insured/subscriber [IL]: MICHAEL MARTINEZ; MI (member ID) HST615122592; 6806 CHESTNUT AVE; TRENTON, NJ, 08691
- payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826
- referring provider [DN]: THOMAS BERGSTROM; XX (NPI) 1179655839
- rendering provider [82]: MARY CLARK; XX (NPI) 1992501921
- Submission reference TRC54705589, dated 2026-08-27 0800, purpose code 00, structure 0019, type CH.

## Eligibility (270 inquiry / 271 response)
Inquiry for service type 30 (health benefit plan coverage), plan date (291) 2026-08-19.
Inquiry parties: payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: MICHAEL MARTINEZ; MI (member ID) HST615122592.
Subject DOB 1967-12-25, sex M.

Response:
- benefit: 1 (active coverage), coverage level IND, service type 30 (health benefit plan coverage), plan: DELAWARE VALLEY MUTUAL EPO
- plan date (291): 2026-08-19
- eligibility begin (356): 2024-01-01
Response parties: payer [PR]: DELAWARE VALLEY MUTUAL; PI (payer ID) 1550193826; provider [1P]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; insured/subscriber [IL]: MICHAEL MARTINEZ; MI (member ID) HST615122592.
Subject DOB 1967-12-25, sex M.
Eligibility exchange reference ELG67221453, dated 2026-09-27 0800, purpose code 11, structure 0022.

## Clearinghouse acknowledgment (277CA)
Status A2 (accepted for adjudication), claim status code 20 (accepted for processing), date 2026-08-28, action code WQ, amount $127.
D9 (clearinghouse claim number): TRC54705589.
Trace (2 (referenced transaction trace)): TRC54705589.
received date (050): 2026-08-28.
Parties: clearinghouse [AY]: CLEARWAY EDI SERVICES; 46 (ETIN) CWEDI01; submitter [41]: BRANDYWINE MOVEMENT SCIENCES; 46 (ETIN) 794935003; billing provider [85]: BRANDYWINE MOVEMENT SCIENCES; XX (NPI) 1110692305; patient [QC]: MICHAEL MARTINEZ; MI (member ID) HST615122592.
Acknowledgment reference ACK54705589, dated 2026-08-28 0800, purpose code 08, structure 0085, type TH.

## Chart note (verbatim)

PT treatment note 2026-08-19. Dx: Unilateral primary osteoarthritis left knee. 97140 (15 min): manual therapy (soft tissue and joint mobilization). 97110 (31 min): therapeutic exercise for strength and ROM. Total timed minutes: 46. Patient tolerated treatment well; skilled services remain medically necessary.

## Transmission envelopes (control data)
- eligibility_270: sender [ZZ] 1110692305 to receiver [ZZ] 1550193826, interchange 796631203 date 260927 time 0800 version 00501 usage P; group HS control 796631203 date 20260927 time 0800 spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1; segments 12
- eligibility_271: sender [ZZ] 1550193826 to receiver [ZZ] 1110692305, interchange 314689408 date 260927 time 0800 version 00501 usage P; group HB control 314689408 date 20260927 time 0800 spec 005010X279A1; transaction 271 control 0001 impl 005010X279A1; segments 13
- claim_837p: sender [ZZ] 794935003 to receiver [ZZ] 1550193826, interchange 869115381 date 260827 time 0800 version 00501 usage P; group HC control 869115381 date 20260827 time 0800 spec 005010X222A1; transaction 837 control 0001 impl 005010X222A1; segments 30
- ack_277ca: sender [ZZ] CWEDI01 to receiver [ZZ] 794935003, interchange 871737040 date 260828 time 0800 version 00501 usage P; group HN control 871737040 date 20260828 time 0800 spec 005010X214; transaction 277 control 0001 impl 005010X214; segments 15
- remit_835: sender [ZZ] 1550193826 to receiver [ZZ] 1110692305, interchange 900177217 date 260922 time 0800 version 00501 usage P; group HP control 900177217 date 20260922 time 0800 spec 005010X221A1; transaction 835 control 0001; segments 28
