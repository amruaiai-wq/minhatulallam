"""Make the publishable copy of site/preview.html for the claude.ai artifact.

The artifact host adds its own <!doctype>, <html> and viewport meta, so this strips them,
sets the page title, and writes site/artifact.html (git-ignored if large; not committed).
Run `python tools/build_preview.py` first, then this, then publish site/artifact.html
to the existing artifact URL noted in CLAUDE.md.
"""
import pathlib
root = pathlib.Path(__file__).resolve().parent.parent
s = (root / "site/preview.html").read_text(encoding="utf-8")
head = '<!doctype html>\n<html lang="th">\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
assert s.startswith(head), "preview.html header changed; update build_artifact.py"
s = s[len(head):].replace("<title>Minhat al-Allam Thai</title>",
    '<title>มินหะตุลอัลลาม ฉบับไทย</title>\n<script>document.documentElement.lang="th";</script>', 1)
# Compress the embedded data (≈15 MB JSON → ≈3.4 MB gzip+base64) so the artifact stays far
# under the 16 MB page limit. The browser inflates it with DecompressionStream, recreates
# <script id="data">, then runs the app script unchanged.
import base64, gzip, json, re
m = re.search(r'<script id="data" type="application/json">(.*?)</script>', s, re.S)
gz = base64.b64encode(gzip.compress(m.group(1).encode(), 9)).decode()
rest = s[m.end():]
app = re.search(r"<script>(.*?)</script>", rest, re.S)
loader = (
    '<script id="data-gz" type="text/plain">' + gz + '</script>\n<script>\n(async function () {\n'
    '  var b = atob(document.getElementById("data-gz").textContent.trim());\n'
    '  var u = new Uint8Array(b.length); for (var i = 0; i < b.length; i++) u[i] = b.charCodeAt(i);\n'
    '  var txt = await new Response(new Blob([u]).stream().pipeThrough(new DecompressionStream("gzip"))).text();\n'
    '  var d = document.createElement("script"); d.id = "data"; d.type = "application/json"; d.textContent = txt;\n'
    '  document.body.appendChild(d);\n'
    '  var a = document.createElement("script"); a.textContent = ' + json.dumps(app.group(1)).replace("</", "<\\/") + ';\n'
    '  document.body.appendChild(a);\n'
    '})();\n</script>')
s = s[:m.start()] + rest[:app.start()] + loader + rest[app.end():]
out = root / "site/artifact.html"
out.write_text(s, encoding="utf-8")
print(out, f"{len(s.encode()) / 1e6:.1f} MB")
