#!/usr/bin/env python3
"""Strict checkpoint 005 -> 006 audit with length warnings."""
from collections import Counter
from pathlib import Path
import json,re,unicodedata,sys
ROOT=Path(__file__).resolve().parent
OLD=ROOT.parent/'MagiciansQuest_005'/'translation'
NEW=ROOT/'translation'
TOK=re.compile(r"\$\d{3}(?:'[^;\r\n\t]*)?;")
new=[]; errs=[]; warnings=[]; g=Counter(); group=Counter()
files=sorted(OLD.rglob('*.jsonl'))
for f in files:
 path=f.relative_to(OLD);target=NEW/path
 if not target.exists():errs.append(f'missing {path}');continue
 aa=[json.loads(x) for x in f.read_text(encoding='utf8').splitlines()]
 bb=[json.loads(x) for x in target.read_text(encoding='utf8').splitlines()]
 if len(aa)!=len(bb):errs.append(f'row count {path}');continue
 for line,(a,b) in enumerate(zip(aa,bb),1):
  if a.keys()!=b.keys():errs.append(f'keys {path}:{line}')
  for k in a:
   if k!='vi' and a[k]!=b[k]:errs.append(f'altered {k} {path}:{line}')
  if a['vi']!=b['vi']:
   if a['vi'] is not None or b['vi'] is None: errs.append(f'overwrite {path}:{line}')
   else:
    va=b['vi']; en=b['en']
    if TOK.findall(en)!=TOK.findall(va):errs.append(f'control {path}:{line}')
    if va.count('▼')>max(2,en.count('▼')):errs.append(f'page wraps {path}:{line}')
    if unicodedata.normalize('NFC',va)!=va:errs.append(f'non NFC {path}:{line}')
    if b.get('max_utf8_bytes') and len(va.encode('utf8'))>b['max_utf8_bytes']:errs.append(f'byte overflow {path}:{line}')
    if '\t' in va or '\r' in va or '\n' in va:errs.append(f'line control {path}:{line}')
    width=[len(TOK.sub('',s).strip()) for s in va.split('▼')]
    if max(width)>34:warnings.append((str(path),line,width,va))
    new.append({'file':str(path),'id':b['id'],'en':en,'vi':va,'ctx':b.get('ctx')})
    g[str(path)]+=1
  if b['vi'] is not None: group[str(path).split('/')[0]]+=1
extra=[str(f.relative_to(NEW)) for f in NEW.rglob('*.jsonl') if not (OLD/f.relative_to(NEW)).exists()]
if extra:errs+=['extra '+str(p) for p in extra]
assert len(files)==501,len(files)
assert len(new)==368,len(new)
assert len(g)==5,len(g)
assert sum(group.values())==4082, group
if errs:print('FAIL',len(errs),*errs[:30],sep='\n');sys.exit(1)
# Limit warnings to avoid hard-coded pixel assumptions; report each.
lines=['# QA Checkpoint 006','','- Baseline: 005 — 3.714/55.976 mục.','- Kết quả: **4.082/55.976**, bổ sung **368** trang thoại.','- 501 tệp JSONL đối chiếu: ID, `en`, `ctx`, thứ tự và trường kỹ thuật không thay đổi.','- 5 tệp thoại có thay đổi; chỉ bổ sung trường `vi` trước đó trống.','- Mã `$...;`, dấu `▼`, Unicode NFC và giới hạn byte: **PASS**.','- Chưa test pixel-width và hiển thị trên ROM/giả lập; cần rà bằng đúng font.','',f'- Cảnh báo chiều dài dòng (>34 ký tự, đã bỏ mã): **{len(warnings)}**.','', '| Tệp | Mục mới |','|---|---:|']
lines += [f'| `{f}` | {count} |' for f,count in sorted(g.items())]
if warnings:
 lines+=['','## Các dòng cần kiểm tra tràn pixel','']
 lines += [f'- `{f}:{ln}` — {width} — `{s}`' for f,ln,width,s in warnings]
(ROOT/'QA-006.md').write_text('\n'.join(lines)+'\n',encoding='utf8')
(ROOT/'DELTA-006.jsonl').write_text(''.join(json.dumps(s,ensure_ascii=False,separators=(',',':'))+'\n' for s in new),encoding='utf8')
print('PASS',len(files),'files',len(new),'new',dict(group),'WARN_LONG',len(warnings));
for w in warnings[:35]:print(w)