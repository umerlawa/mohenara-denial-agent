"""Walk parsed segments per transaction type into structured dicts.
Anything not explicitly handled lands in case['unmapped'] and is still rendered."""

from x12 import parse_file
import codes as C

KNOWN = {
    "270": {"ISA", "GS", "ST", "BHT", "HL", "NM1", "DMG", "DTP", "EQ", "SE", "GE", "IEA", "TRN", "REF", "N3", "N4", "PER"},
    "271": {"ISA", "GS", "ST", "BHT", "HL", "NM1", "DMG", "DTP", "EB", "MSG", "SE", "GE", "IEA", "TRN", "REF", "N3", "N4", "PER"},
    "837": {"ISA", "GS", "ST", "BHT", "NM1", "PER", "HL", "N3", "N4", "REF", "SBR", "DMG", "CLM", "HI", "LX", "SV1", "DTP", "SE", "GE", "IEA"},
    "277": {"ISA", "GS", "ST", "BHT", "HL", "NM1", "TRN", "STC", "REF", "DTP", "SE", "GE", "IEA", "QTY", "AMT"},
    "835": {"ISA", "GS", "ST", "BPR", "TRN", "DTM", "N1", "N3", "N4", "PER", "REF", "LX", "CLP", "NM1", "SVC", "CAS", "AMT", "LQ", "MOA", "SE", "GE", "IEA"},
}


def envelope(segs):
    env = {}
    for s in segs:
        if s.sid == "ISA":
            env["isa"] = {
                "sender_qual": s.e(5), "sender": s.e(6).strip(),
                "receiver_qual": s.e(7), "receiver": s.e(8).strip(),
                "date": s.e(9), "time": s.e(10), "control": s.e(13),
                "version": s.e(12), "usage": s.e(15),
            }
        elif s.sid == "GS":
            env["gs"] = {"func": s.e(1), "sender": s.e(2), "receiver": s.e(3),
                         "date": s.e(4), "time": s.e(5), "control": s.e(6),
                         "version": s.e(8)}
        elif s.sid == "ST":
            env["st"] = {"type": s.e(1), "control": s.e(2), "impl": s.e(3)}
        elif s.sid == "SE":
            env["se"] = {"count": s.e(1), "control": s.e(2)}
        elif s.sid == "GE":
            env["ge"] = {"count": s.e(1), "control": s.e(2)}
        elif s.sid == "IEA":
            env["iea"] = {"count": s.e(1), "control": s.e(2)}
    return env


def name_row(s):
    """NM1 -> dict."""
    return {
        "entity": s.e(1), "type": s.e(2), "last": s.e(3), "first": s.e(4),
        "middle": s.e(5), "id_qual": s.e(8), "id": s.e(9),
    }


def walk_eligibility(path, kind):
    segs = parse_file(path)
    out = {"env": envelope(segs), "parties": [], "dates": [], "eb": [], "msgs": [],
           "trn": [], "dmg": None, "eq": None, "bht": None, "unmapped": []}
    known = KNOWN["270"] | KNOWN["271"]
    cur_party = None
    for s in segs:
        if s.sid in ("ISA", "GS", "ST", "SE", "GE", "IEA", "HL"):
            continue
        elif s.sid == "BHT":
            out["bht"] = {"structure": s.e(1), "purpose": s.e(2), "ref": s.e(3), "date": s.e(4), "time": s.e(5), "type": s.e(6)}
        elif s.sid == "NM1":
            cur_party = name_row(s)
            cur_party["addr"] = []
            out["parties"].append(cur_party)
        elif s.sid in ("N3", "N4") and cur_party is not None:
            cur_party["addr"].append("*".join([e for e in s.elems if e]))
        elif s.sid == "PER" and cur_party is not None:
            cur_party["contact"] = s.elems
        elif s.sid == "REF" and cur_party is not None:
            cur_party.setdefault("refs", []).append((s.e(1), s.e(2)))
        elif s.sid == "DMG":
            out["dmg"] = {"dob": s.e(2), "gender": s.e(3)}
        elif s.sid == "TRN":
            out["trn"].append({"type": s.e(1), "ref": s.e(2), "origin": s.e(3)})
        elif s.sid == "DTP":
            out["dates"].append({"qual": s.e(1), "fmt": s.e(2), "value": s.e(3)})
        elif s.sid == "EQ":
            out["eq"] = s.e(1)
        elif s.sid == "EB":
            out["eb"].append({"info": s.e(1), "coverage": s.e(2), "service": s.e(3),
                              "plan": s.e(4), "plan_desc": s.e(5), "raw": s.raw})
        elif s.sid == "MSG":
            out["msgs"].append(s.e(1))
        else:
            out["unmapped"].append(s.raw)
    return out


def walk_claim(path):
    segs = parse_file(path)
    out = {"env": envelope(segs), "parties": [], "sbr": None, "clm": None, "dx": [],
           "lines": [], "bht": None, "dmg": None, "unmapped": []}
    cur_party = None
    cur_line = None
    for s in segs:
        if s.sid in ("ISA", "GS", "ST", "SE", "GE", "IEA", "HL"):
            continue
        elif s.sid == "BHT":
            out["bht"] = {"structure": s.e(1), "purpose": s.e(2), "ref": s.e(3), "date": s.e(4), "time": s.e(5), "type": s.e(6)}
        elif s.sid == "NM1":
            cur_party = name_row(s)
            cur_party["addr"] = []
            out["parties"].append(cur_party)
        elif s.sid in ("N3", "N4") and cur_party is not None:
            cur_party["addr"].append("*".join([e for e in s.elems if e]))
        elif s.sid == "PER" and cur_party is not None:
            cur_party["contact"] = s.elems
        elif s.sid == "REF" and cur_line is not None:
            cur_line.setdefault("refs", []).append((s.e(1), s.e(2)))
        elif s.sid == "REF" and cur_party is not None:
            cur_party.setdefault("refs", []).append((s.e(1), s.e(2)))
        elif s.sid == "DMG":
            out["dmg"] = {"dob": s.e(2), "gender": s.e(3)}
        elif s.sid == "SBR":
            out["sbr"] = {"payer_resp": s.e(1), "relation": s.e(2), "filing": s.e(9)}
        elif s.sid == "CLM":
            comp = s.comp(5)
            out["clm"] = {
                "id": s.e(1), "charge": s.e(2),
                "pos": comp[0] if comp else "",
                "facility_qual": comp[1] if len(comp) > 1 else "",
                "frequency": comp[2] if len(comp) > 2 else "",
                "provider_sig": s.e(6), "assignment": s.e(7),
                "benefits_assign": s.e(8), "release": s.e(9),
            }
        elif s.sid == "HI":
            for el in s.elems:
                if el:
                    parts = el.split(":")
                    out["dx"].append({"qual": parts[0], "code": parts[1] if len(parts) > 1 else ""})
        elif s.sid == "LX":
            cur_line = {"lx": s.e(1)}
            cur_party = None
            out["lines"].append(cur_line)
        elif s.sid == "SV1" and cur_line is not None:
            comp = s.comp(1)
            cur_line.update({
                "proc_qual": comp[0] if comp else "",
                "cpt": comp[1] if len(comp) > 1 else "",
                "mods": comp[2:],
                "charge": s.e(2), "unit_type": s.e(3), "units": s.e(4),
                "dx_pointer": s.e(7),
            })
        elif s.sid == "DTP" and cur_line is not None:
            cur_line["dos"] = {"qual": s.e(1), "fmt": s.e(2), "value": s.e(3)}
        else:
            out["unmapped"].append(s.raw)
    return out


def walk_ack(path):
    segs = parse_file(path)
    out = {"env": envelope(segs), "parties": [], "stc": [], "trn": [], "refs": [],
           "dates": [], "bht": None, "amt": [], "qty": [], "unmapped": []}
    for s in segs:
        if s.sid in ("ISA", "GS", "ST", "SE", "GE", "IEA", "HL"):
            continue
        elif s.sid == "BHT":
            out["bht"] = {"structure": s.e(1), "purpose": s.e(2), "ref": s.e(3), "date": s.e(4), "time": s.e(5), "type": s.e(6)}
        elif s.sid == "NM1":
            out["parties"].append(name_row(s))
        elif s.sid == "TRN":
            out["trn"].append({"type": s.e(1), "ref": s.e(2)})
        elif s.sid == "STC":
            comp = s.comp(1)
            out["stc"].append({
                "category": comp[0] if comp else "",
                "status": comp[1] if len(comp) > 1 else "",
                "date": s.e(2), "action": s.e(3), "amount": s.e(4), "raw": s.raw,
            })
        elif s.sid == "REF":
            out["refs"].append((s.e(1), s.e(2)))
        elif s.sid == "DTP":
            out["dates"].append({"qual": s.e(1), "fmt": s.e(2), "value": s.e(3)})
        elif s.sid == "AMT":
            out["amt"].append((s.e(1), s.e(2)))
        elif s.sid == "QTY":
            out["qty"].append((s.e(1), s.e(2)))
        else:
            out["unmapped"].append(s.raw)
    return out


def walk_remit(path):
    segs = parse_file(path)
    out = {"env": envelope(segs), "bpr": None, "trn": [], "dates": [], "payer": None,
           "payee": None, "clp": None, "claim_parties": [], "claim_dates": [],
           "lines": [], "claim_cas": [], "moa": [], "refs": [], "unmapped": []}
    cur_n1 = None
    cur_line = None
    in_claim = False
    for s in segs:
        if s.sid in ("ISA", "GS", "ST", "SE", "GE", "IEA", "LX"):
            continue
        elif s.sid == "BPR":
            out["bpr"] = {"handling": s.e(1), "amount": s.e(2), "credit": s.e(3),
                          "method": s.e(4), "date": s.e(16)}
        elif s.sid == "TRN":
            out["trn"].append({"type": s.e(1), "ref": s.e(2), "origin": s.e(3)})
        elif s.sid == "DTM" and not in_claim and cur_line is None:
            out["dates"].append({"qual": s.e(1), "value": s.e(2)})
        elif s.sid == "N1":
            cur_n1 = {"entity": s.e(1), "name": s.e(2), "id_qual": s.e(3), "id": s.e(4), "addr": []}
            if s.e(1) == "PR":
                out["payer"] = cur_n1
            elif s.e(1) == "PE":
                out["payee"] = cur_n1
        elif s.sid in ("N3", "N4") and cur_n1 is not None and cur_line is None:
            cur_n1["addr"].append("*".join([e for e in s.elems if e]))
        elif s.sid == "PER" and cur_n1 is not None:
            cur_n1["contact"] = s.elems
        elif s.sid == "REF" and cur_line is not None:
            cur_line.setdefault("refs", []).append((s.e(1), s.e(2)))
        elif s.sid == "REF":
            out["refs"].append((s.e(1), s.e(2)))
        elif s.sid == "CLP":
            in_claim = True
            out["clp"] = {
                "claim_id": s.e(1), "status": s.e(2), "charge": s.e(3),
                "paid": s.e(4), "patient_resp": s.e(5), "filing": s.e(6),
                "payer_control": s.e(7), "pos": s.e(8), "frequency": s.e(9),
            }
        elif s.sid == "NM1" and in_claim:
            out["claim_parties"].append(name_row(s))
        elif s.sid == "DTM" and in_claim and cur_line is None:
            out["claim_dates"].append({"qual": s.e(1), "value": s.e(2)})
        elif s.sid == "SVC":
            comp = s.comp(1)
            cur_line = {
                "proc_qual": comp[0] if comp else "",
                "cpt": comp[1] if len(comp) > 1 else "",
                "mods": comp[2:],
                "charge": s.e(2), "paid": s.e(3), "units": s.e(5),
                "cas": [], "rarcs": [], "dates": [], "amts": [],
            }
            out["lines"].append(cur_line)
        elif s.sid == "DTM" and cur_line is not None:
            cur_line["dates"].append({"qual": s.e(1), "value": s.e(2)})
        elif s.sid == "CAS":
            triples = []
            i = 2
            while i < len(s.elems) + 1:
                code, amt, qty = s.e(i), s.e(i + 1), s.e(i + 2)
                if code:
                    triples.append({"group": s.e(1), "code": code, "amount": amt, "qty": qty})
                i += 3
            target = cur_line["cas"] if cur_line is not None else out["claim_cas"]
            target.extend(triples)
        elif s.sid == "AMT" and cur_line is not None:
            cur_line["amts"].append((s.e(1), s.e(2)))
        elif s.sid == "LQ" and cur_line is not None:
            cur_line["rarcs"].append(s.e(2))
        elif s.sid == "MOA":
            out["moa"].append([e for e in s.elems if e])
        else:
            out["unmapped"].append(s.raw)
    return out


def load_case(case_dir):
    case = {"id": case_dir.name, "files": {}, "unmapped": []}
    f = case_dir / "eligibility_270.edi"
    if f.exists():
        case["files"]["270"] = walk_eligibility(f, "270")
    f = case_dir / "eligibility_271.edi"
    if f.exists():
        case["files"]["271"] = walk_eligibility(f, "271")
    f = case_dir / "claim_837p.edi"
    if f.exists():
        case["files"]["837"] = walk_claim(f)
    f = case_dir / "ack_277ca.edi"
    if f.exists():
        case["files"]["277"] = walk_ack(f)
    f = case_dir / "remit_835.edi"
    if f.exists():
        case["files"]["835"] = walk_remit(f)
    f = case_dir / "chart_note.txt"
    case["chart_note"] = f.read_text().strip() if f.exists() else None
    for key, blob in case["files"].items():
        for raw in blob.get("unmapped", []):
            case["unmapped"].append((key, raw))
    return case
