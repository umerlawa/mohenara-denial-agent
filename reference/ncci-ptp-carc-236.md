# CARC 236 + RARC N20 — identifying an NCCI PTP denial on the remit

> **Retrieved 2026-08-12.** Every rule below carries a primary-source citation.
>
> **Retrieval note (read before quoting anything back to a payer):** direct HTTP fetching of
> `cms.gov` (all subdomains), `x12.org`, and every MAC domain tried (`med.noridianmedicare.com`,
> `medicare.fcso.com`, `www.palmettogba.com`, `www.wpsgha.com`, `www.ngsmedicare.com`,
> `www.cgsmedicare.com`, `www.novitas-solutions.com`) was blocked by this environment's egress
> policy (proxy answered 403 to CONNECT). Rule text below was retrieved via **domain-restricted
> search over those same primary domains**, so each cited URL is the authoritative source but the
> wording is a retrieved excerpt, **not a verbatim full-text read**. Nothing here is sourced to a
> billing blog. Where the wording could not be pinned down, the item sits in **Open questions**
> instead of being asserted.
>
> **Scope.** This file solves *identification and routing* only: the remit says `CO-236` + `N20`,
> and the resolver must know that this is an NCCI **procedure-to-procedure (PTP)** denial and
> which line it hit. Once the family is known, **all disposition logic lives in
> [`reference/ncci-ptp-and-mue.md`](./ncci-ptp-and-mue.md)** — CCMI semantics (§3), the bypass
> modifiers (§4–§5), the disqualifying conditions (§6), beneficiary liability (§11), and the
> decision matrix (§12). This file does not restate them.

---

## 1. The one-line routing rule

| Observed on the 835 | Family | Route to |
|---|---|---|
| `CO-236` on a service line, with or without `N20` | **NCCI PTP (code-pair) denial**, provider liability | `ncci-ptp-and-mue.md` §3 → §6 → §12 rows 3–8 |
| `CO-151` + `N362` | MUE (units) denial — a **different** edit program | `ncci-ptp-and-mue.md` §7–§9, §12 rows 9–11 |
| `CO-97` | Bundling, but **not necessarily PTP** — see §4 below | Diagnose first; do not assume PTP |

**Why 236 and not something else:** CMS instructs its contractors directly. "MACs shall assign
**CARC 236 with Group Code CO and MSN 16.8** for claims that fail the PTP edits"
([CMS Transmittal 4188 / CR 10852, R4188CP](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/2018Downloads/R4188CP.pdf);
[Medicare Claims Processing Manual, Ch. 23 §20.9](https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/Downloads/clm104c23.pdf)).
Group code **CO** = contractual obligation = provider liability, which is consistent with the
Medicare rule that a PTP denial cannot be billed to the beneficiary
(`ncci-ptp-and-mue.md` §11).

---

## 2. CARC 236 — official wording

| Field | Value |
|---|---|
| Code | **236** |
| Description | "This procedure or procedure/modifier combination is **not compatible with another procedure or procedure/modifier combination provided on the same day** according to the National Correct Coding Initiative **or workers compensation state regulations/fee schedule requirements**." |
| Group code Medicare uses | **CO** (contractual obligation) |
| Medicare Summary Notice message | **16.8** |
| What it asserts | A code-pair conflict on a **single date of service, same provider, same beneficiary** — not units, not medical necessity, not coverage. |

Sources: [CMS Transmittal 4188 (R4188CP)](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/2018Downloads/R4188CP.pdf);
[Medicare Claims Processing Manual Ch. 23](https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/Downloads/clm104c23.pdf);
[Noridian JE Part B, Not Separately Payable / National Correct Coding Initiative](https://med.noridianmedicare.com/web/jeb/topics/claim-submission/reason-code-guidance/not-separately-payable-national-correct-coding-initiative)
and [Noridian JF Part B, same page](https://med.noridianmedicare.com/web/jfb/topics/claim-submission/reason-code-guidance/not-separately-payable-national-correct-coding-initiative).

> **Provenance caveat, do not skip.** The canonical CARC list is maintained by **X12** and
> `x12.org` was egress-blocked in this retrieval, so the wording above is confirmed from **three
> independent primary reproductions** (a CMS transmittal, the CMS claims-processing manual, and a
> MAC's published reason-code guidance) that agree with each other — **not** from the X12 list
> itself. See **Open questions** before quoting it as "the X12 definition" in an appeal letter.

**The workers'-compensation clause is not decoration.** CARC 236 is shared between two rule
regimes: Medicare/Medicaid NCCI **and** state workers' compensation fee-schedule edits. A WC payer
can send 236 off a **state** edit set that is stricter or older than the current NCCI file, so a
pair that clears a Medicare NCCI scrubber can still deny 236 on a comp claim. On a WC remit,
verifying the pair against the CMS NCCI file is **not** sufficient — the state fee schedule
governs. (Clause text per the sources above; no primary WC-specific source was retrieved — see
**Open questions**.)

**Two things CARC 236 does *not* tell you**, both of which the disposition turns on:

1. **Which code is the column-one partner.** The 835 names only the denied line.
2. **The Correct Coding Modifier Indicator (CCMI, 0/1/9)** for the pair. It is not carried in an
   835 at all. This is the known structural gap flagged in `reference/README.md` §5 (G3): a
   resolver working only from case artifacts **cannot** reach the CCMI and must look it up in the
   PTP edit file for the date-of-service quarter, or route to human review.

---

## 3. RARC N20 — official wording and what it adds

| Field | Value |
|---|---|
| Code | **N20** |
| Description | "**Service not payable with other service rendered on the same date.**" |
| Type | Remittance Advice Remark Code (informational; carried alongside, never instead of, a CARC) |

Source: [CMS, Medicare Claims Processing Manual Ch. 22 — Remittance Advice Remark Codes](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c22_remit_phase3_apr24-03_r2.pdf)
(the same CMS-published RARC list already cited for M80 in `carc-rarc-remedies.md`).

**What N20 adds to 236:** nothing that changes the decision. It restates the same-date conflict in
beneficiary-readable language. It does **not** name the partner code, does not give the CCMI, does
not say whether a bypass modifier is permitted, and does not distinguish "you forgot a modifier"
from "these two are never payable together."

**What N20 is useful for:** it is a *confirming* signal, not a *diagnosing* one. Two practical uses:

- **Corroboration.** `CO-236` + `N20` together are consistent only with a same-date code-pair
  conflict. If a remit carries `236` with a remark pointing at units, frequency, or coverage
  instead, re-diagnose before routing.
- **Line targeting.** In the corpus artifacts the RARC rides on the **denied line only** (the
  paid lines on the same claim carry no remark), so N20 marks the column-two line as reliably as
  the 236 does. *(Corpus observation, not a payer rule.)*

> **Caution on the pairing itself.** The CMS instruction retrieved above names CARC **236**, group
> code **CO**, and **MSN 16.8** — it does **not** name a RARC. No primary text was located that
> instructs MACs to send **N20** specifically on PTP denials (the Noridian denial-resolution page
> that does document N20 pairs it with CARC **234**, in the DME jurisdictions). Treat `N20` as
> *this payer's* corroborating remark, and key the routing on **236**, not on N20. See
> **Open questions**.

---

## 4. 236 vs. 97 vs. B15 — which one a payer sends, and why 236 is the PTP signature

| CARC | Description | What it actually asserts | Is it a PTP edit? |
|---|---|---|---|
| **236** | "This procedure or procedure/modifier combination is not compatible with another procedure or procedure/modifier combination provided on the same day according to the National Correct Coding Initiative or workers compensation state regulations/fee schedule requirements." | A **named-program code-pair edit** (NCCI PTP, or a state WC fee-schedule edit) fired on one DOS. | **Yes — by CMS instruction, this is the PTP denial code.** |
| **97** | "The benefit for this service is included in the payment/allowance for another service/procedure that has already been adjudicated." | **Payment-bundling in general.** The same code covers the global surgical package, OPPS packaging, and MPFS status "B" (always-bundled) codes — *and* PTP bundling. | **Sometimes.** 97 alone does not establish a PTP edit; you must determine which bundling rule fired. See `carc-rarc-remedies.md` §5 (CARC 97), including the trap that a status-"B" code is never separately payable **even with a modifier**. |
| **B15** | "This service/procedure requires that a **qualifying service/procedure be received and covered**. The qualifying other service/procedure has not been received/adjudicated." | A **prerequisite is missing** — the payer needs the qualifying service to exist/adjudicate. Structurally the opposite complaint from PTP: not "these two conflict" but "the required partner is absent." | **No.** Do not route a B15 into PTP logic. |

Sources: 236 per §2 above; 97 per [First Coast, Tips to prevent CARC CO 97](https://medicare.fcso.com/claims/tips-prevent-claim-adjustment-reason-code-carc-co-97)
(as already carried in `carc-rarc-remedies.md` §5); B15 per Noridian denial-resolution pages
([B15 / N674](https://med.noridianmedicare.com/web/jddme/topics/ra/denial-resolution/n674-b15),
[B15 / M114](https://med.noridianmedicare.com/web/jadme/topics/ra/denial-resolution/m114-b15)).

**Why 236 is the modern PTP signature — the defensible version of that claim:**

- CMS **instructs** its contractors to use 236 (with CO and MSN 16.8) for claims that fail PTP
  edits ([R4188CP](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/2018Downloads/R4188CP.pdf);
  [Ch. 23](https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/Downloads/clm104c23.pdf)).
  That is a *specific* instruction naming the NCCI program.
- 236's description **names the NCCI by name**; 97's and B15's do not. 236 therefore carries
  program-level information that 97 cannot: 97 is compatible with four different bundling rules,
  only one of which is PTP.
- Operational consequence: **`236` → route straight to PTP logic. `97` → diagnose the bundling
  rule first.** A resolver that treats 97 as PTP will recommend a bypass modifier on a status-"B"
  code, which is never payable, and on a global-surgery denial, which needs 24/25/58/78/79
  reasoning instead.

> **What is *not* established:** what MACs or commercial payers used **before** 236 (the folklore
> answer is B15 with M80, or 97), and whether a commercial payer or Medicare Advantage plan running
> NCCI-style edits will send 236, 97, or something proprietary. No primary source was located for
> either. See **Open questions** — and do not tell a client "236 replaced B15/M80" on this file's
> authority.

---

## 5. Reading the remit: which line is column two (denied) and which is column one

**The rule that makes the remit self-labelling:**

> "If a provider reports the two codes of an edit pair for the same beneficiary on the same date of
> service, the **Column One code is eligible for payment, but the Column Two code is denied** unless
> a clinically appropriate NCCI PTP-associated modifier is also reported."
> ([CMS, Medicare NCCI PTP Edits](https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits/medicare-ncci-procedure-procedure-ptp-edits))

A MAC states the same thing in remittance terms: "the major/**column 1** code is eligible for
payment and the minor/**column 2** code is **denied with claim adjustment reason code (CARC)
CO236**"
([Noridian JE Part B, Not Separately Payable/NCCI](https://med.noridianmedicare.com/web/jeb/topics/claim-submission/reason-code-guidance/not-separately-payable-national-correct-coding-initiative)).

### 5a. Procedure

| Step | What to do | Confidence |
|---|---|---|
| 1 | **The line carrying `CO-236` is the column-two code.** Read its HCPCS/CPT and its modifiers off that 835 service line. | **Certain** — it is definitional; the payer denied it *because* it is column two. |
| 2 | The column-one partner is **another line on the same claim, same DOS, same rendering provider**, and it will normally be **paid** (or adjusted for an unrelated reason such as CO-45 fee-schedule reduction). | High, but see step 3. |
| 3 | **When more than one other line exists, the 835 does not tell you which one is the partner.** Resolve it by looking the pair up in the **NCCI PTP edit file / MAC PTP lookup tool for the DOS quarter** — each edit row is an explicit Column One / Column Two pair. | **This is a genuine gap in the remit**, not an inference you may skip. Use [Noridian's NCCI PTP Lookup Tool](https://med.noridianmedicare.com/web/jeb/topics/claim-submission/ncci/ncci-ptp-lookup-tool) or the [CMS PTP edit files](https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits/medicare-ncci-procedure-procedure-ptp-edits). |
| 4 | The same lookup returns the **CCMI** for the pair — the field the whole disposition turns on (`ncci-ptp-and-mue.md` §3). Use the file version **in effect on the DOS**, not today's. | Required. There is no way to get CCMI from the 835. |

**Sanity checks that catch a mis-diagnosis:**

- If the **denied** line's code is the one the PTP file lists in **column one**, this is not a PTP
  denial as billed — re-diagnose (`ncci-ptp-and-mue.md` §2).
- If a line already carries **59/XE/XS/XP/XU** and still denied 236, the payer rejected the bypass
  (modifier on the wrong code, CCMI 0, or an edit that ignores the modifier) — this is **not** the
  "forgot the modifier" fact pattern, and appending another modifier is not the remedy.
- One claim can carry a 236 line **and** unrelated denials on other lines. Resolve per line.

### 5b. What this corpus actually looks like *(observed in `corpus/v2-chain-corpus-v1.1-md`, not a rule)*

41 cases contain at least one `CO-236` service line; every one of them carries `N20` on that same
line. 39 are Novitas Medicare Part B; 2 are a Medicare Advantage HMO. The recurring shape:

| Line | Code | Outcome |
|---|---|---|
| Denied | a **timed one-on-one** therapy code (`97110`, `97112`, `97116`, `97140`, `97750`) **with no 59/X modifier** | `CO-236` + `N20`, paid $0 |
| Paid | the **untimed group** code `97150` (or another one-on-one code) | allowed, `CO-45` + `PR-2` |
| Often also paid | sibling one-on-one lines that **do** carry `-59` | allowed, `CO-45` + `PR-2` |

The third row is the tell: on the same claim, same DOS, the lines with `-59` were paid and the line
without it was denied 236. That is the bypass mechanism visible in one artifact.

**CMS guidance is directly on point for this exact pair type:** "the therapist would use the **-59
modifier** to bill for both group therapy and individual therapy CPT codes to distinguish that the
two coded services represent **different sessions or separate encounters** on the same day," and
"**without the -59 modifier, payment would be made for the lower-priced group therapy CPT code**,
in accordance with CPT/CCI rules"
([CMS, 11 Part B Billing Scenarios for PTs and OTs (Individual vs. Group Treatment)](https://www.cms.gov/medicare/coding-billing/therapy-services/11-part-b-billing-scenarios-pts-and-ots-individual-vs-group-treatment);
[PDF](https://www.cms.gov/medicare/billing/therapyservices/downloads/11_part_b_billing_scenarios_for_pts_and_ots.pdf)).

> **Two cautions on that CMS document.** (1) It is old — the PDF is marked "Reviewed 9/2009" and
> derives from a 2002 Open Door Forum — and it **predates the X{EPSU} modifiers (effective
> 2015)**. If the distinctness is a *separate encounter*, current CMS guidance says the specific
> modifier (**XE**) is preferred over 59 (`ncci-ptp-and-mue.md` §5–§6, citing
> [MLN1783722](https://www.cms.gov/files/document/mln1783722-proper-use-modifiers-59-xe-xp-xs-xu.pdf)).
> (2) It does **not** substitute for the pair's CCMI and it does **not** license appending 59 to a
> line whose record does not document a distinct session. "Different sessions" must be in the note.

---

## 6. Remedy: modifier warranted and absent, vs. bundling correct

**Do not re-derive the test here.** The disqualifying conditions and the affirmative test live in
`ncci-ptp-and-mue.md` §6, and the CCMI decision key in §3. This section only maps the two outcomes
onto a 236 remit.

| Situation | Disposition | Authority |
|---|---|---|
| **CCMI = 1**, a bypass modifier (59/XE/XS/XP/XU) was **warranted and absent**, and the **medical record already documents** the separate encounter / anatomic site / specimen | **Workable.** Correct the column-two line by appending the *most specific* applicable modifier and pursue the Part B route in §7. Prefer XE/XS/XP/XU over 59 where one fits (`ncci-ptp-and-mue.md` §5). | The reviewer "may change the initial determination **only if** the correct coding initiative edit has a **modifier indicator of '1'** and the reviewer determines that an NCCI-associated modifier **could have been appended**" ([R4188CP](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/2018Downloads/R4188CP.pdf); [Ch. 23](https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/Downloads/clm104c23.pdf)) |
| **CCMI = 0** | **Write off the column-two line.** No modifier bypass exists; an appeal cannot succeed on the merits. Medicare: not billable to the beneficiary. | On appeal, if the CCMI is "0" and the claim was coded correctly, "there are **no circumstances** in which both procedures of the PTP code pair should be paid" ([CMS, Medicare NCCI FAQ Library](https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits/medicare-ncci-faq-library)); liability rule at `ncci-ptp-and-mue.md` §11 |
| **CCMI = 1** but any §6 disqualifier is present (same site *and* same encounter; the only rationale is different diagnoses or different descriptors; the record does not document distinctness) | **Write off.** Appending 59 anyway is an audit exposure, not an appeal strategy. | `ncci-ptp-and-mue.md` §6 (sourced to [MLN1783722](https://www.cms.gov/files/document/mln1783722-proper-use-modifiers-59-xe-xp-xs-xu.pdf), the [2026 NCCI Policy Manual Ch. 1](https://www.cms.gov/files/document/01-chapter1-ncci-medicare-policy-manual-2026-final.pdf), and [OIG OEI-03-02-00771](https://oig.hhs.gov/oei/reports/oei-03-02-00771.pdf)) |
| **CCMI = 9**, or the edit does not exist in the DOS-quarter file | Challenge the **applicability of the edit**, not the modifier. | `ncci-ptp-and-mue.md` §3, §12 row 3 |
| **Coding itself was wrong** (the correct code pair carries no edit) | Correct the coding, not the modifier. | `ncci-ptp-and-mue.md` §12 row 7 |

**Which code gets the modifier.** MAC guidance: "when appropriate, a modifier to identify
separately identifiable service should be appended to the **Column 2 code**"
([Noridian](https://med.noridianmedicare.com/web/jeb/topics/claim-submission/reason-code-guidance/not-separately-payable-national-correct-coding-initiative)).
CMS's appeal instruction is phrased more broadly — an NCCI-associated modifier "could have been
appended to **either code** of a correctly coded edit code pair"
([R4188CP](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/2018Downloads/R4188CP.pdf)).
**Operationally: put it on the column-two (denied) line**, which is what the MAC instruction and
this corpus's paid `-59` lines both show. Do not read CMS's "either code" as licence to modify the
paid line and leave the denied one untouched.

**A modifier is never the fix for a documentation gap.** Do not go back to the provider asking for
a modifier *because* a denial arrived; the record must already establish the distinctness
(`ncci-ptp-and-mue.md` §6, final row).

---

## 7. The correction route on Medicare Part B

A 236 denial is an **initial determination on an adjudicated claim** — not a rejection. That fixes
the route: it is a **reopening or a redetermination**, never a fresh original claim.

| Route | Use when | Deadline | Source |
|---|---|---|---|
| **Clerical-error reopening** (Part B reopening request; many MACs accept telephone/portal reopenings) | The claim was substantively right and the defect is a **minor error or omission** — the classic case being **"we neglected to include the modifier."** MAC reopening request forms list exactly that reason: "We neglected to include modifier (indicate modifier to append to claim) when the claim was initially submitted." | **1 year** from the initial determination for any reason; 4 years with good cause | [First Coast, Part B Redetermination and Clerical Error Reopening Request Form](https://medicare.fcso.com/sites/default/files/documents/form-52005-partb-redetermination-reopening.pdf); [CMS Pub. 100-04 Ch. 34](https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/downloads/clm104c34.pdf); [CGS, Reopening vs. Redetermination job aid](https://www.cgsmedicare.com/partb/forms/pdf/reopen_vs_redet_jobaid.pdf) |
| **Redetermination** (appeal level 1) | The dispute is **substantive**: the edit was misapplied, the pair is CCMI 9, the coding is defended as billed, or documentation must be weighed. | **120 days** from receipt of the initial determination | [CGS job aid](https://www.cgsmedicare.com/partb/forms/pdf/reopen_vs_redet_jobaid.pdf); [CMS, First Level of Appeal](https://cms.gov/Medicare/Appeals-and-Grievances/OrgMedFFSAppeals/RedeterminationbyaMedicareContractor); `reference/appeal-levels.md` §1 |
| **New original claim (frequency 1)** | **Never**, for a 236. The claim was adjudicated; resending it produces a duplicate denial. | — | `reference/resubmission-and-frequency-codes.md` §5 and §7a |

**Rules that decide which of the first two you file:**

- Adding, changing, or deleting **modifier 59** (and 24, 25, 54, 57, 58, 76, 78, 79, 80, 95, AQ,
  AS, GA) is on MAC lists of **reopening-eligible** minor errors
  ([NGS, Reopenings for Minor Errors and Omissions](https://www.ngsmedicare.com/web/ngs/reopenings-for-minor-errors-and-omissions);
  [CGS, Reopenings](https://www.cgsmedicare.com/jc/claims/reopenings.html); as carried in
  `resubmission-and-frequency-codes.md` §7b).
- Filing the wrong one is partly self-correcting: "irrespective of the request for an appeal,
  contractors shall treat the request as a request for **reopening**" when the issue is really a
  minor error or omission ([CMS Pub. 100-04 Ch. 34](https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/downloads/clm104c34.pdf)).
  Do not rely on this — the reopening clock (1 year) is longer than the redetermination clock
  (120 days), so a late "reopening" cannot be rescued into an appeal.
- **A reopening cannot add services.** "A reopening shall not be granted to add items or services
  that were not previously billed"
  ([First Coast, Part B redetermination and clerical error reopening request form](https://medicare.fcso.com/appeals/new-part-b-medicare-redetermination-and-clerical-error-reopening-request-form-available-now)).
  Fine for appending a modifier to an existing line; not a route to bill a line you left off.
- **Contractor discretion is real:** "the contractor has discretion in determining what meets this
  definition and therefore, what could be corrected through a reopening"
  ([CMS Pub. 100-04 Ch. 34](https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/downloads/clm104c34.pdf)).
  If the MAC declines the reopening and time remains, file the redetermination.
- **A reopening is not an appeal** and confers no appeal rights of its own
  (`reference/appeal-levels.md` §4b).

**What the reviewer will actually do on a 236 appeal** — write to this, not to sympathy:

> The reviewer "must determine whether the claim was coded correctly… whether the provider reported
> an incorrect code, a medically unnecessary service, or **simply neglected to use a modifier**,"
> and may change the determination **only** where the CCMI is "1" and an NCCI-associated modifier
> could have been appended.
> ([CMS Transmittal 4188](https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/2018Downloads/R4188CP.pdf);
> [Ch. 23](https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/Downloads/clm104c23.pdf))

So the appeal must state, in order: (1) the pair and its **CCMI = 1** for the DOS quarter, (2) the
modifier being appended and to which line, (3) the **record language** establishing the separate
encounter/site/specimen. Missing (1) or (3) is why these appeals fail.

**Not Part B:** this section is Medicare FFS only. The 2 Medicare Advantage cases in this corpus
run on the Part C track — different deadlines, different levels — see `reference/appeal-levels.md`
§5. Do not apply the reopening rules above to an MA plan.

---

## 8. Decision table

Read top to bottom; first match governs.

| # | Observed | Action |
|---|---|---|
| 1 | `CO-236` on a service line | Family = **NCCI PTP**. Denied line = **column two**. Do not evaluate MUE logic. |
| 2 | `N20` present | Corroborates same-date bundling. Adds no decision content. Do not key routing on it. |
| 3 | Column-one partner ambiguous (≥2 other lines) | Look the pair up in the **PTP edit file for the DOS quarter**; the 835 does not identify it. |
| 4 | CCMI unknown (always, from an 835 alone) | Look it up. If unavailable, route to **`awaiting_human`** — do not guess (`README.md` §5 G3). |
| 5 | CCMI = 0 | **Write off** the column-two line. Not billable to the Medicare beneficiary. |
| 6 | CCMI = 1, distinctness real **and documented in the record**, no bypass modifier was billed | **Reopening** (Part B) appending the most specific modifier to the column-two line; §7. |
| 7 | CCMI = 1, any `ncci-ptp-and-mue.md` §6 disqualifier present | **Write off.** |
| 8 | CCMI = 9, or no edit exists for the pair in the DOS-quarter file | Challenge **applicability of the edit** via redetermination; §7. |
| 9 | The denied line **already** carried 59/XE/XS/XP/XU | Not a "missing modifier" case. Diagnose why the bypass was rejected before filing anything. |
| 10 | Payer is a commercial plan, MA plan, or workers' comp carrier | §1–§5 identification still reads, but the **Medicare-specific** rules (MSN 16.8, no balance billing, reopening/redetermination route) do **not** transfer. See **Open questions**. |

---

## Open questions

- **X12/WPC canonical text for CARC 236 and RARC N20.** `x12.org` was egress-blocked, so the
  wording in §2 and §3 is confirmed only from CMS and MAC reproductions (three of them, in
  agreement). Before quoting either as "the X12 definition," open the X12 CARC/RARC lists and
  confirm the current text, its start date, and any Last Modified date. In particular the CARC 236
  **"Usage" note** (the standard "Refer to the 835 Healthcare Policy Identification Segment…"
  language) could not be confirmed per-code — the same limitation already recorded in
  `carc-rarc-remedies.md`.
- **Whether CMS instructs any RARC on PTP denials.** The retrieved CMS instruction names CARC 236,
  group code CO, and MSN 16.8 only. No primary text was found instructing **N20** (or M80, or any
  other remark) on PTP denials; the MAC page that documents N20 pairs it with CARC **234** in the
  DME jurisdictions. `N20` on a PTP remit may be payer-specific. Key routing on 236.
- **Exact text of MSN message 16.8.** Not retrieved. Only its assignment to PTP failures is
  confirmed. Do not quote a beneficiary-facing MSN sentence you have not read.
- **What preceded 236 for PTP denials.** No primary source was located showing that Medicare
  previously used B15/M80 or CARC 97 for PTP edits, or when 236 took over. Transmittal 4188 (CR
  10852, issued December 2018) is the earliest **retrieved** instruction naming 236 for PTP, but
  this retrieval did not establish that it was the *first*. Do not assert a "236 replaced X"
  history.
- **Whether commercial payers and Medicare Advantage plans use CARC 236 for their bundling edits.**
  Not established from any primary source. Two cases in this corpus show an MA HMO sending
  `CO-236` + `N20`, which is corpus evidence, not a rule. A commercial payer may license NCCI,
  modify it, add proprietary bundling edits, and may send 97 or a proprietary code instead. The
  Medicare-only rules — MSN 16.8, no beneficiary balance billing, the reopening/redetermination
  route — do not transfer (`ncci-ptp-and-mue.md` §1, §11; `appeal-levels.md` §5–§6).
- **Workers' compensation.** CARC 236's own description names state WC fee schedules, but no
  primary WC source was retrieved. Which states' edit sets diverge from NCCI, and how a WC 236 is
  disputed, is unestablished. Do not apply the NCCI PTP file or the Medicare appeal route to a
  comp remit without checking the state fee schedule.
- **Whether a bypass modifier may be appended to the column-one code.** MAC guidance says append to
  **column two**; CMS's appeal instruction says an NCCI-associated modifier "could have been
  appended to either code." These are not obviously the same rule. §6 resolves it operationally
  (use column two) but the discrepancy is unresolved in primary text.
- **Why a line that already carried 59/X still denied 236.** Several candidate causes (modifier on
  the wrong code, CCMI 0, edits that ignore modifiers for specific code sets — one MAC page
  mentions claims processed "as if the modifier were not present" for certain codes). The
  governing list of such codes was not retrieved. Row 9 of §8 routes these to human diagnosis
  deliberately.
- **NCCI PTP file version vs. date of service.** The requirement to use the DOS-quarter file is
  carried from `ncci-ptp-and-mue.md`; the precise rule for which quarterly version governs a given
  DOS was not confirmed from primary text there or here.
- **Deadlines.** The 1-year reopening and 120-day redetermination figures are cross-referenced from
  `resubmission-and-frequency-codes.md` §7a and `appeal-levels.md`; nothing in this file
  independently establishes a deadline, and timely-filing interaction is out of scope
  (`reference/timely-filing.md`).
