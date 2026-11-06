#!/usr/bin/env python3
"""Checkpoint 017 full immutable diff against checkpoint 016 ZIP."""
from pathlib import Path
import zipfile,json,collections,re,unicodedata,sys
ROOT=Path(__file__).resolve().parent
BASE=ROOT.parent/'MagiciansQuest-VietHoa-Checkpoint-016.zip'
TOKEN=re.compile(r"\$\d+(?:'[-\d]+)*;")
EXPECTED={'translation/04-thoai/talkfigs__0eng__data__0023.002.jsonl':120,
          'translation/04-thoai/talkfigs__0eng__data__0023.003.jsonl':120}
errors=[];changes=[];counter=collections.Counter();total=filled=0
with zipfile.ZipFile(BASE) as z:
    names=sorted(n for n in z.namelist() if n.startswith('MagiciansQuest_016/translation/') and n.endswith('.jsonl'))
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
            if o.get('vi') not in ('',None):errors.append(f'Overwrite {rel} {o.get("id")}')
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
if filled!=6525:errors.append(f'Filled {filled}')
if len(changes)!=240:errors.append(f'Changed {len(changes)}')
if dict(counter)!=EXPECTED:errors.append(f'Unexpected changed files {dict(counter)}')
if errors:
    print('FAIL',len(errors),'errors')
    print('\n'.join(errors[:120]))
    sys.exit(1)
(ROOT/'DELTA-017.jsonl').write_text(''.join(json.dumps(row,ensure_ascii=False,separators=(',',':'))+'\n' for row in changes),'utf8')
(ROOT/'QA-017.md').write_text(f'''# QA — Magician’s Quest Checkpoint 017

- Baseline bất biến: `MagiciansQuest-VietHoa-Checkpoint-016.zip`.
- Đối chiếu **{len(names)} tệp JSONL**, **{total:,} bản ghi**.
- **240 trang mới**: `0023.002` (120), `0023.003` (120).
- **{filled:,} / {total:,}** trường `vi` đã điền, trong đó hội thoại **3.400 / 52.608**.
- **PASS — 0 lỗi**: không thay ID, tiếng Anh gốc, metadata, số dòng, không ghi đè bản dịch cũ, trật tự mã điều khiển, Unicode NFC, xuống dòng, ngưỡng 34 ký tự/dòng.
- Giữ biến `$500;`, `$503'318;`, thẻ màu `$000'3;`/`$000'1;` và mã biểu cảm `$024`, `$023`, `$022`.
- Chi tiết delta gồm **240 bản ghi** tại `DELTA-017.jsonl`.
- **Chưa kiểm thử trực tiếp trên ROM NDS hoặc kiểm tra độ rộng glyph bằng font thật**; ngưỡng 34 ký tự là kiểm tra sơ bộ, chưa đảm bảo không tràn khung.
''','utf8')
print('PASS',len(names),'JSONL',total,'rows',filled,'translated',len(changes),'new',dict(counter))