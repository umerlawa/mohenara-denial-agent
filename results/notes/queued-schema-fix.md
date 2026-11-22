# Queued: the one schema gap that has actually cost a case

Not applied yet, deliberately. Changing the model-facing contract mid-run would
mean the final numbers described two different configurations. Applied
immediately after the Bedrock runs finish.

## The gap

`schema/resolution.json` makes the two states disjoint with `allOf`/`if`/`then`:
`status: resolved` **requires** `resolution`, `status: awaiting_human`
**requires** `awaiting_human`.

`MODEL_OUTPUT_SCHEMA` in `src/mohenara/prompts.py` has top-level
`required: ["status", "rationale"]` and nothing conditional. So
`{"status": "resolved", "rationale": "..."}` with no `resolution` object
satisfies the schema the model is given and fails the validator that decides
whether to persist.

Most of the model schema is fine — the family and path enums, `evidence`
`minItems: 1`, and the nested `required` lists are all present. This is the
narrow remainder.

## What it has cost

One case in roughly 700 calls: `MOH2-000105` in `results/nothink-sonnet-low/`,
whose recorded failure reads:

    'root_cause' is a required property
    'next_action' is a required property
    'evidence' ...

The call was billed, the answer was discarded, and the case scored as wrong.
0.14% incidence — which is why it is queued rather than rushed.

## The fix, and why not the obvious one

The obvious fix is to mirror the `allOf`/`if`/`then` into `MODEL_OUTPUT_SCHEMA`.
Not doing that: structured-output implementations accept a restricted JSON
Schema subset, conditional keywords are commonly outside it, and a schema the
API rejects would break **every** call rather than 1 in 700. That is a bad
trade to make on an assumption.

Instead:

1. **Move schema validation inside the retry loop.** Today validation runs
   after the loop, so an invalid resolution is raised and thrown away. Inside
   the loop it becomes a retryable failure like any other — the model gets
   another attempt with the same prompt, and the first attempt's cost is
   already recorded in the ledger. This fixes the whole class, not just this
   instance: any validator rejection the model could correct on a second look
   now gets one.
2. **Add `blocks.minItems: 1`** to the model schema. The validator requires a
   non-empty `blocks` array and the model schema does not say so.
3. **Sharpen the prompt.** It already says "resolved carries `resolution`;
   awaiting_human carries `awaiting_human`. Never both." Make it also say
   *never neither*.

## Verification

One live call after the change, to confirm structured output still works at
all — the failure mode being guarded against is a schema the API silently
rejects. Then the offline suites.
