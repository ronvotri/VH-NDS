#!/usr/bin/env python3
"""Verify checkpoint 040 is exclusively a 240-page vi addition from checkpoint 039.
Usage: python qa_040.py /path/to/MagiciansQuest-VietHoa-Checkpoint-039.zip
"""
from pathlib import Path
from collections import Counter
import sys,re,json,zipfile,unicodedata
BASE=Path(__file__).resolve().parent
TOKEN=re.compile(r'\$[\d\']+;')
TARGET={'talkfigs__0eng__data__0032.003.jsonl':120,'talkfigs__0eng__data__0032.004.jsonl':120}

def check(z):
 all_files=sorted((BASE/'translation').rglob('*.jsonl'))
 assert len(all_files)==501, ('file count',len(all_files))
 old_total=new_total=translated_old=translated_new=added=0
 npc=0;npc_count=0
 for f in all_files:
  rel=f.relative_to(BASE).as_posix()
  old=json.loads('[]') if False else [json.loads(s) for s in z.read('MagiciansQuest_039/'+rel).decode('utf8').splitlines()]
  new=[json.loads(s) for s in f.read_text('utf8').splitlines()]
  assert len(old)==len(new),('changed rows',rel)
  old_total+=len(old);new_total+=len(new)
  for i,(a,b) in enumerate(zip(old,new)):
   translated_old+=bool(a.get('vi'))
   translated_new+=bool(b.get('vi'))
   if '04-thoai' in rel:
    npc_count+=1;npc+=bool(b.get('vi'))
   if f.name not in TARGET:
    assert a==b,('unintended change',rel,i)
   else:
    assert a.get('vi') in (None,''),('prior vi exists',rel,i)
    assert a.keys()==b.keys(),('field altered',rel,i)
    assert {k:v for k,v in a.items() if k!='vi'}=={k:v for k,v in b.items() if k!='vi'},('source altered',rel,i)
    assert b.get('vi'),('untranslated',rel,i)
    vi=b['vi']
    assert TOKEN.findall(a['en'])==TOKEN.findall(vi),('control mismatch',rel,i)
    assert '\t' not in vi and '\r' not in vi and '\n' not in vi,('special char',rel,i)
    assert unicodedata.normalize('NFC',vi)==vi,('NFC',rel,i)
    assert vi.count('▼')<=3,('page overflow',rel,i)
    assert all(len(TOKEN.sub('',line))<=34 for line in vi.split('▼')),('line too long',rel,i)
    if b.get('max_utf8_bytes'):
     assert len(vi.encode('utf8'))<=b['max_utf8_bytes'],('byte limit',rel,i)
    added+=1
 assert old_total==new_total==55976,(old_total,new_total)
 assert translated_old==11509,translated_old
 assert translated_new==11749,translated_new
 assert added==240,added
 assert npc_count==52608 and npc==8624,(npc_count,npc)
 print('QA PASS: 501 JSONL, 55,976 records, 240 new vi, 11,509 old unchanged.')
 print('TOTAL 11,749 / 55,976 = %.2f%%; NPC 8,624 / 52,608' % (100*translated_new/new_total))
 return {'files':len(all_files),'records':new_total,'added':added,'translated':translated_new,'npc':npc}

if __name__=='__main__':
 source=Path(sys.argv[1]) if len(sys.argv)>1 else Path('/mnt/data/MagiciansQuest-VietHoa-Checkpoint-039.zip')
 with zipfile.ZipFile(source) as z:check(z)