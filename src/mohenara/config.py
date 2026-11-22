"""Provider and model registry, loaded from config/models.json.

Model IDs and provider wiring are configuration, not code: swapping a model,
or moving one between providers, is a JSON edit. Rates live here too so a
pricing change cannot require touching the resolver.
"""
from __future__ import annotations

import functools
import json
import os
import pathlib

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
CONFIG_PATH = REPO_ROOT / "config" / "models.json"


class UnknownModel(KeyError):
    pass


@functools.lru_cache(maxsize=1)
def _cfg() -> dict:
    return json.loads(CONFIG_PATH.read_text())


def all_models() -> dict:
    return dict(_cfg()["models"])


def model_names() -> list[str]:
    return sorted(_cfg()["models"])


def model(name: str) -> dict:
    """Resolve an alias (`opus-4-6`) or a raw model id to its config entry."""
    models = _cfg()["models"]
    if name in models:
        return {"alias": name, **models[name]}
    for alias, spec in models.items():
        if spec["id"] == name:
            return {"alias": alias, **spec}
    raise UnknownModel(
        f"{name!r} is not in config/models.json. Add it there rather than "
        "hardcoding a model id, so swapping models stays a config change."
    )


def provider_names() -> list[str]:
    return sorted(_cfg()["providers"])


def host_managed_auth_env() -> list[str]:
    """Credential channels the CLI can use besides a provider's own keys.

    The resolver strips every one of these from its subprocess. The list lives
    in config/models.json rather than in code because it is part of the same
    statement the registry makes -- WHICH account a model bills -- and it was
    the unstated half of that statement that let a managed container's own
    login serve $8.96 of calls the project's API key never saw.
    """
    return list(_cfg().get("host_managed_auth_env", []))


def subprocess_env_allowlist() -> list[str]:
    """The ONLY ambient variables the resolver's CLI subprocess may keep.

    Default-deny, because two denylists failed in sequence: the SDK's env
    overlay resurrected popped keys, and the CLI then authenticated from its
    on-disk login with every env channel closed. The provider's own
    credential_env and env flags are added on top of this list at spawn time.
    """
    return list(_cfg().get("subprocess_env_allowlist", []))


def providers() -> dict[str, dict]:
    """Every provider, name -> spec, without the env-override handling.

    For callers that need to reason about providers other than the one they are
    using -- stripping a foreign provider's credentials out of a subprocess, for
    one. `provider()` is still the way to get the spec you intend to spend on.
    """
    return {name: {"name": name, **spec}
            for name, spec in _cfg()["providers"].items()}


def committed_provider(name: str) -> dict:
    """The provider exactly as config/models.json declares it.

    No environment overrides. For assertions about what the repository ships --
    the build guardrails -- as distinct from what a given deployment is running
    at. The two are different questions and conflating them made the test suite
    fail whenever a deployment legitimately raised its own cap.
    """
    spec = _cfg()["providers"].get(name)
    if spec is None:
        raise UnknownModel(f"no provider {name!r} in config/models.json")
    return {"name": name, **spec}


def provider(name: str) -> dict:
    spec = committed_provider(name)

    # Env overrides, so a deployment can raise its own caps without editing a
    # tracked file. The caps in config/models.json were build guardrails; a
    # demo or a production deployment has different limits, and editing the
    # committed file to say so means a merge conflict on every pull.
    #
    #   MOHENARA_BUDGET_BEDROCK=250      -> the hard refuse ceiling
    #   MOHENARA_STOP_BEDROCK=200        -> the soft stop for eval runs
    #
    # Raising a cap is deliberate either way: the gate itself, the per-call
    # accounting and the separation between providers are unchanged, and a
    # malformed value raises rather than silently reverting to the default.
    for env_key, field in ((f"MOHENARA_BUDGET_{name.upper()}", "budget_usd"),
                           (f"MOHENARA_STOP_{name.upper()}", "stop_eval_usd")):
        raw = os.environ.get(env_key)
        if raw is None or not raw.strip():
            continue
        try:
            value = float(raw)
        except ValueError as exc:
            raise ValueError(
                f"{env_key}={raw!r} is not a number. A budget the guard cannot "
                "parse must not fall back to a default -- fix or unset it."
            ) from exc
        if value < 0:
            raise ValueError(f"{env_key}={raw!r} is negative")
        spec[field] = value

    if spec["stop_eval_usd"] > spec["budget_usd"]:
        raise ValueError(
            f"provider {name!r}: eval stop ${spec['stop_eval_usd']:.2f} is above "
            f"the refuse ceiling ${spec['budget_usd']:.2f}, so the stop can never "
            "fire and eval runs would spend to the hard cap."
        )
    return spec


def provider_for(model_name: str) -> dict:
    return provider(model(model_name)["provider"])


def defaults() -> dict:
    return {k: v for k, v in _cfg()["default"].items() if not k.startswith("_")}


def serving_provider() -> str:
    """The one provider the operator and internal apps may spend on.

    Read from config/models.json rather than hardcoded, because which provider
    serves the apps is a deployment decision that has already changed once: the
    build ran on Bedrock, and the apps now serve opus-5, which this AWS account
    is not entitled to and which only the first-party Anthropic API can reach.
    A constant in the source would have made that a code change.
    """
    return _cfg().get("serving_provider", "bedrock")


class DefaultUnservable(RuntimeError):
    """The configured default cannot serve denials in this deployment."""


def check_default() -> dict:
    """Validate the serving default at import time, not at first denial.

    This exists because the default was once set to a model that only the
    Anthropic API serves. Nothing complained until an operator submitted a real
    denial, which then failed four retries deep with a credentials error -- the
    worst possible moment and the least legible message. The three things that
    can be wrong are all knowable before any request arrives, so they are
    checked here.
    """
    d = defaults()
    try:
        spec = model(d["model"])
    except UnknownModel as exc:
        raise DefaultUnservable(f"default model {d['model']!r}: {exc}") from exc

    serving = serving_provider()
    if spec["provider"] != serving:
        raise DefaultUnservable(
            f"default model {d['model']!r} is served by {spec['provider']!r}, "
            f"but the apps may only spend on {serving!r}. "
            f"{spec.get('note', '')}".strip())
    if d["effort"] not in spec.get("efforts", []):
        raise DefaultUnservable(
            f"default effort {d['effort']!r} is not offered by {d['model']!r}; "
            f"it accepts {spec.get('efforts')}")
    if d.get("input_format") not in ("md", "edi"):
        raise DefaultUnservable(
            f"default input_format {d.get('input_format')!r} must be md or edi")
    return d
