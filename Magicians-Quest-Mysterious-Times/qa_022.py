#!/usr/bin/env python3
"""Full field-level QA of checkpoint 022 against canonical checkpoint 021 ZIP."""
from pathlib import Path
import json,collections,re,unicodedata,zipfile,sys
ROOT=Path(__file__).resolve().parent
BASE=ROOT.parent/'MagiciansQuest-VietHoa-Checkpoint-021.zip'
TOK=re.compile(r"\$\d+(?:'[-\d]+)*;")
EXPECTED={f'translation/04-thoai/talkfigs__0eng__data__{s}.jsonl':120 for s in ('0025.002','0025.003')}
errors=[];changes=[];counts=collections.Counter();records=translated=0
with zipfile.ZipFile(BASE) as z:
    zip_prefix='MagiciansQuest_021/translation/'
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
if translated!=7625:errors.append(f'Translated {translated} != 7625')
if len(changes)!=240:errors.append(f'Delta {len(changes)} != 240')
if dict(counts)!=EXPECTED:errors.append(f'Changed files {dict(counts)} != {EXPECTED}')
if errors:
    print(f'FAIL: {len(errors)} errors');print('\n'.join(errors[:70]));sys.exit(1)
(ROOT/'DELTA-022.jsonl').write_text(''.join(json.dumps(v,ensure_ascii=False,separators=(',',':'))+'\n' for v in changes),'utf8')
(ROOT/'QA-022.md').write_text(f'''# QA — Magician’s Quest Checkpoint 022

- **Baseline:** `MagiciansQuest-VietHoa-Checkpoint-021.zip`.
- **PASS — 0 lỗi dữ liệu:** toàn bộ {len(names)} tệp JSONL, {records:,} bản ghi được đối chiếu với baseline.
- **240 mục `vi` mới**: `0025.002` (120) và `0025.003` (120), không ghi đè bản dịch cũ.
- **Tổng:** {translated:,}/{records:,} = {translated/records*100:.2f}% • Hội thoại NPC: 4.500/52.608.
- Trường khác `vi` bất biến; bảo toàn ID, thứ tự, English gốc, `ctx`, mã điều khiển và biến tên, Unicode NFC.
- Không CR/LF/tab trong `vi`; tối đa 3 dấu `▼` và 34 ký tự không tính mã kỹ thuật mỗi dòng; giữ giới hạn byte nếu có.
- `DELTA-022.jsonl` lưu đầy đủ câu gốc, bản mới và ID. Các bản dịch tay: `vi_0025_002.txt`, `vi_0025_003.txt`.
- **Chưa kiểm thử ROM NDS / độ rộng pixel thật**; QA này chỉ bao gồm dữ liệu và ngưỡng ký tự.
''','utf8')
print('PASS',len(names),'JSONL;',records,'records;',translated,'translated;',len(changes),'new; files:',dict(counts))