"""Tarjih points (author's preferred view) still without the author's Arabic words.
Usage: python tools/tarjih.py <vol> [bab]   -> lines: file pages W.i excerpt"""
import json, re, sys, glob
vol = sys.argv[1]; bab = sys.argv[2] if len(sys.argv) > 2 else None
AR = re.compile(r'[؀-ۿ]')
T = re.compile(r'ผู้แต่ง(?:เห็นว่า|ว่า|:|สรุปว่า|เลือก)\s*(?:ทัศนะ|ที่ถูก|ที่ชัด|ที่มีน้ำหนัก|ที่ใกล้|ที่ปรากฏ|นี่(?:คือ|ต้องพิจารณา|มีข้อพิจารณา)|ต้องพิจารณา|มีข้อพิจารณา|การใช้หลักฐาน|ไม่ถูกต้อง|ถูกต้อง)'
               r'|(?<!ใน)ทัศนะที่(?:มีน้ำหนัก|ถูกต้อง|ชัด)(?:กว่า|ที่สุด)?(?:คือ|ใน)')
for f in sorted(glob.glob(f'vol{vol}/entries/*.json')):
    e = json.load(open(f))
    if bab and e['bab'] != bab: continue
    for s in e['sections']:
        for i, p in enumerate(s['points_th']):
            m = T.search(p)
            if m and not AR.search(p[m.start(): m.start() + 50]):
                print(f.split('/')[-1][:-5], e['bab'], e['pages'], f'W{s["wajh"]}.{i}', p[m.start(): m.start() + 110])
