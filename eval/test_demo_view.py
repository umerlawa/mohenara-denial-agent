"""What the demo screen is handed. Offline: seeds a job, calls no model.

`jobs.demo_view` is where the honesty boundary is enforced for the demo
frontend: the browser receives artifacts plus already-anchored annotations, and
has nothing to analyse even if it wanted to. These tests pin the two properties
that matter.

  Before the run finishes there are NO annotations, whatever the job holds.
  After it finishes, annotations exist only for segments the model quoted and
  that were then found verbatim in the artifact.
"""
from __future__ import annotations

import json
import pathlib
import sys

import pytest

REPO = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "src"))

from mohenara import jobs  # noqa: E402

CASE = "MOH2-000029"

GP_LINES = ["SV1*HC:97110*77.92*UN*2***1~",
            "SV1*HC:97112*44.76*UN*1***1~",
            "SV1*HC:97140*47.07*UN*1***1~"]
CLM_BEFORE = "CLM*PA25896500*169.75***11:B:1*Y*A*Y*Y~"
CLM_AFTER = "CLM*PA25896500*169.75***11:B:7*Y*A*Y*Y~"


def prediction() -> dict:
    """A resolution shaped the way the extended schema asks for."""
    return {
        "schema_version": "1.0", "case_id": CASE, "status": "resolved",
        "rationale": "All three lines denied CO-4 + N822: no GP modifier.",
        "usage": {"cost_usd": 0.3, "model": "claude-opus-5", "effort": "high"},
        "resolution": {
            "root_cause": {"family": "missing_therapy_modifier",
                           "explanation": "Therapy CPTs billed without GP."},
            "next_action": {"path": "correct_and_resubmit",
                            "detail": "Append GP to all three lines.",
                            "resubmission_frequency_code": "7"},
            "evidence": [
                {"artifact": "claim_837p.edi", "fact": f"{q} has no GP modifier.",
                 "chip": "Missing GP modifier", "severity": "error",
                 "segments": [{"text": q, "id": "SV1"}]}
                for q in GP_LINES
            ] + [
                {"artifact": "remit_835.edi", "fact": "CO-4 with N822.",
                 "chip": "Payer: missing modifier", "severity": "context",
                 "segments": [{"text": "CAS*CO*4*77.92~"}]},
            ],
            "corrected_claim": {
                "artifact": "claim_837p.edi",
                "edits": [
                    {"before": q, "after": q.replace("HC:", "HC:").replace(
                        "*77.92", ":GP*77.92").replace("*44.76", ":GP*44.76").replace(
                        "*47.07", ":GP*47.07"), "why": "append GP"}
                    for q in GP_LINES
                ] + [{"before": CLM_BEFORE, "after": CLM_AFTER,
                      "why": "frequency code 7 -- replacement claim"}],
            },
        },
    }


@pytest.fixture
def seeded(tmp_path, monkeypatch):
    """A job on disk, without going near the queue's executor or the model."""
    monkeypatch.setattr(jobs, "QUEUE", tmp_path)

    def make(state: str, resolution: dict | None):
        job = {"id": "demo01", "label": CASE, "state": state,
               "input_format": "edi", "case_id": CASE, "notes": None,
               "created_at": "2026-08-20T00:00:00+00:00",
               "updated_at": "2026-08-20T00:00:00+00:00",
               "resolution": resolution, "error": None, "answers": [],
               "_source": {"files": None, "text": None, "case_id": CASE}}
        (tmp_path / "demo01.json").write_text(json.dumps(job))
        return jobs.demo_view("demo01")
    return make


def test_the_artifacts_are_available_before_the_run_finishes(seeded):
    """The left pane fills immediately; that is the whole before/after shot."""
    view = seeded("resolving", None)
    assert "claim_837p.edi" in view["artifacts"]
    assert CLM_BEFORE in view["artifacts"]["claim_837p.edi"]


def test_a_running_job_carries_no_annotations(seeded):
    view = seeded("resolving", None)
    assert view["annotations"]["anchored"] == []
    assert view["corrected"] is None
    assert view["rationale"] is None


def test_annotations_are_withheld_until_the_job_is_terminal(seeded):
    """Even holding a full resolution, a non-terminal job shows nothing.

    Guards against a half-written resolution flashing onto the screen mid-run.
    """
    view = seeded("resolving", prediction())
    assert view["annotations"]["anchored"] == []
    assert view["corrected"] is None


def test_a_resolved_job_anchors_the_three_therapy_lines(seeded):
    view = seeded("resolved", prediction())
    hits = [a for a in view["annotations"]["anchored"]
            if a["artifact"] == "claim_837p.edi" and a["severity"] == "error"]
    assert len(hits) == 3
    assert {h["text"] for h in hits} == set(GP_LINES)
    assert all(h["chip"] == "Missing GP modifier" for h in hits)


def test_the_corrected_claim_carries_frequency_code_7(seeded):
    view = seeded("resolved", prediction())
    c = view["corrected"]
    assert c["artifact"] == "claim_837p.edi"
    assert CLM_AFTER in c["text"]
    assert any("11:B:7" in ch["after"] for ch in c["changed"])
    assert c["dropped"] == []


def test_the_corrected_claim_differs_only_on_the_reported_lines(seeded):
    view = seeded("resolved", prediction())
    c = view["corrected"]
    before = view["artifacts"]["claim_837p.edi"].split("\n")
    after = c["text"].split("\n")
    differing = [i + 1 for i, (a, b) in enumerate(zip(before, after)) if a != b]
    assert differing == sorted(ch["line"] for ch in c["changed"])
    assert len(differing) == 4, "three service lines plus the CLM frequency code"


def test_a_decision_only_resolution_shows_no_corrected_file(seeded):
    """bill_patient produces no claim; the right pane must fall back to a card."""
    pred = prediction()
    pred["resolution"]["next_action"] = {"path": "bill_patient",
                                         "detail": "Bill the patient."}
    pred["resolution"]["corrected_claim"] = None
    view = seeded("resolved", pred)
    assert view["corrected"] is None
    assert view["next_action"]["path"] == "bill_patient"


def test_the_demo_payload_names_no_model(seeded):
    """Same rule as the operator app: the audience learns nothing about the backend."""
    view = seeded("resolved", prediction())
    blob = json.dumps(view).lower()
    for banned in ("opus", "sonnet", "claude", "cost_usd", "effort", "_source"):
        assert banned not in blob, f"the demo view leaks {banned!r}"


def test_an_unknown_job_has_no_view():
    assert jobs.demo_view("nope-does-not-exist") is None


# --- parked cases: partial findings and the verification trail ---------------
#
# A parked case is not an empty one. The model reports what the artifacts DO
# establish in `partial`, the demo anchors those findings exactly like final
# evidence, and after a human answers, the trail pairs each question with the
# answer that unblocked it.

PARKED_SEGMENT = "CAS*CO*4*77.92~"


def parked_prediction() -> dict:
    return {
        "schema_version": "1.0", "case_id": CASE, "status": "awaiting_human",
        "rationale": "Defect signature is settled; the disposition is not.",
        "usage": {"cost_usd": 0.2, "model": "claude-opus-5", "effort": "high"},
        "awaiting_human": {
            "question": "Was a corrected claim already submitted for PA25896500?",
            "why_needed": "A prior corrected submission changes the vehicle.",
            "blocks": ["next_action.path"],
            "asked_of": "provider",
        },
        "partial": {
            "evidence": [
                {"artifact": "remit_835.edi",
                 "fact": "All three lines carry CO-4 with N822.",
                 "chip": "Missing modifier on every line", "severity": "error",
                 "segments": [{"text": PARKED_SEGMENT}]},
                {"artifact": "chart_note.txt",
                 "fact": "PT plan of care documented.",
                 "chip": "Physical therapy confirmed", "severity": "context",
                 "segments": []},
            ],
            "denial": {"group": "CO", "carc": "4", "rarc": "N822", "level": "line"},
        },
    }


def test_a_parked_case_anchors_its_partial_findings(seeded):
    view = seeded("needs_input", parked_prediction())
    hits = view["annotations"]["anchored"]
    assert len(hits) == 1
    assert hits[0]["artifact"] == "remit_835.edi"
    assert hits[0]["text"].strip() == PARKED_SEGMENT
    assert hits[0]["chip"] == "Missing modifier on every line"


def test_a_parked_case_lists_what_it_established(seeded):
    view = seeded("needs_input", parked_prediction())
    found = view["partial_findings"]
    assert [f["chip"] for f in found] == [
        "Missing modifier on every line", "Physical therapy confirmed"]
    assert view["question"].startswith("Was a corrected claim")
    assert view["why_needed"].startswith("A prior corrected")
    assert view["denial"]["carc"] == "4"


def test_partial_findings_are_only_reported_while_parked(seeded):
    """Once resolved, the findings live in resolution.evidence; no duplicates."""
    view = seeded("resolved", prediction())
    assert view["partial_findings"] == []


def test_the_answer_trail_reaches_the_view(seeded, tmp_path):
    pred = prediction()
    view_before = seeded("resolved", pred)
    assert view_before["answers"] == []

    # Same job, now carrying a recorded answer.
    import json as _json
    p = tmp_path / "demo01.json"
    job = _json.loads(p.read_text())
    job["answers"] = [{"question": "Was a corrected claim already submitted?",
                       "answer": "No -- confirmed with the clearinghouse.",
                       "at": "2026-08-20T01:00:00+00:00",
                       "documents": ["clearinghouse-log.md"]}]
    p.write_text(_json.dumps(job))
    view = jobs.demo_view("demo01")
    assert view["answers"][0]["question"].startswith("Was a corrected")
    assert view["answers"][0]["documents"] == ["clearinghouse-log.md"]


def test_a_parked_view_still_leaks_nothing(seeded):
    view = seeded("needs_input", parked_prediction())
    blob = json.dumps(view).lower()
    for banned in ("opus", "sonnet", "claude", "cost_usd", "effort", "_source"):
        assert banned not in blob, f"the parked demo view leaks {banned!r}"


def test_the_assembler_carries_partial_findings_through():
    """The bug a live run found: the model emitted `partial`, the schema
    allowed it, the prompt asked for it -- and _assemble dropped it between
    the structured output and the persisted prediction, because it copies
    fields by hand and nobody taught it the new one."""
    from mohenara.loader import load_case
    from mohenara.resolve import _assemble

    case = load_case(CASE, "edi")
    structured = {
        "status": "awaiting_human", "rationale": "r",
        "awaiting_human": {"question": "q?", "why_needed": "w",
                           "blocks": ["next_action.path"]},
        "partial": {"evidence": [{"artifact": "remit_835.edi", "fact": "f",
                                  "segments": [{"text": "CAS*CO*4*77.92~"}]}]},
    }
    usage = {"input_tokens": 1, "output_tokens": 1,
             "cache_read_input_tokens": 0, "cache_creation_input_tokens": 0}
    doc = _assemble(case, structured, usage, 0.1, "m", "low")
    assert doc["partial"]["evidence"][0]["fact"] == "f", (
        "partial findings dropped by the assembler; the demo's settled-ground "
        "cards render from this field")

    # And a resolved case must NOT grow one (the schema forbids the pair).
    resolved = {"status": "resolved", "rationale": "r",
                "resolution": {"root_cause": {}, "next_action": {}, "evidence": []},
                "partial": {"evidence": [{"artifact": "none", "fact": "x"}]}}
    doc2 = _assemble(case, resolved, usage, 0.1, "m", "low")
    assert "partial" not in doc2


# --- the live stream's two buffers -------------------------------------------

def test_thinking_and_structured_output_stream_into_separate_buffers():
    """The bug a Bedrock shakedown found: a heavier-thinking model streams
    thousands of thinking characters before its structured output starts, and
    with one shared buffer the partial-JSON readers parsed the thinking --
    which can literally draft the schema's key names -- instead of the answer.
    The kinds must land apart, and the extractors must see only the JSON."""
    from mohenara import annotate

    job_id = "stream-kind-test"
    jobs._stream_open(job_id)
    try:
        jobs._stream_append(job_id, 'Drafting {"rationale": "a decoy" now. ',
                            "thinking")
        jobs._stream_append(job_id, '{"status":"resolved","rationale":"the real one',
                            "json")
        s = jobs.stream_state(job_id)
        assert s["text"] == '{"status":"resolved","rationale":"the real one'
        assert "decoy" in s["reasoning"]
        assert annotate.partial_string_field(s["text"], "rationale") == "the real one"
        assert annotate.partial_evidence_items(s["text"]) == []
    finally:
        with jobs._STREAM_LOCK:
            jobs._STREAMS.pop(job_id, None)


def test_a_kindless_append_still_reaches_the_structured_buffer():
    """`kind` defaults to the structured output so an older caller keeps the
    behaviour it had -- the text buffer -- rather than silently losing deltas."""
    job_id = "stream-default-test"
    jobs._stream_open(job_id)
    try:
        jobs._stream_append(job_id, '{"status":')
        assert jobs.stream_state(job_id)["text"] == '{"status":'
        assert jobs.stream_state(job_id)["reasoning"] == ""
    finally:
        with jobs._STREAM_LOCK:
            jobs._STREAMS.pop(job_id, None)


def test_both_stream_buffers_stay_bounded():
    job_id = "stream-bound-test"
    jobs._stream_open(job_id)
    try:
        for kind in ("json", "thinking"):
            jobs._stream_append(job_id, "x" * 250_000, kind)
        s = jobs.stream_state(job_id)
        assert len(s["text"]) == 200_000
        assert len(s["reasoning"]) == 200_000
    finally:
        with jobs._STREAM_LOCK:
            jobs._STREAMS.pop(job_id, None)
