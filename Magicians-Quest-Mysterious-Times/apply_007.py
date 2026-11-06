#!/usr/bin/env python3
"""Create checkpoint 007 from checkpoint 006 without touching source fields."""
from pathlib import Path
import json,re,unicodedata,sys
ROOT=Path(__file__).resolve().parent
TOK=re.compile(r"\$\d{3}(?:'[^;\r\n\t]*)?;")
START=re.compile(r"^((?:\$(?:024|023|022)'[^;\r\n\t]*;)+)")
new=[]
for g in ('0004','0005'):
 path=ROOT/'translation'/'04-thoai'/f'talkfigs__0eng__data__{g}.001.jsonl'
 rows=[json.loads(s) for s in path.read_text(encoding='utf8').splitlines()]
 manual=(ROOT/f'manual_{g}.txt').read_text(encoding='utf8').splitlines()
 assert len(rows)==len(manual),(g,len(rows),len(manual))
 for idx,(r,vi) in enumerate(zip(rows,manual),1):
  assert r['vi'] is None, (g,idx)
  leading=START.match(r['en'])
  prefix=leading.group(1) if leading else ''
  # Replace the sole named NPC variable with its exact source token.
  if '$503\'??;' in vi:
   matches=[t for t in TOK.findall(r['en']) if t.startswith('$503\'')]
   assert len(matches)==1,(g,idx,matches)
   vi=vi.replace("$503'??;", matches[0])
  vi=prefix+vi
  if TOK.findall(vi)!=TOK.findall(r['en']):
   raise ValueError(f'TOK {g}#{idx} expected={TOK.findall(r["en"])} actual={TOK.findall(vi)}')
  if vi.count('▼')>max(2,r['en'].count('▼')):
   raise ValueError(f'WRAP {g}#{idx} {vi}')
  if any(x in vi for x in ['\t','\r','\n']):raise ValueError(f'Control {g}#{idx}')
  if unicodedata.normalize('NFC',vi)!=vi:raise ValueError(f'NFC {g}#{idx}')
  if r.get('max_utf8_bytes') and len(vi.encode('utf8'))>r['max_utf8_bytes']:raise ValueError(f'BYTES {g}#{idx}')
  r['vi']=vi
  new.append({'file':str(path.relative_to(ROOT/'translation')),'id':r['id'],'en':r['en'],'vi':vi,'ctx':r.get('ctx')})
 path.write_text(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in rows),encoding='utf8')
(ROOT/'DELTA-007.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in new),encoding='utf8')
print('OK, updated rows:',len(new))