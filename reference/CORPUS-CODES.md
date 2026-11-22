# Remit codes this corpus actually carries

Extracted **deterministically** from `corpus/v2-chain-corpus-v1.1-md/*/case.md`
for the 140 labeled cases — by regex over the artifacts, not by reading any
answer key. This file records *which codes to research*, never what the
answers are.

It exists because the first research pass covered the codes a denial textbook
would cover, and this corpus uses a partly different set. Four codes the
system must recognise appeared in no reference file at all.

| family | n | remit signature |
|---|---:|---|
| cob_other_primary | 13 | `MA04`, `CO-22` / `OA-22` |
| eligibility_terminated | 13 | `N30`, **`PR-27` (8) / `CO-27` (5)** |
| exact_duplicate | 13 | `OA-18` + `N111` |
| missing_referring_provider | 13 | `CO-16` + `N286` |
| missing_therapy_modifier | 13 | `CO-4` + `N822` |
| mue_exceeded | 13 | `CO-151` + `N362` |
| ncci_ptp_no59 | 14 | `CO-236` + `N20` |
| none (clean, paid) | 20 | `PR-2` + `CO-45` |
| threshold_no_kx | 14 | `CO-119` + `N435` |
| timely_filing | 14 | `CO-29` + `N211` |

## Claim filing indicator (payer programme)

Also extracted deterministically from the same artifacts. This matters because
the group code is dispositive **only on Medicare FFS** — on a commercial remit
it is the payer's assertion, not a binding write-off
(`co27-terminated-coverage-liability.md`). A resolver therefore has to know
which programme it is looking at *before* it reads the group code.

Overall across the 140 labeled cases: **`MB` 93 (66%), `CI` 46 (33%), `HM` 1**.

| family | filing indicators |
|---|---|
| cob_other_primary | `CI` 13 |
| eligibility_terminated | **`CI` 13** (all commercial) |
| exact_duplicate | `MB` 13 (all Part B) |
| missing_referring_provider | `MB` 11, `CI` 2 |
| missing_therapy_modifier | `MB` 11, `CI` 2 |
| mue_exceeded | `MB` 12, `CI` 1 |
| ncci_ptp_no59 | `MB` 12, `CI` 1, `HM` 1 |
| none (clean, paid) | `MB` 18, `CI` 2 |
| threshold_no_kx | `MB` 14 (all Part B) |
| timely_filing | `CI` 12, `MB` 2 |

**All 13 CARC-27 cases are `CI`.** So every terminated-coverage case in this
corpus sits in the commercial branch — the one where an unconditional
"CO means never bill the patient" is wrong.

## Why this mattered

`eligibility_terminated` splits **PR-27 in 8 cases and CO-27 in 5**. Same
reason code, opposite liability: PR puts the balance on the patient, CO makes
it a provider write-off. A resolver that keys on CARC 27 alone cannot tell
those apart, and would be confidently wrong on whichever group it guessed
against. This is the concrete case behind the spine card's rule that the group
code, not the reason code, decides liability.

`CO-45` and `PR-2` appear on the clean paid claims *and* alongside real
denials — they are contractual adjustment and coinsurance, not denial signals.
A resolver treating either as a denial will invent defects on clean claims.

## Regenerate

    python - <<'PY'
    import json, re, pathlib, collections
    labels = {json.loads(l)['case_id']: json.loads(l)
              for l in open('eval/dev_labels.jsonl')}
    md = pathlib.Path('corpus/v2-chain-corpus-v1.1-md')
    per = collections.defaultdict(collections.Counter)
    for cid, lab in labels.items():
        t = (md / cid / 'case.md').read_text()
        for g, c in set(re.findall(r'\b(CO|PR|OA|PI)-(\d+|[A-Z]\d+)\b', t)):
            per[lab['defect']][f'{g}-{c}'] += 1
        for r in set(re.findall(r'\b([MN]A?\d{2,3})\b', t)):
            per[lab['defect']][r] += 1
    for fam in sorted(per):
        print(fam, per[fam].most_common(6))
    PY

That snippet reads the label file only to group cases by family for display.
It is a one-off analysis run by hand, not part of the system: nothing under
`src/` may open that file, and `eval/test_leakage.py` enforces it.
