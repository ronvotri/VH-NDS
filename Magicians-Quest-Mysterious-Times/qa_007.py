#!/usr/bin/env python3
"""Audit checkpoint 006 to checkpoint 007: diff is only 190 fresh vi values."""
from collections import Counter
from pathlib import Path
import json,re,unicodedata,sys
ROOT=Path(__file__).resolve().parent
OLD=ROOT.parent/'MagiciansQuest_006'/'translation'
NEW=ROOT/'translation'
TOK=re.compile(r"\$\d{3}(?:'[^;\r\n\t]*)?;")
new=[];errs=[];warnings=[];group=Counter(); perfile=Counter(); total=0
oldfiles=sorted(OLD.rglob('*.jsonl'))
for f in oldfiles:
 rel=f.relative_to(OLD); target=NEW/rel
 if not target.exists(): errs.append('missing '+str(rel));continue
 a=[json.loads(x) for x in f.read_text(encoding='utf8').splitlines()]
 b=[json.loads(x) for x in target.read_text(encoding='utf8').splitlines()]
 if len(a)!=len(b):errs.append('row-count '+str(rel));continue
 for line,(x,y) in enumerate(zip(a,b),1):
  if x.keys()!=y.keys():errs.append(f'keys {rel}:{line}')
  if any(x[k]!=y[k] for k in x if k!='vi'):errs.append(f'non-vi change {rel}:{line}')
  if x['vi']!=y['vi']:
   if x['vi'] is not None or y['vi'] is None:errs.append(f'overwrite {rel}:{line}')
   else:
    v=y['vi'];e=y['en']
    if TOK.findall(v)!=TOK.findall(e):errs.append(f'token {rel}:{line}')
    if v.count('▼')>max(2,e.count('▼')):errs.append(f'wrap {rel}:{line}')
    if any(ch in v for ch in '\r\n\t'):errs.append(f'format-control {rel}:{line}')
    if unicodedata.normalize('NFC',v)!=v:errs.append(f'NFC {rel}:{line}')
    if y.get('max_utf8_bytes') and len(v.encode('utf8'))>y['max_utf8_bytes']:errs.append(f'byte-overflow {rel}:{line}')
    visual=[len(TOK.sub('',ln).strip()) for ln in v.split('▼')]
    if max(visual)>34:warnings.append(f'{rel}:{line} {visual} {v}')
    new.append({'file':str(rel),'id':y['id'],'en':e,'vi':v,'ctx':y.get('ctx')})
    perfile[str(rel)]+=1
  if y['vi'] is not None:group[str(rel).split('/')[0]]+=1;total+=1
extra=[str(f.relative_to(NEW)) for f in NEW.rglob('*.jsonl') if not (OLD/f.relative_to(NEW)).exists()]
if extra:errs+=['extra '+str(x) for x in extra]
assert len(oldfiles)==501,len(oldfiles)
assert len(new)==190,len(new)
assert len(perfile)==2,len(perfile)
assert total==4272,(total,group)
if errs:
 print('FAIL',len(errs),*errs[:30],sep='\n');sys.exit(1)
# A page may still be too wide in actual 160 px font even when <=34 Unicode chars.
report=['# QA checkpoint 007','','- Baseline: checkpoint 006 — **4.082/55.976** mục.','- Mới xử lý: **190** trang thoại, tổng **4.272/55.976** mục (7,63%).','- Đối chiếu **501** file JSONL: chỉ bổ sung `vi` đang trống, không đổi ID, EN, ctx hoặc dữ liệu kỹ thuật.','- Bảo toàn các mã `$...;`, dấu ngắt `▼`, định dạng UTF-8 NFC và giới hạn byte.','- Cảnh báo dòng dài hơn 34 ký tự (không tính mã điều khiển): **'+str(len(warnings))+'**.','- Chưa xác nhận hiển thị thực tế/font pixel trên ROM NDS; cần thử trong game.','','| Tệp | Trang mới |','|---|---:|']
report += [f'| `{p}` | {n} |' for p,n in sorted(perfile.items())]
if warnings:
 report += ['','## Dòng dài cần kiểm tra']+[f'- {x}' for x in warnings]
(ROOT/'QA-007.md').write_text('\n'.join(report)+'\n',encoding='utf8')
(ROOT/'DELTA-007.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n' for x in new),encoding='utf8')
print('PASS',len(oldfiles),'files',len(new),'new pages',total,'total',dict(group),'WARN',len(warnings))