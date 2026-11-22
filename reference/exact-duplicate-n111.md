# Exact duplicate: `OA-18` + `N111`

> Retrieved **2026-08-12**. Every rule below carries a primary-source citation.
>
> **Retrieval conditions.** Direct HTTP fetching of `x12.org`, `cms.gov`, `ecfr.gov` and the MAC
> domains was refused by this environment's egress proxy (403 to CONNECT). Rule text below was
> retrieved by **domain-restricted search over those same primary domains**, so the cited URL is
> the authoritative source but the wording is a retrieved excerpt, not a verbatim full-text read.
> Where that limit bites on a specific claim, it is named in **§10 Open questions** rather than
> smoothed over.
>
> **Scope.** Written for the corpus signature `OA-18` + `N111` on **Medicare Part B (FFS)**,
> which is where the 13 `exact_duplicate` cases sit. Commercial rules differ and are flagged where
> they appear.
>
> **This file supersedes** the three conflicting exact-duplicate dispositions recorded in
> `README.md` §4 C3 (`denial-lifecycle.md` §7, `carc-rarc-remedies.md` §5, and
> `resubmission-and-frequency-codes.md` §5). See **§9**.

---

## 0. The decision in one table

| What is actually true | Disposition | Never |
|---|---|---|
| **True duplicate** — the same service, already adjudicated on a prior claim | **No further action.** The prior claim's determination governs the money. Post the original claim's outcome and close the account. `do_not_resubmit`. | Do not resubmit in any form. Do not bill the patient. |
| **False duplicate** — a legitimately repeated/distinct service on the same day that the payer matched as a duplicate because no distinguishing modifier was on the line | Add the distinguishing modifier (**76 / 77 / 91**, or the site/laterality/E-M modifier that actually describes it) and put that line back in front of the payer — on Part B as a **new original claim** for the affected line(s), or by **reopening**. | Do not re-send the line unchanged; do not send frequency `7` to Part B. |
| **Payer matched wrongly** — different beneficiary/DOS/provider, or no prior adjudicated claim exists | Contest the duplicate finding: **reopening first** (telephone/portal/CER, MAC-dependent), redetermination where the MAC's published duplicate guidance directs an appeal with documentation | Do not run an appeal and a resubmission on the same DOS/CPT at once |

Group code `OA` is on this denial in every corpus case: **the balance is never patient responsibility**, whichever branch you land in (§2).

---

## 1. The two codes

| Code | Type | Official text | Source |
|---|---|---|---|
| **18** | CARC | "Exact duplicate claim/service **(Use only with Group Code OA except where state workers' compensation regulations requires CO)**" | [X12, Claim Adjustment Reason Codes](https://x12.org/codes/claim-adjustment-reason-codes); restated verbatim by [Palmetto GBA JJ Part B — CARC 18](https://dominoapps.palmettogba.com/palmetto/jjb.nsf/DIDC/PCAF563WNL~Claims~Denial%20Resolution%20Tool) and [CMS Transmittal R2372CP, *Claim Adjustment Reason Code* update](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/downloads/R2372CP.pdf) |
| **N111** | RARC | "**No appeal right except duplicate claim/service issue. This service was included in a claim that has been previously billed and adjudicated.**" | [X12/WPC, Remittance Advice Remark Codes](https://x12.org/codes/remittance-advice-remark-codes) (list **maintained by CMS** — see below); quoted by [Noridian JE Part B, *How to Verify Claim Denial Resolutions Efficiently*](https://med.noridianmedicare.com/web/jeb/article-detail/-/view/10525/how-to-verify-claim-denial-resolutions-efficiently): "Duplicate claims will normally contain the remark code N111: No appeal right except duplicate claim/service issue"; also carried in [CMS MM11880](https://www.cms.gov/files/document/mm11880.pdf) |
| **OA** | Group code | "A group code identifies the general category of payment adjustment and must always be used in conjunction with a claim adjustment reason code to show liability for amounts not covered by Medicare for a claim or service." OA = **Other Adjustment**, used where neither CO nor PR fits. | [CMS, *Medicare Claims Processing Manual* Pub. 100-04 Ch. 22 (Remittance Advice)](https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/Downloads/clm104c22.pdf) |

**Who maintains what** (matters when a payer argues about wording): "**CMS is the national maintainer of the remittance advice remark code list**," used by reference in the ASC X12N 835; the **Health Care Code Maintenance Committee** maintains the claim adjustment reason codes, meeting each X12 trimester (February, June, October), with both lists reposted **three times a year**.
Source: [CMS MM6229, *Remittance Advice Remark Code (RARC) and Claim Adjustment Reason Code (CARC) update*](https://www.cms.gov/outreach-and-education/medicare-learning-network-mln/mlnmattersarticles/downloads/mm6229.pdf); [CMS Transmittal R743CP](https://www.cms.gov/transmittals/downloads/R743CP.PDF). A RARC carries no money: remark codes "represent non-financial information critical to understanding the adjudication" ([Novitas, *Electronic Billing Guide Ch. 10 — CARC/RARC/Group Codes*](https://www.novitas-solutions.com/webcenter/portal/MedicareJH/pagebyid?contentId=00004554)).

**Note on the pairing.** The corpus pairs `18` with `N111`; **DME MACs** pair `18` with `N522` ([Noridian JA DME, *Reason Code 18 | Remark Code N522*](https://med.noridianmedicare.com/web/jadme/topics/ra/denial-resolution/n522-b18)). `N522` guidance is DME-jurisdiction guidance and should not be applied to a Part B professional claim without checking it.

---

## 2. Why the group code is `OA` and not `CO`

| Question | Answer | Source |
|---|---|---|
| Is `OA` a payer choice? | **No.** The X12 code note on CARC 18 restricts it: "*Use only with Group Code OA except where state workers' compensation regulations requires CO.*" A Medicare Part B remit showing `CO-18` is off-code. | [X12 CARC list](https://x12.org/codes/claim-adjustment-reason-codes); [Palmetto GBA JJ Part B — CARC 18](https://dominoapps.palmettogba.com/palmetto/jjb.nsf/DIDC/PCAF563WNL~Claims~Denial%20Resolution%20Tool) |
| Why not `CO`? | `CO` asserts that "a contractual agreement between the payer and payee, or a regulatory requirement, resulted in an adjustment" — i.e. an amount the provider must absorb *under this claim's adjudication*. A duplicate adjustment is not a reduction of an allowed amount at all: **nothing was adjudicated here**, because the service was already adjudicated on the prior claim. There is no contractual write-off to assert. | [CMS Pub. 100-04 Ch. 22](https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/Downloads/clm104c22.pdf) |
| What does `OA` positively mean here? | `OA` is the residual category — liability is **not stated**. It points you off this claim and onto the prior one. Medicare also uses `OA` in the neighbouring "you filed this to the wrong place" situations, e.g. claims denied because the provider "misfiled a claim to the incorrect Medicare contractor office." | [CMS Pub. 100-04 Ch. 22](https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/Downloads/clm104c22.pdf); [CMS Transmittal R2229CP](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/downloads/R2229CP.pdf) |
| Financial consequence | Only **`PR`** transfers liability to the beneficiary. `OA-18` therefore **never** supports billing the patient, and never supports a contractual write-off either — writing it off silently destroys the payment that may already exist on the original claim. | [CMS Pub. 100-04 Ch. 22](https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/Downloads/clm104c22.pdf); consistent with `carc-rarc-remedies.md` §2 |

Practical read of an `OA-18` line: **this is not a denial of the service. It is a statement that this claim is not the place where the service gets decided.**

---

## 3. `N111` and the appeal-rights question — resolving the conflict with `denial-lifecycle.md` §7

`denial-lifecycle.md` §7 asserts flatly that exact duplicates "are **rejected and do not have appeal rights**." `N111` on the same remit says there is no appeal right *except* on the duplicate claim/service issue. Both are quoting real sources; the flat version is **over-broad**. The reconciliation is in CMS Pub. 100-04 Ch. 1 §120 and its clarifying transmittal:

| Rule | Text | Source |
|---|---|---|
| Exact duplicates are hard-coded | "Exact duplicates are controlled by the claims processing system through '**hard coded**' edits, and may not be user-controlled. In addition, **Medicare contractors cannot override or bypass exact duplicate edits.**" | [CMS Pub. 100-04 Ch. 1 §120, *Detection of Duplicate Claims*](https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/Downloads/clm104c01.pdf); [CMS Transmittal R2678CP, *Clarification of Detection of Duplicate Claims Section*](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/Downloads/R2678CP.pdf) |
| Exact duplicates carry no appeal rights | "All exact duplicate claims or claim lines are **auto-denied or rejected** (absent appropriate modifiers)… Claims or claim lines that have been determined to be an **exact duplicate are rejected and do not have appeal rights.**" | [R2678CP](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/Downloads/R2678CP.pdf); [CMS Pub. 100-04 Ch. 1 §120.2](https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/Downloads/clm104c01.pdf) |
| …**but the duplicate finding itself is contestable** | "**The denial of a claim as a duplicate of another claim may be appealed when the denial is based on criteria other than those specified above for exact duplication.**" (i.e. suspect-duplicate determinations — §4) | [R2678CP](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/Downloads/R2678CP.pdf); [CMS Pub. 100-04 Ch. 1 §120.3](https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/Downloads/clm104c01.pdf) |
| A Part B MAC's own duplicate-appeal instruction | If you appeal a duplicate denial, "**documentation supporting that the service(s) was not a duplicate**" must be submitted, "for each service billed (including those paid)." | [Palmetto GBA JJ Part B — CARC 18](https://dominoapps.palmettogba.com/palmetto/jjb.nsf/DIDC/PCAF563WNL~Claims~Denial%20Resolution%20Tool) |

**Resolution — state it this way, not the flat way.** `N111` is not a contradiction of CMS policy; it is CMS policy written onto the remit. What is closed and what is open:

- **Closed:** the merits of the service under *this* claim number. They were decided on the prior claim. If you disagree with that decision, the appeal belongs to the **original** claim's determination and runs on the original remit's 120-day clock, not this one.
- **Closed:** arguing the exact-duplicate edit itself. It is hard-coded and no contractor can bypass it.
- **Open (the `N111` carve-out):** whether this was a duplicate at all. That is the "duplicate claim/service issue," and it is the only live question on this remit. A denial resting on **suspect**-duplicate criteria rather than exact-duplicate criteria is expressly appealable (R2678CP).

So `denial-lifecycle.md` §7 is right that you cannot appeal your way into a second payment for the same service, and wrong if read as "nothing about this denial can be challenged."

---

## 4. The decisive distinction: true duplicate vs false duplicate

CMS distinguishes two edit populations. Everything downstream turns on which one you are in.

| | **Exact duplicate** (true duplicate) | **Suspect duplicate** (candidate false duplicate) |
|---|---|---|
| Definition | A claim/claim line that matches an already-received claim on the system's match elements, **absent appropriate modifiers** | Claims/lines with "closely-aligned elements sufficient to suggest that duplication may be present and, as such, require that the suspect claim be reviewed" |
| Handling | Auto-denied or rejected by hard-coded edit; contractors cannot override or bypass | Reviewed by contractor local software modules, or suspended for contractor review |
| Appeal rights | **None** on the exact-duplicate determination | **Appealable** ("denial… may be appealed when the denial is based on criteria other than those specified above for exact duplication") |
| Criteria published? | Match elements for professional claims: **same beneficiary, same provider, same date of service, same CPT/HCPCS** (across more than one claim number) | **No** — "the criteria for identifying suspect duplicate claims submitted by physicians and other suppliers are **not published** and vary according to the type of billing entity, type of item or service being billed, and other relevant criteria" |
| Source | [CMS Pub. 100-04 Ch. 1 §120.2](https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/Downloads/clm104c01.pdf); [R2678CP](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/Downloads/R2678CP.pdf); match elements per [CMS RAC topic 0091, *Duplicate Claims — Professional Services*](https://www.cms.gov/research-statistics-data-and-systems/monitoring-programs/medicare-ffs-compliance-programs/recovery-audit-program/approved-rac-topics-items/0091-exact-duplicate-claims) | [CMS Pub. 100-04 Ch. 1 §120.3](https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/Downloads/clm104c01.pdf); [R2678CP](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/Downloads/R2678CP.pdf) |

**The false duplicate is a coding failure, not a payer failure.** CMS says so directly: "Correct coding rules applicable to all billers of health care claims **encourage the appropriate use of condition codes or modifiers to identify claims that may appear to be duplicates, but, in fact, are not**," and "identical services being repeated should be submitted using CPT modifier **76**, **77**, or **91**."
Source: [R2678CP](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/Downloads/R2678CP.pdf); [CMS Pub. 100-04 Ch. 1 §120](https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/Downloads/clm104c01.pdf).

### 4.1 Modifiers that distinguish a repeat/distinct service

| Modifier | Use | Source |
|---|---|---|
| **76** | "Repeat procedure by same physician" — the same service repeated the same day, subsequent to the original, by the same physician/QHP. **The first service is submitted without `76`; the repeat service(s) carry `76`.** | [CMS MCD Article A53482, *Billing and Coding: Repeat or Duplicate Services on the Same Day*](https://www.cms.gov/medicare-coverage-database/view/article.aspx?articleId=53482); [R2678CP](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/Downloads/R2678CP.pdf) |
| **77** | "Repeat procedure by another physician" — same service repeated the same day by a different physician. On some services, "failure to use CPT modifier 77 **and submit the necessary documentation** will result in denial." | [A53482](https://www.cms.gov/medicare-coverage-database/view/article.aspx?articleId=53482) |
| **91** | "Repeat clinical diagnostic laboratory test" — where the same lab test must be repeated the same day to obtain multiple results. | [A53482](https://www.cms.gov/medicare-coverage-database/view/article.aspx?articleId=53482); [R2678CP](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/Downloads/R2678CP.pdf) |
| **59 / XE, XP, XS, XU** | Distinct procedural service — a different session, practitioner, site, or non-overlapping service. Use only where no other modifier describes it. | [CMS MLN1783722, *Proper Use of Modifiers 59, XE, XP, XS & XU*](https://www.cms.gov/files/document/mln1783722-proper-use-modifiers-59-xe-xp-xs-xu.pdf) |
| **RT / LT** (and site/laterality modifiers) | Different anatomic site. First Coast, on `OA18` specifically: "ensure necessary appropriate modifiers are appended to claim lines… **Append the applicable modifier(s) to the procedure code even if the diagnosis indicates the exact site of the procedure**" — e.g. `RT`/`LT`. | [First Coast, *Tips to prevent claim adjustment reason code OA18*](https://medicare.fcso.com/claims/tips-prevent-claim-adjustment-reason-code-oa18) |

**Two failure modes when using `76`** — both create the denial they were meant to prevent:
- Do **not** report modifier `76` on multiple claim lines to represent quantity; **report multiple units of service** where appropriate. ([First Coast, *Tips on how to avoid billing a duplicate claim*](https://medicare.fcso.com/claims/tips-how-avoid-billing-duplicate-claim); Novitas reports "an increase in duplicative billing of modifier 76" — [Novitas, *Modifier 76 Fact Sheet*](https://www.novitas-solutions.com/webcenter/portal/MedicareJL/pagebyid?contentId=00092327))
- If repeats must be split across claims, **notate in the narrative why the claim is split**, or the system reads them as an exact duplicate. If the second service is unrelated, carry the diagnosis specific to each procedure on its own line. ([First Coast](https://medicare.fcso.com/claims/tips-how-avoid-billing-duplicate-claim))

**Prevention, which is also the cheapest remedy:** bill **all services rendered on the same date of service on a single claim**. ([Palmetto GBA JJ Part B — CARC 18](https://dominoapps.palmettogba.com/palmetto/jjb.nsf/DIDC/PCAF563WNL~Claims~Denial%20Resolution%20Tool))

### 4.2 Telling them apart from the case artifacts

1. **Check claim status before anything else.** Every MAC leads with this: verify the original claim's adjudication status in the portal or IVR before rebilling. Noridian: "Before rebilling any claim, review the Noridian Medicare Portal in Claim inquiry for status of initial claim to avoid another denial"; its IVR "will skip duplicate denial and provide **original claim status**." Palmetto: use eServices or the IVR "to verify claim adjudication status of the initial claim submission before submitting another claim." NGS: "Verify the claim status by utilizing NGSConnex/IVR system before resubmitting."
   Sources: [Noridian JE Part B, *Exact Duplicate Claim/Service*](https://med.noridianmedicare.com/web/jeb/topics/claim-submission/reason-code-guidance/exact-duplicate-claim-service); [Palmetto GBA JJ Part B — CARC 18](https://dominoapps.palmettogba.com/palmetto/jjb.nsf/DIDC/PCAF563WNL~Claims~Denial%20Resolution%20Tool); [NGS, *Reason Code: OA-18*](https://www.ngsmedicare.com/web/ngs/search-details?selectedArticleId=3953469)
2. **Original still pending?** Then this is a self-inflicted duplicate and there is nothing to do but wait: "Wait until remittance advice received by your office to ensure claim finalized before correcting claim, rebilling claim, or submitting appeal." A duplicate fires "even if the original claim is in a processing status waiting to be paid." ([Noridian JE Part B](https://med.noridianmedicare.com/web/jeb/topics/claim-submission/reason-code-guidance/exact-duplicate-claim-service); [NGS, *How to Avoid Duplicate Claim Denials*](https://www.ngsmedicare.com/web/ngs/how-to-avoid-duplicate-claim-denials))
3. **Was the service genuinely performed twice / at two sites / by two physicians?** If yes and the line carries no `76`/`77`/`91`/`59-X`/`RT`/`LT`, you are in the **false-duplicate** branch (§6).
4. **Was there no prior adjudicated claim at all** (front-end 277CA rejection, or a claim under a different beneficiary/DOS)? Then the match is wrong — §7. Note the boundary: a claim that died at the front end (999/277CA) or was returned unprocessable **never adjudicated**, so it has no payer claim control number and cannot be the "previously billed and adjudicated" claim `N111` refers to.

---

## 5. True duplicate — the disposition, stated plainly

**Take no further action. Do not resubmit.** The prior claim's determination governs; post that outcome (payment, or its own denial with its own appeal rights) and close this claim. There is no version of a resubmission that clears an exact-duplicate edit, because the edit is hard-coded and no contractor can bypass it ([CMS Pub. 100-04 Ch. 1 §120](https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/Downloads/clm104c01.pdf); [R2678CP](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/Downloads/R2678CP.pdf)).

### Why resubmitting makes things worse — five mechanisms

| # | Mechanism | Source |
|---|---|---|
| 1 | Every 837 arriving with `CLM05-3 = 1` is treated as a brand-new claim — "all claim submissions are considered new claims" — so it is matched against the already-adjudicated claim and **re-fires the same edit**. You buy another `OA-18` and nothing else. | [NGS, *How to Avoid Duplicate Claim Denials*](https://www.ngsmedicare.com/web/ngs/how-to-avoid-duplicate-claim-denials) |
| 2 | The Part B escape hatch other payers offer is **unavailable**: the CMS 837P companion guide restricts `CLM05-3`, and Medicare Part B/DME FFS does not accept a `7` replacement. So "send it as a corrected claim" is not an option on this payer. | [CMS 837P Companion Guide](https://www.cms.gov/Medicare/Billing/ElectronicBillingEDITrans/downloads/5010a1837bcg.pdf); [NGS](https://www.ngsmedicare.com/web/ngs/how-to-avoid-duplicate-claim-denials) ("When a claim processes, a provider should follow the reopening or appeal process to make corrections to the claim") |
| 3 | A correction sent without a valid frequency code "will deny as a duplicate **and the original claim number or DCN will not be adjusted**" — the original stays wrong and the correction is lost, so the AR looks worked when nothing happened. | [BCBSOK CPCP025, *Corrected Claim Submissions*](https://www.bcbsok.com/docs/provider/ok/standards/cpcp/cpcp025-corrected-claim-submissions-01-02-25.pdf) (commercial policy, cited for the failure mode) |
| 4 | Auto-rebill loops manufacture the denial at scale; payers explicitly ask billers to stop clearinghouse auto-rebill early — "only auto-rebill claims after 30 days and ensure they are not resubmitting your claims after 14 days." | [Noridian JE Part B, *Exact Duplicate Claim/Service*](https://med.noridianmedicare.com/web/jeb/topics/claim-submission/reason-code-guidance/exact-duplicate-claim-service) |
| 5 | Repeat duplicate submission is a **program-integrity** exposure, not just noise: contractors run continuing analysis of duplicate claim receipts, educate the responsible provider, and escalate if it continues. Duplicate payments across claim numbers for the same beneficiary/CPT/date/provider are a standing **RAC recovery topic**. | [CMS RAC topic 0091, *Duplicate Claims — Professional Services*](https://www.cms.gov/research-statistics-data-and-systems/monitoring-programs/medicare-ffs-compliance-programs/recovery-audit-program/approved-rac-topics-items/0091-exact-duplicate-claims); [CMS Pub. 100-04 Ch. 1 §120](https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/Downloads/clm104c01.pdf). *`denial-lifecycle.md` §7 additionally reports an OIG-referral clause attributed to Ch. 1; that specific clause was **not re-confirmed verbatim in this retrieval** — see §10.* |

**Also never:** an appeal and a resubmission running at the same time on the same DOS/CPT. A second original claim while an appeal is pending is an exact duplicate **by construction**.

**And never bill the patient.** `OA` states no liability (§2).

---

## 6. False duplicate — putting a legitimately repeated service back in front of Medicare Part B

The line was denied because, on the payer's match elements, it looked identical. The fix is to make it **not identical** by carrying the modifier that describes what actually happened, then getting that corrected line adjudicated.

| Route | When | Detail | Source |
|---|---|---|---|
| **Resubmit the affected line(s) as a new original claim (`CLM05-3 = 1`), now carrying the distinguishing modifier** | The modifier was simply missing from your submission | First Coast, on `OA18`: "ensure necessary appropriate modifiers are appended to claim lines, if applicable, and **resubmit the claim**." This works because the exact-duplicate edit matches "absent appropriate modifiers" — a correctly modified line is no longer an exact match. Resubmit the corrected line(s), not the whole paid claim, or the already-paid lines duplicate. | [First Coast, *Tips to prevent CARC OA18*](https://medicare.fcso.com/claims/tips-prevent-claim-adjustment-reason-code-oa18); [CMS Pub. 100-04 Ch. 1 §120.2](https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/Downloads/clm104c01.pdf); line-level scope per [Palmetto GBA JJ Part B — CARC 18](https://dominoapps.palmettogba.com/palmetto/jjb.nsf/DIDC/PCAF563WNL~Claims~Denial%20Resolution%20Tool) |
| **Clerical-error reopening to add the modifier** | Where the MAC accepts a modifier addition as a minor omission | "A contractor **must** process clerical errors (which includes minor errors and omissions) as reopenings, instead of as redeterminations." A reopening may be requested **within 1 year** of the initial determination for any reason. **Limit:** a reopening cannot be used "to add items or services not previously billed." | [42 CFR 405.980](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-405/subpart-I/subject-group-ECFR70fab268832aef1/section-405.980); [Novitas, *How to Correct Claim Errors by Clerical Error Reopening or Requesting a Redetermination*](https://www.novitas-solutions.com/webcenter/portal/MedicareJH/pagebyid?contentId=00134860) |
| **Not available: frequency `7` corrected claim** | — | Medicare Part B / DME FFS does not accept it. Do not populate `resubmission_frequency_code` for Part B. | [CMS 837P Companion Guide](https://www.cms.gov/Medicare/Billing/ElectronicBillingEDITrans/downloads/5010a1837bcg.pdf); [NGS](https://www.ngsmedicare.com/web/ngs/how-to-avoid-duplicate-claim-denials) |

**Clock constraint that can eliminate the resubmission route entirely:** a new original claim must still land **within 1 calendar year of the date of service** (42 CFR 424.44 — see `timely-filing.md` §2.1). If the duplicate denial arrives late in that year, reopening (1 year from the *determination*) may be the only surviving door.

**Commercial payers only:** the `7` + `REF*F8` corrected-claim path in `resubmission-and-frequency-codes.md` §5 applies there, not to Part B.

---

## 7. The duplicate finding is believed wrong on Medicare Part B — which door?

Answer in order. The route is **reopening, not appeal**, in the ordinary case; the appeal exists but is the fallback, and a redetermination is not a way to re-argue the service's merits.

| Step | Action | Why / authority |
|---|---|---|
| 1 | **Verify status of the original claim first** (portal / IVR). The IVR skips the duplicate denial and returns the original claim's status. | [Noridian JE Part B, *Exact Duplicate Claim/Service*](https://med.noridianmedicare.com/web/jeb/topics/claim-submission/reason-code-guidance/exact-duplicate-claim-service); [Palmetto GBA JJ Part B](https://dominoapps.palmettogba.com/palmetto/jjb.nsf/DIDC/PCAF563WNL~Claims~Denial%20Resolution%20Tool); [NGS](https://www.ngsmedicare.com/web/ngs/search-details?selectedArticleId=3953469) |
| 2 | **Reopening** — the published route for "denied duplicate in error." Noridian states it explicitly: "If a supplier feels a claim denied duplicate in error, **contact Telephone Reopenings**." Have the claim **ICN** ready; Noridian requires the ICN for a telephone reopening, and since 1/1/2024 corrections available through Self-Service Reopenings must be done on the Noridian Medicare Portal. | [Noridian JE Part B, *Exact Duplicate Claim/Service*](https://med.noridianmedicare.com/web/jeb/topics/claim-submission/reason-code-guidance/exact-duplicate-claim-service); [Noridian, *Self Service Reopenings (Part B)*](https://med.noridianmedicare.com/web/portalguide/inquiry-guide/claim-status/self-service-reopenings-part-b) |
| 2a | **On Novitas (the corpus's Part B payer): "telephone reopening" is not the name of the door.** Novitas's clerical-error-reopening channels are the **Novitasphere portal**, the **IVR automated claim corrections** service, and the faxed/mailed **Part B Redetermination and Clerical Error Reopening Request Form (FP152)**. A CER "allows you to change claim data without submitting a written appeal… to correct minor errors or omissions of claim specific information." **Redeterminations may not be filed by telephone.** | [Novitas, *How to Correct Claim Errors by Clerical Error Reopening or Requesting a Redetermination*](https://www.novitas-solutions.com/webcenter/portal/MedicareJH/pagebyid?contentId=00134860); [Novitas, *Automated Claim Corrections via the IVR*](https://www.novitas-solutions.com/webcenter/portal/MedicareJH/pagebyid?contentId=00132380); [Novitas, *IVR User Guide for Conducting Unlimited Part B Claim Corrections*](https://www.novitas-solutions.com/webcenter/portal/MedicareJH/pagebyid?contentId=00086538); [Novitas, *Tutorial: Completing the FP152 form*](https://www.novitas-solutions.com/webcenter/portal/MedicareJH/pagebyid?contentId=00002683) |
| 3 | **Know what a reopening is not.** "Reopenings are separate and distinct from the appeals process and are **not a party's right**"; all decisions to grant a reopening are at contractor discretion, and a decision **to reopen or not to reopen is itself not appealable**. Third-party payer error does not count as clerical error. So the reopening can simply be refused, with no further recourse on that request. | [CMS Pub. 100-04 Ch. 34, *Reopening and Revision of Claim Determinations*](https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/downloads/clm104c34.pdf); [42 CFR 405.980](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-405/subpart-I/subject-group-ECFR70fab268832aef1/section-405.980); [42 CFR 405.926](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-405/subpart-I/subject-group-ECFRba80b2c5e3f1227/section-405.926) |
| 4 | **Redetermination (appeal)** — available where the denial rests on **suspect**-duplicate criteria rather than exact duplication, and it is the route MAC duplicate guidance points to when you are asserting the services were distinct. File within **120 days of receipt of the determination notice**, with "documentation supporting that the service(s) was not a duplicate… for each service billed (including those paid)." | [R2678CP](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/Downloads/R2678CP.pdf); [Palmetto GBA JJ Part B — CARC 18](https://dominoapps.palmettogba.com/palmetto/jjb.nsf/DIDC/PCAF563WNL~Claims~Denial%20Resolution%20Tool); [Novitas, *Appeals Reference Guide — Medicare Part B*](https://www.novitas-solutions.com/webcenter/portal/MedicareJH/pagebyid?contentId=00002675); [CMS, *First Level of Appeal: Redetermination*](https://www.cms.gov/medicare/appeals-grievances/fee-for-service/first-level-appeal-redetermination-medicare-contractor) |
| 5 | **What a redetermination will not do:** re-decide the underlying service on this claim number (that determination lives on the original claim), or override the exact-duplicate edit. And a pure billing error is not an appeal matter — Palmetto: once a billing error is identified and corrected, the claim is resubmitted as a new claim; billing errors are not sent in as first-level appeals. | [R2678CP](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/Downloads/R2678CP.pdf); [Palmetto GBA JJ Part B](https://dominoapps.palmettogba.com/palmetto/jjb.nsf/DIDC/PCAF563WNL~Claims~Denial%20Resolution%20Tool) |

**Do not confuse this with `MA130`.** An `MA130` unprocessable return has **no appeal and no reopening rights** and is fixed only by a new corrected claim ([Novitas](https://www.novitas-solutions.com/webcenter/portal/MedicareJH/pagebyid?contentId=00134860)). `MA130` appears in zero corpus cases; `OA-18` + `N111` is a different animal — it is an adjudicated outcome with a payer claim control number.

---

## 8. Decision table keyed to what you can observe

| Observed | Family | Disposition |
|---|---|---|
| `OA-18` + `N111`, `$0` paid, 277CA shows accepted (A2/status 20), 835 CLP carries a payer claim control number, prior claim finalized and **paid** | `exact_duplicate`, true | **No further action.** Post the original's payment; close. Do not resubmit; do not bill patient (`OA`). |
| Same, prior claim finalized and **denied** for its own reason | `exact_duplicate`, true | No action on this claim. Work the **original** claim's denial on its own remit and its own 120-day appeal clock. |
| Same, prior claim **still pending / not finalized** | `exact_duplicate`, true (self-inflicted) | **Hold.** Do nothing until the original finalizes. |
| Same, but the DOS genuinely carries a repeated/distinct service and the line has **no** `76`/`77`/`91`/`59-X`/`RT`/`LT` | `exact_duplicate`, false | Add the modifier; resubmit the affected line(s) as a new `1` (Part B), or seek a clerical-error reopening. Watch the 1-year-from-DOS claim clock. |
| Same, but no prior adjudicated claim exists, or the match is against a different beneficiary/DOS/provider | duplicate finding wrong | Reopening first (§7 step 2/2a); redetermination as the fallback with documentation for each service billed. |
| `CO-18` on a Medicare Part B remit | off-code | The X12 note restricts 18 to `OA` outside workers' comp. Treat the group code as suspect and re-read the remit before acting on liability. |
| No 835 at all (999/277CA rejection, or `MA130` return) | not a duplicate at all | Never adjudicated → no duplicate record to collide with. Correct and submit a **new** claim. |

---

## 9. What this corrects in the rest of `reference/`

| File | Its claim | Correction |
|---|---|---|
| `denial-lifecycle.md` §7 | Exact duplicates "are rejected and **do not have appeal rights**" (flat) | Right about the merits and about the exact-duplicate edit; **over-broad as written**. `N111` preserves the duplicate-issue question, and R2678CP makes suspect-duplicate denials appealable. Use §3 wording. |
| `denial-lifecycle.md` §7 | Pairs CARC 18 with `N522` | `N522` is the **DME MAC** pairing. The Part B corpus pairing is `N111`. Do not import DME guidance. |
| `carc-rarc-remedies.md` §5 (CARC 18) | "If a repeat service: add the appropriate modifier/condition code and resubmit corrected line(s) only" | **Correct, but only for the false-duplicate branch**, and on Part B the resubmission must be a new `1` (frequency `7` is unavailable). Not a disposition for a true duplicate. |
| `resubmission-and-frequency-codes.md` §5 | "needs correction → `7` with `REF*F8`" | **Not available on Medicare Part B / DME FFS** — that file's own §6 says so. Commercial only. |
| `README.md` §4 C3 | "Three files give three answers and none resolves Medicare Part B" | Resolved here: the three answers are three different branches of one decision (§0), and the Part B route is reopening-first (§7). |

---

## 10. Open questions

Cited gaps. Do not fill these with a plausible guess at runtime; escalate instead.

1. **Verbatim X12/WPC list text not read.** `x12.org` and `cms.gov` were fetch-blocked (403 at the egress proxy). The wording of CARC 18 and RARC N111 in §1 is corroborated across CMS transmittals, a CMS MLN article, and four MACs — but it is a **restatement, not a verbatim read of the WPC/X12 code list**. Anything turning on a single word of the code text should be re-verified against [x12.org](https://x12.org/codes/remittance-advice-remark-codes) from an unblocked network.
2. **`N111` does not tell you whether the edit was exact or suspect.** No source located states that `N111` is reserved for exact duplicates (or `N522` for either). Since appeal rights differ between the two populations (§4), **the remit alone cannot settle which population you are in.** Where the distinction decides the case, treat it as unresolved rather than assuming "exact."
3. **Suspect-duplicate criteria are unpublished by design** — CMS says the criteria for physicians and other suppliers "are not published and vary according to the type of billing entity, type of item or service being billed, and other relevant criteria" ([R2678CP](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/Downloads/R2678CP.pdf)). They cannot be reproduced or predicted from the artifacts.
4. **Rejection vs denial characterization.** Ch. 1 §120.2 says exact duplicates are "auto-denied **or** rejected" and that those "determined to be an exact duplicate are rejected and do not have appeal rights," while the corpus shows an adjudicated 835 with a payer claim control number. Whether a Part B `OA-18` line is formally a non-appealable rejection or an initial determination with a narrowed appeal right was **not settled** in this retrieval. Practical effect is the same (reopening first), but it decides whether a redetermination request is *dismissed* rather than *decided*.
5. **The exact match-element list in Ch. 1 §120.2(B)** (physicians, practitioners and other suppliers except DMEPOS) could not be read verbatim. §4 uses the RAC topic 0091 formulation — same beneficiary, same provider, same date of service, same CPT/HCPCS, across more than one claim number. Do not assert additional match elements (place of service, billed amount, rendering NPI) as authoritative; they appear in MAC prose but were not confirmed in the manual.
6. **Novitas-specific route for a duplicate-denied line is inferred, not published.** Novitas publishes CER channels (Novitasphere, IVR claim corrections, form FP152) and a **["Novitasphere claim correction exclusion code list"](https://www.novitas-solutions.com/webcenter/portal/MedicareJH/pagebyid?contentId=00081421)** that could not be read in this retrieval. **Whether a line denied `OA-18`/`N111` is eligible for a Novitas CER — and specifically whether adding modifier `76`/`77`/`91` to it is accepted as a minor omission rather than refused as "adding a service not previously billed" — is unverified.** For the 13 corpus cases this means: the *disposition* (`do_not_resubmit` for a true duplicate) is solid; the *contest channel* for a wrong finding on Novitas should be treated as portal/CER-or-redetermination, with the exact channel confirmed by the payer before it is asserted to a client.
7. **The OIG-referral escalation clause** attributed to Pub. 100-04 Ch. 1 in `denial-lifecycle.md` §7 was **not re-confirmed verbatim** here. The program-integrity exposure of repeat duplicates is independently supported by the standing RAC recovery topic ([0091](https://www.cms.gov/research-statistics-data-and-systems/monitoring-programs/medicare-ffs-compliance-programs/recovery-audit-program/approved-rac-topics-items/0091-exact-duplicate-claims)); the specific OIG-referral wording should not be quoted to a payer until read in the manual.
