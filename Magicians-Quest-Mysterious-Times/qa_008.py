#!/usr/bin/env python3
"""Compare all checkpoint 007 JSONL rows to checkpoint 008; reject non-vi edits."""
from pathlib import Path
from collections import Counter
import json,re,unicodedata,sys
root=Path(__file__).resolve().parent
oldroot=Path('/mnt/data/MagiciansQuest_007/translation')
newroot=root/'translation'
tok=re.compile(r"\$\d{3}(?:'[^;\r\n\t]*)?;")
errors=[];warnings=[];news=[];byfile=Counter(); counts=Counter(); total=0
oldfiles=sorted(oldroot.rglob('*.jsonl'))
for oldfile in oldfiles:
    rel=oldfile.relative_to(oldroot); newfile=newroot/rel
    if not newfile.exists():errors.append(f'Missing file {rel}');continue
    old=[json.loads(s) for s in oldfile.read_text(encoding='utf-8').splitlines()]
    new=[json.loads(s) for s in newfile.read_text(encoding='utf-8').splitlines()]
    if len(old)!=len(new):errors.append(f'Count mismatch {rel}');continue
    for rowid,(a,b) in enumerate(zip(old,new),1):
        if a.keys()!=b.keys() or any(a[k]!=b[k] for k in a if k!='vi'):errors.append(f'Unexpected field change {rel}:{rowid}');continue
        if a.get('vi')!=b.get('vi'):
            if a['vi'] is not None or b['vi'] is None:errors.append(f'Overwrite {rel}:{rowid}');continue
            vi=b['vi']; en=b['en']
            if tok.findall(vi)!=tok.findall(en):errors.append(f'Control tokens {rel}:{rowid}')
            if vi.count('▼')>max(2,en.count('▼')):errors.append(f'Page lines {rel}:{rowid}')
            if any(x in vi for x in '\r\n\t'):errors.append(f'Unexpected control chars {rel}:{rowid}')
            if unicodedata.normalize('NFC',vi)!=vi:errors.append(f'Not NFC {rel}:{rowid}')
            if b.get('max_utf8_bytes') is not None and len(vi.encode('utf-8'))>b['max_utf8_bytes']:errors.append(f'UTF8 overflow {rel}:{rowid}')
            lengths=[len(tok.sub('',line).strip()) for line in vi.split('▼')]
            if max(lengths)>34:warnings.append(f'{rel}:{rowid} long {lengths}')
            news.append({'file':str(rel),'id':b['id'],'en':en,'vi':vi,'ctx':b.get('ctx')})
            byfile[str(rel)]+=1
        if b.get('vi') is not None:
            counts[str(rel).split('/')[0]]+=1
            total+=1
extras=[str(x.relative_to(newroot)) for x in newroot.rglob('*.jsonl') if not (oldroot/x.relative_to(newroot)).exists()]
if extras:errors.extend('New unexpected file '+s for s in extras)
if len(oldfiles)!=501:errors.append(f'Expected 501 JSONL; found {len(oldfiles)}')
if len(news)!=178:errors.append(f'Expected 178 changes; found {len(news)}')
if total!=4450:errors.append(f'Expected 4450 translated; found {total}')
if set(byfile.values())!={84,94}:errors.append(f'Wrong changes per group: {byfile}')
report=['# QA checkpoint 008','',f'- Baseline: checkpoint 007 — 4.272/55.976 mục.','- Đợt 008: **178 trang hội thoại mới**, tổng **4.450/55.976 (7,95%)**.','- Đối chiếu 501 tệp JSONL; chỉ được điền `vi` ở các mục trước đó chưa dịch.','- Đối chiếu token `$...;`, dấu `▼`, Unicode NFC, dấu xuống dòng, byte UTF-8.','- Số cảnh báo dòng dài hơn 34 ký tự: **'+str(len(warnings))+'**.','- Chưa kiểm thử pixel/font thực tế trong ROM NDS.','','| Tệp | Trang mới |','|---|---:|']
report += [f'| `{path}` | {n} |' for path,n in sorted(byfile.items())]
if errors:report += ['','## Lỗi']+[f'- {e}' for e in errors]
if warnings:report += ['','## Cảnh báo']+[f'- {w}' for w in warnings]
(root/'QA-008.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
(root/'DELTA-008.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n' for x in news),encoding='utf-8')
print('QA', 'FAIL' if errors else 'PASS', 'files',len(oldfiles),'new',len(news),'total',total,'warnings',len(warnings),'errors',len(errors))
for x in errors[:15]:print('ERROR:',x)
for x in warnings[:10]:print('WARNING:',x)
if errors:sys.exit(1)