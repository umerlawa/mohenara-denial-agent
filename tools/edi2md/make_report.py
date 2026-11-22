"""Build conversion_report.md: conversion stats, unmapped segments, token comparison.
Tokenizer: tiktoken o200k_base when available; otherwise a labeled fallback estimate.
Run: python3 make_report.py"""

import json
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "corpus" / "v2-chain-corpus-v1.1"
OUT = ROOT / "corpus" / "v2-chain-corpus-v1.1-md"

EDI_FILES = ["eligibility_270.edi", "eligibility_271.edi", "claim_837p.edi",
             "ack_277ca.edi", "remit_835.edi", "chart_note.txt"]

try:
    import tiktoken
    ENC = tiktoken.get_encoding("o200k_base")
    TOKENIZER = "tiktoken o200k_base"

    def count(text):
        return len(ENC.encode(text))
except Exception:
    ENC = None
    TOKENIZER = "fallback estimate: len(text)/4 (tiktoken unavailable)"

    def count(text):
        return len(text) // 4


def main():
    case_ids = sorted(json.loads(l)["case_id"] for l in open(SRC / "dev_index.jsonl"))
    log = json.loads((OUT / "conversion_log.json").read_text())
    edi_tok, md_tok, rows = [], [], []
    for cid in case_ids:
        raw = ""
        for f in EDI_FILES:
            p = SRC / "edi" / cid / f
            if p.exists():
                raw += p.read_text()
        e = count(raw)
        m = count((OUT / cid / "case.md").read_text())
        edi_tok.append(e)
        md_tok.append(m)
        rows.append((cid, e, m))

    def stats(xs):
        return f"min {min(xs)}, median {int(statistics.median(xs))}, max {max(xs)}, total {sum(xs)}"

    lines = []
    w = lines.append
    w("# Conversion report: v2-chain-corpus-v1.1 EDI to markdown")
    w("")
    w(f"Template: {log['template']}")
    w(f"Cases in index: {log['cases_in_index']}")
    w(f"Converted: {log['converted']}")
    w(f"Failures: {len(log['failures'])}" + (f" -> {log['failures']}" if log["failures"] else ""))
    w("")
    w("## Unmapped segments encountered")
    if log["unmapped_segment_counts"]:
        for k, v in log["unmapped_segment_counts"].items():
            w(f"- {k}: {v}")
    else:
        w("None. Every segment in every file was interpreted by the walkers.")
    w("")
    w("## Token comparison")
    w(f"Tokenizer: {TOKENIZER}")
    w("")
    w(f"- EDI artifacts (concatenated, incl. chart note): {stats(edi_tok)}")
    w(f"- case.md: {stats(md_tok)}")
    ratio = sum(md_tok) / sum(edi_tok)
    w(f"- md/edi total token ratio: {ratio:.3f}")
    w("")
    w("## Per-case tokens (edi, md)")
    for cid, e, m in rows:
        w(f"- {cid}: {e}, {m}")
    (OUT / "conversion_report.md").write_text("\n".join(lines) + "\n")
    print(f"tokenizer: {TOKENIZER}")
    print(f"edi: {stats(edi_tok)}")
    print(f"md:  {stats(md_tok)}")
    print(f"ratio: {ratio:.3f}")


if __name__ == "__main__":
    main()
