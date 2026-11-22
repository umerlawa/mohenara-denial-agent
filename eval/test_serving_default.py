"""The default the apps serve denials with must be servable. Offline.

This exists because it was not. The default was set to `opus-5` at high effort
-- the strongest model in the frontier comparison, and a reasonable thing to
want -- but opus-5 is registered on the Anthropic provider, and this AWS account
is NOT-ENTITLED to it on Bedrock. Nothing complained at startup. The first real
denial an operator submitted failed four retries deep with a credentials error,
and the Playwright suite reported it as three unrelated journey failures.

Two separate defects, both checked here:

  1. The default named a provider the serving apps may not spend on. The
     Anthropic budget in this repo is scoped to the frontier comparison phase;
     routing operator traffic there would spend the wrong ledger.
  2. Nothing validated the default before the first request. A misconfiguration
     knowable at import time surfaced at the worst possible moment instead.
"""
from __future__ import annotations

import pathlib
import sys

import pytest

REPO = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "src"))

from mohenara import config  # noqa: E402


def test_default_is_servable():
    """The whole guard, exactly as the apps call it at startup."""
    assert config.check_default()["model"]


def test_default_model_is_on_the_serving_provider():
    spec = config.model(config.defaults()["model"])
    assert spec["provider"] == config.serving_provider(), (
        f"the apps serve denials on {config.serving_provider()!r}; a default on "
        f"{spec['provider']!r} spends a budget the deployment did not intend "
        "for operator traffic")


def test_default_effort_is_offered_by_the_default_model():
    d = config.defaults()
    assert d["effort"] in config.model(d["model"])["efforts"]


def test_default_model_is_priced():
    """A model with no rates must raise rather than read as free."""
    assert config.model(config.defaults()["model"])["rates"]


def _a_model(*, on_serving: bool) -> str:
    """A registered model on (or off) the configured serving provider.

    The negative fixtures below used to name models outright, which pinned
    them to the committed serving provider -- and the one sanctioned reason to
    flip that provider (a temporary Bedrock shakedown of the demo flow) turned
    three of them red on a perfectly healthy checkout. Computed from config,
    the same guard checks run whichever way the provider points.
    """
    serving = config.serving_provider()
    effort = config.defaults()["effort"]
    for name in sorted(config.all_models()):
        spec = config.model(name)
        if (spec["provider"] == serving) != on_serving:
            continue
        # An on-provider pick must offer the default effort, or the effort
        # check fires before the one the fixture is aiming at.
        if on_serving and effort not in spec["efforts"]:
            continue
        return name
    pytest.skip("the registry has no model fitting this fixture")


@pytest.mark.parametrize("kind,expect", [
    ("off-provider", "may only spend"),
    ("bad-effort", "not offered"),
    ("bad-format", "md or edi"),
    ("unknown-model", "default model"),
])
def test_the_guard_rejects_what_it_is_there_to_reject(monkeypatch, kind, expect):
    """A guard that never fires is indistinguishable from no guard."""
    bad = dict(config.defaults())
    if kind == "off-provider":
        bad["model"] = _a_model(on_serving=False)
    elif kind == "bad-effort":
        bad.update(model=_a_model(on_serving=True), effort="turbo")
    elif kind == "bad-format":
        bad.update(model=_a_model(on_serving=True), input_format="pdf")
    else:
        bad["model"] = "no-such-model"
    monkeypatch.setattr(config, "defaults", lambda: dict(bad))
    with pytest.raises(config.DefaultUnservable) as exc:
        config.check_default()
    assert expect in str(exc.value)


def test_the_serving_app_runs_the_guard_at_import():
    """Not just available -- actually wired into the app that needs it."""
    src = (REPO / "src" / "mohenara" / "api.py").read_text()
    assert "config.check_default()" in src, (
        "the operator app must validate its default at import, or a bad "
        "default is discovered by an operator rather than by startup")


def test_every_model_the_apps_cannot_serve_says_why_in_the_registry():
    """The registry has to carry the reason, or the next person re-picks it.

    Written against whichever models are off the serving provider rather than a
    fixed list, so it keeps meaning something when the serving provider changes
    -- which it has, once.
    """
    serving = config.serving_provider()
    off = [n for n, m in config.all_models().items() if m["provider"] != serving]
    assert off, "nothing to check: every registered model is on the serving provider"
    for name in off:
        spec = config.model(name)
        # Either the model explains itself or its provider does. Most models on
        # the non-serving provider are unremarkable -- the provider's own note
        # covers them. A model that is off it for a reason of its own, like a
        # frontier model this account cannot invoke, has to say so itself.
        note = spec.get("note", "") or config.provider(spec["provider"]).get("note", "")
        assert note.strip(), (
            f"{name} cannot serve the apps and neither it nor provider "
            f"{spec['provider']!r} says why")


def test_the_serving_provider_is_a_real_provider():
    assert config.serving_provider() in config.provider_names()


@pytest.mark.headroom
def test_the_serving_provider_has_headroom_left():
    """Is there money left to demo with. NOT a correctness check.

    Deliberately kept OUT of verify-offline, behind `make verify-headroom`.
    It asserts a fact about this deployment's wallet, not about the code, and
    the two must not be conflated: a correct checkout reporting red because a
    budget ran out is the same mistake that made the budget-isolation tests
    read the deployment's caps while asserting the shipped ones.

    Run it before a demo. It fails while there is under one denial of headroom,
    so the budget runs out in a test rather than in front of a client.
    """
    from mohenara import spend

    name = config.serving_provider()
    left = config.provider(name)["budget_usd"] - spend.provider_total(name)
    assert left > 0.40, (
        f"[{name}] ${left:.2f} left, which is under one denial at the current "
        f"default. Raise budget_usd in config/models.json, or set "
        f"MOHENARA_BUDGET_{name.upper()}, before demoing to anyone.")
