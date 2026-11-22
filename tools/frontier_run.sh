#!/usr/bin/env bash
# The generation comparison: Opus 5 and Sonnet 5 on the Anthropic API, against
# the Opus 4.6 results on the IDENTICAL subset.
#
# Runs only after the Bedrock phase is finished. This key is for this
# comparison and nothing else; the $9 budget is gated separately in spend.py
# and cannot draw on the Bedrock $50.
#
# Step 1 (probe) measures what these two models actually emit. Step 2 is sized
# from that measurement, not from the 1.3x tokenizer estimate in
# results/frontier_plan.md -- the Bedrock phase already showed twice that
# extrapolating a long run from a short sample understates it.
set -u -o pipefail
cd "$(dirname "$0")/.."
set -a; . ./.env.local; set +a

STEP="${1:-probe}"
EFFORT=low          # pinned: 4.6 has no xhigh, and changing two variables at
                    # once would not say which one moved the number

case "$STEP" in
  probe)
    SLICE=eval/slices/dev5.txt
    FORMATS=edi
    ;;
  compare)
    SLICE="${SLICE:?set SLICE after sizing it from the probe}"
    FORMATS="edi md"
    ;;
  *) echo "usage: $0 [probe|compare]" >&2; exit 2 ;;
esac

for MODEL in opus-5 sonnet-5; do
  for FMT in $FORMATS; do
    RUN="frontier-${MODEL}-${EFFORT}-${FMT}"
    [ "$STEP" = probe ] && RUN="probe-${MODEL}-${FMT}"
    echo "=== $(date -u +%FT%TZ) $RUN ==="
    .venv/bin/python -u eval/run_eval.py \
        --slice "$SLICE" --format "$FMT" --model "$MODEL" --effort "$EFFORT" \
        --run-id "$RUN" --resume
    .venv/bin/python -u eval/score.py --predictions "results/$RUN" \
        --slice "$SLICE" --json "results/$RUN/score.json"
  done
done

echo "=== $(date -u +%FT%TZ) $STEP complete ==="
.venv/bin/python -c "import sys;sys.path.insert(0,'src');from mohenara import spend;print(spend.summary())"
