"""Every billed call reaches the ledger, including the ones that failed.

Offline: the Agent SDK turn is stubbed, so nothing here calls an API.

The failure mode this guards is specific and was real. `_run_query` used to
RAISE when a turn failed, and `resolve_case` used to raise before recording
when the model returned no structured output. In both cases the call had
already completed and the tokens had already been billed -- the turn simply
did not finish usefully. The cost was real and the ledger never saw it, which
makes the budget guard understate spend: the one direction it must never fail
in. With retries added on top, a single case could burn three billed turns and
record none of them.
"""
from __future__ import annotations

import pathlib
import sys

import pytest

REPO = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "src"))

from mohenara import resolve, spend  # noqa: E402
from mohenara.loader import Case     # noqa: E402

USAGE = {"input_tokens": 10, "output_tokens": 500,
         "cache_read_input_tokens": 30_000, "cache_creation_input_tokens": 5_000}

CASE = Case("MOH2-900999", "edi", "# a case", ("claim_837p.edi",))


@pytest.fixture(autouse=True)
def isolated_ledger(tmp_path, monkeypatch):
    monkeypatch.setattr(spend, "SPEND_PATH", tmp_path / "spend.json")
    monkeypatch.setattr(spend, "check_before_call", lambda **k: None)
    # record() defaults its path argument at call time, so point it here too.
    real_record = spend.record

    def record(*a, **kw):
        kw.setdefault("path", tmp_path / "spend.json")
        return real_record(*a, **kw)

    monkeypatch.setattr(spend, "record", record)
    monkeypatch.setattr(resolve.spend, "record", record)
    monkeypatch.setattr(resolve.spend, "check_before_call", lambda **k: None)
    return tmp_path / "spend.json"


def stub(monkeypatch, results):
    """Feed _run_query's return values in order; anyio.run calls the thunk."""
    seq = list(results)

    def fake_anyio_run(thunk):
        return seq.pop(0)

    monkeypatch.setattr(resolve.anyio, "run", fake_anyio_run)
    monkeypatch.setattr(resolve.time, "sleep", lambda *_: None)


def test_a_failed_turn_is_still_billed(isolated_ledger, monkeypatch):
    """Three failed turns, three ledger entries -- not zero."""
    stub(monkeypatch, [(None, dict(USAGE), "", "error_max_turns")] * 3)
    with pytest.raises(resolve.ResolutionInvalid):
        resolve.resolve_case(CASE, model="opus-4-6", effort="low", run_id="t")

    ledger = spend.load(isolated_ledger)
    assert len(ledger["entries"]) == 3, (
        "billed-but-failed turns did not reach the ledger; the budget guard "
        f"would understate spend. entries={ledger['entries']}"
    )
    assert ledger["providers"]["bedrock"]["usd"] > 0


def test_no_structured_output_is_still_billed(isolated_ledger, monkeypatch):
    stub(monkeypatch, [(None, dict(USAGE), "prose, not json", None)] * 3)
    with pytest.raises(resolve.ResolutionInvalid):
        resolve.resolve_case(CASE, model="opus-4-6", effort="low", run_id="t")
    assert len(spend.load(isolated_ledger)["entries"]) == 3


def test_a_transport_failure_bills_nothing(isolated_ledger, monkeypatch):
    """No usage came back, so there is genuinely nothing to record."""
    def boom(_):
        raise Exception("Claude Code returned an error result: success")

    monkeypatch.setattr(resolve.anyio, "run", boom)
    monkeypatch.setattr(resolve.time, "sleep", lambda *_: None)
    with pytest.raises(resolve.ResolutionInvalid):
        resolve.resolve_case(CASE, model="opus-4-6", effort="low", run_id="t")
    assert spend.load(isolated_ledger)["entries"] == []


def test_a_retry_that_succeeds_bills_both_turns(isolated_ledger, monkeypatch):
    """The failed first turn was billed too; the ledger must show both."""
    good = {
        "status": "resolved",
        "rationale": "r",
        "resolution": {
            "root_cause": {"family": "none", "explanation": "e"},
            "next_action": {"path": "none", "detail": "d"},
            "evidence": [{"artifact": "remit_835.edi", "fact": "f"}],
        },
    }
    stub(monkeypatch, [
        (None, dict(USAGE), "", "error_max_turns"),
        (good, dict(USAGE), "", None),
    ])
    result = resolve.resolve_case(CASE, model="opus-4-6", effort="low", run_id="t")
    assert result.status == "resolved"
    entries = spend.load(isolated_ledger)["entries"]
    assert len(entries) == 2, (
        f"expected the failed turn AND the successful one in the ledger, got "
        f"{len(entries)}"
    )
