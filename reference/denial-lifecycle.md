# Denial Lifecycle — Professional (837P) Claims, US RCM

> Retrieved 2026-08-12. Every rule below carries a primary-source citation.
> Retrieval constraint: direct document fetch (WebFetch/curl) to cms.gov, x12.org and ecfr.gov was blocked by this environment's egress proxy. Rules below were established from search-engine extracts **of the cited primary pages themselves**; no secondary billing blog is cited as authority. Where exact regulatory or code-list wording matters for a runtime decision, re-verify the quoted string against the cited URL. Items that could not be established are in **Open questions**, not guessed.

---

## 1. Decision gate: rejection vs denial

This is the first branch. Everything downstream depends on it. A claim that was **never adjudicated** has no appeal rights, so an appeal filed against it is wasted work and burns the timely-filing clock.

| | **Rejection** | **Denial** |
|---|---|---|
| Where it surfaces | 999 / TA1 (envelope + syntax), 277CA Claim Acknowledgement, or clearinghouse front-end report | 835 Health Care Claim Payment/Advice (ERA) or paper RA |
| Was it adjudicated? | No — stopped at front-end/pre-adjudication edits | Yes — an initial determination was made |
| Carries CARC/RARC? | No. Carries Claim Status Category Code (CSCC) + Claim Status Code (CSC) | Yes. CARC + group code in CAS; RARC as supplemental explanation |
| Appeal rights | None | Yes (payer-specific ladder, §6) |
| Correct action | Fix the data, submit a **new original** claim | Rework (corrected claim), appeal, transfer to patient, write off, or forward to next payer (§4) |
| Source | CMS, *Acknowledgement Transactions (TA1, 999, 277CA)* — https://www.cms.gov/Regulations-and-Guidance/Administrative-Simplification/Versions5010andD0/Downloads/Acknowledgements_National_Presentation_9-29-10_final.pdf ; Novitas, *Understanding the 277CA* — https://www.novitas-solutions.com/webcenter/content/conn/UCM_Repository/uuid/dDocName:00004758 | CMS, *Medicare Claims Processing Manual* Ch. 22 (Remittance Advice) — https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c22.pdf |

**Medicare-specific hard rule.** Medicare calls its rejections "returned as unprocessable." RARC **MA130** reads: *"Your claim contains incomplete and/or invalid information, and no appeal rights are afforded because the claim is unprocessable."* A claim returned as unprocessable *does not meet the criteria to be considered a claim, is not denied, and is not afforded appeal rights*; it has **no redetermination and no Clerical Error Reopening rights**, and can only be fixed by submitting a **new claim** with correct information.
Sources: Noridian (DME MAC), *Incomplete or Invalid Claims Processing Terminology* — https://med.noridianmedicare.com/web/jddme/claims-appeals/claim-submission/terminology ; WPS GHA, *How to Correct a Rejected Claim* — https://www.wpsgha.com/guides-resources/view/318 ; CGS, *Claim Submission Errors / Return Unprocessable Claims* — https://www.cgsmedicare.com/partb/pubs/specman/pdf/specman_claim_submission_errors.pdf

**Payer-type note.** The 277CA is an ASC X12 acknowledgement **adopted by Medicare FFS for error handling; it is not mandated under HIPAA**, so commercial and Medicaid payers vary in whether the biller sees a 277CA, a proprietary clearinghouse report, or both. Do not assume a 277CA exists for every payer.
Source: CMS, *Medicare Claims Processing Manual* Ch. 24 (General EDI and EDI Support) — https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c24.pdf

---

## 2. Transaction sequence for one 837P

| Step | Transaction / artifact | What a failure here means | Source |
|---|---|---|---|
| 1 | 837P submitted | — | CMS 5010A1 837P Companion Guide — https://www.cms.gov/Medicare/Billing/ElectronicBillingEDITrans/downloads/5010a1837bcg.pdf |
| 2 | TA1 (interchange) / 999 (functional) | Envelope or X12 syntax failure. Medicare FFS rejects only submissions out of compliance with the 005010 standard at this layer, responding on the 999 | CMS Acknowledgement Transactions — https://www.cms.gov/Regulations-and-Guidance/Administrative-Simplification/Versions5010andD0/Downloads/Acknowledgements_National_Presentation_9-29-10_final.pdf ; CMS Ch. 24 — https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c24.pdf |
| 3 | 277CA Claim Acknowledgement | Claim-level content edits. Accepted claims get a claim control number; rejected claims get CSCC + CSC in STC | CMS Ch. 24 (above); TMHP *277CA Companion Guide* — https://www.tmhp.com/sites/default/files/file-library/edi/277CA_COMPANION_GUIDE_5010.pdf ; CGS *277CA Edit Lookup Tool* — https://www.cgsmedicare.com/jb/help/5010_277ca_tool.html |
| 4 | Adjudication → 835 ERA (+ EFT) | Paid, adjusted, or denied. Adjustments appear in CAS with group code + CARC; RARC supplies supplemental explanation | CMS Ch. 22 — https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c22.pdf |
| 5 | Post → disposition (§4) | — | HFMA MAP Keys AR-5 / AR-6 — https://www.hfma.org/data-and-insights/map-initiative/map-keys/ |

277CA rejection categories: **A3** and **A7** are rejection Claim Status Category Codes; **A7 = "Acknowledgement/Rejected for Invalid Information."** Category code list is maintained by X12 — https://x12.org/codes/claim-status-category-codes (see Open questions on exact A3 wording).
Source: TMHP 277CA Companion Guide (above); X12 Claim Status Category Codes.

---

## 3. Reading the 835 — the fields that decide disposition

### 3.1 Claim adjustment group codes (CAS01) — this determines who eats the balance

| Group code | Meaning | Can the patient be billed? | Source |
|---|---|---|---|
| **CO** | Contractual Obligation — amounts the provider is financially liable for | **No.** Patient may not be billed for CO amounts | Noridian, *Claim Adjustment Group Codes* — https://med.noridianmedicare.com/web/jddme/topics/ra/claim-adjustment-group-codes ; CMS MLN *Remittance Advice Resources and FAQs* — https://www.cms.gov/outreach-and-education/medicare-learning-network-mln/mlnproducts/downloads/icn905367textonly.pdf |
| **PR** | Patient Responsibility — billable to the patient or to another payer on the patient's behalf | **Yes** | same as above |
| **OA** | Other Adjustment — used where neither CO nor PR fits (e.g. exact-duplicate adjustments) | Neither; informational/other | CAQH CORE 360 rule — https://www.caqh.org/hubfs/CARCsRARCs_835_Rule.pdf |
| **PI** | Payer Initiated Reduction | n/a | CAQH CORE 360 rule (above) |

**Medicare-only restriction:** Medicare contractors may use only **CO, OA and PR**. CMS has **never** permitted Medicare contractors to use **PI**, because PI fails to identify financial liability for the unpaid amount. Commercial payers may use PI.
Source: CMS, *Medicare Claims Processing Manual* Ch. 22 — https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c22.pdf ; CAQH CORE 360 rule — https://www.caqh.org/hubfs/CARCsRARCs_835_Rule.pdf

A group code must always be used **in conjunction with** a CARC; the difference between submitted charge and actual payment must be fully accounted for or the 835 will not balance.
Source: CMS Ch. 22 (above).

### 3.2 Claim status (CLP02)

| Value | Meaning | Lifecycle significance | Source |
|---|---|---|---|
| 22 | Reversal of previous payment | The remit is taking money back; expect a paired corrected/adjustment claim and/or a PLB withhold. Not a new denial to appeal | CMS Ch. 22 — https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c22.pdf |

(Full CLP02 value list: see Open questions.)

### 3.3 CARC/RARC governance

- CARCs explain why a claim or service line was adjudicated differently than billed; RARCs convey supplemental explanation for an adjustment already described by a CARC. Lists are maintained by X12 and updated **three times a year (end of March, July, November)**. Source: X12 code lists — https://x12.org/codes ; Mass.gov 835 Payment Advice and CARC/RARC lists — https://www.mass.gov/info-details/835-payment-advice-and-eobcarc-rarc-lists
- Under the ACA-adopted CAQH **CORE 360** operating rule, health plans must use a uniform set of CAGC/CARC/RARC combinations for four CORE-defined business scenarios: (1) Additional Information Required — Missing/Invalid/Incomplete **Documentation**; (2) Additional Information Required — Missing/Invalid/Incomplete **Data from Submitted Claim**; (3) **Billed Service Not Covered** by Health Plan; (4) **Benefit for Billed Service Not Separately Payable**. Payers may use proprietary combinations only where they do not conflict with or fall within those four scenarios. Source: CAQH CORE 360 rule — https://www.caqh.org/hubfs/43908627/drupal/core/Payment-Remittance-CARCs-RARCs-Rule.pdf ; CMS Operating Rules FAQs — https://www.cms.gov/priorities/key-initiatives/burden-reduction/administrative-simplification/operating-rules/faqs
- **Scenario 1 vs 2 is the rework/appeal fork.** Scenario 2 (missing/invalid data on the claim) is a claim-data defect → rework. Scenario 1 (missing documentation) is a records defect → appeal/redetermination with records attached. Source: CAQH CORE 360 rule (above).

---

## 4. The five dispositions and how to choose

Apply in order. First match wins.

| # | Test on the 835 / 277CA | Disposition | Why | Source |
|---|---|---|---|---|
| 0 | No 835 exists — outcome came on a 277CA/999/clearinghouse report, or RARC **MA130** is present | **Correct and submit a NEW original claim.** Never appeal | Not adjudicated; no appeal rights, no reopening rights | Noridian terminology — https://med.noridianmedicare.com/web/jddme/claims-appeals/claim-submission/terminology ; WPS — https://www.wpsgha.com/guides-resources/view/318 |
| 1 | Denial reason is a **provider-side data/coding defect** on the claim (wrong modifier, DOS, units, POS, NPI, member ID) and payer accepts replacement claims | **Rework — corrected/replacement claim** (§5) | The determination is factually right for what was billed; the billed facts were wrong | UnitedHealthcare, *Claim reconsideration and appeals process* — https://www.uhcprovider.com/en/admin-guides/administrative-guides-manuals-2022/ch10-claims-process-2022/claim-rec-pro-res-dis-ch10-guide.html |
| 1a | Same as #1 but payer is **Medicare Part B FFS** | **Reopening** (clerical error), not a replacement claim and not an appeal | CMS requires clerical-error adjustments to be handled as reopenings; a redetermination request involving a clerical error must be processed as a reopening | CMS, *Medicare Claims Processing Manual* Ch. 34 — https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/downloads/clm104c34.pdf ; CGS *Reopening vs. Redetermination Job Aid* — https://www.cgsmedicare.com/partb/forms/pdf/reopen_vs_redet_jobaid.pdf |
| 2 | Claim data was correct; the **payer's determination is wrong**, or the denial requires clinical documentation / medical necessity / auth argument | **Appeal** (§6) | Appeal is the only channel that changes a determination on the same claim facts | CMS, *First Level of Appeal: Redetermination* — https://www.cms.gov/medicare/appeals-grievances/fee-for-service/first-level-appeal-redetermination-medicare-contractor |
| 3 | Balance carries group code **PR** | **Transfer to patient** (statement / secondary billing) | Only PR amounts may be billed to the beneficiary or another payer on their behalf | Noridian, *Claim Adjustment Group Codes* — https://med.noridianmedicare.com/web/jddme/topics/ra/claim-adjustment-group-codes |
| 3a | Medicare denial as not reasonable and necessary **and** a valid ABN was issued (modifier **GA**) | **Transfer to patient** | With a valid ABN, financial liability shifts to the beneficiary; without one the provider is liable | CMS, *Medicare Claims Processing Manual* Ch. 30 (Financial Liability Protections) — https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c30.pdf ; CMS ABN tutorial MLN909183 — https://www.cms.gov/Outreach-and-Education/Medicare-Learning-Network-MLN/MLNProducts/ABN-Tutorial/formCMSR131tutorial111915f.html |
| 4 | RARC **MA18**, **N89** or **MA07** present on a Medicare remit | **No action — already forwarded.** Do not bill the secondary yourself | Medicare selected the claim for crossover to a COBA trading partner (MA18 = single supplemental payer; N89 = multiple payers simultaneously; MA07 = Medicaid) | CMS COBA Companion Guide — https://www.cms.gov/files/document/hipaacompanionguide101211pdf ; CGS DME MAC Supplier Manual Ch. 7 (Crossover Claims) — https://www.cgsmedicare.com/jc/pubs/pdf/chpt7.pdf |
| 5 | Balance carries **CO**, and no appeal basis survives, or appeal rights are exhausted/absent | **Write off** | CO amounts are provider-liable and cannot be billed to the patient; write-off is the terminal disposition once appeal is exhausted or declined | Noridian group codes (above); HFMA MAP Key **AR-6** defines denial write-offs as the final disposition "where all efforts of appeal have been exhausted or provider chooses to write off" — https://www.hfma.org/data-and-insights/map-initiative/map-keys/ |

**Never simultaneously:** an appeal and a corrected claim on the same DOS/CPT pair. The second submission is at risk of the duplicate edits in §8.

---

## 5. Rework mechanics: corrected/replacement claims

| Payer type | Mechanism | Key constraint | Source |
|---|---|---|---|
| **Medicare Part B FFS (837P)** | **Not available.** The only valid CLM05-3 value is `1` (ORIGINAL); a claim with any other value is rejected. Corrections go through reopening or redetermination | Sending frequency 7 to Medicare Part B produces a rejection, not a correction | CMS 5010A1 837P Companion Guide — https://www.cms.gov/Medicare/Billing/ElectronicBillingEDITrans/downloads/5010a1837bcg.pdf ; CMS Ch. 34 — https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/downloads/clm104c34.pdf |
| **Commercial / Medicaid (where supported)** | 2300 loop **CLM05-3** = `7` (replacement) or `8` (void); **REF01 = `F8`** carries the original payer claim control number | REF F8 is required when CLM05-3 indicates a corrected/replacement claim; sending a replacement without F8 is treated as a fresh original and can duplicate | CMS 837 professional element mapping — https://www.cms.gov/Medicare/Billing/ElectronicBillingEDITrans/downloads/professionalclaim4010a1to5010.pdf ; Mass.gov 837 Companion Document — https://www.mass.gov/doc/companion-guide-ver-10/download |
| **Commercial example — UnitedHealthcare** | Corrected claim via portal or EDI; corrected-claim information must be received **within 180 calendar days of the original remittance date** | Corrected claim ≠ reconsideration. Corrected claims fix submission errors; reconsideration disputes the outcome | UHC Admin Guide Ch.10 — https://www.uhcprovider.com/en/admin-guides/administrative-guides-manuals-2022/ch10-claims-process-2022/claim-rec-pro-res-dis-ch10-guide.html |

---

## 6. Appeal ladders by payer type

### 6.1 Medicare FFS (Part A/B) — 42 CFR Part 405 Subpart I

| Level | Forum | Deadline to file | Decision timeframe | Threshold | Source |
|---|---|---|---|---|---|
| 1 | Redetermination — MAC | **120 days** from receipt of the initial determination (RA/MSN); receipt presumed 5 calendar days after notice date | 60 days | none | CMS *First Level of Appeal* — https://www.cms.gov/medicare/appeals-grievances/fee-for-service/first-level-appeal-redetermination-medicare-contractor |
| 2 | Reconsideration — QIC | **180 days** from receipt of the redetermination notice | — | none | CMS *Second Level of Appeal* — https://www.cms.gov/medicare/appeals-grievances/fee-for-service/second-level-appeal |
| 3 | ALJ hearing — OMHA | **60 days** from receipt of the reconsideration | — | **AIC $200 for CY2026** (up from $190 in CY2025) | CMS *Third Level of Appeal* — https://www.cms.gov/medicare/appeals-grievances/fee-for-service/third-level-appeal ; Federal Register 90 FR (Dec. 4, 2025) AIC notice — https://www.govinfo.gov/content/pkg/FR-2025-12-04/pdf/2025-21879.pdf |
| 4 | Medicare Appeals Council | see Open questions | — | none | CMS appeals index — https://www.cms.gov/medicare/appeals-grievances/fee-for-service |
| 5 | Federal district court | see Open questions | — | **AIC $1,960 for CY2026** | CMS *Fifth Level of Appeal* — https://www.cms.gov/medicare/appeals-grievances/fee-for-service/fifth-level-appeal ; FR AIC notice (above) |

**Evidence rule that changes level-1/2 strategy.** A provider or supplier (or a beneficiary represented by one) that submits evidence for the first time at the OMHA/ALJ level must show **good cause** under §405.1028 for not producing it earlier; the ALJ or attorney adjudicator examines new evidence for good cause and may exclude it. Practical consequence: **all documentation must be filed by the QIC reconsideration, not held back.**
Source: 42 CFR 405.1018 / 405.1028 — https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-405/subpart-I/subject-group-ECFR18c5ab80164e759

**Form.** A redetermination must be requested in writing, either on **Form CMS-20027** or as a written request containing the required information; the form is recommended but not required, and supporting documentation should be attached to the request.
Source: CMS *First Level of Appeal* (above); Form CMS-20027 — https://www.cms.gov/medicare/cms-forms/cms-forms/downloads/cms20027.pdf

### 6.2 Medicare FFS — reopening (not an appeal)

| | Reopening | Redetermination |
|---|---|---|
| Use for | Clerical errors, minor errors/omissions | Substantive disagreement with the determination |
| Window | **1 year** from the initial determination without needing good cause | 120 days |
| Note | A redetermination request that involves a clerical error **must be processed as a reopening**; correcting clerical errors through the appeals process is neither cost-efficient nor necessary | — |
| Source | CMS Ch. 34 — https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/downloads/clm104c34.pdf ; WPS *How to Request a Clerical Error Reopening* — https://www.wpsgha.com/guides-resources/view/how-to-request-a-clerical-error-reopening-cer | CMS Ch. 29 — https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c29.pdf |

Reopening is **not available** for claims returned as unprocessable (§1) — those have no CER rights. Source: Noridian terminology — https://med.noridianmedicare.com/web/jddme/claims-appeals/claim-submission/terminology

### 6.3 Medicare Advantage (Part C)

| Rule | Detail | Source |
|---|---|---|
| Standard reconsideration deadline | **60 calendar days** after receipt of the written organization determination notice | 42 CFR 422.582 — https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-422/subpart-M/section-422.582 |
| Plan decision timeframe | MA org must issue a reconsidered determination no later than **60 calendar days** from receipt of a standard reconsideration request where the determination is fully favorable to the enrollee | 42 CFR 422.590 — https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-422/subpart-M/section-422.590 |
| Non-contract provider | Must complete a **Waiver of Liability** statement waiving any right to payment from the enrollee in order to use the enrollee appeal process; an "assignee" is a non-contract provider who formally agrees to waive payment from the beneficiary | CMS *Notices and Forms* (Managed Care) — https://www.cms.gov/medicare/appeals-grievances/managed-care/notices-forms ; 42 CFR Part 422 Subpart M — https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-422/subpart-M |
| Contracted provider payment disputes | Governed by the provider contract, not Subpart M — see UHC MA non-contracted dispute/appeal rights doc for one plan's split — https://www.uhcprovider.com/content/dam/provider/docs/public/health-plans/medicare/MA-Non-Cont-Provider-Dispute-Appeal-Rights.pdf | (as cited) |

### 6.4 Medicaid

| Rule | Detail | Source |
|---|---|---|
| Claim filing limit (FFS baseline) | The State agency **must require providers to submit all claims no later than 12 months from the date of service** | 42 CFR 447.45 — https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-C/part-447/subpart-A/section-447.45 |
| Managed care appeals | An MCO/PIHP/PAHP may have **only one level of appeal for enrollees**; after an upheld adverse benefit determination the enrollee may request a **State fair hearing**; if the plan fails the §438.408 notice/timing requirements the enrollee is **deemed to have exhausted** the plan's process | 42 CFR 438.402 — https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-C/part-438/subpart-F/section-438.402 ; 42 CFR 438.408 — https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-C/part-438/subpart-F/section-438.408 |
| Continuation of benefits | Requires an appeal about termination/suspension/reduction of previously authorized services ordered by an authorized provider, within the unexpired authorization period; enrollee must request State fair hearing and continuation within **10 calendar days** of the adverse appeal resolution notice | 42 CFR 438.420 — https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-C/part-438/subpart-F/section-438.420 |
| Everything else | State-specific. Deadlines, forms and provider-dispute channels are set by the State plan / State Medicaid manual, not by federal rule | 42 CFR Part 438 Subpart F — https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-C/part-438/subpart-F |

**Do not apply Medicare appeal deadlines to Medicaid.** The 120/180/60-day ladder in §6.1 is Original Medicare only.

### 6.5 Commercial / ERISA group health plans

| Rule | Detail | Source |
|---|---|---|
| Claimant appeal window | Plans must give claimants **at least 180 days** after receiving an adverse benefit determination to appeal | 29 CFR 2560.503-1 — https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XXV/subchapter-G/part-2560/section-2560.503-1 |
| Provider standing | The rules do not preclude an **authorized representative** of a claimant from pursuing a claim or appeal on the claimant's behalf — the usual route for a provider to use the member's ERISA appeal rights | 29 CFR 2560.503-1 (above) |
| Content of denial notice | Must state the specific reason(s) and reference the specific plan provisions relied on | 29 CFR 2560.503-1 (above) |
| Review independence | Review may not defer to the initial determination and must not be conducted by the original decision-maker or their subordinate; medical-judgment appeals require consultation with an appropriately trained health care professional | 29 CFR 2560.503-1 (above) |
| Internal + external review | Non-grandfathered plans additionally follow the internal claims/appeals and external review rules | 45 CFR 147.136 — https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-B/part-147/section-147.136 ; 29 CFR 2590.715-2719 — https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XXV/subchapter-L/part-2590/subpart-C/section-2590.715-2719 |
| Payer-contract track (example) | UnitedHealthcare runs a 2-step process — Step 1 Claim Reconsideration, Step 2 Appeal — with **12 months total** to complete both | UHC *Pre- and post-service appeals and reconsiderations* — https://www.uhcprovider.com/en/claims-payments-billing/appeals.html ; UHC Admin Guide Ch.10 — https://www.uhcprovider.com/en/admin-guides/administrative-guides-manuals-2022/ch10-claims-process-2022/claim-rec-pro-res-dis-ch10-guide.html |

**Two distinct commercial tracks.** A provider dispute under the *participation contract* (reconsideration/provider appeal) is not the same as the member's *ERISA benefit appeal*. Underpayment and contract-rate disputes go to the first; medical-necessity and benefit denials can go to either, and the ERISA route requires the member's authorization.

### 6.6 Out-of-network claims under the No Surprises Act

| Step | Timing | Source |
|---|---|---|
| Open negotiation | **30 business days** | 45 CFR 149.510 — https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-B/part-149 |
| Initiate Federal IDR | **4-business-day window beginning on the 31st business day** after open negotiation started | CMS Federal IDR materials — https://www.cms.gov/nosurprises/notices ; DOL Notice of IDR Initiation — https://www.dol.gov/sites/dolgov/files/ebsa/laws-and-regulations/laws/no-surprises-act/notice-of-idr-initiation.pdf |
| Remit signalling | CMS publishes required RARCs for NSA-related remittance information | CMS, *Guidance on Required Remittance Advice Remark Codes* — https://www.cms.gov/cciio/programs-and-initiatives/other-insurance-protections/caa-nsa-rarc-codes.pdf |

Parties may still settle after the negotiation period closes and before the IDR entity issues a determination. Source: CMS Federal IDR Operations Final Rule fact sheet — https://www.cms.gov/newsroom/fact-sheets/federal-independent-dispute-resolution-operations-final-rule

---

## 7. "Do not resubmit" — when resubmitting is actively harmful

| Signal | Why resubmitting hurts | Correct action | Source |
|---|---|---|---|
| **CARC 18** — *"Exact duplicate claim/service (Use only with Group Code OA except where state workers' compensation regulations requires CO)"*, often with RARC **N522** | Medicare exact-duplicate edits are **hard-coded**; MACs **cannot override or bypass** them. Claims/lines determined to be exact duplicates are **rejected and do not have appeal rights** | Check claim status first; if you believe the duplicate finding is wrong, use **Telephone Reopenings**, not a new claim | CMS, *Medicare Claims Processing Manual* Ch. 1 — https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/Downloads/clm104c01.pdf ; X12 CARC list — https://x12.org/codes/claim-adjustment-reason-codes ; Noridian *Reason Code 18 / Remark Code N522* — https://med.noridianmedicare.com/web/jddme/topics/ra/denial-resolution/n522-b18 |
| Repeat duplicate submissions from the same billing entity | Contractors must run continuing analysis of duplicate claim receipts and identify responsible providers; if a provider keeps submitting duplicates after education, the MAC **initiates program integrity action**, with possible referral to the OIG for fraud or abuse | Fix the AR workflow (status check before rebill), not the claim | CMS Ch. 1 — https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/Downloads/clm104c01.pdf |
| **MA18 / N89 / MA07** on a Medicare remit | Medicare already forwarded the claim to the supplemental payer / Medicaid via COBA. A manual secondary submission creates a duplicate at the secondary payer | Wait for the secondary payer's remit | CMS COBA Companion Guide — https://www.cms.gov/files/document/hipaacompanionguide101211pdf ; CGS Supplier Manual Ch. 7 — https://www.cgsmedicare.com/jc/pubs/pdf/chpt7.pdf |
| **MUE denial where MAI = 2** (absolute per-day date-of-service edit based on policy — anatomy, code definition, or published CMS policy) | Units above the MUE value deny **with or without an appropriate modifier**; re-billing with a modifier will not clear it. MACs may pay excess units on appeal for MAI **1** or **3**, not for MAI 2 | Re-code to the correct code/units, or dispute the coding basis; do not re-bill the same units with modifiers | CMS *Medicare NCCI Medically Unlikely Edits* — https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits/medicare-ncci-medically-unlikely-edits-mues ; Noridian MUE — https://med.noridianmedicare.com/web/jeb/topics/claim-submission/medically-unlikely-edits |
| An appeal is already pending on the same claim | A second original claim for the same DOS/line is an exact duplicate by construction (see row 1) | Wait for the appeal decision | CMS Ch. 1 (above) |
| Modifier 59 / X{EPSU} used only to clear a PTP edit | Modifier 59 or an X-modifier should be used **only if no other modifier describes the service**; NCCI policy is published annually in the NCCI Policy Manual | Verify the services are genuinely distinct and documented before re-billing | CMS *NCCI Coding Policy Manual* — https://www.cms.gov/files/document/2025nccimedicarepolicymanualcompletepdf.pdf ; Noridian NCCI — https://med.noridianmedicare.com/web/jfa/topics/claim-submission/ncci |

**Rejections are the exception.** Resubmission is the *only* remedy for a 277CA rejection or an MA130 unprocessable return — those never adjudicated, so no duplicate record exists to collide with. Source: WPS — https://www.wpsgha.com/guides-resources/view/318

---

## 8. Timely-filing clocks — the constraint that removes options

| Payer type | Claim filing limit | Effect of a rejection | Source |
|---|---|---|---|
| Medicare FFS | **1 calendar year from the date of service** for services on/after 1/1/2010 | Claims rejected as unprocessable are **not considered submitted claims** for timely-filing purposes; the corrected claim must still land within 12 months of DOS. The original rejected submission does **not** hold the date | 42 CFR 424.44 — https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-424/subpart-C/section-424.44 ; CMS *Timely Filing Requirements for Medicare FFS Claims* — https://www.cms.gov/Medicare/Medicare-Fee-for-Service-Payment/ProspMedicareFeeSvcPmtGen/downloads/Health_Reform_Timely_Filing_Provider_Notice.pdf ; Noridian *Timely Filing* — https://med.noridianmedicare.com/web/jeb/topics/claim-submission/timely-filing ; WPS — https://www.wpsgha.com/guides-resources/view/318 |
| Medicare FFS — exceptions | The filing period is extended where CMS or a contractor determines the failure was caused by error or misrepresentation of an employee, contractor, or agent of HHS acting within scope of authority | narrow; does not cover ordinary rejections | 42 CFR 424.44 (above); CMS notice (above) |
| Medicaid | State must require submission **no later than 12 months from DOS** (federal floor; states may be stricter) | state-specific | 42 CFR 447.45 — https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-C/part-447/subpart-A/section-447.45 |
| Commercial | Contract-defined. Example: UHC allows **180 calendar days from the original remittance date** for corrected-claim information and **12 months total** for reconsideration + appeal | contract-specific | UHC Admin Guide Ch.10 — https://www.uhcprovider.com/en/admin-guides/administrative-guides-manuals-2022/ch10-claims-process-2022/claim-rec-pro-res-dis-ch10-guide.html ; UHC appeals — https://www.uhcprovider.com/en/claims-payments-billing/appeals.html |

Timely-filing denial code: **CARC 29**, *"The time limit for filing has expired."* Noridian (DME MAC) guidance states such denials do not carry appeal rights except where the delay was caused by circumstances outside the supplier's control (e.g. act of nature). Treat that as contractor guidance, not universal — see Open questions.
Source: Noridian *Reason Code 29 / Remark Code N211* — https://med.noridianmedicare.com/web/jddme/topics/ra/denial-resolution/n211-29 ; Mass.gov CARC list — https://www.mass.gov/doc/companion-guide-carc-memo-0/download

---

## 9. Ownership — derived from what each rule requires

Each row states who must act because a cited rule makes that actor's input mandatory. Job titles vary by organization (see Open questions).

| Step | What the rule requires | Therefore owned by | Source |
|---|---|---|---|
| 277CA / MA130 rejection | A **new claim** carrying corrected data elements | Billing/EDI (claim-data owner). Not appeals staff | WPS — https://www.wpsgha.com/guides-resources/view/318 |
| Status check before any rebill | Providers must verify adjudication status via portal/IVR before submitting another claim, and should bill all same-DOS services on one claim | AR follow-up / denial management | Noridian *Reason Code 18 / N522* — https://med.noridianmedicare.com/web/jddme/topics/ra/denial-resolution/n522-b18 ; CGS *Top Five Claim Denials — Duplicate Denials* — https://www.cgsmedicare.com/partb/mr/top5/duplicate_denials.html |
| Medicare appeal filing | Written request by a **party**, on CMS-20027 or equivalent, with supporting documentation attached | The billing provider/supplier as appellant | CMS *First Level of Appeal* — https://www.cms.gov/medicare/appeals-grievances/fee-for-service/first-level-appeal-redetermination-medicare-contractor |
| Clinical documentation assembly | All evidence must be in by the QIC level or good cause must be shown at OMHA | Clinical/HIM, before level 2 — not deferrable to level 3 | 42 CFR 405.1018 / 405.1028 — https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-405/subpart-I/subject-group-ECFR18c5ab80164e759 |
| MA non-contract appeal | Signed **Waiver of Liability** relinquishing payment from the enrollee | Provider entity with authority to waive revenue (finance/contracting), not the biller alone | CMS *Notices and Forms* — https://www.cms.gov/medicare/appeals-grievances/managed-care/notices-forms |
| Shifting liability to a Medicare patient | Valid ABN obtained **before** the service; GA modifier on the claim | Front-desk/clinical intake at time of service; coding applies the modifier | CMS Ch. 30 — https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c30.pdf |
| Patient statement | Only PR-coded balances may be billed to the patient | Patient financial services, gated on the 835 group code | Noridian group codes — https://med.noridianmedicare.com/web/jddme/topics/ra/claim-adjustment-group-codes |
| Overpayment/recoupment response | Rebuttal within 15 days is **not** an appeal; only an appeal request triggers §935 limitation on recoupment | Finance/AR must route to appeals to stop recoupment | CMS *Limitation on Recoupment (935)* — https://www.cms.gov/Research-Statistics-Data-and-Systems/Monitoring-Programs/recovery-audit-program/downloads/Section935Recoupment.pdf ; CMS Financial Management Manual Ch. 4 — https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/fin106c04pdf.pdf |
| Write-off approval | Terminal disposition after appeals exhausted or declined; tracked as HFMA MAP Key **AR-6** (denial write-offs / average monthly net patient service revenue), alongside **AR-5** remittance denial rate | Revenue cycle leadership | HFMA MAP Keys — https://www.hfma.org/data-and-insights/map-initiative/map-keys/ |

---

## 10. Money moving backward: reversals and recoupment

| Event | Signal | Rule | Source |
|---|---|---|---|
| Payer reverses a prior payment | 835 **CLP02 = 22**, showing the negating negative amount; the corrected adjustment claim appears separately | Do not treat the reversal line as a fresh denial to appeal; pair it with its adjustment claim before posting | CMS Ch. 22 — https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c22.pdf |
| Medicare overpayment demand | Demand letter; PLB-level adjustments on the ERA per the X12 835 TR3 | Recoupment under §935 may begin **no earlier than day 41** and only if no valid redetermination request was received in that period | CMS *Limitation on Recoupment (935)* — https://www.cms.gov/Research-Statistics-Data-and-Systems/Monitoring-Programs/recovery-audit-program/downloads/Section935Recoupment.pdf ; 42 CFR 405.379 — https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-405/subpart-C/subject-group-ECFRcb4be12070a402f/section-405.379 |
| Rebuttal | 15 days from the demand letter to submit a statement why recoupment should not proceed | **Rebuttal statements are not appeal requests** and do not trigger §935 | CMS §935 material (above); Noridian *Elements of a Demand Letter* — https://med.noridianmedicare.com/web/jadme/claims-appeals/overpayments/elements-of-a-demand-letter |
| Appeal reverses the overpayment | Adjustments made to the overpayment and interest; interest paid to the provider where funds were recouped and later reversed at ALJ or beyond | — | 42 CFR 405.379 (above) |

---

## 11. Frequently-cited CARC/RARC anchors

Exact code text is maintained by X12 and updated in March, July and November. Verify strings at https://x12.org/codes before quoting them to a payer.

| Code | Text as published | Lifecycle meaning | Source |
|---|---|---|---|
| CARC 18 | Exact duplicate claim/service (Use only with Group Code OA except where state workers' compensation regulations requires CO) | Duplicate — see §7 | X12 — https://x12.org/codes/claim-adjustment-reason-codes ; Mass.gov CARC memo — https://www.mass.gov/doc/companion-guide-carc-memo-0/download |
| CARC 29 | The time limit for filing has expired | Timely filing — §8 | Mass.gov CARC memo (above); Noridian — https://med.noridianmedicare.com/web/jddme/topics/ra/denial-resolution/n211-29 |
| CARC 96 | Non-covered charge(s) | Coverage denial; group code determines patient vs provider liability | CMS transmittal R2372CP — https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/downloads/R2372CP.pdf |
| CARC 197 | Precertification/authorization/notification/pre-treatment absent (payment denied/reduced for absence of, or exceeded, pre-certification/authorization) | Auth denial — appeal track, often with retro-auth request | CMS transmittal R2372CP (above); Mass.gov CARC list — https://www.mass.gov/doc/claim-adjustment-reason-codes-and-remittance-advice-remark-codes-carcs-and-rarcs-posted-2122026-0/download |
| CARC 204 | This service/equipment/drug is not covered under the patient's current benefit plan | Benefit denial; check for PR vs CO | Mass.gov CARC list (above) |
| RARC MA130 | Your claim contains incomplete and/or invalid information, and no appeal rights are afforded because the claim is unprocessable | Rejection, not denial — §1 | Noridian — https://med.noridianmedicare.com/web/jddme/claims-appeals/claim-submission/terminology ; CGS — https://www.cgsmedicare.com/partb/pubs/specman/pdf/specman_claim_submission_errors.pdf |
| RARC N522 | (paired with CARC 18 on Medicare duplicate denials) | Duplicate — §7 | Noridian — https://med.noridianmedicare.com/web/jddme/topics/ra/denial-resolution/n522-b18 |
| RARC MA18 / N89 / MA07 | Crossover to a COBA trading partner: MA18 individual supplemental payer, N89 multiple payers simultaneously, MA07 Medicaid | Do not bill the secondary — §7 | CMS COBA Companion Guide — https://www.cms.gov/files/document/hipaacompanionguide101211pdf ; CGS Ch. 7 — https://www.cgsmedicare.com/jc/pubs/pdf/chpt7.pdf |

---

## Open questions

- **Exact X12 code strings could not be read at source.** x12.org was blocked by this environment's egress proxy. CARC/RARC text above is reproduced from CMS transmittals and State Medicaid CARC memos that republish the list. Re-verify against https://x12.org/codes/claim-adjustment-reason-codes and https://x12.org/codes/remittance-advice-remark-codes before quoting verbatim to a payer.
- **CSCC A3 exact wording.** A3 and A7 were confirmed as 277CA rejection categories, and A7 as "Acknowledgement/Rejected for Invalid Information." The canonical text for A3 (and the full A1/A2/A6 set) was not retrievable; see https://x12.org/codes/claim-status-category-codes.
- **Full CLP02 claim status value list.** Only CLP02 = 22 (reversal of previous payment) was confirmed from CMS Ch. 22. The values for paid-as-primary, denied, and processed-as-secondary were not confirmed at source; see the X12 835 TR3 and CMS Ch. 22 §https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c22.pdf.
- **Medicare Appeals Council (level 4) and federal district court filing deadlines** were not confirmed in this pass; only the CY2026 AIC amounts were. Verify at https://www.cms.gov/medicare/appeals-grievances/fee-for-service.
- **Whether timely-filing (CARC 29) denials carry appeal rights** is stated as "no appeal rights except circumstances outside the supplier's control" by Noridian's DME MAC guidance. It was not possible to confirm whether every MAC and every jurisdiction treats a timely-filing denial as a non-appealable event versus an appealable initial determination. Do not generalize this to Part B, Medicaid or commercial payers.
- **Suspect-duplicate vs exact-duplicate handling.** CMS Ch. 1 establishes that *exact* duplicates are hard-coded, non-overridable, rejected and without appeal rights. Whether *suspect* duplicate denials are appealable, and the exact CMS definition separating the two, could not be confirmed at source; contractor pages point both ways.
- **Whether a provider may file a Medicaid managed-care appeal in their own name** (as opposed to as the enrollee's authorized representative) is state-specific and was not established from 42 CFR 438 subpart F in this pass.
- **Commercial payer deadlines are contract-specific.** Only UnitedHealthcare's published timeframes (180 days corrected claim; 12 months total reconsideration + appeal) were verified. Do not apply them to Aetna, Cigna, Elevance/Anthem, or BCBS plans without reading that payer's provider manual.
- **Role titles for step ownership** (denial analyst, AR follow-up, coder, appeals specialist, patient financial services) are operational convention. No primary source defines an RCM org chart; §9 instead derives ownership from what each cited rule requires the actor to supply.
- **First-pass and appeal-overturn rate benchmarks** were not gathered. HFMA MAP Keys AR-5 (remittance denial rate) and AR-6 (denial write-offs as % of net patient service revenue) are the industry-standard definitions — https://www.hfma.org/data-and-insights/map-initiative/map-keys/ — but current benchmark values were not retrieved.
