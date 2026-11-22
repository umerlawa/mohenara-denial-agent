#!/usr/bin/env bash
# `make verify` from a clean checkout -- the only definition of done.
#
# Clones HEAD into a scratch directory and builds it from nothing but the
# committed tree plus credentials. Running the suites in the working directory
# would not prove this: a file that was never committed, or a stale artifact
# left by an earlier run, would silently hold the suite up.
#
# Credentials are the one thing that cannot come from the checkout, because
# .env.local is gitignored and must stay that way. It is copied in, never
# committed, and never printed.
set -euo pipefail

SRC="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${1:-${TMPDIR:-/tmp}/mohenara-clean-verify}"
LOG="$SRC/results/verify_clean_checkout.log"

# Tee everything. The run log IS a deliverable -- the brief asks for the final
# PR to carry proof the suites were green from a clean checkout -- and a log
# that only exists in a scratch directory does not survive the container.
mkdir -p "$(dirname "$LOG")"
exec > >(tee "$LOG") 2>&1
echo "=== $(date -u +%FT%TZ) log: $LOG"

rm -rf "$DEST"
mkdir -p "$(dirname "$DEST")"

echo "=== $(date -u +%FT%TZ) cloning HEAD ($(git -C "$SRC" rev-parse --short HEAD)) into $DEST"
git -C "$SRC" clone --quiet --no-hardlinks "$SRC" "$DEST"
cd "$DEST"
git log --oneline -1

# Credentials only. Nothing else crosses from the working tree.
install -m 600 "$SRC/.env.local" "$DEST/.env.local"

echo "=== $(date -u +%FT%TZ) building the environment"
python3 -m venv .venv
.venv/bin/pip install -q --upgrade pip
.venv/bin/pip install -q -r requirements.txt

# The image blocks 'playwright install' and ships Chromium already; reuse the
# installed node modules rather than re-fetching them from the network.
cp -r "$SRC/node_modules" "$DEST/node_modules"
cp "$SRC/package.json" "$DEST/package.json" 2>/dev/null || true

# VERIFY_LIVE=0 dry-runs the clone/build/offline path without spending, which
# is how a setup bug gets found before the run that matters.
LIVE="${VERIFY_LIVE:-1}"
echo "=== $(date -u +%FT%TZ) make verify VERIFY_LIVE=$LIVE"
set -a; . ./.env.local; set +a

# The suites below spend real money. Account it to the one real ledger, not to
# the clone's copy -- otherwise this verification quietly spends outside the
# budget it is supposed to be verifying under.
export MOHENARA_SPEND_PATH="$SRC/results/spend.json"
echo "ledger: $MOHENARA_SPEND_PATH"
make verify VERIFY_LIVE="$LIVE"

echo "=== $(date -u +%FT%TZ) clean-checkout verification finished"
