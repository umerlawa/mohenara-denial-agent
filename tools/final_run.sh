#!/usr/bin/env bash
# The final labeled-slice run, at the chosen default configuration.
#
# Sequential and resumable. `--resume` means a run that dies at case 90 costs
# nothing to restart, which is what makes an unattended long run safe against
# the budget rather than merely hopeful.
#
# `edi` runs first: it is the chosen default format, so if the budget cuts the
# phase short there is still a complete result at the default configuration.
set -u -o pipefail
cd "$(dirname "$0")/.."
set -a; . ./.env.local; set +a

MODEL="${MODEL:-opus-4-6}"
EFFORT="${EFFORT:-low}"
SLICE="${SLICE:-eval/slices/full140.txt}"
FORMATS="${FORMATS:-edi md}"

for FMT in $FORMATS; do
  RUN="final-${MODEL}-${EFFORT}-${FMT}"
  echo "=== $(date -u +%FT%TZ) starting $RUN ==="
  .venv/bin/python -u eval/run_eval.py \
      --slice "$SLICE" --format "$FMT" --model "$MODEL" --effort "$EFFORT" \
      --run-id "$RUN" --resume

  echo "=== $(date -u +%FT%TZ) scoring $RUN against the full slice ==="
  # The strict number. Missing counts as wrong, so a run the budget gate cut
  # short scores low here BY CONSTRUCTION -- that is the honest headline and it
  # is not softened.
  .venv/bin/python -u eval/score.py --predictions "results/$RUN" --slice "$SLICE" \
      --json "results/$RUN/score.json"

  # If the gate stopped the run early, also score what it actually attempted.
  # Reported alongside the strict number, never instead of it: one says how the
  # system performed, the other says how much of the slice the budget bought.
  # Built from the slice up to the last case the run reached -- NOT from the
  # prediction files. A case that was attempted and failed writes no
  # prediction, so listing predictions would drop every failure from its own
  # denominator and flatter the run by exactly its failures.
  ATTEMPTED="results/$RUN/attempted.txt"
  .venv/bin/python -u - "$RUN" "$SLICE" "$ATTEMPTED" <<'PYEOF'
import json, pathlib, sys
run, slice_path, out = sys.argv[1], sys.argv[2], sys.argv[3]
ids = [l.strip() for l in pathlib.Path(slice_path).read_text().splitlines() if l.strip()]
done = {p.stem for p in pathlib.Path(f"results/{run}/predictions").glob("*.json")}
rj = pathlib.Path(f"results/{run}/run.json")
failed = set()
if rj.exists():
    failed = {f["case_id"] for f in json.loads(rj.read_text()).get("failures", [])}
reached = done | failed
last = max((i for i, c in enumerate(ids) if c in reached), default=-1)
pathlib.Path(out).write_text("\n".join(ids[: last + 1]) + "\n" if last >= 0 else "")
PYEOF
  if [ "$(wc -l < "$ATTEMPTED")" -lt "$(wc -l < "$SLICE")" ]; then
    echo "=== $(date -u +%FT%TZ) $RUN is PARTIAL: $(wc -l < "$ATTEMPTED") of $(wc -l < "$SLICE") cases"
    echo "=== scoring the attempted subset (reported alongside the strict number, not instead of it)"
    .venv/bin/python -u eval/score.py --predictions "results/$RUN" \
        --slice "$ATTEMPTED" --json "results/$RUN/score_attempted.json"
  else
    rm -f "$ATTEMPTED"
  fi
done

echo "=== $(date -u +%FT%TZ) final run phase complete ==="
.venv/bin/python -c "import sys;sys.path.insert(0,'src');from mohenara import spend;print(spend.summary())"
