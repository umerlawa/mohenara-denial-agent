# The runs stalled because Opus 4.6 is throttled, not because anything broke

## What the errors actually were

From roughly 03:18 UTC the eval runs began failing with:

    Exception: Claude Code returned an error result: success

A nonsense message — the SDK reads `message.get("error", ...)` off a result
envelope whose `error` field held the string `success`. It gave no indication
of the cause, and three cases exhausted every retry on it.

`tools/bedrock_preflight.py` names it directly:

    ThrottlingException  us.anthropic.claude-opus-4-6-v1

The CLI was swallowing a Bedrock `ThrottlingException` and surfacing it as that
string. Every "transient hiccup" in the logs from 03:18 onward is this.

## It is specific to one model, and that matters

Probed at the same moment, on the same credentials:

| model | probe |
|---|---|
| `us.anthropic.claude-opus-4-6-v1` | **ThrottlingException** |
| `us.anthropic.claude-sonnet-4-6` | SUCCESS |
| `us.anthropic.claude-opus-4-5` | SUCCESS |
| `us.anthropic.claude-haiku-4-5` | SUCCESS |
| `us.anthropic.claude-opus-4-7` / `4-8` / `opus-5` | NOT-ENTITLED (unchanged) |

So this is not the account, the credentials, the proxy, or the harness. It is a
per-model rate limit on the one model the matrix selected as the default.

## What it cost, and what it did not

Throttled attempts return no usage, so they are not billed — spend sat at
$32.49 across the whole stalled window. The cost was throughput, not money:
roughly one case per five minutes against 26 seconds before, and three cases
recorded as failures after exhausting their retries.

The retry backoff was lengthened to 5s/15s/45s over four attempts once the
burst pattern was visible. That is right for a brief throttle and still too
short for a quota window measured in tens of minutes.

## The decision, and the fallback that is ready

A watcher probes every two minutes and logs the moment it clears. If it does
not clear, the remaining work moves to `sonnet-4-6`, which is available now and
costs about three quarters of Opus per case.

Switching is defensible on the evidence rather than merely forced. The matrix
chose Opus on five-case cells, and `results/matrix.md` already records that no
accuracy difference in that table is statistically meaningful — while the
15-case calibration ranked the models the other way round, at 86.7% for Sonnet
against 73.3% for Opus. The default was always a thin choice; availability now
decides it.

Any such switch is recorded here and in the run's own `run.json`, never
silently.
