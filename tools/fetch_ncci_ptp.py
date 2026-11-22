#!/usr/bin/env python3
"""Generate reference/runtime/10-ncci-ptp-therapy.md from a real CMS PTP file.

The resolver's reference card 07-ncci-and-mue.md says: "look the pair up in
the PTP edit file for the DOS quarter, else awaiting_human -- do not guess."
This tool supplies that edit file, as a distilled card the prompt's reference
library picks up automatically (prompts.reference_library concatenates
reference/runtime/*.md).

The invariant this tool exists to keep: CCMI values enter a deployment ONLY
from CMS's published file -- never typed from memory, never estimated. The
card it writes names its source file and hash, so every value is traceable.

The card is deployment-local data and is gitignored, deliberately: CMS gates
the download behind the AMA CPT End User Agreement, whose terms (internal
use, no redistribution or derivative commercial use of CPT) are for the
DEPLOYING organisation to accept and interpret -- so the licensed content
stays out of the hosted repository, and each deployment generates its card
from the file it accepted the licence for.

No PHI is involved in any direction: the input is CMS's public code-pair
table, the output is code pairs and indicator digits.

Usage:
    # Download the quarterly "PTP Coding Edits" file (practitioner services)
    # from cms.gov yourself, then:
    python tools/fetch_ncci_ptp.py --file ~/Downloads/ptp-practitioner.zip \
        --label "Q3 2026 practitioner services"

Accepts .zip (takes every .csv/.txt inside), .csv or .txt. For .xlsx, export
to CSV first, or install openpyxl. By default keeps pairs where BOTH codes
fall in 97000-97999 (the therapy family this corpus exercises); widen with
--min/--max.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import pathlib
import sys
import zipfile

REPO = pathlib.Path(__file__).resolve().parent.parent
CARD = REPO / "reference" / "runtime" / "10-ncci-ptp-therapy.md"


def rows_from_text(text: str):
    sample = text[:4096]
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=",\t|;")
    except csv.Error:
        dialect = csv.excel
    reader = csv.reader(io.StringIO(text), dialect)
    header = None
    for row in reader:
        cells = [c.strip() for c in row]
        if header is None:
            if any("column 1" in c.lower().replace("*", "") for c in cells):
                header = cells
            continue
        if len(cells) >= 2 and cells[0] and cells[1]:
            yield cells


def collect(path: pathlib.Path):
    if path.suffix.lower() == ".zip":
        with zipfile.ZipFile(path) as z:
            for name in z.namelist():
                if name.lower().endswith((".csv", ".txt")):
                    yield from rows_from_text(
                        z.read(name).decode("utf-8", "replace"))
                elif name.lower().endswith(".xlsx"):
                    yield from xlsx_rows(io.BytesIO(z.read(name)))
    elif path.suffix.lower() == ".xlsx":
        yield from xlsx_rows(path)
    else:
        yield from rows_from_text(path.read_text(encoding="utf-8", errors="replace"))


def xlsx_rows(src):
    try:
        import openpyxl  # noqa: PLC0415
    except ImportError:
        sys.exit("this file is .xlsx: export it to CSV, or pip install openpyxl")
    wb = openpyxl.load_workbook(src, read_only=True)
    for ws in wb:
        header = None
        for row in ws.iter_rows(values_only=True):
            cells = ["" if c is None else str(c).strip() for c in row]
            if header is None:
                if any("column 1" in c.lower().replace("*", "") for c in cells):
                    header = cells
                continue
            if len(cells) >= 2 and cells[0] and cells[1]:
                yield cells


def in_range(code: str, lo: int, hi: int) -> bool:
    return code.isdigit() and lo <= int(code) <= hi


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--file", required=True, type=pathlib.Path,
                    help="the CMS PTP file you downloaded (.zip/.csv/.txt/.xlsx)")
    ap.add_argument("--label", required=True,
                    help='which release this is, e.g. "Q3 2026 practitioner services"')
    ap.add_argument("--min", type=int, default=97000)
    ap.add_argument("--max", type=int, default=97999)
    args = ap.parse_args()
    if not args.file.is_file():
        sys.exit(f"no such file: {args.file}")

    digest = hashlib.sha256(args.file.read_bytes()).hexdigest()[:16]
    kept: dict[tuple[str, str], list[str]] = {}
    total = 0
    for cells in collect(args.file):
        total += 1
        c1, c2 = cells[0].replace("*", "").strip(), cells[1].replace("*", "").strip()
        if not (in_range(c1, args.min, args.max) and in_range(c2, args.min, args.max)):
            continue
        # CMS column order: col1, col2, [pre-1996 flag], effective, deletion,
        # modifier indicator, rationale. Files vary on the flag column, so the
        # indicator is found by shape: the first single-digit 0/1/9 cell after
        # the codes.
        ccmi = next((c for c in cells[2:] if c in ("0", "1", "9")), "?")
        dates = [c for c in cells[2:] if any(ch.isdigit() for ch in c) and c not in ("0", "1", "9")]
        eff = dates[0] if dates else ""
        dele = dates[1] if len(dates) > 1 else ""
        kept[(c1, c2)] = [ccmi, eff, dele]
    if not kept:
        sys.exit(f"read {total} rows but none in {args.min}-{args.max}; "
                 "is this really a PTP edit file?")

    lines = [
        "# NCCI PTP edits — therapy code pairs (from the CMS quarterly file)",
        "",
        f"Source: `{args.file.name}` (sha256 {digest}), {args.label}. "
        f"Generated by `tools/fetch_ncci_ptp.py`; every value below is copied "
        f"from that file, none is recalled or estimated.",
        "",
        "Column One is payable; Column Two is denied when billed together on "
        "the same date. **CCMI 1** = a bypass modifier is allowed when the "
        "record documents distinctness; **CCMI 0** = never billable together; "
        "**CCMI 9** = the edit does not apply. A pair NOT listed here for the "
        "DOS quarter has no PTP edit in this range. Cite this file when a "
        "disposition rests on a CCMI value. If the DOS falls outside the "
        "release named above, this card does not answer the question -- park.",
        "",
        "| Column One | Column Two | CCMI | effective | deleted |",
        "|---|---|---|---|---|",
    ]
    for (c1, c2), (ccmi, eff, dele) in sorted(kept.items()):
        lines.append(f"| {c1} | {c2} | {ccmi} | {eff} | {dele} |")

    CARD.write_text("\n".join(lines) + "\n")
    print(f"wrote {CARD} ({len(kept)} pairs of {total} rows; source sha {digest})")
    print("NOTE: the card joins the cacheable prompt prefix -- the next resolve "
          "re-writes the cache once, then reads warm again.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
