"""polish.py EDITS.py — EDITS defines E = {"vol1/entries/h001.json": [(old,new),...]}; each old must occur exactly once in the file's strings."""
import sys, runpy
sys.path.insert(0, "/home/user/minhatulallam/tools")
import jsonio
R = runpy.run_path(sys.argv[1]); E = R["E"]; G = R.get("G", {})
bad = 0
for f, eds in E.items():
    p = "/home/user/minhatulallam/" + f
    e, fmt = jsonio.load(p)
    def walk(x, fn):
        if isinstance(x, str): return fn(x)
        if isinstance(x, list): return [walk(y, fn) for y in x]
        if isinstance(x, dict): return {k: walk(v, fn) for k, v in x.items()}
        return x
    for old, new in eds:
        cnt = [0]
        def c(s): cnt[0] += s.count(old); return s
        walk(e, c)
        if cnt[0] != 1:
            print("MISS" if cnt[0] == 0 else "MULTI", f, old[:50]); bad += 1; continue
        e = walk(e, lambda s: s.replace(old, new))
    for h in e["hadith"]:
        if h["no"] in G: h["grade_th"] = G.pop(h["no"])
    jsonio.save(p, e, fmt)
print("done, problems:", bad, "unused grades:", list(G))
