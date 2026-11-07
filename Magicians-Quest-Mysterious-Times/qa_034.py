#!/usr/bin/env python3
"""Full field-level QA of checkpoint 034 against immutable checkpoint 033 ZIP."""
from pathlib import Path
import json, collections, re, unicodedata, zipfile, sys
ROOT=Path(__file__).resolve().parent
BASE=ROOT.parent.parent/'MagiciansQuest-VietHoa-Checkpoint-033.zip'
TOK=re.compile(r"\$\d+(?:'[-\d]+)*;")
EXPECTED={
 'translation/04-thoai/talkfigs__0eng__data__0030.001.jsonl':120,
 'translation/04-thoai/talkfigs__0eng__data__0030.002.jsonl':120,
}
issues=[];delta=[];counts=collections.Counter();records=old_done=done=0
with zipfile.ZipFile(BASE) as z:
    prefix='MagiciansQuest_033/'
    names=sorted(n for n in z.namelist() if n.startswith(prefix+'translation/') and n.endswith('.jsonl'))
    if len(names)!=501:issues.append(f'Wrong file count {len(names)} (expected 501)')
    for name in names:
        rel=name[len(prefix):]
        old=[json.loads(s) for s in z.read(name).decode('utf8').splitlines()]
        target=ROOT/rel
        if not target.is_file():issues.append(f'Missing {rel}');continue
        new=[json.loads(s) for s in target.read_text('utf8').splitlines()]
        if len(old)!=len(new):issues.append(f'Length changed {rel}');continue
        for a,b in zip(old,new):
            records+=1
            old_done+=bool(a.get('vi'));done+=bool(b.get('vi'))
            if list(a)!=list(b):issues.append(f'Fields order changed {rel} {a.get("id")}')
            if any(a.get(k)!=b.get(k) for k in set(a)|set(b) if k!='vi'):
                issues.append(f'Original source changed {rel} {a.get("id")}')
            if a.get('vi')==b.get('vi'):continue
            if a.get('vi') not in (None,''):issues.append(f'Previous VI overwritten {rel} {a.get("id")}')
            vi=b.get('vi')
            if not isinstance(vi,str) or not vi:issues.append(f'Missing VI {rel} {a.get("id")}');continue
            if TOK.findall(a['en'])!=TOK.findall(vi):issues.append(f'Token mismatch {rel} {a.get("id")}')
            if vi!=unicodedata.normalize('NFC',vi):issues.append(f'NFC mismatch {rel} {a.get("id")}')
            if any(c in vi for c in '\r\n\t'):issues.append(f'Illegal whitespace {rel} {a.get("id")}')
            if vi.count('▼')>3:issues.append(f'Page breaks {rel} {a.get("id")}')
            if any(len(TOK.sub('',part))>34 for part in vi.split('▼')):issues.append(f'Line too long {rel} {a.get("id")}')
            limit=b.get('max_utf8_bytes')
            if limit and len(vi.encode('utf8'))>limit:issues.append(f'Exceeded byte cap {rel} {a.get("id")}')
            counts[rel]+=1
            delta.append({'file':rel.removeprefix('translation/'),'id':b['id'],'en':a['en'],'old_vi':a.get('vi'),'vi':vi,'ctx':b.get('ctx')})
if records!=55976:issues.append(f'Total records {records} != 55976')
if old_done!=10088:issues.append(f'Baseline translated {old_done} != 10088')
if done!=10328:issues.append(f'New translated {done} != 10328')
if len(delta)!=240:issues.append(f'Changed record count {len(delta)} != 240')
if dict(counts)!=EXPECTED:issues.append(f'Expected only two translated files: {dict(counts)} != {EXPECTED}')
if issues:
 print(f'FAIL {len(issues)} QA errors');print('\n'.join(issues[:100]));sys.exit(1)
(ROOT/'DELTA-034.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n' for x in delta),'utf8')
(ROOT/'QA-034.md').write_text(f'''# QA — Magician’s Quest · Đợt 034

- **PASS:** đối chiếu toàn bộ {len(names)} tệp JSONL / {records:,} bản ghi với checkpoint 033 (ZIP nguồn của người dùng).
- **240 mục `vi` mới:** `0030.001` (120) và `0030.002` (120).
- **Tổng:** {done:,}/{records:,} = {done/records*100:.2f}%; hội thoại NPC: 7.203/52.608.
- **Bất biến:** giữ nguyên {old_done:,} bản dịch cũ; `id`, `en`, `ctx`, các trường cấu trúc và thứ tự bản ghi đều không đổi.
- **0 lỗi QA trong lô mới:** mã điều khiển `$...;` giữ đúng danh sách/thứ tự, Unicode NFC, không chứa CR/LF/tab, tối đa 3 ngắt `▼`, mỗi dòng tối đa 34 ký tự nhìn thấy, byte cap đạt khi có.
- **Chưa kiểm thử trực tiếp trên ROM NDS và chưa đo độ rộng pixel bằng font thực.** Tên thay thế từ `$500;`, `$515;` có thể dài hơn dự kiến.
''','utf8')
print('PASS',len(names),'JSONL,',records,'total entries,',done,'translated,',len(delta),'new;',dict(counts))