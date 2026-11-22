"""The queue's concurrency and its stop button. Offline: no model calls.

Two properties that must both hold at once:

  * Warm cache, parallel work. The prompt's shared prefix is ~90k tokens.
    The first call of a cold batch must run ALONE (one cache write); the
    rest must then run in parallel (cache reads). All-parallel pays the
    write N times; all-serial pays five minutes of wall clock.
  * A cancel stops the spend. A queued job never starts; a running job's
    abort flag stops the retry loop from respawning the call it killed.
"""
from __future__ import annotations

import pathlib
import sys
import threading
import time

import pytest

REPO = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "src"))

from mohenara import jobs  # noqa: E402
from mohenara.resolve import ResolveAborted  # noqa: E402


class _FakeResult:
    status = "resolved"
    resolution = {"status": "resolved", "resolution": {}, "rationale": "r",
                  "case_id": "MOH2-000000", "usage": {}}


@pytest.fixture()
def isolated_queue(tmp_path, monkeypatch):
    monkeypatch.setattr(jobs, "QUEUE", tmp_path / "queue")
    # Each test decides the cache temperature itself.
    monkeypatch.setitem(jobs._LAST_DONE, "t", 0.0)
    return tmp_path / "queue"


def _submit_fakes(monkeypatch, n, fake):
    monkeypatch.setattr(jobs, "resolve_case", fake)
    monkeypatch.setattr(jobs, "_build_case", lambda *a, **k: type(
        "C", (), {"case_id": "MOH2-000000", "rendered": "", "artifacts": []})())
    out = [jobs.submit(label=f"j{i}", input_format="edi",
                       files={"remit_835.edi": "CLP*X*4*1*0~"}) for i in range(n)]
    return out


def _wait_all(ids, want, timeout=10):
    t0 = time.time()
    while time.time() - t0 < timeout:
        states = {i: (jobs._read(i) or {}).get("state") for i in ids}
        if all(s in want for s in states.values()):
            return states
        time.sleep(0.02)
    raise AssertionError(f"timed out; states={states}")


def test_a_cold_batch_warms_solo_then_fans_out(isolated_queue, monkeypatch):
    spans = []
    lock = threading.Lock()

    def fake(case, **kw):
        t0 = time.time()
        time.sleep(0.25)
        with lock:
            spans.append((t0, time.time()))
        return _FakeResult()

    subs = _submit_fakes(monkeypatch, 3, fake)
    _wait_all([s["id"] for s in subs], {"resolved"})
    spans.sort()
    first, rest = spans[0], spans[1:]
    # Nothing overlaps the warm-up call...
    for t0, _ in rest:
        assert t0 >= first[1] - 0.02, (
            "a cold batch must warm the cache with ONE solo call; a second "
            "call started while the first was still writing the prefix")
    # ...and the remainder genuinely ran in parallel.
    assert rest[0][1] > rest[1][0] or rest[1][1] > rest[0][0]
    assert min(r[0] for r in rest) < max(r[1] for r in rest) - 0.25, (
        "the post-warm-up calls ran serially; the pool is not fanning out")


def test_a_warm_batch_runs_parallel_from_the_start(isolated_queue, monkeypatch):
    jobs._LAST_DONE["t"] = time.time()
    spans = []
    lock = threading.Lock()

    def fake(case, **kw):
        t0 = time.time()
        time.sleep(0.25)
        with lock:
            spans.append((t0, time.time()))
        return _FakeResult()

    subs = _submit_fakes(monkeypatch, 3, fake)
    t0 = time.time()
    _wait_all([s["id"] for s in subs], {"resolved"})
    took = time.time() - t0
    assert took < 0.65, f"three warm 0.25s resolves took {took:.2f}s -- serial"


def test_cancelling_a_queued_job_prevents_it_from_starting(isolated_queue, monkeypatch):
    started = []
    gate = threading.Event()

    def fake(case, **kw):
        started.append(kw)
        gate.wait(2)
        return _FakeResult()

    jobs._LAST_DONE["t"] = time.time()
    # Fill every worker so the last job stays queued.
    subs = _submit_fakes(monkeypatch, jobs._POOL._max_workers + 1, fake)
    victim = subs[-1]["id"]
    time.sleep(0.1)
    assert (jobs._read(victim) or {}).get("state") == "queued"
    out = jobs.cancel(victim)
    assert out and out["state"] == "cancelled"
    gate.set()
    _wait_all([s["id"] for s in subs], {"resolved", "cancelled"})
    assert (jobs._read(victim) or {}).get("state") == "cancelled"
    assert len(started) == jobs._POOL._max_workers, (
        "the cancelled job's resolve ran anyway")


def test_an_aborted_resolve_lands_as_cancelled_not_failed(isolated_queue, monkeypatch):
    def fake(case, **kw):
        # What resolve_case does when the kill lands and the flag is set.
        raise ResolveAborted("MOH2-000000: cancelled by the operator")

    subs = _submit_fakes(monkeypatch, 1, fake)
    states = _wait_all([subs[0]["id"]], {"cancelled", "failed"})
    assert list(states.values()) == ["cancelled"], (
        "an operator cancel must not be reported as a failure")
    job = jobs._read(subs[0]["id"])
    assert job.get("error") is None


def test_the_resolver_abort_flag_reads_the_job_state(isolated_queue, monkeypatch):
    seen = {}

    def fake(case, should_abort=None, **kw):
        seen["flag"] = should_abort
        jobs._set(seen["id"], state="cancelling")
        assert should_abort(), "the abort flag must observe the cancelling state"
        raise ResolveAborted("cancelled")

    subs = _submit_fakes(monkeypatch, 1, fake)
    seen["id"] = subs[0]["id"]
    _wait_all([subs[0]["id"]], {"cancelled"})
    assert callable(seen["flag"])


def test_cancelled_jobs_are_cleared_with_the_finished(isolated_queue, monkeypatch):
    def fake(case, **kw):
        raise ResolveAborted("cancelled")

    subs = _submit_fakes(monkeypatch, 1, fake)
    _wait_all([subs[0]["id"]], {"cancelled"})
    assert jobs.clear_finished() == 1
    assert jobs._read(subs[0]["id"]) is None
