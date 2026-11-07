#!/usr/bin/env python3
"""Full delta QA: compare checkpoint 036 against user-supplied checkpoint 035."""
from pathlib import Path
from collections import Counter
import json, re, unicodedata, zipfile, sys
ROOT = Path(__file__).resolve().parent
BASE = ROOT.parent.parent/'MagiciansQuest-VietHoa-Checkpoint-035.zip'
ZIP_PREFIX = 'MagiciansQuest_035/'
TOK = re.compile(r"\$\d+(?:'[-\d]+)*;")
TARGETS = {
 'translation/04-thoai/talkfigs__0eng__data__0030.005.jsonl': 120,
 'translation/04-thoai/talkfigs__0eng__data__0031.001.jsonl': 120,
}
problems,changes,counts=[],[],Counter()
original_count=translated_count=0
with zipfile.ZipFile(BASE) as z:
    names=sorted(x for x in z.namelist() if x.startswith(ZIP_PREFIX+'translation/') and x.endswith('.jsonl'))
    if len(names)!=501: problems.append(f'Expected 501 JSONL, found {len(names)}')
    for full in names:
        rel = full[len(ZIP_PREFIX):]
        before = [json.loads(s) for s in z.read(full).decode('utf-8').splitlines()]
        path = ROOT/rel
        if not path.exists():
            problems.append(f'Missing file {rel}')
            continue
        after = [json.loads(s) for s in path.read_text('utf-8').splitlines()]
        if len(before)!=len(after):
            problems.append(f'Row count mismatch {rel}')
            continue
        for i,(old,new) in enumerate(zip(before,after),1):
            original_count+=1
            if old.keys()!=new.keys():problems.append(f'Key change {rel}:{i}')
            for key in set(old)|set(new):
                if key!='vi' and old.get(key)!=new.get(key):
                    problems.append(f'Non-vi field change: {rel}:{i}:{key}')
            vi=new.get('vi')
            if isinstance(vi,str) and vi:translated_count+=1
            if old.get('vi')==vi:continue
            if old.get('vi') not in [None,'']:
                problems.append(f'Overwrote previous VI: {rel}:{i}');continue
            if not isinstance(vi,str) or not vi:
                problems.append(f'Empty new VI: {rel}:{i}');continue
            if TOK.findall(old['en']) != TOK.findall(vi):problems.append(f'Lost control token: {rel}:{i}')
            if vi!=unicodedata.normalize('NFC',vi):problems.append(f'Not NFC: {rel}:{i}')
            if any(c in vi for c in '\r\n\t'):problems.append(f'Illegal whitespace: {rel}:{i}')
            if vi.count('▼')>3:problems.append(f'>3 linebreaks: {rel}:{i}')
            if max(len(TOK.sub('',part)) for part in vi.split('▼'))>34:problems.append(f'>34 chars: {rel}:{i}')
            cap=new.get('max_utf8_bytes')
            if cap and len(vi.encode('utf-8'))>cap:problems.append(f'UTF8 byte cap: {rel}:{i}')
            changes.append({'file':rel.removeprefix('translation/'),'id':new['id'],'en':old['en'],'old_vi':old.get('vi'),'vi':vi,'ctx':new.get('ctx')})
            counts[rel]+=1

if original_count!=55976:problems.append(f'Expected 55976 rows, got {original_count}')
if translated_count!=10808:problems.append(f'Expected 10808 translated, got {translated_count}')
if len(changes)!=240:problems.append(f'Expected 240 new, got {len(changes)}')
if dict(counts)!=TARGETS:problems.append(f'Unexpected changed files: {dict(counts)}')
if problems:
    print(f'FAIL {len(problems)} errors\n'+'\n'.join(problems[:70]));sys.exit(1)

(ROOT/'DELTA-036.jsonl').write_text(''.join(json.dumps(row,ensure_ascii=False,separators=(',',':'))+'\n' for row in changes),encoding='utf-8')
(ROOT/'QA-036.md').write_text(f'''# QA — Magician’s Quest, đợt 036

- **Baseline:** ZIP checkpoint 035 do người dùng cung cấp; so sánh từng tệp và từng trường JSONL.
- **PASS:** {len(names)} tệp JSONL / {original_count:,} mục; chỉ có {len(changes)} trường `vi` bổ sung tại hai tệp `0030.005` (120) và `0031.001` (120).
- **Tổng dịch:** {translated_count:,} / {original_count:,} = {translated_count/original_count*100:.2f}%; hội thoại NPC: 7.683/52.608.
- Không sửa hoặc ghi đè 10.568 mục cũ; giữ nguyên `id`, `en`, `ctx`, thứ tự, các trường kỹ thuật và mã lựa chọn/biểu cảm/biến.
- Mã `$...;` giống nguyên văn theo thứ tự; Unicode NFC; không CR/LF/tab; tối đa 3 dấu `▼`; chiều dài nhìn thấy mỗi dòng không quá 34 ký tự; giữ byte budget nếu có.
- **Chưa kiểm thử thực tế trong ROM NDS** hoặc đo bề rộng pixel bằng font thật; tên người chơi/NPC có thể dài hơn giới hạn ký tự trước khi thay biến.
''',encoding='utf-8')
print('PASS',len(names),'JSONL',original_count,'rows',translated_count,'translated',len(changes),'new',dict(counts))