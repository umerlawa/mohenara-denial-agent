# Contradictions resolved — C1, C2, C3, C4

> Written **2026-08-12**. Resolves four of the six conflicts listed in `README.md` §4.
> C5 and C6 are **not** addressed here and remain open.
>
> **Retrieval conditions.** Direct fetching of `cms.gov`, `x12.org`, `ecfr.gov` and the MAC hosts is
> still refused by this environment's egress proxy (`EGRESS_BLOCKED` on every attempt, including
> `clm104c22.pdf`, `x12.org/resources/...` and `med.noridianmedicare.com`). Every quotation below was
> obtained by **domain-restricted search over those same primary domains**: the cited URL is the
> authority, the wording is a retrieved excerpt, not a verbatim full-text read. Where that limit
> changes what may be asserted, it is stated in the row, not smoothed over.
>
> **Precedence.** Where this file and an older reference file disagree, this file governs for C1, C2
> and C4. For **C3, the governing file is `exact-duplicate-n111.md`** — this file records its
> holding and the downstream files that still need editing.

---

## Summary

| # | Question | Resolution | Settled by | File(s) to correct |
|---|---|---|---|---|
| **C1** | Does Medicare permit group code `CR`? | **Yes.** Medicare FFS = **`CO`, `CR`, `OA`, `PR`**. Only `PI` is barred. `carc-rarc-remedies.md` is right. | CMS Pub. 100-04 Ch. 22 (Group Codes), restated in CMS Transmittal R470CP | `denial-lifecycle.md` §3.1 |
| **C2** | What does a `PI` adjustment oblige? | **Two hard duties** (never bill the patient; never auto-write-off) **and one default** (challenge/appeal unless a contract term is found). The mandatory half is sourced; "always appeal" is a triage default, not a payer rule. | CMS Pub. 100-04 Ch. 22 + X12 835 TR3 group-code definition | `denial-lifecycle.md` §3.1 (`PI … n/a` must be replaced); `carc-rarc-remedies.md` §7 and `runtime/00-group-codes.md` (soften "Appeal" to the conditional form) |
| **C3** | Exact-duplicate disposition | **One rule, three branches**, keyed to *true duplicate / false duplicate / wrong finding*. Already resolved in full by `exact-duplicate-n111.md`. | CMS Pub. 100-04 Ch. 1 §120 + Transmittal R2678CP | `denial-lifecycle.md` §7; `carc-rarc-remedies.md` §5; `resubmission-and-frequency-codes.md` §5; `README.md` §4 C3; `runtime/04-exact-duplicate.md` |
| **C4** | Does the Medicare timely-filing non-appealability rule reach Part B? | **Yes.** 42 CFR 405.926 sits in Part 405 **Subpart I — "…Under Original Medicare (Part A and Part B)."** `timely-filing.md` §9.1 is right. | 42 CFR 405.926(n), by the scope of its own subpart; CMS Transmittal R2140CP | `denial-lifecycle.md` Open questions (the "do not generalize to Part B" caveat) |

None of the four required a manufactured answer. Where a sub-question is still open it is stated as
open, under **What is still not settled** in each section.

---

## C1 — Medicare permitted group codes: `CR` is permitted

### Resolution

**Medicare FFS contractors may use `CO`, `CR`, `OA` and `PR`. The only group code CMS bars is `PI`.**
`carc-rarc-remedies.md` §2a is correct; `denial-lifecycle.md` §3.1 is wrong by omission.

The two files were never actually disputing `CR` on the evidence — they were reporting the same
CMS prohibition from different directions. Ch. 22 states the restriction as a **prohibition on `PI`**,
not as a four-item whitelist:

> "Although X12 permits use of another group code, **PI** (payer initiated), with an adjustment
> reason code, **CMS has never permitted Medicare contractors to use this group code as it fails to
> identify financial liability for the unpaid amount.**"
> — [CMS Transmittal R470CP](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/downloads/R470CP.pdf);
> [CMS, Medicare Claims Processing Manual Ch. 22](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c22.pdf)

X12 defines exactly five group codes (`CO`, `CR`, `OA`, `PI`, `PR`). Subtract the one CMS prohibits
and the permitted Medicare set is `CO`, `CR`, `OA`, `PR` — which is how CMS and the MACs state it
directly: *"Medicare contractors are limited to use of the `CO`, `CR`, `OA`, and `PR` group codes"*
([Noridian, Claim Adjustment Group Codes](https://med.noridianmedicare.com/web/jddme/topics/ra/claim-adjustment-group-codes),
a MAC republication of Ch. 22).

Ch. 22 also affirmatively contemplates `CR` on a Medicare remittance in the sentence that defines
what a group code is for:

> "A group code must always be used in conjunction with a claim adjustment reason code to show
> liability for amounts not covered by Medicare for a claim or service **or to identify a correction
> or reversal of a prior decision**."
> — [CMS Pub. 100-04 Ch. 22](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c22.pdf)

`denial-lifecycle.md` §3.1 has no source for excluding `CR`. It cites the same Ch. 22 URL, and its
own §3.2 documents `CLP02 = 22` (reversal of previous payment) on Medicare remits — the exact
transaction `CR` exists to annotate.

**Primary source that settles it:** [CMS, *Medicare Claims Processing Manual* Pub. 100-04 Ch. 22 —
Remittance Advice](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c22.pdf),
Group Codes; issued via [CMS Transmittal R470CP](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/downloads/R470CP.pdf).

### What `CR` actually means for a resolver — and why it never decides liability

`CR` is **bookkeeping, not liability**. It carries no financial responsibility of its own and never
stands alone: *"`CR` explains the reason for the correction; `PR`, `CO` and/or `OA` must always be
used in tandem with `CR` to show the revised information"*
([Ch. 22](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c22.pdf)).
So the liability gate in `carc-rarc-remedies.md` §2 is unaffected by this correction: on a
reversal/correction remit, read the `CO`/`PR`/`OA` that accompanies the `CR`, never the `CR` itself.

### File to correct

**`denial-lifecycle.md` §3.1.** Two edits:

1. Add a `CR` row to the group-code table — *"Correction and Reversal. Bookkeeping only; carries no
   liability. Never appears alone: read the `CO`/`PR`/`OA` used in tandem with it."*
2. Change the Medicare-only restriction sentence from *"Medicare contractors may use only **CO, OA
   and PR**"* to *"Medicare contractors may use only **CO, CR, OA and PR**; CMS has never permitted
   `PI`."*

### Impact, and what does not change

Low, as `README.md` §4 C1 said — but not zero. Measured over the corpus (563 cases,
`grep` over `corpus/v2-chain-corpus-v1.1/edi/`): **`CAS*CO` 1473, `CAS*PR` 629, `CAS*OA` 249,
`CAS*CR` 0, `CAS*PI` 0.** No corpus case turns on this. The failure mode the correction prevents is
a resolver that treats `CR` as an impossible value on a Medicare remit and mis-handles a reversal.

The load-bearing half of the rule is untouched and both files already agree on it:
**`PI` on a remit means the payer is not Medicare FFS** (or the remit is off-code). `runtime/00-group-codes.md`
already states the corrected set and needs no edit.

### What is still not settled

- **No verbatim read.** `cms.gov` returned `EGRESS_BLOCKED`; the Ch. 22 and R470CP wording above is a
  retrieved excerpt corroborated across CMS transmittal text and two MAC republications. Re-read
  Ch. 22 from an unblocked network before quoting a group-code list to a payer.
- **Whether Medicare actually emits `CAS*CR` in practice, and in which segment**, was not established.
  Permission is not usage. Zero occurrences in this corpus; do not assert a `CR` pattern to a client.

---

## C2 — What a `PI` adjustment obliges

### Resolution

A `PI` adjustment carries **two obligations that are sourced and mandatory**, and **one default that
is triage judgment, not a payer rule**. Stating all three as one flat "appeal" over-claims; stating
none of them (`n/a`) under-acts, which is exactly the failure `README.md` §4 C2 predicted.

| # | Rule | Status | Basis |
|---|---|---|---|
| 1 | **Never bill the patient.** `PI` does not assign patient liability. On a Medicare remit the point is absolute — a beneficiary may be billed *"only when Group Code `PR` is used with an adjustment"* — and off Medicare, `PI`'s own definition is that the payer believes the amount is **not** the patient's responsibility. | **Mandatory, sourced** | [CMS Pub. 100-04 Ch. 22](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c22.pdf); X12 835 TR3 group-code definition, as republished in payer companion guides ([MagnaCare 835](https://www.magnacare.com/wp-content/uploads/2024/03/MagnacareCompanionGuide_835_5010A1.pdf); [BCBSNC 835 Ch. 4](https://www.bluecrossnc.com/content/dam/bcbsnc/pdf/providers/network-participation/hipaa/835-5010-v3-0.pdf)) |
| 2 | **Never auto-write-off.** A write-off is the disposition for `CO` — *"a contractual agreement between the payer and payee, or a regulatory requirement, resulted in an adjustment."* `PI` asserts the **opposite**: the reduction has **no supporting contract** behind it. Absorbing a `PI` amount concedes a deduction the payer itself has not claimed a contractual basis for. | **Mandatory, sourced** | Ch. 22 (`CO` definition); X12 835 TR3 (`PI` definition), per the RFI formulation *"the dollars were not assigned due to no contract between the payer and provider (`PI`)"* |
| 3 | **Default to challenging it** — appeal, or a written contract-based dispute under the payer's provider-dispute process. | **Default, not a rule** | Authored triage default. No primary source located obliges an appeal on every `PI`. |

**The operative test, and it is a fork, not a reflex:** `PI` is frequently a **mis-selection for `CO`**.
Before appealing, determine whether a contract term or regulatory requirement actually covers the
reduction.

- **A term covers it** → the payer coded the adjustment wrong; the correct code was `CO` and the
  economics of a write-off may genuinely be right. Request a corrected 835 rather than appealing a
  reduction you are contractually bound to.
- **No term covers it** → the payer has said so on its own remit. Dispute it. Do not write it off.
- **Either way** → the balance does not go to the patient (rule 1). That is the branch-independent
  part, and it is the one worth hard-coding.

This is the same structural argument `co27-terminated-coverage-liability.md` makes for `CO-27`:
`CO` and `PI` are assertions about whether a **contract** reaches the amount, and the participation
agreement — not the group code — is the instrument that answers it.

**Primary source that settles it:**
[CMS, *Medicare Claims Processing Manual* Pub. 100-04 Ch. 22](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c22.pdf)
for the `PR`-only patient-billing rule and the `CO` definition; the ASC X12N 835 (005010X221A1) TR3
group-code definition for `PI` itself, reached through payer companion-guide republications.

### Files to correct

1. **`denial-lifecycle.md` §3.1** — replace the `PI` row's *"n/a"* in the "Can the patient be billed?"
   column with **"No — and never write it off automatically; see the `PI` rule."** `n/a` is the
   defect: it reads as "no guidance" on the one code whose whole meaning is that the payer has no
   contractual basis.
2. **`carc-rarc-remedies.md` §7** — the row *"Any adjustment with **PI** | Appeal | [never]
   Auto-write-off"* keeps its "never" (that half is sourced) but should carry the contract test:
   *"Verify whether a contract/regulatory term reaches the amount; if none does, appeal. Never
   auto-write-off; never bill the patient."*
3. **`runtime/00-group-codes.md`** — its ladder row *"Any **PI** adjustment | `appeal`"* mirrors
   `carc-rarc-remedies.md` §7 and inherits the same softening: `appeal` stays the default
   `next_action`, but the row should carry *"never `bill_patient`, never `do_not_resubmit`"* as the
   branch-independent part. Its group-code table (*"Medicare FFS sends CO, CR, OA, PR only"*) is
   already correct under C1 and needs no edit.
4. **Citation attribution (minor).** `carc-rarc-remedies.md` §2 attributes the *"no contract between
   the payer and provider (`PI`)"* sentence to [X12 RFI #2052](https://x12.org/resources/requests-for-interpretation/rfi-2052-casco45-being-used-denial).
   Search returns that sentence against [X12 RFI #2535, *835 Secondary Payment (OA23) Clarifications*](https://x12.org/resources/requests-for-interpretation/rfi-2535-835-secondary-payment-oa23-clarifications).
   Neither RFI page could be opened (`x12.org` egress-blocked), so treat the attribution as
   **unverified**, not as established error — re-check both RFIs before citing either to a payer.

### Impact

**Zero corpus cases.** `CAS*PI` occurrences across all 563 cases: **0** — expected, since the corpus
is 69% Medicare Part B and Medicare may not send `PI` (C1). This rule is currently unreachable in
this corpus and matters only for the 30% commercial population and for future payers.

### What is still not settled

- **No primary source obliges an appeal on a `PI` adjustment.** The mandatory duties are the two
  negatives. "Appeal" is the sensible default and is defensible from `PI`'s definition, but it is
  authored triage — do not present it to a payer or a client as a cited rule.
- **Whether CAQH CORE 360 permits `PI` in any of its four denial business scenarios** was not
  retrieved (the combination tables are a separate CAQH companion document; the same gap is recorded
  in `carc-rarc-remedies.md` Open questions and in `co27-terminated-coverage-liability.md`). If a
  CORE scenario permits `PI`, the "no contract behind it" reading weakens for that scenario.
- **Medicaid.** State Medicaid programs are observed sending `PI`; patient liability there is
  separately governed by [42 CFR 447.15](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-C/part-447/subpart-A/section-447.15).
  Rule 1 holds; rule 3 was not researched for Medicaid.

---

## C3 — Exact-duplicate disposition: one rule, three branches

### Resolution

**Already resolved in this repository.** `reference/exact-duplicate-n111.md` (retrieved 2026-08-12)
supersedes all three conflicting dispositions and states the rule with a condition on each branch.
That file governs; this section records the holding and the edits still outstanding elsewhere.

The three "conflicting" answers were never three answers to one question — they were **three
branches of one decision**, each stated without its condition. The condition is *what is actually
true about the service*, which the remit alone does not tell you: check the original claim's status
in the MAC portal/IVR **before** doing anything.

| Condition | Disposition | Never |
|---|---|---|
| **True duplicate** — the same service, already adjudicated on a prior claim | **No further action** (`do_not_resubmit`). The prior claim's determination governs the money; post that outcome and close. If the original is still pending, **hold**. If the original was denied, work **that** claim's denial on **its** remit and **its** 120-day clock. | Do not resubmit in any form. Do not bill the patient. |
| **False duplicate** — a genuinely repeated or distinct service that matched as a duplicate because no distinguishing modifier was on the line | Add the modifier that describes what happened (**76 / 77 / 91 / 59-X / RT-LT**) and put the **affected line(s) only** back in front of the payer: on **Part B, as a new original claim (`CLM05-3 = 1`)**, or by **clerical-error reopening**. Watch the 1-year-from-DOS claim clock ([42 CFR 424.44](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-424/subpart-C/section-424.44)) — it can close this door entirely. | Do not resend the line unchanged. Do not send frequency `7` to Part B. Do not resend the whole claim. |
| **Wrong finding** — no prior adjudicated claim exists, or the match is against a different beneficiary / DOS / provider | Contest it: **reopening first** (Novitas: Novitasphere, IVR claim corrections, or form FP152 — *not* "telephone reopening", which is the Noridian channel name); **redetermination** as the fallback, within 120 days, with documentation that each service billed was not a duplicate. | Do not run an appeal and a resubmission on the same DOS/CPT at once — that is a duplicate by construction. |

Group code `OA` is on this denial in every corpus case, so **the balance is never patient
responsibility in any branch**.

**On the `N111` appeal-rights carve-out** — the sharpest part of the conflict — the flat
`denial-lifecycle.md` §7 statement is **right on the merits and over-broad as written**:

- **Closed:** the merits of the service under *this* claim number (decided on the prior claim), and
  the exact-duplicate edit itself — it is hard-coded and *"Medicare contractors cannot override or
  bypass exact duplicate edits."*
- **Open (the carve-out):** *whether this was a duplicate at all.* CMS: *"The denial of a claim as a
  duplicate of another claim **may be appealed** when the denial is based on criteria other than
  those specified above for exact duplication"* — i.e. **suspect**-duplicate determinations.

`N111` is therefore not a contradiction of CMS policy; it is CMS policy written onto the remit.

**Primary source that settles it:**
[CMS, Pub. 100-04 Ch. 1 §120, *Detection of Duplicate Claims*](https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/Downloads/clm104c01.pdf)
and [CMS Transmittal R2678CP, *Clarification of Detection of Duplicate Claims Section*](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/Downloads/R2678CP.pdf)
— §120.2 (exact duplicates: hard-coded, no appeal rights) and §120.3 (suspect duplicates: appealable).
Part B unavailability of frequency `7`: [CMS 837P Companion Guide](https://www.cms.gov/Medicare/Billing/ElectronicBillingEDITrans/downloads/5010a1837bcg.pdf).
Full citation set in `exact-duplicate-n111.md` §§1–8.

### Files to correct

| File | What is wrong | Edit |
|---|---|---|
| `denial-lifecycle.md` §7 | *"…rejected and **do not have appeal rights**"* stated flat; and CARC 18 paired with `N522` | Adopt the closed/open split above (`exact-duplicate-n111.md` §3). `N522` is the **DME MAC** pairing — the Part B corpus pairing is `N111`; do not import DME guidance to a Part B professional claim. |
| `carc-rarc-remedies.md` §5 (CARC 18) | *"add the appropriate modifier/condition code and resubmit corrected line(s) only"* | Correct, but **only for the false-duplicate branch**, and on Part B the resubmission must be a new `1`. Not a disposition for a true duplicate. Add the condition. |
| `resubmission-and-frequency-codes.md` §5 | corollary (b): *"it needs correction → `7` with `REF*F8`"* | **Commercial/Medicaid only.** That file's own §6 says Part B rejects any `CLM05-3` other than `1`. Add the payer-type qualifier in §5 so §5 cannot be read without §6. Its (c) — *"contact Telephone Reopenings"* — is Noridian's channel name and does not describe Novitas, this corpus's Part B payer. |
| `README.md` §4 C3 | *"Three files give three answers and none resolves Medicare Part B"* | Now resolved. Replace with a pointer to `exact-duplicate-n111.md`, and update the §2 routing table row for `exact_duplicate` from **"Disposition unsafe"** to that file. |
| `runtime/04-exact-duplicate.md` | Stale: *"No reference file establishes `N111` as a payer rule"*; *"use **Telephone Reopenings**"*; and the closing *"Uncertain: `N111` … unresolved at source (README §4 C3)"* | `N111` is now sourced (X12/CMS, quoted by Noridian JE). Replace the Uncertain block with the exact-vs-suspect distinction, and the reopening channel with the payer-specific form. Also drop the un-reconfirmed **OIG-referral** clause (see below). |

### Impact

**13 corpus cases** (`OA-18` + `N111`), all Novitas Medicare Part B. This was the one family the
README marked *"Disposition unsafe"*; it is now safe for the **true-duplicate** branch, which is the
disposition the corpus signature most often implies.

### What is still not settled

Carried forward verbatim from `exact-duplicate-n111.md` §10 — these are the reasons this resolution
does not extend further than it does:

- **`N111` does not tell you whether the edit was exact or suspect**, and appeal rights differ between
  the two. No source was located reserving `N111` to exact duplicates. **Where that distinction
  decides the case, the remit alone cannot settle it** — treat as unresolved, do not assume "exact."
- **Suspect-duplicate criteria are unpublished by design** (CMS says so explicitly). They cannot be
  reproduced from the artifacts.
- **Rejection vs denial characterization.** Ch. 1 §120.2 says exact duplicates are "auto-denied **or**
  rejected", while the corpus shows an adjudicated 835 carrying a payer claim control number. Whether
  a Part B `OA-18` line is formally a non-appealable rejection or an initial determination with a
  narrowed appeal right was not settled. Practical effect is the same (reopening first); it decides
  whether a redetermination is *dismissed* rather than *decided*.
- **The Novitas channel for a duplicate-denied line is inferred, not published** — specifically whether
  adding `76`/`77`/`91` is accepted as a minor omission or refused as "adding a service not previously
  billed." Confirm with the payer before asserting the channel to a client.
- **The OIG-referral escalation clause** in `denial-lifecycle.md` §7 was **not re-confirmed** in the
  manual. The program-integrity exposure is independently real ([CMS RAC topic 0091](https://www.cms.gov/research-statistics-data-and-systems/monitoring-programs/medicare-ffs-compliance-programs/recovery-audit-program/approved-rac-topics-items/0091-exact-duplicate-claims)); the OIG wording should not be quoted until read.

---

## C4 — The Medicare timely-filing rule reaches Part B

### Resolution

**Yes. `timely-filing.md` §9.1 is correct as stated, and it applies to Medicare Part B.**
`denial-lifecycle.md`'s warning — *"Do not generalize this to Part B, Medicaid or commercial payers"* —
is right about Medicaid and commercial and **wrong about Part B**.

The conflict is settled by the **scope of the regulation itself**, not by weighing two assertions.
42 CFR 405.926 lives in:

> **42 CFR Part 405, Subpart I — "Determinations, Redeterminations, Reconsiderations, and Appeals
> Under Original Medicare (Part A and Part B)"**
> — [eCFR, 42 CFR Part 405 Subpart I](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-405/subpart-I)

and within it, §405.926(n) places on the list of actions that are **not initial determinations** a
determination that *"a provider or supplier failed to submit a claim timely, or failed to submit a
timely claim despite being requested to do so by the beneficiary or the beneficiary's subrogee"*
([42 CFR 405.926](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-405/subpart-I/subject-group-ECFRba80b2c5e3f1227/section-405.926)).
Not an initial determination → nothing to appeal, because the Medicare FFS appeal ladder begins with
a redetermination **of an initial determination**. The subpart's own title carries Part B.

CMS states the consequence directly, in a Pub. 100-04 transmittal that binds all FFS contractors —
Part B MACs included:

> "When a claim is denied for having been filed after the timely filing period, such denial does not
> constitute an 'initial determination,' and the determination that a claim was not filed timely is
> **not subject to appeal**."
> — [CMS Transmittal R2140CP](https://www.cms.gov/regulations-and-guidance/guidance/transmittals/downloads/r2140cp.pdf)

`timely-filing.md` §9.1 additionally cites **Part B** MAC guidance for the remedy that replaces the
appeal ([Noridian **JE Part B**, Timely Filing](https://med.noridianmedicare.com/web/jeb/topics/claim-submission/timely-filing);
[NGS, Requesting an Exception to Timely Filing](https://www.ngsmedicare.com/web/ngs/timely-filing?selectedArticleId=592187)) —
so the file already carries Part B sourcing, and `README.md` §4 C4's read that it "carries the
stronger citation and should win" is confirmed.

**Why `denial-lifecycle.md` hedged, and why the hedge does not survive.** Its own Open questions
entry names its source: Noridian's **DME MAC** page for CARC 29 / `N211`, which adds an
"acts of nature / circumstances outside the supplier's control" carve-out. That is one MAC's
jurisdiction-specific phrasing of the **42 CFR 424.44 exception process**, not evidence that Part B
sits outside §405.926. Generalizing *from a DME page* was the risk it correctly flagged; it then
over-corrected into doubting a regulation whose own subpart title answers the question.

**Primary source that settles it:**
[42 CFR 405.926(n)](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-405/subpart-I/subject-group-ECFRba80b2c5e3f1227/section-405.926),
read with the title of its containing subpart,
[42 CFR Part 405 Subpart I](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-405/subpart-I);
operationalized for contractors by [CMS Transmittal R2140CP](https://www.cms.gov/regulations-and-guidance/guidance/transmittals/downloads/r2140cp.pdf).

### The rule, stated precisely — the scope limit that matters more than the Part A/B question

What is un-appealable is the determination **"the claim was filed late."** Three things follow, and
`timely-filing.md` §9.1 already states all three:

1. **If the provider concedes lateness**, there is no appeal. The route is a **written
   waiver/extension request to the MAC** under one of the four [42 CFR 424.44](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-424/subpart-C/section-424.44)
   exceptions — not a redetermination request.
2. **If the provider disputes that the claim was late** — the payer's receipt date is wrong, or an
   earlier accepted submission exists — that is a **factual dispute about the receipt date**, not a
   plea for forgiveness, and the remedy is proof of receipt (`timely-filing.md` §8). This is the
   branch that most `CO-29` work actually lands in.
3. **Never bill the patient.** `CO-29` is provider liability; on Medicare, where the beneficiary's
   request for payment was timely but the provider did not file, the provider may not charge the
   beneficiary beyond the deductible/coinsurance that would have applied had Medicare paid
   ([R2140CP](https://www.cms.gov/regulations-and-guidance/guidance/transmittals/downloads/r2140cp.pdf);
   [R830CP](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/Downloads/R830CP.pdf)).

**The rest of `denial-lifecycle.md`'s warning stands and should be kept.** Medicaid and commercial
timely-filing denials **are** generally appealable — there is no analogue to §405.926 outside
Original Medicare (`timely-filing.md` §9.2). The correction is narrow: strike **Part B** from the
list, keep Medicaid and commercial.

### File to correct

**`denial-lifecycle.md`, Open questions**, the CARC 29 bullet. Replace the final sentence
*"Do not generalize this to Part B, Medicaid or commercial payers"* with:

> The rule is settled for **Original Medicare, Parts A and B**: 42 CFR 405.926 sits in Part 405
> Subpart I, *"…Under Original Medicare (Part A and Part B),"* and R2140CP binds all FFS contractors.
> See `timely-filing.md` §9.1. **Do not generalize it to Medicaid, commercial or Medicare Advantage** —
> those have no §405.926 analogue and are generally appealable (`timely-filing.md` §9.2).

`runtime/03-timely-filing.md` already states the corrected rule (*"Do not file a Medicare
redetermination on CO-29 — 42 CFR 405.926 makes 'failed to file timely' not an initial determination"*,
with the DME and `N211`-error carve-outs) and needs **no edit**.

### Impact

**14 corpus cases** (`CO-29` + `N211`), Medicare Part B. The correction removes a live risk of
`awaiting_human` escalation on a family the reference set can in fact dispose of.

### What is still not settled

- **`N211` is not conclusive on its own.** CMS has documented at least one instance where `N211` was
  applied **in error** to claims whose underlying exception-request decisions **were** appealable
  ([CMS Transmittal R3118CP](https://www.cms.gov/regulations-and-guidance/guidance/transmittals/downloads/r3118cp.pdf)).
  Do not treat the presence of `N211` alone as proof that no door exists.
- **Whether a denial of a 424.44 *exception request* is itself appealable** was not established. The
  un-appealable action is the lateness determination; the status of the MAC's refusal of a waiver
  request is a different question and is not answered in this set.
- **No verbatim read of §405.926 or R2140CP.** `ecfr.gov` and `cms.gov` are egress-blocked; the
  subpart title and §405.926(n) text above are search-retrieved. The subpart title is corroborated by
  the eCFR URL structure itself, which is the strongest form of confirmation available here.

---

## Not addressed by this file

**C5** (can Medicare Part B accept frequency `7`) and **C6** (Medicare Advantage reconsideration
deadline: 60 vs 65 days, and 30 vs 60 days to decide) remain as recorded in `README.md` §4.

C5 is a *confidence* conflict rather than a substantive one — both files reach "do not send `7` to
Part B", and C3 above independently relies on that conclusion via the CMS 837P companion guide — so
the schema rule stands unchanged: **`resubmission_frequency_code` must not be populated for Part B.**

C6 is a genuine numeric conflict, all sides citing CMS, and it is **unresolved**. It touches the 8
`PAY-MA2` corpus cases. Do not pick a number from this file.
