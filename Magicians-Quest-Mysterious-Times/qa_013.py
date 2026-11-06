#!/usr/bin/env python3
"""Validate batch 013 against immutable batch 012, produce patch delta and report."""
import json,re,unicodedata,collections,zipfile,pathlib,sys
ROOT=pathlib.Path(__file__).resolve().parent
BASE=ROOT.parent/'MagiciansQuest-VietHoa-Checkpoint-012.zip'
TOKEN=re.compile(r"\$\d+(?:'[-\d]+)*;")
expected={
 'translation/04-thoai/talkfigs__0eng__data__0021.004.jsonl':120,
 'translation/04-thoai/talkfigs__0eng__data__0021.005.jsonl':68,
}
problems=[];total=filled=0;count=collections.Counter();changes=[];unchanged_filled=0
with zipfile.ZipFile(BASE) as zin:
    files=sorted(n for n in zin.namelist() if n.startswith('MagiciansQuest_012/translation/') and n.endswith('.jsonl'))
    if len(files)!=501:problems.append(f'501 JSONL expected, got {len(files)}')
    for member in files:
        rel=member.split('/',1)[1]
        orig=[json.loads(line) for line in zin.read(member).decode('utf8').splitlines()]
        path=ROOT/rel
        if not path.is_file():problems.append('Missing '+rel);continue
        new=[json.loads(line) for line in path.read_text(encoding='utf-8').splitlines()]
        if len(orig)!=len(new):problems.append('Row count changed '+rel);continue
        for before,after in zip(orig,new):
            total+=1
            if before['id']!=after['id']:problems.append('ID changed '+rel);continue
            for k in set(before)|set(after):
                if k!='vi' and before.get(k)!=after.get(k):problems.append(f'Changed {k}: {rel} {before["id"]}')
            vi=after.get('vi')
            if vi not in (None,''):filled+=1
            old=before.get('vi')
            if vi==old:continue
            if old not in ('',None):problems.append('Overwrite '+rel+' '+before['id'])
            if vi in ('',None):problems.append('Blank new text '+rel+' '+before['id']);continue
            if TOKEN.findall(before['en'])!=TOKEN.findall(vi):problems.append('Token mismatch '+rel+' '+before['id'])
            if unicodedata.normalize('NFC',vi)!=vi:problems.append('Not NFC '+rel+' '+before['id'])
            if any(ch in vi for ch in '\t\n\r'):problems.append('Literal whitespace '+rel+' '+before['id'])
            if vi.count('▼')>3:problems.append('Too many visual breaks '+rel+' '+before['id'])
            if any(len(TOKEN.sub('',a))>34 for a in vi.split('▼')):problems.append('Long visual line '+rel+' '+before['id'])
            if after.get('max_utf8_bytes') is not None and len(vi.encode())>after['max_utf8_bytes']:
                problems.append('Byte limit '+rel+' '+before['id'])
            count[rel]+=1
            changes.append({'file':rel.removeprefix('translation/'),'id':after['id'],'en':after['en'],'old_vi':old,'vi':vi,'ctx':after.get('ctx')})
if total!=55976:problems.append(f'Wrong total {total}')
if filled!=5565:problems.append(f'Wrong filled total {filled}')
if len(changes)!=188:problems.append(f'Wrong changes {len(changes)}')
if dict(count)!=expected:problems.append(f'Wrong changed files {dict(count)}')
if problems:
 print('FAIL',len(problems),'\n'+'\n'.join(problems[:100]));sys.exit(1)
(ROOT/'DELTA-013.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n' for x in changes),encoding='utf-8')
(ROOT/'QA-013.md').write_text(f'''# QA — Checkpoint 013 · Magician’s Quest (NDS)

- Nguồn bất biến: `MagiciansQuest-VietHoa-Checkpoint-012.zip`.
- Tổng: **{total:,}** hàng trong **{len(files)}** tệp JSONL; **{filled:,}** mục đã điền `vi` (trước đợt là 5.377).
- Đã dịch thêm: **188** trang, `0021.004` (120) và `0021.005` (68). Không ghi đè câu đã dịch.
- Thay đổi: **{len(changes)}** bản ghi, chỉ trong `vi`, lưu tại `DELTA-013.jsonl`.
- Kiểm tra: **0 lỗi** ID/EN/ctx/metadata, mã `$...;`, NFC, CR/LF/TAB, số dấu `▼`, giới hạn 34 ký tự nhìn thấy mỗi dòng và `max_utf8_bytes` nếu có.
- Tên địa danh: **Điểm Hẹn Hò** (Lovers Point), đúng thẻ màu `$000'5;...$000'1;`.
- Chưa kiểm thử trong ROM/giả lập; ngưỡng 34 ký tự không bảo đảm vừa giới hạn độ rộng pixel thực của font Việt (khoảng 160 px).
''',encoding='utf-8')
print('PASS:',len(files),'files',total,'rows',filled,'filled',len(changes),'new changes; 0 errors')