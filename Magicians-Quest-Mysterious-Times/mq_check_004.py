#!/usr/bin/env python3
"""Compare checkpoint 003 and 004 for only-vi edits and unchanged JSONL records."""
from pathlib import Path
import json,hashlib,collections,unicodedata,re
A=Path('/mnt/data/MagiciansQuest_003/translation')
B=Path('/mnt/data/MagiciansQuest_004/translation')
allfiles=sorted(A.rglob('*.jsonl'))
files=[];delta=[];errors=[]
counts=collections.Counter()
for src in allfiles:
 rel=src.relative_to(A);b=B/rel
 if not b.exists():errors.append('file missing '+str(rel));continue
 x=[json.loads(s) for s in src.read_text(encoding='utf8').splitlines()]
 y=[json.loads(s) for s in b.read_text(encoding='utf8').splitlines()]
 if len(x)!=len(y):errors.append('row count changed '+str(rel));continue
 c=0
 for i,(o,n) in enumerate(zip(x,y)):
  if set(o)!=set(n):errors.append('key set modified '+str(rel));continue
  for k in o.keys():
   if k!='vi' and o[k]!=n[k]:errors.append('non-vi change '+str(rel)+' row '+str(i)+' '+k)
  if o['vi']!=n['vi']:
   if o['vi'] is not None:errors.append('existing vi overwritten '+str(rel)+' '+str(i));continue
   if n['vi'] is None:errors.append('unexpected blank '+str(rel)+' '+str(i));continue
   c+=1
   delta.append(dict(file=str(rel),id=n['id'],en=n['en'],vi=n['vi'],ctx=n.get('ctx')))
  if n['vi'] is not None:counts[str(rel).split('/')[0]]+=1
 if c:files.append((str(rel),c))
for extra in B.rglob('*.jsonl'):
 if not (A/extra.relative_to(B)).exists():errors.append('untracked file '+str(extra))
old_n=sum(1 for f in allfiles for s in f.read_text(encoding='utf8').splitlines() if json.loads(s).get('vi') is not None)
assert old_n==2014,old_n
assert len(delta)==1368,(len(delta),len(files))
assert sum(counts.values())==3382,counts
assert not errors,errors[:12]
(B.parent/'DELTA-004.jsonl').write_text(''.join(json.dumps(row,ensure_ascii=False,separators=(',',':'))+'\n' for row in delta),encoding='utf8')
(B.parent/'QA-004.md').write_text('# Kiểm tra checkpoint 004\n\n'+f'- Từ {old_n} lên {sum(counts.values())} trường `vi` (+{len(delta)}).\n'+f'- **{len(allfiles)} JSONL nguyên cấu trúc**, chỉ chỉnh trường `vi` của {len(files)} tệp.\n'+'- Kiểm tra mã điều khiển, giới hạn byte, Unicode NFC qua `qa_checkpoint.py`: PASS.\n'+'- **Chưa kiểm tra trên ROM/font thực tế.**\n\n'+'| Tệp thay đổi | Số mới |\n|---|---:|\n'+'\n'.join(f'| `{r}` | {n} |' for r,n in files)+'\n',encoding='utf8')
print('PASS',dict(counts),'TOTAL',len(delta)+old_n,'delta',len(delta),'files',len(files));print(files)