#!/usr/bin/env python3
"""Full field-level QA of checkpoint 028 against canonical checkpoint 027 ZIP."""
from pathlib import Path
import json,collections,re,unicodedata,zipfile,sys
ROOT=Path(__file__).resolve().parent
BASE=ROOT.parent/'MagiciansQuest-VietHoa-Checkpoint-027.zip'
TOK=re.compile(r"\$\d+(?:'[-\d]+)*;")
EXPECTED={'translation/04-thoai/talkfigs__0eng__data__0027.004.jsonl':120,'translation/04-thoai/talkfigs__0eng__data__0027.005.jsonl':81}
errors=[];changes=[];counts=collections.Counter();records=translated=0
with zipfile.ZipFile(BASE) as z:
    zip_prefix='MagiciansQuest_027/translation/'
    names=sorted(n for n in z.namelist() if n.startswith(zip_prefix) and n.endswith('.jsonl'))
    if len(names)!=501:errors.append(f'Expected 501 JSONL, got {len(names)}')
    for name in names:
        rel=name.split('/',1)[1]
        old=[json.loads(s) for s in z.read(name).decode('utf8').splitlines()]
        dst=ROOT/rel
        if not dst.exists():errors.append('Missing '+rel);continue
        new=[json.loads(s) for s in dst.read_text('utf8').splitlines()]
        if len(old)!=len(new):errors.append('Wrong row count '+rel);continue
        for o,n in zip(old,new):
            records+=1
            if o.keys()!=n.keys():errors.append(f'Fields/order {rel} {o.get("id")}')
            if any(o.get(k)!=n.get(k) for k in set(o)|set(n) if k!='vi'):
                errors.append(f'Non-vi modified {rel} {o.get("id")}')
            vi=n.get('vi')
            if isinstance(vi,str) and vi:translated+=1
            if o.get('vi')==vi:continue
            if o.get('vi') not in (None,''):errors.append(f'Previous VI overwritten {rel} {o.get("id")}')
            if not isinstance(vi,str) or not vi:errors.append(f'Empty VI {rel} {o.get("id")}');continue
            if TOK.findall(o['en'])!=TOK.findall(vi):errors.append(f'Tokens {rel} {o.get("id")}')
            if vi!=unicodedata.normalize('NFC',vi):errors.append(f'Unicode NFC {rel} {o.get("id")}')
            if any(c in vi for c in '\n\r\t'):errors.append(f'Illegal whitespace {rel} {o.get("id")}')
            if vi.count('▼')>3:errors.append(f'Excess page breaks {rel} {o.get("id")}')
            if any(len(TOK.sub('',part))>34 for part in vi.split('▼')):errors.append(f'Long line {rel} {o.get("id")}')
            cap=n.get('max_utf8_bytes')
            if cap and len(vi.encode('utf8'))>cap:errors.append(f'Byte budget {rel} {o.get("id")}')
            counts[rel]+=1
            changes.append({'file':rel.removeprefix('translation/'),'id':n['id'],'en':o['en'],'old_vi':o.get('vi'),'vi':vi,'ctx':n.get('ctx')})
if records!=55976:errors.append(f'Total records {records} != 55976')
if translated!=8969:errors.append(f'Translated {translated} != 8768')
if len(changes)!=201:errors.append(f'Delta {len(changes)} != 240')
if dict(counts)!=EXPECTED:errors.append(f'Changed files {dict(counts)} != {EXPECTED}')
if errors:
    print(f'FAIL: {len(errors)} errors');print('\n'.join(errors[:70]));sys.exit(1)
(ROOT/'DELTA-028.jsonl').write_text(''.join(json.dumps(v,ensure_ascii=False,separators=(',',':'))+'\n' for v in changes),'utf8')
(ROOT/'QA-028.md').write_text(f'''# QA — Magician’s Quest Checkpoint 028

- **Baseline:** `MagiciansQuest-VietHoa-Checkpoint-027.zip`.
- **PASS — 0 lỗi dữ liệu:** toàn bộ {len(names)} tệp JSONL, {records:,} bản ghi được đối chiếu với baseline.
- **201 mục `vi` mới**: `0027.004` (120) và `0027.005` (81), không ghi đè bản dịch cũ.
- **Tổng:** {translated:,}/{records:,} = {translated/records*100:.2f}% • Hội thoại NPC: 5.844/52.608.
- Trường khác `vi` bất biến; bảo toàn ID, thứ tự, English gốc, `ctx`, mã điều khiển và biến tên, Unicode NFC.
- Không CR/LF/tab trong `vi`; tối đa 3 dấu `▼` và 34 ký tự không tính mã kỹ thuật mỗi dòng; giữ giới hạn byte nếu có.
- `DELTA-028.jsonl` lưu đầy đủ câu gốc, bản mới và ID. Các bản dịch tay: `vi_0027_004.txt`, `vi_0027_005.txt`.
- **Chưa kiểm thử ROM NDS / độ rộng pixel thật**; QA này chỉ bao gồm dữ liệu và ngưỡng ký tự.
''','utf8')
print('PASS',len(names),'JSONL;',records,'records;',translated,'translated;',len(changes),'new; files:',dict(counts))