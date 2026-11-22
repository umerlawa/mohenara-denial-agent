# Resubmission / claim frequency (CLM05-3: 1 / 7 / 8)

**Recognise:** Remit shows the claim was **adjudicated** (835 has a CLP with a control number in `CLP07`) yet the resubmission went out with `CLM05-3 = 1` and no `REF*F8` — result is CARC **18** "Exact duplicate claim/service" (Medicare Group Code **OA**; DME pairs 18 with RARC **N522**). Compare 837 Loop 2300 `CLM05-3` against 835 `CLP07`. If the claim instead died front-end (999 / 277CA, unprocessable/returned) there is **no** payer claim number and no adjudication.

**Disposition:** Adjudicated + billed content was wrong/incomplete → **corrected claim**: `CLM05-3 = 7` with `REF01=F8`, `REF02` = payer claim control number from 835 `CLP07`, re-sending **all** accurate original lines plus the corrections. Claim should not exist at all (wrong patient, wrong provider, wrong payer, duplicate you created) → `8` void + `REF*F8`, then a new `1`. Front-end rejected → resubmit as `1`, no `REF*F8`. Original still pending on the remit → **hold**, do nothing.

**Do not:** Do not re-send frequency `1` on an adjudicated claim. Every 837 with `CLM05-3=1` is treated as a brand-new claim; duplicate logic matches provider/member/DOS/procedure and fires the edit, which contractors **cannot override or bypass**. Second failure mode: a correction sent without the frequency code denies as duplicate **and the original claim is never adjusted** — the fix is lost. Do not send `REF*F8` on an original. Do not use `5` (late charges) as a correction vehicle. Do not send `7` to **Medicare Part B / DME FFS** — use a clerical-error reopening or redetermination.

**One-line test — corrected claim vs appeal:** was the claim **as billed** incomplete or inaccurate? Yes → corrected claim (`7`). No, the billing was right and you dispute the decision (coverage, medical necessity, amount paid) → **appeal**. "A corrected claim does not constitute an appeal."

| rule | detail | source |
|---|---|---|
| `1` | Admit-through-discharge / original, complete claim; no `REF*F8` | resubmission-and-frequency-codes.md; CMS Blue Button CLM_FREQ_CD; EmblemHealth 837P CG |
| `7` | Replacement — payer voids the original; this claim "represents a complete replacement." All accurate original lines must reappear or you invite refund/overpayment demands | NUBC bill-type frequency codes 837P/D; BCBSOK CPCP025 |
| `8` | Void/cancel — removes the claim rather than revising it | NUBC excerpt; Humana corrected claims |
| `REF*F8` required | TR3 situational: required when CLM05-3 indicates replacement or void (in practice `7`/`8`). Missing → "compliance error and the claim will be rejected" | X12 RFI #2173; BCBSIL claim frequency codes |
| Source of the number | 835 `CLP07` (ICN/DCN/TCN) for **that** payer; never validate length generically | CMS 835 Companion Guide; UHC Admin Guide Ch.10 |
| Part A | `7`/`8` standard; TOB `XX7` adjustment carries the original ICN/DCN, `XX8` cancel, `XXQ` reopening | CMS IOM 100-04 ch.1; CMS R1775CP |
| Part B / DME FFS | `7` not accepted — reopening (1 yr; 4 yr good cause) or redetermination (120 days) | CMS 837P TI CG; NGS duplicate denials; CMS IOM 100-04 ch.34 |
| Medicaid | `7` + state TCN; Member ID / Provider ID cannot be adjusted — void and rebill | NYS Medicaid General Billing Guidelines |
| CARC 18 corollary | Never resolved by resubmitting: confirm disposition, then correct via `7` or contact reopenings if the edit is wrong | Noridian Exact Duplicate Claim/Service |

Uncertain: whether `7` is accepted against a **fully denied** (vs. paid) commercial claim, and whether a `7` may follow an `8` void instead of a new `1`, are unestablished; MA acceptance of `7`/`8` is plan-specific.
