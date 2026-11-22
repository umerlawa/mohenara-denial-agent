# Resubmission and Claim Frequency Codes

> Retrieved 2026-08-12. Every rule below carries a primary-source citation.
>
> **Retrieval note:** direct HTTP fetching of cms.gov, x12.org, nubc.org, nucc.org, MAC
> sites and payer sites was blocked by this environment's network egress proxy. Rule text
> below was retrieved via domain-restricted search over those same primary domains, so the
> cited URL is the authoritative source and the wording is a retrieved excerpt, not a
> verbatim full-document read. Where two retrieved excerpts of the same document conflict,
> the conflict is recorded in **Open questions** rather than resolved by guessing.
>
> **Scope warning:** the single most common error in this domain is applying a Medicare
> Part A rule to Part B, or a commercial rule to Medicare. Frequency 7/8 is *standard* on
> institutional Medicare and on most commercial payers, and is *not accepted* on Medicare
> Part B professional claims. See §6 before asserting anything.

---

## 1. Where the frequency code physically lives

| Transaction / form | Element | Content | Source |
|---|---|---|---|
| 837 Professional (005010X222A1) | Loop 2300 `CLM05-3` | Claim Frequency Type Code | [UHC 837P Companion Guide 005010X222A1](https://www.uhcprovider.com/content/dam/provider/docs/public/resources/edi/EDI-837P-CG-005010X222A1.pdf) |
| 837 Institutional (005010X223A2) | Loop 2300 `CLM05-1` = facility type, `CLM05-2` = `A` (facility code qualifier, "uniform billing claim form bill type"), `CLM05-3` = claim frequency code | Together these reconstruct the Type of Bill | [BCBSIL, Electronic Replacement/Corrected Claim Submissions](https://www.bcbsil.com/docs/provider/il/claims/submission/claim-frequency-codes-prof.pdf) |
| 837 (both) | Loop 2300 `REF01` = `F8`, `REF02` = payer claim control number / DCN / ICN | Links the replacement or void to the claim it replaces | [X12 RFI #2173, Loop 2300 REF01=F8 Control#](https://x12.org/resources/requests-for-interpretation/rfi-2173-loop-2300-ref01f8-control) |
| CMS-1500 (02/12) paper | Item 22, left field "Resubmission Code" = bill frequency code; right field "Original Ref. No." | "Not intended for use for original claim submissions." Code area 11 chars, Original Reference Number area 18 chars, no hyphens or spaces | [NUCC 1500 Reference Instruction Manual v13, 07/2025](https://www.nucc.org/images/stories/PDF/1500_claim_form_instruction_manual_2025_07-v13.pdf) |
| UB-04 / CMS-1450 paper | FL 4 Type of Bill (frequency = last digit); FL 64 Document Control Number | Frequency digit `7`/`8`; FL 64 carries the original claim number | [Humana, Submitting corrected claims](https://assets.humana.com/is/content/humana/cphp_prcorrectedclaimspdf); [CMS MLN, Loop 2300 REF / FL 64 A-C](https://www.cms.gov/outreach-and-education/mln/wbt/mln7388180-mln-wbt-1450/1450/lesson05/20/index.html) |
| 835 remittance (the *source* of the number you put in REF*F8) | `CLP07` = payer claim control number (payer's internal claim number / ICN / DCN) | This is where the value for `REF*F8` comes from | [CMS 835 Companion Guide](https://www.cms.gov/medicare/billing/electronicbillingeditrans/downloads/5010a1835cg.pdf); [BCBSIL](https://www.bcbsil.com/docs/provider/il/claims/submission/claim-frequency-codes-prof.pdf) (DCN "can be obtained from the 835 Electronic Remittance Advice or Electronic Payment Summary") |

The code list itself is **external code source 235, Claim Frequency Type Code**, maintained by the
NUBC, not by X12. X12 references it; the values are UB-04 bill type frequency digits.
The NUBC has confirmed the UB-04 bill type frequency codes are acceptable for use in the
Professional and Dental TR3s (005010X222 and 005010X224).
Sources: [X12 External Code Lists](https://x12.org/codes);
[NUBC, Bill Type Frequency Codes for use in the 837 Professional and Dental claim transactions](https://www.nubc.org/system/files/media/file/2019/06/billTypeFrequencyCodes837.pdf).

---

## 2. Frequency code values

Medicare's own claim frequency table (CLM_FREQ_CD), which mirrors the NUBC list:

| Code | Meaning | Source |
|---|---|---|
| `0` | Non-payment / zero claim | [CMS Blue Button, Variable CLM_FREQ_CD](https://bluebutton.cms.gov/resources/variables/clm_freq_cd/) |
| `1` | Admit through discharge claim — i.e. the **original**, complete claim | [CMS Blue Button, CLM_FREQ_CD](https://bluebutton.cms.gov/resources/variables/clm_freq_cd/) |
| `2` | Interim — first claim | same |
| `3` | Interim — continuing claim | same |
| `4` | Interim — last claim | same |
| `5` | Late charge(s) only claim | same |
| `6` | Adjustment of prior claim | same |
| `7` | **Replacement of prior claim** | same |
| `8` | **Void / cancel prior claim** | same |
| `9` | Final claim for a HH PPS episode (processed like a debit/credit adjustment to the RAP) | same |
| `Q` | Reopening / reconsideration of a previously adjudicated claim **outside** the payer's timely filing limit | [X12 RFI #2173](https://x12.org/resources/requests-for-interpretation/rfi-2173-loop-2300-ref01f8-control); [CMS Pub 100-04 Ch. 1](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c01.pdf) (Medicare Part A reopenings use `Q` in the 4th position of the Type of Bill) |

**Definitional detail that governs behaviour, not just labelling:**

| Code | Definitional rule | Source |
|---|---|---|
| `7` | Used when a bill already issued for a specific Provider / Patient / Payer / Insured / "Statement Covers Period" "needs to be restated in its entirety." The payer "operates on the principle to void the original bill, and the information present on this bill represents a complete replacement of the previously issued bill." | NUBC UB-04 definition, as reproduced in [NUBC bill type frequency code excerpt](https://www.nubc.org/system/files/media/file/2019/06/billTypeFrequencyCodes837.pdf) |
| `7` | Operational consequence: **every** accurate line from the original must be re-sent. "All accurate line items from the original submission must appear on the replacement claim along with the line items requiring a correction to avoid unintended refund or overpayment requests." | [BCBSOK CPCP025, Corrected Claim Submissions](https://www.bcbsok.com/docs/provider/ok/standards/cpcp/cpcp025-corrected-claim-submissions-01-02-25.pdf) |
| `8` | Removes the claim from the payer's file rather than revising it. Used where the bill previously submitted was wrong in a way that cannot be restated (e.g. it should not exist at all). | [NUBC excerpt](https://www.nubc.org/system/files/media/file/2019/06/billTypeFrequencyCodes837.pdf); [Humana](https://assets.humana.com/is/content/humana/cphp_prcorrectedclaimspdf) ("Void/Cancel of Prior Claim") |
| `5` | Do **not** use `5` (late charges) to submit a correction. Some payers deny it. Late/added charges must go on a full `7` replacement of the entire claim. | [BCBSTX CPCP025 update, late/added charges](https://www.bcbstx.com/provider/standards/standards-requirements/disclosures/2024/03-28-24-cpcp025-corrected-clm-submit-late-added-charge-update); [BCBSIL CPCP025](https://www.bcbsil.com/docs/provider/il/standards/cpcp/2024/cpcp025-07012024.pdf) |
| `6` vs `7` | `6` ("Adjustment of prior claim") exists in the Medicare CLM_FREQ_CD table, but current payer instructions direct providers to `7` for replacement. Do not emit `6` unless a payer companion guide names it. | [CMS Blue Button CLM_FREQ_CD](https://bluebutton.cms.gov/resources/variables/clm_freq_cd/) vs. [BCBSIL](https://www.bcbsil.com/docs/provider/il/claims/submission/claim-frequency-codes-prof.pdf) ("BCBSIL only accepts claim frequency code 7 to replace a prior claim or 8 to void a prior claim") |

---

## 3. The REF*F8 payer claim control number requirement

| Rule | Detail | Source |
|---|---|---|
| TR3 situational rule (837I 005010X223A2, Loop 2300 REF Payer Claim Control Number) | "Required when CLM05-3 (Claim Frequency Code) indicates this claim is a replacement or void to a previously adjudicated claim." | [X12 RFI #2173](https://x12.org/resources/requests-for-interpretation/rfi-2173-loop-2300-ref01f8-control) |
| The TR3 does **not** enumerate which CLM05-3 values count as "replacement or void" | X12 confirmed the situational rule "does not specify which Claim Frequency Code values are considered to be 'replacement' or 'void'". Payers resolve this in their companion guides — in practice `7` and `8`. | [X12 RFI #2173](https://x12.org/resources/requests-for-interpretation/rfi-2173-loop-2300-ref01f8-control) |
| Frequency `Q` (reopening outside timely filing) | X12's response: a reopening within timely filing is sent as a replacement (`7`); a reopening outside timely filing "could be considered a 'replacement' claim and therefore reporting the Loop 2300, REF01=F8 would be appropriate and useful to the payer." | [X12 RFI #2173](https://x12.org/resources/requests-for-interpretation/rfi-2173-loop-2300-ref01f8-control) |
| Segment construction | Original claim number / DCN goes in **Loop 2300 REF02**, with qualifier **F8 in REF01**. | [BCBSIL](https://www.bcbsil.com/docs/provider/il/claims/submission/claim-frequency-codes-prof.pdf); [BCBSNM claim frequency codes](https://www.bcbsnm.com/docs/provider/nm/claim-frequency-codes.pdf) |
| Failure mode if omitted | "Failure to submit without the original claim number or DCN will generate a compliance error and the claim will be rejected." | [BCBSIL](https://www.bcbsil.com/docs/provider/il/claims/submission/claim-frequency-codes-prof.pdf) |
| Do not send it on originals | Payers expect `REF*F8` **only** when CLM05-3 is `7` or `8`. | [EmblemHealth 837P Companion Guide](https://www.emblemhealth.com/content/dam/emblemhealth/pdfs/provider/837P.pdf) |
| Medicare Part A specific | On an adjustment (TOB `XX7`), "the provider inserts the ICN/DCN of the claim to be adjusted." Medicare requires the DCN from the remittance advice showing Medicare's payment for the original claim on adjusted, voided or cancelled claims. | [CMS Pub 100-04 Ch. 1, General Billing Requirements](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c01.pdf) |
| Medicaid (NY example) | "When submitting an Adjustment (Replacement) or a Void to a previously paid claim, the Transaction Control Number (TCN) assigned to the claim intended to be adjusted or voided must be entered," and if a TCN is entered the frequency position of FL 4 must be `7` or `8`. | [NYS Medicaid, General Billing Guidelines (Institutional)](https://www.emedny.org/ProviderManuals/AllProviders/General_Billing_Guidelines_Institutional.pdf) |

**Where to get the number:** the payer's claim control number is returned in **835 CLP07**.
Sources: [CMS 835 Companion Guide](https://www.cms.gov/medicare/billing/electronicbillingeditrans/downloads/5010a1835cg.pdf);
[BCBSIL](https://www.bcbsil.com/docs/provider/il/claims/submission/claim-frequency-codes-prof.pdf).
UHC states the corrected claim carries "the 12-digit original claim number under the Original
Reference Number" ([UHC Administrative Guide Ch.10, Claim correction and resubmission](https://www.uhcprovider.com/en/admin-guides/administrative-guides-manuals-2022/ch10-claims-process-2022/claim-corr-resub-ch10-guide.html)) —
the length is payer-specific, so never validate length generically.

---

## 4. Decision table — which frequency code is correct

| Situation | Correct action | Why / Source |
|---|---|---|
| First submission of this service, never sent before | `1` original, **no** `REF*F8` | [CMS Blue Button CLM_FREQ_CD](https://bluebutton.cms.gov/resources/variables/clm_freq_cd/); [EmblemHealth CG](https://www.emblemhealth.com/content/dam/emblemhealth/pdfs/provider/837P.pdf) |
| Claim was **rejected front-end** (999 / 277CA) or returned as unprocessable — it never reached adjudication and has no payer claim number | Resubmit as `1` original. **Not** `7`. | Rejected claims "do not enter the payer's claim processing system for adjudication but are returned for correction and electronic resubmission" ([UHC, Avoid claim rejections and denials](https://www.uhcprovider.com/en/resource-library/news/2025/avoid-claim-rejections-denials.html)); Medicare unprocessable claims "must be corrected and submitted as a new claim" and have no reopening or redetermination rights ([Noridian, Unprocessable (Return/Reject) Claims Must Be Resubmitted](https://med.noridianmedicare.com/web/jddme/article-detail/-/view/2230703/reminder-unprocessable-return-reject-claims-must-be-resubmitted); [WPS, How to Correct a Rejected Claim](https://www.wpsgha.com/guides-resources/view/318)) |
| Claim **adjudicated** (paid or denied), and the billed content was wrong or incomplete — wrong CPT/HCPCS, wrong or missing modifier, wrong diagnosis, wrong units, wrong DOS, missing line, late/added charges | `7` replacement + `REF*F8` with the original claim number, containing **all** correct lines plus the corrected ones | "A corrected claim is used to update a previously processed claim with new or additional information … should only be submitted if the original claim information was incomplete or inaccurate"; all accurate original lines must reappear ([BCBSOK CPCP025](https://www.bcbsok.com/docs/provider/ok/standards/cpcp/cpcp025-corrected-claim-submissions-01-02-25.pdf)) |
| The claim should not exist at all — billed for the wrong patient, wrong rendering/billing provider, wrong payer, or a duplicate you created | `8` void + `REF*F8`, then file the correct claim as a new `1` | `XX8` is used "when the claim should be removed rather than revised" ([NUBC excerpt](https://www.nubc.org/system/files/media/file/2019/06/billTypeFrequencyCodes837.pdf)); Medicaid: any field "except the Provider ID number or the Member's Medicaid ID number can be adjusted" — those require void + rebill ([NYS Medicaid General Billing Guidelines](https://www.emedny.org/ProviderManuals/AllProviders/General_Billing_Guidelines_Institutional.pdf)) |
| Adding late charges to an already-adjudicated institutional claim | `7` replacing the **entire** claim, not `5` | [BCBSTX CPCP025 late/added charges update](https://www.bcbstx.com/provider/standards/standards-requirements/disclosures/2024/03-28-24-cpcp025-corrected-clm-submit-late-added-charge-update) |
| Original claim still pending / not finalized on the remit | Do nothing. Check status. Do not send `1`, `7`, or `8` yet. | "Wait until remittance advice received by your office to ensure claim finalized before correcting claim, rebilling claim, or submitting appeal" ([Noridian, Exact Duplicate Claim/Service](https://med.noridianmedicare.com/web/jeb/topics/claim-submission/reason-code-guidance/exact-duplicate-claim-service)) |
| Denial is about coverage, medical necessity, or a payment rule you disagree with — the claim as billed was accurate | **Appeal**, not a corrected claim. See §7. | "A corrected claim does not constitute an appeal" ([BCBSOK CPCP025](https://www.bcbsok.com/docs/provider/ok/standards/cpcp/cpcp025-corrected-claim-submissions-01-02-25.pdf)) |
| Medicare Part B (professional) claim already adjudicated and needs correction | **Do not** send `7`. Use a clerical error reopening or a redetermination. See §6. | [CMS 837P Companion Guide](https://www.cms.gov/Medicare/Billing/ElectronicBillingEDITrans/downloads/5010a1837bcg.pdf); [NGS, How to Avoid Duplicate Claim Denials](https://www.ngsmedicare.com/web/ngs/how-to-avoid-duplicate-claim-denials) |

---

## 5. Why resending frequency `1` produces a duplicate denial

The mechanism, stated by payers in their own words:

| Step | Rule | Source |
|---|---|---|
| 1 | Every 837 arriving with `CLM05-3 = 1` is treated as a brand-new claim. "All claim submissions are considered new claims." | [NGS, How to Avoid Duplicate Claim Denials](https://www.ngsmedicare.com/web/ngs/how-to-avoid-duplicate-claim-denials) |
| 2 | The payer's duplicate logic matches the new claim against the already-adjudicated one on provider / member / date of service / procedure and fires an exact-duplicate edit. | [Noridian, Exact Duplicate Claim/Service](https://med.noridianmedicare.com/web/jeb/topics/claim-submission/reason-code-guidance/exact-duplicate-claim-service) |
| 3 | The result is CARC **18**, "Exact duplicate claim/service" (Medicare pairs it with Group Code **OA**; DME pairs 18 with RARC **N522**). | [X12 Claim Adjustment Reason Codes](https://x12.org/codes/claim-adjustment-reason-codes); [CMS Pub 100-04 Ch. 22, Remittance Advice](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c22.pdf); [Noridian, Reason Code 18 / Remark Code N522](https://med.noridianmedicare.com/web/jadme/topics/ra/denial-resolution/n522-b18) |
| 4 | The edit cannot be waived. "Medicare contractors cannot override or bypass exact duplicate edits in the claims processing system." | [Noridian, Exact Duplicate Claim/Service](https://med.noridianmedicare.com/web/jeb/topics/claim-submission/reason-code-guidance/exact-duplicate-claim-service) |
| 5 | The frequency code is precisely what suppresses this. It "allows Cigna to recognize the electronic submission as a corrected claim, instead of a duplicate claim submission." | [Cigna, Electronic Claims Submission](https://static.cigna.com/assets/chcp/resourceLibrary/medicalResourcesList/medicalDoingBusinessWithCigna/eServices/eSrvcsElecClaimSubmission.html) |
| 6 | Second failure mode — correct intent, wrong coding: "A claim correction submitted without the appropriate frequency code will deny as a duplicate **and the original claim number or DCN will not be adjusted**." So the original claim stays wrong and the correction is lost. | [BCBSOK CPCP025](https://www.bcbsok.com/docs/provider/ok/standards/cpcp/cpcp025-corrected-claim-submissions-01-02-25.pdf) |
| 7 | Third failure mode — auto-rebill loops. Payers explicitly ask billers to stop clearinghouse auto-rebill at 14 days: "only auto-rebill claims after 30 days and ensure they are not resubmitting your claims after 14 days." | [Noridian, Exact Duplicate Claim/Service](https://med.noridianmedicare.com/web/jeb/topics/claim-submission/reason-code-guidance/exact-duplicate-claim-service) |

**Corollary for the resolution system:** a CARC-18 denial is almost never resolved by
resubmitting. Confirm the original claim's disposition first; then either (a) it paid
correctly and no action is needed, (b) it needs correction → `7` with `REF*F8`, or
(c) the duplicate edit is wrong → contact reopenings / appeal.
"If a supplier feels a claim denied duplicate in error, contact Telephone Reopenings."
([Noridian](https://med.noridianmedicare.com/web/jeb/topics/claim-submission/reason-code-guidance/exact-duplicate-claim-service))

---

## 6. Payer-type differences — do not generalise

| Payer type | Does frequency `7`/`8` work? | Correct mechanism | Source |
|---|---|---|---|
| **Medicare Part A / institutional (FFS)** | **Yes.** Provider-initiated adjustments use claim frequency code `7`; TOB `XX7` adjustment, `XX8` cancel, `XXQ` reopening. | Submit adjustment TOB `XX7` with the original ICN/DCN. Reopenings outside the normal window use `Q` in the 4th TOB position. | [CMS Pub 100-04 Ch. 1](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c01.pdf); [CMS transmittal R1775CP](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/downloads/R1775CP.pdf) ("For provider initiated adjustments, MACs should continue with their current method of reporting (claim frequency code '7' for Part A claims)") |
| **Medicare Part B / professional (FFS)** | **No.** The CMS 837P companion guide restricts `CLM05-3`; a value other than `1` is rejected. See Open questions for a version conflict in the retrieved text. | Adjudicated claim → **clerical error reopening** (minor error/omission) or **redetermination**. Rejected/unprocessable claim → resubmit as a new `1` claim. | [CMS 837P TI Companion Guide](https://www.cms.gov/Medicare/Billing/ElectronicBillingEDITrans/downloads/5010a1837bcg.pdf); [NGS, How to Avoid Duplicate Claim Denials](https://www.ngsmedicare.com/web/ngs/how-to-avoid-duplicate-claim-denials) ("When a claim processes, a provider should follow the reopening or appeal process to make corrections to the claim") |
| **Medicare DME MAC** | Treated like Part B: duplicate edits cannot be bypassed; corrections go through reopenings. | Telephone/written reopening; redetermination for non-clerical issues. | [Noridian JA/JD DME, Reason Code 18 / N522](https://med.noridianmedicare.com/web/jadme/topics/ra/denial-resolution/n522-b18); [CGS Supplier Manual Ch. 13, Inquiries, Reopenings & Appeals](https://www.cgsmedicare.com/jc/pubs/pdf/chpt13.pdf) |
| **Medicare Advantage (Part C)** | Plan-specific — many MA plans accept `7`/`8` like commercial. Appeals are **not** the FFS process; they run under 42 CFR Part 422 Subpart M. | Follow the plan's provider manual for corrections; use the plan's reconsideration/dispute process for denials. | [CMS, Medicare Managed Care Appeals & Grievances](https://www.cms.gov/medicare/appeals-grievances/managed-care); [CMS Parts C & D Grievances/Determinations/Appeals Guidance](https://www.cms.gov/medicare/appeals-and-grievances/mmcag/downloads/parts-c-and-d-enrollee-grievances-organization-coverage-determinations-and-appeals-guidance.pdf); [Humana, Submitting corrected claims](https://assets.humana.com/is/content/humana/cphp_prcorrectedclaimspdf) |
| **Medicaid (FFS)** | **Yes**, but state-specific. Adjustment/void requires the state's claim control number (TCN/ICN). | Adjustment = complete new claim with all fields, frequency `7` + TCN. Member ID and Provider ID generally **cannot** be adjusted — void (`8`) and rebill. | [NYS Medicaid General Billing Guidelines (Institutional)](https://www.emedny.org/ProviderManuals/AllProviders/General_Billing_Guidelines_Institutional.pdf); [Texas Medicaid 837I Companion Guide](http://www.tmhp.com/sites/default/files/file-library/edi/837I_ACUTE_CARE_COMPANION_GUIDE_5010.pdf) |
| **Commercial** | **Yes**, and it is the required mechanism. Most large payers accept only `7` and `8`. | `7` + original claim number in `REF*F8`; `8` to void. | [BCBSIL](https://www.bcbsil.com/docs/provider/il/claims/submission/claim-frequency-codes-prof.pdf); [BCBSOK CPCP025](https://www.bcbsok.com/docs/provider/ok/standards/cpcp/cpcp025-corrected-claim-submissions-01-02-25.pdf); [Cigna](https://static.cigna.com/assets/chcp/resourceLibrary/medicalResourcesList/medicalDoingBusinessWithCigna/eServices/eSrvcsElecClaimSubmission.html); [UHC Admin Guide Ch.10](https://www.uhcprovider.com/en/admin-guides/administrative-guides-manuals-2022/ch10-claims-process-2022/claim-corr-resub-ch10-guide.html); [Aetna, Electronic claim filing](https://www.aetna.com/content/dam/aetna/pdfs/aetnacom/healthcare-professionals/documents-forms/COB-claim-CSI.pdf); [Humana](https://assets.humana.com/is/content/humana/cphp_prcorrectedclaimspdf) |

---

## 7. Corrected claim vs reopening vs appeal

### 7a. Medicare FFS — the three-way split

| Claim state | Remedy | Deadline | Source |
|---|---|---|---|
| Rejected / returned as unprocessable (no initial determination made) | Correct and submit as a **new claim**. No appeal rights, no reopening rights. | Subject to the ordinary 1-year timely filing limit | [WPS, How to Correct a Rejected Claim](https://www.wpsgha.com/guides-resources/view/318); [Noridian DME](https://med.noridianmedicare.com/web/jddme/article-detail/-/view/2230703/reminder-unprocessable-return-reject-claims-must-be-resubmitted) |
| Adjudicated, and the defect is a **minor error or omission (clerical error)** | **Reopening** (Part A: adjustment TOB `XX7`; Part B: clerical error reopening request) | Within **1 year** of the initial determination for any reason; **4 years** with good cause | [CMS Pub 100-04 Ch. 34, Reopening and Revision of Claim Determinations](https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/downloads/clm104c34.pdf); [42 CFR 405.980](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-405/subpart-I/subject-group-ECFR70fab268832aef1); [CGS, Reopening vs. Redetermination job aid](https://www.cgsmedicare.com/partb/forms/pdf/reopen_vs_redet_jobaid.pdf) |
| Adjudicated, and the dispute is substantive (coverage, medical necessity, bundling judgement, amount paid) | **Redetermination** (appeal level 1) | 120 days from receipt of the initial determination | [CGS, Reopening vs. Redetermination job aid](https://www.cgsmedicare.com/partb/forms/pdf/reopen_vs_redet_jobaid.pdf); [CMS, First Level of Appeal](https://cms.gov/medicare/appeals-and-grievances/orgmedffsappeals/redeterminationbyamedicarecontractor.html) |

Routing rule CMS imposes on contractors: if a party files an **appeal** but the issue is
actually a minor error or omission, "irrespective of the request for an appeal, contractors
shall treat the request as a request for reopening."
([CMS Pub 100-04 Ch. 34](https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/downloads/clm104c34.pdf))

### 7b. What counts as a clerical error (reopening-eligible)

| Reopening-eligible | Not reopening-eligible | Source |
|---|---|---|
| Mathematical or computational mistakes; transposed procedure or diagnostic codes; inaccurate data entry; misapplication of a fee schedule; computer errors; incorrect data items including a modifier or date of service | Medical necessity determinations; substantive coverage disputes | [CMS Pub 100-04 Ch. 34](https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/downloads/clm104c34.pdf); [CGS, Reopenings for Minor Errors and Omissions](https://www.cgsmedicare.com/jc/claims/reopenings.html) |
| Adding/changing/deleting modifiers such as 24, 25, 54, 57, 58, 59, 76, 78, 79, 80, 95, AQ, AS, GA; increasing units without increasing billed amount | Adding a new or corrected **diagnosis** to a claim/line that was already submitted and **paid** | [NGS, Reopenings for Minor Errors and Omissions](https://www.ngsmedicare.com/web/ngs/reopenings-for-minor-errors-and-omissions); [CGS](https://www.cgsmedicare.com/jc/claims/reopenings.html) |

Caveat to carry: "the contractor has discretion in determining what meets this definition
and therefore, what could be corrected through a reopening."
([CMS Pub 100-04 Ch. 34](https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/downloads/clm104c34.pdf))

### 7c. Commercial — the equivalent split

| Test | Remedy | Source |
|---|---|---|
| The claim as originally submitted was **incomplete or inaccurate** | Corrected claim, frequency `7` | "A corrected claim … should only be submitted if the original claim information was incomplete or inaccurate." [BCBSOK CPCP025](https://www.bcbsok.com/docs/provider/ok/standards/cpcp/cpcp025-corrected-claim-submissions-01-02-25.pdf) |
| The claim was accurate and you dispute the payer's decision | Appeal / reconsideration — **a corrected claim is not an appeal** | [BCBSOK CPCP025](https://www.bcbsok.com/docs/provider/ok/standards/cpcp/cpcp025-corrected-claim-submissions-01-02-25.pdf); [UHC, Pre- and post-service appeals and reconsiderations](https://www.uhcprovider.com/en/claims-payments-billing/appeals.html); [Cigna, Appeals and Disputes](https://www.cigna.com/health-care-providers/coverage-and-claims/appeals-disputes) |

---

## 8. Deadlines that gate a corrected claim

| Payer type | Clock | Source |
|---|---|---|
| Medicare FFS — original claim filing | For services on or after 1 Jan 2010, claim must be filed no later than the close of the period ending **1 calendar year** after the date of service. Extension only for specified exceptions; no extension granted where requested more than 4 years after the DOS. | [42 CFR 424.44](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-424/subpart-C/section-424.44); [CMS, Timely Filing Requirements for Medicare FFS Claims](https://www.cms.gov/Medicare/Medicare-Fee-for-Service-Payment/ProspMedicareFeeSvcPmtGen/downloads/Health_Reform_Timely_Filing_Provider_Notice.pdf) |
| Medicare FFS — adjustment bills | An adjustment bill that corrects or supplements information previously submitted on a **timely** claim is "subject to the rules governing administrative finality, rather than the time limitation for filing." | [CMS Pub 100-04 Ch. 1](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c01.pdf) |
| Medicare FFS — reopening | 1 year from the initial determination for any reason; 4 years with good cause | [42 CFR 405.980](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-405/subpart-I/subject-group-ECFR70fab268832aef1); [CMS Pub 100-04 Ch. 34](https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/downloads/clm104c34.pdf) |
| Medicare FFS — redetermination | 120 days from receipt of the initial determination | [CGS job aid](https://www.cgsmedicare.com/partb/forms/pdf/reopen_vs_redet_jobaid.pdf) |
| Medicare Advantage — reconsideration | Filed with the plan within **65 calendar days** of the notice of the organization determination; standard reconsideration decided no later than 30 calendar days | [CMS, Reconsideration by the MA (Part C) Health Plan](https://www.cms.gov/medicare/appeals-grievances/managed-care/reconsideration-advantage-health-plan-part-c); [CMS Parts C & D Appeals Guidance](https://www.cms.gov/medicare/appeals-and-grievances/mmcag/downloads/parts-c-and-d-enrollee-grievances-organization-coverage-determinations-and-appeals-guidance.pdf) |
| UnitedHealthcare — corrected claims | All claim information "including corrected claims" must arrive within the contractual timely filing window measured from date of service/discharge; and corrected claim information "must be received within 180 calendar days from the original remittance date." | [UHC Admin Guide Ch.10, Claim correction and resubmission](https://www.uhcprovider.com/en/admin-guides/administrative-guides-manuals-2022/ch10-claims-process-2022/claim-corr-resub-ch10-guide.html) |
| Cigna — claim submission | Individual professionals: itemized bill within 180 days of the date of service; facilities: within 180 days of discharge | [Cigna, When to File](https://static.cigna.com/assets/chcp/resourceLibrary/clinicalReimbursementPayment/medicalClinicalReimburseWhenToFile.html) |
| Commercial generally | Contract-specific. UHC states explicitly: refer to the Participation Agreement for timely filing. | [UHC Admin Guide Ch.10](https://www.uhcprovider.com/en/admin-guides/administrative-guides-manuals-2022/ch10-claims-process-2022/claim-corr-resub-ch10-guide.html) |

---

## 9. Pre-submit validation checklist for a frequency 7 or 8 claim

| Check | Fail condition | Source |
|---|---|---|
| Original claim is **finalized** on a remittance | Original still pending → hold; submitting now yields CARC 18 | [Noridian](https://med.noridianmedicare.com/web/jeb/topics/claim-submission/reason-code-guidance/exact-duplicate-claim-service) |
| Original claim actually **adjudicated** (not front-end rejected) | Rejected/unprocessable → must go as frequency `1`, and `7` will have no claim number to reference | [WPS](https://www.wpsgha.com/guides-resources/view/318); [UHC](https://www.uhcprovider.com/en/resource-library/news/2025/avoid-claim-rejections-denials.html) |
| `REF01 = F8` present with the payer claim control number in `REF02` | Missing → compliance error / rejection | [BCBSIL](https://www.bcbsil.com/docs/provider/il/claims/submission/claim-frequency-codes-prof.pdf) |
| Control number taken from 835 `CLP07` for **this** payer | Wrong payer's ICN → no match | [CMS 835 CG](https://www.cms.gov/medicare/billing/electronicbillingeditrans/downloads/5010a1835cg.pdf) |
| Replacement contains **all** correct original lines, not just the changed one | Omitted lines vanish → refund/overpayment exposure | [BCBSOK CPCP025](https://www.bcbsok.com/docs/provider/ok/standards/cpcp/cpcp025-corrected-claim-submissions-01-02-25.pdf) |
| Institutional: `CLM05-2 = A` with the correct facility type in `CLM05-1` | Malformed TOB | [BCBSIL](https://www.bcbsil.com/docs/provider/il/claims/submission/claim-frequency-codes-prof.pdf) |
| Payer is not Medicare Part B / DME FFS | Part B FFS rejects non-`1` frequency; use reopening instead | [CMS 837P CG](https://www.cms.gov/Medicare/Billing/ElectronicBillingEDITrans/downloads/5010a1837bcg.pdf); [NGS](https://www.ngsmedicare.com/web/ngs/how-to-avoid-duplicate-claim-denials) |
| Member ID / billing provider unchanged (Medicaid) | Changed → must void and rebill, not replace | [NYS Medicaid](https://www.emedny.org/ProviderManuals/AllProviders/General_Billing_Guidelines_Institutional.pdf) |
| Not using `5` (late charges) as a correction vehicle | May deny | [BCBSTX CPCP025 update](https://www.bcbstx.com/provider/standards/standards-requirements/disclosures/2024/03-28-24-cpcp025-corrected-clm-submit-late-added-charge-update) |

---

## Open questions

- **CMS 837P companion guide — exact current restriction on `CLM05-3`.** Two retrieved
  excerpts of [the CMS 837P TI Companion Guide](https://www.cms.gov/Medicare/Billing/ElectronicBillingEDITrans/downloads/5010a1837bcg.pdf)
  conflict: one states the only valid value is `1` and anything else is rejected; another
  states valid values are `1` and `7` but that `7` is "processed as original claims and may
  result in duplicate claim rejection, as the claims processing system does not process
  electronic replacements." Both point to the same practical conclusion (do not rely on `7`
  for Medicare Part B FFS), but the literal rejection-vs-duplicate behaviour is unverified.
  The document could not be fetched directly. **Verify against the current companion guide
  and the specific MAC before asserting the failure mode.**
- **Full verbatim NUBC code source 235 list.** The authoritative list lives in the
  AHA-copyrighted [Official UB-04 Data Specifications Manual](https://www.nubc.org/subscription-information),
  which is licensed and was not retrievable. The value/label table in §2 is reproduced from
  [CMS Blue Button CLM_FREQ_CD](https://bluebutton.cms.gov/resources/variables/clm_freq_cd/),
  which is a Medicare-derived rendering. Alphabetic frequency values (`A`–`E`, `G`, `M`, `Q`
  etc., used for NOE/NOA and reopenings) were not enumerated from a primary source and are
  not asserted here beyond `Q`.
- **Whether every payer requires a separate new original claim after a frequency `8` void.**
  The void removes the claim; whether the corrected claim must then be sent as `1` (versus
  the payer accepting a `7` against the voided claim) was not established from a primary
  source for any payer other than the general Medicaid adjustment-vs-void guidance cited.
- **Behaviour when `REF*F8` carries a control number the payer cannot match.** Payers state
  that a missing DCN rejects; none of the retrieved primary sources state the disposition of
  a *present but unmatched* control number, or the specific 277CA status code returned.
- **Whether a frequency `7` can be used against a claim that was fully denied** (as opposed
  to paid) at a given commercial payer. BCBS CPCP025 speaks of "a previously processed
  claim" without distinguishing paid from denied; several payers route denied-claim disputes
  to appeals instead. Payer-by-payer confirmation needed.
- **Medicare Advantage corrected-claim mechanics per plan.** Confirmed only that MA appeals
  run under 42 CFR Part 422 Subpart M and that individual plans (e.g. Humana) publish `7`/`8`
  instructions. There is no CMS-level rule establishing `7`/`8` acceptance across all MA
  plans.
- **Aetna's specific frequency-code and original-claim-number field requirements.** Aetna
  confirms electronic corrected/voided claim submission "including the originally assigned
  claims number"
  ([Aetna, Electronic claim filing](https://www.aetna.com/content/dam/aetna/pdfs/aetnacom/healthcare-professionals/documents-forms/COB-claim-CSI.pdf)),
  but the code values and segment-level requirements were not retrievable from an Aetna
  primary source.
- **State Medicaid variation.** Only New York and Texas companion guides were reached. Other
  states' rules on which fields may be adjusted versus require void-and-rebill are unverified.
