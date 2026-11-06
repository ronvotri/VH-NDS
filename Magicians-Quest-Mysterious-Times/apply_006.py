#!/usr/bin/env python3
"""Apply manually authored NPC translations for checkpoint 006.
Only set previously empty `vi`; never touch ID, EN, ctx, or control codes.
"""
import json, re, shutil, unicodedata
from pathlib import Path
ROOT=Path(__file__).resolve().parent
SOURCE=ROOT.parent/'MagiciansQuest_005'
TARGET=ROOT
CONTROL=re.compile(r"\$\d{3}(?:'[^;\r\n\t]*)?;")
PREFIX=re.compile(r"^(?:(?:\$\d{3}(?:'[^;\r\n\t]*)?;))+")
NAMES=['0002','0003','0006','0007','0008']
records=[]
for n in NAMES:
 source=SOURCE/'translation/04-thoai'/f'talkfigs__0eng__data__{n}.001.jsonl'
 target=TARGET/'translation/04-thoai'/source.name
 if not target.exists():
  target.parent.mkdir(parents=True,exist_ok=True)
  shutil.copy2(source,target)
 rows=[json.loads(t) for t in source.read_text(encoding='utf8').splitlines()]
 lines=(ROOT/f'manual_{n}.txt').read_text(encoding='utf8').splitlines()
 assert len(rows)==len(lines),(n,len(rows),len(lines))
 for i,(rec,trans) in enumerate(zip(rows,lines),1):
  assert rec['vi'] is None,(n,i,'already translated')
  raw=rec['en']
  pref=PREFIX.match(raw)
  new=(pref.group() if pref else '')+trans
  assert CONTROL.findall(new)==CONTROL.findall(raw),(n,i,'control',CONTROL.findall(raw),CONTROL.findall(new))
  assert trans.count('▼')<=max(2,raw.count('▼')),(n,i,'pages')
  assert unicodedata.normalize('NFC',trans)==trans,(n,i,'NFC')
  maxbytes=rec.get('max_utf8_bytes')
  if maxbytes: assert len(new.encode('utf8'))<=maxbytes,(n,i,'bytes',len(new.encode('utf8')),maxbytes)
  rec['vi']=new
  records.append({'file':str(target.relative_to(TARGET)),'id':rec['id'],'en':raw,'vi':new,'ctx':rec['ctx']})
 target.write_text(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n' for x in rows),encoding='utf8')
(ROOT/'DELTA-006.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in records),encoding='utf8')
print('Applied',len(records),'records across',len(NAMES),'files')