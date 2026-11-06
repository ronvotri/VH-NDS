#!/usr/bin/env python3
"""Strict checkpoint-008 -> checkpoint-009 comparison, emitting delta and QA report.
Usage: python qa_009.py [directory of extracted checkpoint 008]
"""
from pathlib import Path
import json,re,unicodedata,sys
from collections import Counter
ROOT=Path(__file__).resolve().parent
OLD=Path(sys.argv[1]) if len(sys.argv)>1 else Path('/mnt/data/MQ-extract-008/MagiciansQuest_008')
TOK=re.compile(r"\$\d{3}(?:'[^;\r\n\t]*)?;")
errors=[];warnings=[];changes=[];counts=Counter();byfile=Counter();translations=Counter()
basefiles=sorted((OLD/'translation').rglob('*.jsonl'))
newfiles=sorted((ROOT/'translation').rglob('*.jsonl'))
if len(basefiles)!=501 or len(newfiles)!=501:errors.append(f'Expected 501 JSONL: old={len(basefiles)}, new={len(newfiles)}')
for oldfile in basefiles:
    rel=oldfile.relative_to(OLD/'translation')
    newfile=ROOT/'translation'/rel
    if not newfile.is_file():errors.append(f'Missing {rel}');continue
    prev=[json.loads(s) for s in oldfile.read_text(encoding='utf-8').splitlines()]
    curr=[json.loads(s) for s in newfile.read_text(encoding='utf-8').splitlines()]
    if len(prev)!=len(curr):errors.append(f'Row count {rel}');continue
    for line,(a,b) in enumerate(zip(prev,curr),1):
        if a.keys()!=b.keys() or any(a[k]!=b[k] for k in a if k!='vi'):
            errors.append(f'Unexpected non-VI change {rel}:{line}');continue
        if a['vi']!=b['vi']:
            if a['vi'] is not None or b['vi'] is None:
                errors.append(f'Overwrite existing translation {rel}:{line}');continue
            en,vi=b['en'],b['vi']
            if TOK.findall(vi)!=TOK.findall(en):errors.append(f'Control token mismatch {rel}:{line}')
            if vi.count('▼')>max(2,en.count('▼')):errors.append(f'Too many visual lines {rel}:{line}')
            if any(ch in vi for ch in '\r\n\t'):errors.append(f'Invalid whitespace {rel}:{line}')
            if unicodedata.normalize('NFC',vi)!=vi:errors.append(f'Unicode not NFC {rel}:{line}')
            if b.get('max_utf8_bytes') is not None and len(vi.encode('utf-8'))>b['max_utf8_bytes']:errors.append(f'Byte limit overflow {rel}:{line}')
            line_lengths=[len(TOK.sub('',x).strip()) for x in vi.split('▼')]
            if max(line_lengths)>34:warnings.append(f'{rel}:{line} long line {line_lengths}')
            changes.append({'file':rel.as_posix(),'id':b['id'],'en':en,'vi':vi,'ctx':b.get('ctx')})
            byfile[rel.as_posix()]+=1
        if b['vi'] is not None:
            counts[rel.parts[0]]+=1
if any(x.relative_to(ROOT/'translation') not in {f.relative_to(OLD/'translation') for f in basefiles} for x in newfiles):errors.append('Extra JSONL')
if len(changes)!=240:errors.append(f'Expected 240 changes, found {len(changes)}')
if dict(byfile)!={f'04-thoai/talkfigs__0eng__data__0020.{n}.jsonl':120 for n in ('001','002')}:
    errors.append(f'Unexpected changed files/counts {byfile}')
if sum(counts.values())!=4690:errors.append(f'Expected 4,690 translated records, got {sum(counts.values())}')
(ROOT/'DELTA-009.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n' for x in changes),encoding='utf-8')
report=[
'# QA checkpoint 009','',
'**Baseline:** checkpoint 008: 4.450/55.976. **Current:** 4.690/55.976 (+240).','',
'- Chỉ sửa `vi` ở 240 trang trước đây còn trống; không thay ID, EN, `ctx`, thứ tự hoặc biến kỹ thuật.',
'- Kiểm thử 501 tệp JSONL: token `$...;` theo thứ tự, dấu `▼`, Unicode NFC, byte UTF-8 nếu có giới hạn.',
'- Cảnh báo dòng dài >34 ký tự sau khi bỏ token: '+str(len(warnings))+'.',
'- **Chưa kiểm thử chiều rộng pixel của font NDS, chưa kiểm thử bằng ROM sạch**.','',
'| Tệp | Trang mới |','|---|---:|'
]
report += [f'| `{p}` | {n} |' for p,n in byfile.items()]
if warnings:report+=['','## Cảnh báo']+[f'- {x}' for x in warnings]
if errors:report+=['','## Lỗi']+[f'- {x}' for x in errors]
(ROOT/'QA-009.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
print('QA', 'FAIL' if errors else 'PASS','files',len(basefiles),'changes',len(changes),'total',sum(counts.values()),'warnings',len(warnings),'errors',len(errors))
print('BYGROUP',dict(counts))
for x in errors[:20]:print('ERROR:',x)
for x in warnings[:15]:print('WARNING:',x)
if errors:raise SystemExit(1)