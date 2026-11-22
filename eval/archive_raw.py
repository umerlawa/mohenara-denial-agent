#!/usr/bin/env python3
"""Compress each run's raw/ directory into raw.tar.gz once the run is scored.

Raw API responses are the substrate of the token-accounting replay test, so
they are kept -- but one file per case across a 12-cell matrix and a 140-case
final run is thousands of tiny files in git. Archiving keeps the evidence and
keeps the tree navigable.

Refuses to archive a run that has not been scored, and verifies the archive
reads back before deleting anything.

    python eval/archive_raw.py            # every scored run
    python eval/archive_raw.py --check    # report only
"""
from __future__ import annotations

import argparse
import json
import pathlib
import shutil
import tarfile

REPO = pathlib.Path(__file__).resolve().parent.parent
RESULTS = REPO / "results"


def archive(run_dir: pathlib.Path, *, check_only: bool) -> str | None:
    raw = run_dir / "raw"
    if not raw.is_dir() or not any(raw.glob("*.json")):
        return None
    n = len(list(raw.glob("*.json")))
    if not (run_dir / "score.json").exists():
        return f"{run_dir.name}: {n} raw files, NOT scored yet — leaving uncompressed"
    if check_only:
        return f"{run_dir.name}: {n} raw files ready to archive"

    tarball = run_dir / "raw.tar.gz"
    with tarfile.open(tarball, "w:gz") as tf:
        tf.add(raw, arcname="raw")

    # Verify before deleting: an archive that cannot be read back is worse
    # than the loose files it replaced.
    with tarfile.open(tarball, "r:gz") as tf:
        members = [m for m in tf.getmembers() if m.name.endswith(".json")]
        if len(members) != n:
            tarball.unlink(missing_ok=True)
            return f"{run_dir.name}: archive held {len(members)} of {n} — aborted, files kept"
        sample = tf.extractfile(members[0])
        json.loads(sample.read())          # must parse

    shutil.rmtree(raw)
    size = tarball.stat().st_size / 1024
    return f"{run_dir.name}: {n} raw files -> raw.tar.gz ({size:.0f} KB)"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    if not RESULTS.is_dir():
        print("no results/ yet")
        return 0
    for run_json in sorted(RESULTS.glob("*/run.json")):
        msg = archive(run_json.parent, check_only=args.check)
        if msg:
            print(" ", msg)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
