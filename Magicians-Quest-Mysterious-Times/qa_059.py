#!/usr/bin/env python3
"""Compare checkpoints 058/059 for only 240 new Vietnamese fields."""
import json,zipfile,re,unicodedata,sys,collections
OLD=sys.argv[1] if len(sys.argv)>1 else '/mnt/data/MagiciansQuest-VietHoa-Checkpoint-058.zip'
NEW=sys.argv[2] if len(sys.argv)>2 else '/mnt/data/MagiciansQuest-VietHoa-Checkpoint-059.zip'
TOKEN=re.compile(r"\$\d{3}(?:'[0-9-]+)*;")
with zipfile.ZipFile(OLD) as a,zipfile.ZipFile(NEW) as b:
 assert a.testzip() is None and b.testzip() is None
 old={n.split('/',1)[1]:a.read(n) for n in a.namelist() if not n.endswith('/')}
 new={n.split('/',1)[1]:b.read(n) for n in b.namelist() if not n.endswith('/')}
 paths=[p for p in old if p.startswith('translation/') and p.endswith('.jsonl')]
 assert len(paths)==501,len(paths)
 total=before=after=count=0;changed=collections.Counter()
 targets={f'translation/04-thoai/talkfigs__0eng__data__0040.{i:03d}.jsonl' for i in (15,16)}
 for p in paths:
  assert p in new,(p,'new archive missing source')
  prev=[json.loads(x) for x in old[p].decode().splitlines()]
  curr=[json.loads(x) for x in new[p].decode().splitlines()]
  assert len(prev)==len(curr),(p,'row count')
  total+=len(prev);before+=sum(r.get('vi') is not None for r in prev);after+=sum(r.get('vi') is not None for r in curr)
  for x,y in zip(prev,curr):
   assert {k:v for k,v in x.items() if k!='vi'}=={k:v for k,v in y.items() if k!='vi'},(p,'source key changed')
   if x['vi']!=y['vi']:
    assert p in targets and x['vi'] is None and isinstance(y['vi'],str) and y['vi'],(p,'unexpected vi change')
    assert TOKEN.findall(x['en'])==TOKEN.findall(y['vi']),(p,x['id'],'TOKEN')
    assert unicodedata.normalize('NFC',y['vi'])==y['vi'],(p,x['id'],'NFC')
    assert '\r' not in y['vi'] and '\n' not in y['vi'] and '\t' not in y['vi'],(p,x['id'],'CRLF')
    assert y['vi'].count('▼')<=3,(p,x['id'],'BREAK COUNT')
    assert all(len(TOKEN.sub('',line))<=34 for line in y['vi'].split('▼')),(p,x['id'],'WIDTH')
    count+=1;changed[p]+=1
  if p not in targets:assert old[p]==new[p],(p,'unexpected byte change')
 assert (total,before,after,count)==(55976,16032,16272,240),(total,before,after,count)
 assert len(changed)==2 and sorted(changed.values())==[120,120],changed
 for required in ['DELTA-059.jsonl','QA-059.md','CHECKPOINT-2026-11-08-DOT-59.md','manual_0040_015.tsv','manual_0040_016.tsv','build_059.py','qa_059.py']:
  assert required in new,required
 delta=[json.loads(x) for x in new['DELTA-059.jsonl'].decode().splitlines()]
 assert len(delta)==240
 print(f'QA PASS: {len(paths)} JSONL; {total} records; {before}->{after} translated; exactly {count} new; token/NFC/width PASS; other JSONL byte-identical; ZIP CRC PASS')
