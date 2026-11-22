#!/usr/bin/env python3
"""Exec the Claude Code CLI with nothing but the credentials it is meant to have.

This is the resolver's cli_path. It exists because every denylist failed:

  1. The Agent SDK builds the subprocess env as {**os.environ, **options.env},
     so keys POPPED from options.env silently come back from the parent.
  2. Keys BLANKED to "" closed the env channel, and the CLI still
     authenticated: its on-disk state (~/.claude.json, `oauthAccount`) carries
     the login of whoever owns the machine -- the managed container's session
     here, the developer's personal account on a laptop. File descriptors
     injected by a managed launcher are a third channel.

A denylist cannot enumerate channels it does not know about, and each miss is
silent: the call succeeds and someone else gets billed. So this wrapper is
DEFAULT-DENY on all three:

  env   rebuilt from the explicit allowlist in config/models.json
        (subprocess_env_allowlist) plus whatever the resolver passed through
        MOHENARA_ENV_ALLOWLIST -- the provider's own credentials and flags.
  disk  HOME is pointed at a private, empty directory, so ~/.claude.json and
        any credentials file belong to this project and start blank.
  fds   everything above stderr is closed before exec.

The proof of correctness is behavioural, not this file: tools/
anthropic_auth_probe.py step 1 runs the pipeline with a bogus key and MUST see
an auth failure. If any credential channel survives, that probe fails loudly.
"""
from __future__ import annotations

import os
import sys


class GuardConfigError(ValueError):
    """The guard's own contract is broken; refuse rather than run unguarded."""


def clean_env(environ: dict) -> dict:
    """The environment the CLI actually gets. Pure, so the tests test THIS.

    The first regression here passed its tests while every credential rode
    along anyway, because the tests read an intermediate dict and not the
    layer that reached the subprocess. This function IS that layer now.
    """
    allow = [k for k in environ.get("MOHENARA_ENV_ALLOWLIST", "").split(",") if k]
    if not allow:
        raise GuardConfigError("empty MOHENARA_ENV_ALLOWLIST; refusing to exec "
                               "with an unconstrained environment")
    home = environ.get("MOHENARA_CLI_HOME")
    if not home:
        raise GuardConfigError("MOHENARA_CLI_HOME not set")

    clean = {k: environ[k] for k in allow
             if k in environ and environ[k] != ""}
    clean["HOME"] = home
    return clean


def main() -> None:
    real = os.environ.get("MOHENARA_REAL_CLI")
    if not real or not os.path.exists(real):
        sys.stderr.write("cli_guard: MOHENARA_REAL_CLI not set or missing\n")
        raise SystemExit(96)

    try:
        clean = clean_env(dict(os.environ))
    except GuardConfigError as exc:
        sys.stderr.write(f"cli_guard: {exc}\n")
        raise SystemExit(97) from exc

    os.makedirs(clean["HOME"], exist_ok=True)

    # Publish the PID that is about to BECOME the CLI (execve keeps it), so a
    # cancel request can terminate the in-flight call instead of watching it
    # spend. Written before exec, best-effort: a cancel facility must never be
    # the reason a resolve fails to start.
    pidfile = os.environ.get("MOHENARA_PIDFILE")
    if pidfile:
        try:
            with open(pidfile, "w") as f:
                f.write(str(os.getpid()))
        except OSError:
            pass

    # Launcher-injected credentials can ride on inherited descriptors.
    os.closerange(3, 256)

    os.execve(real, [real] + sys.argv[1:], clean)


if __name__ == "__main__":
    main()
