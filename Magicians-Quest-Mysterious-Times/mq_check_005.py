#!/usr/bin/env python3
"""Delta QA: compare fixed checkpoint 004 with this 005; only add translations to empty vi fields."""
from pathlib import Path
from collections import Counter
import json,unicodedata,re,hashlib
BASE=Path(__file__).resolve().parent
OLD=BASE.parent/'MagiciansQuest_004/translation'
NEW=BASE/'translation'
RE=re.compile(r"\$\d{3}(?:'[^;\r\n\t]*)?;")
changes=[]; groups=Counter(); altered=[]; errors=[]
files=sorted(OLD.rglob('*.jsonl'))
assert len(files)>500, 'invalid source file count'
for f in files:
 rel=f.relative_to(OLD); g=NEW/rel
 if not g.exists(): errors.append(f'missing {rel}');continue
 a=[json.loads(t) for t in f.read_text(encoding='utf8').splitlines()]
 b=[json.loads(t) for t in g.read_text(encoding='utf8').splitlines()]
 if len(a)!=len(b):errors.append(f'row count {rel}');continue
 for n,(before,after) in enumerate(zip(a,b),1):
  if before.keys()!=after.keys(): errors.append(f'keys {rel}:{n}');continue
  for key in before:
   if key!='vi' and before[key]!=after[key]:errors.append(f'non-vi {rel}:{n} {key}')
  if before['vi']!=after['vi']:
   if before['vi'] is not None: errors.append(f'overwrite prior translation {rel}:{n}');continue
   if after['vi'] is None: errors.append(f'removed translation {rel}:{n}');continue
   orig,bn=after['en'],after['vi']
   if RE.findall(orig)!=RE.findall(bn):errors.append(f'control {rel}:{n}')
   if bn.count('▼')>max(2,orig.count('▼')):errors.append(f'visual lines {rel}:{n}')
   if unicodedata.normalize('NFC',bn)!=bn:errors.append(f'unicode {rel}:{n}')
   if after.get('max_utf8_bytes') and len(bn.encode('utf8'))>after['max_utf8_bytes']:errors.append(f'bytes {rel}:{n}')
   changes.append({'file':str(rel),'id':after['id'],'en':orig,'vi':bn,'ctx':after.get('ctx')})
   altered.append(str(rel))
  if after['vi'] is not None:groups[str(rel).split('/')[0]]+=1
for g in NEW.rglob('*.jsonl'):
 if not (OLD/g.relative_to(NEW)).exists():errors.append(f'untracked extra {g.relative_to(NEW)}')
assert not errors, '\n'.join(errors[:20])
assert sum(groups.values())==3714,groups
assert len(changes)==332,len(changes)
assert len(set(altered))==4,set(altered)
(BASE/'DELTA-005.jsonl').write_text(''.join(json.dumps(s,ensure_ascii=False,separators=(',',':'))+'\n' for s in changes),encoding='utf8')
summary=Counter(altered)
text='# QA Checkpoint 005\n\n'
text+='- Baseline: checkpoint 004 — 3.382/55.976 trường `vi`.\n'
text+='- Checkpoint 005 — **3.714/55.976**, thêm **332 mục**.\n'
text+=f'- Kiểm tra **{len(files)} tệp JSONL**: mọi ID, thứ tự, trường `en`, `ctx`, giới hạn byte và cấu trúc giữ nguyên.\n'
text+='- Kiểm tra mã điều khiển, biến tên, ngắt trang, UTF-8, Unicode NFC: PASS.\n'
text+='- Chỉ bổ sung `vi` trước đó còn trống; không ghi đè 3.382 mục cũ.\n'
text+='- Chưa test font/hiển thị trên ROM sạch USA.\n\n| Tệp | Mục mới |\n|---|---:|\n'
text+='\n'.join(f'| `{k}` | {v} |' for k,v in sorted(summary.items()))+'\n'
(BASE/'QA-005.md').write_text(text,encoding='utf8')
print('PASS',len(files),'files',dict(groups),'new',len(changes),'modified files',len(summary))