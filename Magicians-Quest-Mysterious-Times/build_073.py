#!/usr/bin/env python3
"""Magician's Quest batch 073: strict additive localization, archive and QA."""
import zipfile, json, re, pathlib, collections, unicodedata, csv, io, hashlib, sys, datetime
SRC=pathlib.Path('/mnt/data/MagiciansQuest-VietHoa-Checkpoint-072.zip')
DST=pathlib.Path('/mnt/data/MagiciansQuest-VietHoa-Checkpoint-073.zip')
OLD='MagiciansQuest_072/'
NEW='MagiciansQuest_073/'
FILES=['0041.021','0041.022']
TOKEN=re.compile(r"\$\d{3}(?:'[0-9-]+)*;")
PREFIX=re.compile(r"^(?:\$(?:024|023|022|034|040)(?:['0-9-]+)*;)+")
# Translation for only the pages genuinely absent from the existing translation memory.
NEW_021={
90:'Thích cô bạn nào thì...▼rủ người ta hẹn hò nhỉ...',
91:'Thế phải đi đâu đây?▼Có nhất thiết phải đến▼chỗ đặc biệt không?',
92:'Ờ thì...▼Chỗ nào cũng được.',
93:'Ừm... Bọn tớ đang hẹn hò.▼Vậy... có phải là...',
94:'bọn tớ yêu nhau không?▼Hẹn hò là thế à?',
95:'Xin lỗi, tớ còn gà mờ▼chuyện này lắm...',
96:'Này... lúc đi chơi cùng tớ,▼cậu thường nghĩ gì thế?',
97:'Tớ... tớ chỉ thấy hồi hộp,▼đầu óc trống trơn luôn!',
98:'Cậu nghĩ tớ có gì▼bất thường không?',
99:'Hôm nọ có bạn gái khác▼ngỏ lời với tớ,▼nhưng tớ từ chối rồi.',
100:'Tớ cũng áy náy lắm,▼nhưng biết sao giờ?▼Tớ có bạn gái rồi mà!',
101:'Nghĩ lại mới thấy...▼Có luật nào cấm▼quen hai bạn gái không nhỉ?',
102:'Một ngày nào đó tớ muốn▼phiêu lưu thật xa!',
103:'Đánh khủng long, săn▼kho báu hải tặc...▼Toàn chuyện thú vị!',
104:'Tất nhiên, khi đi,▼tớ muốn có cậu đồng hành!',
105:'$500;, cậu đã nghĩ▼lớn lên mình muốn▼làm gì chưa?',
106:'Còn tớ á? Đừng cười nhé...',
107:'Lớn lên tớ sẽ phát minh▼cách trẻ lại rồi▼trẻ mãi không già!',
108:'Thế là tụi mình có thể▼rong chơi cùng nhau mãi!',
109:'Này $500;, cậu có▼thích cô bạn nào không?',
110:'Ý là, tớ cũng mến cậu,▼nhưng khác kiểu ấy, hiểu chứ?',
111:'Tớ cũng chẳng hiểu.▼Sao một chữ "thích" thôi▼mà nam nữ cứ rối tung lên?',
112:'Trời, sống sao mà khó ghê.',
113:'Cậu mê anh hùng chứ?▼Tớ muốn làm anh hùng!',
114:'Không biết phải làm gì▼mới thành anh hùng nhỉ?',
115:'Biết đâu chỉ cần bày ra▼trò nghịch lớn nhất▼vũ trụ là thành anh hùng!',
116:'Ê, cậu giúp tớ nhé!▼Hai đứa cùng làm anh hùng!',
117:'Hả? Trời, muộn rồi!',
118:'Chắc phải về thôi...▼Cậu thấy sao?$019\'6701;',
119:'Ở lại nhé...$019\'6702;',
120:'Tớ phải về đây!$019\'6703;',
}
NEW_022={
1:'Nếu cậu muốn thì▼tớ ở lại với cậu▼bao lâu cũng được!$074;',
2:'Thật ra tớ cũng chưa▼muốn về! Trùng hợp ghê!',
3:'Ừ, cậu nói đúng.▼Hôm nay vui thật đấy!',
4:'Thôi... Hẹn gặp lại nhé!',
5:'Ê $500;! Tớ vừa▼nhớ ra có việc cực kỳ▼quan trọng phải làm!',
6:'Vậy hôm nay kết thúc$023\'328\'104\'10;▼ở đây nhé!',
}
NEW_TRANSLATIONS={'0041.021':NEW_021,'0041.022':NEW_022}

def count_static(s): return [len(TOKEN.sub('',seg)) for seg in s.split('▼')]

with zipfile.ZipFile(SRC) as zin:
  assert zin.testzip() is None
  names=zin.namelist()
  jsonl=[n for n in names if n.startswith(OLD+'translation/') and n.endswith('.jsonl')]
  print('JSONL files:',len(jsonl))
  memory={}; memory_provenance={}
  original_total=0;original_translated=0
  for n in jsonl:
    content=zin.read(n).decode('utf-8')
    rows=[json.loads(x) for x in content.splitlines()]
    original_total+=len(rows)
    for row in rows:
      if isinstance(row.get('vi'),str) and row['vi']:
        original_translated+=1
        # Exact key: never transfer color expression prefixes or reorder game tokens.
        memory[row['en']]=row['vi'];memory_provenance[row['en']]=n
  assert len(jsonl)==501 and original_total==55976 and original_translated==19332,(len(jsonl),original_total,original_translated)
  patches={}; delta=[]; manuals={}; extras={};errors=[]; reports=[];orig_rows={}
  for s in FILES:
    name=next(n for n in names if n.endswith(f'0041.{s[-3:]}.jsonl') and '/translation/' in n)
    rows=[json.loads(line) for line in zin.read(name).decode('utf-8').splitlines()]
    new=NEW_TRANSLATIONS[s]
    hits=0; hand=0; fixed=0
    assert all(r['vi'] is None for r in rows)
    for idx,r in enumerate(rows,1):
      en=r['en']
      if en in memory:
        vi=memory[en];hits+=1
      else:
        if idx not in new:
          errors.append(f'Untranslated source missing page={s}#{idx}: {en}')
          continue
        vi=new[idx];hand+=1
        # Only prefix codes reflect speaker; the rest of the text remains authored Vietnamese.
        vi=PREFIX.match(en).group(0)+vi if PREFIX.match(en) else vi
      # QA token equality must preserve every control code as an ordered sequence.
      et=TOKEN.findall(en);vt=TOKEN.findall(vi)
      if et!=vt:
        errors.append(f'token order {s}#{idx} EN={et!r} VI={vt!r} {vi!r}')
      if not unicodedata.is_normalized('NFC',vi):errors.append(f'NFC {s}#{idx}')
      if vi.count('▼')>3:errors.append(f'Break count {s}#{idx}: {vi!r}')
      widths=count_static(vi)
      if max(widths)>34:errors.append(f'Line width {s}#{idx}: {widths} {vi!r}')
      if not vi.strip():errors.append(f'empty VI {s}#{idx}')
      r['vi']=vi
      delta.append({"id":r['id'],"en":en,"vi":vi,"ctx":r['ctx']})
    patches[name]=''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in rows).encode('utf-8')
    orig_rows[name]=rows
    reports.append((s,len(rows),hits,hand,fixed))
    tsv=io.StringIO();writer=csv.writer(tsv,delimiter='\t',lineterminator='\n');writer.writerow(['id','en','vi','ctx'])
    for r in rows:writer.writerow([r['id'],r['en'],r['vi'],r['ctx']])
    manuals[f'manual_{s.replace(".","_")}.tsv']=tsv.getvalue().encode()
    extras[f'vi_{s.replace(".","_")}.txt']=''.join(r['vi']+'\n' for r in rows).encode()
  if errors:
    print('ERRORS:',*errors,sep='\n');sys.exit(1)
  assert sum(a[1] for a in reports)==126 and sum(a[2] for a in reports)==89 and sum(a[3] for a in reports)==37
  assert len(delta)==126
  # Independently validate every translated row inside the prospective merged JSONL corpus.
  new_all=0;all_count=0;old_unchanged=0;nonvi_unchanged=0;changed_files=[]
  for n in jsonl:
    old=zin.read(n)
    merged=patches.get(n,old)
    old_rows=[json.loads(l) for l in old.decode().splitlines()]
    new_rows=[json.loads(l) for l in merged.decode().splitlines()]
    assert len(new_rows)==len(old_rows),(n,len(new_rows),len(old_rows))
    if n not in patches:assert old==merged
    else:changed_files.append(n)
    for a,b in zip(old_rows,new_rows):
      assert {k:v for k,v in a.items() if k!='vi'}=={k:v for k,v in b.items() if k!='vi'}
      nonvi_unchanged+=1
      if a['vi'] is not None:assert b['vi']==a['vi'];old_unchanged+=1
      elif b['vi'] is not None:new_all+=1
      all_count+=1
  assert all_count==55976 and old_unchanged==19332 and new_all==126
  assert len(changed_files)==2
  report_text=f'''# QA — Checkpoint 073 (09/11/2026)

- Nguồn gốc: checkpoint 072, **19.332/55.976** bản ghi đã dịch.
- Đợt 073: `0041.021` **120 trang**, `0041.022` **6 trang**, tổng **126** trang.
- Từ bộ nhớ dịch: **89** câu tiếng Anh khớp hoàn toàn; dịch thủ công mới: **37**.
- Sau khi hợp nhất: **19.458 / 55.976** bản ghi, đạt **34,76%**.
- QA toàn bộ **501 JSONL / 55.976 bản ghi**: **PASS**.
- 19.332 bản dịch cũ bảo toàn; ngoài 2 JSONL đích, 499 JSONL khác giữ nguyên byte.
- ID, EN, CTX và mọi trường ngoài `vi`: không thay đổi trên 55.976 bản ghi.
- Đảm bảo token NDS giữ đúng thứ tự, Unicode NFC, tối đa 3 dấu `▼`, tối đa 34 ký tự tĩnh mỗi dòng cho 126 mục mới.
- ZIP được kiểm tra CRC; chưa thử trực tiếp trên ROM NDS (và chưa xác thực độ rộng biến động khi biến thay thế tên nhân vật).

## Tệp tiếp theo

Nguồn `0041.023` trở đi cần kiểm tra số lượng tệp trong archive trước khi chọn đợt 074.
'''
  checkpoint_text=f'''# Magician’s Quest: Checkpoint 073 — 09/11/2026

**Tiến độ: 19.458 / 55.976 (34,76%)**

- Đợt 073: 126 trang thoại NPC: `0041.021` (120) và `0041.022` (6).
- Tái sử dụng 89 bản dịch cũ trùng khớp; dịch mới 37 trang về tình cảm, khát vọng, anh hùng và hẹn gặp lại.
- Thoại NPC đã dịch: **16.333 / 52.608** (checkpoint 072: 16.207).
- QA tĩnh: 501 JSONL / 55.976 bản ghi; không tác động ngoài hai tệp đích.
- Bàn giao: `DELTA-073.jsonl`, `manual_0041_021.tsv`, `manual_0041_022.tsv`, `QA-073.md`, `build_073.py`.
- Chưa chạy thử bản dịch trên ROM NDS.
'''
  extras['DELTA-073.jsonl']=''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in delta).encode()
  extras['QA-073.md']=report_text.encode()
  extras['CHECKPOINT-2026-11-09-DOT-73.md']=checkpoint_text.encode()
  extras['build_073.py']=pathlib.Path(__file__).read_bytes()
  extras.update(manuals)
  readme_name=OLD+'README.md';handoff_name=OLD+'BAN_GIAO.md'
  readme_start=(f'**Checkpoint mới nhất: 073 (09/11/2026) — 19.458 / 55.976 (34,76%).** '
    f'Thêm 126 trang thoại NPC `0041.021` + `0041.022`; QA 501 JSONL PASS. '
    f'Xem `CHECKPOINT-2026-11-09-DOT-73.md`, `QA-073.md`, `DELTA-073.jsonl`.\n\n')
  handoff_start=(f'## Checkpoint 073 — 09/11/2026\n\n'
    f'- **19.458/55.976 (34,76%)**, thoại NPC **16.333/52.608**; tăng 126 mục từ checkpoint 072.\n'
    f'- Hoàn thành `0041.021` (120 trang) + `0041.022` (6 trang); 89 câu tái sử dụng và 37 câu dịch mới.\n'
    f'- QA toàn bộ 501 JSONL / 55.976 bản ghi: giữ 19.332 mục cũ, chỉ thêm 126 `vi`, bảo toàn mã NDS, NFC và giới hạn dòng.\n'
    f'- Full ZIP: `MagiciansQuest-VietHoa-Checkpoint-073.zip` tại `/Dịch giả lập`, chưa kiểm thử trên ROM.\n\n')
  replacements={readme_name:(readme_start+zin.read(readme_name).decode()).encode(),handoff_name:(handoff_start+zin.read(handoff_name).decode()).encode()}
  patches.update(replacements)
  # Next source: detect post-0041.022 available, don't claim staged when none exist.
  future=[]
  for n in jsonl:
    m=re.search(r'__data__([0-9]+)\.([0-9]+)\.jsonl$',n)
    if m and (int(m.group(1)),int(m.group(2)))>(41,22):
      future.append((int(m.group(1)),int(m.group(2)),n))
  future.sort();print('Next source candidates',[(n,a,b) for a,b,n in future[:5]])
  # Pack checkpoint full source retaining all original archive members, updating exactly target and docs.
  with zipfile.ZipFile(DST,'w') as zout:
    for info in zin.infolist():
      if not info.filename.startswith(OLD): raise ValueError(info.filename)
      renamed=NEW+info.filename[len(OLD):]
      newinfo=zipfile.ZipInfo(renamed,date_time=info.date_time)
      newinfo.compress_type=info.compress_type
      newinfo.external_attr=info.external_attr
      newinfo.create_system=info.create_system
      newinfo.flag_bits=info.flag_bits
      newinfo.comment=info.comment
      zout.writestr(newinfo,patches.get(info.filename,zin.read(info.filename)))
    for newname,contents in extras.items():
      zout.writestr(NEW+newname,contents,compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
print('Translation report:',reports)
with zipfile.ZipFile(DST) as z:
  assert z.testzip() is None
  assert len(z.namelist())==len(names)+len(extras)
print('Archive:',DST,DST.stat().st_size,'bytes; files',len(names)+len(extras))
print('sha256',hashlib.sha256(DST.read_bytes()).hexdigest())
print('READY')
