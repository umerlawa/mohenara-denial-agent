"""Every citation names a file that exists. Offline: reads results/ only.

The brief requires code meanings to come from the reference files, cited by
filename, never recalled from memory. `citations[].source` is a free string,
so nothing structurally prevents the model from inventing a plausible
filename -- and an invented citation is worse than none, because it reads as
provenance and cannot be followed.

Measured across every run on disk when this was written: 382 citations, 337 to
runtime cards the model was given and 45 to research files those cards cite by
name, and zero to anything else. The model follows the provenance chain
correctly -- a card says "per resubmission-and-frequency-codes.md §6" and the
model cites that upstream authority, which is right. This test exists so that
staying true is checked rather than lucky.

Two levels are legitimate, and the distinction matters:
  - reference/runtime/*.md  the cards actually loaded into the prompt
  - reference/*.md          the research those cards cite by name
Anything else is an invention.
"""
from __future__ import annotations

import collections
import json
import pathlib
import re

import pytest

REPO = pathlib.Path(__file__).resolve().parent.parent
RUNTIME = REPO / "reference" / "runtime"
RESEARCH = REPO / "reference"


def known_sources() -> set[str]:
    return ({p.name for p in RUNTIME.glob("*.md")}
            | {p.name for p in RESEARCH.glob("*.md")})


def basename(source: str) -> str:
    """Strip a trailing section reference: 'card.md §4' -> 'card.md'."""
    return re.split(r"\s+§", source.strip())[0]


def all_predictions() -> list[pathlib.Path]:
    return sorted((REPO / "results").glob("*/predictions/*.json"))


def artifact_names() -> set[str]:
    """Case-artifact filenames. These are evidence, not authority."""
    import sys
    sys.path.insert(0, str(REPO / "src"))
    from mohenara.loader import EDI_ARTIFACTS
    return {f for f, _ in EDI_ARTIFACTS} | {"case.md"}


def test_no_citation_names_a_file_that_does_not_exist():
    """The hard invariant: invented provenance.

    A citation naming a file that exists nowhere in the repo reads as
    provenance and cannot be followed. That is the failure that matters and it
    fails the build.
    """
    preds = all_predictions()
    if not preds:
        pytest.skip("no predictions on disk")
    known = known_sources() | artifact_names()
    assert known, "no reference files found; the check would be vacuous"

    invented: collections.Counter = collections.Counter()
    total = 0
    for path in preds:
        d = json.loads(path.read_text())
        for c in ((d.get("resolution") or {}).get("citations") or []):
            total += 1
            if basename(str(c.get("source", ""))) not in known:
                invented[f"{path.parent.parent.name}/{path.stem}: {c.get('source')!r}"] += 1

    assert total, "no citations found; the check would be vacuous"
    assert not invented, (
        f"{sum(invented.values())} of {total} citations name a file that exists "
        f"nowhere in this repo:\n  " + "\n  ".join(list(invented)[:10])
    )


def test_citations_point_at_authority_not_at_case_artifacts(capsys):
    """The softer one: a real file, but of the wrong kind.

    `citations[].source` is for the reference material that justifies the
    routing decision. A case artifact belongs in `evidence[].artifact` -- it is
    what happened, not the rule that says what to do about it. Putting one in
    `citations` is a category error rather than an invention, so it is reported
    with its rate rather than failing the build.

    Measured when this was written: 2 of 837 citations, 0.24%. The bound is
    deliberately loose; it exists to catch the day this becomes systematic, not
    to police a rounding error.
    """
    preds = all_predictions()
    if not preds:
        pytest.skip("no predictions on disk")
    refs, arts = known_sources(), artifact_names()

    miscategorised: collections.Counter = collections.Counter()
    total = 0
    for path in preds:
        d = json.loads(path.read_text())
        for c in ((d.get("resolution") or {}).get("citations") or []):
            total += 1
            b = basename(str(c.get("source", "")))
            if b in arts and b not in refs:
                miscategorised[b] += 1

    rate = sum(miscategorised.values()) / max(total, 1)
    if miscategorised:
        with capsys.disabled():
            print(f"\n  note: {sum(miscategorised.values())}/{total} citations "
                  f"({rate:.2%}) name a case artifact rather than a reference "
                  f"file: {dict(miscategorised)}")
    assert rate < 0.05, (
        f"{rate:.1%} of citations name a case artifact instead of the reference "
        f"that justifies the decision. That was 0.24% when this bound was set, "
        f"so this is now systematic: {dict(miscategorised)}"
    )


def test_a_cited_runtime_card_was_actually_in_the_prompt():
    """A card in reference/runtime/ is loaded; one merely in reference/ is not.

    This asserts the loaded set is non-empty and that the prompt really
    contains the cards, so the first test cannot pass by both sides being
    empty.
    """
    import sys
    sys.path.insert(0, str(REPO / "src"))
    from mohenara.prompts import system_prompt

    cards = sorted(p.name for p in RUNTIME.glob("*.md"))
    assert cards, "no runtime cards"
    prompt = system_prompt()
    for card in cards:
        assert card in prompt, f"{card} is in runtime/ but not in the prompt"


def test_research_files_the_cards_cite_by_name_all_exist():
    """The cards' own citation chain must not dangle either.

    If a card cites a research file that has been renamed or deleted, the model
    faithfully passes that dead name through and every citation downstream of
    it becomes unfollowable.
    """
    known = known_sources()
    dangling: dict[str, set[str]] = {}
    for card in sorted(RUNTIME.glob("*.md")):
        text = card.read_text()
        for name in set(re.findall(r"\b[a-z0-9][a-z0-9-]*\.md\b", text)):
            if name not in known:
                dangling.setdefault(card.name, set()).add(name)
    assert not dangling, (
        "runtime cards cite files that do not exist; the model will pass these "
        f"dead names straight through: {dangling}"
    )
