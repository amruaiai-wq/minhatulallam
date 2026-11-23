"""List what a polish pass checks: pages, grades, translations, and points with verdict words.
Usage: python tools/polish_scan.py <vol> <bab>"""
import json, re, sys, glob
vol, bab = sys.argv[1], sys.argv[2]
K = re.compile(r'ที่ถูกต้อง|มีน้ำหนัก|ที่ถูก|ผู้แต่ง|ทัศนะที่|รอบคอบ|ชาซ|ที่ชัด')
for f in sorted(glob.glob(f'vol{vol}/entries/*.json')):
    e = json.load(open(f))
    if e['bab'] != bab: continue
    print('==', f.split('/')[-1][:-5], e['pages'], e['topic_ar'])
    for h in e['hadith']:
        print(' ', h['no'], 'G:', h['grade_th'])
        if re.search(r'ว่า [^«]*(ไหม|หรือ|อย่างไร)\b', h['translation_th']): print('   T?', h['translation_th'][:300])
    for s in e['sections']:
        for p in s['points_th']:
            if K.search(p): print('  W%d' % s['wajh'], p[:260])
