#!/usr/bin/env python3
"""Apply hand-written translations preserving source ID/control tokens."""
from pathlib import Path
import json, re, unicodedata, sys
ROOT=Path(__file__).resolve().parent
TOKEN=re.compile(r"\$\d+(?:'\d+)*;")
FRONT=re.compile(r"^(?:(?:\$0(?:24|23|22)'\d+(?:'\d+)*;))+")
TAIL=re.compile(r"(?:\$0(?:19|34)'\d+(?:'\d+)*;)+$")
TARGETS=[('talkfigs__0eng__data__0020.005.jsonl','manual_0020_005.txt'),('talkfigs__0eng__data__0021.001.jsonl','manual_0021_001.txt')]
report=[]
for filename,manual_name in TARGETS:
 manual=ROOT/manual_name
 if not manual.exists(): continue
 path=ROOT/'translation'/'04-thoai'/filename
 raw=path.read_text(encoding='utf8').splitlines()
 recs=[json.loads(v) for v in raw]
 trans=manual.read_text(encoding='utf8').splitlines()
 if len(trans)>len(recs):raise ValueError(f'{manual_name}: {len(trans)} translations > {len(recs)} records')
 changed=0
 for i,vi in enumerate(trans):
  d=recs[i];src=d['en']
  if d['vi'] not in ('',None):
   if d['vi'] == (FRONT.search(src).group(0) if FRONT.search(src) else '')+vi.strip()+(TAIL.search(src).group(0) if TAIL.search(src) else ''):continue
   raise ValueError(f'overwriting {d["id"]}')
  if not vi.strip():raise ValueError(f'blank translation at {i}')
  a=FRONT.search(src);b=TAIL.search(src)
  vi=(a.group(0) if a else '')+vi.strip()+(b.group(0) if b else '')
  vi=unicodedata.normalize('NFC',vi)
  if TOKEN.findall(src)!=TOKEN.findall(vi): raise ValueError(f'control tokens at {i}: {TOKEN.findall(src)} vs {TOKEN.findall(vi)}')
  if vi.count('▼')>3: raise ValueError(f'too many lines at {i}')
  if max(len(x) for x in TOKEN.sub('',vi).split('▼'))>34: raise ValueError(f'line length >34 at {i}: {vi}')
  if any(ch in vi for ch in '\r\t\n'):raise ValueError(f'bad special chars {i}')
  if d.get('max_utf8_bytes') and len(vi.encode('utf8'))>d['max_utf8_bytes']:raise ValueError(f'utf8 bytes at {i}')
  d['vi']=vi; changed+=1
 path.write_text(''.join(json.dumps(d,ensure_ascii=False,separators=(',',':'))+'\n' for d in recs),encoding='utf8')
 report.append((filename,changed))
print(report)