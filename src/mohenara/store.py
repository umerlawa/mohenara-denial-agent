"""Case state store: park an unresolvable case, accept an answer, resume.

This module is THE api for the awaiting-human flow. The frontend calls these
functions and so does the scripted test -- deliberately, because a test that
exercises a private side door proves nothing about the path an operator
actually takes.

A parked case is a file under results/inbox/. Resuming re-runs the resolver
with the human's answer appended after the case data, which keeps the cached
prefix intact.
"""
from __future__ import annotations

import json
import pathlib
from dataclasses import dataclass

from . import resolve as _resolve
from .loader import Case, load_case, load_from_files, load_from_text

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
INBOX = REPO_ROOT / "results" / "inbox"
RESOLVED = REPO_ROOT / "results" / "inbox_resolved"


class NotParked(KeyError):
    pass


@dataclass(frozen=True)
class ParkedCase:
    case_id: str
    question: str
    why_needed: str
    blocks: list[str]
    asked_of: str | None
    input_format: str
    rendered: str
    model: str
    effort: str
    answers: tuple
    resolution: dict

    @classmethod
    def from_file(cls, path: pathlib.Path) -> "ParkedCase":
        d = json.loads(path.read_text())
        aw = d["resolution"]["awaiting_human"]
        return cls(
            case_id=d["case_id"], question=aw["question"],
            why_needed=aw.get("why_needed", ""), blocks=aw.get("blocks", []),
            asked_of=aw.get("asked_of"), input_format=d["input_format"],
            rendered=d["rendered"], model=d["model"], effort=d["effort"],
            answers=tuple(d.get("answers", ())),
            resolution=d["resolution"],
        )


def park(resolution: dict, case: Case, *, model: str, effort: str,
         answers: list[dict] | None = None) -> pathlib.Path:
    """Persist a case that stopped to ask. Returns the inbox path.

    `answers` carries the human answers already given, so a case that parks a
    second time resumes with everything it has been told rather than only the
    most recent reply.
    """
    if resolution.get("status") != "awaiting_human":
        raise ValueError("only an awaiting_human resolution can be parked")
    INBOX.mkdir(parents=True, exist_ok=True)
    path = INBOX / f"{case.case_id}.json"
    path.write_text(json.dumps({
        "case_id": case.case_id,
        "input_format": case.input_format,
        "rendered": case.rendered,
        "model": model,
        "effort": effort,
        "answers": answers or [],
        "resolution": resolution,
    }, indent=2) + "\n")
    return path


def list_parked() -> list[ParkedCase]:
    if not INBOX.is_dir():
        return []
    return [ParkedCase.from_file(p) for p in sorted(INBOX.glob("*.json"))]


def get_parked(case_id: str) -> ParkedCase:
    path = INBOX / f"{case_id}.json"
    if not path.exists():
        raise NotParked(f"{case_id} is not awaiting human input")
    return ParkedCase.from_file(path)


def answer(case_id: str, human_answer: str, *, run_id: str = "inbox",
           files: dict[str, str] | None = None,
           model: str | None = None, effort: str | None = None,
           on_delta=None) -> dict:
    """Inject a human's answer and resume the case to completion.

    This is the single entry point the frontend and the test both use.

    `files` carries documents the operator obtained while answering -- an
    authorisation letter, a corrected remit, the payer's written policy. The
    answer to "was an authorisation obtained" is frequently a document rather
    than a sentence, and retyping its contents into a text box loses exactly
    the detail that settles the case.

    `model` and `effort` override what the case was originally parked with. A
    case that needed a human usually needed one because it was hard, and the
    operator should be able to spend a stronger model on the second pass than
    the first attempt used.
    """
    if not human_answer or not human_answer.strip():
        raise ValueError("an empty answer cannot unblock a case")

    parked = get_parked(case_id)
    case = load_from_text(parked.rendered, parked.input_format, parked.case_id)

    if files:
        # Appended as named documents rather than merged into the case body, so
        # the model can tell what the operator supplied from what the payer
        # sent -- and so the evidence trail can name the right source.
        for name, contents in files.items():
            if not contents or not contents.strip():
                continue
            human_answer += (f"\n\n## Document supplied by the operator: "
                             f"`{pathlib.Path(name).name}`\n\n```\n"
                             f"{contents.strip()}\n```")

    # Replay every answer this case has been given, oldest first, so a case on
    # its second question does not lose the fact that unblocked the first.
    replay = "\n\n".join(
        [f"Q: {a['question']}\nA: {a['answer']}" for a in parked.answers]
        + [f"Q: {parked.question}\nA: {human_answer}"]
    )
    result = _resolve.resolve_case(
        case, model=model or parked.model, effort=effort or parked.effort,
        run_id=run_id, human_answer=replay, on_delta=on_delta,
    )

    if result.status == "awaiting_human":
        # The answer unblocked one thing and the case hit another. Re-park it
        # with the NEW question, keeping the human answer so far, and leave it
        # in the inbox. Filing it as resolved and deleting it -- which is what
        # used to happen -- lost the case entirely: it vanished from the inbox
        # with its new question unanswered and unasked.
        prior = list(parked.answers)
        park(result.resolution, case, model=parked.model, effort=parked.effort,
             answers=prior + [{"question": parked.question, "answer": human_answer}])
        return result.resolution

    RESOLVED.mkdir(parents=True, exist_ok=True)
    (RESOLVED / f"{case_id}.json").write_text(
        json.dumps({"case_id": case_id, "question": parked.question,
                    "answer": human_answer, "resolution": result.resolution},
                   indent=2) + "\n")
    (INBOX / f"{case_id}.json").unlink(missing_ok=True)
    return result.resolution


def resolve_or_park(case_id: str | None = None, *, input_format: str = "md",
                    text: str | None = None,
                    files: dict[str, str] | None = None,
                    model: str = _resolve.DEFAULT_MODEL,
                    effort: str = _resolve.DEFAULT_EFFORT,
                    run_id: str = "adhoc") -> dict:
    """Run a case; park it automatically if the model stopped to ask.

    Three ways in, one Case out: an uploaded file set, pasted text, or a corpus
    case id. Upload is checked first so that dropping an EDI artifact set does
    not depend on the operator also clearing the paste box.
    """
    if files:
        case = load_from_files(files, input_format, case_id or "MOH2-000000")
    elif text is not None:
        case = load_from_text(text, input_format, case_id or "MOH2-000000")
    else:
        case = load_case(case_id, input_format)
    result = _resolve.resolve_case(case, model=model, effort=effort, run_id=run_id)
    if result.status == "awaiting_human":
        park(result.resolution, case, model=model, effort=effort)
    return result.resolution
