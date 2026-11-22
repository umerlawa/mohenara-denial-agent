"""Work queue for the operator app: many denials in, states out.

A single-shot form could get away with a spinner. A queue cannot: the operator
drops in five denials, walks away, and needs to know on return which ones are
done, which need them, and which failed. So the states are real and are kept on
the server -- a browser refresh must not lose the queue, and two tabs must not
disagree about it.

States, and what each one means to the person watching:

    queued      accepted, not started
    reading     artifacts parsed and rendered
    resolving   the model has the case
    needs_input the system refused to guess and asked a question
    resolved    done
    failed      the call did not survive its retries

Deliberately NOT modelled: progress percentages. A resolve is one API call with
no observable interior, and a bar that advances on a timer is a lie told to
whoever is watching a demo.

Persisted to results/queue/ as one file per job, so the queue survives a restart
and can be read by anything else without going through this process.
"""
from __future__ import annotations

import datetime as _dt
import json
import os
import pathlib
import signal
import threading
import time as _time
import uuid
from concurrent.futures import ThreadPoolExecutor

from . import annotate, config, store
from .loader import load_case, load_from_files, load_from_text
from .resolve import ResolutionInvalid, ResolveAborted, resolve_case

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
QUEUE = REPO_ROOT / "results" / "queue"

STATES = ("queued", "reading", "resolving", "needs_input", "resolved", "failed",
          "cancelling", "cancelled")

_LOCK = threading.Lock()

# Live token stream, per job, in memory only.
#
# Deliberately NOT persisted with the job. It is worth watching while it is
# happening and worth nothing afterwards -- the finished rationale is on the
# resolution. Writing every delta to disk would multiply the queue's write
# volume by the length of the output for a value that expires in seconds.
_STREAMS: dict[str, dict] = {}
_STREAM_LOCK = threading.Lock()


def stream_state(job_id: str) -> dict:
    """What has arrived so far for one job. Empty dict if nothing has."""
    with _STREAM_LOCK:
        s = _STREAMS.get(job_id)
        return dict(s) if s else {}


def _stream_open(job_id: str) -> None:
    with _STREAM_LOCK:
        _STREAMS[job_id] = {"text": "", "reasoning": "", "started": _dt.datetime.now(
            _dt.timezone.utc).timestamp()}


def _stream_append(job_id: str, chunk: str, kind: str = "json") -> None:
    """Two buffers, never mixed. `text` is the structured output as it is
    written; `reasoning` is the model thinking out loud. They must stay apart
    because thinking prose can contain the key names ("rationale",
    "evidence") that the partial-JSON readers anchor on -- one buffer meant a
    heavier-thinking model's draft got parsed instead of its answer."""
    with _STREAM_LOCK:
        s = _STREAMS.get(job_id)
        if s is not None:
            key = "reasoning" if kind == "thinking" else "text"
            # Bounded. A pathological run must not grow a process-lifetime
            # buffer without limit; the tail is what a viewer is reading.
            s[key] = (s[key] + chunk)[-200_000:]


# A small pool, with one deliberate brake. Fully serial cost a five-case batch
# five sequential minutes; fully parallel has two real costs: provider
# throttling (which once killed a run -- the resolver's backoff now absorbs
# it), and a cache-write stampede. The prompt's shared prefix is ~90k tokens;
# the first call of a cold batch WRITES it and everyone after READS it at a
# tenth of the price -- unless they all start together, in which case every
# call pays the write. So: N workers, but the first call after a cold gap runs
# alone (the warm gate below), and the rest fan out against the warm cache.
_POOL = ThreadPoolExecutor(
    max_workers=int(os.environ.get("MOHENARA_RESOLVE_CONCURRENCY", "3")),
    thread_name_prefix="resolve")

# Cache freshness: Anthropic prompt caches live ~5 minutes; treat anything
# older than 4 as cold so the gate errs toward one cheap serial call rather
# than N expensive parallel writes.
_CACHE_FRESH_S = 240
_WARM_GATE = threading.Lock()
_LAST_DONE = {"t": 0.0}


def _with_cache_warmup(call):
    """Run `call`; if the cache looks cold, run it ALONE first.

    Every concurrent job funnels through here. The first one to find the
    cache cold takes the gate and resolves solo -- writing the shared prefix
    once -- while the rest block on the gate, re-check on acquiry, find the
    cache warm, release immediately and fan out in parallel.
    """
    gated = False
    if _time.time() - _LAST_DONE["t"] > _CACHE_FRESH_S:
        _WARM_GATE.acquire()
        gated = True
        if _time.time() - _LAST_DONE["t"] <= _CACHE_FRESH_S:
            _WARM_GATE.release()
            gated = False
    try:
        out = call()
        _LAST_DONE["t"] = _time.time()
        return out
    finally:
        if gated:
            _WARM_GATE.release()


def _now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds")


def _path(job_id: str) -> pathlib.Path:
    return QUEUE / f"{job_id}.json"


def _write(job: dict) -> dict:
    QUEUE.mkdir(parents=True, exist_ok=True)
    tmp = _path(job["id"]).with_suffix(".tmp")
    tmp.write_text(json.dumps(job, indent=2) + "\n")
    tmp.replace(_path(job["id"]))
    return job


def _read(job_id: str) -> dict | None:
    p = _path(job_id)
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text())
    except json.JSONDecodeError:
        return None


def _set(job_id: str, **fields) -> dict | None:
    with _LOCK:
        job = _read(job_id)
        if job is None:
            return None
        job.update(fields, updated_at=_now())
        return _write(job)


def submit(*, label: str, input_format: str, files: dict[str, str] | None = None,
           text: str | None = None, case_id: str | None = None,
           notes: str | None = None) -> dict:
    """Accept one denial and start it. Returns the job immediately."""
    job_id = uuid.uuid4().hex[:12]
    job = {
        "id": job_id,
        "label": label,
        "state": "queued",
        "input_format": input_format,
        "notes": (notes or "").strip() or None,
        "created_at": _now(),
        "updated_at": _now(),
        "case_id": case_id,
        "resolution": None,
        "error": None,
        "answers": [],
        "_source": {"files": files, "text": text, "case_id": case_id},
    }
    _write(job)
    _POOL.submit(_run, job_id)
    return public(job)


def _build_case(src: dict, input_format: str, case_id: str):
    if src.get("files"):
        return load_from_files(src["files"], input_format, case_id or "MOH2-000000")
    if src.get("text"):
        return load_from_text(src["text"], input_format, case_id or "MOH2-000000")
    return load_case(src["case_id"], input_format)


def _pidfile(job_id: str) -> pathlib.Path:
    return QUEUE / f"{job_id}.pid"


def _abort_requested(job_id: str) -> bool:
    return ((_read(job_id) or {}).get("state")) == "cancelling"


def _run(job_id: str) -> None:
    job = _read(job_id)
    if job is None:
        return
    if job["state"] in ("cancelled", "cancelling"):
        # Cancelled while it sat in the queue; never start it.
        _set(job_id, state="cancelled")
        return
    d = config.defaults()
    try:
        _set(job_id, state="reading")
        case = _build_case(job["_source"], job["input_format"], job.get("case_id"))

        # Operator notes ride with the case rather than replacing it. They are
        # context the documents do not carry -- "the payer verbally approved
        # this on the 3rd" -- and are labelled as the operator's so the model
        # can weigh them differently from what the payer actually sent.
        extra = None
        if job.get("notes"):
            extra = f"## Note from the operator\n\n{job['notes']}"

        _set(job_id, state="resolving", case_id=case.case_id)
        _stream_open(job_id)
        result = _with_cache_warmup(lambda: resolve_case(
            case, model=d["model"], effort=d["effort"],
            run_id="queue", human_answer=extra,
            on_delta=lambda c, k: _stream_append(job_id, c, k),
            pidfile=_pidfile(job_id),
            should_abort=lambda: _abort_requested(job_id)))

        if result.status == "awaiting_human":
            store.park(result.resolution, case, model=d["model"], effort=d["effort"])
            _set(job_id, state="needs_input", resolution=result.resolution)
        else:
            _set(job_id, state="resolved", resolution=result.resolution)
    except ResolveAborted:
        _set(job_id, state="cancelled")
    except ResolutionInvalid as exc:
        _set(job_id, state="failed", error=str(exc)[:400])
    except Exception as exc:                                  # noqa: BLE001
        # Broad on purpose: one bad denial must not take the queue with it.
        if _abort_requested(job_id):
            _set(job_id, state="cancelled")
        else:
            _set(job_id, state="failed", error=f"{type(exc).__name__}: {str(exc)[:400]}")
    finally:
        _pidfile(job_id).unlink(missing_ok=True)


def cancel(job_id: str) -> dict | None:
    """Stop one job: a queued one never starts, a running one is killed.

    Killing means SIGTERM to the CLI subprocess (its PID published by
    tools/cli_guard.py just before exec). The resolver sees the dead call as
    a failed attempt, finds the cancel flag before retrying, and raises
    ResolveAborted instead of respawning the spend.
    """
    job = _read(job_id)
    if job is None or job["state"] not in ("queued", "reading", "resolving"):
        return None
    if job["state"] == "queued":
        return public(_set(job_id, state="cancelled"))
    out = _set(job_id, state="cancelling")
    try:
        pid = int(_pidfile(job_id).read_text().strip())
        os.kill(pid, signal.SIGTERM)
    except (OSError, ValueError):
        # No pidfile yet (call not spawned) or already gone: the flag alone
        # stops the next attempt, which is the one that would spend.
        pass
    return public(out)


def cancel_all() -> int:
    """Stop everything still moving. Returns how many jobs were told to stop."""
    n = 0
    for j in listing():
        if j["state"] in ("queued", "reading", "resolving") and cancel(j["id"]):
            n += 1
    return n


def answer(job_id: str, human_answer: str, *,
           files: dict[str, str] | None = None) -> dict | None:
    """Resume a parked job with the operator's answer and any documents."""
    job = _read(job_id)
    if job is None or job["state"] != "needs_input":
        return None
    _set(job_id, state="resolving")
    _POOL.submit(_resume, job_id, human_answer, files)
    return public(_read(job_id))


def _resume(job_id: str, human_answer: str, files: dict[str, str] | None) -> None:
    job = _read(job_id)
    if job is None:
        return
    try:
        # The resume streams like the first pass: the demo's right pane shows
        # the model reworking the case WITH the human's answer, live.
        _stream_open(job_id)
        # Capture the question this answer addressed BEFORE the resume
        # overwrites the resolution -- the verification trail pairs them.
        asked = ((job.get("resolution") or {}).get("awaiting_human") or {}).get("question")
        res = _with_cache_warmup(lambda: store.answer(
            job["case_id"], human_answer, files=files, run_id="queue",
            on_delta=lambda c, k: _stream_append(job_id, c, k)))
        answers = job.get("answers", []) + [{"question": asked,
                                             "answer": human_answer, "at": _now(),
                                             "documents": sorted((files or {}))}]
        if res.get("status") == "awaiting_human":
            _set(job_id, state="needs_input", resolution=res, answers=answers)
        else:
            _set(job_id, state="resolved", resolution=res, answers=answers)
    except Exception as exc:                                  # noqa: BLE001
        _set(job_id, state="failed", error=f"{type(exc).__name__}: {str(exc)[:400]}")


# What the operator is told when a denial fails. The real error -- a throttle,
# a credentials problem, a schema rejection -- stays on the job record on disk
# and in the internal app, because that is where it gets diagnosed. It does not
# go on the operator's screen: the first version of this app put the raw text
# there and a client demo would have read "4 attempts all failed; last was
# RuntimeError: provider 'anthropic' needs ['ANTHROPIC_API_KEY']... Any tokens
# these attempts consumed are in the ledger."
OPERATOR_FAILURE = ("This denial could not be resolved and has been logged for "
                    "review. Nothing was submitted to the payer.")


def client_safe(prediction: dict | None) -> dict | None:
    """A prediction with the accounting record removed.

    `usage` carries cost_usd, the model id and the effort level. The operator
    app is deliberately incurious about all three, but stripping the controls
    from the page while the JSON still answers the question is not privacy --
    it is one `curl /api/queue` away from a client demo showing the model name
    and the per-denial cost. The record itself is not lost: the spend ledger and
    the parked-case store both keep it, on the server, where it belongs.
    """
    if not prediction:
        return prediction
    return {k: v for k, v in prediction.items() if k != "usage"}


def public(job: dict) -> dict:
    """The job without its source documents or its accounting record.

    `_source` holds the entire case text, which is large and which the queue
    view never needs. Sending it on every poll would make the list heavy for no
    benefit.
    """
    out = {k: v for k, v in job.items() if k != "_source"}
    out["resolution"] = client_safe(job.get("resolution"))
    out["error"] = OPERATOR_FAILURE if job.get("error") else None
    res = (job.get("resolution") or {}).get("resolution") or {}
    out["payer"] = res.get("payer")
    out["billed_amount"] = res.get("billed_amount")
    out["date_of_service"] = res.get("date_of_service")
    out["filing_deadline"] = res.get("filing_deadline")
    out["family"] = (res.get("root_cause") or {}).get("family")
    out["path"] = (res.get("next_action") or {}).get("path")
    aw = (job.get("resolution") or {}).get("awaiting_human") or {}
    out["question"] = aw.get("question")
    out["asked_of"] = aw.get("asked_of")
    return out


def demo_view(job_id: str) -> dict | None:
    """Everything the demo screen renders, assembled server-side.

    The artifacts, the anchored annotations, and the corrected claim all come
    from here rather than being worked out in the browser. That is not a
    convenience -- it is the honesty boundary. `annotate` matches the model's
    own quotations against the artifact bytes, so the view cannot highlight a
    line the model never cited, and the frontend has nothing to analyse with
    even if it wanted to.

    Before the run finishes there are simply no annotations, because there are
    no findings yet. The input renders plain.
    """
    job = _read(job_id)
    if job is None:
        return None

    case = None
    try:
        case = _build_case(job["_source"], job["input_format"], job.get("case_id"))
    except Exception:                                         # noqa: BLE001
        # A case that will not build has already failed the job; the view still
        # renders, with no artifacts and whatever error state the job carries.
        pass

    artifacts = annotate.artifacts_from_rendered(case.rendered) if case else {}
    prediction = job.get("resolution") or {}
    resolution = prediction.get("resolution") or {}
    partial = prediction.get("partial") or {}
    terminal = job["state"] in ("resolved", "needs_input", "failed", "cancelled")

    # A parked case anchors its PARTIAL findings -- what the model established
    # before it had to stop and ask. Same annotator, same rule: only segments
    # the model quoted, matched against the artifact bytes.
    findings_source = resolution if resolution.get("evidence") else partial
    marks = (annotate.annotations(findings_source, artifacts)
             if terminal else {"anchored": [], "unanchored": []})
    corrected = (annotate.apply_corrections(resolution.get("corrected_claim"), artifacts)
                 if terminal else None)

    aw = prediction.get("awaiting_human") or {}
    pub = public(job)
    return {
        "job": pub,
        "artifacts": artifacts,
        "annotations": marks,
        "corrected": corrected,
        "rationale": prediction.get("rationale") if terminal else None,
        "root_cause": resolution.get("root_cause"),
        "next_action": resolution.get("next_action"),
        "denial": resolution.get("denial") or partial.get("denial"),
        # What the parked case DID establish, for the "settled ground" cards.
        "partial_findings": [
            {"fact": e.get("fact"), "chip": e.get("chip"),
             "severity": e.get("severity"), "artifact": e.get("artifact")}
            for e in (partial.get("evidence") or [])
        ] if job["state"] == "needs_input" else [],
        "question": pub.get("question"),
        "why_needed": aw.get("why_needed"),
        "asked_of": aw.get("asked_of"),
        # The verification trail: every question this case asked and every
        # answer a human gave, with the documents they attached.
        "answers": job.get("answers") or [],
    }


def get(job_id: str) -> dict | None:
    job = _read(job_id)
    return public(job) if job else None


def full(job_id: str) -> dict | None:
    """Including the rendered case, for the detail view."""
    job = _read(job_id)
    if job is None:
        return None
    out = public(job)
    out["has_source"] = bool(job.get("_source"))
    return out


def listing() -> list[dict]:
    if not QUEUE.is_dir():
        return []
    jobs = []
    for p in QUEUE.glob("*.json"):
        try:
            jobs.append(public(json.loads(p.read_text())))
        except json.JSONDecodeError:
            continue
    return sorted(jobs, key=lambda j: j["created_at"], reverse=True)


def clear_finished() -> int:
    """Drop resolved, failed and cancelled jobs. The queue is a worklist, not
    an archive -- results/ is the archive."""
    n = 0
    for p in list(QUEUE.glob("*.json")) if QUEUE.is_dir() else []:
        try:
            if json.loads(p.read_text()).get("state") in ("resolved", "failed",
                                                          "cancelled"):
                p.unlink(); n += 1
        except json.JSONDecodeError:
            continue
    return n
