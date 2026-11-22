# NCCI: PTP Edits, Modifier Indicators, Bypass Modifiers, and MUE/MAI

> Retrieved 2026-08-12. Every rule below carries a primary-source citation.
>
> **Retrieval note:** direct HTTP fetching of `cms.gov` and `oig.hhs.gov` was blocked by this
> environment's network egress policy (proxy returned 403 to CONNECT; WebFetch returned
> `EGRESS_BLOCKED` for every host tried). Rule text below was retrieved via domain-restricted
> search over those same primary domains, so the cited URL is the authoritative source but the
> wording is a retrieved excerpt, **not a verbatim full-text read**. Where an excerpt was
> truncated or a roster could not be enumerated in full, the item is in **Open questions**
> rather than asserted. Before quoting a passage back to a payer in an appeal letter, open the
> cited PDF and confirm the wording.
>
> **Two different edit families warning:** PTP and MUE are separate programs with separate files,
> separate indicators, and **separate resolution paths**. A PTP problem is "these two codes were
> billed together"; an MUE problem is "too many units of one code." Never apply a CCMI rule to a
> units problem or an MAI rule to a code-pair problem.

---

## 1. Scope: which payers actually run these edits

| Payer type | Does NCCI apply? | Source |
|---|---|---|
| **Medicare FFS (Part B practitioner, outpatient hospital, DME)** | Yes. NCCI PTP and MUE are Medicare programs run by CMS; MACs apply them at adjudication. Separate edit files exist per provider setting. | [CMS, Medicare NCCI PTP Edits](https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits/medicare-ncci-procedure-procedure-ptp-edits); [CMS, Medicare NCCI MUEs](https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits/medicare-ncci-medically-unlikely-edits-mues) |
| **Medicaid** | Yes, but under a **separate Medicaid NCCI program** with its own policy manual, its own edit files, and its own technical guidance. Do not cite the Medicare manual at a Medicaid payer. | [CMS, Medicaid NCCI Edit Files](https://www.cms.gov/medicare/coding-billing/ncci-medicaid/medicaid-ncci-edit-files); [2026 Medicaid NCCI Policy Manual](https://www.cms.gov/files/document/2026-ncci-medicaid-policy-manual.pdf); [Medicaid NCCI Technical Guidance Manual](https://www.cms.gov/files/document/ncci-medicaid-technical-guidance-manual-2022.pdf) |
| **Commercial / ERISA / Medicare Advantage** | **Not established by any primary source retrieved.** NCCI is a CMS program; commercial application is a matter of the payer's own edit policy and the participation agreement. See **Open questions**. | — |

> **Do not present a Medicare NCCI rule as universal.** The CCMI and MAI values, the "cannot bill
> the beneficiary" rule, and the MAC appeal behavior below are all sourced to Medicare FFS
> guidance. A commercial payer may license the NCCI tables, modify them, add proprietary edits,
> or set different modifier-bypass behavior, and its member-liability rules are contractual.

**Medicare vs Medicaid, one confirmed divergence:** Medicare has confidential (non-published) MUE
values; the Medicaid NCCI program does not. "Medicare has some non-published or confidential MUEs.
However, there are currently no confidential or non-published edits in the Medicaid NCCI program"
([CMS, Medicaid NCCI FAQ Library](https://www.cms.gov/medicare/coding-billing/ncci-medicaid/medicaid-ncci-faq-library)).

---

## 2. PTP edits: what the edit actually asserts

| Element | Rule | Source |
|---|---|---|
| Purpose | NCCI PTP edits "prevent inappropriate payment of services that should not be reported together." | [CMS, Medicare NCCI PTP Edits](https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits/medicare-ncci-procedure-procedure-ptp-edits) |
| Structure | "Each edit has a Column One and Column Two HCPCS/CPT code." | [CMS, Medicare NCCI PTP Edits](https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits/medicare-ncci-procedure-procedure-ptp-edits) |
| Payment outcome | "If a provider reports the two codes of an edit pair for the same beneficiary on the same date of service, the **Column One code is eligible for payment, but the Column Two code is denied** unless a clinically appropriate NCCI PTP-associated modifier is also reported." | [CMS, Medicare NCCI PTP Edits](https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits/medicare-ncci-procedure-procedure-ptp-edits); [2026 NCCI Medicare Policy Manual, Ch. 1](https://www.cms.gov/files/document/01-chapter1-ncci-medicare-policy-manual-2026-final.pdf) |
| What the edit means clinically | "The existence of the NCCI PTP edit indicates that the 2 codes **generally cannot be reported together unless** the 2 corresponding procedures are performed at **2 separate patient encounters** or **2 separate anatomic locations**." | [CMS MLN901346, How to Use the Medicare NCCI Tools](https://www.cms.gov/outreach-and-education/medicare-learning-network-mln/mlnproducts/downloads/how-to-use-ncci-tools.pdf) |
| Trigger scope | Same provider/supplier, same beneficiary, same date of service. | [CMS, Medicare NCCI PTP Edits](https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits/medicare-ncci-procedure-procedure-ptp-edits) |

**Denial-resolution consequence:** the denied line is always the **Column Two** code. If the
remittance denied the Column One code instead, the problem is not a PTP edit — re-diagnose.

---

## 3. The Correct Coding Modifier Indicator (CCMI) — the primary decision key

This single field decides whether the denial is workable at all.

| CCMI | Verbatim meaning | Operational decision |
|---|---|---|
| **0** | "A CCMI of '0' indicates that NCCI PTP-associated modifiers **cannot be used to bypass the edit**." | **Never bypassable.** No modifier — 59, XE, XS, XP, XU, anatomic, or otherwise — will make the Column Two code payable. If the coding of both codes is correct, the Column Two code is **not separately payable**: adjust/write off. Appending a modifier anyway is a compliance exposure, not an appeal strategy. The only legitimate challenges are (a) the codes were mis-selected and the correct code pair carries no edit, or (b) the edit was applied to the wrong pair/date. |
| **1** | "A CCMI of '1' indicates that NCCI PTP associated modifiers **may be used to bypass an edit under appropriate circumstances**." | **Conditionally bypassable.** A modifier is permitted *only* if the clinical facts and the medical record independently meet the modifier's criteria (§5–§6). CCMI 1 is permission to look, not permission to append. |
| **9** | "A CCMI of '9' indicates that the use of NCCI PTP-associated modifiers is **not specified**. This indicator is used for all code pairs that have a **deletion date that is the same as the effective date**. This indicator prevents blank spaces from appearing in the indicator field." | **Not an active edit.** A CCMI 9 row is a placeholder for a pair that was deleted on the day it took effect. If a payer denied on a CCMI 9 pair, that is grounds to challenge the edit's applicability itself, not to append a modifier. |

Source for all three definitions: [CMS, Medicare NCCI PTP Edits](https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits/medicare-ncci-procedure-procedure-ptp-edits) and [2026 NCCI Medicare Policy Manual, Ch. 1 — General Correct Coding Policies](https://www.cms.gov/files/document/01-chapter1-ncci-medicare-policy-manual-2026-final.pdf).

> **Look up the CCMI before drafting anything.** The CCMI is published in the PTP edit files on the
> CMS NCCI pages and is versioned by quarter. Use the file version in effect **on the date of
> service**, not today's file — edits and indicators change quarterly
> ([CMS, NCCI for Medicare](https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits)).

---

## 4. NCCI PTP-associated modifiers

Only a defined set of modifiers can bypass a PTP edit; ordinary informational modifiers cannot.

| Group | Modifiers confirmed | Source |
|---|---|---|
| Anatomic | E1–E4, FA, F1–F9, TA, T1–T9, LT, RT, LC, LD, RC, LM, RI | [2026 NCCI Medicare Policy Manual, Ch. 1](https://www.cms.gov/files/document/01-chapter1-ncci-medicare-policy-manual-2026-final.pdf) |
| Distinct-service | 59, XE, XP, XS, XU | [2026 NCCI Medicare Policy Manual, Ch. 1](https://www.cms.gov/files/document/01-chapter1-ncci-medicare-policy-manual-2026-final.pdf); [CMS MLN1783722, Proper Use of Modifiers 59, XE, XP, XS & XU](https://www.cms.gov/files/document/mln1783722-proper-use-modifiers-59-xe-xp-xs-xu.pdf) |
| Global-surgery / E-M and other | Chapter 1 provides "further explanation … regarding modifiers **25, 58**, 59, XE, XP, XS, and XU." The **full enumerated roster** beyond the anatomic set could not be read in this environment — see **Open questions**. | [2026 NCCI Medicare Policy Manual, Ch. 1](https://www.cms.gov/files/document/01-chapter1-ncci-medicare-policy-manual-2026-final.pdf) |

**Hierarchy rule (binding, and the most commonly violated rule in the whole program):**
"Modifier 59, XE, XP, XS, & XU may be used **only if no other appropriate modifier describes the
service**" ([2026 NCCI Medicare Policy Manual, Ch. 1](https://www.cms.gov/files/document/01-chapter1-ncci-medicare-policy-manual-2026-final.pdf)).
CMS restates this operationally: "Use these modifiers instead of modifier 59 whenever possible.
**Only use modifier 59 if no other more specific modifier is appropriate**"
([CMS MLN1783722](https://www.cms.gov/files/document/mln1783722-proper-use-modifiers-59-xe-xp-xs-xu.pdf)).

Practical ordering that follows from the hierarchy rule:

1. If a **specific anatomic modifier** describes the distinction (RT/LT, FA/F1–F9, TA/T1–T9, E1–E4, LC/LD/RC/LM/RI) → use it. Do not use 59.
2. Else if a **specific X{EPSU} modifier** describes the distinction → use it. Do not use 59.
3. Else, and only then → 59.

---

## 5. Modifier 59 and the X{EPSU} subset — definitions and correct target

| Modifier | Retrieved definition | Use when | Do **not** use when |
|---|---|---|---|
| **XE** | "Separate Encounter — a service that is distinct because it **occurred during a separate encounter**." CMS adds: "This modifier shall **only** be used to describe separate encounters **on the same date of service**." | Two procedures on the same DOS in genuinely distinct patient encounters (separate sessions, documented as such). | The services were in one continuous session, even if hours long or with a break. Different dates of service — those are not one claim's PTP conflict and need no XE. |
| **XS** | "Separate Structure — a service that is distinct because it was **performed on a separate organ/structure**." | Different organ or anatomic structure, documented. | Same organ/structure, even if a different aspect or approach of it. |
| **XP** | "Separate Practitioner — a service that is distinct because it was **performed by a different practitioner**." | The two services were furnished by different practitioners whose claims land under the same billing entity/TIN. | Same practitioner. A different NPI on paper but the same rendering clinician is not a separate practitioner. |
| **XU** | "Unusual Non-Overlapping Service — a service that is distinct because it **does not overlap**" [the usual components of the main service]. Exact long descriptor not verified verbatim — see **Open questions**. | The Column Two service is genuinely outside the usual components of the Column One service. | The Column Two service is a component of, or overlaps, the Column One service — which is the exact situation the PTP edit was built to catch. |
| **59** | "Distinct Procedural Service" (NCCI PTP-associated modifier). Full CPT descriptor not verified from a CMS source in this retrieval — see **Open questions**. | **Only** where no anatomic modifier and no X{EPSU} modifier describes the distinction. | Any case where a more specific modifier exists, or where the distinctness criteria are not met at all (§6). |

Sources: [CMS MLN1783722, Proper Use of Modifiers 59, XE, XP, XS & XU (April 2026)](https://www.cms.gov/files/document/mln1783722-proper-use-modifiers-59-xe-xp-xs-xu.pdf) and its [landing page](https://www.cms.gov/outreach-and-education/medicare-learning-network-mln/mlnproducts/mln-publications/mln1783722); [2026 NCCI Medicare Policy Manual, Ch. 1](https://www.cms.gov/files/document/01-chapter1-ncci-medicare-policy-manual-2026-final.pdf).

**Provenance:** the X modifiers were "effective January 1, 2015, and were developed to provide
greater reporting specificity in situations where modifier 59 was previously reported and may be
used in lieu of modifier 59"
([CMS MLN1783722](https://www.cms.gov/files/document/mln1783722-proper-use-modifiers-59-xe-xp-xs-xu.pdf)).

**Superseded guidance — do not cite:** MLN Matters **SE1418, "Proper Use of Modifier 59," was
rescinded on June 7, 2021**. The current CMS authority is MLN1783722. Citing SE1418 in an appeal
signals stale research
([CMS MLN1783722](https://www.cms.gov/files/document/mln1783722-proper-use-modifiers-59-xe-xp-xs-xu.pdf); rescinded original archived at [SE1418](https://www.cms.gov/outreach-and-education/medicare-learning-network-mln/mlnmattersarticles/downloads/se1418.pdf)).

---

## 6. When modifier 59 / X{EPSU} is NOT supportable — write off, do not appeal

Each row below is a **disqualifying condition** confirmed against CMS primary guidance. If any row
matches, appending or defending 59/X is not supportable, and the correct disposition is to correct
the coding or adjust the balance — not to appeal.

| Disqualifying condition | Verbatim / near-verbatim rule | Source | Disposition |
|---|---|---|---|
| **CCMI = 0 on the pair** | "NCCI PTP-associated modifiers cannot be used to bypass the edit." | [CMS, Medicare NCCI PTP Edits](https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits/medicare-ncci-procedure-procedure-ptp-edits) | **Write off** the Column Two code (Medicare: not billable to the beneficiary — §9). No modifier appeal exists. |
| **Same anatomic site AND same patient encounter** | "If the 2 codes are performed at the **same anatomic site and same patient encounter**, they aren't considered 'separate and distinct,' and **you shouldn't use modifier 59 or XU** to bypass a PTP edit based on the 2 codes being 'different procedures.'" | [CMS MLN1783722](https://www.cms.gov/files/document/mln1783722-proper-use-modifiers-59-xe-xp-xs-xu.pdf) | **Write off.** This is the single most common abusive-59 pattern. |
| **The only justification offered is "different diagnoses"** | "You don't need a different diagnosis for each HCPCS- or CPT-coded procedure to use modifiers 59, XE, XP, XS, or XU. On the other hand, **different diagnoses aren't adequate criteria** for using modifiers 59, XE, XP, XS, or XU." | [CMS MLN1783722](https://www.cms.gov/files/document/mln1783722-proper-use-modifiers-59-xe-xp-xs-xu.pdf) | **Write off.** A distinct ICD-10 pointer on each line proves nothing about distinctness. |
| **The only justification offered is "the two code descriptors are different"** | "Modifiers 59 or XE, XP, XS, XU are used **inappropriately if the basis for their use is that the narrative description of the 2 codes is different**." | [2026 NCCI Medicare Policy Manual, Ch. 1](https://www.cms.gov/files/document/01-chapter1-ncci-medicare-policy-manual-2026-final.pdf) | **Write off.** Every PTP pair by definition has two different descriptors. |
| **Same session, same incision** | OIG found modifier 59 "was inappropriate because the two services were **not distinct since they were performed at the same session and through the same incision**." | [OIG, Use of Modifier 59 to Bypass Medicare's NCCI, OEI-03-02-00771](https://oig.hhs.gov/oei/reports/oei-03-02-00771.pdf) | **Write off.** |
| **A more specific modifier exists but was not used** | 59/XE/XP/XS/XU "may be used **only if no other appropriate modifier describes the service**." | [2026 NCCI Medicare Policy Manual, Ch. 1](https://www.cms.gov/files/document/01-chapter1-ncci-medicare-policy-manual-2026-final.pdf) | **Correct the claim** to the specific modifier (anatomic or X{EPSU}) and resubmit/reopen — do not appeal the 59. |
| **The medical record does not document the distinctness** | "Documentation in the medical record **must satisfy the criteria required by any NCCI-associated modifier** used." OIG: "for 12 percent of code pairs reviewed, one or both of the services billed **were not documented in the medical record**." | [2026 NCCI Medicare Policy Manual, Ch. 1](https://www.cms.gov/files/document/01-chapter1-ncci-medicare-policy-manual-2026-final.pdf); [OIG OEI-03-02-00771](https://oig.hhs.gov/oei/reports/oei-03-02-00771.pdf) | **Write off.** Appending a modifier the record cannot support is a false-claims exposure, not a denial fix. Do not request a modifier from the provider retroactively to match a denial. |
| **Criteria simply not met** | "Modifier 59 and other NCCI-associated modifiers **should not be used to bypass a PTP edit unless the proper criteria for use of the modifier are met**." | [2026 NCCI Medicare Policy Manual, Ch. 1](https://www.cms.gov/files/document/01-chapter1-ncci-medicare-policy-manual-2026-final.pdf) | **Write off.** |

**The affirmative test (what a supportable 59/X case looks like):** "If you perform 2 procedures at
**separate anatomic sites** or at **separate patient encounters** on the same date of service, you
may use modifiers 59, XE, or XS to show that they're different procedures on that DOS"
([CMS MLN1783722](https://www.cms.gov/files/document/mln1783722-proper-use-modifiers-59-xe-xp-xs-xu.pdf)).
Chapter 1 frames the same test as: appropriate circumstances "**relate to separate patient
encounters, separate anatomic sites, or separate specimens**"
([2026 NCCI Medicare Policy Manual, Ch. 1](https://www.cms.gov/files/document/01-chapter1-ncci-medicare-policy-manual-2026-final.pdf)).

**Enforcement context worth knowing before recommending an appeal:** OIG's review of modifier 59
found Medicare allowed an estimated **$16 million** for secondary services that were not documented
in the medical record, and reported one carrier that recovered **over $200,000** in improper
payments tied to inappropriate modifier 59 use
([OIG OEI-03-02-00771](https://oig.hhs.gov/oei/reports/oei-03-02-00771.pdf)). Modifier 59 is an
audit-targeted modifier; a weak 59 appeal invites review of every other 59 on the same provider.

---

## 7. MUE: definition, files, and what the edit measures

| Element | Rule | Source |
|---|---|---|
| Definition | "An MUE is the **maximum units of service (UOS) reported for a HCPCS/CPT code on the vast majority of appropriately reported claims** by the same provider/supplier for the same beneficiary on the same date of service." | [CMS, Medicare NCCI MUEs](https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits/medicare-ncci-medically-unlikely-edits-mues) |
| Purpose | "Prevent improper payments when services are reported with incorrect units of service"; MUEs are used by MACs "to reduce improper payments for Part B claims." | [CMS, Medicare NCCI MUEs](https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits/medicare-ncci-medically-unlikely-edits-mues) |
| Separate files by setting | "There are separate MUE files depending on the provider: **Practitioner (PRA), Outpatient Hospital (OPH), and Durable Medical Equipment (DME)**." | [CMS, Medicare NCCI MUEs](https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits/medicare-ncci-medically-unlikely-edits-mues) |
| Some values are **not published** | "Although CMS publishes most MUE values on its website, other MUE values are **confidential**" and "aren't released." "The public or confidential status of MUEs may change." | [CMS, Medicare NCCI MUEs](https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits/medicare-ncci-medically-unlikely-edits-mues) |
| Update cadence | Quarterly additions/deletions/revisions files are posted for Outpatient Hospital Services and Practitioner Services. | [CMS, Medicare NCCI MUEs](https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits/medicare-ncci-medically-unlikely-edits-mues); historical values at [Medicare NCCI MUE Archive](https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits/medicare-ncci-medically-unlikely-edit-mue-archive) |

> **Confidential-MUE consequence:** if a denial cites an MUE and the code has no published value,
> you cannot confirm the threshold. Do not assert a number in the appeal. Argue the **units
> actually furnished and documented**, and let the MAC apply the value.

---

## 8. MUE Adjudication Indicator (MAI) — the units decision key

| MAI | Edit type | Verbatim basis | How the claim is adjudicated | Can excess units be paid on appeal? |
|---|---|---|---|---|
| **1** | **Claim line edit** | "An MAI of '1' indicates that the edit is a **claim line MUE**." | "Each line of a claim is adjudicated against the MUE value for the HCPCS/CPT code on that claim line. **If the UOS on the claim line exceeds the MUE value, all UOS for that claim line are denied.**" If the same code is reported on more than one line using CPT modifiers, "each line of the claim is adjudicated **separately** against the MUE value of the code on that claim line." | **Yes.** MACs "may pay correctly coded and correctly counted medically necessary UOS in excess of the MUE value." |
| **2** | **Date of service edit — policy** | "MUEs for HCPCS codes with a MAI of '2' will be **absolute date of service edit**. These are '**per day edits based on policy**.'" Codes get MAI 2 "because UOS on the same date of service in excess of the MUE value **would be considered impossible because it was contrary to statute, regulation, or subregulatory guidance**." | All UOS on all claim lines with the same code and DOS are **summed** and compared against the MUE value. | **Effectively no.** CMS's appeal allowance names only MAI **"1" or "3."** MAI 2 is described as *absolute* and excess units as *impossible*. See **Open questions** for the limit of what was verified. **Correct the units; do not build an appeal.** |
| **3** | **Date of service edit — clinical** | "MUEs for HCPCS/CPT codes with an MAI of '3' are **date of service edits**… '**per day edits based on clinical benchmarks**.'" "The most common per day edit," where "the MUE is based on **clinical information such as billing patterns, prescribing instructions, or other information**." | All UOS on all claim lines with the same code and DOS are **summed** and compared against the MUE value. | **Yes, with records.** "If claim denials based on these edits are appealed, MACs **may pay UOS in excess of the MUE value if there is adequate documentation of medical necessity of correctly reported units**." |

Sources for all MAI rows: [CMS, Medicare NCCI MUEs](https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits/medicare-ncci-medically-unlikely-edits-mues); [CMS Transmittal R1421OTN (CR 8853), Revised Modification to the MUE Program](https://www.cms.gov/regulations-and-guidance/guidance/transmittals/downloads/r1421otn.pdf); [CMS MLN Matters MM8853](https://www.cms.gov/files/document/revised-modification-medically-unlikely-edit-mue-program-mm8853.pdf).

**What the MAC does on an MAI 3 reopening/redetermination:** "If during reopening or redetermination
medical records are provided with respect to an MUE denial for an edit with an MAI of '3', MACs will
review the records to determine **(a)** if the provider or supplier actually furnished units in
excess of the MUE, **(b)** if the codes were used correctly, and **(c)** whether the services were
medically reasonable and necessary"
([CMS, Medicare NCCI MUEs](https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits/medicare-ncci-medically-unlikely-edits-mues)).
Structure the MAI 3 appeal packet to answer those three questions in that order.

---

## 9. MUE resolution: correct vs. appeal, by MAI

| MAI | Correct disposition | Why |
|---|---|---|
| **1** | **First: re-bill correctly, don't appeal.** If the units were legitimately furnished under distinguishable circumstances, split them across separate claim lines with an appropriate modifier. "If a HCPCS/CPT code has an MUE that is adjudicated as a claim line edit (i.e., MAI equal to '1'), **appropriate use of CPT modifiers (i.e., 59 or XE, XP, XS, XU; 76, 77, 91, anatomic) may be used to report the same HCPCS/CPT code on separate lines of a claim**." Anatomic modifiers named: "RT, LT, FA, F1–F9, TA, T1–T9, E1–E4." Only appeal if the units on a single line were genuinely correct and exceed the value. | [CMS, Medicare NCCI MUEs](https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits/medicare-ncci-medically-unlikely-edits-mues); [R1421OTN](https://www.cms.gov/regulations-and-guidance/guidance/transmittals/downloads/r1421otn.pdf) |
| **2** | **Correct the units. Do not appeal.** Because the edit is a summed date-of-service edit, splitting across lines **does not help** — the system sums all lines with the same code and DOS. And excess units are treated as impossible under statute/regulation/subregulatory guidance. If the units billed were a data-entry or unit-conversion error, submit a corrected claim; if they were as intended, the excess is not payable. | [CMS, Medicare NCCI MUEs](https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits/medicare-ncci-medically-unlikely-edits-mues) |
| **3** | **Appeal with records — this is the appealable one.** Splitting lines does not help (summed DOS edit), so the path is reopening or redetermination with documentation establishing that the units were actually furnished, correctly counted, correctly coded, and medically reasonable and necessary. | [CMS, Medicare NCCI MUEs](https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits/medicare-ncci-medically-unlikely-edits-mues) |

> **Critical distinction the system must not blur:** modifiers help on **MAI 1** because each line is
> judged on its own. Modifiers do **not** defeat **MAI 2 or MAI 3**, because those edits sum every
> line carrying that code on that date of service. Recommending "add modifier 76 and rebill" on an
> MAI 3 denial produces a second identical denial.

---

## 10. Denial codes on the remittance

| Edit family | Codes | Source |
|---|---|---|
| **MUE** | "CMS Medicare claims processing contractors assign **MSN message 15.6, ANSI reason code 151, group code CO (contractual obligation), and remark codes N362 and MA01** to claims that fail the MUEs, when the units of service on the claim are in excess of the MUE value, and **deny the entire claim line(s)** for the relevant HCPCS code." RARC **N362** = "the number of days or units of service exceeds our acceptable maximum." | [CMS Transmittal R1421OTN (CR 8853)](https://www.cms.gov/regulations-and-guidance/guidance/transmittals/downloads/r1421otn.pdf); [CMS MLN Matters MM8853](https://www.cms.gov/files/document/revised-modification-medically-unlikely-edit-mue-program-mm8853.pdf) |
| **PTP** | **Not verified in this retrieval.** See **Open questions**. Do not assert a CARC/RARC pairing for PTP denials without confirming it against the MAC's remittance-code guidance. | — |

**Group code CO** signals a contractual-obligation adjustment — provider liability, not patient
liability — which is consistent with the beneficiary-liability rule in §11
([CMS Transmittal R1421OTN](https://www.cms.gov/regulations-and-guidance/guidance/transmittals/downloads/r1421otn.pdf)).

---

## 11. Beneficiary liability — Medicare (do not extend to other payers)

| Rule | Verbatim | Source |
|---|---|---|
| Cannot balance-bill the patient | "**Providers cannot bill a Medicare patient for a service denied based on PTP code pair edits or MUEs.**" | [CMS, Medicare NCCI FAQ Library](https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits/medicare-ncci-faq-library) |
| These are coding denials, not medical-necessity denials | "A denial of services due to a **PTP edit** is a **coding denial, not a medical necessity denial**." Same for MUE: "A denial of services due to an MUE is a coding denial, not a medical necessity denial." | [CMS, Medicare NCCI FAQ Library](https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits/medicare-ncci-faq-library) |
| ABN does not rescue it | "It's **inappropriate to issue an ABN** based on an MUE." "The presence of an ABN **doesn't shift liability to the beneficiary** for units of service denied based on an MUE." Same rule stated for PTP edits. | [CMS, Medicare NCCI FAQ Library](https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits/medicare-ncci-faq-library) |
| Statutory reason | "Denials resulting from MUEs are **not based on any of the statutory provisions that give liability protection to beneficiaries under section 1879 of the Social Security Act**." | [CMS, Medicare NCCI FAQ Library](https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits/medicare-ncci-faq-library) |

> **Consequence for write-off decisions:** on Medicare, an unappealable NCCI denial is a genuine
> **write-off** — it cannot be moved to patient responsibility, and no ABN on file changes that.
> For Medicaid and commercial payers, member liability is governed by the state plan or the
> participation agreement and was **not** established here — see **Open questions**.

---

## 12. Decision matrix for a denial-resolution system

Read top to bottom; the first matching row governs.

| # | Observed condition | Action |
|---|---|---|
| 1 | Denial is a units/frequency denial (e.g. CARC 151 + N362) | Go to the **MUE** branch, row 8+. Do not evaluate CCMI. |
| 2 | Denial is a code-pair denial, denied code is the Column Two code | Go to the **PTP** branch, row 3+. |
| 3 | PTP: look up CCMI **for the DOS quarter**; CCMI = **9** | Edit was deleted effective the same day it took effect. Challenge applicability of the edit itself. |
| 4 | PTP: CCMI = **0** | **Write off** the Column Two code. No modifier bypass exists. Medicare: not billable to beneficiary. Only alternative path is a coding correction if the wrong codes were selected. |
| 5 | PTP: CCMI = **1**, but same anatomic site **and** same encounter | **Write off.** 59/XU not supportable. |
| 6 | PTP: CCMI = **1**, and the only rationale is different diagnoses, or different code descriptors | **Write off.** Both are expressly inadequate criteria. |
| 7 | PTP: CCMI = **1**, distinctness is real, and a **specific anatomic or X{EPSU} modifier** describes it, and the record documents it | **Correct and resubmit/reopen** with the *specific* modifier. Do not use 59. |
| 8 | PTP: CCMI = **1**, distinctness is real and documented, and **no** more specific modifier fits | **Modifier 59** is supportable. Appeal/reopen citing the record's documentation of the distinct encounter/site/specimen. |
| 9 | MUE: **MAI 1**, units were furnished under distinguishable circumstances, record supports it | **Rebill on separate lines** with an appropriate modifier (59/XE/XP/XS/XU, 76, 77, 91, or anatomic). Appeal only if the single-line units were genuinely correct. |
| 10 | MUE: **MAI 2** | **Correct the units.** Do not appeal; do not split lines (edit sums by DOS). If units were as intended, the excess is not payable. |
| 11 | MUE: **MAI 3**, units actually furnished and documented | **Appeal (reopening/redetermination) with medical records** addressing: units actually furnished, correct coding, medical necessity. Do not split lines. |
| 12 | Any of the above where the medical record does not document what the modifier or the units assert | **Write off.** Do not solicit a retroactive modifier or addendum to match a denial. |

---

## Open questions

- **Full roster of NCCI PTP-associated modifiers.** Only the anatomic set (E1–E4, FA, F1–F9, TA, T1–T9, LT, RT, LC, LD, RC, LM, RI) and the distinct-service set (59, XE, XP, XS, XU) were confirmed. Chapter 1 references "further explanation … regarding modifiers 25, 58, 59, XE, XP, XS, and XU," which implies global-surgery and E/M modifiers are in the roster, but the **complete enumerated list** (commonly said to include 24, 25, 27, 57, 58, 78, 79, 91) **could not be read** because cms.gov was egress-blocked. Do not assert that a given global-surgery modifier bypasses a PTP edit without opening [2026 NCCI Medicare Policy Manual, Ch. 1](https://www.cms.gov/files/document/01-chapter1-ncci-medicare-policy-manual-2026-final.pdf).
- **Exact HCPCS long descriptor for modifier XU.** The retrieved excerpt was truncated mid-sentence ("…distinct because it does not"). The bracketed completion above is inference, not a verified quote. Confirm against [MLN1783722](https://www.cms.gov/files/document/mln1783722-proper-use-modifiers-59-xe-xp-xs-xu.pdf) before quoting.
- **Exact CPT descriptor and the enumerated criteria for modifier 59.** The CPT criteria commonly cited (different session, different procedure or surgery, different site or organ system, separate incision/excision, separate lesion, separate injury) come from the AMA CPT manual. They were **not** confirmed from a CMS primary source in this retrieval. Do not quote them as CMS language.
- **CARC/RARC pairing for PTP (code-pair) denials.** Not established — the search budget was exhausted before this could be confirmed. Do not assert CO-97, B15, M80, or any other specific pairing for a PTP denial without confirming it against the relevant MAC's remittance-code guidance.
- **Whether MAI 2 denials are formally non-appealable, or appealable but never overturned.** What is confirmed is (a) MACs may pay excess UOS on appeal for MAI **"1" or "3"**, and (b) MAI 2 edits are "absolute" and excess UOS "would be considered impossible because … contrary to statute, regulation, or subregulatory guidance." No text was located that **explicitly** states an MAI 2 denial cannot be overturned. Treat MAI 2 as practically unappealable; do not tell a client it is *legally* unappealable.
- **Whether the Practitioner PTP file also governs ASC claims**, and the exact names/count of the Medicare PTP edit files (practitioner vs. outpatient hospital). Not confirmed. The MUE file split (PRA / OPH / DME) **was** confirmed; the PTP file split was not.
- **Statutory basis for the Medicaid NCCI program.** Commonly attributed to §6507 of the Affordable Care Act. Not confirmed from a primary source in this retrieval. Cite the [Medicaid NCCI Technical Guidance Manual](https://www.cms.gov/files/document/ncci-medicaid-technical-guidance-manual-2022.pdf) or the [2026 Medicaid NCCI Policy Manual](https://www.cms.gov/files/document/2026-ncci-medicaid-policy-manual.pdf), not the statute, until verified.
- **Substantive Medicaid/Medicare divergences beyond confidential MUEs.** The Medicaid NCCI program has its own manual and its own edit files, so CCMI/MAI semantics may or may not be identical. Only the confidential-MUE divergence was confirmed. Verify per state before applying a Medicare rule to a Medicaid denial.
- **Whether and how commercial payers and Medicare Advantage plans apply NCCI.** No primary source was located. Many commercial payers license or mirror NCCI, but bypass behavior, appeal rights, and member liability are contractual. Do not apply §11 (no balance billing) outside Medicare FFS without reading the participation agreement.
- **NCCI quarterly release/effective dates.** Quarterly updating is confirmed for MUE additions/deletions/revisions files; the specific effective dates each year, and the rule for which file version governs a given date of service, were not confirmed from primary text.
- **Timely-filing and appeal deadlines for NCCI denials.** Out of scope here; see `reference/timely-filing.md` and `reference/appeal-levels.md` in this repo. Nothing in this file establishes a deadline.
