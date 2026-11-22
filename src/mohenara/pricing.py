"""Pricing and cost arithmetic. Deterministic: no model calls.

The Claude Agent SDK reports `total_cost_usd` at Anthropic FIRST-PARTY rates
even when the request is served by Bedrock. Every dollar figure this project
reports is recomputed here from raw token counts against the Bedrock rate
card, so a pricing mistake surfaces as a failing replay test rather than a
quietly wrong number in results/.

Rates are US East `us.*` cross-region inference profiles, USD per million
tokens, captured 2026-08-12.
"""
from __future__ import annotations

from . import config

MILLION = 1_000_000


def rates_for(model_name: str) -> dict:
    """Per-million-token rates from config. Raises if the model has none.

    A model with `rates: null` (a frontier model whose pricing has not been
    looked up yet) must RAISE, not cost $0.00 -- a silent zero would make the
    budget ceiling unenforceable, which is the one failure this module exists
    to prevent.
    """
    spec = config.model(model_name)
    if not spec.get("rates"):
        raise KeyError(
            f"{model_name!r} has no rates in config/models.json "
            f"({spec.get('rates_note', '')}). Populate them before spending: "
            "a missing rate must never read as $0.00."
        )
    return spec["rates"]


def resolve_model(name: str) -> str:
    """Alias or raw id -> the provider's real model id."""
    try:
        return config.model(name)["id"]
    except config.UnknownModel:
        return name


def cost_usd(model: str, *, input_tokens: int, output_tokens: int,
             cache_creation_input_tokens: int = 0,
             cache_read_input_tokens: int = 0) -> float:
    r = rates_for(model)
    return (
        input_tokens * r["input"]
        + output_tokens * r["output"]
        + cache_creation_input_tokens * r["cache_write_5m"]
        + cache_read_input_tokens * r["cache_read"]
    ) / MILLION


def _pick(usage: dict, *names: str) -> int:
    for n in names:
        if usage.get(n) is not None:
            return int(usage[n])
    return 0


def cost_from_usage(model: str, usage: dict) -> float:
    """Cost from a usage dict, tolerating snake_case or camelCase."""
    return cost_usd(
        model,
        input_tokens=_pick(usage, "input_tokens", "inputTokens"),
        output_tokens=_pick(usage, "output_tokens", "outputTokens"),
        cache_creation_input_tokens=_pick(usage, "cache_creation_input_tokens", "cacheCreationInputTokens"),
        cache_read_input_tokens=_pick(usage, "cache_read_input_tokens", "cacheReadInputTokens"),
    )


def cache_hit_rate(usage: dict) -> float:
    """Share of prompt tokens served from cache. 0.0 when nothing was read."""
    read = _pick(usage, "cache_read_input_tokens", "cacheReadInputTokens")
    total = (read + _pick(usage, "input_tokens", "inputTokens")
             + _pick(usage, "cache_creation_input_tokens", "cacheCreationInputTokens"))
    return round(read / total, 6) if total else 0.0
