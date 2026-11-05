"""Build a local preview of the site: the approved prototype with the current JSON embedded.

Usage: python tools/build_preview.py  ->  writes site/preview.html

All volumes (vol*/toc.json + vol*/entries/*.json) are merged into one TOC. Hadith numbers run
across volumes, so topic slugs (h<first hadith no.>) stay unique. Each bab gets `volume` and
`kitab` (vol1 babs have no kitab field; they are all كتاب الطهارة).
Kitab intros (`kitabs[].intro_th`) are collected into `toc.kitab_intros` for the บทนำ page.
"""
import glob
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
proto = (ROOT / "design" / "prototype.html").read_text(encoding="utf-8")

babs, entries, kitab_intros, last = [], [], [], 0
for vdir in sorted(ROOT.glob("vol*"), key=lambda p: int(p.name[3:])):
    toc = json.loads((vdir / "toc.json").read_text(encoding="utf-8"))
    for b in toc["babs"]:
        b.setdefault("kitab", "taharah")
        b["volume"] = toc["volume"]
        babs.append(b)
    for k in toc.get("kitabs", []):
        if k.get("intro_th"):
            kitab_intros.append(dict(k, volume=toc["volume"]))
    last = max(last, toc["hadith_range"][1])
    entries += [json.loads(pathlib.Path(f).read_text(encoding="utf-8"))
                for f in glob.glob(str(vdir / "entries" / "*.json"))]
entries.sort(key=lambda e: e["hadith"][0]["no"])
toc = {"title_ar": "منحة العلام في شرح بلوغ المرام", "hadith_range": [1, last], "babs": babs,
       "kitab_intros": kitab_intros}

data = json.dumps({"toc": toc, "entries": entries}, ensure_ascii=False).replace("</", "<\\/")
pattern = re.compile(r'(<script id="data" type="application/json">)(.*?)(</script>)', re.S)
assert pattern.search(proto), "data block not found in prototype"
html = pattern.sub(lambda m: m.group(1) + data + m.group(3), proto, count=1)
# The prototype has no doctype/charset; without them Thai and Arabic render as mojibake.
if "<meta charset" not in html:
    html = ('<!doctype html>\n<html lang="th">\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '<style>body { margin: 0; }</style>\n' + html)

out = ROOT / "site" / "preview.html"
out.parent.mkdir(exist_ok=True)
out.write_text(html, encoding="utf-8", newline="\r\n")
print(f"{out}  ({len(entries)} topics, hadith {entries[0]['hadith'][0]['no']}-{entries[-1]['hadith'][-1]['no']})")
