#!/usr/bin/env python3
"""Audit 059 → 060, all 501 JSONL files and all source fields, never silently change previous translations."""
import collections,json,re,sys,unicodedata,zipfile
OLD=sys.argv[1] if len(sys.argv)>1 else '/mnt/data/MagiciansQuest-VietHoa-Checkpoint-059.zip'
NEW=sys.argv[2] if len(sys.argv)>2 else '/mnt/data/MagiciansQuest-VietHoa-Checkpoint-060.zip'
TOKEN=re.compile(r"\$\d{3}(?:'[0-9-]+)*;")
with zipfile.ZipFile(OLD) as a, zipfile.ZipFile(NEW) as b:
 assert a.testzip() is None and b.testzip() is None
 old={n.split('/',1)[1]:a.read(n) for n in a.namelist() if not n.endswith('/')}
 new={n.split('/',1)[1]:b.read(n) for n in b.namelist() if not n.endswith('/')}
 paths=[p for p in old if p.startswith('translation/') and p.endswith('.jsonl')]
 assert len(paths)==501,len(paths)
 total=before=after=count=0
 changed=collections.Counter()
 targets={f'translation/04-thoai/talkfigs__0eng__data__0040.{i:03d}.jsonl' for i in (17,18)}
 for p in paths:
  assert p in new,(p,'missing')
  prev=[json.loads(x) for x in old[p].decode().splitlines()]
  curr=[json.loads(x) for x in new[p].decode().splitlines()]
  assert len(prev)==len(curr),(p,'row count')
  total+=len(prev);before+=sum(x.get('vi') is not None for x in prev);after+=sum(x.get('vi') is not None for x in curr)
  for x,y in zip(prev,curr):
   assert {k:v for k,v in x.items() if k!='vi'}=={k:v for k,v in y.items() if k!='vi'},(p,'source changed')
   if x.get('vi')!=y.get('vi'):
    assert p in targets and x.get('vi') is None and isinstance(y.get('vi'),str) and y['vi'],(p,'unexpected vi change')
    assert TOKEN.findall(x['en'])==TOKEN.findall(y['vi']),(p,x['id'],'TOKEN')
    assert unicodedata.normalize('NFC',y['vi'])==y['vi'],(p,x['id'],'NFC')
    assert not any(s in y['vi'] for s in '\r\n\t'),(p,x['id'],'LINE CONTROL')
    assert y['vi'].count('▼')<=3,(p,x['id'],'BREAKS')
    assert all(len(TOKEN.sub('',line))<=34 for line in y['vi'].split('▼')),(p,x['id'],'WIDTH')
    count+=1;changed[p]+=1
  if p not in targets:assert old[p]==new[p],(p,'byte mismatch')
 assert (total,before,after,count)==(55976,16272,16512,240),(total,before,after,count)
 assert len(changed)==2 and sorted(changed.values())==[120,120],changed
 for name in ['DELTA-060.jsonl','QA-060.md','CHECKPOINT-2026-11-08-DOT-60.md','manual_0040_017.tsv','manual_0040_018.tsv','build_060.py','qa_060.py','vi_0040_017.txt','vi_0040_018.txt']:
  assert name in new,name
 delta=[json.loads(x) for x in new['DELTA-060.jsonl'].decode().splitlines()]
 assert len(delta)==240
 print(f'QA PASS: {len(paths)} JSONL; {total} records; {before}->{after} translated; exactly {count} new; token/NFC/width PASS; other JSONL byte-identical; ZIP CRC PASS')
