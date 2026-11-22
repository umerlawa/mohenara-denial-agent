#!/usr/bin/env python3
"""Render a per-case failure analysis from scorer output and transcripts.

Deterministic: formats, never derives. Accuracy figures come from the scorer's
own JSON report and are copied, not recomputed -- an accuracy claim that this
file calculated would be a second, unverified scorer.

The diagnosis for each wrong case is READ from what the system actually
emitted: its stated root cause, its next action, its evidence, its rationale.
The brief is explicit that failures are diagnosed by reading what happened, so
this tool quotes the transcript and does not speculate about causes.

This file never opens the answer key. It only reads the scorer's report, which
already carries the expected values for the cases the scorer judged.

    python eval/make_failure_analysis.py --runs results/final-a results/final-b \
        --out results/failure_analysis.md
"""
from __future__ import annotations

import argparse
import collections
import json
import pathlib


def load(run_dir: pathlib.Path) -> tuple[dict, dict]:
    score = json.loads((run_dir / "score.json").read_text())
    run = json.loads((run_dir / "run.json").read_text())
    return score, run


def prediction(run_dir: pathlib.Path, case_id: str) -> dict | None:
    p = run_dir / "predictions" / f"{case_id}.json"
    return json.loads(p.read_text()) if p.exists() else None


def describe(pred: dict | None) -> tuple[str, str, list[str], str]:
    """What the system said, in its own words."""
    if pred is None:
        return "(no prediction written)", "", [], ""
    if pred.get("status") == "awaiting_human":
        aw = pred.get("awaiting_human") or {}
        return ("parked: awaiting_human", aw.get("question", ""), [],
                pred.get("rationale", ""))
    res = pred.get("resolution") or {}
    rc, na = res.get("root_cause") or {}, res.get("next_action") or {}
    ev = [f"`{e.get('artifact','?')}` {e.get('fact','')}" for e in (res.get("evidence") or [])]
    return (f"{rc.get('family','?')} / {na.get('path','?')}",
            rc.get("explanation", ""), ev, pred.get("rationale", ""))


def section(run_dir: pathlib.Path) -> list[str]:
    score, run = load(run_dir)
    wrong = [c for c in score["per_case"] if not c["correct"]]
    out = [
        f"## `{run_dir.name}`", "",
        f"{run['model']} · effort `{run['effort']}` · format `{run['input_format']}` · "
        f"{score['n_predictions']} predictions against {score['n_labeled']} labeled cases",
        "",
        f"| joint | root cause | next action |", "|---:|---:|---:|",
        f"| **{score['accuracy']:.1%}** | {score['root_cause_accuracy']:.1%} | "
        f"{score['next_action_accuracy']:.1%} |", "",
    ]

    if score.get("failure_reasons"):
        out += ["### Why the wrong ones were wrong", "",
                "| reason | n |", "|---|---:|"]
        for reason, n in sorted(score["failure_reasons"].items(),
                                key=lambda kv: -kv[1]):
            out.append(f"| `{reason}` | {n} |")
        out.append("")

    weak = {f: s for f, s in score.get("by_family", {}).items() if s["accuracy"] < 1.0}
    if weak:
        out += ["### Families that lost cases", "",
                "| family | correct | total | accuracy |", "|---|---:|---:|---:|"]
        for fam, s in sorted(weak.items(), key=lambda kv: kv[1]["accuracy"]):
            out.append(f"| `{fam}` | {s['correct']} | {s['total']} | {s['accuracy']:.0%} |")
        out.append("")

    if not wrong:
        out += ["Every scored case was correct in this run.", ""]
        return out


    # A case with no prediction has no diagnosis to read -- it never produced
    # output. Listing them one by one buries the cases that DID answer and got
    # it wrong, which are the only ones a diagnosis can be written about.
    absent = [c for c in wrong if c["reason"] == "missing_prediction"]
    diagnosable = [c for c in wrong if c["reason"] != "missing_prediction"]
    if absent:
        out += [
            f"### {len(absent)} cases produced no prediction", "",
            "These are not wrong answers. The run did not reach them, or the "
            "call failed after its retries. They count as wrong in the strict "
            "score above -- a missing answer is a missing answer -- but there "
            "is nothing to diagnose, because nothing was written.", "",
            "`" + "`, `".join(c["case_id"] for c in absent[:40]) + "`"
            + (f" … and {len(absent) - 40} more" if len(absent) > 40 else ""), "",
        ]
    if not diagnosable:
        out += ["Every case that produced a prediction was correct.", ""]
        return out

    out += [f"### The {len(diagnosable)} cases that answered and got it wrong", ""]
    for c in diagnosable:
        pred = prediction(run_dir, c["case_id"])
        said, why, evidence, rationale = describe(pred)
        out += [
            f"#### `{c['case_id']}` — `{c['reason']}`", "",
            f"- **expected** `{c['expected_family']}` / `{c['expected_path']}`",
            f"- **said** {said}",
        ]
        if why:
            out.append(f"- **its explanation** {why}")
        if evidence:
            out.append("- **evidence it cited**")
            out += [f"  - {e}" for e in evidence]
        if rationale:
            out.append(f"- **rationale** {rationale}")
        out += [f"- transcript: `{run_dir.name}/transcripts/{c['case_id']}.json`", ""]
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--runs", nargs="+", type=pathlib.Path, required=True)
    ap.add_argument("--out", type=pathlib.Path, required=True)
    ap.add_argument("--preamble", type=pathlib.Path,
                    help="markdown inserted after the header. The interpretation "
                         "of a failure set outlives any single regeneration of "
                         "the tables, so it lives in a file rather than in an "
                         "edit that the next run would overwrite.")
    args = ap.parse_args()

    lines = [
        "# Failure analysis", "",
        "Per-case diagnoses for the runs below. Every accuracy figure is copied "
        "from the scorer's own JSON report; nothing here recomputes one. Each "
        "wrong case is described in the system's own words, read off the "
        "prediction it wrote, because the brief requires failures to be "
        "diagnosed by reading what happened rather than by guessing at it.", "",
        "## How to read a `awaiting_human` failure", "",
        "A parked case scores as wrong: the label space has no value for "
        "\"needs a fact nobody gave me\". Some of those parks are genuine "
        "misses, where a rule in the reference library would have settled the "
        "question from what the artifacts already carry. Others are the system "
        "doing exactly what its cited authority tells it to do, on a question "
        "the corpus expects it to answer anyway.", "",
        "The `ncci_ptp_no59` family is entirely the second kind, and it is the "
        "single largest known gap between what is reported here and what could "
        "be scored by guessing. See `results/notes/corpus-vs-guardrail.md` for "
        "the evidence on both sides and why the guardrail was chosen.", "",
    ]
    if args.preamble:
        lines += [args.preamble.read_text().strip(), ""]
    shared: collections.Counter = collections.Counter()
    for run_dir in args.runs:
        if not (run_dir / "score.json").exists():
            lines += [f"## `{run_dir.name}`", "", "*(not scored)*", ""]
            continue
        lines += section(run_dir)
        score, _ = load(run_dir)
        shared.update(c["case_id"] for c in score["per_case"] if not c["correct"])

    repeated = sorted(c for c, n in shared.items() if n > 1)
    if repeated:
        lines += [
            "## Cases wrong in more than one run", "",
            "A case that fails in every format is a reference or reasoning gap. "
            "A case that fails in only one is a rendering or parsing gap. Only "
            "the first kind is listed here.", "",
        ] + [f"- `{c}`" for c in repeated] + [""]

    args.out.write_text("\n".join(lines))
    print(f"wrote {args.out} ({len(repeated)} cases wrong in more than one run)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
