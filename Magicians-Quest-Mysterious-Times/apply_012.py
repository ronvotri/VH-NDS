#!/usr/bin/env python3
"""Apply handwritten MQ NDS dialogue pages without changing ROM control codes."""
import json, re, unicodedata
from pathlib import Path
ROOT=Path(__file__).resolve().parent
TOK=re.compile(r"\$\d+(?:'[-\d]+)*;")
FRONT=re.compile(r"^(?:\$(?:024|023|022|040)'[-\d]+(?:'[-\d]+)*;)+")
TARGETS=(('talkfigs__0eng__data__0021.002.jsonl','manual_0021_002.txt'),('talkfigs__0eng__data__0021.003.jsonl','manual_0021_003.txt'))
for fname,manual in TARGETS:
 path=ROOT/'translation'/'04-thoai'/fname
 data=[json.loads(s) for s in path.read_text(encoding='utf8').splitlines()]
 texts=(ROOT/manual).read_text(encoding='utf8').splitlines()
 assert len(texts)==len(data)==120, (fname,len(texts),len(data))
 for i,(row,phrase) in enumerate(zip(data,texts),1):
  assert row['vi'] is None, (fname,i,'already translated')
  assert phrase.strip() and '▼' not in phrase[:1] and '▼' not in phrase[-1:], (fname,i)
  # Preserve exact leading facial expression / event control codes.
  prefix=FRONT.search(row['en'])
  vi=(prefix.group() if prefix else '')+phrase
  vi=unicodedata.normalize('NFC',vi)
  assert TOK.findall(vi)==TOK.findall(row['en']), (fname,i, TOK.findall(row['en']),TOK.findall(vi))
  assert vi.count('▼')<=3, (fname,i,'line count')
  assert all(len(TOK.sub('',ln))<=34 for ln in vi.split('▼')), (fname,i,vi)
  assert not any(ch in vi for ch in '\n\r\t'), (fname,i,'formatting')
  if row.get('max_utf8_bytes') is not None:
   assert len(vi.encode('utf8'))<=row['max_utf8_bytes'], (fname,i,'byte limit')
  row['vi']=vi
 path.write_text(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in data),encoding='utf8')
 print('TRANSLATED:',fname,len(data))