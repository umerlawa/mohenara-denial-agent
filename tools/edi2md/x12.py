"""Minimal X12 tokenizer. Deterministic, no dependencies."""


class Segment:
    __slots__ = ("sid", "elems", "raw")

    def __init__(self, raw):
        self.raw = raw
        parts = raw.split("*")
        self.sid = parts[0]
        self.elems = parts[1:]

    def e(self, i, default=""):
        """1-based element access, '' when absent."""
        idx = i - 1
        if 0 <= idx < len(self.elems):
            return self.elems[idx]
        return default

    def comp(self, i):
        """Element i split into sub-elements on ':'."""
        return self.e(i).split(":")


def parse_file(path):
    text = path.read_text().replace("\n", "")
    segs = []
    for raw in text.split("~"):
        raw = raw.strip()
        if raw:
            segs.append(Segment(raw))
    return segs


def values_of(seg):
    """All non-empty elementary values incl. sub-elements, for completeness checks."""
    out = []
    for el in seg.elems:
        for sub in el.split(":"):
            sub = sub.strip()
            if sub:
                out.append(sub)
    return out
