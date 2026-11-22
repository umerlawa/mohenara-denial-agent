"""Case loading and rendering. Deterministic: no model calls, ever.

Both input formats resolve to one rendered string. The `edi` path concatenates
the six raw X12/text artifacts under stable headings; the `md` path reads the
pre-converted case.md. Rendering is byte-stable for a given case so the
leakage test can assert identical output across checkouts.
"""
from __future__ import annotations

import pathlib
from dataclasses import dataclass

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
MD_ROOT = REPO_ROOT / "corpus" / "v2-chain-corpus-v1.1-md"
EDI_ROOT = REPO_ROOT / "corpus" / "v2-chain-corpus-v1.1" / "edi"

# Fixed order so the rendered prompt is byte-stable across filesystems.
EDI_ARTIFACTS = [
    ("claim_837p.edi", "Claim as billed (837P)"),
    ("remit_835.edi", "Adjudication outcome (835)"),
    ("ack_277ca.edi", "Acknowledgement (277CA)"),
    ("eligibility_270.edi", "Eligibility inquiry (270)"),
    ("eligibility_271.edi", "Eligibility response (271)"),
    ("chart_note.txt", "Chart note"),
]


class CaseNotFound(FileNotFoundError):
    pass


@dataclass(frozen=True)
class Case:
    case_id: str
    input_format: str
    rendered: str
    artifacts: tuple[str, ...]

    @property
    def approx_tokens(self) -> int:
        return len(self.rendered) // 4


def available_case_ids(input_format: str) -> list[str]:
    root = MD_ROOT if input_format == "md" else EDI_ROOT
    return sorted(p.name for p in root.iterdir() if p.is_dir())


def load_case(case_id: str, input_format: str) -> Case:
    if input_format not in {"md", "edi"}:
        raise ValueError(f"input_format must be 'md' or 'edi', got {input_format!r}")
    return _load_md(case_id) if input_format == "md" else _load_edi(case_id)


def _load_md(case_id: str) -> Case:
    path = MD_ROOT / case_id / "case.md"
    if not path.exists():
        raise CaseNotFound(f"no case.md for {case_id} at {path}")
    return Case(case_id, "md", path.read_text(), ("case.md",))


def render_edi(case_id: str, artifacts: dict[str, str]) -> Case:
    """Render an EDI artifact set. The ONE renderer, shared by every entry point.

    The corpus loader and the frontend's upload path both come through here, so
    an uploaded artifact set produces bytes identical to the same case read off
    disk. If they had separate renderers, the frontend would be measuring a
    different prompt from the one the eval scored, and every cost and accuracy
    number shown to the operator would quietly describe something else.

    `artifacts` maps filename -> contents. Filenames outside EDI_ARTIFACTS are
    ignored rather than appended, because artifact ORDER is part of the stable
    prefix and an unknown file has no defined position in it.
    """
    parts = [f"# Case {case_id} (raw EDI artifacts)", ""]
    present: list[str] = []
    for filename, heading in EDI_ARTIFACTS:
        contents = artifacts.get(filename)
        # A zero-byte file is absence, not an empty artifact. Rendering it as
        # present-but-blank told the model an acknowledgement WAS received and
        # said nothing, when what happened is that no acknowledgement exists --
        # and listed it among the artifacts that were read.
        if contents is not None and not contents.strip():
            contents = None
        if contents is None:
            # Absence is itself evidence -- a missing 277CA is a real signal,
            # so say so rather than omitting the section silently.
            parts += [f"## {heading} -- `{filename}`", "", "*(artifact not present for this case)*", ""]
            continue
        present.append(filename)
        parts += [f"## {heading} -- `{filename}`", "", "```", contents.strip(), "```", ""]
    return Case(case_id, "edi", "\n".join(parts), tuple(present))


def _load_edi(case_id: str) -> Case:
    folder = EDI_ROOT / case_id
    if not folder.is_dir():
        raise CaseNotFound(f"no EDI folder for {case_id} at {folder}")
    return render_edi(case_id, {
        filename: (folder / filename).read_text()
        for filename, _ in EDI_ARTIFACTS if (folder / filename).exists()
    })


def load_from_text(text: str, input_format: str, case_id: str = "MOH2-000000") -> Case:
    """Build a Case from pasted text, for the frontend."""
    return Case(case_id, input_format, text, ("<pasted>",))


def load_from_files(files: dict[str, str], input_format: str,
                    case_id: str = "MOH2-000000") -> Case:
    """Build a Case from uploaded files, for the frontend.

    An `md` upload is a single document. An `edi` upload is an artifact set,
    matched to EDI_ARTIFACTS by basename and rendered through the same
    function the corpus loader uses.
    """
    if not files:
        raise ValueError("no files supplied")

    if input_format == "md":
        # One document; if several arrive, the .md wins over stray companions.
        md = [n for n in files if n.lower().endswith(".md")] or list(files)
        return Case(case_id, "md", files[md[0]], (pathlib.Path(md[0]).name,))

    known = {f for f, _ in EDI_ARTIFACTS}
    artifacts = {pathlib.Path(name).name: text for name, text in files.items()
                 if pathlib.Path(name).name in known}
    if not artifacts:
        raise ValueError(
            "none of the uploaded files is a recognised EDI artifact. "
            f"Expected one or more of: {', '.join(sorted(known))}"
        )
    return render_edi(case_id, artifacts)
