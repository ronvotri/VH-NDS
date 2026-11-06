#!/usr/bin/env python3
"""Diff/check checkpoint 012 against immutable full checkpoint 011."""
import collections,json,pathlib,zipfile,re,unicodedata,sys
ROOT=pathlib.Path(__file__).resolve().parent
BASE=pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else ROOT.parent/'MagiciansQuest-VietHoa-Checkpoint-011.zip'
TOKEN=re.compile(r"\$\d+(?:'[-\d]+)*;")
counts=collections.Counter(); changed=[]; issues=[]; total=filled=files=0; corrections=[]
with zipfile.ZipFile(BASE) as z:
 oldfiles=sorted(n for n in z.namelist() if n.startswith('MagiciansQuest_011/translation/') and n.endswith('.jsonl'))
 if len(oldfiles)!=501:issues.append(f'expected 501 jsonl, found {len(oldfiles)}')
 for n in oldfiles:
  rel=n.split('/',1)[1]
  newfile=ROOT/rel
  if not newfile.exists():issues.append(f'Missing {rel}');continue
  older=[json.loads(l) for l in z.read(n).decode('utf8').splitlines()]
  newer=[json.loads(l) for l in newfile.read_text(encoding='utf8').splitlines()]
  files+=1
  if len(older)!=len(newer): issues.append('Row count changed '+rel);continue
  for a,b in zip(older,newer):
   total+=1
   if a['id']!=b['id']:issues.append('ID changed '+rel);continue
   for k in set(a)|set(b):
    if k!='vi' and a.get(k)!=b.get(k):issues.append('Non-vi changed '+b['id']+': '+k)
   if b.get('vi') not in (None,''):filled+=1
   if a.get('vi')==b.get('vi'):continue
   old,vi=a.get('vi'),b.get('vi')
   if not vi:issues.append('Blanked translation '+b['id']);continue
   if old not in (None,'') and old.replace('The Emporium','Bách Hóa Tổng Hợp')!=vi:
    issues.append('Unapproved overwrite '+b['id'])
   if old not in (None,''):corrections.append(b['id'])
   if TOKEN.findall(b['en'])!=TOKEN.findall(vi):issues.append('Mismatched control tokens '+b['id'])
   if unicodedata.normalize('NFC',vi)!=vi:issues.append('Non NFC '+b['id'])
   if any(x in vi for x in '\r\n\t'):issues.append('CR/LF/TAB introduced '+b['id'])
   if vi.count('▼')>3:issues.append('Too many ▼ '+b['id'])
   if any(len(TOKEN.sub('',x))>34 for x in vi.split('▼')):
    issues.append('More than 34 chars/line '+b['id'])
   if b.get('max_utf8_bytes') is not None and len(vi.encode('utf8'))>b['max_utf8_bytes']:
    issues.append('UTF-8 byte length over '+b['id'])
   if b.get('max_utf8_bytes') is None and len(vi.encode('utf8'))>1000:
    issues.append('Unexpected large field '+b['id'])
   counts[rel]+=1
   changed.append({'file':rel.removeprefix('translation/'),'id':b['id'],'en':b['en'],'old_vi':old,'vi':vi,'ctx':b.get('ctx')})
expected={
 'translation/04-thoai/talkfigs__0eng__data__0021.002.jsonl':120,
 'translation/04-thoai/talkfigs__0eng__data__0021.003.jsonl':120,
 'translation/04-thoai/talkfigs__0eng__data__0012.001.jsonl':4,
 'translation/04-thoai/talkfigs__0eng__data__0021.001.jsonl':1,
 'translation/01-he-thong/picstat__magic__msg_e.dat.002.jsonl':1,
}
# The path of 0012/0021 is dialogue, verify exactly. Names are also validated by total count.
if total!=55976:issues.append(f'Row total incorrect {total}')
if filled!=5377:issues.append(f'Filled total expected 5377, got {filled}')
if len(changed)!=246:issues.append(f'Changed count expected 246, got {len(changed)}')
if len(corrections)!=6:issues.append(f'Corrections expected 6, got {len(corrections)}')
if dict(counts)!=expected:issues.append('Changed files not expected '+str(dict(counts)))
if issues:
 print('FAIL '+str(len(issues))+' issues:\n'+'\n'.join(issues[:100]));sys.exit(1)
(ROOT/'DELTA-012.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n' for x in changed),encoding='utf8')
(ROOT/'QA-012.md').write_text(f'''# QA — Checkpoint 012 · Magician’s Quest (NDS)

- **Nguồn đối chiếu:** Checkpoint 011 (được đóng gói đầy đủ), 5.137/55.976 mục `vi`.
- **Mốc mới:** **{filled}/55.976 mục** (+240 trang thoại mới +6 điều chỉnh cách gọi tên cửa hàng).
- **Quy mô rà:** {files} tệp JSONL, {total} bản ghi, đủ ID và thứ tự gốc.
- **Delta:** {len(changed)} thay đổi **chỉ trong `vi`**, trong đó {len(corrections)} thay tên cửa hàng có chủ đích; mọi bản dịch cũ khác được bảo vệ.
- **Kiểm tra:** 0 thay đổi `id`, `en`, `ctx`, metadata; 0 sai chuỗi mã `$...;`, 0 lỗi NFC/CR/LF/TAB; 0 trang vượt 3 dấu ▼, 0 dòng quá 34 ký tự sau khi bỏ mã, 0 lỗi giới hạn UTF-8 nếu có khai báo.
- **Đã dịch:** `0021.002` (120) và `0021.003` (120).
- **Thống nhất tên:** `The Emporium` → `Bách Hóa Tổng Hợp` thêm 6 vị trí, khớp thuật ngữ đã có tại `0999.006`.
- **Còn chờ:** chạy vá bản ROM sạch, đo rộng pixel 9×16 bằng font tiếng Việt thực tế, kiểm thử tốc độ thoại và ngắt trang trong giả lập/NDS. QA cấu trúc không thay thế được QA hình ảnh.
''',encoding='utf8')
print(f'PASS — {files} files, {total} rows, {filled} filled, {len(changed)} changes, {len(corrections)} corrections, 0 errors')