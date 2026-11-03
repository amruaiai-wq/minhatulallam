"""Build a local preview of the site: the approved prototype with the current JSON embedded.

Usage: python tools/build_preview.py  ->  writes site/preview.html
"""
import glob
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
proto = (ROOT / "design" / "prototype.html").read_text(encoding="utf-8")

toc = json.loads((ROOT / "vol1" / "toc.json").read_text(encoding="utf-8"))
entries = [json.loads(pathlib.Path(f).read_text(encoding="utf-8"))
           for f in sorted(glob.glob(str(ROOT / "vol1" / "entries" / "*.json")))]
entries.sort(key=lambda e: e["hadith"][0]["no"])

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
out.write_text(html, encoding="utf-8")
print(f"{out}  ({len(entries)} topics, hadith {entries[0]['hadith'][0]['no']}-{entries[-1]['hadith'][-1]['no']})")
