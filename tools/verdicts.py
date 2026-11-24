"""List explanation points that state a verdict without the author's Arabic words.
Usage: python tools/verdicts.py <vol> <bab>"""
import json, re, sys, glob
vol, bab = sys.argv[1], sys.argv[2]
AR = re.compile(r'[؀-ۿ]')
K = re.compile(r'ผู้แต่ง|ที่ถูก|มีน้ำหนัก|ที่ชัด|ต้องพิจารณา|ทัศนะที่แข็งแรง')
for f in sorted(glob.glob(f'vol{vol}/entries/*.json')):
    e = json.load(open(f))
    if e['bab'] != bab: continue
    print('==', f.split('/')[-1][:-5], e['pages'], '|', ' / '.join(h['grade_th'] for h in e['hadith']))
    for s in e['sections']:
        for i, p in enumerate(s['points_th']):
            for m in K.finditer(p):
                seg = p[max(0, m.start() - 40): m.start() + 160]
                if not AR.search(p[m.start(): m.start() + 60]):
                    print(f'  W{s["wajh"]}.{i}: …{seg}…')
                break
