# Coordination of Benefits and Eligibility: Primacy Order, 270/271, and Terminated Coverage

> Retrieved 2026-08-12.
>
> ## ⚠ RETRIEVAL FAILURE NOTICE — READ BEFORE CITING
>
> **Live retrieval was unavailable in the session that produced this file.** The web-search budget
> was exhausted (200/200) and the network egress proxy returned `EGRESS_BLOCKED` for every primary
> domain attempted: `cms.gov`, `ecfr.gov`, `x12.org`, `govinfo.gov`, `content.naic.org`, `dol.gov`,
> `med.noridianmedicare.com`. No external page was read.
>
> Every row therefore carries a **Basis** column with exactly one of two values:
>
> | Basis | Meaning | Safe to quote at runtime? |
> |-------|---------|---------------------------|
> | **`corpus`** | Verified this session by reading files under `/home/user/mohenara-tathastu/corpus/v2-chain-corpus-v1.1-md/`. The claim describes what the transactions in this repo actually contain. | **Yes** — but only as a statement about this repo's data, not as external legal authority. |
> | **`pointer`** | The named primary source is real and is the correct authority for the rule, but **its text was not retrieved in this session**. The rule statement is reconstructed, not quoted. | **No.** Treat as a research lead requiring one human lookup at the cited URL before it is relied on. |
>
> A denial-resolution system consuming this file **must not present a `pointer` row to a user as
> established authority.** Downgrade it, or gate it behind verification. Sections whose whole
> content is `pointer` are marked at the section heading.
>
> Rules I could not pin down even to a confident `pointer` are in **[§11 Open questions](#11-open-questions)** and are not asserted anywhere above it.

---

## 1. Decision entry point — which section applies

| Signal on the 835 / 271 | Problem class | Go to |
|---|---|---|
| CARC **22** (any group code), RARC **MA04** | Payer believes someone else is primary | §5, §6 |
| CARC **109** | Payer believes it is not the payer at all (wrong plan/contractor), not a COB order question | §5.4 |
| CARC **27** with group **PR** | Coverage ended; payer asserts patient liability | §8 |
| CARC **27** with group **CO** | Coverage ended; payer asserts **provider** liability | §8 |
| 271 returns `EB*6` (Inactive) | Eligibility says no active coverage on the plan date | §7, §8 |
| 271 returns `EB*R` (Other or Additional Payer) | Another payer exists on this member's record | §5, §7.3 |
| 271 returns `AAA` rejection | The inquiry itself failed; **not** evidence of no coverage | §7.5 |
| Payer reversed a previously paid claim months later | Retroactive termination / rescission / grace-period reversal | §9 |
| Coverage restored after denial | Retroactive reinstatement | §10 |

---

## 2. Codes this file resolves — definitions verified against this repo

These four are the COB/eligibility denial surface actually present in
`corpus/v2-chain-corpus-v1.1-md/`. Counts are occurrences across the corpus.

| Code | Group codes observed | Wording as carried in the corpus | Count | Basis |
|---|---|---|---|---|
| **CARC 22** | `OA` and `CO` | "care may be covered by another payer per coordination of benefits" | OA-22 ×103, CO-22 ×48 | `corpus` — `grep -rhoE "(CO\|PR\|OA\|PI)-[0-9]+ \([^)]*\)"` over `corpus/v2-chain-corpus-v1.1-md/` |
| **CARC 27** | `PR` and `CO` | "expenses incurred after coverage terminated" | PR-27 ×76, CO-27 ×66 | `corpus` — same enumeration |
| **RARC MA04** | MOA segment | "secondary payment cannot be considered without primary payer identity" | e.g. `corpus/v2-chain-corpus-v1.1-md/MOH2-000087/case.md` | `corpus` |
| **RARC N30** | MOA segment | "patient ineligible for this service" | e.g. `corpus/v2-chain-corpus-v1.1-md/MOH2-000587/case.md` | `corpus` |

**Load-bearing observation from the corpus:** CARC 27 appears under **both** `PR` and `CO` at
comparable frequency (76 vs 66). The reason code is therefore **not** sufficient to decide patient
liability. The **group code** decides it. See §8.1.

> Cross-reference: general CARC/RARC/group-code semantics, and the CMS rule that a Medicare
> beneficiary may be billed only when group code `PR` is used, are already established in
> [`reference/carc-rarc-remedies.md`](./carc-rarc-remedies.md) §§2–3 of this repo. This file does
> not restate them.

---

## 3. Medicare Secondary Payer — who is primary

> **Section basis: `pointer` throughout.** Statutory/regulatory citations below are the correct
> authorities and the thresholds are the well-known ones, but no text was retrieved this session.
> Verify each at the URL before use.

### 3.1 The three employment-based MSP provisions

| Provision | Beneficiary | Coverage that triggers it | Size threshold | Primary payer | Source (not retrieved) |
|---|---|---|---|---|---|
| **Working Aged** | Age 65+ | Group Health Plan (GHP) by virtue of the **current employment status** of the beneficiary **or spouse** | Employer has **20 or more** employees | **GHP primary**, Medicare secondary | [42 U.S.C. §1395y(b)(1)(A)](https://www.law.cornell.edu/uscode/text/42/1395y); [42 CFR §411.172](https://www.ecfr.gov/current/title-42/section-411.172) |
| Working Aged — below threshold | Age 65+ | Same | Employer has **fewer than 20** employees | **Medicare primary** | [42 U.S.C. §1395y(b)(1)(A)](https://www.law.cornell.edu/uscode/text/42/1395y) |
| **Disability** | Under 65, Medicare on the basis of disability | **Large** Group Health Plan (LGHP) by virtue of the current employment status of the beneficiary **or a family member** | Employer has **100 or more** employees | **LGHP primary**, Medicare secondary | [42 U.S.C. §1395y(b)(1)(B)](https://www.law.cornell.edu/uscode/text/42/1395y); [42 CFR §411.200](https://www.ecfr.gov/current/title-42/section-411.200) |
| Disability — below threshold | Under 65, disabled | Same | Employer has **fewer than 100** employees | **Medicare primary** | [42 U.S.C. §1395y(b)(1)(B)](https://www.law.cornell.edu/uscode/text/42/1395y) |
| **ESRD** | Medicare on the basis of End-Stage Renal Disease | **Any** GHP — current employment status is **not** required, retiree and COBRA coverage counts | **No size threshold** | **GHP primary for a 30-month coordination period**; Medicare primary thereafter | [42 U.S.C. §1395y(b)(1)(C)](https://www.law.cornell.edu/uscode/text/42/1395y); [42 CFR §411.162](https://www.ecfr.gov/current/title-42/section-411.162) |

**Three traps in the table above:**

1. **"Current employment status" is the switch for Working Aged and Disability, not "has insurance."**
   Retiree GHP coverage and COBRA are *not* current employment status. A 67-year-old on a retiree
   plan → **Medicare primary**, retiree plan secondary. `pointer` — [42 CFR §411.170](https://www.ecfr.gov/current/title-42/section-411.170).
2. **ESRD ignores both of those.** ESRD makes the GHP primary for 30 months even if the coverage is
   retiree or COBRA and even if the employer has 3 employees. `pointer` — [42 U.S.C. §1395y(b)(1)(C)](https://www.law.cornell.edu/uscode/text/42/1395y).
3. **The disability threshold is 100, not 20.** Applying the Working Aged number to a
   disability-entitled beneficiary is the single most common MSP misread. `pointer` — [42 U.S.C. §1395y(b)(1)(B)](https://www.law.cornell.edu/uscode/text/42/1395y).

### 3.2 Non-employment MSP situations

| Situation | Primary payer | Note | Source (not retrieved) |
|---|---|---|---|
| Workers' compensation | **WC primary** for the work-related injury | Medicare may make a conditional payment if WC will not pay promptly | [42 U.S.C. §1395y(b)(2)](https://www.law.cornell.edu/uscode/text/42/1395y); [42 CFR §411.40](https://www.ecfr.gov/current/title-42/section-411.40) |
| No-fault / med-pay (auto) | **No-fault primary** for the accident-related services | Conditional payment available | [42 CFR §411.50](https://www.ecfr.gov/current/title-42/section-411.50) |
| Liability (incl. self-insurance) | **Liability insurer primary**; Medicare pays conditionally and recovers | Recovery pursued by the BCRC/CRC | [42 CFR §411.50](https://www.ecfr.gov/current/title-42/section-411.50) |
| Federal Black Lung Program | **Black Lung primary** for black-lung-related services only | | [CMS MSP Manual Ch. 1](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/msp105c01.pdf) |
| VA-authorized care | **VA primary** for the VA-authorized episode | Not a COB order question so much as a separate payer of the episode | [CMS MSP Manual Ch. 1](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/msp105c01.pdf) |
| **Medicaid** | **Always last.** Medicaid is payer of last resort; all other liable third parties pay first | This is a federal statutory duty on the State agency, not a plan-design choice | [42 U.S.C. §1396a(a)(25)](https://www.law.cornell.edu/uscode/text/42/1396a); [42 CFR §433.139](https://www.ecfr.gov/current/title-42/section-433.139) |

### 3.3 MSP type / value codes to carry on the claim

`pointer` — these are the MSP types CMS uses to classify the primary; institutional claims carry
them as value codes. Verify against
[CMS MSP Manual Ch. 3](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/msp105c03.pdf)
before writing them onto a claim.

| Code | MSP type |
|---|---|
| 12 | Working Aged |
| 13 | ESRD |
| 14 | No-fault |
| 15 | Workers' Compensation |
| 16 | Public Health Service / other federal agency |
| 41 | Black Lung |
| 42 | Veterans Affairs |
| 43 | Disability (LGHP) |
| 47 | Liability |

---

## 4. Commercial COB order of benefit determination

> **Section basis: `pointer` throughout.** The NAIC Coordination of Benefits Model Regulation
> (**Model #120**) is the source of the ordering rules below. Its text was not retrieved this
> session. Index: [NAIC Model Laws, Regulations and Guidelines](https://content.naic.org/model-laws).

### 4.1 Scope caveat — do not apply this universally

| Plan type | Is the NAIC order binding? | Source (not retrieved) |
|---|---|---|
| Fully-insured commercial plan | Only to the extent the **state has adopted** Model #120 (most have, with variations). The binding instrument is the **state regulation**, not the NAIC model. | [NAIC Model Laws index](https://content.naic.org/model-laws) |
| **Self-funded ERISA plan** | **No.** State insurance law is preempted; the plan's own COB provision in the SPD controls, and it may order benefits differently. | [29 U.S.C. §1144](https://www.law.cornell.edu/uscode/text/29/1144) (preemption + deemer clause) |
| Medicare | **No.** MSP (§3) governs, by statute. | [42 U.S.C. §1395y(b)](https://www.law.cornell.edu/uscode/text/42/1395y) |
| Medicaid | **No.** Payer of last resort, by statute. | [42 U.S.C. §1396a(a)(25)](https://www.law.cornell.edu/uscode/text/42/1396a) |

**Consequence for a denial-resolution system:** never tell a biller "the birthday rule makes X
primary" without first establishing that the plan is fully-insured and the state has adopted the
model. For a self-funded plan the only correct next step is *read the SPD's COB section*.

### 4.2 The ordering rules, in sequence

Apply in order; the first rule that resolves the tie wins.

| # | Rule | Test | Basis |
|---|---|---|---|
| 1 | **Non-dependent / dependent** | The plan covering the person as **employee, member, subscriber, or retiree** is primary over the plan covering that same person as a **dependent**. | `pointer` — [NAIC Model #120](https://content.naic.org/model-laws) |
| 2 | **Child, parents married or living together — the BIRTHDAY RULE** | The plan of the parent whose **birthday falls earlier in the calendar year** is primary. **Month and day only — the birth *year* is irrelevant.** If both parents share the same month and day, the plan that has covered the parent **longer** is primary. | `pointer` — [NAIC Model #120](https://content.naic.org/model-laws) |
| 3 | **Child, parents separated / divorced, court decree names the responsible parent** | The plan of the parent the **decree** makes responsible for health coverage is primary. A decree naming a parent responsible overrides the birthday rule. | `pointer` — [NAIC Model #120](https://content.naic.org/model-laws) |
| 4 | **Child, joint custody with no assignment of responsibility** | Fall back to the **birthday rule**. | `pointer` — [NAIC Model #120](https://content.naic.org/model-laws) |
| 5 | **Child, separated parents, no decree** | Order: custodial parent → **spouse of custodial parent** → non-custodial parent → spouse of non-custodial parent. | `pointer` — [NAIC Model #120](https://content.naic.org/model-laws) |
| 6 | **Active vs. inactive employee** | The plan covering the person as an **active** employee (or as that employee's dependent) is primary over a plan covering them as **laid off or retired**. | `pointer` — [NAIC Model #120](https://content.naic.org/model-laws) |
| 7 | **Continuation coverage** | The plan covering as an active employee/member/dependent is primary; the **COBRA or state continuation** plan is secondary. | `pointer` — [NAIC Model #120](https://content.naic.org/model-laws) |
| 8 | **Longer / shorter length of coverage** | If none of the above resolves it, the plan that has covered the person **longer** is primary. | `pointer` — [NAIC Model #120](https://content.naic.org/model-laws) |

### 4.3 The birthday-rule exception that is routinely missed

`pointer` — [NAIC Model #120](https://content.naic.org/model-laws).

If the **other** plan's contract does **not** contain the birthday rule but instead uses an older
**gender rule** (father's plan primary), and the two plans therefore disagree about the order, the
**other plan's rule determines the order of benefits**. Do not assume the birthday rule wins a
conflict by default.

### 4.4 Birthday rule — hard boundaries

| Assertion | True? | Basis |
|---|---|---|
| Applies to spouses covering each other | **No.** It is a **dependent-child** rule only. Spouses are resolved by rule 1 (non-dependent/dependent). | `pointer` — [NAIC Model #120](https://content.naic.org/model-laws) |
| Uses the older parent's plan | **No.** Uses the **earlier date in the calendar year**. A parent born 1999-02-03 beats one born 1961-11-20. | `pointer` — [NAIC Model #120](https://content.naic.org/model-laws) |
| Overrides a court decree | **No.** Rule 3 precedes rule 4. | `pointer` — [NAIC Model #120](https://content.naic.org/model-laws) |
| Applies when one plan is Medicare | **No.** MSP governs. | `pointer` — [42 U.S.C. §1395y(b)](https://www.law.cornell.edu/uscode/text/42/1395y) |
| Applies to a self-funded ERISA plan | **Not by force of state law.** Only if the plan document adopts it. | `pointer` — [29 U.S.C. §1144](https://www.law.cornell.edu/uscode/text/29/1144) |

---

## 5. Working an "other insurance is primary" denial (CARC 22 / MA04)

### 5.1 First distinguish the two failure modes — they have opposite remedies

| Code | What the payer is actually saying | Is it a coverage denial? | Correct action |
|---|---|---|---|
| **CARC 22** | "Our COB/MSP record shows another payer is primary for this date." | Yes — a COB-order determination | Establish the true primary (§5.2). Bill the primary, then rebill this payer as secondary. |
| **RARC MA04** | "You submitted this to us as **secondary** but did not give us the primary's identity or payment data." | **No** — a claim-completeness defect | Populate the primary payer's adjudication data and **resubmit**. Appealing MA04 consumes the appeal window for nothing. |
| **CARC 109** | "This is not our claim at all — send it to the correct payer/contractor." | No — wrong-payer routing | Identify the correct payer (frequently a Medicare Advantage plan) and bill it. Do not appeal to the payer that disclaimed. |

`corpus` for the MA04 wording and its co-occurrence with OA-22 on a denied secondary claim:
`corpus/v2-chain-corpus-v1.1-md/MOH2-000087/case.md` carries MOA `MA04` alongside three lines of
`OA-22`, on a claim submitted with `payer responsibility P (primary)` while the 271 for the same
member returned `benefit: R (other or additional payer)` naming a Medicare Part B payer and the
message `PLAN IS PRIMARY PAYER FOR THIS MEMBER`.

### 5.2 Sequence for a CARC 22

| Step | Action | Why | Basis |
|---|---|---|---|
| 1 | Re-run a **270** for the **date of service**, not today's date | Coverage and COB order are date-specific; a plan-date query for today answers the wrong question | `corpus` — every corpus 270 carries `plan date (291)` equal to the DOS, e.g. `MOH2-000587` DOS 2025-06-12 / `plan date (291) 2025-06-12` |
| 2 | Read the 271 for `EB*R` (Other or Additional Payer) and the 2120 payer loop naming it | This is where the other carrier's identity is returned | `corpus` — `MOH2-000087` returns `benefit: R (other or additional payer) … plan: NOVITAS SOLUTIONS MEDICARE PART B FFS` plus a second `payer [PR]` party with a payer ID |
| 3 | Decide the order using §3 (Medicare involved) or §4 (two commercial plans) | The 271 tells you *that* another payer exists; it does not always tell you *which is primary* | `corpus` for the data shape; §3/§4 `pointer` for the ordering law |
| 4 | If the denying payer's COB record is **wrong**: the record must be corrected, then the claim **resubmitted** — not appealed | An appeal argues the adjudication; the defect is upstream in the COB record | `pointer` — [CMS MSP Manual Ch. 3](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/msp105c03.pdf) |
| 5 | If correct: bill the primary, wait for its 835, then submit the secondary claim carrying the primary's payment and adjustment data | Otherwise the secondary rejects with MA04 | See §6 |

### 5.3 Who can correct a wrong COB record

| Payer type | Who fixes it | Provider can do it directly? | Basis |
|---|---|---|---|
| **Medicare FFS** | The **Benefits Coordination & Recovery Center (BCRC)**. The MAC cannot change an MSP record; it reads the record CMS holds. | **No.** The provider (or beneficiary) reports; BCRC updates. Resubmit only after the record is updated. | `pointer` — [CMS, Coordination of Benefits & Recovery Overview](https://www.cms.gov/medicare/coordination-benefits-recovery/overview) and [MSP Manual Ch. 5](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/msp105c05.pdf) |
| **Commercial** | The plan's COB unit, usually only on the **member's** attestation — many plans will not accept a provider's assertion that other coverage ended | Usually no; the patient must call | See §11 — no single authority establishes this across carriers |
| **Medicaid** | The State agency's TPL unit; the State has a statutory duty to identify and pursue liable third parties | No | `pointer` — [42 CFR §433.138](https://www.ecfr.gov/current/title-42/section-433.138) |

**Practical consequence:** a CARC 22 caused by a stale COB record is a **patient-action** item, not a
billing-office item, and the resolution clock is the payer's record-update cycle, not the appeal
window. Track it as a hold, and watch the **filing** deadline (which keeps running) — see
[`reference/timely-filing.md`](./timely-filing.md).

### 5.4 CARC 109 vs CARC 22

CARC 109 is not a COB-order dispute. The most common cause is that the beneficiary is enrolled in a
**Medicare Advantage (Part C)** plan, so Original Medicare is not the payer at all. Bill the MA
plan. `pointer` — see [`reference/carc-rarc-remedies.md`](./carc-rarc-remedies.md) row 109, which
was built from retrieved sources.

---

## 6. Submitting the secondary claim so it does not bounce with MA04

`pointer` for the 837 loop references — X12N 005010X222A1 (837P) TR3 was not retrieved this
session. The failure mode is `corpus`-verified (`MOH2-000087`).

| Requirement | 837P location | Effect if omitted |
|---|---|---|
| Identify the destination payer as secondary | Loop 2000B `SBR01 = S` | Claim adjudicated as primary; wrong benefits applied |
| Identify the **other** (primary) payer | Loop 2320 `SBR` + loop 2330B payer name/ID | **MA04** |
| Primary payer's **claim-level** paid amount | Loop 2320 `AMT` | **MA04** |
| Primary payer's **claim-level** adjustments | Loop 2320 `CAS` | **MA04** |
| Primary payer's **line-level** paid amount | Loop 2430 `SVD` | Line-level MA04 / balancing rejection |
| Primary payer's **line-level** adjustments | Loop 2430 `CAS` | Line-level MA04 / balancing rejection |
| Primary payer's adjudication date | Loop 2430 `DTP*573` | Varies by payer |

**Balancing rule:** the secondary claim must balance — billed = paid + all adjustments — at both
claim and line level. An MA04 on a claim that *does* carry `SBR`/`AMT` is usually a balancing
failure, not a missing-segment failure. `pointer` — X12N 005010X222A1 TR3; see §11.

**Do not appeal MA04.** It is a rejection for incomplete data. Correct and resubmit. Confirm the
correct resubmission mechanism (new claim vs. frequency-7 replacement) in
[`reference/resubmission-and-frequency-codes.md`](./resubmission-and-frequency-codes.md).

---

## 7. The 270/271 eligibility transaction and the EB segment

### 7.1 Standing of the transaction

| Fact | Basis |
|---|---|
| The 270/271 Health Care Eligibility Benefit Inquiry and Response is the **HIPAA-mandated standard** for eligibility; the adopted version is ASC X12N **005010X279A1**. | `pointer` — [45 CFR §162.1202](https://www.ecfr.gov/current/title-45/section-162.1202) |
| Corpus transactions use exactly this implementation guide. | `corpus` — envelope in `MOH2-000087/case.md`: `version 00501 … spec 005010X279A1; transaction 270 control 0001 impl 005010X279A1` |
| Medicare FFS eligibility is served by **HETS**; its companion guide documents which EB values Medicare returns. | `pointer` — [CMS HETS 270/271 Companion Guide](https://www.cms.gov/files/document/hetscompanionguide270271.pdf) |

### 7.2 EB01 — Eligibility or Benefit Information code

`EB01` is the first element of the `EB` segment in 271 loop 2110C (subscriber) / 2110D (dependent).
It states **what kind of statement** the rest of the segment makes.

The values below marked `corpus` are confirmed present in this repo's 271s. The remainder are
`pointer` — the X12 code list at [x12.org/codes](https://x12.org/codes) was not retrievable this
session, and the values must be checked against the 005010X279A1 TR3 before being relied on.

| EB01 | Meaning | Basis |
|---|---|---|
| **1** | **Active Coverage** | `corpus` — 518 occurrences, rendered `benefit: 1 (active coverage)` |
| 2 | Active — Full Risk Capitation | `pointer` |
| 3 | Active — Services Capitated | `pointer` |
| 4 | Active — Services Capitated to Primary Care Physician | `pointer` |
| 5 | Active — Pending Investigation | `pointer` |
| **6** | **Inactive** | `corpus` — 45 occurrences, rendered `benefit: 6 (inactive)` |
| 7 | Inactive — Pending Eligibility Update | `pointer` |
| 8 | Inactive — Pending Investigation | `pointer` |
| A | Co-Insurance | `pointer` |
| B | Co-Payment | `pointer` |
| C | Deductible | `pointer` |
| F | Limitations | `pointer` |
| G | Out of Pocket (Stop Loss) | `pointer` |
| I | Non-Covered | `pointer` |
| **R** | **Other or Additional Payer** | `corpus` — 45 occurrences, rendered `benefit: R (other or additional payer)` |
| U | Contact Following Entity for Eligibility or Benefit Information | `pointer` |
| V | Cannot Process | `pointer` |

### 7.3 What **EB\*6** means, precisely

| Question | Answer | Basis |
|---|---|---|
| What does `EB*6` assert? | **Inactive** — the payer states there is **no active coverage for the plan date in the request** for the service type in the request. | `corpus` (code/label pairing) + `pointer` (X12 definition) |
| Does it mean the member never had coverage? | **No.** It is a statement about the queried date only. In this repo every `EB*6` response also returns an `eligibility begin (356)` in the past — coverage existed and then stopped. | `corpus` — `MOH2-000587`: `benefit: 6 (inactive)` with `eligibility begin (356): 2024-01-01`, `eligibility end (357): 2025-05-31` |
| Does it mean the member has no coverage **anywhere**? | **No.** A 271 answers for the payer you asked. Another carrier may be active. `EB*6` from carrier A is not evidence the patient is uninsured. | `corpus` — 271s are addressed to a single `payer [PR]` party |
| Does it distinguish "terminated" from "not yet effective"? | **Not by itself.** Read the dates (§7.4). | `corpus` |
| Is it appealable? | It is not a denial. It is an eligibility answer. It becomes a denial only when a claim is adjudicated (CARC 27). | — |

### 7.4 How a **terminated** coverage appears in a 271

The termination is carried in the **dates**, not in EB01. `EB*6` alone tells you "inactive"; the
`DTP` segments tell you "inactive *because it ended on this date*."

| DTP qualifier | Meaning | Basis |
|---|---|---|
| **291** | **Plan date** — the date the response is answering for (echoes the 270's requested date) | `corpus` — present in every corpus 271 |
| **356** | **Eligibility Begin** — coverage start | `corpus` |
| **357** | **Eligibility End** — **coverage termination date** | `corpus` |
| 346 / 347 | Plan Begin / Plan End | `pointer` — not observed in this corpus |

**The terminated-coverage signature, exactly as it appears in this repo** (`corpus` —
`corpus/v2-chain-corpus-v1.1-md/MOH2-000587/case.md`, service date 2025-06-12):

```
- benefit: 6 (inactive), coverage level IND, service type 30, plan: ATLANTIC SHORE ASSURANCE PPO
- plan date (291): 2025-06-12
- eligibility begin (356): 2024-01-01
- eligibility end (357): 2025-05-31
```

Read it as: coverage ran 2024-01-01 → 2025-05-31; the DOS 2025-06-12 falls **12 days after
termination**; hence `EB*6`. The matching 835 on that same case denied with `PR-27` and MOA `N30`.

**Contrast with an active response** (`corpus` — `MOH2-000087`): `benefit: 1 (active coverage)` with
`eligibility begin (356): 2024-01-01` and **no** `357`. **Absence of a `DTP*357` is the marker of
open-ended active coverage.**

**Decision procedure for a machine reader:**

| 271 pattern | Conclusion |
|---|---|
| `EB*6` + `DTP*357` present + DOS **after** the 357 date | Coverage **terminated** before the DOS. Genuine post-termination service. Go to §8. |
| `EB*6` + `DTP*357` present + DOS **on or before** the 357 date | **Contradiction.** The payer says inactive but its own end date covers the DOS. Do not write off — challenge, and check whether the 270 asked for the wrong plan date. |
| `EB*6` + `DTP*356` **after** the DOS | Coverage had **not started yet** — this is a not-yet-effective problem, not a termination. Different remedy (check enrollment effective date, retroactive enrollment). |
| `EB*6` + no dates at all | Uninformative. Re-query; escalate to the payer. Insufficient basis to bill the patient. |
| `EB*1` for the DOS but claim denied CARC 27 | **The 271 contradicts the 835.** This is the strongest appeal posture available on a CARC 27 — see §8.3. |

**Warning:** payers vary in whether they return `EB*6` at all for a terminated member. Some return
`EB*1` with a past `DTP*357`, some return an `AAA` rejection, some return `EB*6` with no dates.
Never treat the absence of `EB*6` as proof coverage was active. See §11.

### 7.5 `AAA` rejections are not eligibility answers

`pointer` — the `AAA` (Request Validation) segment and its reject-reason list in 005010X279A1 were
not retrieved this session; no `AAA` segments appear in this repo's corpus.

An `AAA` means the **inquiry failed** — bad member ID, name mismatch, DOB mismatch, provider not
recognised, date outside the allowable inquiry window. It is **not** a statement that the patient
lacks coverage, and it must never be used as the evidentiary basis for billing a patient or writing
a balance off. Correct the inquiry and re-query. Reject reasons and their follow-up-action codes
should be read from the TR3 before being acted on — see §11.

---

## 8. Terminated coverage: bill the patient, or write it off

### 8.1 The primary determinant is the group code, not CARC 27

| 835 adjustment | Payer is asserting | Billable to patient? | Basis |
|---|---|---|---|
| **`PR-27`** | Patient responsibility for expenses incurred after coverage terminated | **Yes**, subject to every override in §8.2 | `corpus` (76 occurrences; `MOH2-000587` bills the full $181.22 as `patient responsibility`) + `pointer` — [CMS Claims Processing Manual Ch. 22](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c22.pdf) on group-code liability |
| **`CO-27`** | **Contractual obligation** — provider liability | **No.** Write off. Billing the patient over a `CO` adjustment is a contract breach. | `corpus` (66 occurrences) + `pointer` — [CMS Claims Processing Manual Ch. 22](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c22.pdf) |
| `OA-27` | Liability not asserted | **No** — treat as unresolved, not as patient liability | `pointer` — [CMS Claims Processing Manual Ch. 22](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c22.pdf) |

**Why `CO-27` exists at all:** a payer uses `CO` on a terminated-coverage denial when the
**contract** puts the eligibility-verification risk on the provider — typically where the provider
did not verify eligibility, or verified it too far in advance of the service. In that posture the
balance is a contractual write-off even though the patient in fact had no coverage. This is
payer-contract-specific; see §11.

### 8.2 Overrides — checks that must clear *before* any `PR-27` is billed

Run every row. A single failure blocks patient billing.

| # | Check | If it fails | Basis |
|---|---|---|---|
| 1 | Did the 271 for the **DOS** actually show inactive? | If the 271 showed `EB*1` for the DOS, do **not** bill the patient — appeal (§8.3) | `corpus` |
| 2 | Is the patient retroactively **Medicaid**-eligible for the DOS? Medicaid retroactive eligibility can reach back up to **3 months** before the application month. | Bill Medicaid. If the patient already paid, **refund** them. | `pointer` — [42 U.S.C. §1396a(a)(34)](https://www.law.cornell.edu/uscode/text/42/1396a); [42 CFR §435.915](https://www.ecfr.gov/current/title-42/section-435.915) |
| 3 | Is the provider enrolled in Medicaid and is this a Medicaid-covered service? Medicaid participation requires accepting the Medicaid payment **as payment in full**. | Do not bill the beneficiary. | `pointer` — [42 CFR §447.15](https://www.ecfr.gov/current/title-42/section-447.15) |
| 4 | Is the patient a **QMB**? QMBs may not be billed for Medicare cost sharing. | Do not bill. | `pointer` — [42 U.S.C. §1396a(n)(3)(B)](https://www.law.cornell.edu/uscode/text/42/1396a); see [`reference/carc-rarc-remedies.md`](./carc-rarc-remedies.md) §3 |
| 5 | Is the DOS inside an ACA marketplace **grace period** where the issuer pended rather than terminated? | The termination may not be final — see §9.2 | `pointer` — [45 CFR §156.270](https://www.ecfr.gov/current/title-45/section-156.270) |
| 6 | Is this a **rescission** rather than a termination? Rescissions are prohibited absent fraud or intentional misrepresentation of material fact. | Challenge the termination itself — see §9.1 | `pointer` — [45 CFR §147.128](https://www.ecfr.gov/current/title-45/section-147.128) |
| 7 | Does the **participation agreement** contain a hold-harmless or eligibility-verification clause? Many bar balance billing where the provider held a payer-issued eligibility confirmation. | Write off per contract | See §11 — payer-specific |
| 8 | Is another payer actually primary and active for the DOS? | Bill that payer instead of the patient | §5 |
| 9 | Did the payer **already pay** and then reverse the claim retroactively? | Different rules — §9 | `pointer` |

### 8.3 The strongest appeal posture on a CARC 27

If a **271 for the date of service** returned `EB*1` (Active Coverage) and the claim was
subsequently denied CARC 27, the payer's own eligibility response contradicts its own adjudication.
Appeal citing the 271 by its exchange reference and date.

`corpus` — the corpus preserves an exchange reference on every 271 (e.g. `MOH2-000587`:
`Eligibility exchange reference ELG34168586, dated 2025-07-18 0800`), which is the identifier to
quote in the appeal.

**Note the trap in that specific case:** the 271 is dated **2025-07-18** while the DOS is
**2025-06-12** and the 835 production date is **2025-07-16**. The eligibility check was run *after*
the claim was already denied. A post-hoc 271 is much weaker evidence than a contemporaneous one.
When arguing detrimental reliance, the 271's **transaction date** matters as much as its content.
`corpus`.

### 8.4 Write-off vs patient-transfer decision table

| Situation | Disposition |
|---|---|
| `CO-27` | Write off |
| `OA-27` | Hold — liability unresolved; work the underlying cause |
| `PR-27`, 271 confirms inactive for DOS, all §8.2 checks clear | Transfer to patient responsibility |
| `PR-27`, 271 showed active for DOS | Appeal (§8.3); do **not** transfer |
| `PR-27`, patient retroactively Medicaid-eligible | Bill Medicaid; refund patient if already collected |
| `PR-27`, patient is QMB | Do not bill |
| `PR-27`, but contract has an eligibility hold-harmless clause and eligibility was verified | Write off per contract |
| `PR-27` following a retroactive rescission | Challenge the rescission first (§9.1) |
| `PR-27`, coverage genuinely ended, no other coverage, no override | Patient is self-pay for the DOS |

---

## 9. Retroactive termination

> **Section basis: `pointer` throughout.**

### 9.1 Rescission vs prospective termination — not the same thing

| Concept | Definition | Constraint | Source (not retrieved) |
|---|---|---|---|
| **Rescission** | A cancellation or discontinuance of coverage that has **retroactive effect** | **Prohibited** unless the individual performed an act of **fraud** or made an **intentional misrepresentation of material fact**; requires **30 days advance written notice** before the rescission | [45 CFR §147.128](https://www.ecfr.gov/current/title-45/section-147.128); [PHSA §2712](https://www.law.cornell.edu/uscode/text/42/300gg-12) |
| **Termination for non-payment of premium** | Coverage ends because premiums were not paid | **Carved out** of the rescission definition — a retroactive termination to the paid-through date is not treated as a prohibited rescission | [45 CFR §147.128](https://www.ecfr.gov/current/title-45/section-147.128) |

**Practical read:** the biller's first question on a retroactive termination is *which of these two
it is*. If the payer is rescinding for an alleged application misstatement, §147.128 constrains it
and the termination is contestable. If the member simply stopped paying premiums, it generally is
not — and the exposure shifts to §9.2.

### 9.2 The ACA marketplace 90-day grace period — the most common cause of a retroactive term

| Element | Rule | Source (not retrieved) |
|---|---|---|
| Who gets it | Marketplace QHP enrollees **receiving advance premium tax credits (APTC)** who have paid at least one full month's premium in the benefit year | [45 CFR §156.270(d)](https://www.ecfr.gov/current/title-45/section-156.270) |
| Length | **3 consecutive months** | [45 CFR §156.270(d)](https://www.ecfr.gov/current/title-45/section-156.270) |
| Month 1 | Issuer **must pay** claims | [45 CFR §156.270(d)](https://www.ecfr.gov/current/title-45/section-156.270) |
| Months 2–3 | Issuer **may pend** claims | [45 CFR §156.270(d)](https://www.ecfr.gov/current/title-45/section-156.270) |
| Provider notice | The issuer must **notify providers** of the possibility that claims may be denied | [45 CFR §156.270(d)](https://www.ecfr.gov/current/title-45/section-156.270) |
| If premiums are never paid | Coverage terminates **retroactive to the end of month 1**; claims paid for months 2–3 can be reversed and recouped | [45 CFR §156.270(d)](https://www.ecfr.gov/current/title-45/section-156.270); [45 CFR §155.430](https://www.ecfr.gov/current/title-45/section-155.430) |
| Non-APTC enrollees | **Do not** get the federal 3-month grace period. State-law grace periods (commonly ~31 days) apply instead. | [45 CFR §156.270(d)](https://www.ecfr.gov/current/title-45/section-156.270) |

**Why this matters for the denial system:** a claim that was **paid** and is later **reversed** with
a terminated-coverage adjustment, on a marketplace plan, at 60–90 days after the DOS, is almost
certainly a grace-period expiry. The distinctive markers are a reversal on the 835 (group code `CR`
or a negative-adjustment claim) and a termination date that lands on a **month end** roughly two
months before the reversal.

### 9.3 Medicare and Medicare Advantage retroactive disenrollment

| Situation | Consequence | Source (not retrieved) |
|---|---|---|
| Beneficiary is **retroactively disenrolled** from an MA plan or PACE organization | The MA plan's payments are reversed; the claim belongs to **Original Medicare** for those dates | [42 CFR §424.44(b)](https://www.ecfr.gov/current/title-42/section-424.44) |
| Timely filing | This is one of the enumerated **exceptions** to the Medicare 1-year filing limit | [42 CFR §424.44(b)](https://www.ecfr.gov/current/title-42/section-424.44); [CMS Claims Processing Manual Ch. 1 §70.7](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c01.pdf) |

### 9.4 Medicaid retroactive termination / redetermination loss

Medicaid coverage lost at redetermination is normally **prospective**. Where a State applies a
retroactive termination, the §447.15 payment-in-full bar applies only to periods when the person
was in fact a beneficiary — but state rules on billing for retroactively-terminated periods vary and
are not federally uniform. `pointer` — [42 CFR §447.15](https://www.ecfr.gov/current/title-42/section-447.15). See §11.

---

## 10. Retroactive reinstatement

> **Section basis: `pointer` throughout.**

| Question | Rule | Source (not retrieved) |
|---|---|---|
| What triggers it | Premium paid within the grace period; successful appeal of a termination; correction of an enrollment error; Medicaid or marketplace eligibility appeal decided for the enrollee; retroactive Medicare entitlement determination | [45 CFR §155.430](https://www.ecfr.gov/current/title-45/section-155.430) |
| What the payer must do | Reprocess claims denied during the retroactively-covered period | [45 CFR §156.270](https://www.ecfr.gov/current/title-45/section-156.270) |
| What the **provider** must do | If the balance was transferred to the patient and collected, **refund the patient** and bill the reinstated payer. Continuing to collect from a patient whose coverage was restored for that date creates a refund liability. | See §11 — no single federal authority; driven by contract and state law |
| Does the filing clock restart | **Medicare: yes, by exception.** Retroactive Medicare entitlement covering the DOS is an enumerated exception to the 1-year limit, with an extension keyed to the date of the entitlement notification. | [42 CFR §424.44(b)](https://www.ecfr.gov/current/title-42/section-424.44); [CMS Claims Processing Manual Ch. 1 §70.7](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c01.pdf) |
| | **Commercial: not automatically.** Depends on contract and state prompt-pay law. Do not assume an extension. | See [`reference/timely-filing.md`](./timely-filing.md) and §11 |

**Enumerated Medicare exceptions to the 1-year filing limit relevant to this file** — `pointer`,
[42 CFR §424.44(b)](https://www.ecfr.gov/current/title-42/section-424.44):

| Exception | Trigger |
|---|---|
| Administrative error | Error or misrepresentation by CMS, a contractor, or an agent thereof |
| **Retroactive Medicare entitlement** | Beneficiary notified of Medicare entitlement retroactive to or before the DOS |
| **Retroactive entitlement + State Medicaid recovery** | Retroactive entitlement combined with a State Medicaid agency recovering payment from the provider 6+ months after the DOS |
| **Retroactive disenrollment from MA / PACE** | Beneficiary retroactively disenrolled from an MA plan or PACE provider organization |

Verify the exact extension window (an additional period running from the month of notification) at
[CMS Claims Processing Manual Ch. 1 §70.7](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c01.pdf)
before quoting a date. See §11.

---

## 11. Open questions

Nothing in this section is asserted above. These are gaps, not rules.

**Blocking — caused by this session's retrieval failure**

- **Every `pointer` row in this file is unverified.** No external source was read. The whole of §§3,
  4, 6, 9, 10 and most of §7 rests on reconstructed knowledge of the cited authorities. A
  verification pass against the listed URLs is required before this file is used as runtime
  authority.
- **Exact statutory wording and current thresholds for 42 U.S.C. §1395y(b)(1)** could not be
  confirmed. The 20 / 100 employee thresholds and the 30-month ESRD coordination period are stated
  from knowledge, not from retrieved text.
- **42 CFR Part 411 subpart structure** — section numbers are cited (411.162, 411.170, 411.172,
  411.200) but the subpart organisation was not confirmed; eCFR section-level URLs are used to
  avoid asserting an unverified subpart path.
- **NAIC Model #120's exact ordering text**, including the precise formulation of the
  gender-rule-conflict exception in §4.3 and the Medicare-interaction reversal of the
  non-dependent/dependent rule, was not retrieved. The direct model-law PDF URL is not known; only
  the [NAIC model-laws index](https://content.naic.org/model-laws) is cited.
- **The complete X12 EB01 code list** could not be retrieved. Only values 1, 6 and R are
  corpus-confirmed. Values 2, 3, 4, 5, 7, 8, A, B, C, F, G, I, U, V are stated from knowledge and
  must be checked against ASC X12N 005010X279A1.
- **The `AAA` reject-reason and follow-up-action code lists** were not retrieved and no `AAA`
  segment appears in this repo's corpus. §7.5 therefore states only the general principle and
  enumerates nothing.
- **837P loop numbers in §6** (2000B, 2320, 2330B, 2430) are from knowledge of 005010X222A1; the
  TR3 was not retrieved.
- **The exact length of the Medicare filing extension** under the 42 CFR §424.44(b) exceptions is
  not stated in §10 because it could not be verified.
- **MSP value/type codes in §3.3** are stated from knowledge and were not verified against the MSP
  Manual.

**Substantive — would remain open even with retrieval**

- **Does the 005010X279A1 TR3 *require* a `DTP*357` when `EB01 = 6`?** The corpus shows payers
  supplying it, but whether it is a required, situational, or optional element is unconfirmed. This
  matters: if it is merely situational, an `EB*6` with no dates is TR3-conformant and cannot be
  treated as a payer defect.
- **Does CAQH CORE Phase II Rule 260 impose a data-content requirement on inactive responses** —
  e.g. must an inactive 271 return the termination date? Not established. [CAQH CORE](https://www.caqh.org/core/eligibility-benefits).
- **Whether a self-funded ERISA plan may lawfully order benefits contrary to the state-adopted
  birthday rule in every state.** ERISA preemption is asserted at §4.1 on the strength of 29 U.S.C.
  §1144, but the interaction with state COB regulations applied to the plan's *insurer* (vs. the
  plan itself) was not researched.
- **State-level caps on how far back a commercial payer may retroactively terminate coverage.**
  Several states impose limits (commonly expressed as a maximum retroactive-recoupment lookback).
  No survey was performed; nothing is asserted.
- **State-level rules governing whether a balance may be transferred to a patient after a
  retroactive termination**, and whether the provider must first exhaust an appeal. Varies; not
  established.
- **Whether commercial payers will accept a provider-submitted COB correction**, or require the
  member to initiate. §5.3 asserts only the Medicare position (BCRC) with confidence; the
  commercial row is marked as unestablished.
- **Medicaid MCO retroactive disenrollment** — whether the claim reverts to Medicaid FFS and
  whether a filing-limit exception exists. State-specific; not researched.
- **Whether `OA-22` and `CO-22` carry different operational meaning.** The corpus contains both
  (103 vs 48) but no source was available to explain the payer's choice between them.
  [`reference/carc-rarc-remedies.md`](./carc-rarc-remedies.md) §Open questions already records that
  no group-code usage restriction could be confirmed for CARC 22.
- **Whether `CO-27` reflects a uniform industry convention or is purely contract-driven.** §8.1
  offers an explanation marked as payer-contract-specific; it is not sourced.
- **No Surprises Act interaction.** Whether NSA balance-billing protections ([45 CFR Part 149](https://www.ecfr.gov/current/title-45/part-149))
  reach a patient whose coverage was retroactively terminated — i.e. whether the patient counts as
  uninsured (Good Faith Estimate regime) or as a plan participant (surprise-billing regime) for the
  DOS — was not researched and could change the §8.4 disposition.

---

## 12. Related files in this repo

| File | Covers |
|---|---|
| [`reference/carc-rarc-remedies.md`](./carc-rarc-remedies.md) | Group-code liability semantics, CARC 22 / 27 / 109 / MA04 / N30 base entries, QMB and payment-in-full overrides |
| [`reference/timely-filing.md`](./timely-filing.md) | Filing clocks, including 42 CFR §424.44 and the appeal-vs-filing distinction |
| [`reference/resubmission-and-frequency-codes.md`](./resubmission-and-frequency-codes.md) | Whether to resubmit or replace after an MA04 or a COB correction |
| [`reference/appeal-levels.md`](./appeal-levels.md) | Appeal ladders — relevant to §8.3 |
