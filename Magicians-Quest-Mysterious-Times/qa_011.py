#!/usr/bin/env python3
"""Verify translation-only delta against checkpoint 010 and report CP 011."""
import json, zipfile, re, unicodedata, pathlib, collections
ROOT=pathlib.Path(__file__).resolve().parent
PREV=pathlib.Path('/mnt/data/MagiciansQuest-VietHoa-Checkpoint-010.zip')
if not PREV.exists(): PREV=ROOT/'MagiciansQuest-VietHoa-Checkpoint-010.zip'
TOKEN=re.compile(r"\$\d+(?:'\d+)*;")
results=[]; problems=[]; counts=collections.Counter(); jsonl_count=0; total_rows=0; total_vi=0
with zipfile.ZipFile(PREV) as z:
 for fname in sorted(z.namelist()):
  if not (fname.startswith('MagiciansQuest_010/translation/') and fname.endswith('.jsonl')):continue
  jsonl_count+=1; rel=fname.removeprefix('MagiciansQuest_010/');newpath=ROOT/rel
  old_data=[json.loads(s) for s in z.read(fname).decode('utf8').splitlines()]
  new_data=[json.loads(s) for s in newpath.read_text(encoding='utf8').splitlines()]
  if len(old_data)!=len(new_data):problems.append('Row count changed '+rel); continue
  for a,b in zip(old_data,new_data):
   total_rows+=1
   if a.get('id')!=b.get('id'):problems.append('ID changed '+rel); continue
   if any(a.get(k)!=b.get(k) for k in set(a)|set(b) if k!='vi'):
    problems.append('Non-vi changed '+str(a['id']))
   if b.get('vi') not in (None,''):total_vi+=1
   if a.get('vi')!=b.get('vi'):
    if a.get('vi') not in ('',None):problems.append('Prior translation overwritten '+str(a['id']))
    if b.get('vi') in ('',None):problems.append('Translation blanked '+str(a['id']))
    if TOKEN.findall(b['en']) != TOKEN.findall(b['vi']):problems.append('Control tags changed '+str(a['id']))
    if b['vi'].count('▼')>3:problems.append('Too many display lines '+str(a['id']))
    if max(map(len,TOKEN.sub('',b['vi']).split('▼')))>34:problems.append('Over 34 chars '+str(a['id']))
    if unicodedata.normalize('NFC',b['vi'])!=b['vi']:problems.append('Non NFC '+str(a['id']))
    if any(x in b['vi'] for x in '\r\n\t'):problems.append('Extra CR LF TAB '+str(a['id']))
    if b.get('max_utf8_bytes') is not None and len(b['vi'].encode('utf8'))>b['max_utf8_bytes']:problems.append('Byte overflow '+str(a['id']))
    counts[rel]+=1
    results.append({'file':rel.removeprefix('translation/'),'id':b['id'],'en':b['en'],'vi':b['vi'],'ctx':b.get('ctx')})
expected={'translation/04-thoai/talkfigs__0eng__data__0020.005.jsonl':87,'translation/04-thoai/talkfigs__0eng__data__0021.001.jsonl':120}
if dict(counts)!=expected:problems.append('Unexpected files/changes: '+str(dict(counts)))
if total_vi!=5137:problems.append(f'Expected 5137 filled, found {total_vi}')
if jsonl_count!=501:problems.append(f'Expected 501 JSONLs, found {jsonl_count}')
if total_rows!=55976:problems.append(f'Expected 55976 source records, found {total_rows}')
if problems:raise RuntimeError('\n'.join(problems[:50]))
(ROOT/'DELTA-011.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n' for x in results),encoding='utf8')
report=f'''# QA — Magician’s Quest checkpoint 011

- Baseline: checkpoint 010 = 4.930/55.976.
- Checkpoint 011: **5.137/55.976 (+207 trang)**.
- File JSONL so sánh: **{jsonl_count}**, tổng số bản ghi **{total_rows}**.
- Thay đổi: **{sum(counts.values())}**, đúng hai tệp mới: `0020.005` (87) và `0021.001` (120).
- Chỉ trường `vi` có thay đổi; giữ toàn bộ `id`, `en`, `ctx`, thứ tự và metadata. Không ghi đè bản đã dịch.
- 0 lỗi thứ tự/số lượng mã `$...;`; giữ nguyên mã lựa chọn, biến tên và màu.
- 0 lỗi Unicode NFC, CR/LF/TAB; 0 vi phạm giới hạn thử nghiệm 34 ký tự/dòng hiển thị.
- 0 lỗi giới hạn byte nếu tệp có khai báo.
- **Chưa thử trong ROM/emulator**: cần kiểm tra font tiếng Việt, bề rộng pixel, thời gian hiển thị và tính tự nhiên khi NPC nói liên tục.

| Tệp | Trang mới |
|---|---:|
| `0020.005` | 87 |
| `0021.001` | 120 |
'''
(ROOT/'QA-011.md').write_text(report,encoding='utf8')
print(f'PASS: {jsonl_count} JSONL, {total_rows} rows, {total_vi} vi filled, {len(results)} new, 0 problems')