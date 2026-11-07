#!/usr/bin/env python3
"""QA checkpoint 031; compare every JSONL row with checkpoint 030 ZIP."""
from pathlib import Path
import collections,json,re,zipfile,unicodedata,sys
ROOT=Path(__file__).resolve().parent
BASE=next((p for p in [ROOT.parent/'MagiciansQuest-VietHoa-Checkpoint-030.zip', ROOT.parent.parent/'MagiciansQuest-VietHoa-Checkpoint-030.zip', ROOT.parent.parent/'MagiciansQuest-VietHoa-Checkpoint-030(1).zip'] if p.exists()), ROOT.parent/'MagiciansQuest-VietHoa-Checkpoint-030.zip')
TOK=re.compile(r"\$\d+(?:'[-\d]+)*;")
EXPECTED={'translation/04-thoai/talkfigs__0eng__data__0028.005.jsonl':91,'translation/04-thoai/talkfigs__0eng__data__0029.001.jsonl':120}
issues=[];changes=[];counter=collections.Counter();records=translated=oldtranslated=0
with zipfile.ZipFile(BASE) as z:
    names=sorted(n for n in z.namelist() if n.startswith('MagiciansQuest_030/translation/') and n.endswith('.jsonl'))
    if len(names)!=501:issues.append(f'Unexpected JSONL count {len(names)}')
    for name in names:
        rel=name.split('MagiciansQuest_030/',1)[1]
        old=[json.loads(s) for s in z.read(name).decode('utf8').splitlines()]
        path=ROOT/rel
        if not path.is_file():issues.append(f'MISSING {rel}');continue
        new=[json.loads(s) for s in path.read_text('utf8').splitlines()]
        if len(old)!=len(new):issues.append(f'COUNT {rel}');continue
        for o,n in zip(old,new):
            records+=1
            oldtranslated+=isinstance(o.get('vi'),str) and bool(o['vi'])
            translated+=isinstance(n.get('vi'),str) and bool(n['vi'])
            if list(o)!=list(n):issues.append(f'KEYS {rel}:{o.get("id")}')
            if any(o.get(k)!=n.get(k) for k in set(o)|set(n) if k!='vi'):issues.append(f'MODIFIED_ORIGINAL {rel}:{o.get("id")}')
            vi=n.get('vi')
            if o.get('vi')==vi:continue
            if o.get('vi') not in (None,''):issues.append(f'OVERWRITE {rel}:{o.get("id")}')
            if not isinstance(vi,str) or not vi:issues.append(f'EMPTY_NEW {rel}:{o.get("id")}');continue
            if TOK.findall(o.get('en',''))!=TOK.findall(vi):issues.append(f'TOKENS {rel}:{o.get("id")}')
            if any(c in vi for c in '\r\n\t'):issues.append(f'WHITESPACE {rel}:{o.get("id")}')
            if vi!=unicodedata.normalize('NFC',vi):issues.append(f'NFC {rel}:{o.get("id")}')
            if vi.count('▼')>3:issues.append(f'BREAKS {rel}:{o.get("id")}')
            if any(len(TOK.sub('',s))>34 for s in vi.split('▼')):issues.append(f'WIDTH {rel}:{o.get("id")}')
            if n.get('max_utf8_bytes') and len(vi.encode('utf8'))>n['max_utf8_bytes']:issues.append(f'BYTES {rel}:{o.get("id")}')
            counter[rel]+=1
            changes.append({'file':rel.removeprefix('translation/'),'id':n['id'],'en':o['en'],'old_vi':o.get('vi'),'vi':vi,'ctx':n.get('ctx')})
if records!=55976:issues.append(f'RECORDS {records}')
if oldtranslated!=9449:issues.append(f'BASE_TRANSLATED {oldtranslated}')
if translated!=9660:issues.append(f'NEW_TRANSLATED {translated}')
if len(changes)!=211:issues.append(f'CHANGES {len(changes)}')
if dict(counter)!=EXPECTED:issues.append(f'FILES {dict(counter)}')
if issues:
 print('FAIL',len(issues));print('\n'.join(issues[:100]));sys.exit(1)
(ROOT/'DELTA-031.jsonl').write_text(''.join(json.dumps(v,ensure_ascii=False,separators=(',',':'))+'\n' for v in changes),encoding='utf8')
report=f'''# QA — Magician’s Quest · Đợt 031

- **Đạt:** đối chiếu {len(names)} tệp JSONL / {records:,} bản ghi với ZIP checkpoint 030 (được người dùng cung cấp trực tiếp).
- **211 mục `vi` mới:** `0028.005` (91), `0029.001` (120).
- **Tổng:** {translated:,}/{records:,} = {translated/records*100:.2f}%; hội thoại: 6.535/52.608.
- **Giữ nguyên:** {oldtranslated:,} mục dịch cũ, toàn bộ `id`, `en`, `ctx`, các trường kỹ thuật, thứ tự tệp và bản ghi.
- **0 lỗi dữ liệu:** mã `$...;` đúng thứ tự và giá trị, Unicode NFC, không có CR/LF/tab trong `vi`, tối đa 3 dấu ngắt `▼`, tối đa 34 ký tự nhìn thấy mỗi dòng, giữ byte limit khi có.
- **Giới hạn:** chưa thử ROM NDS hoặc đo rộng pixel bằng font trong game. Những biến tên như `$500;`, `$515;` có độ dài thay đổi sau khi hiện trên máy.
'''
(ROOT/'QA-031.md').write_text(report,encoding='utf8')
print(f'PASS {len(names)} JSONL {records} records baseline={oldtranslated} translated={translated} delta={len(changes)} counts={dict(counter)}')