"""Propose merged grades: 'head (A) rest' -> 'head (A; rest)'; 'ฎออีฟ (อ่อน) rest' -> 'ฎออีฟ (rest)'.
Usage: python tools/grade_merge.py <vol> [--apply]   (only rows the regex handles; prints them)"""
import json, re, sys, glob
sys.path.insert(0, 'tools'); import jsonio
vol = sys.argv[1]; apply = '--apply' in sys.argv
for f in sorted(glob.glob(f'vol{vol}/entries/*.json')):
    e, fmt = jsonio.load(f); ch = False
    for h in e['hadith']:
        g = h['grade_th']
        m = re.fullmatch(r'(\S+) \(([^()]*)\)\s*[—-]?\s*(.+)', g)
        if not m or '(' in m.group(3) and not m.group(3).endswith(')'): continue
        hd, a, rest = m.groups()
        if '(' in rest or ')' in rest:
            rest = re.sub(r'\s*\(([^()]*)\)', r' — \1', rest)
        a = '' if a.strip() in ('อ่อน', 'อ่อนมาก') else a
        new = f"{hd} ({a + '; ' if a else ''}{rest.strip()})"
        print(h['no'], new)
        if apply: h['grade_th'] = new; ch = True
    if ch: jsonio.save(f, e, fmt)
