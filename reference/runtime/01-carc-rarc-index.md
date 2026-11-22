# CARC / RARC index (codes in this corpus)

Sources: `reference/carc-rarc-remedies.md` + Source column.

**Recognise:** 835 `CAS` — group code (CAS01) + CARC + RARCs. CARC 16 and 96 are inert alone; the paired RARC names the defect.
**Disposition:** group code sets liability; CARC sets defect family; MA130 forces resubmit-new-claim.
**Do not:** read a CARC without its group code; never appeal MA130 — no appeal rights, dismissed.

**Group-code gate:** CO = provider liable, never bill patient. PR = patient liable, after QMB / 42 CFR 447.15 / NSA / ABN-validity overrides. OA = liability unstated, not billable; pursue the real reason. PI = no contract behind it, so appeal; never on Medicare FFS. (100-04 ch.22)

| Code | Meaning | Points to | Source |
|---|---|---|---|
| 16 | Missing info / submission error | Defect named by paired RARC; fix, resubmit. Never PR | R2372CP |
| 18 | Exact duplicate (OA) | True dup → `do_not_resubmit`: hard-coded, unappealable; original's disposition governs. Repeat/bilateral service → `correct_and_resubmit`: modifier/condition code, corrected line(s) only | Palmetto JJ; 100-04 ch.1 |
| 22 | Another payer primary (COB) | Bill primary, then secondary with its payment data; fix wrong MSP/BCRC record | MSP Manual ch.3 |
| 27 | After coverage terminated | Re-verify eligibility for DOS. PR ⇒ billable after overrides; else rebill correct payer | R470CP |
| 29 | Filing limit expired | Medicare: 1 year from DOS, four statutory exceptions; else write off, never patient | 100-04 ch.1 §70 |
| 45 | Exceeds fee schedule (PR/CO) | Contractual write-off; 100% of charge = disguised denial, demand corrected 835 | X12 RFI 1802/2052 |
| 50 | Not medically necessary | GZ ⇒ CO, provider liable; GA (signed ABN) ⇒ PR, billable. Appeal with record | R2148CP |
| 96 | Non-covered charge | Paired RARC decides. 96+N425+GY = statutory exclusion: billable, appeal futile. CO ⇒ write off | Noridian 96/N425 |
| 97 | Bundled into another service | NCCI PTP, global, OPPS, or MPFS status B. Modifier needs documented criteria; status B never rebill | NCCI ch.1 |
| 109 | Wrong payer/contractor | MA plan, wrong MAC or payer ID. Bill right payer, do not appeal | Palmetto JM |
| 151 | Frequency/units unsupported | MUE exceeded. Appeal to MAC, not NCCI; miscoded units = correct, resubmit | Noridian 151 |
| 181 | Code invalid on DOS | Deleted or not-yet-effective code. New claim with DOS-effective code; not a coverage appeal | Palmetto JJ 181 |
| 197 | Authorization absent | Medicare: append 14-byte UTN (valid 120 days), resubmit. Commercial retro-auth is plan-specific | CMS OPD PA FAQ |
| 204 | Not a covered benefit | CO ⇒ write off; PR ⇒ bill after overrides. Check for miscoding into an excluded category | Utah Medicaid |
| 206 | NPI missing | Populate required NPI, resubmit; Medicare returns it unprocessable | MS Medicaid EOB |
| B7 | Provider not eligible on DOS | PECOS enrollment dates or CLIA scope. Fix enrollment, then reopen; wrong DOS = resubmit | First Coast B7 |
| B15 | Qualifying primary not adjudicated | Add-on without its primary. Resolve primary first, then rebill | NCCI ch.1 |
| N30 | Patient ineligible for service | Benefit-category ineligibility on DOS. Re-verify, rebill correct plan | Utah Medicaid |
| N130 | See plan restrictions | Non-diagnostic alone. Palmetto pairs 109+N130 for therapy overlapping Part A stay ⇒ bill Part A | Palmetto JM |
| N286 | Invalid referring provider ID | Verify ordering/referring NPI and specialty in PECOS, resubmit | Noridian 16/N286 |
| N290 | Invalid rendering provider ID | Fix Item 24J / 837P loop 2310B, resubmit | Noridian NPI |
| N448 | Not in fee schedule/contract | With CARC 45. Pricing/contract issue — negotiate or appeal, not resubmit | MassHealth |
| M51 | Invalid procedure code | Correct code, resubmit; with 16+MA130 no appeal rights | 100-04 ch.22 |
| M76 | Invalid diagnosis | Fix diagnosis codes/pointers, resubmit; if really CARC 50, appeal with records | 100-04 ch.22 |
| M80 | Same session as approved service | Accompanies 97 or 151. Distinct session must be documented, else write off | 100-04 ch.22 |
| MA04 | Primary payer data missing | `correct_and_resubmit` to the **same** payer: populate primary `SBR`/`AMT`/`CAS`. Completeness defect, not a denial — do not appeal; never `resubmit_other_payer` | Palmetto MSP FAQ; cob-and-eligibility.md §5.1 |
| MA130 | Unprocessable, no appeal rights | Always correct-and-resubmit; redetermination is dismissed | R2041CP |

Uncertain: no required group code established for CARC 22, 109, 204, 206. M80's X12 wording conflicts with the CMS wording used.
