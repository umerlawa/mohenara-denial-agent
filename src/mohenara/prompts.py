"""Prompt assembly. Deterministic: no model calls.

Layout exists to serve prompt caching. Everything stable -- role, decision
procedure, output contract, and the whole reference library -- is assembled
into one prefix that is byte-identical across cases. The case data is the ONLY
thing that varies, and it goes last, in the user turn.

Byte stability is load-bearing, not cosmetic: a single changed byte anywhere
in the prefix invalidates the cache for everything after it, and the harness
overhead alone is ~22k tokens. Reference files are therefore concatenated in
sorted filename order, with no timestamps and no interpolated state.
"""
from __future__ import annotations

import functools
import pathlib

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
# The runtime cards, not the full research. reference/*.md is 294KB (~74k
# tokens); loading it on every request costs ~$34 across the eval matrix
# against an $18 envelope. reference/runtime/ holds distilled decision cards
# derived from those files and citing them, so the code meanings the system
# uses are still read from repo reference files rather than recalled -- just
# from the digest rather than the source.
REFERENCE_DIR = REPO_ROOT / "reference" / "runtime"
FULL_REFERENCE_DIR = REPO_ROOT / "reference"

# The model decides these fields. Everything else in schema/resolution.json --
# case_id, input_format, usage, schema_version -- is filled by the harness from
# measured facts, so the model cannot invent its own token counts or cost.
MODEL_OUTPUT_SCHEMA = {
    "type": "json_schema",
    "schema": {
        "type": "object",
        "additionalProperties": False,
        "required": ["status", "rationale"],
        "properties": {
            "status": {"enum": ["resolved", "awaiting_human"]},
            "rationale": {"type": "string", "maxLength": 1200},
            "resolution": {
                "type": "object",
                "additionalProperties": False,
                "required": ["root_cause", "next_action", "evidence"],
                "properties": {
                    "root_cause": {
                        "type": "object", "additionalProperties": False,
                        "required": ["family", "explanation"],
                        "properties": {
                            "family": {"enum": [
                                "none", "cob_other_primary", "eligibility_terminated",
                                "exact_duplicate", "missing_referring_provider",
                                "missing_therapy_modifier", "mue_exceeded",
                                "ncci_ptp_no59", "threshold_no_kx", "timely_filing"]},
                            "explanation": {"type": "string", "maxLength": 700},
                        },
                    },
                    "next_action": {
                        "type": "object", "additionalProperties": False,
                        "required": ["path", "detail"],
                        "properties": {
                            "path": {"enum": [
                                "none", "appeal", "bill_patient", "correct_and_resubmit",
                                "do_not_resubmit", "resubmit_other_payer"]},
                            "detail": {"type": "string", "maxLength": 700},
                            "resubmission_frequency_code": {"enum": ["7", "8"]},
                        },
                    },
                    "denial": {
                        "type": ["object", "null"], "additionalProperties": False,
                        "required": ["group", "carc"],
                        "properties": {
                            "group": {"enum": ["CO", "PR", "OA", "PI"]},
                            "carc": {"type": "string"},
                            "rarc": {"type": ["string", "null"]},
                            "level": {"enum": ["claim", "line"]},
                        },
                    },
                    "payer": {
                            "type": ["string", "null"],
                            "description": "Payer name exactly as written in the artifacts.",
                        },
                        "billed_amount": {
                            "type": ["number", "null"],
                            "description": "Total billed on the denied claim, in dollars, as a number.",
                        },
                        "date_of_service": {
                            "type": ["string", "null"],
                            "description": "Earliest date of service, YYYY-MM-DD.",
                        },
                        "filing_deadline": {
                            "type": ["string", "null"],
                            "description": (
                                "Last date a corrected claim or appeal can be filed, "
                                "YYYY-MM-DD, derived from the governing limit in the "
                                "reference cards. NULL if the limit cannot be "
                                "established from the artifacts -- never estimate one."
                            ),
                        },
                        "denied_line_idxs": {
                        "type": "array",
                        "items": {"type": "integer", "minimum": 0},
                        "description": "ZERO-based indices of the denied service lines, counting SVC segments in the 835 in order. The first service line is 0, not 1 -- do not copy the LX*n numbering from the artifact.",
                    },
                    "evidence": {
                        "type": "array", "minItems": 1,
                        "items": {
                            "type": "object", "additionalProperties": False,
                            "required": ["artifact", "fact"],
                            "properties": {
                                "artifact": {"enum": [
                                    "none", "ack_277ca.edi", "chart_note.txt",
                                    "claim_837p.edi", "eligibility_270.edi",
                                    "eligibility_271.edi", "remit_835.edi",
                                    "case.md", "human_input", "reference"]},
                                "fact": {"type": "string"},
                                "locator": {"type": "string"},
                                "chip": {
                                    "type": "string",
                                    "description": "Six words or so of plain English, shown against the segment itself. No codes.",
                                },
                                "severity": {"enum": ["error", "warning", "context"]},
                                "segments": {
                                    "type": "array",
                                    "description": "The exact lines this fact rests on, quoted VERBATIM from the artifact.",
                                    "items": {
                                        "type": "object", "additionalProperties": False,
                                        "required": ["text"],
                                        "properties": {
                                            "text": {
                                                "type": "string",
                                                "description": "The line copied character for character, terminator included. Not a paraphrase, not a range, not a segment id on its own.",
                                            },
                                            "line": {"type": ["integer", "null"]},
                                            "id": {"type": ["string", "null"]},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    "corrected_claim": {
                        "type": ["object", "null"],
                        "additionalProperties": False,
                        "required": ["artifact", "edits"],
                        "description": "How to turn the claim as billed into the claim that should have been sent. Only when a corrected claim is actually going out.",
                        "properties": {
                            "artifact": {"enum": [
                                "none", "ack_277ca.edi", "chart_note.txt",
                                "claim_837p.edi", "eligibility_270.edi",
                                "eligibility_271.edi", "remit_835.edi",
                                "case.md", "human_input", "reference"]},
                            "note": {"type": "string"},
                            "edits": {
                                "type": "array", "minItems": 1,
                                "items": {
                                    "type": "object", "additionalProperties": False,
                                    "required": ["before", "after"],
                                    "properties": {
                                        "before": {
                                            "type": "string",
                                            "description": "The line as it stands now, VERBATIM from the artifact.",
                                        },
                                        "after": {
                                            "type": "string",
                                            "description": "The same line as it should read. Change only what must change.",
                                        },
                                        "line": {"type": ["integer", "null"]},
                                        "why": {"type": "string"},
                                    },
                                },
                            },
                        },
                    },
                    "citations": {
                        "type": "array",
                        "items": {
                            "type": "object", "additionalProperties": False,
                            "required": ["source", "rule"],
                            "properties": {"source": {"type": "string"},
                                           "rule": {"type": "string"}},
                        },
                    },
                },
            },
            "awaiting_human": {
                "type": "object", "additionalProperties": False,
                "required": ["question", "why_needed", "blocks"],
                "properties": {
                    "question": {"type": "string"},
                    "why_needed": {"type": "string"},
                    "blocks": {"type": "array", "items": {
                        "enum": ["root_cause.family", "next_action.path"]}},
                    "asked_of": {"enum": ["provider", "payer", "patient", "internal"]},
                },
            },
            "partial": {
                "type": "object", "additionalProperties": False,
                "required": ["evidence"],
                "description": "ONLY with status awaiting_human: what the artifacts DO establish, before the question. A denial usually decomposes -- report the settled parts here, with verbatim segments, exactly as evidence is reported on a resolved case.",
                "properties": {
                    "evidence": {
                        "type": "array", "minItems": 1,
                        "items": {
                            "type": "object", "additionalProperties": False,
                            "required": ["artifact", "fact"],
                            "properties": {
                                "artifact": {"enum": [
                                    "none", "ack_277ca.edi", "chart_note.txt",
                                    "claim_837p.edi", "eligibility_270.edi",
                                    "eligibility_271.edi", "remit_835.edi",
                                    "case.md", "human_input", "reference"]},
                                "fact": {"type": "string"},
                                "locator": {"type": "string"},
                                "chip": {"type": "string"},
                                "severity": {"enum": ["error", "warning", "context"]},
                                "segments": {
                                    "type": "array",
                                    "items": {
                                        "type": "object", "additionalProperties": False,
                                        "required": ["text"],
                                        "properties": {
                                            "text": {"type": "string"},
                                            "line": {"type": ["integer", "null"]},
                                            "id": {"type": ["string", "null"]},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    "denial": {
                        "type": ["object", "null"], "additionalProperties": False,
                        "required": ["group", "carc"],
                        "properties": {
                            "group": {"enum": ["CO", "PR", "OA", "PI"]},
                            "carc": {"type": "string"},
                            "rarc": {"type": ["string", "null"]},
                            "level": {"enum": ["claim", "line"]},
                        },
                    },
                },
            },
        },
    },
}

ROLE = """\
You resolve denied US medical claims. For one case you determine the ROOT CAUSE
of the denial and the CONCRETE NEXT ACTION, and you emit JSON only.

You work from the artifacts in front of you and the reference library below.
You never recall code meanings from memory: CARC, RARC, and claim-status code
meanings come from the reference library, and you cite the file you used.

THE RULE THAT MATTERS MOST: never guess a fact you do not have.

A claim is resolvable when its artifacts plus the reference library determine
both the root cause and the next action. Some denials are not: they turn on a
fact that lives outside the case -- whether the provider actually obtained an
authorization, what a payer said on a call, whether a document exists that was
never filed. For those you STOP and ask, rather than picking the likeliest
answer. A wrong confident answer costs a practice a real appeal deadline; an
honest question costs one phone call.

Do NOT ask when the artifacts already settle the question, or when the answer
would not change the disposition. Asking on a resolvable case is as much a
failure as guessing on an unresolvable one.
"""

PROCEDURE = """\
## Procedure

1. Read the remit (835) first. Identify every adjustment: group code, CARC,
   RARC, and whether it sits at claim level or line level. The group code
   decides who may be billed -- CO is contractual and may not be billed to the
   patient, PR is patient responsibility.
2. Look up every code you found in the reference library. Do not proceed on a
   remembered meaning.
3. Compare the remit against the claim as billed (837P) and the other
   artifacts. The defect is usually the difference between what was sent and
   what the payer needed.
4. Determine the root-cause family from the closed list. Choose `none` only
   when the claim was adjudicated correctly and no rework is warranted.
5. Determine the next action from the closed list. `next_action` is the step
   that RESOLVES THE DENIAL -- it is not general accounts-receivable advice.
   When `root_cause.family` is `none` the claim needs no rework and the path is
   `none`, even where ordinary patient responsibility (PR-2 coinsurance, PR-1
   deductible) is still to be billed in the normal course; that is routine AR,
   not a denial remedy. Reserve `bill_patient` for denials whose resolution IS
   that the balance has become the patient's. Where a corrected claim is going
   out, give the frequency code (7 replacement, 8 void).
6. Fill the claim header from the artifacts: `payer` exactly as written,
   `billed_amount` as a number, `date_of_service` as the earliest DOS, and
   `filing_deadline` as the last date a corrected claim or appeal could be
   filed under the governing limit in the reference cards.

   `filing_deadline` is the one to be careful with. Work gets scheduled against
   a deadline, so an invented one is worse than none: emit `null` whenever the
   limit cannot be established from the artifacts, and never estimate. The
   other three are transcription from the documents and should almost always be
   present.

7. Cite the evidence you actually used. Every conclusion names the artifact
   and the specific fact in it. An empty evidence list is not acceptable.

   QUOTE THE SEGMENT. For each piece of evidence, put the line or lines it
   rests on in `segments`, copied character for character out of the artifact
   -- terminator included, nothing normalised, nothing abbreviated. A reader
   downstream matches your quotation against the artifact bytes to place your
   finding on the right line, so `SV1` alone, a range like "lines 1-3", or a
   tidied-up version of the line all fail to place and the finding is shown
   without a location.

   One segment per line of the artifact. Three defective service lines are
   three quotations, not one quotation covering all of them. Add `chip`: six
   words of plain English a biller would recognise, no codes in it. Add
   `severity`: `error` on the segments that ARE the defect, `context` on the
   ones that merely support the conclusion.

8. When a corrected claim is going out, fill `corrected_claim` with the edits
   that produce it: `before` quoted verbatim as in step 7, `after` the same
   line as it should read. Change only what must change -- the edits are
   applied to the real file, and everything you do not touch stays exactly as
   billed. Include the CLM frequency-code edit whenever you set
   `resubmission_frequency_code`, since that is part of what makes it a
   corrected claim rather than a duplicate.

   Leave `corrected_claim` null when the resolution is a decision rather than a
   file. `do_not_resubmit` and `bill_patient` produce no claim.
9. If step 4 or 5 turns on a fact the artifacts do not carry, first check the
   reference library for a rule that DETERMINES it from what the artifacts DO
   carry. A state filing floor keyed to the subscriber's address, for example,
   settles a timely-filing question outright -- the address is on the claim and
   the floor is in the cards. Applying a documented rule to a fact that is
   present is not guessing; failing to apply it is an avoidable park.

   Park when the fact is absent from BOTH the artifacts and the reference
   library -- and park without hesitation when it is, including wherever a card
   tells you to. The PTP edit file's CCMI is the standing example: the 835
   carries neither the partner code nor the indicator, and the card is explicit
   that you look it up or ask, never guess. Do not talk yourself out of a park
   that a card requires.

   To park, emit status `awaiting_human` with ONE specific answerable question.
   Not "need more information" -- name the fact, say who can answer, and say
   what it would change.

   A parked case is not an empty one. Report what the artifacts DO establish
   in `partial`: the denial codes you read, the segments that carry the
   defect signature, the facts that survive whatever the question's answer
   turns out to be -- each as evidence with verbatim `segments`, `chip` and
   `severity`, exactly as on a resolved case. The person answering your
   question reads this first; showing them the settled ground is what makes
   the one open question answerable.

## Output

JSON only, matching the provided schema. `resolved` carries `resolution`;
`awaiting_human` carries `awaiting_human`. Never both.

Be brief. An RCM operator reads this on one screen between phone calls.
  - `explanation`: at most 50 words. The evidence, not the reasoning that
    found it.
  - `detail`: at most 50 words. The instruction, imperative, specific.
  - `rationale`: at most 80 words.
  - `evidence`: the 2-4 facts that actually decide it, not everything you read.
  - `denied_line_idxs`: **zero-based**. The first service line is `0`. The
    artifacts number their own lines from 1 (`LX*1`); do not carry that over.

Do not restate the case back. Do not explain what you considered and rejected.
Do not hedge -- if the evidence settles it, say it plainly; if it does not,
that is what `awaiting_human` is for.
"""


@functools.lru_cache(maxsize=1)
def reference_library() -> str:
    """Concatenate reference/*.md in sorted order. Cached: same bytes every call."""
    if not REFERENCE_DIR.is_dir():
        return "*(reference library not present)*"
    files = sorted(REFERENCE_DIR.glob("*.md"), key=lambda p: p.name)
    if not files:
        return "*(reference library is empty)*"
    chunks = ["# Reference library",
              "",
              "Cite these files by name. They are the authority for code meanings.",
              ""]
    for path in files:
        chunks += [f"<reference file=\"{path.name}\">", path.read_text().strip(),
                   "</reference>", ""]
    return "\n".join(chunks)


@functools.lru_cache(maxsize=1)
def system_prompt() -> str:
    """The cacheable prefix. Byte-identical for every case in a run."""
    return "\n\n".join([ROLE, reference_library(), PROCEDURE])


def user_prompt(rendered_case: str, human_answer: str | None = None) -> str:
    """The varying tail: case data last, after all stable content."""
    parts = ["Resolve this case.", "", rendered_case]
    if human_answer:
        parts += [
            "",
            "## Answer from the human operator",
            "",
            "You previously stopped and asked a question. Here is the answer:",
            "",
            human_answer.strip(),
            "",
            "Treat this as established fact. Resolve the case now, and record it "
            "in your evidence with artifact `human_input`.",
        ]
    return "\n".join(parts)
