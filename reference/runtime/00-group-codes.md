# Group codes and next_action

**Recognise:** every 835 adjustment carries a group code (CAS01) *and* a CARC. The CARC says why; the **group code alone** says who owes it. A CARC without its group code cannot answer "may this be billed".

**Disposition:** group code fixes liability; first matching ladder row fixes next_action.

**Do not:** infer liability from the CARC. CO-96/CO-204 is a write-off, PR-96/PR-204 is billable — same CARC, opposite answer.

| group code | who owes it / billable to patient | source |
|---|---|---|
| **CO** Contractual Obligation | **Medicare FFS (`MB`): never bill the patient** — CMS makes the group code a programme rule. **Commercial (`CI`/`HM`): not automatic.** CO is the payer's *assertion*; the binding instrument is the participation agreement's hold-harmless clause, which runs to covered members for covered services — a non-member on the DOS sits outside it. Check the filing indicator first. | carc-rarc-remedies.md §2; CMS IOM 100-04 ch.22; co27-terminated-coverage-liability.md |
| **PR** Patient Responsibility | Patient. Medicare: billable "only when Group Code PR is used", subject to overrides. | same |
| **OA** Other Adjustments ("no other group code applies") | Liability **not stated**; not billable. Pursue wrong payer / duplicate / COB. | same |
| **PI** Payer Initiated Reduction — no contract between payer and provider | Not billable, not binding on the provider. Appeal, do not write off. | carc-rarc-remedies.md §2; X12 RFI #2052 |
| **CR** Corrections/Reversals | Reversal bookkeeping; no liability. | same |
| Medicare FFS sends CO, CR, OA, PR only | **PI means the payer is not Medicare FFS.** | carc-rarc-remedies.md §2a |

**PR overrides — PR that still cannot be billed** (carc-rarc-remedies.md §3):

| override | effect |
|---|---|
| QMB (RARC N781/N782) | No Part A/B cost sharing billable; refund collected; bill Medicaid (CMS MLN QMB) |
| Medicaid-participating provider, State-plan service | No balance billing beyond State-plan cost sharing (42 CFR 447.15) |
| No Surprises Act (RARC N830) | Only the PR amount is collectable; refund overages (CMS/CCIIO NSA) |
| Medicare medical necessity, **GZ** (no ABN) | CO + CARC 50, provider liable. **GA** (signed ABN) → PR, billable (CMS R2148CP) |

**next_action ladder — first match wins** (denial-lifecycle.md §4; carc-rarc-remedies.md §4, §7):

| observed | next_action | source |
|---|---|---|
| RARC **MA130**, or no 835 (277CA/999/clearinghouse) | `correct_and_resubmit` — never adjudicated; no appeal *or* reopening rights; send a NEW original claim | CMS R2041CP; IOM 100-04 ch.1 |
| Provider-side data/coding or completeness defect (modifier, DOS, units, POS, NPI, member ID): CARC 16, 181, 206, RARC N286/N290/**MA04** | `correct_and_resubmit` **to the same payer**. Part B FFS vehicle depends on whether the claim was **adjudicated**: returned as unprocessable (RUC — no appeal rights, e.g. CO-4/N822, MA130) was never a claim → **new original** (`CLM05-3 = 1`); an adjudicated denial with a clerical error → **reopening**. Frequency `7` is rejected on Part B either way. Commercial/Medicaid: `7` + `REF*F8`. **MA04** = primary payer's identity/adjudication data missing: supply it and resend. Completeness defect, not a denial; appealing burns the window | denial-lifecycle.md §5; cob-and-eligibility.md §5.1 |
| Claim data right; determination wrong, or defence is records / medical necessity / auth | `appeal` | CMS First Level of Appeal |
| Any **PI** adjustment | `appeal` — reduction with no contract behind it | carc-rarc-remedies.md §7 |
| Another payer primary, or payer disclaims: CARC **22**, **109** (**not MA04**) | `resubmit_other_payer` — bill the true primary/correct contractor; never appeal a disclaiming payer | carc-rarc-remedies.md §7; cob-and-eligibility.md §5.1 |
| **PR** balance, overrides cleared | `bill_patient` | denial-lifecycle.md §4 |
| RARC **MA18 / N89 / MA07** on a Medicare remit | `none` — clean claim, already crossed over; do not bill the secondary | CMS COBA guide |
| Genuine exact duplicate (CARC 18, OA) | `do_not_resubmit` — a duplicate is defective, never `none`; edits are hard-coded, unappealable, the original claim's disposition governs. Other case — repeat/bilateral service: `correct_and_resubmit`, corrected line(s) only | IOM 100-04 ch.1; carc-rarc-remedies.md §5; denial-lifecycle.md §7 |
| **CO** with no appeal basis or rights exhausted; MPFS status "B" code; CARC 29 with no exception | `do_not_resubmit` (write off) — provider-liable, never billable | denial-lifecycle.md §4; HFMA AR-6 |

Never run an appeal and a corrected claim on one DOS/CPT — the second trips duplicate edits.

Uncertain: the enum has no `reopening` value, so both Part B vehicles above are emitted as `correct_and_resubmit` and the vehicle is named in `detail`. The adjudicated-vs-unprocessable split itself is settled (therapy-modifiers-and-threshold.md §8.1; denial-lifecycle.md §4; IOM 100-04 ch.34).
