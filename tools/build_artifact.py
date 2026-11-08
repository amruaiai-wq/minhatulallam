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
out = root / "site/artifact.html"
out.write_text(s, encoding="utf-8")
print(out, f"{len(s.encode()) / 1e6:.1f} MB")
