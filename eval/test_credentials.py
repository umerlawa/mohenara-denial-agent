"""Credentials come from .env.local, and the two providers stay apart. Offline.

Two defects are pinned here, both found by a Playwright run that failed three
journeys for what looked like three unrelated reasons.

  1. THE AMBIENT ENVIRONMENT SHADOWED THE REAL CREDENTIALS. The execution
     container sets its own AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY. They
     are present, so the presence check in `resolve._agent_env` passed; they are
     not this project's, so Bedrock answered 403 and the CLI reported it as
     "Authentication error - this may be a temporary network issue". Meanwhile
     `tools/bedrock_preflight.py` passed on the same models, because it was run
     from a shell that had sourced .env.local by hand. Two entry points, two
     answers, and the one that spent money was the wrong one.

  2. THE SUBPROCESS CARRIED BOTH PROVIDERS' CREDENTIALS. The Anthropic budget is
     scoped to the frontier comparison phase. A Bedrock turn holding
     ANTHROPIC_API_KEY is one routing bug away from spending it.

Nothing here reads or asserts a credential VALUE. Comparisons are on short
hashes, which distinguish two secrets without disclosing either.
"""
from __future__ import annotations

import os
import pathlib
import sys

import pytest

REPO = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "src"))

from mohenara import config, env, resolve  # noqa: E402


def test_env_local_is_gitignored():
    """The invariant everything else here depends on."""
    assert ".env.local" in (REPO / ".gitignore").read_text().split()


def test_env_local_is_not_tracked_by_git():
    """Gitignored is not the same as absent from the index."""
    import subprocess
    out = subprocess.run(["git", "ls-files", ".env.local"], cwd=REPO,
                         capture_output=True, text=True).stdout.strip()
    assert out == "", ".env.local is tracked by git"


def test_dotenv_overrides_the_ambient_environment(tmp_path, monkeypatch):
    """The whole bug in four lines."""
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "ambient-placeholder")
    f = tmp_path / ".env.local"
    f.write_text("AWS_ACCESS_KEY_ID=the-real-one\n")
    env.load(f)
    assert os.environ["AWS_ACCESS_KEY_ID"] == "the-real-one"


@pytest.mark.parametrize("line,key,val", [
    ("AWS_REGION=us-east-1", "AWS_REGION", "us-east-1"),
    ("export AWS_REGION=us-east-1", "AWS_REGION", "us-east-1"),
    ('AWS_REGION="us-east-1"', "AWS_REGION", "us-east-1"),
    ("AWS_REGION='us-east-1'", "AWS_REGION", "us-east-1"),
    ("  AWS_REGION = us-east-1  ", "AWS_REGION", "us-east-1"),
])
def test_the_parser_handles_the_shapes_a_credentials_file_actually_uses(
        tmp_path, line, key, val):
    f = tmp_path / ".env.local"
    f.write_text(line + "\n")
    assert env.parse(f)[key] == val


def test_comments_and_blank_lines_are_skipped(tmp_path):
    f = tmp_path / ".env.local"
    f.write_text("# a comment\n\nAWS_REGION=us-east-1\n")
    assert env.parse(f) == {"AWS_REGION": "us-east-1"}


def test_a_missing_file_is_not_an_error(tmp_path):
    """A deployment may supply credentials some other way."""
    assert env.parse(tmp_path / "nope") == {}


def test_describe_discloses_no_value():
    """It is printed in diagnostics, so it must be safe to print."""
    text = repr(env.describe())
    for value in env.parse().values():
        if value:
            assert value not in text


def test_fingerprints_distinguish_two_secrets_without_revealing_them():
    a, b = env.fingerprint("secret-one"), env.fingerprint("secret-two")
    assert a != b and len(a) == 10
    assert "secret" not in a


# The layer under test is the FINAL subprocess environment -- what the guard
# hands to the CLI -- not the intermediate options.env dict. An earlier
# revision tested the intermediate dict, passed, and every credential rode
# along anyway: the Agent SDK merges options.env OVER os.environ, so a key
# popped from the dict came straight back from the parent. `final_env`
# reproduces the whole chain: the SDK merge, then the guard's allowlist.
sys.path.insert(0, str(REPO / "tools"))
import cli_guard  # noqa: E402


def final_env(model: str) -> dict:
    merged = {**os.environ, **resolve._agent_env(model)}   # the SDK's merge
    return cli_guard.clean_env(merged)                      # the guard's filter


def test_a_bedrock_turn_does_not_carry_the_anthropic_key(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "frontier-only")
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "x")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "x")
    monkeypatch.setenv("AWS_REGION", "us-east-1")
    e = final_env("opus-4-6")
    assert "ANTHROPIC_API_KEY" not in e, (
        "the frontier-only key must not reach a Bedrock subprocess")
    assert e["CLAUDE_CODE_USE_BEDROCK"] == "1"
    assert e["AWS_ACCESS_KEY_ID"] == "x"


def test_an_anthropic_turn_does_not_carry_the_aws_keys(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "frontier-only")
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "x")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "x")
    monkeypatch.setenv("AWS_REGION", "us-east-1")
    e = final_env("opus-5")
    assert "AWS_ACCESS_KEY_ID" not in e and "AWS_SECRET_ACCESS_KEY" not in e
    # And the flag must be ABSENT, not merely false: its presence routes the
    # CLI to Bedrock and charges the wrong budget.
    assert "CLAUDE_CODE_USE_BEDROCK" not in e
    assert e["ANTHROPIC_API_KEY"] == "frontier-only"


def test_no_host_managed_credential_reaches_any_subprocess(monkeypatch):
    """The channel that billed $8.96 to the wrong account, pinned shut.

    The managed container's CLI login (CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST
    plus an OAuth token) silently served every 'anthropic' call while the
    configured key sat unused. The guard's allowlist must exclude every such
    channel for BOTH providers.
    """
    monkeypatch.setenv("ANTHROPIC_API_KEY", "k")
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "x")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "x")
    monkeypatch.setenv("AWS_REGION", "us-east-1")
    for marker in config.host_managed_auth_env():
        monkeypatch.setenv(marker, "host-injected")
    for model in ("opus-5", "opus-4-6"):
        e = final_env(model)
        for marker in config.host_managed_auth_env():
            assert marker not in e, (
                f"{marker} reaches the {model} subprocess; that is the exact "
                "channel that billed the wrong account")


def test_the_guard_gives_the_cli_a_private_home(monkeypatch):
    """~/.claude.json carries the machine owner's login; the CLI must not see it."""
    monkeypatch.setenv("ANTHROPIC_API_KEY", "k")
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "x")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "x")
    monkeypatch.setenv("AWS_REGION", "us-east-1")
    e = final_env("opus-5")
    assert e["HOME"] == str(resolve.CLI_HOME)
    assert e["HOME"] != os.path.expanduser("~"), (
        "the CLI's HOME must never be the real one -- that is where the "
        "on-disk login lives")


def test_the_guard_refuses_an_unconstrained_environment():
    """No allowlist means no exec. Failing open here is the original bug."""
    with pytest.raises(cli_guard.GuardConfigError):
        cli_guard.clean_env({"PATH": "/usr/bin", "MOHENARA_CLI_HOME": "/tmp/h"})
    with pytest.raises(cli_guard.GuardConfigError):
        cli_guard.clean_env({"PATH": "/usr/bin",
                             "MOHENARA_ENV_ALLOWLIST": "PATH"})


def test_the_resolver_execs_through_the_guard():
    """The guard only guards if the resolver actually uses it."""
    src = (REPO / "src" / "mohenara" / "resolve.py").read_text()
    assert "cli_path=str(CLI_GUARD)" in src, (
        "the resolver no longer execs through tools/cli_guard.py; every "
        "credential channel the guard closes is open again")


def test_a_missing_credential_raises_before_the_call(monkeypatch):
    monkeypatch.delenv("AWS_ACCESS_KEY_ID", raising=False)
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "x")
    monkeypatch.setenv("AWS_REGION", "us-east-1")
    with pytest.raises(RuntimeError, match="AWS_ACCESS_KEY_ID"):
        resolve._agent_env("opus-4-6")


def test_every_provider_declares_which_credentials_it_needs():
    """Stripping foreign credentials is only sound if the lists are complete."""
    for name, spec in config.providers().items():
        assert spec.get("credential_env") is not None, (
            f"provider {name} declares no credential_env, so nothing can know "
            "which variables to strip from another provider's subprocess")


def test_no_credential_value_is_committed_anywhere():
    """The invariant stated in CLAUDE.md, checked rather than trusted."""
    import subprocess
    values = [v for v in env.parse().values() if v and len(v) >= 12]
    if not values:
        pytest.skip("no .env.local in this checkout")
    tracked = subprocess.run(["git", "ls-files"], cwd=REPO,
                             capture_output=True, text=True).stdout.split()
    for rel in tracked:
        p = REPO / rel
        if not p.is_file() or p.stat().st_size > 2_000_000:
            continue
        try:
            text = p.read_text(errors="ignore")
        except OSError:
            continue
        for value in values:
            assert value not in text, f"a credential from .env.local appears in {rel}"
