#!/usr/bin/env python3
from pathlib import Path
import re,json,unicodedata
R=Path('/mnt/data/mq35/MagiciansQuest_034')
B=Path('/mnt/data/mq35')
TOK=re.compile(r"\$\d+(?:'[-\d]+)*;")
LEAD=re.compile(r"^(?:(?:\$(?:034|024|023|022|040)'[-\d]+(?:'[-\d]+)*;)+)")

def visible(s):
 return len(TOK.sub('',s))
def wrap(s,limit=31):
 words=s.strip().split()
 lines=[];cur=''
 for w in words:
  nxt=(cur+' '+w).strip() if cur else w
  if cur and visible(nxt)>limit:
   lines.append(cur);cur=w
  else:cur=nxt
 if cur:lines.append(cur)
 return '▼'.join(lines)

failed=[]
for fn in ('0030.003','0030.004'):
 source=R/'translation'/'04-thoai'/f'talkfigs__0eng__data__{fn}.jsonl'
 rows=[json.loads(x) for x in source.read_text('utf8').splitlines()]
 raw=(B/f'vi_{fn.replace(".","_")}_raw.txt').read_text('utf8').splitlines()
 assert len(rows)==len(raw)==120
 out=[]
 for i,(row,line) in enumerate(zip(rows,raw),1):
  en=row['en']; prefix=LEAD.match(en).group(0) if LEAD.match(en) else ''
  vi=unicodedata.normalize('NFC',prefix+wrap(line))
  if TOK.findall(en)!=TOK.findall(vi):failed.append((fn,i,'tokens',TOK.findall(en),TOK.findall(vi),en,vi))
  if vi.count('▼')>3:failed.append((fn,i,'page breaks',vi))
  if max(visible(x) for x in vi.split('▼'))>34:failed.append((fn,i,'line width',vi))
  if any(c in vi for c in '\n\r\t'):failed.append((fn,i,'whitespace',vi))
  if len(vi.encode('utf8'))>row.get('max_utf8_bytes',1<<30):failed.append((fn,i,'bytes',vi))
  out.append(vi)
 (B/f'vi_{fn.replace(".","_")}.txt').write_text('\n'.join(out)+'\n',encoding='utf8')
 print(fn,'max_lines',max(len(s.split('▼')) for s in out),'max_vis',max(max(visible(z) for z in s.split('▼')) for s in out),'issues',len([x for x in failed if x[0]==fn]))
 print('bad lines:')
 for x in failed:
  if x[0]==fn:print(' ',str(x)[:500])
if failed: raise SystemExit(1)