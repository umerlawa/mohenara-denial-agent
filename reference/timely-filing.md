# Timely Filing: Limits, Clock Arithmetic, Proof, and Appeal Rights

> Retrieved 2026-08-12. Every rule below carries a primary-source citation.
>
> **Retrieval note:** direct HTTP fetching of cms.gov, ecfr.gov, x12.org and law.cornell.edu was
> blocked by this environment's network egress policy (proxy returned 403 to CONNECT). Rule text
> below was retrieved via domain-restricted search over those same primary domains, so the cited
> URL is the authoritative source but the wording is a retrieved excerpt, not a verbatim full-text
> read. Anything that could not be pinned to a primary source is in **Open questions**, not asserted.
>
> **Two clocks warning:** the *claim* filing clock runs from the **date of service**. The *appeal*
> clock runs from the **denial / remittance date** and is almost always shorter. Never reuse one
> number for the other.

---

## 1. The denial codes

| Code | Type | Meaning | Source |
|------|------|---------|--------|
| **29** | CARC (Claim Adjustment Reason Code) | "The time limit for filing has expired." National X12 code set; used by every HIPAA-covered payer. | [X12, Claim Adjustment Reason Codes](https://x12.org/codes/claim-adjustment-reason-codes); used as the timely-filing CARC in [NY eMedNY, Guide to Timely Billing](https://www.emedny.org/providermanuals/allproviders/Guide_to_Timely_Billing.pdf) |
| **CO** | Group code paired with 29 | "A contractual agreement between the payer and payee, or a regulatory requirement, resulted in an adjustment." Generally a provider write-off, **not billable to the patient**. | [Novitas, Electronic Billing Guide Ch. 10 — CARC/RARC/Group Codes](https://www.novitas-solutions.com/webcenter/portal/MedicareJH/pagebyid?contentId=00004554) |
| **N211** | RARC (Remittance Advice Remark Code) | "Alert: You may not appeal this decision." Medicare's standard pairing with CARC 29. | [X12, Remittance Advice Remark Codes](https://x12.org/codes/remittance-advice-remark-codes); [Noridian JD DME, Reason Code 29 / Remark Code N211](https://med.noridianmedicare.com/web/jddme/topics/ra/denial-resolution/n211-29) |

**Decoding rule:** the *group code*, not CARC 29, determines patient liability. `CO-29` = provider
liability, write-off, patient cannot be balance-billed. A RARC is explanatory only and never
carries the financial adjustment itself — "remittance remark codes represent non-financial
information critical to understanding the adjudication"
([Novitas, Ch. 10](https://www.novitas-solutions.com/webcenter/portal/MedicareJH/pagebyid?contentId=00004554)).

---

## 2. Initial filing limits by payer type

### 2.1 Medicare fee-for-service (Original Medicare, Parts A and B)

| Rule | Value | Source |
|------|-------|--------|
| Filing limit, services on/after 2010-01-01 | Claim must be filed **no later than the close of the period ending 1 calendar year after the date of service**. | [42 CFR 424.44](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-424/subpart-C/section-424.44) |
| Statutory basis | ACA §6404 reduced the maximum submission period to no more than 12 months / 1 calendar year after the date a service is furnished. | [CMS, Timely Filing Requirements for Medicare FFS Claims](https://www.cms.gov/Medicare/Medicare-Fee-for-Service-Payment/ProspMedicareFeeSvcPmtGen/downloads/Health_Reform_Timely_Filing_Provider_Notice.pdf) |
| Deadline lands on a Federal nonworkday | Time is **extended to the next succeeding workday** (Saturday, Sunday, legal holiday, or statutory/Executive-Order nonworkday). | [42 CFR 424.44](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-424/subpart-C/section-424.44) |
| Corrected / resubmitted claims | Must still meet the **original** filing timeframe — resubmission does not restart the clock. | [FCSO Medicare, Claim timely filing guideline](https://medicare.fcso.com/node/5026) |
| Medicare Secondary Payer (MSP) claims | Same 1 year from date of service. A slow primary payer does **not** extend it. | [Noridian JE Part B, Timely Filing](https://med.noridianmedicare.com/web/jeb/topics/claim-submission/timely-filing); [Noridian JE Part B, MSP Educational Series Q&A](https://med.noridianmedicare.com/web/jeb/topics/msp/educational-series-qa) |

### 2.2 Medicare Advantage (Part C) and other payer types

| Payer type | Filing limit | Source / caveat |
|-----------|--------------|-----------------|
| Medicare Advantage — **contracted** provider | Set by the provider's **contract with the MA organization**, not by 42 CFR 424.44. CMS's MA regulation at 42 CFR 422.520 governs how fast the plan must *pay*, not how fast the provider must *file*. | [42 CFR 422.520](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-422/subpart-K/section-422.520) |
| Medicare Advantage — **non-contracted** provider | See **Open questions** — no primary CMS source establishing a uniform federal filing deadline was located. | — |
| Medicaid **fee-for-service** | Federal floor: "The Medicaid agency **must require providers to submit all claims no later than 12 months from the date of service**." States may and frequently do impose **shorter** limits. | [42 CFR 447.45](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-C/part-447/subpart-A/section-447.45) |
| Commercial / ERISA group health | **No federal filing deadline.** Set by the participation agreement and by state insurance law floors (§5). | See §2.3 and §5 |

> Do not carry the Medicare 1-year rule into a commercial or Medicaid denial. It is a Medicare FFS
> rule grounded in 42 CFR 424.44 and has no application outside Original Medicare.

### 2.3 Named commercial payers (initial claim submission)

| Payer | Initial filing limit | Source |
|-------|---------------------|--------|
| UnitedHealthcare | "No later than 1) **90 days from the date of service**, or 2) the time specified in your Agreement, or 3) the time frame specified in the state guidelines, **whichever is greatest**." Corrected-claim information: within **180 calendar days from the original remittance date**. | [2026 UHC Care Provider Administrative Guide](https://www.uhcprovider.com/content/dam/provider/docs/public/admin-guides/2026-UHC-Administrative-Guide.pdf) |
| Cigna Healthcare | **Participating: 3 months (90 days)** after date of service. **Out-of-network: 6 months (180 days)** after date of service. Consecutive-day services (e.g. hospital confinement) counted from the **last** date of service. | [Cigna, When to File Claims](https://secure.cigna.com/health-care-providers/coverage-and-claims/submit-claims/when-to-file-claims); [CHCP Resources, When to File](https://static.cigna.com/assets/chcp/resourceLibrary/clinicalReimbursementPayment/medicalClinicalReimburseWhenToFile.html) |
| Cigna — COB / secondary | Timely filing determined from the **processing date on the primary carrier's EOB/EOP**, not the date of service. | [Cigna, When to File Claims](https://secure.cigna.com/health-care-providers/coverage-and-claims/submit-claims/when-to-file-claims) |
| BCBS of Texas — HMO | **180 days** from date of service. | [BCBSTX HMO Provider Manual, Sec. F(a) Filing Claims](https://www.bcbstx.com/docs/provider/tx/standards/manuals/hmo-provider-manual/hmo-sec-f-a-general-info.pdf) |
| BCBS of Texas — PPO | **365 days** from date of service. | [BCBSTX PPO Provider Manual, Sec. F(a) Filing Claims](https://www.bcbstx.com/docs/provider/tx/standards/manuals/ppo-provider-manual/ppo-sec-f-a-general-info.pdf) |
| Humana — commercial | **180 days** from date of service for physicians; **90 days** for other providers. COB claims beyond the 365-day limit require a primary remittance **no more than 180 days past the primary payer's EOB date** attached. | [Humana Provider Manual (non-delegated)](https://assets.humana.com/is/content/humana/FINAL589003ALL1024_2025_ProviderManualNonDelegatedpdf); [Humana 2026 Provider Manual](https://assets.humana.com/is/content/humana/FINAL_773902ALL0725-B_2026_ProviderManual-NonDelegated_formattedpdf) |
| Aetna | See **Open questions** — Aetna's 180-day figure is a **dispute/appeal** standard, not a verified initial-submission limit. | [Aetna, Disputes and appeals overview](https://www.aetna.com/health-care-professionals/disputes-appeals/disputes-appeals-overview.html) |

**The BCBSTX row is the general lesson: filing limits vary by product line inside the same payer.**
Resolve against the specific product on the claim, not the payer brand.

---

## 3. How the clock is computed

### 3.1 Which date starts the clock

| Claim type | Start date | Source |
|-----------|-----------|--------|
| Medicare professional (837P / CMS-1500) with span dates | The **line item "From" date**. | [CMS, Medicare Claims Processing Manual Ch. 1](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c01.pdf); [CMS Transmittal R2140CP](https://www.cms.gov/regulations-and-guidance/guidance/transmittals/downloads/r2140cp.pdf) |
| Medicare institutional (837I / CMS-1450) with span dates | The **"Through" date** on the claim. | [CMS Transmittal R2140CP](https://www.cms.gov/regulations-and-guidance/guidance/transmittals/downloads/r2140cp.pdf); [CMS MLN, Timely Filing — CMS-1450 & 837I](https://www.cms.gov/OUTREACH-AND-EDUCATION/MLN/WBT/MLN7388180-MLN-WBT-1450/1450/lesson01/08/index.html) |
| Medicare line item split | If a line item "From" date is not timely but the "To" date is timely, **contractors must split the line item** and deny only the untimely portion. A partial timely-filing denial on a multi-line claim is expected behavior, not an error. | [CMS Transmittal R2140CP](https://www.cms.gov/regulations-and-guidance/guidance/transmittals/downloads/r2140cp.pdf) |
| Cigna, consecutive-day services | Counted from the **last** date of service. | [Cigna, When to File Claims](https://secure.cigna.com/health-care-providers/coverage-and-claims/submit-claims/when-to-file-claims) |
| Ohio Medicaid inpatient hospital | **365 days from the date of discharge** (not admission). | [Ohio Admin. Code 5160-1-19](https://codes.ohio.gov/ohio-administrative-code/rule-5160-1-19) |
| Secondary / COB claims (commercial) | Frequently runs from the **primary payer's EOB/processing date**, not the date of service. Verify per payer. | [Cigna](https://secure.cigna.com/health-care-providers/coverage-and-claims/submit-claims/when-to-file-claims); [Humana Provider Manual](https://assets.humana.com/is/content/humana/FINAL589003ALL1024_2025_ProviderManualNonDelegatedpdf) |

### 3.2 Which date stops the clock (the "receipt date")

| Submission mode | Date that counts | Source |
|-----------------|------------------|--------|
| Medicare — general principle | "A submission is considered to be a filed claim for purposes of determining timely filing **on the date that the submission is received by the appropriate Medicare claims processing contractor**." Not the date you transmitted, not the postmark. | [CMS Transmittal R2140CP](https://www.cms.gov/regulations-and-guidance/guidance/transmittals/downloads/r2140cp.pdf) |
| Medicare — paper | Date of receipt **in the mailroom**. A paper claim received by 5:00 p.m. on a business day (or by closing time if the contractor closes between 4:00 and 5:00 p.m.) counts as received that date, even if the envelope is not opened or keyed until later. | [CMS, Medicare Claims Processing Manual Ch. 1](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c01.pdf); [CMS Transmittal R273CP](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/downloads/r273cp.pdf) |
| Medicare — electronic | The date the claim **passes all front-end edits**. | [CMS Transmittal R273CP](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/downloads/r273cp.pdf) |
| Commercial (BCBSTX example) | The clearinghouse/payer acceptance report is the evidence of receipt "within our claims processing system"; the report is forwarded within 48 hours of transmission. | [BCBSTX PPO Provider Manual, Electronic Filing](https://ccpa.bcbstx.com/docs/provider/tx/standards/manuals/ppo-provider-manual/ppo-sec-f-e-electronic-filing.pdf) |

### 3.3 What does NOT stop the clock

| Event | Effect | Source |
|-------|--------|--------|
| Medicare claim returned as **unprocessable / RTP** | The submission "is **not considered a claim** under Medicare regulation." No permanent record is kept. Its receipt date does **not** establish timely filing. The clock keeps running while the claim sits in the RTP queue. | [CMS Transmittal R2140CP](https://www.cms.gov/regulations-and-guidance/guidance/transmittals/downloads/r2140cp.pdf); [Noridian JE Part B, Timely Filing](https://med.noridianmedicare.com/web/jeb/topics/claim-submission/timely-filing) |
| Medicare: claim with incomplete or invalid information | "For a claim to be considered timely, the claim must be filed **without any incomplete or invalid information**. Thus, any unprocessable claims submitted prior to the timely filing denial do not count towards the one-year time limit." | [Noridian JE Part B, Timely Filing](https://med.noridianmedicare.com/web/jeb/topics/claim-submission/timely-filing) |
| Commercial: EDI **rejection** (front-end, pre-adjudication) | A rejection is not an accepted claim. It "must be resolved and resubmitted with requested information before the payer ultimately accepts the claim for adjudication." | [BCBSTX PPO Provider Manual, Electronic Filing](https://ccpa.bcbstx.com/docs/provider/tx/standards/manuals/ppo-provider-manual/ppo-sec-f-e-electronic-filing.pdf) |
| Resubmitting a corrected claim (Medicare) | Does not restart the original clock. | [FCSO Medicare](https://medicare.fcso.com/node/5026) |

**Operational consequence:** the single most common cause of a legitimate CO-29 is a claim that was
transmitted early but **rejected at the front end** and never re-worked. Check the 277CA / clearinghouse
acknowledgment history before assuming the claim was "filed."

---

## 4. Medicare FFS exceptions to the 1-year limit

42 CFR 424.44(b) permits four exceptions, detailed in Medicare Claims Processing Manual Ch. 1
§§70.7.1–70.7.4 ([CMS Transmittal R2140CP](https://www.cms.gov/regulations-and-guidance/guidance/transmittals/downloads/r2140cp.pdf)).

| # | Exception | Trigger | Extension granted | Source |
|---|-----------|---------|-------------------|--------|
| 1 | **Administrative error** | Failure to file timely was caused by error or misrepresentation of an employee, Medicare contractor (MAC/intermediary/carrier), or agent of HHS performing Medicare functions within the scope of its authority. | Through the **last day of the 6th calendar month following the month** in which the beneficiary or provider was notified the error was corrected. | [42 CFR 424.44](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-424/subpart-C/section-424.44); [CMS Transmittal R2140CP](https://www.cms.gov/regulations-and-guidance/guidance/transmittals/downloads/r2140cp.pdf) |
| 2 | **Retroactive Medicare entitlement** | Beneficiary was not entitled at time of service; after the filing period expired, receives notification of entitlement effective retroactive to or before the date of service. | Per §70.7.2 (6-month formula). | [CMS Transmittal R2140CP](https://www.cms.gov/regulations-and-guidance/guidance/transmittals/downloads/r2140cp.pdf) |
| 3 | **Retroactive entitlement + State Medicaid agency recoupment** | State Medicaid agency recoups its payment from the provider **6 months or more** after the date the service was furnished to a dually eligible beneficiary. | From the **end of the 6th calendar month from the month in which the State Medicaid agency recovered its money**. | [CMS Transmittal R2140CP](https://www.cms.gov/regulations-and-guidance/guidance/transmittals/downloads/r2140cp.pdf); [Palmetto GBA JM Part B, Claim Timeliness Requirements and Criteria for a Timeliness Extension](https://dominoapps.palmettogba.com/palmetto/jmb.nsf/DID/AWNPNM6234) |
| 4 | **Retroactive MA / PACE disenrollment** | Beneficiary was enrolled in an MA plan or PACE organization, later disenrolled retroactive to or before the date of service, and the MA plan/PACE org **recoups its payment 6 months or more** after the date of service. | Per §70.7.4 (6-month formula). | [CMS Transmittal R2140CP](https://www.cms.gov/regulations-and-guidance/guidance/transmittals/downloads/r2140cp.pdf) |

| Procedural rule | Detail | Source |
|-----------------|--------|--------|
| Outer bound on administrative-error extensions | "Contractors will not accept requests for extensions for such errors that extend **beyond 4 years from the date of service**." | [CMS Transmittal R2140CP](https://www.cms.gov/regulations-and-guidance/guidance/transmittals/downloads/r2140cp.pdf) |
| How to request | A **written waiver/extension request** with supporting evidence, sent to the MAC — not an appeal form. NGS: submit the CMS-1500, a letter explaining why the claim is beyond one year, and documentation supporting the extension, addressed to the Claims Department Manager. | [NGS, Requesting an Exception to Timely Filing](https://www.ngsmedicare.com/web/ngs/timely-filing?selectedArticleId=592187); [Noridian JE Part B, Timely Filing](https://med.noridianmedicare.com/web/jeb/topics/claim-submission/timely-filing) |
| Evidence accepted for administrative error | Written agency report (Medicare, SSA, FI, carrier, MAC) based on agency records describing how its error caused the late filing; a copy of an agency letter reflecting the error; a written statement of an agency employee with personal knowledge; or the MAC's Claims Processing Issues Log (CPIL) showing the system error. Requires a **clear and direct relationship** between the error and the late filing, and the claim must be submitted within 6 months after the month the provider was notified the error was corrected. | [Palmetto GBA, Checklist for Timely Filing Extension](https://www.palmettogba.com/palmetto/jma.nsf/DIDC/AWNPNM6234~Claims) |
| Evidence accepted for MA/PACE recoupment | Dated screen prints of CWF showing MA plan or PACE eligibility at the time of original submission, or proof of MA plan / PACE recoupment. Both the claim and the written request must be received within **6 months of the recoupment date or date of accretion**. | [Palmetto GBA, Checklist for Timely Filing Extension](https://www.palmettogba.com/palmetto/jma.nsf/DIDC/AWNPNM6234~Claims) |
| Evidence for State Medicaid recoupment | Official letters from the State Medicaid office, Social Security Office, or other official entity. | [Noridian JE Part B, Timely Filing](https://med.noridianmedicare.com/web/jeb/topics/claim-submission/timely-filing) |

---

## 5. State-law floors on commercial filing limits

State insurance law can override a contract's filing limit. Where the state sets a floor, the
contract cannot be shorter.

| State | Rule | Source |
|-------|------|--------|
| **California** (DMHC-regulated plans) | A plan may **not** impose a claim receipt deadline shorter than **90 days for contracted** providers and **180 days for non-contracted** providers after the date of service. For supplemental/COB claims where the plan is not primary, the deadline may not be less than **90 days from the date of payment, contest, denial, or notice from the primary payer**. | [CA DMHC, Claims Technical Assistance Guide (rev. 2020-01-31)](https://www.dmhc.ca.gov/Portals/0/Docs/OFR/Claims%20TAG%20Revised%201_31_2020.pdf) |
| **New York** | Providers have **120 days** after the date of service to submit claims for the claim to be valid and enforceable against an HMO or insurer, **unless the parties agree to a period more favorable to the provider**. | [NY Insurance Law §3224-a](https://www.nysenate.gov/legislation/laws/ISC/3224-A); [NY DFS OGC Opinion 09-07-05, Time Limit on Claim Submission](https://www.dfs.ny.gov/insurance/ogco2009/rg090705.htm) |
| **New York** — untimely-filing relief | A participating provider may request **reconsideration of a claim denied solely because it was untimely**. If the provider shows the non-compliance resulted from an **unusual occurrence** and that it has a **pattern or practice of timely submitting claims**, the HMO or insurer **must pay the claim**, but may reduce reimbursement by **up to 25%** of what it would have paid. | [NY Insurance Law §3224-a](https://www.nysenate.gov/legislation/laws/ISC/3224-A) |
| **Texas** | The **95-day** claim filing deadline of Tex. Ins. Code §843.337 (HMO) and §1301.102 (PPO) applies to **all physicians and providers submitting claims to a managed care carrier, regardless of contracting status** — but only to providers **licensed in Texas**; out-of-state providers are not subject to it. | [Tex. Ins. Code Ch. 843](https://statutes.capitol.texas.gov/Docs/IN/htm/IN.843.htm); [Tex. Ins. Code Ch. 1301](https://statutes.capitol.texas.gov/GetStatute.aspx?Code=IN&Value=1301); [TDI, Prompt Pay FAQ](https://www.tdi.texas.gov/hprovider/ppsb418faq.html) |

> **New York's §3224-a "unusual occurrence + pattern of timely filing" test is the strongest
> statutory appeal ground for a timely-filing denial found in this research.** It is a mandatory
> payment obligation on the payer, not a discretionary courtesy. It applies only to participating
> providers under NY-regulated policies.

---

## 6. Medicaid — federal floor and state variation

Federal rule: the state Medicaid agency **must require** submission no later than **12 months from
the date of service** ([42 CFR 447.45](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-C/part-447/subpart-A/section-447.45)).
That is a ceiling on state leniency, not a guarantee to the provider — several states are far shorter.

| State | Medicaid FFS initial filing limit | Source |
|-------|-----------------------------------|--------|
| **California (Medi-Cal)** | Received by the Fiscal Intermediary within **6 months following the month** in which services were rendered. Late claims are subject to a **reduction schedule (100% / 75% / 50%)** rather than a flat denial, and require a DHCS-issued **delay reason code**. | [Medi-Cal Provider Manual, Claim Submission and Timeliness Overview](https://mcweb.apps.prd.cammis.medi-cal.ca.gov/file/manual?fn=Claim_Submission_Overview.pdf) |
| **New York** | **90 days** from the date of service for initial submission. Claims submitted after 90 days require a **delay reason code** and must be submitted **within 30 days of the time submission came within the provider's control**. Claims with dates of service more than **2 years** prior to receipt are denied with **CARC 29**. | [eMedNY, Guide to Timely Billing](https://www.emedny.org/providermanuals/allproviders/Guide_to_Timely_Billing.pdf); [eMedNY, Information for All Providers — General Billing](https://www.emedny.org/providermanuals/allproviders/pdfs/information_for_all_providers-general_billing.pdf); [eMedNY FOD-7001, Submitting Claims over 90 Days](https://www.emedny.org/HIPAA/QuickRefDocs/FOD-7001_Sub_Claims_Over_90_days_Old.pdf) |
| **Texas** | Received by TMHP within **95 days of each date of service**. Where eligibility determination was delayed, the claim must still be submitted within **365 days** of the date of service. | [Texas Medicaid Provider Procedures Manual, §1.06 Claims Filing](https://www.tmhp.com/sites/default/files/microsites/provider-manuals/tmppm/html/TMPPM/1_06_Claims_Filing/1_06_Claims_Filing.htm) |
| **Ohio** | Original claims must be received by ODM within **365 days** of the date the service was provided; **inpatient hospital: 365 days from date of discharge**. | [Ohio Admin. Code 5160-1-19](https://codes.ohio.gov/ohio-administrative-code/rule-5160-1-19); [ODM, Timely Filing Extension guidance (Nov. 2024)](https://dam.assets.ohio.gov/image/upload/medicaid.ohio.gov/Links/Timely_Filing_Extension-_Providers_Nov_24.pdf) |
| **Florida** | **12-month** claim submission time limit, with exceptions where the claim meets specified conditions. | [Florida Medicaid Provider General Handbook](https://ahca.myflorida.com/medicaid/review/general/59g_5020_provider_general_requirements.pdf) |

**Medicaid-specific mechanism to check before writing off:** several states use **delay reason codes**
submitted on the claim rather than an appeal. New York and California both operate this way
([eMedNY FOD-7001](https://www.emedny.org/HIPAA/QuickRefDocs/FOD-7001_Sub_Claims_Over_90_days_Old.pdf);
[Medi-Cal](https://mcweb.apps.prd.cammis.medi-cal.ca.gov/file/manual?fn=Claim_Submission_Overview.pdf)).
NY delay reason examples: code 4 (delay in certifying provider), code 7 (third-party processing
delay — applies only where Medicare or another third-party payer caused the delay), code 8 (delay in
eligibility determination), code 9 (original claim rejected or denied for a reason unrelated to the
timely billing rules)
([eMedNY, Edits 02160/02163](https://www.emedny.org/listserv/eMedNYGeneralUpdates/Edits_02160_and_02163_delay_reasons4and8___01-17-13.pdf);
[eMedNY, Delay Reason Code 7](https://www.emedny.org/listserv/eMedNYGeneralUpdates/Paper_Claims_02162_Delay_Code7_Processing_Delay_06-13-13.pdf)).
Medicaid MCO limits are set by the MCO contract and are not covered by these FFS citations.

---

## 7. The appeal clock — separate from, and shorter than, the filing clock

| Payer type | Deadline to appeal a denial | Runs from | Source |
|-----------|------------------------------|-----------|--------|
| Medicare FFS — redetermination (Level 1) | **120 calendar days** | Date of **receipt** of the initial claim determination (RA/MSN); receipt presumed 5 calendar days after the notice date absent evidence to the contrary | [CMS, First Level of Appeal](https://www.cms.gov/medicare/appeals-grievances/fee-for-service/first-level-appeal-redetermination-medicare-contractor); [42 CFR 405.942](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-405/subpart-I/subject-group-ECFR3ec6343ada14c59/section-405.942) |
| ERISA group health plan (self-funded and most fully insured group coverage) | Plans must give claimants **at least 180 days** following receipt of an adverse benefit determination to appeal | Receipt of the adverse benefit determination notice | [29 CFR 2560.503-1](https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XXV/subchapter-G/part-2560/section-2560.503-1); [DOL EBSA, Benefit Claims Procedure Regulation](https://www.dol.gov/agencies/ebsa/about-ebsa/our-activities/resource-center/publications/group-health-and-disability-plans-benefit-claims-procedure-regulation) |
| UnitedHealthcare | **12 months** to complete **both** steps — Step 1 claim reconsideration, Step 2 appeal — "or as required by law or your Agreement" | Date of the **EOB or PRA** | [UHC Administrative Guide, Claim reconsideration and appeals process](https://www.uhcprovider.com/en/admin-guides/administrative-guides-manuals-2022/ch10-claims-process-2022/claim-rec-pro-res-dis-ch10-guide.html); [UHC, Pre- and post-service appeals and reconsiderations](https://www.uhcprovider.com/en/claims-payments-billing/appeals.html) |
| Aetna | Reconsideration within **180 calendar days** of the initial claim decision; then appeal within **60 calendar days** of the reconsideration decision. For PPO-based claims, dispute within **180 calendar days from the date of Aetna's last action**. | Initial claim decision / last action | [Aetna, Disputes and appeals overview](https://www.aetna.com/health-care-professionals/disputes-appeals/disputes-appeals-overview.html); [Aetna, Provider Appeals](https://www.aetna.com/health-care-professionals/disputes-appeals/provider-appeals.html) |
| BCBS of Texas | Two levels of claim review; BCBSTX completes the first review within 45 days of receipt and the second within 45 days of receipt of the second request. **Deadline to request is stated in the manual's claim review section — verify per product.** | — | [BCBSTX PPO Provider Manual, Claim Review Process](https://www.bcbstx.com/docs/provider/tx/standards/manuals/ppo-provider-manual/ppo-sec-f-h-claim-review-process.pdf) |
| Medicaid | Varies by state; not federally standardized for provider claim disputes. Verify in the state manual. | — | — |

**Arithmetic trap:** for Medicare, the redetermination window runs from *receipt*, and receipt is
presumed 5 calendar days after the notice date. Compute `notice_date + 5 + 120`, not `notice_date + 120`
([CMS, First Level of Appeal](https://www.cms.gov/medicare/appeals-grievances/fee-for-service/first-level-appeal-redetermination-medicare-contractor)).

---

## 8. What counts as proof of timely filing

| Evidence | Accepted? | Source |
|----------|-----------|--------|
| Clearinghouse / EDI **acceptance** report showing the payer's actual response to the electronic claim | **Yes** — the strongest evidence. Anthem: "Proof must be from a clearinghouse and must show the actual Anthem response to the submission of the electronic claim." UHC: "include confirmation that it was received and accepted within your filing limit, and an EDI report." | [Anthem, Timely filing: Acceptable forms of proof](https://files.providernews.anthem.com/3136/CABC-CM-039312-23-Timely-Filing-Acceptable-forms-of-proof-Flyer_FINAL.pdf); [Anthem CA Medicaid Reimbursement Policy, Proof of Timely Filing](https://providers.anthem.com/docs/gpp/california-provider/CA_CAID_RP_proof_timely_filing.pdf); [UHC, EDI Quick Tips for Claims](https://www.uhcprovider.com/en/resource-library/edi/edi-quick-tips-claims.html) |
| Payer acknowledgment report forwarded post-transmission | **Yes** — BCBSTX: forwarded within 48 hours after transmission is received and "can be used as proof of claim receipt within our claims processing system." | [BCBSTX PPO Provider Manual, Electronic Filing](https://ccpa.bcbstx.com/docs/provider/tx/standards/manuals/ppo-provider-manual/ppo-sec-f-e-electronic-filing.pdf) |
| Primary carrier's EOB showing the claim was filed with the primary within its deadline (COB claims) | **Yes** (BCBSTX) | [BCBSTX PPO Provider Manual, Claim Review Process](https://www.bcbstx.com/docs/provider/tx/standards/manuals/ppo-provider-manual/ppo-sec-f-h-claim-review-process.pdf) |
| Documentation that the claim was filed with the **wrong division** of the same Blue plan | **Yes** (BCBSTX) | [BCBSTX PPO Provider Manual, Claim Review Process](https://www.bcbstx.com/docs/provider/tx/standards/manuals/ppo-provider-manual/ppo-sec-f-h-claim-review-process.pdf) |
| Payer correspondence requesting additional information, or payer documentation that the claim was incomplete | **Yes** (BCBSTX) | [BCBSTX PPO Provider Manual, Claim Review Process](https://www.bcbstx.com/docs/provider/tx/standards/manuals/ppo-provider-manual/ppo-sec-f-h-claim-review-process.pdf) |
| An EDI **rejection** report | **No** — a rejected claim was never accepted for adjudication. | [BCBSTX PPO Provider Manual, Electronic Filing](https://ccpa.bcbstx.com/docs/provider/tx/standards/manuals/ppo-provider-manual/ppo-sec-f-e-electronic-filing.pdf) |
| Medicare exception requests: agency error report / agency letter / statement of an agency employee with personal knowledge / MAC Claims Processing Issues Log entry; CWF screen prints; proof of MA-plan or PACE recoupment | **Yes**, for the four §70.7 exceptions specifically | [Palmetto GBA, Checklist for Timely Filing Extension](https://www.palmettogba.com/palmetto/jma.nsf/DIDC/AWNPNM6234~Claims) |
| A screenshot of the practice management system showing a "submitted" date | See **Open questions** — no primary source found either accepting or rejecting this. | — |

---

## 9. Is a timely-filing denial appealable?

### 9.1 Medicare fee-for-service — **No, not through the appeals process**

| Rule | Detail | Source |
|------|--------|--------|
| Statutory/regulatory basis | 42 CFR 405.926 lists actions that are **not initial determinations**; determinations that a provider or supplier **failed to submit a claim timely**, or failed to submit a timely claim despite being requested to do so by the beneficiary or the beneficiary's subrogee, are on that list. | [42 CFR 405.926](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-405/subpart-I/subject-group-ECFRba80b2c5e3f1227/section-405.926) |
| Consequence | "When a claim is denied for having been filed after the timely filing period, such denial does not constitute an 'initial determination,' and the determination that a claim was not filed timely is **not subject to appeal**." | [CMS Transmittal R2140CP](https://www.cms.gov/regulations-and-guidance/guidance/transmittals/downloads/r2140cp.pdf); [NGS, Requesting an Exception to Timely Filing](https://www.ngsmedicare.com/web/ngs/timely-filing?selectedArticleId=592187) |
| RARC signalling this | **N211** — "Alert: You may not appeal this decision." | [Noridian JD DME, Reason Code 29 / Remark Code N211](https://med.noridianmedicare.com/web/jddme/topics/ra/denial-resolution/n211-29) |
| The correct route instead | A **written timely-filing waiver / extension request** to the MAC under one of the four 42 CFR 424.44(b) exceptions (§4 above) — not a redetermination request. | [Noridian JE Part B, Timely Filing](https://med.noridianmedicare.com/web/jeb/topics/claim-submission/timely-filing); [NGS](https://www.ngsmedicare.com/web/ngs/timely-filing?selectedArticleId=592187) |
| Narrow redetermination carve-out (DME) | Noridian JD DME states the denial "cannot be appealed **unless** there was an act of nature, such as a flood, fire, or there are other circumstances outside of the supplier's control, then a Redetermination request may be submitted with all relevant supporting documentation." | [Noridian JD DME, Reason Code 29 / Remark Code N211](https://med.noridianmedicare.com/web/jddme/topics/ra/denial-resolution/n211-29) |
| Warning about false N211 | CMS has documented at least one instance where N211 was applied **in error** to claims whose underlying exception request decisions **were** appealable. Do not treat the presence of N211 alone as conclusive. | [CMS Transmittal R3118CP](https://www.cms.gov/regulations-and-guidance/guidance/transmittals/downloads/r3118cp.pdf) |

**Important distinction for the resolution system:** the un-appealable determination is *"the claim was
filed late."* If the provider's position is that the claim was **not** late — that the payer's receipt
date is wrong, or that an earlier accepted submission exists — that is a factual dispute about the
receipt date, and the operative remedy is to present proof of receipt (§8) rather than to concede
lateness and argue for forgiveness.

### 9.2 Commercial and Medicaid — **Yes, generally appealable**

There is no analogue to 42 CFR 405.926 outside Original Medicare. Timely-filing denials are handled
through the payer's ordinary reconsideration/appeal channel or a state-law relief mechanism:

| Ground | Payer type | Source |
|--------|-----------|--------|
| Statutory relief: unusual occurrence + pattern of timely filing → payer **must pay**, may reduce by up to 25% | NY-regulated HMOs and insurers, participating providers | [NY Insurance Law §3224-a](https://www.nysenate.gov/legislation/laws/ISC/3224-A) |
| State filing floor overrides a shorter contractual limit (90/180 days CA; 95 days TX for TX-licensed providers regardless of contracting status; 120 days NY unless more favorable to provider) | Commercial, state-regulated | [CA DMHC Claims TAG](https://www.dmhc.ca.gov/Portals/0/Docs/OFR/Claims%20TAG%20Revised%201_31_2020.pdf); [TDI Prompt Pay FAQ](https://www.tdi.texas.gov/hprovider/ppsb418faq.html); [NY Ins. Law §3224-a](https://www.nysenate.gov/legislation/laws/ISC/3224-A) |
| Contract or state guideline is longer than the payer's default | UHC — limit is "whichever is **greatest**" of 90 days, the Agreement, or state guidelines | [2026 UHC Administrative Guide](https://www.uhcprovider.com/content/dam/provider/docs/public/admin-guides/2026-UHC-Administrative-Guide.pdf) |
| Claim was filed with the wrong division / payer requested more information / claim was incomplete per the payer | BCBSTX (illustrative of the general category) | [BCBSTX PPO Provider Manual, Claim Review Process](https://www.bcbstx.com/docs/provider/tx/standards/manuals/ppo-provider-manual/ppo-sec-f-h-claim-review-process.pdf) |
| COB: clock ran from the primary EOB date, not date of service | Cigna, Humana, CA DMHC-regulated plans | [Cigna](https://secure.cigna.com/health-care-providers/coverage-and-claims/submit-claims/when-to-file-claims); [Humana](https://assets.humana.com/is/content/humana/FINAL589003ALL1024_2025_ProviderManualNonDelegatedpdf); [CA DMHC Claims TAG](https://www.dmhc.ca.gov/Portals/0/Docs/OFR/Claims%20TAG%20Revised%201_31_2020.pdf) |
| Medicaid: submit with an approved **delay reason code** rather than appeal | NY, CA (mechanism varies by state) | [eMedNY FOD-7001](https://www.emedny.org/HIPAA/QuickRefDocs/FOD-7001_Sub_Claims_Over_90_days_Old.pdf); [Medi-Cal Claim Submission Overview](https://mcweb.apps.prd.cammis.medi-cal.ca.gov/file/manual?fn=Claim_Submission_Overview.pdf) |

---

## 10. Patient liability on a timely-filing denial

| Payer type | Can the patient be billed? | Source |
|-----------|---------------------------|--------|
| Medicare FFS | **No.** Where the beneficiary's request for payment was filed timely (or would have been had the provider acted) but the provider is responsible for not filing timely, the provider **may not charge the beneficiary** except for deductible and/or coinsurance amounts that would have applied had Medicare paid. | [CMS Transmittal R2140CP](https://www.cms.gov/regulations-and-guidance/guidance/transmittals/downloads/r2140cp.pdf); [CMS Transmittal R830CP](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/Downloads/R830CP.pdf) |
| Commercial — Cigna | **No.** "Cigna Healthcare prohibits balance billing your patient if claims are denied because they were not submitted within the time frame outlined above." | [Cigna, When to File Claims](https://secure.cigna.com/health-care-providers/coverage-and-claims/submit-claims/when-to-file-claims) |
| Commercial — general | Determined by the **group code**. `CO` = contractual obligation, provider write-off, "not billed to the patient." A `PR` group code on code 29 would signal the opposite and should be treated as an anomaly worth verifying against the contract. | [Novitas, Electronic Billing Guide Ch. 10](https://www.novitas-solutions.com/webcenter/portal/MedicareJH/pagebyid?contentId=00004554) |
| Medicaid | See **Open questions**. | — |

---

## Open questions

- **Medicare Advantage non-contracted provider filing deadline.** No primary CMS source was located
  establishing a uniform federal timely-filing deadline for non-contracted providers billing MA plans.
  42 CFR 422.520 governs *prompt payment by the plan* (95% of clean claims within 30 days for
  non-contracted/PFFS claims; all other claims within 60 days), not provider filing.
  42 CFR 424.44 by its terms governs Medicare FFS claims. Treat MA filing limits as
  plan-document-driven and verify per plan.
- **Aetna's initial claim submission limit.** Aetna's widely cited 180-day figure was confirmed only as
  a **dispute/appeal** standard, not as an initial filing limit. The initial-submission number could not
  be pinned to Aetna's Office Manual through the available retrieval method.
- **Outer cap on Medicare timely-filing extensions.** Secondary sources state the limit "cannot be
  extended beyond December 31 of the third calendar year after the year in which the services were
  furnished." This could not be located in the current text of 42 CFR 424.44 and may be residual
  pre-2010 language. What *was* confirmed in the CMS transmittal is a different figure: contractors
  will not accept **administrative-error** extension requests extending **beyond 4 years from the date
  of service** ([R2140CP](https://www.cms.gov/regulations-and-guidance/guidance/transmittals/downloads/r2140cp.pdf)).
  Do not assert the December-31 rule.
- **Exact subsection lettering of 42 CFR 424.44.** CMS manual text refers the exceptions to
  "42 C.F.R. §424.44(b)"; the search-derived excerpts of the regulation itself did not confirm
  subsection lettering for the basic limit, the nonworkday extension, or the exceptions. Cite the
  section, not a subsection, unless the full text is verified.
- **X12 code-set metadata for CARC 29.** The official start date, last-modified date, and any notes
  attached to CARC 29 could not be read — the X12 code lists are behind an access-restricted page and
  x12.org was egress-blocked. The description text is confirmed by multiple primary payer/state
  sources; the metadata is not.
- **Whether a practice-management-system screenshot constitutes acceptable proof of timely filing.**
  No primary payer source was found either accepting or rejecting it. Every confirmed acceptable form
  of proof originates from the **payer or clearinghouse** side of the transaction, which is suggestive
  but not dispositive.
- **Patient liability on Medicaid timely-filing denials.** Federal Medicaid provider-agreement rules
  generally bar billing beneficiaries for covered services, but no primary source addressing the
  timely-filing scenario specifically was located.
- **Medicaid managed care organization filing limits.** The 42 CFR 447.45 12-month floor and the state
  FFS limits in §6 are FFS rules. MCO limits are contractual and were not researched.
- **Whether "1 calendar year" under 42 CFR 424.44 means the same calendar date one year later**
  (e.g. DOS 2025-03-15 → 2026-03-15) or the day before. The regulation's phrasing is "the close of the
  period ending 1 calendar year after the date of service"; the precise boundary day was not confirmed
  from primary text. Where a claim sits on that boundary, treat it as contestable and obtain the MAC's
  stated deadline.
