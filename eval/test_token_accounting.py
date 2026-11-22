"""Replay test: recompute every number from the stored raw responses.

An accuracy claim is only as good as its cost claim. This asserts the numbers
in results/ were derived from what the API actually returned, not from
anything the model wrote or the harness assumed.

Runs against whatever run directories exist; skips cleanly when there are
none, so it never blocks a fresh checkout.
"""
from __future__ import annotations

import json
import pathlib
import sys
import tarfile

import pytest

REPO = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "src"))

from mohenara import pricing  # noqa: E402

RESULTS = REPO / "results"


def run_dirs() -> list[pathlib.Path]:
    """Every scored run, whether or not its raw responses have been archived.

    This used to require a `raw/` DIRECTORY, which quietly excluded every run
    that had been through eval/archive_raw.py -- including all twelve matrix
    cells. The suite that exists to prove the published numbers came from real
    API responses was therefore verifying none of the published numbers, and
    it reported that as passing rather than as skipped. Archiving a run is the
    prescribed workflow, so the archive is read here rather than avoided.
    """
    if not RESULTS.is_dir():
        return []
    return [p.parent for p in RESULTS.glob("*/run.json")
            if (p.parent / "raw").is_dir() or (p.parent / "raw.tar.gz").exists()]


def raw_responses(run_dir: pathlib.Path) -> dict[str, dict]:
    """case_id -> raw response, read from raw/ or from raw.tar.gz."""
    out: dict[str, dict] = {}
    live = run_dir / "raw"
    if live.is_dir():
        for path in sorted(live.glob("*.json")):
            out[path.stem] = json.loads(path.read_text())
        return out

    archive = run_dir / "raw.tar.gz"
    if archive.exists():
        with tarfile.open(archive, "r:gz") as tar:
            for member in tar.getmembers():
                if not member.isfile() or not member.name.endswith(".json"):
                    continue
                fh = tar.extractfile(member)
                if fh is None:
                    continue
                out[pathlib.Path(member.name).stem] = json.loads(fh.read().decode())
    return out


@pytest.mark.parametrize("run_dir", run_dirs(), ids=lambda p: p.name)
def test_prediction_usage_matches_raw_response(run_dir: pathlib.Path):
    """Every token count in a prediction must appear in its raw response."""
    checked = 0
    for case_id, raw in sorted(raw_responses(run_dir).items()):
        pred_path = run_dir / "predictions" / f"{case_id}.json"
        if not pred_path.exists():
            continue
        pred = json.loads(pred_path.read_text())
        ru, pu = raw["usage"], pred["usage"]
        for field in ("input_tokens", "output_tokens",
                      "cache_read_input_tokens", "cache_creation_input_tokens"):
            assert int(ru.get(field, 0)) == int(pu[field]), (
                f"{case_id}: {field} disagrees between raw response "
                f"({ru.get(field)}) and prediction ({pu[field]})"
            )
        checked += 1
    assert checked, f"{run_dir.name}: no raw responses could be read"


@pytest.mark.parametrize("run_dir", run_dirs(), ids=lambda p: p.name)
def test_cost_recomputes_from_raw_tokens(run_dir: pathlib.Path):
    """Recompute cost from raw usage against the Bedrock rate card."""
    checked = 0
    for case_id, raw in sorted(raw_responses(run_dir).items()):
        pred_path = run_dir / "predictions" / f"{case_id}.json"
        if not pred_path.exists():
            continue
        pred = json.loads(pred_path.read_text())
        expected = pricing.cost_from_usage(raw["model"], raw["usage"])
        assert abs(expected - pred["usage"]["cost_usd"]) < 1e-9, (
            f"{case_id}: cost {pred['usage']['cost_usd']} does not "
            f"recompute to {expected} from raw tokens"
        )
        checked += 1
    assert checked, f"{run_dir.name}: no raw responses could be read"


@pytest.mark.parametrize("run_dir", run_dirs(), ids=lambda p: p.name)
def test_run_summary_equals_sum_of_cases(run_dir: pathlib.Path):
    summary = json.loads((run_dir / "run.json").read_text())
    total = sum(json.loads(p.read_text())["usage"]["cost_usd"]
                for p in (run_dir / "predictions").glob("*.json"))
    assert abs(total - summary["cost_usd"]) < 1e-6, (
        f"{run_dir.name}: run.json says {summary['cost_usd']}, "
        f"cases sum to {total}"
    )


@pytest.mark.parametrize("run_dir", run_dirs(), ids=lambda p: p.name)
def test_cache_prefix_actually_engages(run_dir: pathlib.Path):
    """A silently broken cacheable prefix is invisible without this check.

    Caching no-ops below the model's minimum prefix with no error, so after
    the first case of a run some later case must show a nonzero cache read.
    """
    reads = [json.loads(p.read_text())["usage"]["cache_read_input_tokens"]
             for p in sorted((run_dir / "predictions").glob("*.json"))]
    if len(reads) < 2:
        pytest.skip("needs at least two cases")
    assert any(r > 0 for r in reads[1:]), (
        "no case after the first read from cache; the stable prefix is not "
        "caching, which silently multiplies cost"
    )


def test_ledger_total_matches_its_entries():
    from mohenara import spend
    ledger = spend.load()
    if not ledger["entries"]:
        pytest.skip("ledger empty")
    total = sum(e["cost_usd"] for e in ledger["entries"])
    assert abs(total - ledger["total_usd"]) < 1e-4, (
        f"ledger total {ledger['total_usd']} != sum of entries {total}"
    )


# --- the frontend leg -------------------------------------------------------
#
# The brief requires the replay to reach the numbers the frontend DISPLAYS, not
# just the ones the harness wrote. That chain has three links:
#
#   raw API response -> prediction file   (tests above)
#   prediction file  -> HTTP API          (tests below, against the internal app)
#   HTTP API         -> rendered DOM      (tests/internal.spec.js)
#
# Without the middle link the chain has a gap exactly where a serialisation bug
# would live: the files could be right, the page could show something else, and
# every test above would still pass.

@pytest.fixture(scope="module")
def client():
    """Against the INTERNAL app, which is where these routes live.

    The customer-facing app deliberately serves no run, spend or cost route --
    that is asserted by the operator Playwright suite. So the API leg of the
    accounting chain is the internal app's, and pointing this at the customer
    app would be asserting the absence of the thing being verified.
    """
    fastapi_testclient = pytest.importorskip("fastapi.testclient")
    from mohenara.internal_api import app
    return fastapi_testclient.TestClient(app)


@pytest.mark.parametrize("run_dir", run_dirs(), ids=lambda p: p.name)
def test_api_serves_the_raw_numbers_unaltered(client, run_dir: pathlib.Path):
    """Per-case usage from the API must equal the raw response, field by field.

    Compared against the RAW response rather than the prediction file, so a bug
    that corrupted both the file and the endpoint identically cannot hide here.
    """
    resp = client.get(f"/api/runs/{run_dir.name}")
    assert resp.status_code == 200, resp.text
    served = {p["case_id"]: p["usage"] for p in resp.json()["predictions"]}

    checked = 0
    for case_id, raw in sorted(raw_responses(run_dir).items()):
        if case_id not in served:
            continue
        ru, su = raw["usage"], served[case_id]
        for field in ("input_tokens", "output_tokens",
                      "cache_read_input_tokens", "cache_creation_input_tokens"):
            assert int(ru.get(field, 0)) == int(su[field]), (
                f"{run_dir.name}/{case_id}: {field} served as {su[field]} but "
                f"the raw response says {ru.get(field)}"
            )
        expected = pricing.cost_from_usage(raw["model"], ru)
        assert abs(expected - su["cost_usd"]) < 1e-9, (
            f"{run_dir.name}/{case_id}: API serves cost {su['cost_usd']}, "
            f"raw tokens recompute to {expected}"
        )
        checked += 1
    assert checked, f"{run_dir.name}: no raw responses could be read"


@pytest.mark.parametrize("run_dir", run_dirs(), ids=lambda p: p.name)
def test_api_run_total_equals_the_persisted_total(client, run_dir: pathlib.Path):
    """Journey 4 asserts the DOM shows this number; assert it is the right one."""
    on_disk = json.loads((run_dir / "run.json").read_text())
    listed = {r["run_id"]: r for r in client.get("/api/runs").json()}
    assert run_dir.name in listed, f"{run_dir.name} missing from /api/runs"
    assert abs(listed[run_dir.name]["cost_usd"] - on_disk["cost_usd"]) < 1e-9


def test_api_spend_matches_the_ledger_per_provider(client):
    """The header must not understate spend, and must not merge the budgets."""
    from mohenara import config, spend

    ledger = spend.load()
    served = {p["name"]: p for p in client.get("/api/spend").json()["providers"]}
    assert set(served) == set(config.provider_names()), (
        "a provider missing from /api/spend is a budget the operator cannot see"
    )
    for name, p in served.items():
        cfg = config.provider(name)
        assert p["refuse_at"] == cfg["budget_usd"]
        assert p["stop_at"] == cfg["stop_eval_usd"]
        recorded = ledger.get("providers", {}).get(name, {}).get("usd", 0.0)
        assert abs(p["usd"] - recorded) < 1e-6, (
            f"{name}: /api/spend shows ${p['usd']}, ledger holds ${recorded}"
        )
