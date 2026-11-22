# Other insurance is primary (CARC 22) — and MA04, which is not the same thing

**Recognise:** 835 carries CARC **22** "care may be covered by another payer per coordination of benefits", commonly with MOA **MA04** (corpus `OA-22` x103, `CO-22` x48; cob-and-eligibility.md §2; CORPUS-CODES.md). Corroborate with a **271 for the DOS**: **`EB*R`** (other or additional payer) plus a 2120 payer loop naming the carrier — MOH2-000087 returns `benefit: R … plan: NOVITAS SOLUTIONS MEDICARE PART B FFS`, `PLAN IS PRIMARY PAYER FOR THIS MEMBER`, against a claim sent `payer responsibility P (primary)` (§5.1–5.2).

**Disposition — split by code, they are different problems.**
- **CARC 22 alone** → `resubmit_other_payer`. Coverage exists; only the **order** is wrong.
- **MA04** → `correct_and_resubmit` **to the same payer**. MA04 is a claim *completeness* defect, not a routing one: the primary's adjudication data is missing. Supply it and resend to this payer. Sending it elsewhere is wrong, and appealing it burns the window for nothing (cob-and-eligibility.md §5.1; rarc-index-corpus.md).

For CARC 22: Bill the true primary, then rebill this payer as secondary carrying the primary's adjudication data. Never appeal a payer that says the claim is not its own (carc-rarc-remedies.md §7).

**Do not:** confuse with **eligibility_terminated**. That is **CARC 27 + N30**, coverage *ended* (`EB*6` with `DTP*357` before the DOS), and the group code picks bill_patient vs write-off. CARC 22 means coverage is active and misordered: `EB*R`, no termination date, **never billable to the patient** under `OA` or `CO`. Do not **appeal MA04** — a completeness rejection; correct and resubmit (§5.1, §6). CARC **109** is not a COB-order question: the payer disclaims the claim outright, usually a Medicare Advantage enrollee — bill the MA plan (§5.4).

| rule | detail | source |
|---|---|---|
| Query date | Run the 270 with `DTP*291` = **the DOS**, never today — order is date-specific | §5.2 (all corpus 270s) |
| `EB*R` proves | Another payer is on the record — *that* one exists, not *which* is primary; order comes from the rows below | §5.2 |
| MSP, employment | Working Aged 65+: GHP primary at **20+** employees; Disability: LGHP at **100+**. Trigger is **current employment status** — retiree/COBRA is not | 42 USC 1395y(b)(1)(A)-(B); 42 CFR 411.170/172/200 |
| MSP, ESRD | GHP primary **30 months**, **no** size threshold, retiree/COBRA counts | 42 USC 1395y(b)(1)(C); 42 CFR 411.162 |
| Non-employment | WC, no-fault, liability, Black Lung, VA primary for the related episode; Medicare may pay conditionally | 42 CFR 411.40, 411.50 |
| Medicaid | **Always last** — payer of last resort by statute | 42 USC 1396a(a)(25); 42 CFR 433.139 |
| Commercial order | non-dependent over dependent → child, parents together: **birthday rule** (earlier **month/day**; year irrelevant) → court decree beats birthday → custodial-parent chain → active over laid-off/retired → active over COBRA → longer coverage | NAIC Model #120 §4.2 |
| Birthday limits | Children only, not spouses. Loses to a decree. N/A when Medicare is involved. N/A to a **self-funded ERISA** plan unless its SPD adopts it — read the SPD. If the other plan uses the gender rule, **that plan's rule sets the order** | NAIC #120 §4.1, 4.3–4.4; 29 USC 1144 |
| Wrong COB record | Medicare: only the **BCRC** can fix it, not the MAC — report, wait for the update, then **resubmit**, not appeal. Hold the claim; the **filing clock keeps running** | CMS COB&R overview; MSP Manual ch.3, ch.5; timely-filing.md |
| Secondary claim, to avoid MA04 | `SBR01=S` (2000B); other payer 2320 `SBR` + 2330B; claim `AMT`+`CAS` (2320); line `SVD`+`CAS` (2430). Any omission → MA04. Must **balance**: billed = paid + adjustments, claim and line | 005010X222A1 TR3 §6 |

Uncertain: whether `OA-22` and `CO-22` differ operationally — corpus holds both, no source explains the choice. Whether commercial payers accept a provider-submitted COB correction or require the member (only BCRC is firm). Every MSP, NAIC and 837 row is a research `pointer` — authority correct, text not retrieved; verify before quoting (§11).
