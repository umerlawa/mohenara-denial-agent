"""Fixture tests for the scorer.

The static "only the scorer reads labels" guard lives in eval/test_leakage.py
alongside the runtime leakage test. It was briefly duplicated here, and the two
copies promptly drifted: this file's copy did not know about test_leakage.py
and failed the moment that file was added. One guard, one exclusion list.

Every expected number here was decided when the fixture was written, not read
off a scorer run. That is the point: these tests fail if the scorer's
arithmetic or its failure taxonomy drifts, so an accuracy claim elsewhere in
the repo means something.

Run:  python -m pytest eval/test_score.py -q
"""
from __future__ import annotations

import json
import pathlib
import subprocess
import sys

import pytest

REPO = pathlib.Path(__file__).resolve().parent.parent
FIXTURES = REPO / "eval" / "fixtures"
LABELS = FIXTURES / "labels.jsonl"
SCORER = REPO / "eval" / "score.py"


def run_scorer(pred_dir: str, *extra: str) -> tuple[int, dict]:
    """Invoke the scorer as a subprocess and return (exit_code, report)."""
    out = REPO / "results" / "_test" / f"{pred_dir}.json"
    # Delete first. Otherwise a scorer invocation that crashed would leave the
    # PREVIOUS run's report in place, out.exists() would pass, and the test
    # would assert against numbers this run never produced.
    out.parent.mkdir(parents=True, exist_ok=True)
    out.unlink(missing_ok=True)
    proc = subprocess.run(
        [sys.executable, str(SCORER),
         "--predictions", str(FIXTURES / pred_dir),
         "--labels", str(LABELS),
         "--json", str(out), "--quiet", *extra],
        capture_output=True, text=True,
    )
    assert out.exists(), f"scorer wrote no report\nstdout:{proc.stdout}\nstderr:{proc.stderr}"
    return proc.returncode, json.loads(out.read_text())


# --- headline accuracy on fixtures of known score ---------------------------

@pytest.mark.parametrize("fixture,accuracy,correct", [
    ("perfect",        1.0, 10),
    ("zero",           0.0, 0),
    ("partial",        0.6, 6),
    ("malformed",      0.9, 9),
    ("schema_invalid", 0.9, 9),
    ("missing",        0.7, 7),
])
def test_accuracy_is_reproduced_exactly(fixture, accuracy, correct):
    _, report = run_scorer(fixture)
    assert report["accuracy"] == accuracy
    assert report["correct"] == correct
    assert report["n_labeled"] == 10


# --- the negative control -----------------------------------------------------

def test_negative_control_scores_zero_on_every_metric():
    """Deliberately wrong predictions must score 0, not merely 'low'.

    A scorer that accidentally credits partial matches would still look
    plausible on a real run; this is the test that catches it.
    """
    _, report = run_scorer("zero")
    assert report["accuracy"] == 0.0
    assert report["root_cause_accuracy"] == 0.0
    assert report["next_action_accuracy"] == 0.0
    assert report["correct"] == 0


def test_negative_control_fails_the_threshold():
    code, _ = run_scorer("zero")
    assert code == 1


def test_perfect_run_passes_the_threshold():
    code, _ = run_scorer("perfect")
    assert code == 0


# --- per-field accuracy is tracked separately from joint accuracy -------------

def test_per_field_accuracy_differs_from_joint():
    """partial/ holds one wrong-family, one wrong-path, one wrong-both, one parked.

    Joint 6/10; each field 7/10, since the wrong-family case still has the
    right path and vice versa. If these three collapse to one number, the
    scorer is not measuring what it claims to.
    """
    _, report = run_scorer("partial")
    assert report["accuracy"] == 0.6
    assert report["root_cause_accuracy"] == 0.7
    assert report["next_action_accuracy"] == 0.7


# --- failure taxonomy: a red score must be diagnosable ------------------------

def test_missing_predictions_count_as_wrong_not_skipped():
    """Answering only the easy cases must not raise the score."""
    _, report = run_scorer("missing")
    assert report["failure_reasons"][
        "missing_prediction"] == 3
    assert report["n_labeled"] == 10, "denominator must stay the full label set"


def test_unreadable_json_is_reported_as_its_own_reason():
    _, report = run_scorer("malformed")
    assert report["failure_reasons"]["unreadable_json"] == 1


def test_schema_invalid_prediction_is_rejected():
    """Proves the validator actually rejects: same file, valid JSON, bad enum."""
    _, report = run_scorer("schema_invalid")
    assert report["failure_reasons"]["schema_invalid"] == 1


def test_awaiting_human_scores_wrong_and_is_labelled():
    _, report = run_scorer("partial")
    assert report["failure_reasons"]["awaiting_human"] == 1


def test_wrong_field_reasons_are_distinguished():
    _, report = run_scorer("partial")
    reasons = report["failure_reasons"]
    assert reasons["wrong_root_cause"] == 1
    assert reasons["wrong_next_action"] == 1
    assert reasons["wrong_both"] == 1


# --- determinism ---------------------------------------------------------------

def test_scoring_is_deterministic():
    _, first = run_scorer("partial")
    _, second = run_scorer("partial")
    assert first == second


# --- missing-counts-as-wrong applies to EVERY metric, not just the headline --

def test_line_metric_counts_an_unanswered_case_as_wrong(tmp_path):
    """A case that supplies no denied_line_idxs must stay in the denominator.

    The line metric used to skip such cases entirely, dropping them from
    numerator AND denominator. That quietly redefined it as "accuracy among
    cases that answered" -- so a system that answered one case correctly and
    declined the rest scored 100%. The joint metric has always counted a
    missing answer as wrong; this asserts the line metric does too.
    """
    src = FIXTURES / "perfect"
    stripped = tmp_path / "stripped"
    stripped.mkdir()
    for path in sorted(src.glob("*.json")):
        (stripped / path.name).write_text(path.read_text())

    # Strip denied_line_idxs from every case except the first.
    files = sorted(stripped.glob("*.json"))
    for path in files[1:]:
        pred = json.loads(path.read_text())
        res = pred.get("resolution")
        if isinstance(res, dict):
            res.pop("denied_line_idxs", None)
            path.write_text(json.dumps(pred))

    out = REPO / "results" / "_test" / "line_metric.json"
    proc = subprocess.run(
        [sys.executable, str(SCORER), "--predictions", str(stripped),
         "--labels", str(LABELS), "--json", str(out), "--quiet"],
        capture_output=True, text=True,
    )
    assert out.exists(), proc.stderr[-500:]
    line = json.loads(out.read_text())["line_level"]

    full = run_scorer("perfect")[1]["line_level"]
    assert line["scored"] == full["scored"], (
        "stripping denied_line_idxs shrank the denominator from "
        f"{full['scored']} to {line['scored']}; unanswered cases must still "
        "be counted as wrong"
    )
    assert line["unanswered"] > 0, "the stripped cases were not recorded as unanswered"
    assert line["correct"] < full["correct"], "stripping the field did not lose any credit"
    assert line["accuracy"] < full["accuracy"]


def test_the_schema_covers_every_effort_the_config_advertises():
    """A model advertising an effort the schema rejects fails AFTER the call.

    config/models.json is the registry, and swapping a model is meant to be a
    config change. But the schema validates at WRITE time -- after the API call
    has been paid for -- so an effort level present in the registry and absent
    from the schema means a run that spends money on every case and persists
    none of them. Catching the mismatch here makes it a free test failure
    instead of a paid-for one.
    """
    sys.path.insert(0, str(REPO / "src"))
    from mohenara import config

    schema = json.loads((REPO / "schema" / "resolution.json").read_text())

    def find_effort_enum(node):
        if isinstance(node, dict):
            if "effort" in node.get("properties", {}):
                enum = node["properties"]["effort"].get("enum")
                if enum:
                    return set(enum)
            for v in node.values():
                got = find_effort_enum(v)
                if got:
                    return got
        elif isinstance(node, list):
            for v in node:
                got = find_effort_enum(v)
                if got:
                    return got
        return None

    allowed = find_effort_enum(schema)
    assert allowed, "no effort enum found in schema/resolution.json"

    advertised = {e for name in config.model_names()
                  for e in config.model(name).get("efforts", [])}
    missing = sorted(advertised - allowed)
    assert not missing, (
        f"config/models.json advertises effort levels the schema rejects: "
        f"{missing}. A run at one of these would pay for every case and "
        f"persist none. Schema allows: {sorted(allowed)}"
    )
