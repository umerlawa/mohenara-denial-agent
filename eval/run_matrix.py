#!/usr/bin/env python3
"""Run the eval matrix: models x formats x efforts, then score every cell.

Each cell is one `run_eval` invocation plus one `score` invocation. Cells run
sequentially so the prompt cache stays warm across cases within a cell (the
5-minute TTL is the reason a cell is cheap after its first case).

Refuses to start a cell that would cross the provider's eval stop, so an
overrun ends the matrix cleanly with the completed cells intact rather than
half-writing one.

    python eval/run_matrix.py --slice eval/slices/dev25.txt
    python eval/run_matrix.py --slice eval/slices/dev25.txt --dry-run
"""
from __future__ import annotations

import argparse
import json
import pathlib
import subprocess
import sys
import time

REPO = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "src"))

from mohenara import spend  # noqa: E402

MODELS = ["opus-4-6", "sonnet-4-6"]
FORMATS = ["md", "edi"]
# Opus 4.6 / Sonnet 4.6 expose low|medium|high|max. `xhigh` arrived with
# Opus 4.7 and 400s here, so the three tiers are low / high / max.
EFFORTS = ["low", "high", "max"]


def cells() -> list[dict]:
    out = []
    for model in MODELS:
        for fmt in FORMATS:
            for effort in EFFORTS:
                out.append({"model": model, "format": fmt, "effort": effort,
                            "run_id": f"mx-{model}-{fmt}-{effort}"})
    return out


def run_cell(cell: dict, slice_path: pathlib.Path) -> dict:
    run_dir = REPO / "results" / cell["run_id"]
    if (run_dir / "run.json").exists():
        prior = json.loads((run_dir / "run.json").read_text())
        # run.json is written whether or not the cell finished -- the budget
        # gate and a failed case both leave one behind. Treating its presence
        # as "done" published a budget-truncated cell's partial accuracy as a
        # matrix result, forever, because the re-run that would have completed
        # it skipped itself.
        n_expected = len([l for l in slice_path.read_text().splitlines() if l.strip()])
        counts = prior.get("counts", {})
        n_done = sum(counts.get(k, 0) for k in ("resolved", "awaiting_human"))
        if n_done >= n_expected and not prior.get("failures"):
            print(f"  = {cell['run_id']}: already complete ({n_done}/{n_expected}), skipping")
            return prior
        print(f"  ! {cell['run_id']}: INCOMPLETE ({n_done}/{n_expected} cases, "
              f"{len(prior.get('failures', []))} failed) -- re-running with --resume")

    subprocess.run(
        [sys.executable, str(REPO / "eval" / "run_eval.py"),
         "--slice", str(slice_path), "--format", cell["format"],
         "--model", cell["model"], "--effort", cell["effort"],
         "--run-id", cell["run_id"], "--resume"],
        cwd=str(REPO), check=False,
    )
    return json.loads((run_dir / "run.json").read_text())


def score_cell(cell: dict, slice_path: pathlib.Path) -> dict:
    """Score a cell against ITS slice.

    Without --slice the scorer measures 5 predictions against all 140 labels
    and reports ~3%, which is correct arithmetic for a full run and nonsense
    for a cell.
    """
    out = REPO / "results" / cell["run_id"] / "score.json"
    subprocess.run(
        [sys.executable, str(REPO / "eval" / "score.py"),
         "--predictions", str(REPO / "results" / cell["run_id"]),
         "--slice", str(slice_path),
         "--json", str(out), "--quiet"],
        cwd=str(REPO), check=False,
    )
    return json.loads(out.read_text()) if out.exists() else {}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--slice", required=True, type=pathlib.Path)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    plan = cells()
    n_cases = len([l for l in args.slice.read_text().splitlines() if l.strip()])
    print(f"matrix: {len(plan)} cells x {n_cases} cases = {len(plan) * n_cases} case-runs")
    print(f"spend before: {spend.summary()}\n")

    if args.dry_run:
        for c in plan:
            print(f"  {c['run_id']}")
        return 0

    started = time.time()
    for i, cell in enumerate(plan, 1):
        try:
            spend.check_before_call(model_name=cell["model"], is_eval_run=True)
        except spend.BudgetExceeded as exc:
            print(f"\nBUDGET STOP before cell {i}/{len(plan)}: {exc}")
            print("Completed cells are intact; the matrix report covers what ran.")
            break
        print(f"[{i}/{len(plan)}] {cell['run_id']}")
        summary = run_cell(cell, args.slice)
        score = score_cell(cell, args.slice)
        print(f"      accuracy {score.get('accuracy', 0):.1%}  "
              f"cost ${summary.get('cost_usd', 0):.3f}\n")

    print(f"matrix wall time {(time.time() - started) / 60:.1f} min")
    print(f"spend after: {spend.summary()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
