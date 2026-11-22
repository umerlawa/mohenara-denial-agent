#!/usr/bin/env python3
"""Size the comparison subset from the probe's measured usage. Deterministic.

The Bedrock phase made the same mistake twice -- projecting a long run from a
short sample and coming in low both times. So this sizes from the probe's
measured MEAN, then applies the worst-case multiplier that the Bedrock phase
actually observed between a 5-case sample and the full slice (1.33x), rather
than assuming the sample was representative.
"""
from __future__ import annotations

import json
import pathlib
import statistics
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "src"))
from mohenara import config, spend  # noqa: E402

RESULTS = pathlib.Path(__file__).resolve().parent.parent / "results"

# Observed on Bedrock: the full 140-case slice cost 1.33x what the 5-case
# matrix slice predicted, because a minority of cases reason far longer.
SAMPLE_UNDERSTATEMENT = 1.33
TIERS = (25, 15, 10, 5)


def warm_stats(run_id: str) -> tuple[float, float]:
    preds = sorted((RESULTS / run_id / "predictions").glob("*.json"))
    if len(preds) < 2:
        raise SystemExit(f"{run_id}: need at least two cases to separate warm from cold")
    costs = [json.loads(p.read_text())["usage"]["cost_usd"] for p in preds]
    return costs[0], statistics.mean(costs[1:])


def main() -> int:
    stop = config.provider("anthropic")["stop_eval_usd"]
    spent = spend.provider_total("anthropic")
    budget = stop - spent
    print(f"anthropic: ${spent:.2f} spent, ${budget:.2f} to the ${stop:.2f} stop\n")

    per_case = 0.0
    cold = 0.0
    for model in ("opus-5", "sonnet-5"):
        c, w = warm_stats(f"probe-{model}-edi")
        adj = w * SAMPLE_UNDERSTATEMENT
        # Two formats per model, each paying its own cold start.
        per_case += 2 * adj
        cold += 2 * c
        print(f"{model:9} probe cold ${c:.4f}  warm ${w:.4f}  "
              f"adjusted ${adj:.4f} (x{SAMPLE_UNDERSTATEMENT})")

    print(f"\n4 runs: cold ${cold:.2f} + ${per_case:.4f}/case (adjusted)")
    for n in TIERS:
        total = cold + per_case * (n - 1)
        fits = "FITS" if total <= budget else "over"
        print(f"  n={n:3}  ${total:6.2f}   {fits}")
        if total <= budget:
            print(f"\nchoose eval/slices/dev{n}.txt -- ${total:.2f} of ${budget:.2f}")
            return 0
    print("\nno tier fits; report rather than run a comparison that cannot finish")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
