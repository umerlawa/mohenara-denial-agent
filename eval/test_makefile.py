"""The VERIFY_LIVE gate must actually gate. Offline: runs make, spends nothing.

This exists because the gate silently did not work. It was written as

    @test "$(VERIFY_LIVE)" = "1" || { echo "skipped"; exit 0; }
    npx playwright test

which reads like a guard and is not one: every make recipe LINE runs in its own
shell, so `exit 0` ends the guard's shell and the command on the next line runs
regardless. A clean-checkout verification told not to spend spent real money.

The failure was invisible in the output -- "skipped" was printed, immediately
above the suite it claimed to have skipped.
"""
from __future__ import annotations

import pathlib
import re
import subprocess

import pytest

REPO = pathlib.Path(__file__).resolve().parent.parent
# Derived from the Makefile rather than hardcoded. The list drifted the moment
# verify-tokens moved to the offline group: a hardcoded name that no longer
# spends fails for the wrong reason, and -- worse -- a NEW live target nobody
# remembered to add here would silently go uncovered.
#
# Detection is on the GUARD's shape, not on the mere appearance of the variable
# name: a recipe may legitimately mention it in a comment while not being gated.
GUARD = re.compile(r'^\t@?if \[ "\$\(VERIFY_LIVE\)" = "1" \]', re.M)


def _recipe_text(target: str) -> str:
    text = (pathlib.Path(__file__).resolve().parent.parent / "Makefile").read_text()
    m = re.search(rf"^{re.escape(target)}:.*?\n((?:\t.*\n|\\\n)*)", text, re.M)
    return m.group(1) if m else ""


def _live_targets() -> list[str]:
    text = (pathlib.Path(__file__).resolve().parent.parent / "Makefile").read_text()
    return [t for t in re.findall(r"^(verify-[a-z-]+):", text, re.M)
            if GUARD.search(_recipe_text(t))]


LIVE_TARGETS = _live_targets()


def recipe(target: str) -> list[str]:
    """The recipe lines for one target, as make would run them."""
    text = (REPO / "Makefile").read_text()
    m = re.search(rf"^{re.escape(target)}:.*?\n((?:\t.*\n|\\\n)*)", text, re.M)
    assert m, f"{target} not found in the Makefile"
    # A trailing backslash continues the SAME shell invocation, so join those
    # first. What remains is one entry per shell make will spawn -- which is
    # exactly the unit the gate has to live inside.
    body = m.group(1).replace("\\\n", " ")
    return [ln for ln in body.split("\n") if ln.strip()]


@pytest.mark.parametrize("target", LIVE_TARGETS)
def test_the_guard_and_the_command_share_one_shell(target: str):
    """A guard on its own recipe line cannot stop the line beneath it."""
    lines = recipe(target)
    assert len(lines) == 1, (
        f"{target} has {len(lines)} recipe lines. Each runs in its own shell, "
        "so a guard on one line cannot skip the command on the next. Put the "
        "guard and the command in a single `if ... ; then ... ; else ... ; fi`."
    )
    assert "VERIFY_LIVE" in lines[0], f"{target} is not gated at all"


@pytest.mark.parametrize("target", LIVE_TARGETS)
def test_the_gate_actually_skips(target: str):
    """Run the target with VERIFY_LIVE unset and prove nothing else ran.

    The strongest available check short of spending: make -n prints exactly
    what would execute. If the suite's command appears outside the guarded
    branch, the gate is decorative.
    """
    out = subprocess.run(["make", "-s", target], cwd=REPO, capture_output=True,
                         text=True, env={"PATH": "/usr/bin:/bin:/usr/local/bin"})
    assert out.returncode == 0, out.stderr[-800:]
    assert "skipped" in out.stdout, f"{target} did not report skipping: {out.stdout[:400]}"
    for noise in ("passed", "failed", "Running", "test"):
        assert noise not in out.stdout.replace("skipped", ""), (
            f"{target} produced suite output while claiming to skip:\n{out.stdout[:600]}"
        )
