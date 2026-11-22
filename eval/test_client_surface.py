"""Nothing internal reaches the client-facing app. Offline: spends nothing.

The operator app is supposed to be incurious about the model. Removing the
controls from the page is the easy half; the hard half is the payload behind it,
which is one `curl /api/queue` away from anybody watching a demo. Three leaks
have already been found this way and each is pinned below:

  usage       cost_usd, the model id and the effort level rode on every poll,
              because `public()` copied the whole prediction through.
  _source     the entire case text, on every poll, for a list that shows none
              of it.
  error       the raw technical failure. A credentials error reached the
              operator's screen reading "provider 'anthropic' needs
              ['ANTHROPIC_API_KEY'] ... Any tokens these attempts consumed are
              in the ledger."

These are asserted against a constructed job rather than a live one, so the test
fails on the leak itself rather than only when a real denial happens to fail.
"""
from __future__ import annotations

import json
import pathlib
import sys

import pytest

REPO = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "src"))

from mohenara import jobs  # noqa: E402

# Every word that would tell a client something the app is meant not to tell
# them. 'claude' is here for the model id, 'anthropic'/'bedrock' for the vendor.
BANNED = ("opus", "sonnet", "claude", "anthropic", "bedrock", "effort",
          "cost_usd", "cache_read", "cache_creation", "input_tokens", "_source")

JOB = {
    "id": "abc123", "label": "6 artifacts", "state": "failed",
    "case_id": "MOH2-000009", "input_format": "edi",
    "created_at": "2026-08-19T00:00:00+00:00",
    "updated_at": "2026-08-19T00:01:00+00:00",
    "notes": None, "answers": [],
    "_source": {"files": {"835.edi": "ISA*00*...~ the entire artifact"}},
    "error": ("MOH2-000009: 4 attempts all failed; last was RuntimeError: "
              "provider 'anthropic' needs ['ANTHROPIC_API_KEY'] in the "
              "environment; load .env.local first. Any tokens these attempts "
              "consumed are in the ledger."),
    "resolution": {
        "schema_version": "1.0", "case_id": "MOH2-000009", "status": "resolved",
        "rationale": "CO-197 with no auth on the 837P.",
        "resolution": {
            "payer": "NOVITAS", "billed_amount": 240.86,
            "date_of_service": "2026-07-05", "filing_deadline": "2027-07-05",
            "root_cause": {"family": "auth_missing"},
            "next_action": {"path": "appeal_with_documentation"},
        },
        "usage": {"input_tokens": 4, "output_tokens": 1032,
                  "cache_read_input_tokens": 92798, "cost_usd": 0.117,
                  "model": "claude-opus-5", "effort": "high", "calls": 1},
    },
}


def _text(payload) -> str:
    return json.dumps(payload).lower()


@pytest.mark.parametrize("banned", BANNED)
def test_the_queue_payload_carries_nothing_internal(banned):
    assert banned.lower() not in _text(jobs.public(JOB)), (
        f"{banned!r} reaches the operator app through /api/queue")


def test_the_detail_payload_carries_nothing_internal():
    """`full()` is the richer view, so it is the likelier leak of the two."""
    out = dict(JOB)
    for banned in BANNED:
        assert banned.lower() not in _text(jobs.public(out))


def test_the_operator_sees_a_plain_failure_not_a_stack_trace():
    pub = jobs.public(JOB)
    assert pub["error"] == jobs.OPERATOR_FAILURE
    assert "RuntimeError" not in pub["error"]


def test_the_real_error_is_still_kept_on_the_job():
    """Sanitising the view must not destroy the record it was sanitised from."""
    assert "ANTHROPIC_API_KEY" in JOB["error"], "the fixture must keep the raw text"
    assert "RuntimeError" in JOB["error"]
    # public() is a projection, not a mutation: the job it read is untouched.
    jobs.public(JOB)
    assert "RuntimeError" in JOB["error"]


def test_a_job_with_no_error_reports_none():
    ok = {**JOB, "state": "resolved", "error": None}
    assert jobs.public(ok)["error"] is None


def test_the_claim_header_still_reaches_the_operator():
    """The counterpart assertion: stripping must not strip what the app is for."""
    pub = jobs.public(JOB)
    assert pub["payer"] == "NOVITAS"
    assert pub["billed_amount"] == 240.86
    assert pub["date_of_service"] == "2026-07-05"
    assert pub["filing_deadline"] == "2027-07-05"
    assert pub["family"] == "auth_missing"
    assert pub["path"] == "appeal_with_documentation"
    assert pub["resolution"]["rationale"].startswith("CO-197")


def test_the_operator_app_serves_no_internal_route():
    """Route-level, not control-level: an absent view is still one URL away."""
    from mohenara import api

    served = {r.path for r in api.app.routes}
    for internal in ("/api/spend", "/api/runs", "/api/models", "/api/families",
                     "/api/economics", "/api/confusion", "/api/failures"):
        assert internal not in served, f"{internal} must not exist on the operator app"


def test_the_static_page_names_no_model():
    page = (REPO / "src" / "mohenara" / "static" / "index.html").read_text().lower()
    for banned in ("opus", "sonnet", "claude", "effort", "cost_usd"):
        assert banned not in page, f"the operator page mentions {banned!r}"
