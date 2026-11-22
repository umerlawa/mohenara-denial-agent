# RARC / CARC index — the codes this corpus actually carries

> **Retrieved 2026-08-12.**
>
> **Retrieval conditions.** Direct HTTPS fetch of `x12.org`, `cms.gov`, `ecfr.gov` and every
> MAC host is refused by this environment's egress proxy (`gateway answered 403 to CONNECT`;
> confirmed via `$HTTPS_PROXY/__agentproxy/status`). Wording below was retrieved by
> domain-restricted search over those same primary domains plus government republications of
> the X12 lists (CMS transmittals, MAC provider pages, state agency code lists). **X12 is the
> controlling authority** ([X12, Remittance Advice Remark Codes](https://x12.org/codes/remittance-advice-remark-codes);
> [X12, Claim Adjustment Reason Codes](https://x12.org/codes/claim-adjustment-reason-codes)).
> Every wording below is a **retrieved excerpt, not a verbatim read of the live X12 list** —
> rows where that matters are called out in **Open questions**.
>
> Columns marked *corpus* were measured deterministically over
> `corpus/v2-chain-corpus-v1.1{,-md}/` (563 cases) by grep. No label file was opened.
>
> **Gate:** the group code (835 `CAS01`), never the CARC, assigns liability
> ([CMS, Medicare Claims Processing Manual ch. 22](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c22.pdf);
> [Noridian, Claim Adjustment Group Codes](https://med.noridianmedicare.com/web/jddme/topics/ra/claim-adjustment-group-codes)).

---

## 1. RARCs

`MOA` = claim-level `MOA` segment. `LQ*HE` = line-level `LQ` segment in 2110. Placement is
*corpus*-measured and is load-bearing: a line-level parser that only reads `MOA` misses
N822/N20/N362 entirely, and a claim-level parser that only reads `MOA` misses which **line** failed.

| RARC | Official wording (X12, via primary republication) | 835 placement *(corpus)* | Pairs with *(corpus)* | What it points to | Source |
|---|---|---|---|---|---|
| **N822** | "Missing procedure modifier(s)." | `LQ*HE`, 152 lines | `CO-4` | A required modifier is absent from the line — here the therapy discipline modifier (`GP`); fix the line and submit a **new** claim, not an appeal | [NGS, Reason Code CO-16](https://www.ngsmedicare.com/web/ngs/search-details?selectedArticleId=11775612); [X12 RARC list](https://x12.org/codes/remittance-advice-remark-codes) |
| **N435** | "Exceeds number/frequency approved /allowed within time period without support documentation." | `MOA`, 45 claims | `CO-119` | Benefit/threshold ceiling hit with nothing on the claim attesting medical necessity — for outpatient therapy that attestation is the `KX` modifier | [CMS, Transmittal R2776CP](https://www.cms.gov/regulations-and-guidance/guidance/transmittals/downloads/r2776cp.pdf); [CMS, Therapy Reason Codes and Statements](https://www.cms.gov/files/document/therapy-reason-codes-and-statements.pdf) |
| **N20** | "Service not payable with other service rendered on the same date." | `LQ*HE`, 56 lines | `CO-236` | The *column-2* line of an NCCI PTP pair; names the denied line, not the pair — the partner code is not on the remit | [Noridian, Reason Code 234 / Remark N20](https://med.noridianmedicare.com/web/jadme/topics/ra/denial-resolution/n20-234); [CMS, Transmittal R731CP](https://www.cms.gov/regulations-and-guidance/guidance/transmittals/downloads/r731cp.Pdf) |
| **N111** | "No appeal right except duplicate claim/service issue. This service was included in a claim that has been previously billed and adjudicated." | `MOA`, 45 claims | `OA-18` | Appeal rights are foreclosed **except** on the question of whether the duplication is real; merits arguments are dead on arrival | [CMS, Transmittal AB-02-067](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/downloads/AB02067.pdf); [Noridian, How to Verify Claim Denial Resolutions](https://med.noridianmedicare.com/web/jeb/article-detail/-/view/10525/how-to-verify-claim-denial-resolutions-efficiently) |
| **N362** | "The number of Days or Units of Service exceeds our acceptable maximum." | `LQ*HE`, 45 lines | `CO-151` | MUE ceiling on that HCPCS for that beneficiary/date; the MUE value and its MAI are **not on the remit** | [CMS, Transmittal R12763CP](https://www.cms.gov/files/document/r12763cp.pdf); [Noridian, MUE — Units Exceed Acceptable Maximum](https://med.noridianmedicare.com/web/jeb/topics/claim-submission/reason-code-guidance/mue-service-exceeds-max) |
| **N211** | "You may not appeal this decision." | `MOA`, 45 claims | `CO-29` | Flat bar on appeal — with `CO-29` this is the Medicare FFS timely-filing bar, so the only routes left are the statutory filing exceptions or write-off | [CMS, Transmittal R32CP](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/downloads/R32CP.pdf) |
| **N286** | "Missing/incomplete/invalid referring provider primary identifier." | `MOA`, 45 claims | `CO-16` | The referring/ordering provider NPI (item 17b / 837P loop 2310A) is absent or fails PECOS validation; correct and resubmit as a new claim | [Noridian, Reason Code 16 / Remark N286](https://med.noridianmedicare.com/web/jddme/topics/ra/denial-resolution/n286-16); [CMS, Transmittal R436CP](https://www.cms.gov/regulations-and-guidance/guidance/transmittals/downloads/r436cp.pdf) |
| **N30** | "Patient ineligible for this service." | `MOA`, 45 claims | `PR-27` / `CO-27` | Beneficiary not eligible for *this* service on the DOS; **N30 does not state why, and does not set liability** — read `CAS01` (PR vs CO), not the RARC | [Noridian, Reason Code 97 / Remark N30](https://med.noridianmedicare.com/web/jddme/topics/ra/denial-resolution/n30-97); [Utah Medicaid, Claim Denial Codes](https://medicaid-documents.dhhs.utah.gov/Documents/pdfs/ClaimDenialCodes.pdf) |
| **MA04** | "Secondary payment cannot be considered without the identity of or payment information from the primary payer. The information was either not reported or was illegible." | `MOA`, 45 claims | `CO-22` / `OA-22` | **The COB signature.** Demands the *primary payer's identity and its adjudication data* on the claim — 837P loop 2320 `SBR`/`AMT` plus the primary's `CAS` amounts. A completion defect: resubmit with the primary's data, do **not** appeal | [Noridian, Reason Code 22 / Remark MA04](https://med.noridianmedicare.com/web/jadme/topics/ra/denial-resolution/ma04-22); [Palmetto GBA, Medicare as Secondary Payer (JM Part B)](https://dominoapps.palmettogba.com/palmetto/jmb.nsf/DID/J6AJLTHH0Q) |
| **M49** | "Missing/incomplete/invalid value code(s) or amount(s)." | **absent** — 0 occurrences | — | Real RARC, but an institutional (UB-04 value code) defect. **It is not in this corpus.** All 99 apparent hits, across 54 files, are the substring `M49` inside member ID `3AE3VM3DM49`; zero standalone occurrences | [CMS, Transmittal AB-03-095](https://www.cms.gov/regulations-and-guidance/guidance/transmittals/downloads/AB03095.pdf) |
| **M542** | — **not a RARC. No such code exists in the X12 RARC list.** | 837P `HI*ABK:M542~` only, 22 claims | — | **ICD-10-CM `M54.2`, Cervicalgia** (neck pain), the principal diagnosis, decimal stripped per 837P convention; `ABK` is the HI qualifier for the principal ICD-10-CM diagnosis | [CMS, ICD-10-CM/PCS MS-DRG Definitions Manual](https://www.cms.gov/icd10m/fy2025-version42.1-fullcode-cms/fullcode_cms/P0554.html); [CDC, ICD-10-CM browser](https://icd10cmtool.cdc.gov/); [CMS, Qualifiers for ICD-10 Diagnosis Codes on Electronic Claims](https://www.cms.gov/medicare/coding/icd10/downloads/icd10listservqualifiersfordiagnosiscodes.pdf) |

---

## 2. CARCs

| CARC | Official wording (X12, via primary republication) | Group code *(corpus)* | What it points to | Source |
|---|---|---|---|---|
| **2** | "Coinsurance Amount." | `PR` only | Beneficiary coinsurance on an **allowed, paid** line — an adjudication result, never a defect; billable to the patient subject to QMB / 42 CFR 447.15 / ABN-validity overrides | [Noridian, Claim Adjustment Group Codes](https://med.noridianmedicare.com/web/jddme/topics/ra/claim-adjustment-group-codes); [CMS, Medicare Claims Processing Manual ch. 22](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c22.pdf) |
| **4** | "The procedure code is inconsistent with the modifier used or a required modifier is missing." Usage: refer to the 835 Healthcare Policy Identification Segment (loop 2110 `REF`), if present. | `CO` only | Modifier defect on the line; unprocessable, so `CO` and never billable to the patient. Paired `N822` names it as a **missing** modifier, not a wrong one | [Palmetto GBA, Code/Modifier Combination Invalid and Modifier Invalid/Missing (JM Part B)](https://www.palmettogba.com/palmetto/jmb.nsf/DID/8EELL47648); [CT OHS, CARC code list (X12 republication)](https://portal.ct.gov/-/media/ohs/health-it-advisory-council/apcd-advisory-group/data-submission-guide-workgroup/meeting-materials/6-30-22/carc-codes_final.pdf) |
| **45** | "Charge exceeds fee schedule/maximum allowable or contracted/legislated fee arrangement." Usage: this adjustment amount cannot equal the total service or claim charge amount, and must not duplicate prior-payer adjustments. (Use only with Group Codes `PR` or `CO` depending upon liability.) | `CO` only | Contractual write-off on an **allowed, paid** line — the gap between charge and allowed amount. Not a denial. A `CAS*CO*45` equal to 100% of the charge is a disguised denial; demand a corrected 835 | [X12 RFI #1802, CO45 adjust as a full writeoff](https://x12.org/resources/requests-for-interpretation/rfi-1802-co45-adjust-full-writeoff); [X12 RFI #2052](https://x12.org/resources/requests-for-interpretation/rfi-2052-casco45-being-used-denial); [CMS, Transmittal R2372CP](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/downloads/R2372CP.pdf) |
| **119** | "Benefit maximum for this time period or occurrence has been reached." | `CO` only | Threshold/benefit ceiling. For outpatient therapy, the `KX` threshold: absent `KX`, **the therapist is financially liable** and liability transfers to the beneficiary only on a valid ABN (CMS-R-131) — which would show as `PR`, not `CO` | [CMS, Medicare Claims Processing Manual ch. 5](https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/Downloads/clm104c05.pdf); [Noridian, Per-Beneficiary KX Modifier Thresholds](https://med.noridianmedicare.com/web/jfb/specialties/outpatient-therapy/per-beneficiary_kx_modifier_thresholds); [CMS, MM9751](https://www.cms.gov/outreach-and-education/medicare-learning-network-mln/mlnmattersarticles/downloads/mm9751.pdf) |
| **151** | "Payer deems the information submitted does not support this many/frequency of services." | `CO` only | MUE failure on **units**. Appeal goes to the MAC (MUE values are not appealable to NCCI); if the units were miscoded, correct and resubmit instead. Never patient liability under `CO` | [CMS, Transmittal R12471CP](https://www.cms.gov/files/document/r12471cp.pdf); [Noridian, MUE — Units Exceed Acceptable Maximum](https://med.noridianmedicare.com/web/jeb/topics/claim-submission/reason-code-guidance/mue-service-exceeds-max) |
| **236** | "This procedure or procedure/modifier combination is not compatible with another procedure or procedure/modifier combination provided on the same day according to the National Correct Coding Initiative or workers compensation state regulations/ fee schedule requirements." | `CO` only | NCCI PTP edit. CMS assigns CARC 236 with Group Code `CO` and MSN 16.8 for PTP failures. Modifier 59/`XE`/`XS`/`XP`/`XU` may unbundle **only** where the CCMI is `1` and the documentation supports it — and the CCMI is not on the remit | [CMS, Transmittal R4188CP](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/2018Downloads/R4188CP.pdf); [Noridian, Not Separately Payable / NCCI](https://med.noridianmedicare.com/web/jeb/topics/claim-submission/reason-code-guidance/not-separately-payable-national-correct-coding-initiative); [CMS, MLN1783722 Proper Use of Modifiers 59, XE, XP, XS, XU](https://www.cms.gov/files/document/mln1783722-proper-use-modifiers-59-xe-xp-xs-xu.pdf) |

---

## 3. `PR-2` + `CO-45` — the paid-line signature, and the trap in it

Established: `PR-2` and `CO-45` are the two halves of a **normally adjudicated, paid** service
line. Billed = paid + `CO-45` (contractual) + `PR-2` (coinsurance); the 835 must balance at the
service, claim, and provider level, so a paid line's charge is fully accounted for by exactly
these two adjustments and nothing is being denied
([CMS, Medicare Claims Processing Manual ch. 22](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c22.pdf);
[CMS MLN, Remittance Advice Resources and FAQs ICN 905367](https://www.cms.gov/Outreach-and-Education/Medicare-Learning-Network-MLN/MLNProducts/Downloads/ICN905367TextOnly.pdf)).

| Assertion | Verdict | Evidence *(corpus, 563 cases)* |
|---|---|---|
| `CO-45` and `PR-2` are adjustments, not denials | **True** | They co-occur on every paid line; `CO-45` never appears alone as a 100%-of-charge write-off |
| A resolver may treat `PR-2` or `CO-45` as a denial signal | **False — invents defects on clean claims** | 117 cases carry the pair with no other CARC; all 117 are `status 1 (processed as primary, paid)` |
| The **pair's presence** is the signature of a correctly adjudicated **claim** | **False — it is the signature of a correctly adjudicated LINE** | 86 cases carry `CO-45` + `PR-2` on some lines *and* a real denial CARC on others: `CO-151` (45/45 cases) and `CO-236` (41/41 cases) are always partial denials |
| Claim `status 1 (paid)` means the claim is clean | **False** | 203 cases are status 1; only 117 are clean. The other 86 are the MUE and NCCI partial denials above |
| The safe clean-claim test | **`CO-45` + `PR-2` present AND no other CARC anywhere on the claim** | 117/117 precision on this corpus |
| Whole-claim denial families never show the pair | **True** | `CO-119`, `CO-29`, `OA-18`, `CO-16`, `PR-27`, `CO-27`, `OA-22`, `CO-22`, `CO-4`: 0 of their cases carry `CO-45` |

> Parser note: `CO-4` is a **prefix of** `CO-45`. Matching on the bare string `CO-4` mislabels
> all 203 clean/partially-paid cases as therapy-modifier denials. Anchor on `CO-4 ` / `CO-4(`
> or use a word boundary.

---

## 4. `M542` — resolved: noise, and the reason it looked like a code

| Question | Answer |
|---|---|
| Is `M542` a RARC? | No. It is not on the X12 RARC list; no `M`-series RARC has four digits |
| What is it? | ICD-10-CM **`M54.2` Cervicalgia**, the principal diagnosis, written without the decimal as 837P requires |
| Where does it appear? | `HI*ABK:M542~` in the 837P only — 22 claims, 0 occurrences in any 835 `MOA` or `LQ` segment *(corpus)* |
| Why does it cross unrelated defect families? | It is the study population's shared presenting diagnosis (outpatient PT for neck pain), so it is orthogonal to the defect |
| Decision-relevant? | **No — noise for remit parsing.** Never cite it as a remark code |
| Why it was mistaken for one | A RARC-shaped regex such as `[MN]A?\d{2,3}` matches the diagnosis string. The same misfire produces the phantom `M49` in §1 (from member ID `3AE3VM3DM49`). **Extract RARCs from `MOA`/`LQ` segments by position, not by pattern over free text** |

---

## Open questions

- **No wording below was read verbatim from the live X12 lists.** `x12.org` is egress-blocked in
  this environment. Every quoted narrative is a retrieved excerpt from a CMS transmittal, a MAC
  page, or a state-agency republication. X12 revises RARC/CARC wording three times a year; treat
  each string as accurate-as-republished, not as a current verbatim read.
- **`N30` usage conflict.** Noridian documents `N30` paired with **CARC 97** (bundled); this
  corpus pairs it with **CARC 27** (coverage terminated). Whether X12 intends `N30` as
  eligibility-specific, or the MACs simply reuse it, is not established. Do not infer the
  eligibility *reason* from `N30` — it is not in the code.
- **`N362` / CARC pairing conflict.** [CMS R12763CP](https://www.cms.gov/files/document/r12763cp.pdf)
  pairs `N362` with **CARC 119** for frequency-limited screening services, while the MUE
  instruction pairs it with **CARC 151**. This corpus uses `151`+`N362` (MUE) and `119`+`N435`
  (threshold). Which convention a non-Medicare payer follows is not established.
- **`CO-151` + `N362` normally also carries `MA01`** (appeal rights) per the CMS MUE instruction.
  `MA01` does not appear anywhere in this corpus. Whether its absence is a corpus simplification
  or a payer variation is unresolved; do not assert appeal rights from the remit alone.
- **CARC 4 "Usage" note** (loop 2110 `REF*0K`) is corroborated only by state-agency and
  vendor republications, not by a CMS or X12 document read directly. The base narrative is solid;
  the Usage sentence is not.
- **One stray `LQ*HE*M80`** appears on a single line in the corpus (documented in
  `carc-rarc-remedies.md` §6). Too rare to key on; not investigated here.
- **No group code is established as *required* for CARC 2, 22, 27, or 45** beyond CARC 45's
  "use only with `PR` or `CO`". This corpus is internally consistent (`PR-2`, `CO-45`), but that
  is an observation about this corpus, not a rule.
