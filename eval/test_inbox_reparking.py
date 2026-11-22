"""A case that parks a second time must not vanish. Offline: resolve is stubbed.

The bug: answer() filed every resumed case as resolved, wrote it to
inbox_resolved/ and deleted it from the inbox -- including when the resumed
case had itself come back as awaiting_human. The operator's answer unblocked
one question, the case hit a second one, and the case then disappeared from
the inbox with that second question unasked and unanswerable. Nothing else in
the suite noticed, because the awaiting-human test only ever exercised a case
that resolved on the first answer.
"""
from __future__ import annotations

import json
import pathlib
import sys

import pytest

REPO = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "src"))

from mohenara import store  # noqa: E402
from mohenara.loader import Case  # noqa: E402

CASE = Case("MOH2-900123", "md", "# case text", ("case.md",))


def parked_payload(question: str) -> dict:
    return {
        "schema_version": "1", "case_id": CASE.case_id, "input_format": "md",
        "status": "awaiting_human", "rationale": "need a fact",
        "awaiting_human": {"question": question, "why_needed": "w",
                           "blocks": ["root_cause.family"], "asked_of": "payer"},
        "usage": {"cost_usd": 0.0},
    }


def resolved_payload() -> dict:
    return {
        "schema_version": "1", "case_id": CASE.case_id, "input_format": "md",
        "status": "resolved", "rationale": "done",
        "resolution": {"root_cause": {"family": "none", "explanation": "e"},
                       "next_action": {"path": "none", "detail": "d"},
                       "evidence": [{"artifact": "remit_835.edi", "fact": "f"}]},
        "usage": {"cost_usd": 0.0},
    }


@pytest.fixture(autouse=True)
def isolated_inbox(tmp_path, monkeypatch):
    monkeypatch.setattr(store, "INBOX", tmp_path / "inbox")
    monkeypatch.setattr(store, "RESOLVED", tmp_path / "inbox_resolved")
    return tmp_path


def stub_resolution(monkeypatch, payload, capture=None):
    class R:
        status = payload["status"]
        resolution = payload

    def fake(case, **kw):
        if capture is not None:
            capture.append(kw.get("human_answer"))
        return R()

    monkeypatch.setattr(store._resolve, "resolve_case", fake)


def test_a_case_that_parks_again_stays_in_the_inbox(isolated_inbox, monkeypatch):
    store.park(parked_payload("What is the auth number?"), CASE,
               model="opus-4-6", effort="low")
    stub_resolution(monkeypatch, parked_payload("And what is the filing limit?"))

    store.answer(CASE.case_id, "AUTH-1")

    still = {p.case_id for p in store.list_parked()}
    assert CASE.case_id in still, "the case vanished from the inbox on re-park"
    assert not (isolated_inbox / "inbox_resolved" / f"{CASE.case_id}.json").exists(), (
        "an unresolved case was filed as resolved"
    )
    assert store.get_parked(CASE.case_id).question == "And what is the filing limit?"


def test_the_second_resume_still_carries_the_first_answer(isolated_inbox, monkeypatch):
    store.park(parked_payload("Q1?"), CASE, model="opus-4-6", effort="low")
    stub_resolution(monkeypatch, parked_payload("Q2?"))
    store.answer(CASE.case_id, "A1")

    seen: list = []
    stub_resolution(monkeypatch, resolved_payload(), capture=seen)
    store.answer(CASE.case_id, "A2")

    assert seen, "resolve_case was not called on the second answer"
    replayed = seen[0]
    assert "A1" in replayed and "A2" in replayed, (
        f"the second resume lost the first answer; it saw only: {replayed!r}"
    )
    assert replayed.index("A1") < replayed.index("A2"), "answers replayed out of order"


def test_a_case_that_resolves_still_leaves_the_inbox(isolated_inbox, monkeypatch):
    """The fix must not break the ordinary path."""
    store.park(parked_payload("Q?"), CASE, model="opus-4-6", effort="low")
    stub_resolution(monkeypatch, resolved_payload())
    store.answer(CASE.case_id, "the answer")

    assert store.list_parked() == []
    filed = isolated_inbox / "inbox_resolved" / f"{CASE.case_id}.json"
    assert filed.exists()
    assert json.loads(filed.read_text())["answer"] == "the answer"


def test_an_inbox_file_written_before_answers_existed_still_loads(isolated_inbox):
    """Older parked files carry no `answers` key; they must not crash."""
    inbox = isolated_inbox / "inbox"
    inbox.mkdir(parents=True)
    (inbox / f"{CASE.case_id}.json").write_text(json.dumps({
        "case_id": CASE.case_id, "input_format": "md", "rendered": "x",
        "model": "opus-4-6", "effort": "low",
        "resolution": parked_payload("legacy?"),
    }))
    assert store.get_parked(CASE.case_id).answers == ()
