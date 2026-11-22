#!/usr/bin/env python3
"""Score denial-resolution predictions against eval/dev_labels.jsonl.

This file is the ONLY code in the repo permitted to open dev_labels.jsonl.
It contains no model calls: given the same predictions and labels it returns
the same numbers every time.

Headline metric is JOINT accuracy -- a case counts as correct only when both
the root-cause family and the next-action path match the label. Per-field
accuracy is reported alongside it, because a system can look strong on one
field while being useless on the other.

Scoring decisions that are easy to get wrong, made explicit:

  * A labeled case with no prediction counts as WRONG, not skipped. Skipping
    would let a run inflate its score by answering only the easy cases.
  * A prediction that is malformed, schema-invalid, or still parked in
    awaiting_human counts as WRONG. Each is reported under its own reason so
    a red score can be diagnosed without guessing.
  * Predictions for cases that carry no label are ignored and counted, not
    treated as errors: running a wider slice than the label set is normal.
  * Trap cases score normally on the headline fields but are excluded from
    the line-level metric, per corpus governance.

Usage:
    python eval/score.py --predictions results/<run_id>
    python eval/score.py --predictions results/<run_id> --json report.json
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys
from collections import Counter, defaultdict

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_LABELS = REPO_ROOT / "eval" / "dev_labels.jsonl"
SCHEMA_PATH = REPO_ROOT / "schema" / "resolution.json"

# Why a case failed to score. Ordered most-specific first for reporting.
REASON_MISSING = "missing_prediction"
REASON_UNREADABLE = "unreadable_json"
REASON_SCHEMA = "schema_invalid"
REASON_PARKED = "awaiting_human"
REASON_WRONG_FAMILY = "wrong_root_cause"
REASON_WRONG_PATH = "wrong_next_action"
REASON_WRONG_BOTH = "wrong_both"


def load_labels(path: pathlib.Path) -> dict[str, dict]:
    if not path.exists():
        raise SystemExit(
            f"labels not found: {path}\n"
            "The scorer cannot run without labels. If this is a leakage-test "
            "checkout, that is expected -- the resolution system must still run."
        )
    labels: dict[str, dict] = {}
    for lineno, raw in enumerate(path.read_text().splitlines(), 1):
        if not raw.strip():
            continue
        try:
            row = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"{path}:{lineno}: malformed label JSON: {exc}") from exc
        labels[row["case_id"]] = row
    return labels


def load_validator():
    """Return a callable(obj) -> list[str] of schema errors, or None if unavailable."""
    try:
        import jsonschema
    except ImportError:
        return None
    schema = json.loads(SCHEMA_PATH.read_text())
    validator = jsonschema.Draft202012Validator(schema)
    return lambda obj: [e.message for e in validator.iter_errors(obj)]


def load_predictions(pred_dir: pathlib.Path) -> dict[str, tuple[dict | None, str | None]]:
    """Map case_id -> (parsed prediction, read error).

    Accepts either <dir>/predictions/<CASE>.json or <dir>/<CASE>.json so the
    scorer works against a full run directory or a bare fixture directory.
    """
    if not pred_dir.exists():
        raise SystemExit(f"predictions directory not found: {pred_dir}")
    search = pred_dir / "predictions"
    if not search.is_dir():
        search = pred_dir

    out: dict[str, tuple[dict | None, str | None]] = {}
    for path in sorted(search.glob("*.json")):
        case_id = path.stem
        try:
            out[case_id] = (json.loads(path.read_text()), None)
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            out[case_id] = (None, f"{type(exc).__name__}: {exc}")
    return out


def score_case(label: dict, pred: dict | None, read_error: str | None,
               schema_errors) -> tuple[bool, bool, str | None]:
    """Return (family_correct, path_correct, failure_reason)."""
    if read_error is not None:
        return False, False, REASON_UNREADABLE
    if pred is None:
        return False, False, REASON_MISSING

    if schema_errors is not None:
        errors = schema_errors(pred)
        if errors:
            return False, False, REASON_SCHEMA

    if pred.get("status") != "resolved":
        # Parked cases are legitimate mid-flight states but score as wrong:
        # an unanswered case has not been resolved.
        return False, False, REASON_PARKED

    resolution = pred.get("resolution") or {}
    got_family = (resolution.get("root_cause") or {}).get("family")
    got_path = (resolution.get("next_action") or {}).get("path")

    family_ok = got_family == label["defect"]
    path_ok = got_path == label["correct_path"]

    if family_ok and path_ok:
        return True, True, None
    if not family_ok and not path_ok:
        return False, False, REASON_WRONG_BOTH
    return family_ok, path_ok, REASON_WRONG_FAMILY if not family_ok else REASON_WRONG_PATH


def build_report(labels: dict[str, dict], preds: dict, schema_errors) -> dict:
    per_case = []
    reasons: Counter[str] = Counter()
    by_family: dict[str, Counter] = defaultdict(Counter)
    line_total = line_correct = line_unanswered = 0

    for case_id, label in sorted(labels.items()):
        pred, read_error = preds.get(case_id, (None, None))
        family_ok, path_ok, reason = score_case(label, pred, read_error, schema_errors)
        joint_ok = family_ok and path_ok
        if reason:
            reasons[reason] += 1

        family = label["defect"]
        by_family[family]["total"] += 1
        by_family[family]["correct"] += int(joint_ok)

        # Line-level metric excludes trap cases per corpus governance -- and
        # nothing else. It used to skip any case that did not supply
        # denied_line_idxs, dropping it from numerator AND denominator, which
        # silently turned the metric into "accuracy among cases that answered"
        # and contradicted the missing-counts-as-wrong rule the joint metric
        # follows. A case that parked, failed, or omitted the field now counts
        # in the denominator as wrong, which is what every other number here
        # already does.
        if not label.get("trap"):
            resolution = (pred or {}).get("resolution") or {}
            got_lines = resolution.get("denied_line_idxs")
            line_total += 1
            if got_lines is None:
                line_unanswered += 1
            else:
                line_correct += int(sorted(got_lines) == sorted(label["denied_line_idxs"]))

        per_case.append({
            "case_id": case_id,
            "correct": joint_ok,
            "family_correct": family_ok,
            "path_correct": path_ok,
            "reason": reason,
            "expected_family": label["defect"],
            "expected_path": label["correct_path"],
            # `or {}` on every hop: a prediction carrying an explicit
            # "root_cause": null would otherwise raise AttributeError here and
            # take down the scoring of every OTHER case with it. A malformed
            # prediction must score as wrong, not crash the report.
            "got_family": ((((pred or {}).get("resolution") or {}).get("root_cause") or {})
                           .get("family")),
            "got_path": ((((pred or {}).get("resolution") or {}).get("next_action") or {})
                         .get("path")),
            "trap": bool(label.get("trap")),
        })

    n = len(labels)
    joint = sum(c["correct"] for c in per_case)
    fam = sum(c["family_correct"] for c in per_case)
    path = sum(c["path_correct"] for c in per_case)
    unlabeled = sorted(set(preds) - set(labels))

    return {
        "n_labeled": n,
        "n_predictions": len(preds),
        "n_unlabeled_predictions": len(unlabeled),
        "unlabeled_prediction_ids": unlabeled,
        "accuracy": round(joint / n, 6) if n else 0.0,
        "root_cause_accuracy": round(fam / n, 6) if n else 0.0,
        "next_action_accuracy": round(path / n, 6) if n else 0.0,
        "correct": joint,
        "line_level": {
            "scored": line_total,
            "correct": line_correct,
            "unanswered": line_unanswered,
            "accuracy": round(line_correct / line_total, 6) if line_total else None,
        },
        "failure_reasons": dict(sorted(reasons.items())),
        "by_family": {
            f: {"total": c["total"], "correct": c["correct"],
                "accuracy": round(c["correct"] / c["total"], 6)}
            for f, c in sorted(by_family.items())
        },
        "per_case": per_case,
    }


def render(report: dict, threshold: float) -> str:
    lines = [
        "",
        f"  cases scored        {report['n_labeled']}",
        f"  predictions found   {report['n_predictions']}"
        + (f"  ({report['n_unlabeled_predictions']} unlabeled, ignored)"
           if report["n_unlabeled_predictions"] else ""),
        "",
        f"  ACCURACY (joint)    {report['accuracy']:.1%}  "
        f"({report['correct']}/{report['n_labeled']})",
        f"    root cause        {report['root_cause_accuracy']:.1%}",
        f"    next action       {report['next_action_accuracy']:.1%}",
    ]
    line = report["line_level"]
    if line["accuracy"] is not None:
        unanswered = line.get("unanswered", 0)
        note = f", {unanswered} unanswered" if unanswered else ""
        lines.append(f"    denied lines      {line['accuracy']:.1%}  "
                     f"({line['correct']}/{line['scored']}, traps excluded{note})")
    if report["failure_reasons"]:
        lines += ["", "  failures by reason"]
        for reason, count in sorted(report["failure_reasons"].items(),
                                    key=lambda kv: -kv[1]):
            lines.append(f"    {reason:<22} {count}")
    lines += ["", "  accuracy by defect family"]
    for family, stats in report["by_family"].items():
        lines.append(f"    {family:<28} {stats['accuracy']:6.1%}  "
                     f"({stats['correct']}/{stats['total']})")
    verdict = "PASS" if report["accuracy"] >= threshold else "FAIL"
    lines += ["", f"  {verdict}  threshold {threshold:.0%}", ""]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--predictions", required=True, type=pathlib.Path)
    parser.add_argument("--labels", type=pathlib.Path, default=DEFAULT_LABELS)
    parser.add_argument("--slice", type=pathlib.Path,
                        help="restrict scoring to the case IDs in this file. "
                             "A slice run must be scored against its slice; "
                             "missing-counts-as-wrong still applies WITHIN it, "
                             "so this narrows the denominator without softening "
                             "the rule.")
    parser.add_argument("--json", type=pathlib.Path,
                        help="write the full machine-readable report here")
    parser.add_argument("--threshold", type=float, default=0.85,
                        help="accuracy required for exit status 0 (default 0.85)")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    labels = load_labels(args.labels)
    if args.slice:
        wanted = {ln.strip() for ln in args.slice.read_text().splitlines() if ln.strip()}
        unknown = wanted - set(labels)
        if unknown:
            raise SystemExit(
                f"{args.slice}: {len(unknown)} case(s) have no label, e.g. "
                f"{sorted(unknown)[:3]}"
            )
        labels = {k: v for k, v in labels.items() if k in wanted}
    preds = load_predictions(args.predictions)
    schema_errors = load_validator()
    if schema_errors is None and not args.quiet:
        print("warning: jsonschema not installed; schema validation skipped",
              file=sys.stderr)

    report = build_report(labels, preds, schema_errors)

    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(report, indent=2) + "\n")
    if not args.quiet:
        print(render(report, args.threshold))

    return 0 if report["accuracy"] >= args.threshold else 1


if __name__ == "__main__":
    raise SystemExit(main())
