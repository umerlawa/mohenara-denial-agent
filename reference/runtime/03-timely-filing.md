# Timely filing (CARC 29)

**Recognise:** CARC **29** "the time limit for filing has expired" on the 835, nearly always group **CO**; Medicare pairs RARC **N211** "you may not appeal this decision". Test: DOS on the 837 → payer **receipt** date vs the limit for that payer *and product line* (timely-filing.md §1).

**Disposition:** genuinely late, no exception → `do_not_resubmit` / write off (CO = provider liability, not billable). Proof of an accepted submission inside the window → `appeal` with the clearinghouse acceptance report: dispute the receipt date, don't plead forgiveness. Medicare FFS with a 424.44 exception → written waiver request to the MAC, not a redetermination. NY/CA Medicaid → `correct_and_resubmit` with the approved **delay reason code** (§6).

**Do not:** file a Medicare redetermination on CO-29 — 42 CFR 405.926 makes "failed to file timely" not an initial determination (§9.1). Carve-outs: DME acts of nature / outside the supplier's control; N211 has also been applied in error (R3118CP). Do not apply Medicare's 1-year rule to commercial, Medicaid or MA (contract-driven; 422.520 sets plan payment speed, not filing). Do not bill the patient (§10).

| limit | detail | source |
|---|---|---|
| Medicare FFS | 1 calendar year from DOS; deadline on a Federal nonworkday → next workday; MSP identical — a slow primary never extends it | 42 CFR 424.44 |
| Medicaid FFS | federal floor 12 months from DOS, states shorter: NY 90d, TX 95d, CA 6 months post-service-month (100/75/50 reduction), OH 365d (inpatient from **discharge**) | 42 CFR 447.45; state manuals |
| Commercial | none federally. UHC greatest of 90d / Agreement / state; Cigna 90d par, 180d OON; BCBSTX HMO 180d, PPO 365d; Humana 180d physicians | payer manuals §2.3 |
| State floors override contracts | CA 90d par / 180d non-par; NY 120d unless more favorable; TX 95d for TX-licensed providers regardless of contracting | CA DMHC TAG; NY Ins. Law §3224-a; Tex. Ins. Code 843.337/1301.102 |

| clock | detail | source |
|---|---|---|
| Starts | 837P: line "From" date. 837I: "Through" date. Cigna consecutive days: **last** DOS. COB (Cigna, Humana, CA): the **primary payer's EOB date**. Medicare splits a line, denying only the untimely part — partial CO-29 is expected | CMS R2140CP; §3.1 |
| Stops | when the payer/MAC **receives** it: electronic = the date it passes front-end edits; paper = mailroom receipt | CMS R273CP |
| Does **not** stop | RTP/unprocessable ("not considered a claim"), EDI rejections, corrected resubmissions (no restart). Check 277CA history: sent early, rejected front-end, never reworked is the commonest true CO-29 | CMS R2140CP; Noridian JE |
| Appeal clock (from the remit, shorter) | Medicare redetermination 120d from **receipt**, presumed notice+5 → notice+125; ERISA ≥180d; UHC 12 months from EOB/PRA; Aetna 180d, then 60d | 42 CFR 405.942; 29 CFR 2560.503-1; §7 |

| remedy | detail | source |
|---|---|---|
| Medicare exceptions (4) | CMS/contractor administrative error; retroactive entitlement, alone or with State Medicaid recoupment; retroactive MA/PACE disenrollment + recoupment ≥6mo after DOS. Window = end of the 6th calendar month after notice/recoupment; refused past **4 years from DOS** | 42 CFR 424.44; R2140CP §70.7 |
| Proof accepted | clearinghouse/payer **acceptance** report (strongest); primary EOB for COB; wrong-division filing or payer info request. An EDI **rejection** report is not proof | §8; Anthem; BCBSTX |
| NY relief | par provider, untimely-only denial + unusual occurrence + pattern of timely filing → payer **must pay**, may cut up to 25% | NY Ins. Law §3224-a |

Uncertain: MA non-contracted deadlines, Aetna's initial-submission limit, the "1 calendar year" boundary day, and whether a PM screenshot is proof (§Open questions).
