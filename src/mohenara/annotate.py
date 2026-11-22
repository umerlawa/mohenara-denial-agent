"""Anchor the model's findings onto the real input. Deterministic: no model calls.

This module is the reason the demo view can be trusted. A screen that highlights
"the three lines missing a GP modifier" is worth nothing if the frontend found
those lines by looking for SV1 segments itself -- that would be the demo's own
analysis wearing the model's clothes, and it would keep highlighting confidently
on a case the model got wrong.

So the direction of travel is fixed: the model names the segments it used,
verbatim, and this module MATCHES those quotations against the artifact bytes.
Nothing is highlighted that the model did not quote, and nothing is highlighted
where the quotation does not actually occur in the input. A finding whose
quotation cannot be found is reported as unanchored rather than being placed
somewhere plausible.

The same rule governs the corrected claim. The model supplies segment
replacements, not a rewritten file, and `apply_corrections` applies them to the
real artifact -- so every line the view paints green is a line that genuinely
differs from the input, and every other line is byte-identical by construction
rather than by trust.
"""
from __future__ import annotations

import json
import re

# `render_edi` writes each artifact as "## Heading -- `name.edi`" followed by a
# fenced block. Parsing it back is how the demo recovers the raw artifacts for
# both entry points at once -- an uploaded set and a corpus case reach this
# module in the same shape, so neither can drift from the other.
_ARTIFACT_HEADING = re.compile(r"^##\s+.*?--\s+`([^`]+)`\s*$")


def artifacts_from_rendered(rendered: str) -> dict[str, str]:
    """{filename: contents} recovered from a rendered case."""
    out: dict[str, str] = {}
    name: str | None = None
    fence = False
    buf: list[str] = []
    for line in rendered.splitlines():
        m = _ARTIFACT_HEADING.match(line)
        if m and not fence:
            name = m.group(1)
            buf = []
            continue
        if name and line.strip() == "```":
            if fence:                       # closing
                out[name] = "\n".join(buf)
                name, fence, buf = None, False, []
            else:
                fence = True
            continue
        if fence:
            buf.append(line)
    return out


def _lines(text: str) -> list[str]:
    return text.splitlines()


def _find(haystack: list[str], quote: str, hint: int | None) -> int | None:
    """1-based line of `quote` in `haystack`, or None.

    Compared on stripped text: the artifacts are wrapped and re-indented on
    their way through the renderer, and a leading space is not a difference
    worth refusing an anchor over. Everything else must match exactly -- a
    substring match would let "SV1" alone light up three lines.
    """
    needle = quote.strip()
    if not needle:
        return None
    hits = [i for i, ln in enumerate(haystack, 1) if ln.strip() == needle]
    if len(hits) == 1:
        return hits[0]
    if not hits:
        return None
    # Ambiguous: several identical lines. The model's own line number breaks the
    # tie if it points at one of them; otherwise the reference is not specific
    # enough to anchor and must not be placed arbitrarily.
    return hint if hint in hits else None


def _find_all(haystack: list[str], quote: str, hint: int | None) -> list[int]:
    """Every 1-based line whose stripped text equals `quote`, for annotation.

    Same equality rule as `_find`, different ambiguity rule. An EDI claim
    repeats identical segments -- the same `LQ*HE*N822~` on every denied
    service line -- and a model that cites that segment has cited a line that
    is byte-identical wherever it occurs. Highlighting every occurrence states
    exactly that and nothing more, so annotations take all of them (unless the
    model's own line number picks one). Corrections still go through `_find`:
    an edit must land on exactly one line or be dropped, because rewriting a
    line the model did not mean is a fabrication, not a highlight.
    """
    needle = quote.strip()
    if not needle:
        return []
    hits = [i for i, ln in enumerate(haystack, 1) if ln.strip() == needle]
    if hint in hits:
        return [hint]
    return hits


def annotations(resolution: dict, artifacts: dict[str, str]) -> dict:
    """Turn the model's evidence into anchored annotations.

    Returns {"anchored": [...], "unanchored": [...]}. An annotation carries the
    artifact, the 1-based line, the quoted text, the chip and the severity. The
    caller renders exactly this and reads nothing else out of the input.
    """
    anchored: list[dict] = []
    unanchored: list[dict] = []

    for item in (resolution or {}).get("evidence") or []:
        artifact = item.get("artifact")
        chip = (item.get("chip") or item.get("fact") or "").strip()
        severity = item.get("severity") or "context"
        segments = item.get("segments") or []

        if not segments:
            # Evidence without a segment reference is still evidence -- it is
            # just not placeable. Older predictions are all of this kind.
            unanchored.append({"artifact": artifact, "chip": chip,
                               "severity": severity, "reason": "no segment cited"})
            continue

        body = artifacts.get(artifact)
        if body is None:
            unanchored.append({"artifact": artifact, "chip": chip,
                               "severity": severity,
                               "reason": f"artifact {artifact!r} is not in this case"})
            continue

        rows = _lines(body)
        for seg in segments:
            quote = seg.get("text") or ""
            lines = _find_all(rows, quote, seg.get("line"))
            if not lines:
                unanchored.append({
                    "artifact": artifact, "chip": chip, "severity": severity,
                    "quote": quote,
                    "reason": "quoted segment does not occur in the artifact",
                })
                continue
            for line in lines:
                anchored.append({
                    "artifact": artifact, "line": line, "text": rows[line - 1],
                    "chip": chip, "severity": severity,
                    "segment_id": seg.get("id"),
                    "fact": item.get("fact"),
                })

    anchored.sort(key=lambda a: (a["artifact"], a["line"]))
    return {"anchored": anchored, "unanchored": unanchored}


def apply_corrections(corrected: dict | None, artifacts: dict[str, str]) -> dict | None:
    """Apply the model's segment replacements to the real artifact.

    Returns the corrected text plus the exact lines that changed, so the view
    can paint those green and nothing else. Every unchanged line is unchanged by
    construction: this only ever replaces lines the model quoted and that were
    found verbatim.

    Returns None when there is no corrected claim -- a decision-only resolution
    such as do_not_resubmit produces no file, and the caller shows a resolution
    card instead.
    """
    if not corrected:
        return None
    artifact = corrected.get("artifact")
    body = artifacts.get(artifact)
    if body is None:
        return {"artifact": artifact, "text": None, "changed": [], "dropped": [
            {"before": e.get("before"), "reason": f"artifact {artifact!r} not in this case"}
            for e in corrected.get("edits") or []],
            "note": corrected.get("note")}

    rows = _lines(body)
    changed: list[dict] = []
    dropped: list[dict] = []
    taken: set[int] = set()

    for edit in corrected.get("edits") or []:
        before = edit.get("before") or ""
        line = _find(rows, before, edit.get("line"))
        if line is None or line in taken:
            dropped.append({
                "before": before, "why": edit.get("why"),
                "reason": ("segment already replaced by an earlier edit"
                           if line in taken else
                           "quoted segment does not occur in the artifact"),
            })
            continue
        after = edit.get("after") or ""
        taken.add(line)
        # Preserve the original indentation so the diff is about the segment,
        # not about whitespace the model did not intend to change.
        indent = rows[line - 1][:len(rows[line - 1]) - len(rows[line - 1].lstrip())]
        rows[line - 1] = indent + after.strip()
        changed.append({"line": line, "before": before.strip(),
                        "after": after.strip(), "why": edit.get("why")})

    changed.sort(key=lambda c: c["line"])
    return {"artifact": artifact, "text": "\n".join(rows), "changed": changed,
            "dropped": dropped, "note": corrected.get("note")}


# --- streaming ---------------------------------------------------------------

_TRAILING_ESCAPE = re.compile(r'(?<!\\)(?:\\\\)*\\(?:u[0-9a-fA-F]{0,3})?$')


def _complete_object(buffer: str, start: int) -> tuple[dict | None, int]:
    """Parse one JSON object starting at buffer[start] == '{'.

    Returns (object, index-after) when the object is COMPLETE in the buffer,
    (None, len(buffer)) when the buffer ends inside it. String- and
    escape-aware, so braces inside quoted values do not fool the depth count.
    """
    depth = 0
    in_str = False
    i = start
    while i < len(buffer):
        ch = buffer[i]
        if in_str:
            if ch == "\\":
                i += 2
                continue
            if ch == '"':
                in_str = False
        elif ch == '"':
            in_str = True
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                try:
                    return json.loads(buffer[start:i + 1]), i + 1
                except json.JSONDecodeError:
                    return None, i + 1
        i += 1
    return None, len(buffer)


def partial_evidence_items(buffer: str) -> list[dict]:
    """Every COMPLETED evidence item in a partial structured-output buffer.

    The demo's findings display shows each finding the moment the model
    finishes writing it -- which is only honest if 'finished' means the item's
    JSON object is complete in the stream, not that a timer decided it was
    time to reveal one. An item cut off mid-write is excluded; it appears on a
    later poll once its closing brace has arrived.

    Both evidence arrays are read -- `resolution.evidence` on a case heading
    for resolved, `partial.evidence` on one heading for a park -- because the
    reader cannot know which way the run will land while it is still running.
    """
    out: list[dict] = []
    seen: set[tuple] = set()
    at = 0
    while True:
        key = buffer.find('"evidence"', at)
        if key < 0:
            break
        bracket = buffer.find("[", key)
        if bracket < 0:
            break
        i = bracket + 1
        while i < len(buffer):
            ch = buffer[i]
            if ch == "{":
                obj, i = _complete_object(buffer, i)
                if obj is None:
                    break
                ident = (obj.get("artifact"), obj.get("fact"))
                if obj.get("fact") and ident not in seen:
                    seen.add(ident)
                    out.append({k: obj.get(k) for k in
                                ("artifact", "fact", "chip", "severity")})
            elif ch == "]":
                break
            else:
                i += 1
        at = key + len('"evidence"')
    return out


def partial_string_field(buffer: str, field: str) -> str:
    """The value so far of a top-level JSON string field in a partial buffer.

    The model's structured output arrives as JSON text deltas, and `rationale`
    is the second property in the schema, so it lands early and streams for
    most of the run. Rendering the raw JSON at a client would be ugly; guessing
    at the prose would be dishonest. This reads the real field out of the
    incomplete buffer instead, decoding escapes properly and tolerating a cut
    in the middle of one.
    """
    key = json.dumps(field) + ":"
    at = buffer.find(key)
    if at < 0:
        key = json.dumps(field) + " :"
        at = buffer.find(key)
        if at < 0:
            return ""
    i = buffer.find('"', at + len(key))
    if i < 0:
        return ""

    out: list[str] = []
    j = i + 1
    while j < len(buffer):
        ch = buffer[j]
        if ch == "\\":
            out.append(buffer[j:j + 2])
            j += 2
            continue
        if ch == '"':
            break
        out.append(ch)
        j += 1

    frag = "".join(out)
    # A buffer can end mid-escape ("...\\u12"); trim the incomplete tail rather
    # than failing to decode the whole field for one truncated character.
    frag = _TRAILING_ESCAPE.sub("", frag)
    try:
        return json.loads('"' + frag + '"')
    except json.JSONDecodeError:
        return ""
