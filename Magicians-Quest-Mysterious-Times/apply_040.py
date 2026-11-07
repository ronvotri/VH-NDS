#!/usr/bin/env python3
"""Apply handwritten VI pages from vi_0032_00{3,4}_raw.txt to existing JSONL.
Only fills vi when empty or identical to expected output; all technical fields preserved.
Run from the extracted checkpoint directory. No network/ROM required.
"""
from pathlib import Path
import re, json, unicodedata
ROOT=Path(__file__).resolve().parent
TOKEN=re.compile(r'\$[0-9\']+;')
START=re.compile(r'^(?:\$[0-9\']+;)+')
END=re.compile(r'(?:\$[0-9\']+;)+$')

def wrap(s,width=34):
 chunks=[];line=''
 for part in s.split(' '):
  if not part:continue
  test=(line+' '+part) if line else part
  if len(TOKEN.sub('',test))>width and line:
   chunks.append(line);line=part
  else:line=test
 if line:chunks.append(line)
 assert len(chunks)<=4,('page overflow',s)
 return '▼'.join(chunks)

def apply(stem):
 path=ROOT/'translation'/'04-thoai'/f'talkfigs__0eng__data__{stem}.jsonl'
 manual=ROOT/f'vi_{stem.replace(".","_")}_raw.txt'
 records=[json.loads(s) for s in path.read_text('utf8').splitlines()]
 cores=manual.read_text('utf8').splitlines()
 assert len(records)==len(cores)==120
 for i,(r,vi) in enumerate(zip(records,cores)):
  en=r['en']; p=START.match(en); p=p.group() if p else ''
  q=END.search(en); q=q.group() if q else ''
  if p and vi.startswith(p):p=''
  if p.endswith("$000'3;") and vi.startswith("$000'3;"):vi=vi[len("$000'3;"):]
  if p.endswith('$500;') and vi.startswith('$500;'):vi=vi[len('$500;'):]
  if p.endswith("$000'1;") and '$507' in p and vi.startswith("$507'393;"):
   vi=vi[len("$507'393;"):]
  out=wrap(p+unicodedata.normalize('NFC',vi)+q)
  assert TOKEN.findall(out)==TOKEN.findall(en),(stem,i,'control')
  assert r.get('vi') in (None,'',out),(stem,i,'refuse overwrite')
  r['vi']=out
 path.write_text('\n'.join(json.dumps(x,ensure_ascii=False,separators=(',',':')) for x in records)+'\n','utf8')
 print(stem,len(records),'pages applied')

if __name__=='__main__':
 for stem in ('0032.003','0032.004'):apply(stem)