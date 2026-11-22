"""Awaiting-human flow, both directions. No browser.

Feeds a case that cannot be resolved from its artifacts, asserts the system
parks it with a SPECIFIC question, injects an answer through the same
`store.answer()` the frontend calls, and asserts the case resumes and the
final resolution actually uses the injected fact.

Then the inverse, which matters just as much: a case whose artifacts settle
the question must never park. A system that asks about everything is as
useless as one that guesses about everything.

Costs money. Gated behind VERIFY_LIVE=1.
"""
from __future__ import annotations

import os
import pathlib
import sys

import pytest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "src"))

from mohenara import store  # noqa: E402
from mohenara.loader import load_case, load_from_text  # noqa: E402
from mohenara.resolve import resolve_case  # noqa: E402

pytestmark = pytest.mark.skipif(
    os.environ.get("VERIFY_LIVE") != "1",
    reason="calls the API; set VERIFY_LIVE=1 to run",
)

MODEL = os.environ.get("VERIFY_MODEL", "us.anthropic.claude-sonnet-4-6")
EFFORT = os.environ.get("VERIFY_EFFORT", "high")

# A case stripped to the point where the disposition genuinely turns on a fact
# no artifact carries: whether an authorization was ever obtained. The remit
# says "precertification absent"; nothing on file says whether the provider
# actually got one. That is a phone call, not an inference.
NEEDS_HUMAN = """\
# Case MOH2-999001

Patient JORDAN REYES, DOB 1978-02-14. Payer: MERIDIAN HEALTH PLAN.
Service date 2026-05-04.

## Adjudication outcome (835)
Claim MR55512301: status 4 (denied). Billed $1,840.00, paid $0.
Adjustment: CO-197 (precertification/authorization/notification absent) $1,840.00.
Remark: N30.

Service lines:

| # | Procedure | Units | Billed | Paid | Adjustments |
|---|---|---|---|---|---|
| 1 | 29881-RT | 1 | $1840.00 | $0 | CO-197 $1840.00 |

## Claim as billed (837P)
Claim MR55512301, total charge $1840.00, POS 24 (ambulatory surgical center),
frequency 1 (original claim). Diagnosis: M23221.
No prior authorization number is present on the claim.

## Chart note
Arthroscopic medial meniscectomy performed 2026-05-04, right knee.
Pre-operative documentation is not in this record.
"""

# Unambiguous: the 271 shows coverage terminated before the date of service,
# and the remit agrees. Nothing here needs a human.
NEEDS_NO_HUMAN_ID = "MOH2-000009"


def _clean_inbox(case_id: str) -> None:
    (store.INBOX / f"{case_id}.json").unlink(missing_ok=True)
    (store.RESOLVED / f"{case_id}.json").unlink(missing_ok=True)


def test_unresolvable_case_parks_with_a_specific_question():
    case_id = "MOH2-999001"
    _clean_inbox(case_id)
    case = load_from_text(NEEDS_HUMAN, "md", case_id)

    result = resolve_case(case, model=MODEL, effort=EFFORT, run_id="verify-human")
    assert result.status == "awaiting_human", (
        "a case turning on whether an authorization exists must not be guessed; "
        f"got {result.status} with "
        f"{result.resolution.get('resolution', {}).get('root_cause', {})}"
    )

    aw = result.resolution["awaiting_human"]
    question = aw["question"].lower()
    assert len(aw["question"]) > 20, "a one-word question is not answerable"
    # Must name the missing fact, not merely announce that something is missing.
    assert any(w in question for w in ("auth", "precert", "prior approval")), (
        f"question does not name the missing fact: {aw['question']!r}"
    )
    assert aw["blocks"], "must say which field is blocked"

    store.park(result.resolution, case, model=MODEL, effort=EFFORT)
    assert case_id in [p.case_id for p in store.list_parked()]


def test_injected_answer_resumes_the_case_and_is_actually_used():
    case_id = "MOH2-999001"
    parked = [p.case_id for p in store.list_parked()]
    if case_id not in parked:
        pytest.skip("depends on the parking test above")

    # Goes through the same entry point the frontend uses.
    final = store.answer(
        case_id,
        "I called Meridian on 2026-07-02. Authorization AUTH-88213 was approved "
        "on 2026-04-28 for CPT 29881-RT, valid through 2026-06-30. It was simply "
        "omitted from the claim.",
        run_id="verify-human",
    )

    assert final["status"] == "resolved", "case must resume to completion"

    blob = str(final).lower()
    assert "auth-88213" in blob or "88213" in blob, (
        "the final resolution does not use the injected fact"
    )
    artifacts = {e["artifact"] for e in final["resolution"]["evidence"]}
    assert "human_input" in artifacts, (
        f"human answer not recorded in evidence; got {artifacts}"
    )
    assert case_id not in [p.case_id for p in store.list_parked()], (
        "a resumed case must leave the inbox"
    )


def test_resolvable_case_never_parks():
    """The inverse. Without this, 'always ask' would pass the suite."""
    case = load_case(NEEDS_NO_HUMAN_ID, "md")
    result = resolve_case(case, model=MODEL, effort=EFFORT, run_id="verify-human")
    assert result.status == "resolved", (
        f"{NEEDS_NO_HUMAN_ID} is fully determined by its artifacts and must not "
        f"stop to ask: {result.resolution.get('awaiting_human')}"
    )


def test_empty_answer_is_refused():
    with pytest.raises(ValueError):
        store.answer("MOH2-999001", "   ")
