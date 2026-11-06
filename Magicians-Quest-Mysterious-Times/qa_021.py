#!/usr/bin/env python3
"""Immutable source/diff audit of checkpoint 021 vs checkpoint 020 ZIP."""
from pathlib import Path
import json, collections, re, unicodedata, zipfile, sys
ROOT=Path(__file__).resolve().parent
BASE=ROOT.parent/'MagiciansQuest-VietHoa-Checkpoint-020.zip'
TOK=re.compile(r"\$\d+(?:'[-\d]+)*;")
EXPECTED={'translation/04-thoai/talkfigs__0eng__data__0024.005.jsonl':74,
          'translation/04-thoai/talkfigs__0eng__data__0025.001.jsonl':120}
errors=[];changes=[];counts=collections.Counter();total=0;filled=0
with zipfile.ZipFile(BASE) as z:
    names=sorted(n for n in z.namelist() if n.startswith('MagiciansQuest_020/translation/') and n.endswith('.jsonl'))
    if len(names)!=501:errors.append(f'Expected 501 JSONL files, got {len(names)}')
    for name in names:
        rel=name.split('/',1)[1]
        old=[json.loads(line) for line in z.read(name).decode('utf8').splitlines()]
        path=ROOT/rel
        if not path.exists():errors.append('Missing '+rel);continue
        new=[json.loads(line) for line in path.read_text('utf8').splitlines()]
        if len(old)!=len(new):errors.append('Count '+rel);continue
        for o,n in zip(old,new):
            total+=1
            if set(o)!=set(n):errors.append('Fields '+rel)
            for key in set(o)|set(n):
                if key!='vi' and o.get(key)!=n.get(key):errors.append(f'Metadata {key} {rel} {o.get("id")}')
            vi=n.get('vi')
            if vi not in (None,''):filled+=1
            if o.get('vi')==vi:continue
            if o.get('vi') not in (None,''):errors.append(f'Overwrite {rel} {o.get("id")}')
            if not isinstance(vi,str) or not vi:errors.append('Blank '+rel);continue
            if TOK.findall(o['en'])!=TOK.findall(vi):errors.append(f'Controls {rel} {o.get("id")}')
            if vi!=unicodedata.normalize('NFC',vi):errors.append(f'NFC {rel} {o.get("id")}')
            if any(x in vi for x in '\n\r\t'):errors.append(f'Whitespace {rel} {o.get("id")}')
            if vi.count('▼')>3:errors.append(f'Too many breaks {rel} {o.get("id")}')
            if any(len(TOK.sub('',s))>34 for s in vi.split('▼')):errors.append(f'Long line {rel} {o.get("id")}')
            cap=n.get('max_utf8_bytes')
            if cap and len(vi.encode('utf8'))>cap:errors.append(f'Cap {rel} {o.get("id")}')
            counts[rel]+=1
            changes.append({'file':rel.removeprefix('translation/'),'id':n['id'],'en':o['en'],'old_vi':o.get('vi'),'vi':vi,'ctx':n.get('ctx')})
if total!=55976:errors.append(f'Total {total}')
if filled!=7385:errors.append(f'Filled {filled}')
if len(changes)!=194:errors.append(f'Changed {len(changes)}')
if dict(counts)!=EXPECTED:errors.append(f'Unexpected changed files {dict(counts)}')
if errors:
    print('FAIL',len(errors),'errors');print('\n'.join(errors[:100]));sys.exit(1)
(ROOT/'DELTA-021.jsonl').write_text(''.join(json.dumps(row,ensure_ascii=False,separators=(',',':'))+'\n' for row in changes),'utf8')
(ROOT/'QA-021.md').write_text(f"""# QA — Magician’s Quest Checkpoint 021

- **Baseline:** `MagiciansQuest-VietHoa-Checkpoint-020.zip`.
- **PASS — 0 lỗi cấu trúc:** đối chiếu {len(names)} tệp JSONL, {total:,} bản ghi, không xóa/đảo hàng.
- Đợt 021: **194 mục `vi` mới** — `0024.005` (74) + `0025.001` (120).
- Tổng đã dịch: **{filled:,}/{total:,} = {filled/total*100:.2f}%**; hội thoại NPC **4.260/52.608**.
- Kiểm tra: trường ngoài `vi` bất biến, không ghi đè bản dịch cũ, mã lệnh đúng thứ tự, Unicode NFC, không CR/LF/tab, tối đa 3 dấu `▼`, tối đa 34 ký tự thấy được/dòng, giới hạn byte nếu khai báo.
- Các biến tên `$500;` và `$515;`, mã màu địa điểm `$000'5;` và `$000'1;`, mã biểu cảm và lựa chọn được giữ nguyên.
- Bản dịch tay tại `vi_0024_005.txt` và `vi_0025_001.txt`. Chi tiết thay đổi tại `DELTA-021.jsonl`.
- **Chưa kiểm thử độ rộng glyph/pixel hoặc chạy ROM NDS thật**; đây là QA văn bản và cấu trúc.
""",'utf8')
print('PASS',len(names),'JSONL',total,'records',filled,'translated',len(changes),'new',dict(counts))