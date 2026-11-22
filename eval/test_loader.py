"""The loader is deterministic and byte-stable. Offline: no model calls.

The property under test is not "upload works" but "upload produces the SAME
BYTES as the corpus loader". The frontend and the eval share one resolver and
one cached prefix; if the two entry points rendered a case differently, every
cost, token and accuracy number the operator sees would describe a prompt the
eval never scored, and nothing else in the suite would notice.
"""
from __future__ import annotations

import pathlib
import sys

import pytest

REPO = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "src"))

from mohenara.loader import (EDI_ARTIFACTS, EDI_ROOT, MD_ROOT,  # noqa: E402
                             load_case, load_from_files, render_edi)


def a_corpus_case() -> str:
    folders = sorted(p.name for p in EDI_ROOT.iterdir() if p.is_dir()) if EDI_ROOT.is_dir() else []
    if not folders:
        pytest.skip("no EDI corpus in this checkout")
    return folders[0]


def artifacts_of(case_id: str) -> dict[str, str]:
    folder = EDI_ROOT / case_id
    return {f: (folder / f).read_text()
            for f, _ in EDI_ARTIFACTS if (folder / f).exists()}


def test_uploaded_edi_renders_identically_to_the_corpus():
    case_id = a_corpus_case()
    from_disk = load_case(case_id, "edi")
    uploaded = load_from_files(artifacts_of(case_id), "edi", case_id)
    assert uploaded.rendered == from_disk.rendered
    assert uploaded.artifacts == from_disk.artifacts


def test_upload_order_does_not_depend_on_the_order_files_arrive():
    """Artifact order is part of the stable prefix, so it cannot follow the
    order a file picker happened to hand them over in -- that would miss the
    cache on every upload and change the prompt for no reason."""
    case_id = a_corpus_case()
    forward = artifacts_of(case_id)
    backward = dict(reversed(list(forward.items())))
    assert (load_from_files(backward, "edi", case_id).rendered
            == load_from_files(forward, "edi", case_id).rendered)


def test_a_missing_artifact_is_reported_as_absent_not_omitted():
    """Absence is evidence. A missing 277CA must show as missing, because a
    silently shorter prompt reads as 'this case has no acknowledgement issue'
    when what happened is that the operator forgot a file."""
    case_id = a_corpus_case()
    partial = {k: v for k, v in artifacts_of(case_id).items() if k != "ack_277ca.edi"}
    rendered = load_from_files(partial, "edi", case_id).rendered
    assert "ack_277ca.edi" in rendered
    assert "*(artifact not present for this case)*" in rendered


def test_unknown_files_are_ignored_rather_than_appended():
    case_id = a_corpus_case()
    with_junk = dict(artifacts_of(case_id), **{"scan.pdf.txt": "IRRELEVANT-MARKER"})
    assert "IRRELEVANT-MARKER" not in load_from_files(with_junk, "edi", case_id).rendered


def test_a_full_path_is_matched_by_basename():
    """Browsers may hand over `MOH2-000001/claim_837p.edi`; the artifact is the
    basename, not the path the operator happened to drag from."""
    case_id = a_corpus_case()
    prefixed = {f"some/where/{k}": v for k, v in artifacts_of(case_id).items()}
    assert (load_from_files(prefixed, "edi", case_id).rendered
            == load_case(case_id, "edi").rendered)


def test_an_edi_upload_with_no_recognised_artifact_is_rejected():
    with pytest.raises(ValueError, match="recognised EDI artifact"):
        load_from_files({"holiday-photo.txt": "nope"}, "edi", "MOH2-000000")


def test_an_empty_upload_is_rejected():
    with pytest.raises(ValueError, match="no files"):
        load_from_files({}, "edi", "MOH2-000000")


def test_uploaded_md_is_the_document_itself():
    if not MD_ROOT.is_dir():
        pytest.skip("no md corpus in this checkout")
    case_id = a_corpus_case()
    src = MD_ROOT / case_id / "case.md"
    if not src.exists():
        pytest.skip(f"no case.md for {case_id}")
    uploaded = load_from_files({"case.md": src.read_text()}, "md", case_id)
    assert uploaded.rendered == load_case(case_id, "md").rendered


def test_render_edi_is_stable_across_calls():
    case_id = a_corpus_case()
    arts = artifacts_of(case_id)
    assert render_edi(case_id, arts).rendered == render_edi(case_id, arts).rendered


def test_a_zero_byte_artifact_reads_as_absent_not_empty():
    """An empty file is absence, and absence is evidence.

    Rendering a zero-byte 277CA as present-but-blank tells the model an
    acknowledgement WAS received and said nothing -- when what happened is
    that no acknowledgement exists. It also listed the file among the
    artifacts that were read, so the evidence trail claimed a source it had
    not actually got anything from.
    """
    case_id = a_corpus_case()
    arts = dict(artifacts_of(case_id))
    arts["ack_277ca.edi"] = "   \n\t\n"
    case = load_from_files(arts, "edi", case_id)

    assert "*(artifact not present for this case)*" in case.rendered
    assert "ack_277ca.edi" not in case.artifacts, (
        "an empty artifact was reported as one that was read"
    )
    blank = load_from_files(
        {k: v for k, v in arts.items() if k != "ack_277ca.edi"}, "edi", case_id)
    assert case.rendered == blank.rendered, (
        "a zero-byte artifact renders differently from a missing one"
    )


def test_the_current_corpus_has_no_empty_artifacts():
    """Guards the change above from silently altering the scored corpus.

    If a corpus artifact were ever empty, the zero-byte rule would change that
    case's prompt -- and every accuracy number measured before the change
    would describe a different prompt than the one measured after.
    """
    if not EDI_ROOT.is_dir():
        pytest.skip("no EDI corpus in this checkout")
    empty = [str(f) for case in sorted(EDI_ROOT.iterdir()) if case.is_dir()
             for f in case.iterdir() if f.is_file() and not f.read_text().strip()]
    assert not empty, f"empty artifacts would change these cases' prompts: {empty[:5]}"
