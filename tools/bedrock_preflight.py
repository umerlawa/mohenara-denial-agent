#!/usr/bin/env python3
"""Bedrock access preflight.

Answers one question: which models can this account actually invoke?

Distinguishes the two failure modes that look alike but need different fixes:
  IAM-DENIED   -> the IAM policy does not permit InvokeModel on that ARN.
                  Fix: broaden the identity policy.
  MARKETPLACE  -> the model is Marketplace-gated and the principal lacks the
                  aws-marketplace:* actions. Fix: add aws-marketplace:Subscribe
                  and aws-marketplace:ViewSubscriptions to the identity policy.
  NOT-ENTITLED -> IAM passed; the account lacks Bedrock model access.
                  Fix: Bedrock console -> Model access (not an IAM change).

Reads AWS creds from the environment (see gitignored .env.local).
Prints no credential material.

    python tools/bedrock_preflight.py            # probe the model ladder
    python tools/bedrock_preflight.py --list     # enumerate visible models
"""
from __future__ import annotations

import argparse
import os
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "src"))

from mohenara import pricing, spend  # noqa: E402

# Ladder is ordered best-first: the first SUCCESS is the model to build on.
LADDER = [
    "us.anthropic.claude-opus-5",
    "us.anthropic.claude-sonnet-5",
    "us.anthropic.claude-opus-4-8",
    "us.anthropic.claude-opus-4-7",
    "us.anthropic.claude-opus-4-6-v1",
    "us.anthropic.claude-opus-4-5-20251101-v1:0",
    "us.anthropic.claude-sonnet-4-6",
    "us.anthropic.claude-sonnet-4-5-20250929-v1:0",
    "us.anthropic.claude-haiku-4-5-20251001-v1:0",
    # Non-Anthropic fallbacks, strongest first.
    "us.amazon.nova-premier-v1:0",
    "us.deepseek.r1-v1:0",
    "zai.glm-5",
    "openai.gpt-oss-120b-1:0",
    "us.meta.llama3-3-70b-instruct-v1:0",
    "qwen.qwen3-32b-v1:0",
    "qwen.qwen3-vl-235b-a22b",
    "qwen.qwen3-coder-30b-a3b-v1:0",
    "deepseek.v3.2",
    "zai.glm-4.7",
    "moonshot.kimi-k2-thinking",
    "mistral.mistral-large-3-675b-instruct",
    "writer.palmyra-x5-v1:0",
]


def classify(exc: Exception) -> str:
    """Map an invoke failure onto the fix that resolves it."""
    msg = str(exc)
    if "not available for this account" in msg:
        return "NOT-ENTITLED"
    # Marketplace-gated models report an IAM-shaped error, but the missing
    # actions are aws-marketplace:*, not bedrock:*. Check before IAM-DENIED.
    if "Marketplace" in msg:
        return "MARKETPLACE"
    if "not authorized" in msg:
        return "IAM-DENIED"
    if "invalid" in msg.lower() or "ResourceNotFound" in type(exc).__name__:
        return "INVALID-ID"
    return type(exc).__name__


def _record_probe(model_id: str, usage: dict) -> float:
    """Charge a probe to the ledger. Every call that spends must be visible.

    A ladder model is often NOT in config/models.json -- discovering whether it
    exists is the point of the ladder -- so its rates are unknown. It is priced
    at the most expensive registered Bedrock rate. Over-counting is the only
    safe direction here: a call recorded at $0.00 silently reopens a budget
    that may already be exhausted.
    """
    try:
        rates = pricing.rates_for(model_id)
        bounded = False
    except KeyError:
        rates = spend.upper_bound_rates("bedrock")
        bounded = True
    norm = {
        "input_tokens": usage.get("inputTokens", 0),
        "output_tokens": usage.get("outputTokens", 0),
        "cache_read_input_tokens": usage.get("cacheReadInputTokens", 0),
        "cache_creation_input_tokens": usage.get("cacheWriteInputTokens", 0),
    }
    cost = (norm["input_tokens"] * rates["input"]
            + norm["output_tokens"] * rates["output"]
            + norm["cache_read_input_tokens"] * rates["cache_read"]
            + norm["cache_creation_input_tokens"] * rates["cache_write_5m"]) / 1e6
    spend.record(run_id="preflight", case_id=model_id,
                 model=("us.anthropic.claude-opus-4-6-v1" if bounded else model_id),
                 effort="n/a", usage=norm, cost=cost)
    return cost


def probe(runtime, model_id: str) -> tuple[str, str]:
    """Invoke a model with a minimal prompt. Returns (status, detail).

    Gated and recorded like any other call. The probe is small -- roughly 20
    input and 16 output tokens -- but "small" is not the same as "exempt", and
    an unrecorded call is spend the budget ceiling can never see.
    """
    try:
        spend.check_provider("bedrock")
    except spend.BudgetExceeded as exc:
        return "BUDGET-STOP", str(exc)
    try:
        resp = runtime.converse(
            modelId=model_id,
            messages=[{"role": "user", "content": [{"text": "Reply with the single word: OK"}]}],
            inferenceConfig={"maxTokens": 16},
        )
        usage = resp.get("usage", {})
        text = resp["output"]["message"]["content"][0].get("text", "").strip()
        cost = _record_probe(model_id, usage)
        return "SUCCESS", (f"{text!r} in={usage.get('inputTokens')} "
                           f"out={usage.get('outputTokens')} ${cost:.6f}")
    except Exception as exc:  # noqa: BLE001 - classification is the point
        return classify(exc), ""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--list", action="store_true", help="enumerate visible models and exit")
    parser.add_argument("--region", default=os.environ.get("AWS_REGION", "us-east-1"))
    args = parser.parse_args()

    try:
        import boto3
    except ImportError:
        print("boto3 not installed: pip install boto3", file=sys.stderr)
        return 2

    if not os.environ.get("AWS_ACCESS_KEY_ID"):
        print("AWS_ACCESS_KEY_ID unset. Load .env.local first:", file=sys.stderr)
        print("  set -a && . ./.env.local && set +a", file=sys.stderr)
        return 2

    identity = boto3.client("sts", region_name=args.region).get_caller_identity()
    print(f"identity : {identity['Arn']}")
    print(f"region   : {args.region}\n")

    if args.list:
        control = boto3.client("bedrock", region_name=args.region)
        summaries = control.list_foundation_models()["modelSummaries"]
        by_provider: dict[str, list[str]] = {}
        for summary in summaries:
            by_provider.setdefault(summary.get("providerName", "?"), []).append(summary["modelId"])
        print(f"{len(summaries)} models visible across {len(by_provider)} providers")
        for provider, ids in sorted(by_provider.items()):
            print(f"\n{provider} ({len(ids)}):")
            for model_id in sorted(ids):
                print(f"    {model_id}")
        return 0

    runtime = boto3.client("bedrock-runtime", region_name=args.region)
    working = []
    for model_id in LADDER:
        status, detail = probe(runtime, model_id)
        print(f"{status:14} {model_id} {detail}".rstrip())
        if status == "SUCCESS":
            working.append(model_id)

    print()
    if working:
        print(f"INVOKABLE ({len(working)}): {', '.join(working)}")
        print(f"Best available: {working[0]}")
        return 0

    print("INVOKABLE: NONE — nothing on the ladder can be called.")
    print("Read the status column: IAM-DENIED needs a policy change;")
    print("NOT-ENTITLED needs Bedrock model access on the account.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

# --- Capability facts verified against Bedrock on 2026-08-12 -------------------
# us.anthropic.claude-opus-4-6-v1  and  us.anthropic.claude-sonnet-4-6
#   InvokeModel via AnthropicBedrock ... OK
#   output_config.effort ............... low | medium | high | max
#                                        (xhigh rejected: 400, arrived in 4.7)
#   thinking {type: adaptive} .......... OK, returns thinking blocks
#   thinking display=summarized ........ OK
#   prompt caching ..................... cache_write 9635 -> cache_read 9635
#                                        (Opus 4.6 needs >=4096-token prefix)
# Non-Anthropic models on this account reject cachePoint outright:
#   "You invoked an unsupported model or your request did not allow prompt
#    caching" - so cache-read accounting is unavailable on them.
