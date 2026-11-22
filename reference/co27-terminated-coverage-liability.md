# CO-27 terminated coverage: may the balance be billed to the patient?

> Retrieved 2026-08-12. Every rule carries a primary-source citation.
>
> **Retrieval caveat.** The egress proxy returned 403 for every primary domain (`cms.gov`,
> `x12.org`, `ecfr.gov`, MAC and payer sites): **no primary page was opened directly**. Citations came
> via indexed search over the named document — its phrasing, not verbatim verification.
> *(paraphrase)* = lead, not quote. **practice** = behaviour, not rule.

## Short answer

The CO group code settles it **only on a Medicare FFS remittance**, where CMS states that providers
may bill a beneficiary only when an adjustment carries group code PR. Elsewhere the group code is
the payer's *assertion*; the binding instrument is the participation agreement's hold-harmless
clause plus state law. Those clauses run to **Members / Covered Persons for Covered Services**, and
someone whose coverage ended before the DOS is usually outside them — so CO-27 on a commercial remit
does **not** automatically create a write-off. Medicaid is state rule, and the states split.

## Conditions table

| Condition | Disposition | Source |
|---|---|---|
| **Medicare FFS** remit shows CO-27 | **Do not bill patient.** "Providers may bill Medicare beneficiaries for an unpaid portion only when an adjustment shows Group Code PR" *(paraphrase)* | [CMS MLN, Remittance Advice Resources and FAQs, ICN 905367](https://www.cms.gov/Outreach-and-Education/Medicare-Learning-Network-MLN/MLNProducts/Downloads/ICN905367TextOnly.pdf); [Medicare Claims Processing Manual Ch. 22](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c22.pdf) |
| CARC 27 from a **primary payer on an MSP claim**, Medicare still liable | **Bill the successor payer, not the patient.** Here CARC 27 signals primary coverage ended mid-stay; Medicare may pay | [First Coast (FCSO), MSP ORM](https://medicare.fcso.com/billing/medicare-secondary-payer-msp-ongoing-responsibility-medicals-orm) |
| Person **never Medicare-entitled** on the DOS | Not a Medicare claim; the PR-only rule governs Medicare RAs, not a non-beneficiary encounter. Self-pay under state law | [42 CFR 424 subpart C](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-424/subpart-C) |
| **Medicaid**, not eligible on DOS, **Florida** | **May bill recipient**, if provider informed of liability and documented it *before* rendering | [Fla. Admin. Code 59G-1.050](https://ahca.myflorida.com/content/download/5921/file/59G-1.050_General_Medicaid_Policy.pdf) |
| **Medicaid**, provider verified and told beneficiary coverage was valid, **New York** | **May not bill** — cannot reverse position after treating on a verified card | [NY Medicaid Update 2014-02](https://www.health.ny.gov/health_care/medicaid/program/update/2014/2014-02.htm) |
| **Medicaid**, denial traceable to provider error/inaction | **May not bill** | [SD Medicaid, Billing a Recipient](https://dss.sd.gov/docs/medicaid/providers/billingmanuals/General/Billing_a_Recipient.pdf); [42 CFR 447.15](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-C/part-447/subpart-A/section-447.15) (binds provider as to amounts paid for **eligible individuals**) |
| **Commercial/exchange**, terminated after the ACA 3-month grace period, DOS in month 2-3 | **May bill the member for full billed charges** — the rule contemplates these claims being denied and makes the issuer warn providers first | [45 CFR 156.270](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-B/part-156/subpart-C/section-156.270); [Health Net provider manual, IFP grace period](https://providerlibrary.healthnetcalifornia.com/epo/provider-manual/eligibility/provider-responsibility-for-verifying-eligibility-for-ifp-member.html); [Colorado DOI Bulletin B-4.77](https://doi.colorado.gov/sites/doi/files/documents/Bulletin-B-4.77-Grace-Period-Considerations-for-Consumers-Providers-and-Carriers.pdf) |
| **Commercial**, DOS in **month 1** of the grace period | **Do not bill** — issuer must pay | [45 CFR 156.270](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-B/part-156/subpart-C/section-156.270) |
| **Commercial**, retro-termination beyond the state's retro-denial window | **Appeal first.** Several states cap retroactive ineligibility denials (6 / 12 / 18 months); a time-barred reversal is the payer's problem, not the patient's | [CT OLR 2007-R-0205 survey of state limits](https://www.cga.ct.gov/2007/rpt/2007-R-0205.htm); [NY DFS OGC Op. 02-11-29](https://www.dfs.ny.gov/insurance/ogco2002/rg021129.htm) |
| **Successor coverage exists** on the 271 (`EB*R`, effective on/before DOS) | **Rebill the successor payer.** Patient billing is premature in every line of business | — |

## Why CO vs PR does not settle it (or does)

CARC 27 is "Expenses incurred after coverage terminated"; N30 is "Patient ineligible for this
service" ([X12 CARC list](https://x12.org/codes/claim-adjustment-reason-codes),
[RARC list](https://x12.org/codes/remittance-advice-remark-codes)). Neither carries a group-code
restriction: the X12 lists define reasons, and CAS01 selection is the payer's under the 835 TR3.

**CO** applies when *a contractual agreement between payer and payee, or a regulatory requirement*
caused the adjustment; **PI** exists where the payer believes the amount is not the patient's
responsibility **but no supporting contract exists**
([BCBSNC 835 companion guide](https://www.bluecrossnc.com/content/dam/bcbsnc/pdf/providers/network-participation/hipaa/835-5010-v3-0.pdf)).
A non-member on the DOS is on its face outside the contract — which is why CO-27 is defensibly a
mis-selection. Hold-harmless clauses read the same way: they bar billing a **Covered Person** for
**Covered Services under the Agreement**
([Health Net](https://providerlibrary.healthnetcalifornia.com/medicare/provider-manual/claims-provider-reimbursement/balance-billing/hold-harmless-provisions-medicare-cmc.html)).
Medicare is the exception proving the point: there the group code *is* the rule, because CMS made it
one by program instruction rather than by contract.

## The 271 as evidence

A 271 showing termination before DOS is the **factual predicate** for self-pay; its absence makes
patient billing indefensible. It is **not** a shield the other way — companion guides state the 271
is *not a guarantee of payment*, benefits remaining subject to eligibility at time of service ([BCBSNC 270/271 guide](https://www.bluecrossnc.com/content/dam/bcbsnc/pdf/providers/network-participation/hipaa/270-271-5010-eligibility-v3-2.pdf)).
**No general detrimental-reliance protection exists.** Exceptions are jurisdictional: NY Medicaid
(above), and state retro-denial statutes limiting the *payer's* look-back. Retain the 271 regardless
— it distinguishes "verified active, terminated retroactively" from "never verified."

## Open questions

- **No primary source I reached answers the literal question** — may a provider bill a patient over
  a commercial payer's CO-27. Authority exists for the general rule (CO = provider liability) and the
  exception's premise (hold harmless covers members only); nothing joins them. Treat the commercial
  rows as reasoned from contract structure, not a cited holding.
- **Prevailing practice** (not rule): billers request a corrected 835 or call to confirm the
  termination date, then bill the patient once the payer confirms no coverage — rather than writing
  off on the group code alone. No primary source endorses *or* forbids this.
- **CAQH CORE 360** publishes permitted CARC/group-code combinations per business scenario
  ([rule PDF](https://www.caqh.org/hubfs/CARCsRARCs_835_Rule.pdf)). If its Scenario 3 list permits
  CO-27, the mis-coding argument weakens sharply. **I could not retrieve that list** — highest-value
  lookup remaining.
- **Medicaid is 50 rules, not one.** FL and NY point opposite ways on identical facts. Resolve by
  state; generalise neither.
