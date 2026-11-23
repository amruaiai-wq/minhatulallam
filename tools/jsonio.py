"""Read/write entry and toc JSON while keeping each file's existing byte format."""
import json, re

def detect(raw):
    e = json.loads(raw)
    for ind in (2, 1):
        for nl in (b"\n", b"\r\n"):
            for tail in (b"", b"\n", b"\r\n"):
                for compact in (False, True):
                    if dump(e, (ind, nl, tail, compact)) == raw:
                        return e, (ind, nl, tail, compact)
    return e, None

def dump(e, fmt):
    ind, nl, tail, compact = fmt
    s = json.dumps(e, ensure_ascii=False, indent=ind)
    if compact:  # short numeric lists on one line, as in hand-written files
        s = re.sub(r"\[\s*(-?\d+(?:,\s*-?\d+)*)\s*\]",
                   lambda m: "[" + ", ".join(x.strip() for x in m.group(1).split(",")) + "]", s)
        S = r'"(?:[^"\\]|\\.)*"'
        s = re.sub(r'"tags_th": \[\n\s*((?:' + S + r'(?:,\n\s*)?)*)\n\s*\]',
                   lambda m: '"tags_th": [' + re.sub(r',\n\s*', ', ', m.group(1)) + ']', s)
        s = re.sub(r'\{\n\s*"ar": (' + S + r'),\n\s*"th": (' + S + r')\n\s*\}', r'{"ar": \1, "th": \2}', s)
    return s.encode().replace(b"\n", nl) + tail

def load(path):
    raw = open(path, "rb").read()
    e, fmt = detect(raw)
    return e, (fmt or (2, b"\n", b"", False))

def save(path, e, fmt):
    open(path, "wb").write(dump(e, fmt))
