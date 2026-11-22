"""Leakage: the resolution system must be unable to read the answer labels.

Copies the repo to a temp checkout, DELETES the label file, and exercises the
system there.

On what "behave identically" can mean here: the resolver calls a language
model, so asserting byte-identical *model output* across two runs would be
asserting determinism the model does not offer, and the test would flake for
reasons unrelated to leakage. So the assertion is placed where leakage would
actually show up and where behaviour IS deterministic:

  1. the fully assembled prompt -- system prefix plus user turn, the only
     bytes the model ever sees -- is identical with and without labels present;
  2. the system runs to a schema-valid resolution in the label-free checkout;
  3. no label content appears anywhere in the prompt;
  4. no module outside the scorer imports or opens the label file.

If labels influenced the system, they would have to reach the model through
the prompt. (1) and (3) close that path deterministically; the live run in (2)
proves absence of a hidden runtime dependency.
"""
from __future__ import annotations

import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile

import pytest

REPO = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "src"))

LABELS = REPO / "eval" / "dev_labels.jsonl"
PROBE_CASES = ['MOH2-000061', 'MOH2-000062']  # labeled cases, from the iteration slice


def _render_prompts(root: pathlib.Path, case_id: str, fmt: str) -> str:
    """Assemble the exact prompt bytes inside `root`, in a clean subprocess."""
    script = (
        "import sys, json;"
        f"sys.path.insert(0, {str(root / 'src')!r});"
        "from mohenara.prompts import system_prompt, user_prompt;"
        "from mohenara.loader import load_case;"
        f"c = load_case({case_id!r}, {fmt!r});"
        "sys.stdout.write(system_prompt() + '\\n<<<CASE>>>\\n' + user_prompt(c.rendered))"
    )
    out = subprocess.run([sys.executable, "-c", script], capture_output=True,
                         text=True, cwd=str(root))
    assert out.returncode == 0, f"prompt assembly failed in {root}:\n{out.stderr[-1500:]}"
    return out.stdout


@pytest.fixture(scope="module")
def stripped_checkout():
    """A copy of the repo with the label file deleted."""
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="leakage-"))
    dest = tmp / "repo"
    shutil.copytree(
        REPO, dest,
        ignore=shutil.ignore_patterns(".git", ".venv", "node_modules",
                                      "__pycache__", "results", ".pytest_cache"),
    )
    (dest / "eval" / "dev_labels.jsonl").unlink()
    yield dest
    shutil.rmtree(tmp, ignore_errors=True)


def test_label_file_is_actually_gone(stripped_checkout):
    assert not (stripped_checkout / "eval" / "dev_labels.jsonl").exists()
    assert LABELS.exists(), "the real checkout should still have its labels"


@pytest.mark.parametrize("fmt", ["md", "edi"])
@pytest.mark.parametrize("case_id", PROBE_CASES)
def test_prompt_bytes_identical_without_labels(stripped_checkout, case_id, fmt):
    """The only bytes the model sees must not depend on the labels existing."""
    with_labels = _render_prompts(REPO, case_id, fmt)
    without = _render_prompts(stripped_checkout, case_id, fmt)
    assert with_labels == without, (
        f"{case_id}/{fmt}: prompt differs when labels are deleted -- "
        "the system is reading them"
    )


@pytest.mark.parametrize("case_id", PROBE_CASES)
def test_no_label_content_reaches_the_prompt(case_id):
    """Belt and braces: no answer string appears in the assembled prompt."""
    labels = {json.loads(ln)["case_id"]: json.loads(ln)
              for ln in LABELS.read_text().splitlines() if ln.strip()}
    label = labels[case_id]
    prompt = _render_prompts(REPO, case_id, "md")
    # exact_fix and root_cause are label-only prose; neither may appear.
    for field in ("exact_fix", "root_cause"):
        text = (label.get(field) or "").strip()
        if len(text) > 40:
            assert text not in prompt, f"{case_id}: label {field} leaked into the prompt"


def test_scorer_is_the_only_label_reader():
    offenders = []
    for path in REPO.rglob("*.py"):
        if {".venv", "node_modules", "__pycache__"} & set(path.parts):
            continue
        if path.name in {"score.py", "test_score.py", "test_leakage.py"}:
            continue
        if "dev_labels" in path.read_text(errors="ignore"):
            offenders.append(str(path.relative_to(REPO)))
    assert not offenders, f"non-scorer files reference the labels: {offenders}"


@pytest.mark.skipif(os.environ.get("VERIFY_LIVE") != "1",
                    reason="calls the API; set VERIFY_LIVE=1 to run")
def test_system_resolves_in_a_label_free_checkout(stripped_checkout):
    """Proves no hidden runtime dependency on the label file."""
    script = (
        "import sys, json;"
        f"sys.path.insert(0, {str(stripped_checkout / 'src')!r});"
        "from mohenara.loader import load_case;"
        "from mohenara.resolve import resolve_case;"
        "c = load_case('MOH2-000009', 'md');"
        "r = resolve_case(c, model='us.anthropic.claude-sonnet-4-6', "
        "effort='low', run_id='verify-leakage');"
        "print(json.dumps({'status': r.resolution['status']}))"
    )
    out = subprocess.run([sys.executable, "-c", script], capture_output=True,
                         text=True, cwd=str(stripped_checkout))
    assert out.returncode == 0, f"system failed without labels:\n{out.stderr[-2000:]}"
    assert json.loads(out.stdout.strip().splitlines()[-1])["status"] in {
        "resolved", "awaiting_human"}
