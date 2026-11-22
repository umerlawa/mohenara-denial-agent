"""Case-header facts read straight off the uploaded artifacts. Deterministic:
no model calls, no spend.

The practice-audience demo shows a money picture the moment cases are
uploaded -- total denied, who the patient is, which payer said no -- before a
single resolution has run. Those numbers cannot come from the model (it has
not run) and must not be typed into a frontend (that is data wearing the
app's clothes), so they are read off the 835 the payer actually sent:

    CLP  billed (CLP03) and paid (CLP04); denied is the difference
    NM1*QC  the patient
    N1*PR   the payer
    DTM*232 / DTM*472  the date of service
    SVC     one per service line

An `.md` case is a prose rendering; when it embeds the raw segments they
parse the same way, and when it does not the fields come back None -- the
view renders what it knows and claims nothing else.
"""
from __future__ import annotations

import re

# One X12 segment: split the transaction on `~`, elements on `*`. The corpus
# (and any real 835 this demo will meet) uses the standard separators; a file
# that does not simply yields no segments and therefore no facts.
_DATE = re.compile(r"^(\d{4})(\d{2})(\d{2})$")


def _segments(text: str) -> list[list[str]]:
    out = []
    for raw in text.split("~"):
        raw = raw.strip()
        if raw:
            out.append(raw.split("*"))
    return out


def _num(s: str) -> float | None:
    try:
        return float(s)
    except (TypeError, ValueError):
        return None


def _iso(yyyymmdd: str | None) -> str | None:
    m = _DATE.match(yyyymmdd or "")
    return f"{m.group(1)}-{m.group(2)}-{m.group(3)}" if m else None


def _title(s: str) -> str:
    return " ".join(w.capitalize() for w in s.split())


def _pick_remit(files: dict[str, str]) -> str | None:
    """The artifact that carries the claim-payment segments.

    Prefer a file named like a remit; fall back to whichever content has a
    CLP segment, which covers an `.md` rendering that embeds the raw lines.
    """
    for name, body in files.items():
        if "835" in name.lower():
            return body
    for body in files.values():
        if "CLP*" in body:
            return body
    return None


def parse(files: dict[str, str]) -> dict:
    """{patient_name, payer, billed, paid, denied, date_of_service,
    service_count, claim_id} -- every value None when the artifacts do not
    state it. Never guesses."""
    out = {"patient_name": None, "payer": None, "billed": None, "paid": None,
           "denied": None, "date_of_service": None, "service_count": None,
           "claim_id": None}
    body = _pick_remit(files or {})
    if body is None:
        return out

    billed = paid = 0.0
    saw_clp = False
    dos_claim = dos_line = None
    services = 0

    for seg in _segments(body):
        sid = seg[0]
        if sid == "CLP" and len(seg) > 4:
            b, p = _num(seg[3]), _num(seg[4])
            if b is not None:
                saw_clp = True
                billed += b
                paid += p or 0.0
                out["claim_id"] = out["claim_id"] or (seg[1] or None)
        elif sid == "NM1" and len(seg) > 4 and seg[1] == "QC":
            last, first = seg[3], seg[4]
            if last and out["patient_name"] is None:
                out["patient_name"] = _title(f"{first} {last}".strip())
        elif sid == "N1" and len(seg) > 2 and seg[1] == "PR":
            if out["payer"] is None and seg[2]:
                out["payer"] = _title(seg[2])
        elif sid == "DTM" and len(seg) > 2:
            if seg[1] == "232" and dos_claim is None:
                dos_claim = _iso(seg[2])
            elif seg[1] == "472" and dos_line is None:
                dos_line = _iso(seg[2])
        elif sid == "SVC":
            services += 1

    if saw_clp:
        out["billed"] = round(billed, 2)
        out["paid"] = round(paid, 2)
        out["denied"] = round(billed - paid, 2)
    out["date_of_service"] = dos_claim or dos_line
    out["service_count"] = services or None
    return out
