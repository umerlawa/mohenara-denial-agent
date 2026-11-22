"""The ledger survives two deployments spending on one account. Offline.

results/spend.json was a tracked file AND the file every running server appends
to. Two deployments of this repo therefore edited the same tracked file, and a
`git pull` had to pick a winner: one pull silently dropped a real $0.407045 call
that a demo had already spent. A budget guard whose ledger loses entries to a
merge is not a guard.

The two roles are now separate:

  results/spend_record.json   committed, and never written at runtime
  results/spend.json          gitignored live state, one per deployment,
                              seeded from the record the first time it is needed

Seeding preserves the property the tracked ledger existed for -- a fresh
checkout must not start from $0 and re-spend money the cap has already
accounted for -- without putting a runtime-written file in git.

`tools/merge_ledger.py` reconciles two deployments' ledgers, because both caps
are per-ACCOUNT and the number that matters is the union.
"""
from __future__ import annotations

import importlib
import json
import pathlib
import subprocess
import sys

import pytest

REPO = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "src"))
sys.path.insert(0, str(REPO / "tools"))

from mohenara import spend  # noqa: E402

import merge_ledger  # noqa: E402

USAGE = {"input_tokens": 100, "output_tokens": 10,
         "cache_read_input_tokens": 0, "cache_creation_input_tokens": 0}


def entry(run="r", case="c", provider="bedrock", model="opus-4-6", cost=1.0):
    return {"run_id": run, "case_id": case, "provider": provider, "model": model,
            "effort": "high", "cost_usd": cost, **USAGE}


# --- the record / live-state split ------------------------------------------

def test_the_live_ledger_is_not_tracked_by_git():
    out = subprocess.run(["git", "ls-files", "results/spend.json"], cwd=REPO,
                         capture_output=True, text=True).stdout.strip()
    assert out == "", (
        "results/spend.json is tracked and is also written on every resolve; "
        "that combination is what silently dropped a real call")


def test_the_record_is_tracked_by_git():
    out = subprocess.run(["git", "ls-files", "results/spend_record.json"], cwd=REPO,
                         capture_output=True, text=True).stdout.strip()
    assert out == "results/spend_record.json", "the spend record must be committed"


def test_the_record_is_never_written_at_runtime():
    """Only `make record-spend` may touch it, and it is not on any write path."""
    src = (REPO / "src" / "mohenara" / "spend.py").read_text()
    body = src[src.index("def record("):]
    assert "SPEND_RECORD" not in body, (
        "record() must not write the committed record; that is what made the "
        "tracked ledger conflict on every pull")


def test_a_fresh_checkout_starts_from_the_recorded_spend(tmp_path, monkeypatch):
    """The property the tracked ledger existed for, kept without tracking it."""
    record = {"providers": {"bedrock": {"usd": 45.86, "calls": 657}},
              "total_usd": 45.86, "calls": 657, "by_run": {}, "entries": []}
    rec = tmp_path / "spend_record.json"
    rec.write_text(json.dumps(record))
    live = tmp_path / "spend.json"          # does not exist yet
    monkeypatch.setattr(spend, "SPEND_RECORD", rec)
    monkeypatch.setattr(spend, "DEPLOYMENT_LEDGER", live)

    assert spend.provider_total("bedrock", live) == 45.86, (
        "a deployment with no ledger of its own must inherit the recorded "
        "spend, or its cap reopens a budget that is already spent")


def test_a_temp_ledger_does_not_inherit_the_record(tmp_path, monkeypatch):
    """Tests hand in their own path and must get an empty ledger, not the build's."""
    rec = tmp_path / "spend_record.json"
    rec.write_text(json.dumps({"providers": {"bedrock": {"usd": 45.86, "calls": 1}},
                               "total_usd": 45.86, "calls": 1, "by_run": {},
                               "entries": []}))
    monkeypatch.setattr(spend, "SPEND_RECORD", rec)
    monkeypatch.setattr(spend, "DEPLOYMENT_LEDGER", tmp_path / "deployment.json")

    assert spend.provider_total("bedrock", tmp_path / "somewhere-else.json") == 0.0


def test_seeding_happens_once_and_then_the_live_ledger_owns_the_total(tmp_path, monkeypatch):
    rec = tmp_path / "spend_record.json"
    rec.write_text(json.dumps({"providers": {"bedrock": {"usd": 10.0, "calls": 1}},
                               "total_usd": 10.0, "calls": 1, "by_run": {},
                               "entries": [entry(cost=10.0)]}))
    live = tmp_path / "spend.json"
    monkeypatch.setattr(spend, "SPEND_RECORD", rec)
    monkeypatch.setattr(spend, "DEPLOYMENT_LEDGER", live)

    spend.record(run_id="demo", case_id="x", model="opus-4-6", effort="high",
                 usage=USAGE, cost=2.0, path=live)
    assert spend.provider_total("bedrock", live) == 12.0
    # And the record is untouched by the write.
    assert json.loads(rec.read_text())["total_usd"] == 10.0


# --- reconciling two deployments --------------------------------------------

def test_merging_a_ledger_with_itself_changes_nothing():
    """The normal case. Re-merging must never inflate a total."""
    a = [entry(case="c1"), entry(case="c2", cost=2.0)]
    merged = merge_ledger.rebuild(merge_ledger.merge([a, list(a)]))
    assert merged["calls"] == 2
    assert merged["providers"]["bedrock"]["usd"] == 3.0


def test_merging_recovers_a_call_only_one_side_has():
    """The $0.407045 the pull dropped is exactly this shape."""
    build = [entry(case="c1"), entry(case="c2", cost=2.0)]
    demo = [entry(case="c1"),
            entry(run="ui", case="c9", provider="anthropic", model="opus-5",
                  cost=0.407045)]
    merged = merge_ledger.rebuild(merge_ledger.merge([build, demo]))
    assert merged["calls"] == 3
    assert merged["providers"]["anthropic"]["usd"] == 0.407045
    assert merged["providers"]["bedrock"]["usd"] == 3.0


def test_two_genuinely_identical_calls_in_one_ledger_are_both_kept():
    """Retries of the same case at the same cost are real and must not dedupe away."""
    a = [entry(case="c1"), entry(case="c1")]
    merged = merge_ledger.rebuild(merge_ledger.merge([a, [entry(case="c1")]]))
    assert merged["calls"] == 2, "max multiplicity, not min and not sum"


def test_the_merged_totals_are_recomputed_not_added():
    """Summaries are derived; adding two of them carries over either one's drift."""
    a = {"providers": {"bedrock": {"usd": 999.0, "calls": 999}},
         "entries": [entry(cost=1.0)]}
    merged = merge_ledger.rebuild(merge_ledger.merge([a["entries"]]))
    assert merged["providers"]["bedrock"]["usd"] == 1.0


def test_a_run_spanning_both_providers_is_still_labelled_mixed_after_a_merge():
    entries = [entry(run="queue", case="a"),
               entry(run="queue", case="b", provider="anthropic", model="opus-5")]
    merged = merge_ledger.rebuild(merge_ledger.merge([entries]))
    assert merged["by_run"]["queue"]["provider"] == "mixed"


def test_the_merge_tool_writes_nothing_without_being_asked(tmp_path):
    """A reconciliation that silently overwrites a ledger is its own hazard."""
    a = tmp_path / "a.json"
    a.write_text(json.dumps({"entries": [entry()]}))
    before = a.read_text()
    subprocess.run([sys.executable, str(REPO / "tools" / "merge_ledger.py"),
                    str(a), str(a)], capture_output=True, text=True, check=True)
    assert a.read_text() == before


@pytest.mark.parametrize("target", ["record-spend", "merge-ledger"])
def test_the_makefile_offers_the_reconciliation_targets(target):
    assert f"\n{target}:" in (REPO / "Makefile").read_text()
