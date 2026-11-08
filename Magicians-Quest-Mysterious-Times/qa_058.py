#!/usr/bin/env python3
"""Verify that checkpoint 058 only fills 240 Vietnamese fields from 057."""
import json, zipfile, re, unicodedata,sys, collections
OLD=sys.argv[1] if len(sys.argv)>1 else '/mnt/data/MagiciansQuest-VietHoa-Checkpoint-057.zip'
NEW=sys.argv[2] if len(sys.argv)>2 else '/mnt/data/MagiciansQuest-VietHoa-Checkpoint-058.zip'
TOKEN=re.compile(r"\$\d{3}(?:'[0-9-]+)*;")
with zipfile.ZipFile(OLD) as a, zipfile.ZipFile(NEW) as b:
 assert a.testzip() is None and b.testzip() is None
 old={n.split('/',1)[1]:a.read(n) for n in a.namelist() if not n.endswith('/')}
 new={n.split('/',1)[1]:b.read(n) for n in b.namelist() if not n.endswith('/')}
 paths=[p for p in old if p.startswith('translation/') and p.endswith('.jsonl')]
 assert len(paths)==501,len(paths)
 count=0; before=after=0;total=0; changed=collections.Counter()
 targets={f'translation/04-thoai/talkfigs__0eng__data__0040.{i:03d}.jsonl' for i in (13,14)}
 for p in paths:
  prev=[json.loads(x) for x in old[p].decode().splitlines()]
  curr=[json.loads(x) for x in new[p].decode().splitlines()]
  assert len(prev)==len(curr),(p,'len');total+=len(prev)
  before+=sum(r.get('vi') is not None for r in prev)
  after+=sum(r.get('vi') is not None for r in curr)
  for x,y in zip(prev,curr):
   assert {k:v for k,v in x.items() if k!='vi'}=={k:v for k,v in y.items() if k!='vi'},(p,'non-vi change')
   if x['vi']!=y['vi']:
    assert p in targets and x['vi'] is None and isinstance(y['vi'],str) and y['vi'],(p,'unexpected change')
    assert TOKEN.findall(x['en'])==TOKEN.findall(y['vi']),(p,'token',x['id'])
    assert unicodedata.normalize('NFC',y['vi'])==y['vi'],(p,'NFC')
    assert '\n' not in y['vi'] and '\t' not in y['vi'] and '\r' not in y['vi']
    assert y['vi'].count('▼')<=3
    assert all(len(TOKEN.sub('',line))<=34 for line in y['vi'].split('▼')),(p,'static width',x['id'])
    count+=1; changed[p]+=1
  if p not in targets: assert old[p]==new[p],(p,'unexpected byte change')
 assert total==55976,total
 assert before==15792 and after==16032,(before,after)
 assert count==240,count
 assert len(changed)==2 and sorted(changed.values())==[120,120],changed
 assert all(z in new for z in ('DELTA-058.jsonl','QA-058.md','CHECKPOINT-2026-11-08-DOT-58.md','manual_0040_013.tsv','manual_0040_014.tsv','build_058.py','qa_058.py'))
 assert len([json.loads(x) for x in new['DELTA-058.jsonl'].decode().splitlines()])==240
 print(f'QA PASS: {len(paths)} JSONL; {total} total records; {before} -> {after} translated; exactly {count} new; token, NFC, static length PASS; other JSONL byte-identical; ZIP CRC PASS')
