"""Convert every corpus case to case.md. Deterministic; no LLM anywhere.

Usage: python3 convert.py [--template v1]
Reads  ../../corpus/v2-chain-corpus-v1.1/
Writes ../../corpus/v2-chain-corpus-v1.1-md/<CASE_ID>/case.md
"""

import argparse
import importlib
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent / "templates"))

from interpret import load_case  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "corpus" / "v2-chain-corpus-v1.1"
OUT = ROOT / "corpus" / "v2-chain-corpus-v1.1-md"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--template", default="v1")
    args = ap.parse_args()
    tpl = importlib.import_module(args.template)

    case_ids = []
    for line in open(SRC / "dev_index.jsonl"):
        case_ids.append(json.loads(line)["case_id"])
    case_ids.sort()

    failures = []
    unmapped_counter = Counter()
    converted = 0
    for cid in case_ids:
        try:
            case = load_case(SRC / "edi" / cid)
            md = tpl.render(case)
            dest = OUT / cid
            dest.mkdir(parents=True, exist_ok=True)
            (dest / "case.md").write_text(md)
            for src_file, raw in case["unmapped"]:
                unmapped_counter[f"{src_file}:{raw.split('*')[0]}"] += 1
            converted += 1
        except Exception as exc:  # report, never skip silently
            failures.append((cid, repr(exc)))

    log = {
        "template": args.template,
        "cases_in_index": len(case_ids),
        "converted": converted,
        "failures": failures,
        "unmapped_segment_counts": dict(sorted(unmapped_counter.items())),
    }
    (OUT / "conversion_log.json").write_text(json.dumps(log, indent=2, sort_keys=True) + "\n")
    print(json.dumps(log, indent=2, sort_keys=True))
    if failures:
        sys.exit(1)


if __name__ == "__main__":
    main()
