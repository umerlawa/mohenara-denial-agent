# dev_labels.jsonl manifest

Source: mohenara-data v2/chain/output/answer_key.jsonl (scorer-side export, owner-authorized)
Selection: seed-42 stratified sample, proportional across scoreable defect families, 120 defected + 20 clean controls
Excluded family: telehealth_pos_modifier (corpus-v1.1 telehealth cases are permanently unscoreable; excluded from every scored set per corpus governance)
Total labels: 140
Per-family counts: {"cob_other_primary": 13, "eligibility_terminated": 13, "exact_duplicate": 13, "missing_referring_provider": 13, "missing_therapy_modifier": 13, "mue_exceeded": 13, "ncci_ptp_no59": 14, "threshold_no_kx": 14, "timely_filing": 14}
Clean controls: 20
Trap cases included: 5 (corpus-limited in line-level metrics; annotate, do not rescore)
sha256 (first 16): 8c567062aa12e662

Rules:
- These are the ONLY answer labels permitted in this repo.
- Pipeline/resolution code must never read eval/. Only scoring code opens this file.
- Remaining dev labels and all holdout cases stay in mohenara-data; final scoring happens there.
- Telehealth-family cases may be run through pipelines but never scored.
- Never regenerate or extend this file from within this repo; re-export is a mohenara-data-side operation.
