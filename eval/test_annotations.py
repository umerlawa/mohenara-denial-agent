"""Annotations come from the model's citations, never from reading the input.

Offline: no model calls, no spend.

The demo view highlights lines of a claim and calls them defects. That screen is
only honest if the highlights trace to something the model actually said. The
tempting implementation -- have the frontend look for SV1 segments without a
modifier -- produces an identical-looking screen that would keep highlighting
confidently on a case the model got wrong, and would be showing the demo's own
analysis under the model's name.

So the rule these tests enforce is narrow and absolute: an annotation exists
only where the model quoted a segment AND that quotation occurs verbatim in the
artifact. Everything else is reported as unanchored, never placed.
"""
from __future__ import annotations

import pathlib
import sys

import pytest

REPO = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "src"))

from mohenara import annotate  # noqa: E402
from mohenara.loader import load_case  # noqa: E402

CASE = "MOH2-000029"

CLAIM = """\
ST*837*0001*005010X222A1~
CLM*PA25896500*169.75***11:B:1*Y*A*Y*Y~
LX*1~
SV1*HC:97110*77.92*UN*2***1~
LX*2~
SV1*HC:97112*44.76*UN*1***1~
LX*3~
SV1*HC:97140*47.07*UN*1***1~
SE*34*0001~"""

ARTIFACTS = {"claim_837p.edi": CLAIM}


def ev(artifact="claim_837p.edi", text=None, chip="Missing GP modifier",
       severity="error", line=None, fact="no GP modifier"):
    seg = [] if text is None else [{"text": text, "line": line, "id": "SV1"}]
    return {"artifact": artifact, "fact": fact, "chip": chip,
            "severity": severity, "segments": seg}


# --- anchoring ---------------------------------------------------------------

def test_a_quoted_segment_anchors_to_its_real_line():
    out = annotate.annotations(
        {"evidence": [ev(text="SV1*HC:97110*77.92*UN*2***1~")]}, ARTIFACTS)
    assert len(out["anchored"]) == 1
    a = out["anchored"][0]
    assert a["line"] == 4 and a["chip"] == "Missing GP modifier"
    assert a["text"] == "SV1*HC:97110*77.92*UN*2***1~"


def test_a_segment_the_model_never_quoted_is_never_highlighted():
    """The whole point. No citation, no annotation -- not even a plausible one."""
    out = annotate.annotations({"evidence": [ev(text=None)]}, ARTIFACTS)
    assert out["anchored"] == []
    assert out["unanchored"][0]["reason"] == "no segment cited"


def test_a_quotation_that_is_not_in_the_artifact_is_not_placed():
    """A hallucinated segment must surface as unanchored, not land somewhere near."""
    out = annotate.annotations(
        {"evidence": [ev(text="SV1*HC:99213*50.00*UN*1***1~")]}, ARTIFACTS)
    assert out["anchored"] == []
    assert "does not occur" in out["unanchored"][0]["reason"]


def test_a_paraphrase_does_not_anchor():
    """`locator`-style prose was the old shape and must not be treated as a quote."""
    out = annotate.annotations(
        {"evidence": [ev(text="the SV1 segments for lines 1 to 3")]}, ARTIFACTS)
    assert out["anchored"] == []


def test_a_substring_does_not_anchor_three_lines():
    """Matching on containment would light up every SV1 from one citation."""
    out = annotate.annotations({"evidence": [ev(text="SV1")]}, ARTIFACTS)
    assert out["anchored"] == []


def test_a_repeated_identical_quotation_anchors_every_occurrence():
    """An EDI remit repeats identical segments -- the same LQ*HE*N822~ under
    every denied line. A model that quoted that segment has cited a line that
    is byte-identical wherever it occurs, so the annotation lands on all of
    them. Dropping it instead -- the old rule -- left a real run's three
    repeated remark codes unmarked on screen."""
    dupes = {"claim_837p.edi": "LX*1~\nSE*34*0001~\nLX*1~"}
    out = annotate.annotations({"evidence": [ev(text="LX*1~")]}, dupes)
    assert [a["line"] for a in out["anchored"]] == [1, 3]
    assert out["unanchored"] == []


def test_the_models_own_line_number_narrows_a_repeated_quotation():
    dupes = {"claim_837p.edi": "LX*1~\nLX*1~"}
    ok = annotate.annotations({"evidence": [ev(text="LX*1~", line=2)]}, dupes)
    assert [a["line"] for a in ok["anchored"]] == [2]


def test_a_wrong_line_number_still_anchors_the_real_occurrences():
    """The quotation is the evidence; the line number is only a tie-breaker.
    A hint pointing nowhere must not un-anchor text that genuinely occurs."""
    dupes = {"claim_837p.edi": "LX*1~\nLX*1~"}
    out = annotate.annotations({"evidence": [ev(text="LX*1~", line=9)]}, dupes)
    assert [a["line"] for a in out["anchored"]] == [1, 2]


def test_a_citation_against_an_absent_artifact_is_unanchored():
    out = annotate.annotations(
        {"evidence": [ev(artifact="remit_835.edi", text="CAS*CO*4*77.92~")]}, ARTIFACTS)
    assert out["anchored"] == []
    assert "not in this case" in out["unanchored"][0]["reason"]


def test_the_three_gp_lines_anchor_together():
    """The shape the demo test asserts end to end."""
    out = annotate.annotations({"evidence": [
        ev(text="SV1*HC:97110*77.92*UN*2***1~"),
        ev(text="SV1*HC:97112*44.76*UN*1***1~"),
        ev(text="SV1*HC:97140*47.07*UN*1***1~"),
    ]}, ARTIFACTS)
    assert [a["line"] for a in out["anchored"]] == [4, 6, 8]
    assert all(a["severity"] == "error" for a in out["anchored"])


def test_leading_whitespace_does_not_block_an_anchor():
    indented = {"claim_837p.edi": "  SV1*HC:97110*77.92*UN*2***1~"}
    out = annotate.annotations(
        {"evidence": [ev(text="SV1*HC:97110*77.92*UN*2***1~")]}, indented)
    assert out["anchored"][0]["line"] == 1


def test_an_empty_resolution_produces_no_annotations():
    assert annotate.annotations({}, ARTIFACTS) == {"anchored": [], "unanchored": []}
    assert annotate.annotations(None, ARTIFACTS)["anchored"] == []


# --- the corrected claim -----------------------------------------------------

def corrected(**kw):
    base = {"artifact": "claim_837p.edi", "edits": [
        {"before": "SV1*HC:97110*77.92*UN*2***1~",
         "after": "SV1*HC:97110:GP*77.92*UN*2***1~", "why": "append GP"},
        {"before": "CLM*PA25896500*169.75***11:B:1*Y*A*Y*Y~",
         "after": "CLM*PA25896500*169.75***11:B:7*Y*A*Y*Y~",
         "why": "frequency code 7, replacement"},
    ]}
    base.update(kw)
    return base


def test_corrections_change_only_the_lines_the_model_quoted():
    out = annotate.apply_corrections(corrected(), ARTIFACTS)
    before, after = CLAIM.splitlines(), out["text"].splitlines()
    differing = [i + 1 for i, (a, b) in enumerate(zip(before, after)) if a != b]
    assert differing == [c["line"] for c in out["changed"]] == [2, 4]
    assert len(before) == len(after)


def test_the_frequency_code_edit_is_reported_as_changed():
    out = annotate.apply_corrections(corrected(), ARTIFACTS)
    clm = [c for c in out["changed"] if c["line"] == 2][0]
    assert "11:B:7" in clm["after"] and "11:B:1" in clm["before"]
    assert "11:B:7" in out["text"]


def test_an_edit_whose_before_is_absent_is_dropped_not_guessed():
    out = annotate.apply_corrections(
        corrected(edits=[{"before": "SV1*HC:99999*1.00*UN*1***1~", "after": "x"}]),
        ARTIFACTS)
    assert out["changed"] == []
    assert out["dropped"] and "does not occur" in out["dropped"][0]["reason"]
    assert out["text"] == CLAIM, "a dropped edit must leave the claim untouched"


def test_two_edits_cannot_both_claim_the_same_line():
    same = corrected(edits=[
        {"before": "LX*1~", "after": "LX*1~", "line": 3},
        {"before": "LX*1~", "after": "LX*9~", "line": 3},
    ])
    out = annotate.apply_corrections(same, ARTIFACTS)
    assert len(out["changed"]) == 1 and len(out["dropped"]) == 1


def test_a_decision_only_resolution_yields_no_corrected_claim():
    """do_not_resubmit produces no file; the view must show a card instead."""
    assert annotate.apply_corrections(None, ARTIFACTS) is None


def test_an_ambiguous_edit_is_still_dropped_never_applied_everywhere():
    """Annotations loosened for repeated segments; corrections must NOT.
    Highlighting every identical occurrence states a fact. Rewriting every
    identical occurrence invents claim content the model never approved."""
    dupes = {"claim_837p.edi": "LX*1~\nLX*1~"}
    out = annotate.apply_corrections(
        {"artifact": "claim_837p.edi",
         "edits": [{"before": "LX*1~", "after": "LX*9~"}]}, dupes)
    assert out["changed"] == []
    assert len(out["dropped"]) == 1
    assert out["text"] == "LX*1~\nLX*1~"


# --- streaming ---------------------------------------------------------------

@pytest.mark.parametrize("buf,want", [
    ('{"status":"resolved","rationale":"All three lines', "All three lines"),
    ('{"rationale":"done."}', "done."),
    ('{"rationale":"a \\"quoted\\" bit', 'a "quoted" bit'),
    ('{"rationale":"line\\nbreak', "line\nbreak"),
    ('{"status":"resolved"', ""),
    ('', ""),
    ('{"rationale":', ""),
    ('{"rationale":"', ""),
])
def test_the_rationale_is_read_out_of_a_partial_buffer(buf, want):
    assert annotate.partial_string_field(buf, "rationale") == want


@pytest.mark.parametrize("tail", ["\\", "\\u", "\\u00", "\\u041"])
def test_a_buffer_cut_mid_escape_still_decodes(tail):
    """Deltas split anywhere, including the middle of an escape sequence."""
    assert annotate.partial_string_field(
        '{"rationale":"ok' + tail, "rationale") == "ok"


def test_the_rationale_grows_monotonically_as_deltas_arrive():
    full = '{"status":"resolved","rationale":"All three lines denied CO-4."}'
    seen = ""
    for i in range(len(full) + 1):
        now = annotate.partial_string_field(full[:i], "rationale")
        assert now.startswith(seen) or len(now) >= len(seen) or now == ""
        if now:
            seen = now
    assert seen == "All three lines denied CO-4."


# --- against the real corpus case -------------------------------------------

def test_the_real_case_round_trips_through_the_renderer():
    """artifacts_from_rendered must recover the bytes the model was shown."""
    case = load_case(CASE, "edi")
    got = annotate.artifacts_from_rendered(case.rendered)
    assert "claim_837p.edi" in got and "remit_835.edi" in got

    on_disk = (REPO / "corpus" / "v2-chain-corpus-v1.1" / "edi" / CASE /
               "claim_837p.edi").read_text().strip()
    assert got["claim_837p.edi"] == on_disk


def test_the_three_therapy_lines_are_quotable_from_the_real_case():
    """The exact strings the model must echo back for the demo to anchor."""
    case = load_case(CASE, "edi")
    claim = annotate.artifacts_from_rendered(case.rendered)["claim_837p.edi"]
    quotes = ["SV1*HC:97110*77.92*UN*2***1~",
              "SV1*HC:97112*44.76*UN*1***1~",
              "SV1*HC:97140*47.07*UN*1***1~"]
    out = annotate.annotations(
        {"evidence": [ev(text=q) for q in quotes]},
        {"claim_837p.edi": claim})
    assert len(out["anchored"]) == 3
    assert out["unanchored"] == []


# --- streaming findings ------------------------------------------------------
#
# The demo's findings display shows each finding the moment its JSON object is
# COMPLETE in the stream buffer. "Complete" is the honesty condition: an item
# revealed before its closing brace arrives would be the frontend guessing.

EV = ('{"artifact":"claim_837p.edi","fact":"no GP modifier","chip":"Missing GP",'
      '"severity":"error","segments":[{"text":"SV1*HC:97110*77.92*UN*2***1~"}]}')


def test_a_completed_finding_is_extracted():
    head = '{"status":"resolved","resolution":{"evidence":['
    # The item's own object is the unit of completeness: with its closing
    # brace missing it is invisible, with it present it is a finding -- the
    # surrounding array may stay open either way.
    assert annotate.partial_evidence_items(head + EV[:-2]) == []
    done = annotate.partial_evidence_items(head + EV)
    assert len(done) == 1
    assert done[0]["chip"] == "Missing GP"
    assert done[0]["severity"] == "error"


def test_an_item_cut_mid_write_is_excluded_until_its_brace_arrives():
    buf = ('{"resolution":{"evidence":[' + EV + ','
           '{"artifact":"remit_835.edi","fact":"CO-4 wi')
    items = annotate.partial_evidence_items(buf)
    assert [i["fact"] for i in items] == ["no GP modifier"]

    complete = buf + 'th N822"}]}}'
    items = annotate.partial_evidence_items(complete)
    assert [i["fact"] for i in items] == ["no GP modifier", "CO-4 with N822"]


def test_braces_inside_strings_do_not_close_an_item():
    tricky = ('{"resolution":{"evidence":[{"artifact":"chart_note.txt",'
              '"fact":"note says {braces} and \\"quotes\\" and ]",'
              '"segments":[]}')
    items = annotate.partial_evidence_items(tricky + "]}}")
    assert len(items) == 1 and "{braces}" in items[0]["fact"]


def test_findings_grow_monotonically_as_the_stream_arrives():
    full = ('{"status":"awaiting_human","partial":{"evidence":['
            + EV + ","
            + EV.replace("97110", "97112").replace("no GP modifier", "second line")
            + "]}}")
    counts = []
    for i in list(range(0, len(full), 25)) + [len(full)]:
        counts.append(len(annotate.partial_evidence_items(full[:i])))
    assert counts == sorted(counts), "a finding must never disappear"
    assert counts[-1] == 2


def test_both_evidence_arrays_are_read_and_duplicates_are_not():
    two = ('{"partial":{"evidence":[' + EV + ']},'
           '"resolution":{"evidence":[' + EV + "]}}")
    assert len(annotate.partial_evidence_items(two)) == 1, (
        "the same fact in both arrays is one finding, not two")


def test_an_empty_or_irrelevant_buffer_yields_no_findings():
    assert annotate.partial_evidence_items("") == []
    assert annotate.partial_evidence_items('{"rationale":"no evidence here"}') == []
