#!/usr/bin/env python3
"""Merge two spend ledgers into one, without double-counting.

Two deployments of this repo spend against the same two accounts: the build
session and the local demo clone. Each keeps its own ledger, because a ledger
that lives in git loses entries to merges -- one pull silently dropped a real
$0.407045 call, which is exactly the failure a budget guard exists to prevent.

Keeping them separate is right; leaving them unreconciled is not. Both caps are
per-ACCOUNT, so the number that matters is the union of the two ledgers, and
that is what this produces.

    python tools/merge_ledger.py results/spend_record.json /path/to/other/spend.json
    python tools/merge_ledger.py a.json b.json --out results/spend_record.json

Deduplication is by the full identity of a call -- run, case, model, effort,
cost and all four token counts -- so re-merging the same pair twice is a no-op
and cannot inflate the total. Two genuinely identical calls in one ledger are
preserved: the count of each identity is taken as the MAXIMUM across inputs,
never the sum, because the same call appearing in both files is the normal case
and summing it is precisely the double-count being avoided.

Prints the reconciliation and writes nothing unless --out is given.
"""
from __future__ import annotations

import argparse
import collections
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "src"))

from mohenara import config  # noqa: E402

FIELDS = ("run_id", "case_id", "provider", "model", "effort", "cost_usd",
          "input_tokens", "output_tokens", "cache_read_input_tokens",
          "cache_creation_input_tokens")


def identity(entry: dict) -> tuple:
    return tuple(entry.get(f) for f in FIELDS)


def read(path: pathlib.Path) -> list[dict]:
    if not path.is_file():
        raise SystemExit(f"no such ledger: {path}")
    return json.loads(path.read_text()).get("entries", [])


def merge(ledgers: list[list[dict]]) -> list[dict]:
    """Union by identity, taking the max multiplicity rather than the sum."""
    wanted: collections.Counter = collections.Counter()
    for entries in ledgers:
        counts = collections.Counter(identity(e) for e in entries)
        for ident, n in counts.items():
            wanted[ident] = max(wanted[ident], n)

    out: list[dict] = []
    seen: collections.Counter = collections.Counter()
    for entries in ledgers:
        for e in entries:
            ident = identity(e)
            if seen[ident] < wanted[ident]:
                seen[ident] += 1
                out.append(e)
    return out


def rebuild(entries: list[dict]) -> dict:
    """Recompute every total from the entries, rather than adding two summaries.

    The summary blocks are derived data. Adding them would carry over any
    drift either ledger had; recomputing cannot.
    """
    providers: dict = {}
    by_run: dict = {}
    for e in entries:
        p = providers.setdefault(e["provider"], {"usd": 0.0, "calls": 0})
        p["usd"] = round(p["usd"] + e["cost_usd"], 6)
        p["calls"] += 1
        r = by_run.setdefault(e["run_id"], {"usd": 0.0, "calls": 0, "providers": {}})
        r["usd"] = round(r["usd"] + e["cost_usd"], 6)
        r["calls"] += 1
        rp = r["providers"].setdefault(e["provider"], {"usd": 0.0, "calls": 0})
        rp["usd"] = round(rp["usd"] + e["cost_usd"], 6)
        rp["calls"] += 1
    for r in by_run.values():
        r["provider"] = (next(iter(r["providers"])) if len(r["providers"]) == 1
                         else "mixed")
    return {
        "providers": providers,
        "total_usd": round(sum(p["usd"] for p in providers.values()), 6),
        "calls": sum(p["calls"] for p in providers.values()),
        "by_run": by_run,
        "entries": entries,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ledgers", nargs="+", type=pathlib.Path)
    ap.add_argument("--out", type=pathlib.Path,
                    help="write the merged ledger here (default: report only)")
    args = ap.parse_args()

    inputs = [read(p) for p in args.ledgers]
    for path, entries in zip(args.ledgers, inputs):
        print(f"  {path}: {len(entries)} entries")

    merged = rebuild(merge(inputs))
    print(f"\nmerged: {merged['calls']} calls, "
          f"{sum(len(e) for e in inputs) - merged['calls']} duplicates dropped\n")

    for name in sorted(merged["providers"]):
        spent = merged["providers"][name]["usd"]
        cap = config.committed_provider(name)["budget_usd"]
        flag = "  <-- OVER THE SHIPPED CAP" if spent >= cap else ""
        print(f"  {name:10s} ${spent:8.4f}  of a shipped ${cap:.2f}{flag}")
        for path, entries in zip(args.ledgers, inputs):
            own = sum(e["cost_usd"] for e in entries if e["provider"] == name)
            print(f"      {path.name}: ${own:.4f}")

    if args.out:
        args.out.write_text(json.dumps(merged, indent=2) + "\n")
        print(f"\nwrote {args.out}")
    else:
        print("\nreport only; pass --out to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
