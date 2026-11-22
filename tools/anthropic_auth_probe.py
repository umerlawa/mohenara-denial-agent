#!/usr/bin/env python3
"""Prove which credential actually serves the Anthropic provider.

Written after $8.96 of 'anthropic' spend turned out never to have touched the
project's API key: the spawned Claude Code CLI carried a managed container's
host credentials and used those. A presence check cannot catch that failure --
the key was present, just ignored -- so this probe tests the negative space:

  step 1  BOGUS KEY MUST FAIL. Run the real resolver pipeline with a
          deliberately invalid ANTHROPIC_API_KEY. If the call succeeds, some
          OTHER credential served it and the isolation (tools/cli_guard.py +
          config subprocess_env_allowlist) has a hole. Spends nothing when
          it behaves -- the API refuses before tokens -- but takes about
          THREE MINUTES: the CLI retries auth errors internally before
          giving up. Patience is part of the probe.

  step 2  REAL KEY IS VALID. GET /v1/models with the configured key. Free --
          no tokens. A 401 here means the key itself is dead, which is a
          different problem from step 1's.

  step 3  ONE MINIMAL BILLED CALL, so usage becomes visible in the Anthropic
          console -- the one place on-box code cannot see. A few tokens,
          roughly a tenth of a cent, gated and recorded like every other call.
          After running this, check the console: if usage appears, billing is
          truthful end to end.

Run it on ANY deployment of this repo -- the managed build container and a
local machine fail in different ways (host-managed OAuth vs a logged-in local
CLI), and both are caught by step 1.

Prints no credential material. Keys are reported as fingerprints only.
"""
from __future__ import annotations

import json
import os
import pathlib
import sys
import urllib.error
import urllib.request

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "src"))

from mohenara import config, env, pricing, spend  # noqa: E402
from mohenara.loader import load_from_text  # noqa: E402
from mohenara.resolve import ResolutionInvalid, resolve_case  # noqa: E402

API = "https://api.anthropic.com"
PROVIDER = "anthropic"
# The cheapest registered model on the provider -- the probe proves billing,
# not capability.
PROBE_MODEL = "sonnet-5"

TINY_CASE = """# Case MOH2-999999 (probe)

## Remittance -- `remit_835.edi`

```
(auth probe -- not a real case; answer with awaiting_human and a one-word question)
```
"""


def _key() -> str:
    val = os.environ.get("ANTHROPIC_API_KEY", "")
    if not val:
        raise SystemExit("no ANTHROPIC_API_KEY; is .env.local present?")
    return val


def _get_models(key: str) -> int:
    req = urllib.request.Request(f"{API}/v1/models", headers={
        "x-api-key": key, "anthropic-version": "2023-06-01"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code


def step1_bogus_key_must_fail() -> bool:
    print("step 1: resolver with a bogus key -- MUST fail with an auth error")
    print("  (the CLI retries auth errors internally; expect ~3 minutes)")
    os.environ["ANTHROPIC_API_KEY"] = "sk-ant-deliberately-invalid-probe-key"
    try:
        case = load_from_text(TINY_CASE, "edi", "MOH2-999999")
        try:
            resolve_case(case, model=PROBE_MODEL, effort="low", run_id="_probe",
                         attempts=1)
        except ResolutionInvalid as exc:
            msg = str(exc)
            authy = any(s in msg.lower() for s in
                        ("401", "auth", "api key", "invalid", "unauthorized"))
            print(f"  failed as required ({'auth-shaped' if authy else 'NOT clearly auth-shaped'}):")
            print(f"    {msg[:180]}")
            if not authy:
                print("  WARNING: the failure does not read as an auth refusal. "
                      "Inspect before trusting the isolation.")
            return True
        print("  *** SUCCEEDED WITH A BOGUS KEY ***")
        print("  Some other credential served this call. The strip list in "
              "config/models.json is incomplete for this machine.")
        return False
    finally:
        env.load()   # restore the real key from .env.local


def step2_real_key_is_valid() -> bool:
    print("step 2: GET /v1/models with the configured key (free)")
    code = _get_models(_key())
    fp = env.fingerprint(_key())
    print(f"  key {fp} -> HTTP {code}")
    return code == 200


def step3_minimal_billed_call() -> None:
    print("step 3: one minimal billed call so the console shows usage")
    spend.check_before_call(model_name=PROBE_MODEL)
    model_id = pricing.resolve_model(PROBE_MODEL)
    body = json.dumps({
        "model": model_id, "max_tokens": 4,
        "messages": [{"role": "user", "content": "Reply with the word ok."}],
    }).encode()
    req = urllib.request.Request(f"{API}/v1/messages", data=body, headers={
        "x-api-key": _key(), "anthropic-version": "2023-06-01",
        "content-type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        out = json.loads(r.read())
    usage = out.get("usage", {})
    cost = pricing.cost_from_usage(model_id, usage)
    spend.record(run_id="_probe", case_id="auth-probe", model=model_id,
                 effort="low", usage=usage, cost=cost)
    print(f"  billed ${cost:.6f} on {PROBE_MODEL} and recorded to the ledger.")
    print("  NOW CHECK THE ANTHROPIC CONSOLE: this call must appear there. "
          "If it does, billing is truthful end to end.")


def main() -> int:
    print(f"deployment ledger: {spend.SPEND_PATH}")
    ok1 = step1_bogus_key_must_fail()
    ok2 = step2_real_key_is_valid()
    if not ok1:
        print("\nverdict: FAIL -- another credential can still serve this provider.")
        return 1
    if not ok2:
        print("\nverdict: FAIL -- the configured key is not valid (expired or revoked).")
        return 1
    step3_minimal_billed_call()
    print("\nverdict: PASS on-box. The console check is the final word.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
