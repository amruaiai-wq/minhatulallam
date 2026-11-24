"""Print an entry compactly for review. Usage: python tools/show.py vol4/entries/h446-447.json [...]"""
import json, sys
for f in sys.argv[1:]:
    e = json.load(open(f))
    print('==', f, e['pages'], e['topic_ar'], '|', e['topic_th'])
    for h in e['hadith']:
        print(f"[{h['no']}] {h['matn_ar']}\n  T: {h['translation_th']}\n  G: {h['grade_th']}")
    for i, k in enumerate(e['key_rulings_th']): print(f'  KR{i}: {k}')
    for v in e.get('vocab', []): print(f"  V: {v['ar']} = {v['th']}")
    for s in e['sections']:
        print(f"  W{s['wajh']} [{s['type']}] {s['heading_th']}")
        for i, p in enumerate(s['points_th']): print(f'    {i}. {p}')
    print('  tags:', ', '.join(e.get('tags_th', [])))
