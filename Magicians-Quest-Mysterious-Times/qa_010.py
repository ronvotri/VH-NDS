#!/usr/bin/env python3
"""QA checkpoint 010 against immutable checkpoint 009; emit delta and human report."""
import pathlib,json,re,unicodedata,collections,sys
OLD=pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else pathlib.Path('/mnt/data/MagiciansQuest_009')
NEW=pathlib.Path(__file__).resolve().parent
TOKEN=re.compile(r"\$\d{3}(?:'[^;\r\n\t]*)?;")
errors=[];warnings=[];changes=[];count=collections.Counter();byfile=collections.Counter();
a=sorted((OLD/'translation').rglob('*.jsonl'));b=sorted((NEW/'translation').rglob('*.jsonl'))
if len(a)!=501 or len(b)!=501:errors.append(f'JSONL count old={len(a)}, new={len(b)}')
if {f.relative_to(OLD/'translation') for f in a}!={f.relative_to(NEW/'translation') for f in b}:errors.append('JSONL filename set differs')
for old in a:
    rel=old.relative_to(OLD/'translation');new=NEW/'translation'/rel
    if not new.exists():errors.append(f'Missing {rel}');continue
    oa=[json.loads(x) for x in old.read_text(encoding='utf-8').splitlines()]
    nb=[json.loads(x) for x in new.read_text(encoding='utf-8').splitlines()]
    if len(oa)!=len(nb):errors.append(f'Row count changed {rel}');continue
    for index,(x,y) in enumerate(zip(oa,nb),1):
        if x.keys()!=y.keys() or any(x[k]!=y[k] for k in x if k!='vi'):
            errors.append(f'Non-VI mutation {rel}:{index}');continue
        if x['vi']!=y['vi']:
            if x['vi'] is not None or y['vi'] is None:errors.append(f'Overwrite old VI {rel}:{index}');continue
            src,tgt=y['en'],y['vi']
            if TOKEN.findall(src)!=TOKEN.findall(tgt):errors.append(f'Token mismatch {rel}:{index}')
            if tgt.count('▼')>max(2,src.count('▼')):errors.append(f'Visual line overflow {rel}:{index}')
            if any(c in tgt for c in '\n\r\t') or '¤' in tgt:errors.append(f'Invalid character {rel}:{index}')
            if unicodedata.normalize('NFC',tgt)!=tgt:errors.append(f'Not NFC {rel}:{index}')
            if y.get('max_utf8_bytes') is not None and len(tgt.encode('utf-8'))>y['max_utf8_bytes']:
                errors.append(f'Byte budget overflow {rel}:{index}')
            lengths=[len(TOKEN.sub('',q).strip()) for q in tgt.split('▼')]
            if max(lengths)>34:warnings.append(f'Long visual line {rel}:{index}: {lengths}')
            changes.append({'file':rel.as_posix(),'id':y['id'],'en':src,'vi':tgt,'ctx':y.get('ctx')})
            byfile[rel.as_posix()]+=1
        if y['vi'] is not None: count[rel.parts[0]]+=1
if len(changes)!=240:errors.append(f'Expected 240 changes but saw {len(changes)}')
expected={f'04-thoai/talkfigs__0eng__data__0020.{part}.jsonl':120 for part in ('003','004')}
if dict(byfile)!=expected:errors.append(f'Unexpected file counts: {dict(byfile)}')
if sum(count.values())!=4930:errors.append(f'Expected 4930 translated, got {sum(count.values())}')
(NEW/'DELTA-010.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n' for x in changes),encoding='utf-8')
report=['# QA — Magician’s Quest, checkpoint 010','',
'**Baseline:** checkpoint 009: 4.690/55.976. **New:** checkpoint 010: 4.930/55.976 (+240).','',
'- Đã đối chiếu 501 tệp JSONL với checkpoint 009; chỉ thay `vi` ở 240 mục chưa dịch.',
'- Bảo toàn `id`, `en`, `ctx`, thứ tự và tất cả trường dữ liệu khác.',
'- Kiểm tra tất cả mã `$...;` đúng thứ tự, dấu `▼`, NFC, byte UTF-8 nếu có giới hạn.',
'- Cảnh báo dòng hiển thị dài hơn 34 ký tự: '+str(len(warnings))+'.',
'- **Chưa kiểm tra bằng ROM/emulator; chưa xác minh chiều rộng pixel font và ngắt dòng thực tế.**','',
'| Tệp JSONL | Trang dịch mới |','|---|---:|']
report += [f'| `{p}` | {n} |' for p,n in sorted(byfile.items())]
if warnings: report+=['','## Cảnh báo']+['- '+x for x in warnings]
if errors: report+=['','## Lỗi']+['- '+x for x in errors]
(NEW/'QA-010.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
print('QA', 'FAILED' if errors else 'PASS', 'files',len(a),'changes',len(changes),'now',sum(count.values()),'warnings',len(warnings),'errors',len(errors))
print('BYGROUP',dict(count))
for x in errors[:12]:print('ERROR',x)
for x in warnings[:12]:print('WARNING',x)
if errors:raise SystemExit(1)