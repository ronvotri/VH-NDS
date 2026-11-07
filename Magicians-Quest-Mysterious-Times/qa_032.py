#!/usr/bin/env python3
"""Compare Magician's Quest checkpoint 032 against immutable checkpoint 031 ZIP."""
from pathlib import Path
import collections,json,re,unicodedata,zipfile,sys
ROOT=Path(__file__).resolve().parent
BASE=ROOT.parent.parent/'MagiciansQuest-VietHoa-Checkpoint-031.zip'
TOK=re.compile(r"\$\d+(?:'[-\d]+)*;")
EXPECTED={
 'translation/04-thoai/talkfigs__0eng__data__0029.002.jsonl':120,
 'translation/04-thoai/talkfigs__0eng__data__0029.003.jsonl':120
}
errors=[];changes=[];changed=collections.Counter();records=translated=oldtranslated=0
with zipfile.ZipFile(BASE) as z:
    prefix='MagiciansQuest_031/'
    names=sorted(n for n in z.namelist() if n.startswith(prefix+'translation/') and n.endswith('.jsonl'))
    if len(names)!=501: errors.append(f'JSONL files {len(names)} != 501')
    for name in names:
        rel=name[len(prefix):]
        old=[json.loads(s) for s in z.read(name).decode('utf8').splitlines()]
        path=ROOT/rel
        if not path.exists(): errors.append(f'Missing file {rel}'); continue
        new=[json.loads(s) for s in path.read_text('utf8').splitlines()]
        if len(old)!=len(new): errors.append(f'Row count changed {rel}');continue
        for o,n in zip(old,new):
            records+=1
            oldtranslated+=bool(o.get('vi'))
            translated+=bool(n.get('vi'))
            if list(o)!=list(n): errors.append(f'Field order changed {rel} {o.get("id")}')
            if any(o.get(k)!=n.get(k) for k in set(o)|set(n) if k!='vi'):
                errors.append(f'Original content changed {rel} {o.get("id")}')
            if o.get('vi')==n.get('vi'):continue
            if o.get('vi') not in (None,''): errors.append(f'Previous VI overwritten {rel} {o.get("id")}')
            vi=n.get('vi')
            if not isinstance(vi,str) or not vi: errors.append(f'Empty newly translated VI {rel} {o.get("id")}');continue
            if TOK.findall(o['en'])!=TOK.findall(vi): errors.append(f'Token order mismatch {rel} {o.get("id")}')
            if vi!=unicodedata.normalize('NFC',vi): errors.append(f'Non-NFC {rel} {o.get("id")}')
            if any(c in vi for c in '\n\r\t'): errors.append(f'Invalid newline/tab {rel} {o.get("id")}')
            if vi.count('▼')>3: errors.append(f'Too many lines {rel} {o.get("id")}')
            if any(len(TOK.sub('',part))>34 for part in vi.split('▼')): errors.append(f'Too wide (char limit) {rel} {o.get("id")}')
            cap=n.get('max_utf8_bytes')
            if cap and len(vi.encode('utf8'))>cap: errors.append(f'Byte cap {rel} {o.get("id")}')
            changed[rel]+=1
            changes.append({'file':rel.removeprefix('translation/'),'id':n['id'],'en':o['en'],'old_vi':o.get('vi'),'vi':vi,'ctx':n.get('ctx')})
if records!=55976: errors.append(f'Records {records} != 55976')
if oldtranslated!=9660:errors.append(f'Baseline translated {oldtranslated} != 9660')
if translated!=9900:errors.append(f'Translated {translated} != 9900')
if len(changes)!=240:errors.append(f'Delta {len(changes)} != 240')
if dict(changed)!=EXPECTED:errors.append(f'Changed files {dict(changed)} != {EXPECTED}')
if errors:
 print('FAIL',len(errors));print('\n'.join(errors[:100]));sys.exit(1)
(ROOT/'DELTA-032.jsonl').write_text(''.join(json.dumps(o,ensure_ascii=False,separators=(',',':'))+'\n' for o in changes),'utf8')
(ROOT/'QA-032.md').write_text(f'''# QA — Magician’s Quest · Đợt 032

- **PASS:** đối chiếu đủ {len(names)} tệp JSONL / {records:,} bản ghi với ZIP checkpoint 031.
- **240 mục `vi` mới:** `0029.002` (120), `0029.003` (120).
- **Tổng:** {translated:,}/{records:,} = {translated/records*100:.2f}%; hội thoại NPC: 6.775/52.608.
- **Bất biến:** giữ nguyên {oldtranslated:,} trường `vi` cũ; giữ `id`, `en`, `ctx`, các trường kỹ thuật, thứ tự tệp và bản ghi.
- **0 lỗi kỹ thuật** trong lô mới: mã `$...;` đúng thứ tự và giá trị, NFC, không CR/LF/tab, mỗi trang tối đa 3 dấu `▼`, từng dòng tối đa 34 ký tự nhìn thấy; byte cap đạt khi có.
- **Chưa kiểm thử ROM NDS hoặc đo độ rộng pixel bằng font trong game.** Cần kiểm tra tên biến động dài và bố cục thoại thực tế.
''','utf8')
print('PASS',len(names),'JSONL',records,'records',oldtranslated,'baseline translated',translated,'now translated',len(changes),'new',dict(changed))