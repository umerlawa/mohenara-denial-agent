"""Independent completeness check. Re-parses every source EDI file with the raw
tokenizer only (no interpreter) and verifies every elementary value appears in
the generated case.md, verbatim or via a small set of declared derived forms.

Declared derived mappings:
  - CCYYMMDD dates may appear as YYYY-MM-DD
  - EDI addresses join N3/N4 elements with ', ' in the markdown
  - single-character values are not checked (no distinguishing power)
  - STRUCTURAL qualifiers whose entire meaning is the rendered form of the value
    they qualify: D8/RD8 (date format; the date is rendered in derived form) and
    HC (procedure code qualifier; the HCPCS/CPT code itself is rendered)
  - HL segments are pure hierarchy scaffolding (level ids, parent pointers, level
    codes); the hierarchy's business content is the NM1 parties, which are checked
Run: python3 verify_completeness.py
"""

STRUCTURAL = {"D8", "RD8", "HC"}

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from x12 import parse_file, values_of  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "corpus" / "v2-chain-corpus-v1.1"
OUT = ROOT / "corpus" / "v2-chain-corpus-v1.1-md"

EDI_FILES = ["eligibility_270.edi", "eligibility_271.edi", "claim_837p.edi",
             "ack_277ca.edi", "remit_835.edi"]


def derived_forms(v):
    forms = [v]
    if len(v) == 8 and v.isdigit():
        forms.append(f"{v[0:4]}-{v[4:6]}-{v[6:8]}")
    return forms


def check_case(cid):
    md_path = OUT / cid / "case.md"
    if not md_path.exists():
        return [("MISSING_MD", "case.md not generated")]
    md = md_path.read_text()
    missing = []
    for fname in EDI_FILES:
        f = SRC / "edi" / cid / fname
        if not f.exists():
            continue
        for seg in parse_file(f):
            if seg.sid == "HL":
                continue
            for v in values_of(seg):
                if len(v) < 2 or v in STRUCTURAL:
                    continue
                if not any(form in md for form in derived_forms(v)):
                    missing.append((fname, f"{seg.sid}: value '{v}' not found"))
    note = SRC / "edi" / cid / "chart_note.txt"
    if note.exists() and note.read_text().strip() not in md:
        missing.append(("chart_note.txt", "verbatim note not found"))
    return missing


def main():
    case_ids = sorted(json.loads(l)["case_id"] for l in open(SRC / "dev_index.jsonl"))
    bad = {}
    checked_values = 0
    for cid in case_ids:
        missing = check_case(cid)
        if missing:
            bad[cid] = missing[:20]
    report = {
        "cases_checked": len(case_ids),
        "cases_failing": len(bad),
        "failures_sample": {k: bad[k] for k in list(bad)[:5]},
    }
    print(json.dumps(report, indent=2))
    (OUT / "completeness_report.json").write_text(json.dumps(
        {"cases_checked": len(case_ids), "cases_failing": len(bad),
         "failures": bad}, indent=2, sort_keys=True) + "\n")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
