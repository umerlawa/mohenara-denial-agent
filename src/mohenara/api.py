"""Operator app: submit denials, watch the queue, answer the ones it stopped on.

Deliberately narrow, and deliberately incurious about the model. There is no
model or effort parameter on any route here and no way to discover from this app
which model resolved a case, at what effort, or what it cost. That is a backend
concern; changing it is a config change in config/models.json, and the person
using this app should not know it happened.

Everything internal -- spend, eval runs, accuracy -- lives in
`mohenara.internal_api`, a different app on a different port. The separation is
structural rather than a matter of hidden controls: this process has no route
that serves any of it.

The HTTP layer is thin. `store.answer()` is the same function the scripted test
calls, so the test exercises the operator's real path rather than a side door.
"""
from __future__ import annotations

import json
import pathlib
import re
import time

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, StreamingResponse
from pydantic import BaseModel

from . import annotate, caseinfo, config, jobs, store
from .resolve import ResolutionInvalid
from . import spend

STATIC = pathlib.Path(__file__).parent / "static"
ASSETS = pathlib.Path(__file__).resolve().parents[2] / "assets"

# Fail here rather than four retries into the first real denial. A default that
# names a model this deployment cannot serve is a startup error, not a runtime
# surprise for whoever happens to submit first.
config.check_default()

app = FastAPI(title="Denial Resolution")


class Denial(BaseModel):
    """One denial. Files are the point; text and notes are optional."""
    label: str | None = None
    input_format: str = "edi"
    # filename -> contents. An `edi` denial is an artifact SET, so the filenames
    # matter: they fix each artifact's position in the cached prefix.
    files: dict[str, str] | None = None
    text: str | None = None
    case_id: str | None = None
    # Free text the operator adds. Context the documents do not carry.
    notes: str | None = None


class BatchRequest(BaseModel):
    denials: list[Denial]


class AnswerRequest(BaseModel):
    answer: str
    files: dict[str, str] | None = None


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    return (STATIC / "index.html").read_text()


DEMO_STATIC = STATIC / "demo"
DEFAULT_VARIANT = "v1"


def _variant_dir(name: str) -> pathlib.Path:
    """Resolve a variant name to its folder, refusing anything path-like.

    Variants are picked by query param from a URL, so the name is untrusted.
    Only [a-z0-9-] gets through: no separators, no traversal, no absolute paths.
    """
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,31}", name or ""):
        raise HTTPException(400, f"bad variant name {name!r}")
    d = DEMO_STATIC / name
    if not (d.is_dir() and (d / "index.html").is_file()):
        raise HTTPException(404, f"no demo variant {name!r}")
    return d


@app.get("/demo", response_class=HTMLResponse)
def demo(v: str = DEFAULT_VARIANT) -> str:
    """The outreach demo, served as swappable variants.

    A separate frontend on the same backend and the same API. `/demo?v=2` picks
    a different design without a backend change and without the operator app
    knowing anything happened -- these are for A/B-ing outreach videos, so the
    expensive part must be the only part that is shared.
    """
    return (_variant_dir(v) / "index.html").read_text()


@app.get("/api/demo/variants")
def api_demo_variants() -> dict:
    found = sorted(d.name for d in DEMO_STATIC.glob("*")
                   if d.is_dir() and (d / "index.html").is_file())
    return {"variants": found, "default": DEFAULT_VARIANT}


@app.get("/assets/{name}")
def api_asset(name: str):
    """Brand assets (the logo). Same untrusted-name rule as the variants."""
    if not re.fullmatch(r"[a-z0-9][a-z0-9._-]{0,63}", name or "") or ".." in name:
        raise HTTPException(400, f"bad asset name {name!r}")
    p = ASSETS / name
    if not p.is_file():
        raise HTTPException(404, f"no asset {name!r}")
    media = {"svg": "image/svg+xml", "png": "image/png",
             "ico": "image/x-icon"}.get(p.suffix.lstrip("."), "application/octet-stream")
    from fastapi.responses import Response
    return Response(p.read_bytes(), media_type=media)


class ParseRequest(BaseModel):
    cases: list[Denial]


@app.post("/api/demo/parse")
def api_demo_parse(req: ParseRequest) -> list[dict]:
    """Deterministic case-header facts for uploaded cases, before any resolve.

    No model call, no job, no spend: this reads the 835 the payer sent and
    reports what it states -- amounts, patient, payer, date -- so the demo can
    show a money picture the moment cases land. Anything the artifacts do not
    state comes back null; the view renders what it knows.
    """
    if not req.cases:
        raise HTTPException(400, "no cases to parse")
    if len(req.cases) > 50:
        raise HTTPException(400, "at most 50 cases per parse")
    out = []
    for i, c in enumerate(req.cases, 1):
        if not c.files:
            raise HTTPException(400, f"case {i} has no files")
        parsed = caseinfo.parse(c.files)
        parsed["label"] = c.label or parsed["claim_id"] or f"Case {i}"
        out.append(parsed)
    return out


@app.get("/api/demo/view/{job_id}")
def api_demo_view(job_id: str) -> dict:
    """Artifacts, anchored annotations and the corrected claim, for one job.

    Assembled in `jobs.demo_view` so the browser has nothing to analyse: every
    highlight traces to a segment the model quoted and that was then matched
    against the artifact bytes.
    """
    view = jobs.demo_view(job_id)
    if view is None:
        raise HTTPException(404, f"no job {job_id}")
    return view


@app.get("/api/demo/stream/{job_id}")
def api_demo_stream(job_id: str) -> StreamingResponse:
    """Server-sent events: the rationale as it is actually written, and elapsed time.

    The timer counts real seconds and the text is real deltas off the wire.
    Nothing here is on a schedule -- see the note in jobs.py about progress bars.
    """
    if jobs.get(job_id) is None:
        raise HTTPException(404, f"no job {job_id}")

    def events():
        sent = 0
        start = time.monotonic()
        while True:
            job = jobs.get(job_id)
            if job is None:
                break
            stream = jobs.stream_state(job_id)
            buffered = stream.get("text", "")
            reasoning = stream.get("reasoning", "")
            payload = {
                "state": job["state"],
                "elapsed_ms": int((time.monotonic() - start) * 1000),
                "rationale": annotate.partial_string_field(buffered, "rationale"),
                # The model thinking out loud, tail only. Some models write
                # most of the run here before the structured output starts;
                # the live headline falls back to this so those runs still
                # show real reasoning instead of a blinking cursor.
                "reasoning": reasoning[-4000:],
                "chars": len(buffered),
                "reasoning_chars": len(reasoning),
                # Each finding the moment its object is complete in the
                # stream -- the findings display renders exactly this list,
                # so a finding can only appear when the model has actually
                # finished writing it.
                "findings": annotate.partial_evidence_items(buffered),
            }
            terminal = job["state"] in ("resolved", "needs_input", "failed",
                                        "cancelled")
            payload["done"] = terminal
            yield f"data: {json.dumps(payload)}\n\n"
            sent += 1
            if terminal:
                break
            # Slow enough not to spin a worker thread, fast enough that the
            # timer reads as live to someone watching.
            time.sleep(0.4)

    return StreamingResponse(events(), media_type="text/event-stream",
                             headers={"Cache-Control": "no-store",
                                      "X-Accel-Buffering": "no"})


@app.get("/api/health")
def api_health() -> dict:
    """Readiness probe, and nothing else.

    Deliberately says nothing about which model is configured or what a run
    costs. The harness needs a route that returns 200 to know the server is up;
    it does not need one that leaks the backend.
    """
    return {"ok": True}


@app.post("/api/batch")
def api_batch(req: BatchRequest) -> list[dict]:
    """Accept one or many denials. Returns immediately; the queue does the work."""
    if not req.denials:
        raise HTTPException(400, "no denials submitted")
    if len(req.denials) > 50:
        raise HTTPException(400, "at most 50 denials per batch")

    out = []
    for i, d in enumerate(req.denials, 1):
        if not d.files and not d.text and not d.case_id:
            raise HTTPException(400, f"denial {i} has no documents, text or case id")
        if d.input_format not in ("md", "edi"):
            raise HTTPException(400, f"denial {i}: format must be md or edi")
        try:
            out.append(jobs.submit(
                label=d.label or d.case_id or f"Denial {i}",
                input_format=d.input_format, files=d.files, text=d.text,
                case_id=d.case_id, notes=d.notes))
        except spend.BudgetExceeded as exc:
            raise HTTPException(402, str(exc)) from exc
        except ValueError as exc:
            raise HTTPException(400, f"denial {i}: {exc}") from exc
    return out


@app.get("/api/queue")
def api_queue() -> list[dict]:
    return jobs.listing()


@app.get("/api/queue/{job_id}")
def api_job(job_id: str) -> dict:
    job = jobs.full(job_id)
    if job is None:
        raise HTTPException(404, f"no job {job_id}")
    return job


@app.post("/api/queue/{job_id}/answer")
def api_job_answer(job_id: str, req: AnswerRequest) -> dict:
    if not req.answer or not req.answer.strip():
        raise HTTPException(400, "an empty answer cannot unblock a denial")
    try:
        out = jobs.answer(job_id, req.answer, files=req.files)
    except spend.BudgetExceeded as exc:
        raise HTTPException(402, str(exc)) from exc
    except ResolutionInvalid as exc:
        raise HTTPException(422, str(exc)) from exc
    if out is None:
        raise HTTPException(409, f"job {job_id} is not waiting for input")
    return out


@app.post("/api/queue/{job_id}/cancel")
def api_job_cancel(job_id: str) -> dict:
    """Stop one denial: never started if queued, killed mid-call if running."""
    out = jobs.cancel(job_id)
    if out is None:
        raise HTTPException(409, f"job {job_id} is not running or queued")
    return out


@app.post("/api/queue/cancel-all")
def api_cancel_all() -> dict:
    """The panic button: stop every queued and running denial."""
    return {"cancelled": jobs.cancel_all()}


@app.post("/api/queue/clear")
def api_clear() -> dict:
    """Drop finished jobs. The queue is a worklist; results/ is the archive."""
    return {"cleared": jobs.clear_finished()}


@app.get("/api/inbox")
def api_inbox() -> list[dict]:
    """Parked cases from eval runs, which have no queue job behind them.

    Kept so a case parked by a batch run is still answerable by a human through
    the same `store.answer` path the queue uses.
    """
    return [{"case_id": p.case_id, "question": p.question,
             "why_needed": p.why_needed, "blocks": p.blocks,
             "asked_of": p.asked_of, "input_format": p.input_format,
             "answers_so_far": len(p.answers)}
            for p in store.list_parked()]


@app.post("/api/inbox/{case_id}/answer")
def api_answer(case_id: str, req: AnswerRequest) -> dict:
    try:
        # Same rule as the queue: the resumed resolution goes back to the
        # operator without its accounting record.
        return jobs.client_safe(store.answer(case_id, req.answer, files=req.files))
    except store.NotParked as exc:
        raise HTTPException(404, str(exc)) from exc
    except spend.BudgetExceeded as exc:
        raise HTTPException(402, str(exc)) from exc
    except ResolutionInvalid as exc:
        raise HTTPException(422, str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
