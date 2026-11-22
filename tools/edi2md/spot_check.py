"""Round-trip spot check: reconstruct key claim facts from case.md alone (regex)
and diff against an independent parse of the source EDI. Fixed seed 42, 10 cases.
Run: python3 spot_check.py"""

import json
import random
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from x12 import parse_file  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "corpus" / "v2-chain-corpus-v1.1"
OUT = ROOT / "corpus" / "v2-chain-corpus-v1.1-md"


def facts_from_edi(cid):
    facts = {}
    segs = parse_file(SRC / "edi" / cid / "claim_837p.edi")
    lines = []
    cur = None
    for s in segs:
        if s.sid == "NM1" and s.e(1) == "IL":
            facts["patient"] = f"{s.e(4)} {s.e(3)}"
        elif s.sid == "LX":
            cur = {}
            lines.append(cur)
        elif s.sid == "SV1" and cur is not None:
            comp = s.comp(1)
            cur["cpt"] = comp[1]
            cur["charge"] = s.e(2)
            cur["units"] = s.e(4)
        elif s.sid == "DTP" and cur is not None and s.e(1) == "472":
            cur["dos"] = s.e(3)
    facts["lines"] = lines
    segs = parse_file(SRC / "edi" / cid / "remit_835.edi")
    cas = []
    payer = ""
    for s in segs:
        if s.sid == "N1" and s.e(1) == "PR":
            payer = s.e(2)
        elif s.sid == "CAS":
            i = 2
            while i < len(s.elems) + 1:
                if s.e(i):
                    cas.append((s.e(1), s.e(i), s.e(i + 1)))
                i += 3
    facts["payer"] = payer
    facts["cas"] = sorted(cas)
    return facts


def facts_from_md(cid):
    md = (OUT / cid / "case.md").read_text()
    facts = {}
    m = re.search(r"Patient (.*?), DOB", md)
    facts["patient"] = m.group(1) if m else ""
    m = re.search(r"Payer: (.*?)\. Service date", md)
    facts["payer"] = m.group(1) if m else ""
    claim_section = md.split("## Claim as billed (837P)")[1].split("##")[0]
    lines = []
    for row in re.finditer(
            r"\| (\d+) \| ([\w\-]+) \| ([\d.]+) UN \| \$([\d.]+) \| (\d{4}-\d{2}-\d{2}) \|",
            claim_section):
        cpt = row.group(2).split("-")[0]
        lines.append({"cpt": cpt, "charge": row.group(4),
                      "units": row.group(3), "dos": row.group(5).replace("-", "")})
    facts["lines"] = lines
    remit_section = md.split("## Adjudication outcome (835)")[1].split("## Claim as billed")[0]
    cas = []
    for m2 in re.finditer(r"(CO|PR|OA|PI)-(\w+) \([^)]*\) \$([\d.]+)", remit_section):
        cas.append((m2.group(1), m2.group(2), m2.group(3)))
    facts["cas"] = sorted(cas)
    return facts


def main():
    case_ids = sorted(json.loads(l)["case_id"] for l in open(SRC / "dev_index.jsonl"))
    rng = random.Random(42)
    sample = rng.sample(case_ids, 10)
    mismatches = []
    for cid in sample:
        edi = facts_from_edi(cid)
        md = facts_from_md(cid)
        for key in ("patient", "payer", "lines", "cas"):
            if edi[key] != md[key]:
                mismatches.append((cid, key, edi[key], md[key]))
    print(json.dumps({"sampled": sample, "mismatches": mismatches}, indent=2))
    sys.exit(1 if mismatches else 0)


if __name__ == "__main__":
    main()
