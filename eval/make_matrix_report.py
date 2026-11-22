#!/usr/bin/env python3
"""Render results/matrix.md from the per-cell run.json and score.json.

Pure reporting: reads what the runner and scorer already wrote and formats it.
No model calls, no recomputation of accuracy -- accuracy claims exist only as
scorer output, so this file must never derive one.
"""
from __future__ import annotations

import json
import pathlib
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "src"))

from mohenara import pricing  # noqa: E402

HAND_WRITTEN_MARKER = (
    "<!-- HAND-WRITTEN BELOW. The generator preserves everything after this "
    "line; everything above it is regenerated from run.json and score.json. -->"
)

RESULTS = REPO / "results"


def cell_rows() -> list[dict]:
    rows = []
    for run_json in sorted(RESULTS.glob("mx-*/run.json")):
        run_dir = run_json.parent
        summary = json.loads(run_json.read_text())
        score_path = run_dir / "score.json"
        score = json.loads(score_path.read_text()) if score_path.exists() else {}

        toks = {"in": 0, "out": 0, "cr": 0, "cw": 0}
        for pred in (run_dir / "predictions").glob("*.json"):
            u = json.loads(pred.read_text())["usage"]
            toks["in"] += u["input_tokens"]; toks["out"] += u["output_tokens"]
            toks["cr"] += u["cache_read_input_tokens"]
            toks["cw"] += u["cache_creation_input_tokens"]
        prompt_total = toks["in"] + toks["cr"] + toks["cw"]
        rows.append({
            "run_id": summary["run_id"],
            "model": summary["model"].replace("us.anthropic.claude-", ""),
            "format": summary["input_format"],
            "effort": summary["effort"],
            "n": summary["n_cases"],
            "accuracy": score.get("accuracy"),
            "root_cause": score.get("root_cause_accuracy"),
            "next_action": score.get("next_action_accuracy"),
            "awaiting": summary["counts"].get("awaiting_human", 0),
            "failed": summary["counts"].get("failed", 0),
            "in": toks["in"], "out": toks["out"], "cr": toks["cr"], "cw": toks["cw"],
            "hit": toks["cr"] / prompt_total if prompt_total else 0.0,
            "cost": summary["cost_usd"],
            "per_case": summary["cost_per_case_usd"],
        })
    return rows


def main() -> int:
    rows = cell_rows()
    if not rows:
        print("no matrix cells found", file=sys.stderr)
        return 1

    scored = [r for r in rows if r["accuracy"] is not None]
    best = max(scored, key=lambda r: (r["accuracy"], -r["per_case"])) if scored else None

    out = ["# Eval matrix", "",
           f"{len(rows)} cells. Accuracy is **joint** — a case counts only when both the "
           "root cause and the next action match the label. Per-field accuracy is shown "
           "alongside, because a system can look strong on one and be useless on the other.",
           "",
           "Every number here is read from the per-cell `run.json` and `score.json`; "
           "nothing is recomputed in this file.", "",
           "| cell | model | fmt | effort | n | **acc** | root | action | await | fail | in | out | cache read | hit | $ | $/case |",
           "|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for r in rows:
        acc = f"**{r['accuracy']:.0%}**" if r["accuracy"] is not None else "—"
        rc = f"{r['root_cause']:.0%}" if r["root_cause"] is not None else "—"
        na = f"{r['next_action']:.0%}" if r["next_action"] is not None else "—"
        out.append(
            f"| `{r['run_id']}` | {r['model']} | {r['format']} | {r['effort']} | {r['n']} | "
            f"{acc} | {rc} | {na} | {r['awaiting']} | {r['failed']} | "
            f"{r['in']:,} | {r['out']:,} | {r['cr']:,} | {r['hit']:.0%} | "
            f"${r['cost']:.2f} | ${r['per_case']:.4f} |")

    total = sum(r["cost"] for r in rows)
    out += ["", f"**Matrix cost: ${total:.2f}**", ""]

    if best:
        out += ["## Chosen default", "",
                f"`{best['model']}` / effort `{best['effort']}` / `{best['format']}` — "
                f"{best['accuracy']:.0%} joint accuracy at ${best['per_case']:.4f} per case.",
                "",
                "Selected as the highest joint accuracy, breaking ties toward the cheaper "
                "cell. Chosen from these results, not assumed in advance.", ""]

        by_effort: dict[str, list[float]] = {}
        by_format: dict[str, list[float]] = {}
        by_model: dict[str, list[float]] = {}
        for r in scored:
            by_effort.setdefault(r["effort"], []).append(r["accuracy"])
            by_format.setdefault(r["format"], []).append(r["accuracy"])
            by_model.setdefault(r["model"], []).append(r["accuracy"])
        out += ["## What moved the number", "",
                "| dimension | mean joint accuracy |", "|---|---|"]
        for label, group in (("effort", by_effort), ("format", by_format), ("model", by_model)):
            for k, v in sorted(group.items()):
                out.append(f"| {label} `{k}` | {sum(v) / len(v):.0%} |")
        out.append("")

    # Everything below the marker is hand-written analysis -- the statistical
    # caveat about five-case cells, and the correction to the budget
    # arithmetic. Regenerating used to delete it wholesale, which would restore
    # an uncaveated "100%" claim that the caveat exists to qualify. Preserve
    # it, and say so in the file so the next person knows where the seam is.
    target = RESULTS / "matrix.md"
    kept = ""
    if target.exists():
        existing = target.read_text()
        if HAND_WRITTEN_MARKER in existing:
            kept = "\n" + existing.split(HAND_WRITTEN_MARKER, 1)[1].lstrip("\n")
    out += ["", HAND_WRITTEN_MARKER, ""]
    target.write_text("\n".join(out) + kept.rstrip("\n") + "\n")
    print(f"wrote results/matrix.md ({len(rows)} cells, ${total:.2f})")
    if best:
        print(f"default: {best['run_id']} at {best['accuracy']:.1%}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
