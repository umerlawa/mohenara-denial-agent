#!/usr/bin/env python3
"""Eval runner: run the resolution system over a slice and write results/.

Takes case IDs, an input format, a model, and an effort level; writes one
prediction, one raw response, and one transcript per case, plus a run summary.

This file never opens the answer-label file, and neither does anything it
imports. Scoring is a separate command run against the directory this writes,
which is what makes the leakage test meaningful rather than decorative. The
static guard in eval/test_score.py enforces that separation by rejecting any
mention of the label filename outside the scorer -- including in a docstring,
which is why this paragraph names no file.

    python eval/run_eval.py --slice eval/slices/dev15.txt --format md \
        --model opus --effort high --run-id dev15-opus-high
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys
import time

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "src"))

from mohenara import config, pricing, spend              # noqa: E402
from mohenara.loader import load_case                    # noqa: E402
from mohenara.resolve import (ResolutionInvalid,         # noqa: E402
                              persist, resolve_case)
from mohenara.store import park                          # noqa: E402

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
RESULTS = REPO_ROOT / "results"

# Only these slice sizes may run, so an accidental full-corpus run cannot
# silently spend the budget. Tiering is a guardrail, not a convention.
ALLOWED_SIZES = {5: "matrix", 10: "matrix", 15: "iteration", 25: "milestone", 50: "milestone", 140: "final"}


def read_slice(path: pathlib.Path) -> list[str]:
    return [ln.strip() for ln in path.read_text().splitlines() if ln.strip()]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--slice", required=True, type=pathlib.Path)
    ap.add_argument("--format", required=True, choices=["md", "edi"])
    ap.add_argument("--model", required=True, help="opus | sonnet | full Bedrock id")
    ap.add_argument("--effort", required=True, choices=["low", "medium", "high", "max"])
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--thinking", default="adaptive", choices=["adaptive", "disabled"],
                    help="adaptive thinking is the default; disabled cuts output "
                         "tokens sharply and is worth measuring, not assuming")
    ap.add_argument("--allow-any-size", action="store_true",
                    help="bypass the tier guard (use only for a deliberate probe)")
    ap.add_argument("--limit", type=int, help="stop after N cases")
    ap.add_argument("--resume", action="store_true",
                    help="skip cases already predicted in this run directory. "
                         "A 140-case run that dies at case 90 must not have to "
                         "re-buy those 90 cases from the budget.")
    args = ap.parse_args()

    case_ids = read_slice(args.slice)
    if args.limit:
        case_ids = case_ids[: args.limit]
    if not args.allow_any_size and len(case_ids) not in ALLOWED_SIZES:
        raise SystemExit(
            f"slice size {len(case_ids)} is not a defined tier "
            f"({sorted(ALLOWED_SIZES)}). Pass --allow-any-size to override."
        )

    model = pricing.resolve_model(args.model)
    run_dir = RESULTS / args.run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    print(f"run {args.run_id}: {len(case_ids)} cases | {args.format} | {model} | "
          f"effort={args.effort} | {spend.summary()}")

    started = time.time()
    # Snapshot the ledger so failed-case costs are attributed to THIS run only;
    # a run id can legitimately be reused by a restart.
    ledger_start = spend.entry_count()
    stats = {"resolved": 0, "awaiting_human": 0, "failed": 0}
    failures: list[dict] = []
    cost_total = 0.0
    failed_cost = 0.0

    for n, case_id in enumerate(case_ids, 1):
        try:
            done = run_dir / "predictions" / f"{case_id}.json"
            if args.resume and done.exists():
                prior = json.loads(done.read_text())
                stats[prior["status"]] += 1
                cost_total += prior["usage"]["cost_usd"]
                print(f"  [{n:3}/{len(case_ids)}] {case_id} {prior['status']:14} "
                      f"${prior['usage']['cost_usd']:.4f}  (resumed, not re-run)",
                      flush=True)
                continue
            case = load_case(case_id, args.format)
            result = resolve_case(case, model=model, effort=args.effort,
                                  run_id=args.run_id, is_eval_run=True,
                                  thinking=args.thinking)
            persist(result, run_dir)
            if result.status == "awaiting_human":
                park(result.resolution, case, model=model, effort=args.effort)
            stats[result.status] += 1
            cost_total += result.cost_usd
            hit = result.transcript["cache_hit_rate"]
            print(f"  [{n:3}/{len(case_ids)}] {case_id} {result.status:14} "
                  f"${result.cost_usd:.4f}  cache {hit:5.1%}", flush=True)
        except spend.BudgetExceeded as exc:
            print(f"\nBUDGET STOP after {n - 1} cases: {exc}", flush=True)
            break
        except Exception as exc:                       # noqa: BLE001
            # Deliberately broad, and deliberately AFTER the BudgetExceeded
            # clause above. A 140-case run died at case 18 because a bare
            # Exception out of the SDK was not in this list, so one flaky call
            # threw away the run. A case that fails is recorded as a failure --
            # which the scorer counts as wrong -- and the run continues.
            # KeyboardInterrupt and SystemExit are BaseException and still stop
            # the run, as they should.
            stats["failed"] += 1
            failures.append({"case_id": case_id,
                             "error": f"{type(exc).__name__}: {str(exc)[:500]}"})
            # A failed case usually cost money -- the turn was billed, it just
            # did not finish usefully -- and resolve_case records that in the
            # ledger. Read it back so run.json's cost_usd matches what was
            # actually spent. Summing only successful cases understated every
            # published per-run and per-matrix-cell cost.
            failed_cost += spend.cost_of(run_id=args.run_id, case_id=case_id,
                                         since=ledger_start)
            print(f"  [{n:3}/{len(case_ids)}] {case_id} FAILED "
                  f"{type(exc).__name__}: {str(exc)[:80]}", flush=True)

    summary = {
        "run_id": args.run_id, "model": model, "effort": args.effort,
        "thinking": args.thinking,
        "input_format": args.format, "slice": str(args.slice),
        "n_cases": len(case_ids), "counts": stats,
        "cost_usd": round(cost_total + failed_cost, 6),
        "cost_usd_successful_cases": round(cost_total, 6),
        "cost_usd_failed_cases": round(failed_cost, 6),
        "cost_per_case_usd": round((cost_total + failed_cost) / max(len(case_ids), 1), 6),
        "wall_seconds": round(time.time() - started, 1),
        "provider": config.provider_for(model)["name"],
        "provider_spend_after": spend.provider_total(config.provider_for(model)["name"]),
        "spend_total_after": spend.total(),
        "failures": failures,
    }
    (run_dir / "run.json").write_text(json.dumps(summary, indent=2) + "\n")

    print(f"\n  resolved {stats['resolved']} | awaiting_human "
          f"{stats['awaiting_human']} | failed {stats['failed']}")
    # Report against THIS run's provider. The grand total against a hardcoded
    # $50 misreports an Anthropic run's headroom entirely -- that budget is $9,
    # and the two never mix.
    prov = config.provider_for(model)
    print(f"  run cost ${cost_total + failed_cost:.4f} | "
          f"{prov['name']} ${spend.provider_total(prov['name']):.2f} "
          f"of ${prov['budget_usd']:.2f} (eval stop ${prov['stop_eval_usd']:.2f})")
    print(f"  wrote {run_dir}")
    return 1 if stats["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
