# Therapy discipline modifiers (GP/GO/GN) and the KX threshold

Similar remits, opposite routes: **CO-4 was never adjudicated** (returned unprocessable, no appeal rights); **CO-119 is an adjudicated denial with appeal rights** (therapy-modifiers-and-threshold.md §0, §8).

## (a) missing_therapy_modifier

**Recognise:** `CO-4` + `N822` on always-therapy CPTs **97110 / 97112 / 97140 / 97530** carrying no GP/GO/GN (CORPUS-CODES.md; therapy §4; CMS R13431CP). CARC 4 = "inconsistent with the modifier used **or a required modifier is missing**" (clause two is operative) and N822 = "Missing procedure modifier(s)" — both wordings confirmed (therapy §2.1–§2.2; X12 CARC/RARC lists). **GP** physical therapy, **GO** occupational therapy, **GN** speech-language pathology: "services delivered under an outpatient ___ plan of care." The modifier follows the **plan of care, not the licence in the room**: a PTA under a PT plan bills GP; CQ (PTA) / CO (OTA) pair to GP/GO (therapy §3; CMS R4440CP). Same family: one modifier per line; rev 43x GO only, 44x GN only; unpaired CQ/CO. **Modifier CO (OTA) is not group code CO** (§3).

**Disposition:** `correct_and_resubmit`. Vehicle: a **new original claim** (`CLM05-3 = 1`) with the modifier appended — not a corrected `7`, not a reopening, not an appeal (therapy §8.1). An unprocessable claim is not a claim, is not denied, has no appeal rights; MAC N822 guidance says submit a new claim (MCPM ch.1 §80.3.1; resubmission §4, §6). Apply on **every** CO-4/N822 — there is no MA130 precondition.

**Work these first — timely filing.** The returned claim **never stopped the filing clock**; the 1-year Medicare limit runs on from DOS and no appeal recovers the time (therapy §8.1; timely-filing.md §3.3).

**Do not:** never `appeal` — a redetermination is dismissed while the clock runs (§8.1). Never `bill_patient` — CO is provider liability (§7.1, §7.4). Never append GP/GO/GN off the CMS therapy list; never solicit a retroactive modifier (§3).

## (b) threshold_no_kx

**Recognise:** `CO-119` + `N435`. CARC 119 = "Benefit maximum for this time period or occurrence has been reached" — CMS names it as the therapy-threshold denial. N435 = "Exceeds number/frequency approved/allowed within time period without support documentation" (therapy §2.1–§2.2; MCPM ch.5). **Read the submitted line for KX before routing** — N435 covers two problems (§2.2).

**Facts:** CY2026 KX threshold **$2,480** PT+SLP combined, **$2,480** OT separately; targeted-MR threshold **$3,000** (therapy §5.2; CMS R13437CP). Two accumulators, per beneficiary per calendar year, **national across providers**, applied in claim-**receipt** order (a first-ever clinic claim can already be over). Use the DOS year's figure (MEI-indexed). KX attaches per line and **does not replace GP/GO/GN**. $3,000 is targeted, not automatic: audit exposure, not adjudication (§5.4).

| line facts | action | source |
|---|---|---|
| No KX; record already justified therapy past threshold, dated on/before DOS | `correct_and_resubmit` — clerical-error reopening (1 yr; Part B has no `7`) | therapy §8.2; MCPM ch.34; resubmission §7a–b |
| Same, but the MAC treats KX as complex/appeal-only | `appeal` — redetermination (120 days); a misfiled reopening is converted, not dismissed | therapy §8.2; appeal-levels.md §1 |
| KX **was** present; denial is a documentation judgment | `appeal` — redetermination with treatment/progress/re-eval notes | therapy §2.2, §8.2; CMS RAC Topic 0228 |
| Accumulator disputed (wrong discipline pool; another provider's claims) | `appeal` the arithmetic; do not append KX | therapy §6, §8.3 |
| Record lacks the justification | `awaiting_human`; if confirmed absent, `do_not_resubmit` and write off — KX would be a false attestation | therapy §5.1, §8.3 |

**Do not:** never `bill_patient` on a CO-119. Limitation of liability (SSA §1833(g)/§1879) puts a missing-KX denial on the **provider**; CO is not billable to the beneficiary (therapy §7.1–§7.2; CMS ABN FAQ Aug-2018). Liability transfers only via a valid **pre-service** ABN (CMS-R-131) with **GA**, which shows as **PR**-119. GZ produces CO; an ABN cannot be obtained retroactively; never report GA with KX (§7.3).

Uncertain: the OT $2,480 figure came from search over R13437CP, not the PDF. KX reopening-eligibility varies by MAC. Some MACs pair N822 with CARC **16** — match both. MA/Medicaid/commercial applicability is unestablished; a commercial CO-119 is a benefit-limit denial needing a benefit-limit appeal, not a KX fix (therapy §1).
