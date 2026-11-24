"""Put the author's Arabic words in front of a Thai verdict quote.
Edit file defines A = [(file, thai_prefix, arabic), ...]: the segment 'ผู้แต่ง: «<thai…>»' whose quote starts with
thai_prefix becomes 'ผู้แต่ง: «<arabic>» <thai…>'. Also handles 'ผู้แต่งว่า<thai_prefix>' (→ 'ผู้แต่ง: «<arabic>» <thai_prefix>').
Usage: python tools/verdict_ar.py EDITS.py"""
import sys, runpy, re, json
sys.path.insert(0, 'tools'); import jsonio
A = runpy.run_path(sys.argv[1])['A']
bad = 0
for f, pre, ar in A:
    e, fmt = jsonio.load(f); s = json.dumps(e, ensure_ascii=False)
    pat = re.compile(r'ผู้แต่ง: «(' + re.escape(pre) + r'[^»]*)»')
    n = len(pat.findall(s))
    if n:
        s = pat.sub(lambda m: 'ผู้แต่ง: «' + ar + '» ' + m.group(1), s)
    elif ('ผู้แต่ง: ' + pre) in s:
        n = s.count('ผู้แต่ง: ' + pre)
        s = s.replace('ผู้แต่ง: ' + pre, 'ผู้แต่ง: «' + ar + '» ' + pre)
    else:
        n = 0
        for lead in ('ผู้แต่งเห็นว่า', 'ผู้แต่งสรุปว่า', 'ผู้แต่งว่า', ''):
            old = lead + pre
            if lead == '' and n == 0 and s.count(old) == 1:
                n = 1; s = s.replace(old, 'ผู้แต่ง: «' + ar + '» ' + pre); break
            if lead and s.count(old):
                n = s.count(old); s = s.replace(old, 'ผู้แต่ง: «' + ar + '» ' + pre); break
    if n == 0: print('MISS', f, pre); bad += 1; continue
    jsonio.save(f, json.loads(s), fmt)
print('done, misses:', bad)
