"""Load credentials from the gitignored .env.local, and let them win.

Loaded from `mohenara/__init__.py`, so every entry point -- the eval runner, both
web apps, the preflight tool, the test suites -- resolves credentials the same
way. That uniformity is the point: this module exists because two entry points
disagreed, and the disagreement cost a full Playwright run.

WHY .env.local OVERRIDES THE AMBIENT ENVIRONMENT

The usual convention is the other way round: the real environment wins and a
dotenv only fills gaps. That convention assumes an ambient variable is either
correct or absent. Here it was neither. The execution container injects its own
AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY -- both set to the same placeholder
string -- which are not this project's credentials and cannot sign a Bedrock
request. Every resolve failed with a 403 the CLI reported as "Authentication
error - this may be a temporary network issue, please try again", four retries
deep, while `tools/bedrock_preflight.py` passed on the same models because it
happened to be run from a shell that had sourced .env.local by hand.

A presence check cannot catch that: the placeholder is present. So the file that
holds the project's real credentials takes precedence over whatever the
surrounding environment claims, and the ambient value is ignored rather than
merged.

NOTHING HERE PRINTS A VALUE. The file is gitignored and must never appear in a
committed file, a log, or a PR. `describe()` reports which keys were loaded and
a short hash of each, which is enough to tell two credentials apart without
disclosing either.
"""
from __future__ import annotations

import hashlib
import os
import pathlib
import re

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
ENV_LOCAL = pathlib.Path(os.environ.get("MOHENARA_ENV_FILE") or REPO_ROOT / ".env.local")

# KEY=VALUE, optionally `export`-prefixed, optionally quoted. Comments and blank
# lines are skipped. Deliberately not a full shell parser: a credentials file
# that needs one is a credentials file that should be simplified.
_LINE = re.compile(r"""^\s*(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*?)\s*$""")

_loaded: dict[str, str] = {}


def parse(path: pathlib.Path = ENV_LOCAL) -> dict[str, str]:
    if not path.is_file():
        return {}
    out: dict[str, str] = {}
    for line in path.read_text().splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = _LINE.match(line)
        if not m:
            continue
        key, val = m.group(1), m.group(2)
        if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
            val = val[1:-1]
        out[key] = val
    return out


def load(path: pathlib.Path = ENV_LOCAL) -> dict[str, str]:
    """Put .env.local into os.environ, overriding what is already there."""
    global _loaded
    _loaded = parse(path)
    for key, val in _loaded.items():
        os.environ[key] = val
    return _loaded


def fingerprint(value: str | None) -> str | None:
    """A short hash. Enough to compare two credentials, useless as one."""
    return hashlib.sha256(value.encode()).hexdigest()[:10] if value else None


def describe() -> dict:
    """What was loaded, safe to print. Keys and hashes, never values."""
    return {
        "path": str(ENV_LOCAL),
        "present": ENV_LOCAL.is_file(),
        "keys": sorted(_loaded),
        "fingerprints": {k: fingerprint(v) for k, v in sorted(_loaded.items())},
    }
