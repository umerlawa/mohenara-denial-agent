#!/usr/bin/env python3
"""Render results/frontier_comparison.md. Deterministic: formats, never derives.

Every accuracy figure is copied from a scorer report. Every cost and token
figure is summed from the prediction files' own usage blocks, which the replay
suite already checks against the raw API responses. Nothing here recomputes an
accuracy, because a figure this file calculated would be a second, unverified
scorer.

Two things this report must not do, both of which would make it misleading:

  * Compare raw token counts across the generation boundary. Models from 4.7
    onward use a tokenizer that emits roughly 30% more tokens for the same
    text. A token count that rises 30% is a change of unit, not a regression.
    Tokens are shown per model and explicitly NOT differenced.
  * Merge denominators. A model that covers 11 cases and one that covers 25 do
    not go in the same column.

    python eval/make_frontier_report.py --out results/frontier_comparison.md
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "src"))
RESULTS = REPO / "results"


def load(run_id: str) -> dict | None:
    d = RESULTS / run_id
    score = d / "score.json"
    if not score.exists():
        return None
    s = json.loads(score.read_text())
    usage = [json.loads(p.read_text())["usage"]
             for p in sorted((d / "predictions").glob("*.json"))]
    if not usage:
        return None
    return {
        "run_id": run_id,
        "model": usage[0].get("model", "?"),
        "effort": usage[0].get("effort", "?"),
        "n": s["n_predictions"],
        "n_labeled": s["n_labeled"],
        "accuracy": s["accuracy"],
        "root": s["root_cause_accuracy"],
        "action": s["next_action_accuracy"],
        "parked": s.get("failure_reasons", {}).get("awaiting_human", 0),
        "cost": sum(u["cost_usd"] for u in usage),
        "in_tok": sum(u["input_tokens"] for u in usage),
        "out_tok": sum(u["output_tokens"] for u in usage),
        "cache_read": sum(u["cache_read_input_tokens"] for u in usage),
        "cache_write": sum(u["cache_creation_input_tokens"] for u in usage),
    }


def row(r: dict) -> str:
    per = r["cost"] / max(r["n"], 1)
    hit = r["cache_read"] / max(r["cache_read"] + r["cache_write"], 1)
    return (f"| `{r['model'].split('.')[-1]}` | {r['n']}/{r['n_labeled']} | "
            f"**{r['accuracy']:.0%}** | {r['root']:.0%} | {r['action']:.0%} | "
            f"{r['parked']} | {r['out_tok']:,} | {hit:.0%} | "
            f"${r['cost']:.2f} | ${per:.4f} |")


HEADER = ("| model | n | **acc** | root | action | parked | out tok | cache hit "
          "| $ | $/case |\n|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=pathlib.Path,
                    default=RESULTS / "frontier_comparison.md")
    ap.add_argument("--runs", nargs="+", required=True,
                    help="run ids, grouped as fmt=run_id")
    args = ap.parse_args()

    groups: dict[str, list[dict]] = {}
    for spec in args.runs:
        fmt, _, run_id = spec.partition("=")
        r = load(run_id)
        if r:
            groups.setdefault(fmt, []).append(r)
        else:
            print(f"  (skipping {run_id}: no score.json or no predictions)")

    out = [
        "# Frontier comparison — 4.6 against 5, on identical cases", "",
        "Every accuracy figure is copied from the scorer's own report. Costs and "
        "tokens are summed from the prediction files' usage blocks, which "
        "`eval/test_token_accounting.py` checks against the raw API responses.",
        "",
        "**Token counts are not comparable across the generation boundary.** "
        "Models from 4.7 onward use a tokenizer that emits roughly 30% more "
        "tokens for the same text, so a 30% rise is a change of unit and not a "
        "regression. Tokens are listed per model and deliberately not "
        "differenced. Accuracy and dollars are comparable and are what the "
        "verdict rests on.", "",
    ]
    for fmt in sorted(groups):
        out += [f"## `{fmt}`", "", HEADER]
        out += [row(r) for r in sorted(groups[fmt], key=lambda r: -r["accuracy"])]
        out += [""]
        ns = {r["n"] for r in groups[fmt]}
        if len(ns) > 1:
            out += ["> The `n` column differs between rows here. These are "
                    "**different denominators** and the accuracy percentages are "
                    "not directly comparable; the smaller row is reported on its "
                    "own coverage, not merged into the larger one.", ""]
    args.out.write_text("\n".join(out) + "\n")
    print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
