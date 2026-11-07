#!/usr/bin/env python3
"""Non-destructively apply delta 035 to a canonical checkpoint 034 translation tree.
Run from inside the extracted checkpoint 035 directory only for QA/recovery;
existing translated values are not overwritten.
"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
patch=[json.loads(s) for s in (ROOT/'DELTA-035.jsonl').read_text('utf8').splitlines()]
by_file={}
for d in patch:by_file.setdefault(d['file'],[]).append(d)
for rel,items in by_file.items():
 path=ROOT/'translation'/rel
 rows=[json.loads(s) for s in path.read_text('utf8').splitlines()]
 by_id={r['id']:r for r in rows}
 for x in items:
  cur=by_id[x['id']]
  assert cur['en']==x['en'] and cur.get('vi') in (None,'',x['vi'])
  cur['vi']=x['vi']
 path.write_text('\n'.join(json.dumps(x,ensure_ascii=False,separators=(',',':')) for x in rows)+'\n','utf8')
print('Applied or confirmed',len(patch),'translations')