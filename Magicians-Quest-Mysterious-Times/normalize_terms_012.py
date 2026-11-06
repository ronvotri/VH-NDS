#!/usr/bin/env python3
"""Unify already translated The Emporium to the approved system label. Only modify vi."""
import json,re,pathlib,unicodedata
ROOT=pathlib.Path(__file__).resolve().parent
TOKEN=re.compile(r"\$\d+(?:'[-\d]+)*;")
changed=[]
for path in sorted((ROOT/'translation').rglob('*.jsonl')):
 recs=[json.loads(l) for l in path.read_text(encoding='utf8').splitlines()]
 dirty=False
 for row in recs:
  old=row.get('vi')
  if old is None or 'The Emporium' not in old:continue
  new=unicodedata.normalize('NFC',old.replace('The Emporium','Bách Hóa Tổng Hợp'))
  assert TOKEN.findall(old)==TOKEN.findall(new)==TOKEN.findall(row['en']),row['id']
  assert max(map(len,TOKEN.sub('',new).split('▼')))<=34,row['id']
  if row.get('max_utf8_bytes') is not None: assert len(new.encode('utf8'))<=row['max_utf8_bytes'],row['id']
  row['vi']=new;dirty=True
  changed.append({'file':str(path.relative_to(ROOT)),'id':row['id'],'old_vi':old,'new_vi':new})
 if dirty:path.write_text(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in recs),encoding='utf8')
assert len(changed)==6,len(changed)
(ROOT/'TERM-CORRECTIONS-012.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in changed),encoding='utf8')
(ROOT/'THUAT-NGU-012.md').write_text('# Chốt địa danh — The Emporium\n\n- **The Emporium → Bách Hóa Tổng Hợp** (tên hiển thị của tiệm đồ phép thuật).\n- Kế thừa lựa chọn đã có tại menu `0999.006`, đồng bộ thêm 6 dòng từng giữ tiếng Anh ở bảng tên và thoại NPC.\n- Giữ nguyên mã tô màu `$000\'5;`, `$000\'1;`, tên chủ tiệm Malila và trường tiếng Anh gốc.\n- Các đoạn gốc khác còn trống sẽ áp dụng từ điển này khi dịch tới.\n- Rà độ rộng hiển thị trực tiếp trên NDS sau khi có ROM thử nghiệm.\n',encoding='utf8')
print('Normalized',len(changed),'translated records')