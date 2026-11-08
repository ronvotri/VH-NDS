#!/usr/bin/env python3
"""Compare full checkpoint 061 and 062 and validate source integrity and NDS tokens."""
import collections, json, re, sys, unicodedata, zipfile
OLD=sys.argv[1] if len(sys.argv)>1 else '/mnt/data/MagiciansQuest-VietHoa-Checkpoint-061.zip'
NEW=sys.argv[2] if len(sys.argv)>2 else '/mnt/data/MagiciansQuest-VietHoa-Checkpoint-062.zip'
TOKEN=re.compile(r"\$\d{3}(?:'[0-9-]+)*;")
with zipfile.ZipFile(OLD) as a, zipfile.ZipFile(NEW) as b:
 assert a.testzip() is None and b.testzip() is None
 old={n.split('/',1)[1]:a.read(n) for n in a.namelist() if not n.endswith('/')}
 new={n.split('/',1)[1]:b.read(n) for n in b.namelist() if not n.endswith('/')}
 paths=sorted(p for p in old if p.startswith('translation/') and p.endswith('.jsonl'))
 assert len(paths)==501,len(paths)
 targets={f'translation/04-thoai/talkfigs__0eng__data__0040.{n}.jsonl' for n in ('021','022')}
 count=total=before=after=0
 changed=collections.Counter()
 for p in paths:
  assert p in new,p
  rows_old=[json.loads(x) for x in old[p].decode().splitlines()]
  rows_new=[json.loads(x) for x in new[p].decode().splitlines()]
  assert len(rows_old)==len(rows_new),(p,'row count')
  total+=len(rows_old)
  before+=sum(r['vi'] is not None for r in rows_old)
  after+=sum(r['vi'] is not None for r in rows_new)
  for prev,cur in zip(rows_old,rows_new):
   assert {k:v for k,v in prev.items() if k!='vi'}=={k:v for k,v in cur.items() if k!='vi'},(p,prev['id'],'source mutation')
   if prev['vi']!=cur['vi']:
    assert p in targets and prev['vi'] is None and isinstance(cur['vi'],str) and cur['vi'],(p,prev['id'],'unexpected mutation')
    assert TOKEN.findall(prev['en'])==TOKEN.findall(cur['vi']),(p,prev['id'],'token mismatch')
    assert unicodedata.normalize('NFC',cur['vi'])==cur['vi'],(p,prev['id'],'NFC')
    assert not any(c in cur['vi'] for c in '\r\n\t'),(p,prev['id'],'extra controls')
    assert cur['vi'].count('▼')<=3,(p,prev['id'],'break count')
    assert all(len(TOKEN.sub('',part))<=34 for part in cur['vi'].split('▼')),(p,prev['id'],'width')
    count+=1;changed[p]+=1
  if p not in targets:assert old[p]==new[p],(p,'changed byte data')
 assert (total,before,after,count)==(55976,16752,16932,180),(total,before,after,count)
 assert sorted(changed.values())==[60,120] and len(changed)==2,changed
 for name in ['DELTA-062.jsonl','QA-062.md','CHECKPOINT-2026-11-08-DOT-62.md','manual_0040_021.tsv','manual_0040_022.tsv','build_062.py','qa_062.py','vi_0040_021.txt','vi_0040_022.txt']:
  assert name in new,name
 delta=[json.loads(s) for s in new['DELTA-062.jsonl'].decode().splitlines()]
 assert len(delta)==180
 delta_index={r['id']:r for r in delta}
 assert len(delta_index)==180
 for path in targets:
  for line in new[path].decode().splitlines():
   row=json.loads(line)
   assert delta_index[row['id']]==row,row['id']
 print(f'QA PASS: {len(paths)} JSONLs, {total} rows, {before} → {after} translated, {count} new; all IDs/EN/CTX/tokens/NFC/width PASS; 499 other JSONLs byte-identical; ZIP CRC PASS')
