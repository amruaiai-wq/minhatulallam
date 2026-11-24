"""List grade_th / translation issues still to fix in a volume (fast polish pass).
Usage: python tools/grade_issues.py <vol>"""
import json, re, sys, glob
vol = sys.argv[1]
def bal(s):
    d = 0
    for c in s:
        d += (c == '(') - (c == ')')
        if d < 0: return False
    return d == 0
for f in sorted(glob.glob(f'vol{vol}/entries/*.json')):
    e = json.load(open(f))
    for h in e['hadith']:
        g = h['grade_th']; why = []
        m = re.fullmatch(r'(\S+)(?: \((.*)\))?', g)
        if not m or not bal(g) or (m.group(2) and not bal(m.group(2))): why.append('shape')
        else:
            inner = m.group(2) or ''
            if not inner: why.append('bare')
            if inner.strip() in ('อ่อน', 'อ่อนมาก', 'ศ่อฮีห์', 'หะซัน'): why.append('redundant')
            if m.group(1) == 'ฎออีฟ' and re.match(r'(อ่อนมาก|มุ[นง]กัร)', inner): why.append('head')
        t = h['translation_th']
        if re.search(r'(?:ถาม|กล่าว)ว่า (?!«)[^«»]{3,120}?(?:ไหม|หรือ|อย่างไร|ไหน)(?: |$)', t): why.append('Tq')
        if why: print(f.split('/')[-1][:-5], h['no'], ','.join(why), '|', g if 'Tq' not in why or len(why) > 1 else '', ('| T: ' + t[:260]) if 'Tq' in why else '')
