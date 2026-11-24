import json,glob,sys
V=sys.argv[1]; START=int(sys.argv[2])
raw=open(f'vol{V}/toc.json','rb').read(); toc=json.loads(raw)
dump=lambda t: json.dumps(t,ensure_ascii=False,indent=1).replace('\n','\r\n').encode()+b'\r\n'
assert dump(toc)==raw
ents={}
for f in sorted(glob.glob(f'vol{V}/entries/*.json')):
  e=json.load(open(f)); ents[(e['bab'],e['topic_ar'])]=e
  assert e['id']==f'v{V}-'+f.split('/')[-1][:-5],f
  assert [s['wajh'] for s in e['sections']]==list(range(1,len(e['sections'])+1)),f
  if not 3<=len(e['key_rulings_th'])<=5: print('kr',f,len(e['key_rulings_th']))
nos=sorted(h['no'] for e in ents.values() for h in e['hadith'])
assert not nos or nos==list(range(START,nos[-1]+1)),nos
n=0
for b in toc['babs']:
  for t in b['topics']:
    if (b['id'],t['ar']) in ents: t['hadith_nos']=[h['no'] for h in ents[(b['id'],t['ar'])]['hadith']]; n+=1
print(n,len(ents),nos[-1] if nos else None)
missing=[k for k in ents if k not in {(b['id'],t['ar']) for b in toc['babs'] for t in b['topics']}]
assert not missing, missing
open(f'vol{V}/toc.json','wb').write(dump(toc))
