# Exact duplicate (CARC 18)

**Recognise:** remit_835 carries CARC **18** "Exact duplicate claim/service" under group
**OA** — X12 restricts 18 to OA except where state workers' comp requires CO — $0 paid, at
line or claim level (carc-rarc-remedies.md §5; X12 CARC list). All 13 `exact_duplicate`
cases in this corpus carry **`OA-18` + MOA `N111`**; that is a corpus co-occurrence
(CORPUS-CODES.md), **not** a documented Medicare Part B pairing rule. No reference file
establishes N111 as a payer rule, so use it as a supporting signal, never as the test. The
pairing the references *do* document — 18 + RARC **N522** on DME MACs (denial-lifecycle.md
§7; Noridian) — appears in no corpus case (README §4 C3).

Confirm the claim **adjudicated rather than rejected**, since only an adjudicated prior
claim can be collided with: an 835 exists and its **`CLP07` carries a payer claim control
number** (resubmission-and-frequency-codes.md §1; CMS 835 Companion Guide). The negative
gate is the reliable one — no 835 at all (277CA / 999 / clearinghouse report), or RARC
**MA130**, means the claim never adjudicated, has no appeal or reopening rights, and the
remedy is a new original claim (denial-lifecycle.md §4 row 0, §7; WPS). Do **not** test any
277CA accepted status: only the rejection categories **A3** and **A7** are confirmed at
source, and no accepted-status category or code was ever retrievable (denial-lifecycle.md
§3, Open questions).

The payer matches on **provider / member / DOS / procedure**, plus POS and billed amount
already on file (carc-rarc-remedies.md §5; Noridian). Every 837 sent as `CLM05-3 = 1` is
treated as brand-new and matched against the already-adjudicated claim.

## The discriminator: true vs false duplicate

**True duplicate** — one service, billed once, sent twice. Disposition
**`do_not_resubmit`**, family `exact_duplicate`.

**False duplicate** — a legitimate **repeat or bilateral service** submitted without the
modifier or condition code that distinguishes it (carc-rarc-remedies.md §5). Disposition
**`correct_and_resubmit`**, per payer:
- **Medicare Part B / DME FFS:** frequency `7` is **not accepted at all**; only
  `CLM05-3 = 1` is valid (resubmission-and-frequency-codes.md §6; CMS 837P TI Companion
  Guide). Adding or changing a modifier on an adjudicated claim is a **clerical-error
  reopening**, and modifier **76** is on the reopening-eligible list
  (resubmission-and-frequency-codes.md §7; NGS *Reopenings for Minor Errors and
  Omissions*). Modifiers 77 and 91 are **not** on that list.
- **Commercial / Medicaid:** replacement `7` + `REF*F8` carrying `CLP07`
  (resubmission-and-frequency-codes.md §6).
- Rebill **corrected line(s) only** — resending the whole claim fires another duplicate
  denial (carc-rarc-remedies.md §5).

Modifiers **59/XE/XP/XS/XU, 76, 77, 91** and anatomic are named by CMS only in the **MUE
MAI-1** context (ncci-ptp-and-mue.md §9). The CARC 18 source says just "the appropriate
modifier/condition code" — do not assert a specific modifier clears a duplicate edit.

## Disposition: `do_not_resubmit` (true duplicate)

**Not `none`.** `none` is reserved for a clean claim adjudicated correctly and needing no
rework. A claim in family `exact_duplicate` **is defective** — it was billed twice — so
`none` is wrong even though carc-rarc-remedies.md §5 phrases the remedy as "take no
action". "No action" here means *stop, do not resend*: that is `do_not_resubmit`.

The duplicate edit is hard-coded, MACs **cannot override or bypass** it, and exact
duplicates are rejected with **no appeal rights**, so no resubmission in any form clears it
(denial-lifecycle.md §7; CMS IOM 100-04 ch.1). Group OA is never patient liability, so
never `bill_patient`. The prior claim's disposition governs the money: check status by
portal/IVR first; if the original paid, post it and close. If the finding looks wrong, use
**Telephone Reopenings** — not a new claim, not a redetermination. If the original is still
pending, **hold**. If an appeal is pending, a second original on the same DOS/line is a
duplicate by construction — wait for the decision. Repeat duplicate submissions draw
continuing contractor analysis and, after education, **program-integrity action with
possible OIG referral** (denial-lifecycle.md §7; CMS IOM 100-04 ch.1).

Uncertain: N111's text ("no appeal right except duplicate claim/service issue") carves out
an appeal right denial-lifecycle.md §7 flatly denies — unresolved at source (README §4 C3).
The exact-vs-suspect duplicate boundary is unconfirmed in any reference file.
