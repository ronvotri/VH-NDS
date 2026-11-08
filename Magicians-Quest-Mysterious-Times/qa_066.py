#!/usr/bin/env python3
"""Exhaustive static QA comparing checkpoint 065 and 066."""
import sys,collections,json,re,unicodedata,zipfile
OLD=sys.argv[1] if len(sys.argv)>1 else '/mnt/data/MagiciansQuest-VietHoa-Checkpoint-065.zip'
NEW=sys.argv[2] if len(sys.argv)>2 else '/mnt/data/MagiciansQuest-VietHoa-Checkpoint-066.zip'
TOKEN=re.compile(r"\$\d{3}(?:'[0-9-]+)*;")
TARGETS={f'translation/04-thoai/talkfigs__0eng__data__0041.{s}.jsonl' for s in ('007','008')}
with zipfile.ZipFile(OLD) as a,zipfile.ZipFile(NEW) as b:
 assert a.testzip() is None and b.testzip() is None,'zip CRC'
 old={p.split('/',1)[1]:a.read(p) for p in a.namelist() if not p.endswith('/')}
 new={p.split('/',1)[1]:b.read(p) for p in b.namelist() if not p.endswith('/')}
 paths=sorted(p for p in old if p.startswith('translation/') and p.endswith('.jsonl'))
 assert len(paths)==501,len(paths)
 before=after=total=changed=0;counts=collections.Counter()
 for p in paths:
  assert p in new,p
  ra=[json.loads(x) for x in old[p].decode().splitlines()]
  rb=[json.loads(x) for x in new[p].decode().splitlines()]
  assert len(ra)==len(rb),(p,'record count')
  total+=len(ra)
  for x,y in zip(ra,rb):
   before+=x['vi'] is not None;after+=y['vi'] is not None
   assert {k:v for k,v in x.items() if k!='vi'}=={k:v for k,v in y.items() if k!='vi'},(p,x['id'],'metadata')
   if x['vi']!=y['vi']:
    assert p in TARGETS and x['vi'] is None and isinstance(y['vi'],str) and y['vi'],(p,x['id'],'unexpected change')
    assert unicodedata.normalize('NFC',y['vi'])==y['vi'],(p,x['id'],'NFC')
    assert TOKEN.findall(x['en'])==TOKEN.findall(y['vi']),(p,x['id'],'token sequence')
    assert y['vi'].count('▼')<=3,(p,x['id'],'breaks')
    assert all(len(TOKEN.sub('',seg))<=34 for seg in y['vi'].split('▼')),(p,x['id'],'width')
    assert all(c not in y['vi'] for c in '\r\n\t'),(p,x['id'],'newline')
    changed+=1;counts[p]+=1
  if p not in TARGETS:assert old[p]==new[p],(p,'unexpected other file change')
 assert (total,before,after,changed)==(55976,17652,17892,240),(total,before,after,changed)
 assert sorted(counts.values())==[120,120],counts
 extras=['DELTA-066.jsonl','QA-066.md','CHECKPOINT-2026-11-09-DOT-66.md','manual_0041_007.tsv','manual_0041_008.tsv','build_066.py','qa_066.py','mq066_translate.py','vi_0041_007.txt','vi_0041_008.txt']
 for p in extras:assert p in new,p
 delta=[json.loads(x) for x in new['DELTA-066.jsonl'].decode().splitlines()]
 assert len(delta)==240
 byid={r['id']:r for r in delta};assert len(byid)==240
 for p in TARGETS:
  for x in [json.loads(x) for x in new[p].decode().splitlines()]:assert byid[x['id']]==x,(p,x['id'])
 print('QA PASS',len(paths),'JSONL',total,'records',before,'->',after,'translated',changed,'new; untouched files 499; tokens NFC static width delta ZIP CRC PASS')
