"""Case-header facts come off the artifact bytes, never typed in. Offline.

The practice-audience demo opens with dollar figures and patient names before
any model has run. Every one of those values must trace to the uploaded 835 --
a frontend that hardcoded a single amount would keep showing it on a case
where it is wrong, which is the same dishonesty the annotation rules exist to
prevent, just wearing a currency sign.
"""
from __future__ import annotations

import pathlib
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "src"))

from mohenara import caseinfo  # noqa: E402

CORPUS = REPO / "corpus" / "v2-chain-corpus-v1.1" / "edi"


def _files(case_id: str) -> dict[str, str]:
    d = CORPUS / case_id
    return {p.name: p.read_text() for p in sorted(d.iterdir())}


def test_the_29_header_matches_the_remit():
    got = caseinfo.parse(_files("MOH2-000029"))
    assert got["billed"] == 169.75
    assert got["paid"] == 0.0
    assert got["denied"] == 169.75
    assert got["patient_name"] == "Elizabeth White"
    assert got["payer"] == "Novitas Solutions Medicare Part B"
    assert got["date_of_service"] == "2026-01-18"
    assert got["service_count"] == 3
    assert got["claim_id"] == "PA25896500"


def test_the_11_header_matches_the_remit():
    got = caseinfo.parse(_files("MOH2-000011"))
    assert got["denied"] == 226.17
    assert got["patient_name"] == "Richard Lopez"
    assert got["payer"] == "Keystone Commercial Health"
    assert got["service_count"] == 3


def test_a_partial_payment_yields_the_difference():
    files = {"remit_835.edi": "N1*PR*ACME HEALTH~"
             "CLP*X1*1*100.00*40.00**CI*REF*11*1~"
             "NM1*QC*1*DOE*JANE****MI*M1~"}
    got = caseinfo.parse(files)
    assert (got["billed"], got["paid"], got["denied"]) == (100.0, 40.0, 60.0)
    assert got["patient_name"] == "Jane Doe"


def test_two_claims_in_one_remit_sum():
    files = {"remit_835.edi": "CLP*A*4*50.00*0**CI*R*11*1~CLP*B*4*25.50*0**CI*R*11*1~"}
    assert caseinfo.parse(files)["denied"] == 75.5


def test_a_case_with_no_remit_states_nothing():
    got = caseinfo.parse({"case.md": "# A prose case with no raw segments."})
    assert all(v is None for v in got.values())
    assert caseinfo.parse({}) == got


def test_an_md_rendering_that_embeds_segments_still_parses():
    """The md format quotes the raw lines; the same facts come off them."""
    md = ("# Case\n\n```\nN1*PR*NOVITAS SOLUTIONS MEDICARE PART B~\n"
          "CLP*PA1*4*169.75*0**MB*X*11*1~\nNM1*QC*1*WHITE*ELIZABETH****MI*Z~\n"
          "DTM*232*20260118~\nSVC*HC:97110*77.92*0**2~\n```\n")
    got = caseinfo.parse({"case.md": md})
    assert got["denied"] == 169.75
    assert got["patient_name"] == "Elizabeth White"
    assert got["date_of_service"] == "2026-01-18"


def test_malformed_amounts_do_not_crash_or_invent():
    got = caseinfo.parse({"remit_835.edi": "CLP*X*4*NOTANUMBER*0~NM1*QC*1~"})
    assert got["billed"] is None and got["denied"] is None
    assert got["patient_name"] is None


def test_the_module_is_deterministic_and_offline():
    """No model client, no HTTP, no env reads -- the same rule the other
    deterministic layers live under."""
    src = (REPO / "src" / "mohenara" / "caseinfo.py").read_text()
    for banned in ("resolve", "anthropic", "bedrock", "requests", "httpx",
                   "os.environ", "subprocess"):
        assert banned not in src, f"caseinfo must not touch {banned}"
