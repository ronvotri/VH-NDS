#!/usr/bin/env python3
"""Full immutable diff: checkpoint 018 ZIP -> checkpoint 019 directory."""
from pathlib import Path
import zipfile,json,collections,re,unicodedata,sys
ROOT=Path(__file__).resolve().parent
BASE=ROOT.parent/'MagiciansQuest-VietHoa-Checkpoint-018.zip'
TOKEN=re.compile(r"\$\d+(?:'[-\d]+)*;")
EXPECTED={'translation/04-thoai/talkfigs__0eng__data__0024.001.jsonl':120,
          'translation/04-thoai/talkfigs__0eng__data__0024.002.jsonl':120}
errors=[];changes=[];counter=collections.Counter();total=filled=0
with zipfile.ZipFile(BASE) as z:
    names=sorted(n for n in z.namelist() if n.startswith('MagiciansQuest_018/translation/') and n.endswith('.jsonl'))
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
            for k in set(o)|set(n):
                if k!='vi' and o.get(k)!=n.get(k):errors.append(f'Metadata {k} {rel} {o.get("id")}')
            vi=n.get('vi')
            if vi not in (None,''):filled+=1
            if o.get('vi')==vi:continue
            if o.get('vi') not in (None,''):errors.append(f'Overwrite {rel} {o.get("id")}')
            if not isinstance(vi,str) or not vi:errors.append('Blank '+rel);continue
            if TOKEN.findall(o['en'])!=TOKEN.findall(vi):errors.append(f'Control {rel} {o.get("id")}')
            if vi!=unicodedata.normalize('NFC',vi):errors.append(f'NFC {rel} {o.get("id")}')
            if any(x in vi for x in '\n\r\t'):errors.append(f'Whitespace {rel} {o.get("id")}')
            if vi.count('▼')>3:errors.append(f'Too many breaks {rel} {o.get("id")}')
            if any(len(TOKEN.sub('',line))>34 for line in vi.split('▼')):errors.append(f'Long line {rel} {o.get("id")}')
            cap=n.get('max_utf8_bytes')
            if cap and len(vi.encode('utf8'))>cap:errors.append(f'Cap {rel} {o.get("id")}')
            counter[rel]+=1
            changes.append({'file':rel.removeprefix('translation/'),'id':n['id'],'en':o['en'],'old_vi':o.get('vi'),'vi':vi,'ctx':n.get('ctx')})
if total!=55976:errors.append(f'Total {total}')
if filled!=6951:errors.append(f'Filled {filled}')
if len(changes)!=240:errors.append(f'Changed {len(changes)}')
if dict(counter)!=EXPECTED:errors.append(f'Unexpected changed files {dict(counter)}')
if errors:
    print('FAIL',len(errors),'errors')
    print('\n'.join(errors[:120]))
    sys.exit(1)
(ROOT/'DELTA-019.jsonl').write_text(''.join(json.dumps(row,ensure_ascii=False,separators=(',',':'))+'\n' for row in changes),'utf8')
(ROOT/'QA-019.md').write_text(f'''# QA — Magician’s Quest Checkpoint 019

- **Baseline:** `MagiciansQuest-VietHoa-Checkpoint-018.zip`.
- **PASS — 0 lỗi:** đối chiếu {len(names)} tệp JSONL, {total:,} bản ghi, không xóa/đảo hàng.
- Đợt 019: **240 mục `vi` mới** — `0024.001` (120) + `0024.002` (120).
- Tổng đã dịch: **{filled:,}/{total:,} = {filled/total*100:.2f}%**; hội thoại NPC **3.826/52.608**.
- Kiểm tra: các trường ngoài `vi` bất biến, không ghi đè bản dịch cũ, mã lệnh đúng thứ tự, Unicode NFC, không có CR/LF/tab, tối đa 3 dấu `▼`, tối đa 34 ký tự thấy được/dòng, giới hạn byte nếu trường có khai báo.
- Giữ mã biểu cảm, các biến tên `$500;` và mọi mã điều khiển đúng thứ tự trong từng bản ghi.
- Bản đối chiếu đầy đủ nằm trong `DELTA-019.jsonl`.
- **Chưa QA độ rộng glyph/pixel hoặc test ROM NDS thật**; đây là QA văn bản và cấu trúc.
''','utf8')
print('PASS',len(names),'JSONL',total,'rows',filled,'translated',len(changes),'new',dict(counter))