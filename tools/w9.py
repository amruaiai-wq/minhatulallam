"""Write vol 9 entries from a scratch batch file: python3 tools/w9.py BATCH.py
BATCH defines ENTRIES = [dict(...)] (schema as in CLAUDE.md, without id/volume) and optional
KINTRO = {kitab_id: [paragraphs]} / BINTRO = {bab_id: [paragraphs]} for toc intros."""
import json, sys, runpy, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
ns = runpy.run_path(sys.argv[1])
for e in ns.get("ENTRIES", []):
    nos = [h["no"] for h in e["hadith"]]
    name = f"h{nos[0]}" + (f"-{nos[-1]}" if len(nos) > 1 else "")
    out = {"id": f"v9-{name}", "volume": 9}
    out.update(e)
    (root / f"vol9/entries/{name}.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print("wrote", name)
tp = root / "vol9/toc.json"
toc = json.loads(tp.read_bytes())
for k, v in ns.get("KINTRO", {}).items():
    next(x for x in toc["kitabs"] if x["id"] == k)["intro_th"] = v
for k, v in ns.get("BINTRO", {}).items():
    next(x for x in toc["babs"] if x["id"] == k)["intro_th"] = v
tp.write_bytes(json.dumps(toc, ensure_ascii=False, indent=1).replace("\n", "\r\n").encode() + b"\r\n")
