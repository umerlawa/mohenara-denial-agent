# reference/ — index for the denial-resolution system

Eight rule files. This README is the routing layer: it says which file answers
which question, how far each file can be trusted, and where the set is silent or
self-contradictory.

**Read this before citing any file.** Three of the nine defect families are not
resolvable from this set, and four pairs of files disagree. Both are listed below.

---

## 1. Reliability tier of each file

Each file states its own retrieval conditions in its header. They are not equal.

| File | Tier | What that means |
|---|---|---|
| `carc-rarc-remedies.md` | **A — cited** | Every rule carries a primary-source URL. Wording is retrieved excerpt, not verbatim read. |
| `denial-lifecycle.md` | **A — cited** | Same. |
| `ncci-ptp-and-mue.md` | **A — cited** | Same. Strongest disposition logic in the set. |
| `resubmission-and-frequency-codes.md` | **A — cited** | Same. |
| `timely-filing.md` | **A — cited** | Same. |
| `appeal-levels.md` | **A — cited** | Same. |
| `cob-and-eligibility.md` | **B — mixed** | Every row is tagged `corpus` (verified against this repo's data) or `pointer` (**source named but never read**). Do not present a `pointer` row as authority. §§3, 4, 6, 9, 10 are `pointer` throughout. |
| `therapy-modifiers-and-threshold.md` | **F — empty** | **Contains no rules at all.** Its own header: *"NO RULES ARE ESTABLISHED IN THIS FILE… Do not cite this file as authority for any billing rule."* It is a list of open questions. |

---

## 2. Routing table — remit signature to file and section

The corpus signatures below are the codes that actually appear in
`corpus/v2-chain-corpus-v1.1-md/`.

| Family | Remit signature in the corpus | Identify from | Choose disposition from | Status |
|---|---|---|---|---|
| `cob_other_primary` | `OA-22` / `CO-22`, MOA `MA04` | `cob-and-eligibility.md` §1, §2, §5.1 | `cob-and-eligibility.md` §5.2 (sequence), §6 (secondary-claim segments), §5.3 (who fixes the COB record) | Covered |
| `eligibility_terminated` | `PR-27` / `CO-27`, MOA `N30`, 271 `EB*6` + `DTP*357` | `cob-and-eligibility.md` §7.4 (271 signature + machine-reader table) | `cob-and-eligibility.md` §8.1 (group code decides), §8.2 (nine overrides), §8.4 (write-off vs patient-transfer table) | Covered — best in the set |
| `exact_duplicate` | `OA-18`, MOA `N111` | `carc-rarc-remedies.md` §5 (CARC 18); `denial-lifecycle.md` §7 row 1 | **Conflicted — see §4 C3.** Three files give three answers and none resolves Medicare Part B. | **Disposition unsafe** |
| `missing_referring_provider` | `CO-16`, MOA `N286` | `carc-rarc-remedies.md` §6 (RARC N286 row) | `carc-rarc-remedies.md` §6 N286 row + §7 summary; `resubmission-and-frequency-codes.md` §4 row 2 / §6 (Part B → new `1`, never `7`) | Covered but **thin** — one table row; and its MA130 gate never fires here (§5) |
| `missing_therapy_modifier` | `CO-4`, MOA `N822`, therapy CPTs with no `GP` | — **nothing** | — **nothing** | **NOT COVERED** |
| `mue_exceeded` | `CO-151`, MOA `N362` | `ncci-ptp-and-mue.md` §10 (exact CARC/group/RARC match) | `ncci-ptp-and-mue.md` §8 (MAI table), §9 (per-MAI disposition), §12 rows 9–11, §11 (no patient liability) | Covered — but MAI is **not on the remit** (§5) |
| `ncci_ptp_no59` | `CO-236`, MOA `M49` / `N20`; rarely `CO-97` | — **CARC 236 appears in no file.** `carc-rarc-remedies.md` §5 CARC 97 covers only the handful of `CO-97` cases | `ncci-ptp-and-mue.md` §3 (CCMI), §6 (disqualifying conditions), §12 rows 3–8 | **Identification NOT COVERED**; disposition strong but CCMI is not on the remit (§5) |
| `threshold_no_kx` | `CO-119`, MOA `N435`, lines with `GP` and no `KX` | — **nothing** | — **nothing** | **NOT COVERED** |
| `timely_filing` | `CO-29`, MOA `N211` | `timely-filing.md` §1 (exact match) | `timely-filing.md` §4 (four Medicare exceptions), §9.1 (not appealable on Medicare FFS), §10 (never billable to patient) | Covered — but see §4 C4 |
| `none` (clean claim) | `CO-45` + `PR-2`, line paid | `carc-rarc-remedies.md` §5 CARC 45 ("this is an adjustment, not a denial") | Post contractual write-off; `PR-2` is patient coinsurance | Covered for `CO-45`. **`PR-2` is documented nowhere in this set.** |

---

## 3. Question-to-file index

| Question | File | Section |
|---|---|---|
| Who owes this balance? | `carc-rarc-remedies.md` | §2 (group codes), §3 (overrides that defeat a PR) |
| Is this a rejection or a denial? | `denial-lifecycle.md` | §1, §2 |
| Appeal, rework, transfer, or write off? | `denial-lifecycle.md` | §4 (five dispositions, first match wins) |
| Frequency `1` vs `7` vs `8`, and `REF*F8`? | `resubmission-and-frequency-codes.md` | §2, §3, §4, §9 |
| Does this payer type even accept a corrected claim? | `resubmission-and-frequency-codes.md` | §6 |
| Corrected claim vs reopening vs appeal? | `resubmission-and-frequency-codes.md` | §7a, §7b (what counts as a clerical error) |
| What does this CARC/RARC mean and what is the remedy? | `carc-rarc-remedies.md` | §5 (CARC table), §6 (RARC table), §7 (disposition summary) |
| Why would resubmitting make this worse? | `denial-lifecycle.md` | §7 |
| How long do I have to file the claim? | `timely-filing.md` | §2 (by payer type), §3 (clock arithmetic) |
| How long do I have to appeal? | `appeal-levels.md` | §1 (Medicare FFS), §5 (MA), §6d (commercial), §8 (routing table) |
| Which evidence must be filed by when? | `appeal-levels.md` | §3 (evidence preclusion at the QIC) |
| Is a timely-filing denial appealable? | `timely-filing.md` | §9.1 (Medicare: no), §9.2 (commercial/Medicaid: yes) |
| Who is primary? | `cob-and-eligibility.md` | §3 (Medicare MSP), §4 (commercial/NAIC) — **all `pointer`** |
| How do I read a 271? | `cob-and-eligibility.md` | §7.2 (EB01 values), §7.4 (termination signature), §7.5 (`AAA` is not an answer) |
| Can I bill the patient after a termination? | `cob-and-eligibility.md` | §8.2, §8.4 |
| Is this PTP pair bypassable? | `ncci-ptp-and-mue.md` | §3 (CCMI), §6 (when 59/X is not supportable) |
| Are these units appealable? | `ncci-ptp-and-mue.md` | §8, §9 (by MAI) |
| Can an NCCI denial go to the patient? | `ncci-ptp-and-mue.md` | §11 (Medicare: no, and an ABN does not change it) |
| Therapy modifiers, KX, thresholds | — | **No file answers this.** Escalate. |

---

## 4. Known contradictions — do not treat either side as settled

**C1 — Medicare permitted group codes.**
`carc-rarc-remedies.md` §2a: *"Medicare FFS (A/B MACs, DME MACs) | **CO, CR, OA, PR only.**"*
`denial-lifecycle.md` §3.1: *"Medicare contractors may use only **CO, OA and PR**."*
Both cite CMS Claims Processing Manual Ch. 22. They disagree on `CR`. Low impact —
no `CR` adjustment appears in the corpus.

**C2 — What `PI` obliges you to do.**
`carc-rarc-remedies.md` §7: *"Any adjustment with **PI** | Appeal — payer asserts a
reduction with no contract behind it | [never] Auto-write-off"* — a mandatory action.
`denial-lifecycle.md` §3.1: *"**PI** | Payer Initiated Reduction | n/a"* — no guidance.
Not strictly incompatible, but a resolver reading only the second will under-act.

**C3 — Exact-duplicate disposition. The sharpest conflict in the set.**
`denial-lifecycle.md` §7: *"Claims/lines determined to be exact duplicates are
**rejected and do not have appeal rights**… use **Telephone Reopenings**, not a new claim."*
`carc-rarc-remedies.md` §5 (CARC 18): *"If a repeat service: add the appropriate
modifier/condition code and **resubmit corrected line(s) only**."*
`resubmission-and-frequency-codes.md` §5: *"(b) it needs correction → **`7` with `REF*F8`**."*
These are three different dispositions. Worse, on Medicare Part B — **69% of this
corpus (386/563 cases are Novitas Medicare Part B)** — `resubmission-and-frequency-codes.md`
§6 says frequency `7` is *not accepted at all*, so its own remedy is unavailable.
Separately, the corpus pairs `OA-18` with **`N111`** (*"no appeal right except
duplicate claim/service issue"*), which carves out an appeal right; `denial-lifecycle.md`
§7 asserts flatly that there is none. `N111` appears in no reference file, and the
`N522` pairing that both files document appears in no corpus case.

**C4 — Are Medicare timely-filing denials appealable, and does that reach Part B?**
`timely-filing.md` §9.1: *"the determination that a claim was not filed timely is
**not subject to appeal**"* (42 CFR 405.926; CMS R2140CP) — stated as a firm Part A/B rule.
`denial-lifecycle.md` Open questions: *"Do not generalize this to Part B, Medicaid
or commercial payers."*
One file's assertion is the other file's explicit warning. `timely-filing.md` carries
the stronger citation and should win, but the conflict is unresolved on the page.

**C5 — Can Medicare Part B accept frequency `7`?**
`denial-lifecycle.md` §5: *"**Not available.** The only valid CLM05-3 value is `1`
(ORIGINAL); a claim with any other value is rejected."* — flat assertion.
`resubmission-and-frequency-codes.md` Open questions: two retrieved excerpts of the
*same* CMS companion guide conflict, and *"the literal rejection-vs-duplicate behaviour
is unverified."*
Same conclusion (do not send `7` to Part B), different confidence. The schema's
`resubmission_frequency_code` field must not be populated for Part B on either reading.

**C6 — Medicare Advantage reconsideration deadline.**
`appeal-levels.md` §5 and `denial-lifecycle.md` §6.3: **60 days**; plan decides within
**60 calendar days**.
`resubmission-and-frequency-codes.md` §8: *"within **65 calendar days** of the notice…
standard reconsideration decided no later than **30 calendar days**."*
Direct numeric conflict on both figures, all citing CMS. Relevant to the 8 corpus cases
on `PAY-MA2` (Keystone Senior Complete HMO).

---

## 5. Gaps a resolver must not paper over

**G1 — Two families have no rules anywhere.** `missing_therapy_modifier` and
`threshold_no_kx` depend entirely on `therapy-modifiers-and-threshold.md`, which
establishes nothing. That file even names `CARC 4` and `CARC 119` — the exact corpus
signatures — as *candidates to verify*, with the instruction *"Do not assume CARC 4
without confirming it."* Together these are ~90 corpus cases. Escalate; do not infer.

**G2 — `ncci_ptp_no59` cannot be identified from this set.** The corpus denies with
`CO-236` + `M49`/`N20`. `CARC 236` appears in no reference file. `ncci-ptp-and-mue.md`
§10 states the PTP remit pairing is *"Not verified in this retrieval"* and warns
*"Do not assert CO-97, B15, M80, or any other specific pairing."* The disposition
logic in that file is excellent once the family is known — the routing into it is missing.

**G3 — The two decision keys are not on the remit.** `ncci-ptp-and-mue.md` turns
every PTP decision on the **CCMI** and every MUE decision on the **MAI**. Neither is
carried in an 835, and §7 notes some MUE values are confidential and unpublished.
A resolver working only from case artifacts cannot reach these; `mue_exceeded` and
`ncci_ptp_no59` should generally resolve to `awaiting_human` unless the disposition
is invariant across indicator values.

**G4 — The set's top-level gate is dead code here.** `carc-rarc-remedies.md` §4 and
`denial-lifecycle.md` §4 row 0 both make **MA130** the first branch (unprocessable →
never appeal, always new claim). **MA130 appears in zero corpus cases.** Neither file
gives a fallback rule for "Medicare Part B, data defect, no MA130" — which is exactly
`missing_referring_provider`.

**G5 — `PR-2` is undocumented.** Every clean claim in the corpus carries `CO-45` +
`PR-2`. `CO-45` is covered; `PR-2` (coinsurance) appears in no file.

---

## 6. Uncited substantive claims

These drive decisions but carry no source. Do not quote them to a payer.

- `denial-lifecycle.md` §4: *"**Never simultaneously:** an appeal and a corrected claim
  on the same DOS/CPT pair."*
- `denial-lifecycle.md` §6.5: *"Underpayment and contract-rate disputes go to the first;
  medical-necessity and benefit denials can go to either."* (`appeal-levels.md` §6a
  covers the same ground **with** citations — use that instead.)
- `timely-filing.md` §3.3: *"the single most common cause of a legitimate CO-29 is a
  claim that was transmitted early but **rejected at the front end** and never re-worked."*
- `ncci-ptp-and-mue.md` §2: *"the denied line is always the **Column Two** code. If the
  remittance denied the Column One code instead, the problem is not a PTP edit."*
- `cob-and-eligibility.md` §8.1: *"**Why `CO-27` exists at all:** a payer uses `CO` …
  where the provider did not verify eligibility."* The file's own §11 confirms this
  *"is not sourced."*
- `cob-and-eligibility.md` §9.2: *"The distinctive markers are a reversal on the 835 …
  and a termination date that lands on a **month end** roughly two months before the reversal."*
- `appeal-levels.md` §6d: *"Treat an unknown commercial deadline as **60 days** until
  the contract is confirmed."* Authored triage default, not a payer rule.

---

## 7. Cross-cutting gates, in order

Run these before reaching for a family-specific file.

1. **Rejection or denial?** `denial-lifecycle.md` §1. No 835 → no appeal rights.
2. **Group code.** `carc-rarc-remedies.md` §2. The CARC never decides liability.
3. **PR overrides.** `carc-rarc-remedies.md` §3 — QMB, Medicaid payment-in-full, NSA,
   ABN validity. Any one defeats a `PR` balance.
4. **Payer type.** Nearly every rule in this set is Medicare FFS. `resubmission-and-frequency-codes.md`
   §6 and `ncci-ptp-and-mue.md` §1 both warn against generalizing. This corpus is
   69% Medicare Part B, 30% commercial, 1% Medicare Advantage.
5. **Clocks.** Claim clock runs from DOS; appeal clock runs from the remit and is
   shorter. `timely-filing.md` header; `appeal-levels.md` header.
