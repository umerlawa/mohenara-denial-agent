#!/usr/bin/env bash
# Finish the Bedrock phase with BOTH formats measured.
#
# The environment degraded partway through the edi run -- transient
# "error result: success" bursts, each retry losing the warm cache prefix and
# costing ~3x a normal case. At the observed $0.111/case the full edi slice
# would consume everything left to the $45 stop and md would never run at all.
#
# So md's budget is RESERVED rather than hoped for. edi is stopped at the
# reserve line, md runs on the stratified dev25, and both get scored. One
# complete format and one stratified quarter beats one complete format and no
# evidence at all on the other.
set -u -o pipefail
# REPO_DIR lets this run from a frozen copy outside the repo. Bash reads a
# running script by byte offset, so executing a COPY is what stops an edit to
# the tracked file from corrupting a run already in flight.
cd "${REPO_DIR:-$(dirname "$0")/..}"
set -a; . ./.env.local; set +a

MODEL=opus-4-6
EFFORT=low
FULL=eval/slices/full140.txt
MD_SLICE=eval/slices/dev25.txt
EDI_RUN="final-${MODEL}-${EFFORT}-edi"
MD_RUN="final-${MODEL}-${EFFORT}-md"

MD_RESERVE=3.20        # measured: 25 md cases at ~$0.11 plus one cold start
EVAL_STOP=45.00
EDI_CEILING=$(.venv/bin/python -c "print(f'{$EVAL_STOP - $MD_RESERVE:.2f}')")

spent() { .venv/bin/python -c "import sys;sys.path.insert(0,'src');from mohenara import spend;print(f'{spend.provider_total(\"bedrock\"):.2f}')"; }

echo "=== $(date -u +%FT%TZ) edi ceiling \$$EDI_CEILING, md reserve \$$MD_RESERVE"

# --- watch the in-flight edi run and stop it at the reserve line ------------
while pgrep -f "eval/run_eval.py.*format edi" > /dev/null 2>&1; do
  s=$(spent)
  over=$(.venv/bin/python -c "print(1 if $s >= $EDI_CEILING else 0)")
  if [ "$over" = "1" ]; then
    echo "=== $(date -u +%FT%TZ) edi reached \$$s >= \$$EDI_CEILING -- stopping it to protect md's reserve"
    pkill -f "eval/run_eval.py.*format edi" || true
    sleep 5
    break
  fi
  sleep 30
done
echo "=== $(date -u +%FT%TZ) edi phase done at \$$(spent), $(ls results/$EDI_RUN/predictions 2>/dev/null | wc -l)/140 cases"

echo "=== $(date -u +%FT%TZ) scoring edi against the full slice"
.venv/bin/python -u eval/score.py --predictions "results/$EDI_RUN" --slice "$FULL" \
    --json "results/$EDI_RUN/score.json" || true

# Also score what it actually attempted, reported alongside and never instead.
ls "results/$EDI_RUN/predictions" | sed 's/\.json$//' | sort > "results/$EDI_RUN/attempted.txt"
if [ "$(wc -l < "results/$EDI_RUN/attempted.txt")" -lt 140 ]; then
  echo "=== scoring the attempted subset (alongside the strict number, not instead of it)"
  .venv/bin/python -u eval/score.py --predictions "results/$EDI_RUN" \
      --slice "results/$EDI_RUN/attempted.txt" \
      --json "results/$EDI_RUN/score_attempted.json" || true
fi

# --- md on the stratified quarter-slice ------------------------------------
echo "=== $(date -u +%FT%TZ) md on $(wc -l < "$MD_SLICE") stratified cases"
for pass in 1 2; do
  before=$(ls "results/$MD_RUN/predictions" 2>/dev/null | wc -l)
  .venv/bin/python -u eval/run_eval.py --slice "$MD_SLICE" --format md \
      --model "$MODEL" --effort "$EFFORT" --run-id "$MD_RUN" --resume
  after=$(ls "results/$MD_RUN/predictions" 2>/dev/null | wc -l)
  [ "$after" -ge "$(wc -l < "$MD_SLICE")" ] && break
  [ "$after" -le "$before" ] && { echo "=== no progress on pass $pass; stopping"; break; }
done

echo "=== $(date -u +%FT%TZ) scoring md"
.venv/bin/python -u eval/score.py --predictions "results/$MD_RUN" --slice "$MD_SLICE" \
    --json "results/$MD_RUN/score.json" || true

echo "=== $(date -u +%FT%TZ) Bedrock phase complete"
.venv/bin/python -c "import sys;sys.path.insert(0,'src');from mohenara import spend;print(spend.summary())"
