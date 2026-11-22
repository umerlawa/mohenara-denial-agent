"""Internal data app. Separate from the operator app on purpose.

The customer-facing app at `mohenara.api` shows a denial and its resolution and
nothing else -- no spend, no eval runs, no accuracy. That separation is
structural rather than cosmetic: those endpoints live HERE, so the process a
client can reach has no route that serves them, and no amount of URL-guessing
against the demo turns up what a run cost or how the system scores.

Run it on its own port, and do not expose it publicly.

    uvicorn mohenara.internal_api:app --app-dir src --port 8766

Deterministic: reads results/ and computes no model output. Every accuracy
figure it serves is copied from a scorer report -- a number this layer derived
would be a second, unverified scorer.
"""
from __future__ import annotations

import collections
import json
import pathlib

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from . import config, spend

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
RESULTS = REPO_ROOT / "results"
STATIC = pathlib.Path(__file__).parent / "static"

app = FastAPI(title="Mohenara internal data")


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    return (STATIC / "internal.html").read_text()


@app.get("/api/runs")
def api_runs() -> list[dict]:
    if not RESULTS.is_dir():
        return []
    runs = []
    for run_json in sorted(RESULTS.glob("*/run.json")):
        try:
            runs.append(json.loads(run_json.read_text()))
        except json.JSONDecodeError:
            continue
    return runs


@app.get("/api/runs/{run_id}")
def api_run_detail(run_id: str) -> dict:
    run_dir = RESULTS / run_id
    if not (run_dir / "run.json").exists():
        raise HTTPException(404, f"no run {run_id}")
    summary = json.loads((run_dir / "run.json").read_text())
    predictions = []
    for path in sorted((run_dir / "predictions").glob("*.json")):
        d = json.loads(path.read_text())
        res = d.get("resolution") or {}
        predictions.append({
            "case_id": d["case_id"], "status": d["status"],
            "family": (res.get("root_cause") or {}).get("family"),
            "path": (res.get("next_action") or {}).get("path"),
            "usage": d["usage"],
        })
    summary["predictions"] = predictions
    return summary


@app.get("/api/spend")
def api_spend() -> dict:
    """Per-provider, because the two budgets never mix. A single combined
    total against a single cap would misreport both of them."""
    ledger = spend.load()
    providers = []
    for name in config.provider_names():
        cfg = config.provider(name)
        p = ledger.get("providers", {}).get(name, {"usd": 0.0, "calls": 0})
        providers.append({
            "name": name,
            "usd": round(float(p.get("usd", 0.0)), 6),
            "calls": int(p.get("calls", 0)),
            "stop_at": cfg["stop_eval_usd"],
            "refuse_at": cfg["budget_usd"],
        })
    return {"providers": providers,
            "total_usd": ledger.get("total_usd", 0.0),
            "calls": ledger.get("calls", 0),
            "by_run": ledger.get("by_run", {})}


@app.get("/api/families")
def api_families() -> list[dict]:
    """Per-family accuracy across every scored run, copied from score reports.

    The per-family view is where a weakness is actually legible: a headline of
    87% hides a family at 14%, and it is the family breakdown that says whether
    the gap is reasoning, reference material, or a labelling disagreement.
    """
    agg: dict[str, dict] = {}
    for score in sorted(RESULTS.glob("*/score.json")):
        run = score.parent.name
        try:
            s = json.loads(score.read_text())
        except json.JSONDecodeError:
            continue
        for fam, st in (s.get("by_family") or {}).items():
            a = agg.setdefault(fam, {"family": fam, "total": 0, "correct": 0, "runs": []})
            a["total"] += st["total"]
            a["correct"] += st["correct"]
            a["runs"].append({"run_id": run, "accuracy": st["accuracy"],
                              "correct": st["correct"], "total": st["total"]})
    for a in agg.values():
        a["accuracy"] = round(a["correct"] / a["total"], 6) if a["total"] else None
    return sorted(agg.values(), key=lambda a: (a["accuracy"] is None, a["accuracy"]))


@app.get("/api/failures")
def api_failures() -> list[dict]:
    """Every wrong case across every scored run, with the reason the scorer gave.

    Grouped by case rather than by run, so a case that fails everywhere -- a
    reference or reasoning gap -- is distinguishable from one that fails in a
    single format, which is a rendering or parsing gap. Those need different
    fixes and a per-run listing hides the difference.
    """
    by_case: dict[str, dict] = {}
    for score in sorted(RESULTS.glob("*/score.json")):
        run = score.parent.name
        try:
            s = json.loads(score.read_text())
        except json.JSONDecodeError:
            continue
        for c in s.get("per_case", []):
            if c["correct"]:
                continue
            e = by_case.setdefault(c["case_id"], {
                "case_id": c["case_id"], "expected_family": c["expected_family"],
                "expected_path": c["expected_path"], "runs": [], "reasons": [],
            })
            e["runs"].append(run)
            e["reasons"].append(c["reason"])
    for e in by_case.values():
        e["n_runs_failed"] = len(e["runs"])
        e["reason_counts"] = dict(collections.Counter(e["reasons"]))
    return sorted(by_case.values(), key=lambda e: -e["n_runs_failed"])


@app.get("/api/case/{case_id}")
def api_case(case_id: str) -> dict:
    """Everything logged for one case, across every run that touched it.

    This is the view that replaces guessing. The brief requires failures to be
    diagnosed by reading what happened, and what happened is the prediction the
    system wrote plus the transcript behind it.
    """
    out = {"case_id": case_id, "runs": []}
    for pred in sorted(RESULTS.glob(f"*/predictions/{case_id}.json")):
        run = pred.parent.parent
        d = json.loads(pred.read_text())
        res = d.get("resolution") or {}
        aw = d.get("awaiting_human") or {}
        verdict = None
        sp = run / "score.json"
        if sp.exists():
            try:
                for c in json.loads(sp.read_text()).get("per_case", []):
                    if c["case_id"] == case_id:
                        verdict = c
                        break
            except json.JSONDecodeError:
                pass
        out["runs"].append({
            "run_id": run.name,
            "status": d.get("status"),
            "family": (res.get("root_cause") or {}).get("family"),
            "path": (res.get("next_action") or {}).get("path"),
            "explanation": (res.get("root_cause") or {}).get("explanation"),
            "detail": (res.get("next_action") or {}).get("detail"),
            "rationale": d.get("rationale"),
            "evidence": res.get("evidence") or [],
            "citations": res.get("citations") or [],
            "question": aw.get("question"),
            "usage": d.get("usage"),
            "verdict": verdict,
            "has_transcript": (run / "transcripts" / f"{case_id}.json").exists(),
        })
    if not out["runs"]:
        raise HTTPException(404, f"nothing logged for {case_id}")
    return out


@app.get("/api/notes")
def api_notes() -> list[dict]:
    """The hand-written analysis in results/, listed so it is findable.

    Conclusions drawn from this data live in markdown beside it. A data browser
    that cannot surface them sends the reader back to the filesystem.
    """
    out = []
    for p in sorted(RESULTS.rglob("*.md")):
        out.append({"path": str(p.relative_to(RESULTS)),
                    "bytes": p.stat().st_size,
                    "title": next((l.lstrip("# ").strip()
                                   for l in p.read_text().splitlines()
                                   if l.startswith("# ")), p.stem)})
    return out


@app.get("/api/note/{path:path}")
def api_note(path: str) -> dict:
    p = (RESULTS / path).resolve()
    if not str(p).startswith(str(RESULTS.resolve())) or not p.is_file():
        raise HTTPException(404, f"no note {path}")
    return {"path": path, "markdown": p.read_text()}


# --- analysis endpoints -----------------------------------------------------
#
# Added after a look at the data showed the headline numbers were hiding the
# most actionable finding in the project: 18% of all failures have the FAMILY
# right and the ACTION wrong. The system diagnoses well and routes badly, and a
# per-family accuracy table cannot show that.

def _scored_runs() -> list[tuple[str, dict]]:
    out = []
    for s in sorted(RESULTS.glob("*/score.json")):
        try:
            out.append((s.parent.name, json.loads(s.read_text())))
        except json.JSONDecodeError:
            continue
    return out


# Resubmitting when you should not draws a second denial and burns a filing
# window; the reverse merely leaves money on the table. Naming the asymmetry is
# the difference between a matrix you look at and one you act on.
COSTLY = {
    ("do_not_resubmit", "correct_and_resubmit"):
        "Tells a biller to resubmit a claim that will be denied again, and spends "
        "a filing window doing it.",
    ("do_not_resubmit", "appeal"):
        "Sends a non-appealable denial to appeal; wasted effort and a lost window.",
    ("appeal", "correct_and_resubmit"):
        "Resubmits where the payer wanted an appeal; the resubmission is a duplicate.",
    ("resubmit_other_payer", "correct_and_resubmit"):
        "Rebills the wrong payer. COB order is not fixed by correcting the claim.",
}


@app.get("/api/confusion")
def api_confusion(field: str = "path") -> dict:
    """Confusion matrix over next_action (default) or root-cause family.

    `path` is the default because that is where the failures are. A matrix over
    family looks almost diagonal and hides the problem.
    """
    if field not in ("path", "family"):
        raise HTTPException(400, "field must be path or family")
    exp_key = "expected_path" if field == "path" else "expected_family"
    got_key = "got_path" if field == "path" else "got_family"

    cells: dict[tuple[str, str], int] = collections.Counter()
    labels: set[str] = set()
    total = correct = 0
    for _, s in _scored_runs():
        for c in s.get("per_case", []):
            e, g = c.get(exp_key), c.get(got_key)
            if not e:
                continue
            labels.add(e)
            total += 1
            if g:
                labels.add(g)
                cells[(e, g)] += 1
                if e == g:
                    correct += 1
            else:
                cells[(e, "(no answer)")] += 1
    labels.add("(no answer)")

    order = sorted(labels)
    return {
        "field": field,
        "labels": order,
        "total": total,
        "diagonal": correct,
        "cells": [{"expected": e, "got": g, "n": n,
                   "costly": COSTLY.get((e, g))}
                  for (e, g), n in sorted(cells.items(), key=lambda kv: -kv[1])],
    }


@app.get("/api/failure-taxonomy")
def api_failure_taxonomy() -> dict:
    """Every failure sorted into what kind of problem it actually is.

    A single accuracy number treats these as equivalent. They are not: a routing
    error needs a rule in a reference card, a parked case may need no fix at all,
    and a missing prediction is an infrastructure problem wearing a wrong answer's
    clothes.
    """
    buckets = collections.Counter()
    detail: dict[str, list] = collections.defaultdict(list)
    for run, s in _scored_runs():
        for c in s.get("per_case", []):
            if c["correct"]:
                continue
            if c["reason"] == "missing_prediction":
                k = "never answered (infrastructure or budget)"
            elif c["reason"] == "awaiting_human":
                k = "refused to guess (parked)"
            elif c.get("family_correct") and not c.get("path_correct"):
                k = "diagnosed right, routed wrong"
            elif not c.get("family_correct") and c.get("path_correct"):
                k = "routed right, diagnosed wrong"
            elif c["reason"] in ("schema_invalid", "unreadable"):
                k = "output unusable"
            else:
                k = "diagnosed and routed wrong"
            buckets[k] += 1
            detail[k].append({"run_id": run, "case_id": c["case_id"],
                              "expected": f"{c['expected_family']}/{c['expected_path']}",
                              "got": f"{c.get('got_family')}/{c.get('got_path')}"})
    tot = sum(buckets.values())
    return {"total": tot,
            "buckets": [{"kind": k, "n": n, "share": round(n / tot, 4) if tot else 0,
                         "cases": detail[k][:60]}
                        for k, n in buckets.most_common()]}


@app.get("/api/reference-usage")
def api_reference_usage() -> dict:
    """Which reference cards actually get cited, and which never do.

    A card nobody cites is either dead weight in a cached prefix that is paid
    for on every single call, or a rule the system is failing to reach for. Both
    are worth knowing and neither is visible anywhere else.
    """
    runtime = {p.name for p in (REPO_ROOT / "reference" / "runtime").glob("*.md")}
    cited = collections.Counter()
    by_family: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    for pred in RESULTS.glob("*/predictions/*.json"):
        try:
            d = json.loads(pred.read_text())
        except json.JSONDecodeError:
            continue
        res = d.get("resolution") or {}
        fam = (res.get("root_cause") or {}).get("family")
        for c in (res.get("citations") or []):
            src = str(c.get("source", "")).split(" §")[0].strip()
            cited[src] += 1
            if fam:
                by_family[src][fam] += 1
    return {
        "cards": [{"source": s, "citations": n, "in_runtime_prefix": s in runtime,
                   "top_families": by_family[s].most_common(3)}
                  for s, n in cited.most_common()],
        "never_cited": sorted(runtime - set(cited)),
    }


@app.get("/api/regressions")
def api_regressions(baseline: str, candidate: str) -> dict:
    """Cases that changed verdict between two runs, both directions.

    A pair of headline accuracies can be identical while half the cases flipped.
    This is the view that says whether a change helped, and where.
    """
    def per_case(run: str) -> dict:
        p = RESULTS / run / "score.json"
        if not p.exists():
            raise HTTPException(404, f"no score.json for {run}")
        return {c["case_id"]: c for c in json.loads(p.read_text()).get("per_case", [])}

    a, b = per_case(baseline), per_case(candidate)

    # A case the candidate never REACHED is not a regression. The scorer counts
    # a missing prediction as wrong, correctly -- but reporting it here as
    # "broke" would blame a budget stop or a throttle on the change under test,
    # which is the one thing a regression view must never do. Compare only cases
    # both runs actually attempted, and report the rest separately.
    attempted = {c for c in set(a) & set(b)
                 if a[c]["reason"] != "missing_prediction"
                 and b[c]["reason"] != "missing_prediction"}
    not_attempted = sorted((set(a) & set(b)) - attempted)

    shared = sorted(attempted)
    fixed = [c for c in shared if not a[c]["correct"] and b[c]["correct"]]
    broke = [c for c in shared if a[c]["correct"] and not b[c]["correct"]]
    return {
        "baseline": baseline, "candidate": candidate,
        "shared_cases": len(shared),
        "not_attempted_by_one_side": len(not_attempted),
        "not_attempted_ids": not_attempted[:60],
        "baseline_correct": sum(a[c]["correct"] for c in shared),
        "candidate_correct": sum(b[c]["correct"] for c in shared),
        "fixed": [{"case_id": c, "was": a[c]["reason"],
                   "now": f"{b[c].get('got_family')}/{b[c].get('got_path')}"} for c in fixed],
        "broke": [{"case_id": c, "now": b[c]["reason"],
                   "was": f"{a[c].get('got_family')}/{a[c].get('got_path')}",
                   "expected": f"{b[c]['expected_family']}/{b[c]['expected_path']}"} for c in broke],
        "net": len(fixed) - len(broke),
    }


@app.get("/api/economics")
def api_economics() -> list[dict]:
    """Cost and cache behaviour per configuration, from the usage blocks.

    Cache hit rate is the number to watch: the prefix is engineered to be
    cacheable and a drop means the design has quietly stopped working, which
    shows up as cost long before it shows up as anything else.
    """
    agg: dict[tuple, dict] = {}
    for run_json in RESULTS.glob("*/run.json"):
        run = run_json.parent
        try:
            meta = json.loads(run_json.read_text())
        except json.JSONDecodeError:
            continue
        for pred in (run / "predictions").glob("*.json"):
            try:
                u = json.loads(pred.read_text())["usage"]
            except (json.JSONDecodeError, KeyError):
                continue
            key = (u.get("model", "?"), u.get("effort", "?"), meta.get("input_format", "?"))
            a = agg.setdefault(key, {"model": key[0], "effort": key[1], "format": key[2],
                                     "cases": 0, "cost": 0.0, "out": 0,
                                     "cache_read": 0, "cache_write": 0})
            a["cases"] += 1
            a["cost"] += u.get("cost_usd", 0.0)
            a["out"] += u.get("output_tokens", 0)
            a["cache_read"] += u.get("cache_read_input_tokens", 0)
            a["cache_write"] += u.get("cache_creation_input_tokens", 0)
    out = []
    for a in agg.values():
        reads, writes = a["cache_read"], a["cache_write"]
        out.append({**a,
                    "cost_per_case": round(a["cost"] / a["cases"], 6) if a["cases"] else 0,
                    "out_per_case": round(a["out"] / a["cases"]) if a["cases"] else 0,
                    "cache_hit_rate": round(reads / (reads + writes), 4) if reads + writes else 0})
    return sorted(out, key=lambda a: -a["cases"])


@app.get("/api/parked")
def api_parked() -> dict:
    """What the system refuses to guess at, and who it wants asked.

    The refusal is the product's distinguishing behaviour, so it deserves its own
    view: whether the parks cluster on one family, and whether they are avoidable
    (a rule exists) or correct (no artifact carries the fact).
    """
    by_family, by_asked, questions = collections.Counter(), collections.Counter(), []
    for pred in RESULTS.glob("*/predictions/*.json"):
        try:
            d = json.loads(pred.read_text())
        except json.JSONDecodeError:
            continue
        if d.get("status") != "awaiting_human":
            continue
        aw = d.get("awaiting_human") or {}
        by_asked[aw.get("asked_of") or "unspecified"] += 1
        questions.append({"run_id": pred.parent.parent.name, "case_id": d["case_id"],
                          "asked_of": aw.get("asked_of"), "blocks": aw.get("blocks"),
                          "question": aw.get("question")})
    for _, s in _scored_runs():
        for c in s.get("per_case", []):
            if c.get("reason") == "awaiting_human":
                by_family[c["expected_family"]] += 1
    return {"total": len(questions),
            "by_expected_family": by_family.most_common(),
            "by_asked_of": by_asked.most_common(),
            "questions": questions[:100]}
