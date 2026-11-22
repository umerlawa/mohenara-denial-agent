# Diagnosed: `denied_line_idxs` is off by one, and the prompt never says which base

Found while investigating the line-level metric, which reads **14.7% (5/34)**
in the final `edi` run against 85.7% joint. That gap was too large to be
reasoning error, so it was worth checking whether it was a definitional one.

## The measurement

Derived the denied service lines independently from each 835 — an `SVC` segment
carrying a `CAS` adjustment — and compared to what the system emitted. No labels
involved; this is the artifact against the prediction.

```
matches: 0   differs: 43   of which off-by-one: 36
  MOH2-000009  predicted [1, 2, 3, 4, 5]   835 CAS-bearing lines [0, 1, 2, 3, 4]
  MOH2-000011  predicted [1, 2, 3]         835 CAS-bearing lines [0, 1, 2]
  MOH2-000029  predicted [1, 2, 3]         835 CAS-bearing lines [0, 1, 2]
  MOH2-000052  predicted [1, 2, 3, 4, 5]   835 CAS-bearing lines [0, 1, 2, 3, 4]
  MOH2-000061  predicted [1, 2, 3, 4]      835 CAS-bearing lines [0, 1, 2, 3]
```

**36 of 43 are exactly one apart.** The system is emitting 1-based indices.

(The remaining 7 are not necessarily wrong. The comparison above treats any
`CAS` as a denial, which over-counts: a `CAS*PR*1` deductible is an adjustment,
not a denial. `MOH2-000022` predicted `[1]` where three lines carry some `CAS`,
and that may well be correct. The crude derivation is good enough to establish
the off-by-one and not good enough to judge the rest.)

## The cause

`schema/resolution.json` documents the contract:

> `"description": "Zero-based indices of the denied service lines."`

`src/mohenara/prompts.py` line 78 is the schema the **model** actually sees:

```python
"denied_line_idxs": {"type": "array", "items": {"type": "integer"}},
```

No description. Nothing in the system prompt or any reference card states the
base either. So the contract is *enforced* in one file and *communicated*
nowhere — and the model picked the convention the artifacts themselves use,
where `LX*1` is the first service line. That is the reasonable reading of an
unstated spec. The defect is the spec, not the inference.

## Why this is not being fixed mid-run

Same reason as the parking diagnosis: the prompt is frozen until both final
runs are done. Changing it now would invalidate cases already bought, break the
cached prefix, and mean `edi` and `md` ran different systems.

It matters less than parking, for one specific reason worth stating: the line
metric is **not** an exit criterion. Exit criterion 1 is joint accuracy over
root cause and next action, and that is 85.7%. The 14.7% understates a real
capability rather than revealing a missing one — the system is identifying the
denied lines correctly and numbering them from one.

## The fix, for after the runs

Add the description to `MODEL_OUTPUT_SCHEMA` in `prompts.py` so the model is
told the base, and add a line to the prompt making it explicit against the
`LX*n` convention it would otherwise inherit from the artifacts. Then re-measure
the line metric on a cheap slice.

Not "subtract one in the validator" — that would be guessing that every
disagreement is an off-by-one, and seven of the forty-three are not.
