"""Reproducible checkpoint-112 builder for Magician's Quest.
Usage: python MQ112_build.py
Inputs: /mnt/data/MagiciansQuest-VietHoa-Checkpoint-111.zip, /mnt/data/MQ112_manual.tsv
Outputs: /mnt/data/MQ112, /mnt/data/MagiciansQuest-VietHoa-Checkpoint-112.zip
"""
import collections, csv, hashlib, io, json, os, pathlib, re, unicodedata, zipfile
from collections import defaultdict
SRC=pathlib.Path('/mnt/data/MagiciansQuest-VietHoa-Checkpoint-111.zip')
OUT=pathlib.Path('/mnt/data/MagiciansQuest-VietHoa-Checkpoint-112.zip')
STAGE=pathlib.Path('/mnt/data/MQ112');STAGE.mkdir(exist_ok=True)
TEXT=pathlib.Path('/mnt/data/MQ112_manual.tsv')
SOURCE_ROOT='MagiciansQuest_111/'
NEW_ROOT='MagiciansQuest_112/'
PAT='translation/04-thoai/talkfigs__0eng__data__0046.{}.jsonl'
TARGETS=[PAT.format(f'{i:03}') for i in range(11,17)]
RE_PREFIX=re.compile(r"^(?:(?:\$024|\$023|\$022|\$034)[^;]*;)+")
RE_TOKEN=re.compile(r"\$\d{3}(?:'\d+)*;")
manual={}
for line in TEXT.read_text('utf-8').splitlines():
 k,vi=line.split('\t',1); assert int(k) not in manual
 manual[int(k)]=vi
assert len(manual)==100 and sorted(manual)==list(range(1,101))

def body(en):return RE_PREFIX.sub('',en)
def check(en,vi,where):
 assert RE_TOKEN.findall(en)==RE_TOKEN.findall(vi),(where,'TOKEN',RE_TOKEN.findall(en),RE_TOKEN.findall(vi))
 assert vi==unicodedata.normalize('NFC',vi),(where,'NFC')
 assert vi.count('▼')<=3,(where,'BREAK',vi)
 for seg in vi.split('▼'):
  part=RE_TOKEN.sub('',seg)
  assert len(part)<=34,(where,'LENGTH',len(part),part)
 assert not re.search('[\u200b\u200c\u200d\ufeff]',vi),(where,'ZERO-WIDTH')

with zipfile.ZipFile(SRC) as z:
 assert z.testzip() is None
 blobs={n[len(SOURCE_ROOT):]:z.read(n) for n in z.namelist() if n.startswith(SOURCE_ROOT) and not n.endswith('/')}
 assert len(blobs)>1500
 all_jsonls=[n for n in blobs if n.startswith('translation/') and n.endswith('.jsonl')]
 assert len(all_jsonls)==501,len(all_jsonls)
 prev=dict()
 total=prev_count=0
 for fname in all_jsonls:
  for line in blobs[fname].decode('utf-8').splitlines():
   if not line.strip():continue
   x=json.loads(line);total+=1
   if x.get('vi'):
    prev_count+=1
    prev.setdefault(x['en'],set()).add(x['vi'])
 assert total==55976,(total,len(all_jsonls))
 assert prev_count==31335,prev_count
 target=[json.loads(line) for n in TARGETS for line in blobs[n].decode('utf-8').splitlines() if line.strip()]
 assert len(target)==720
 assert all(not x.get('vi') for x in target)
 unique_missing={}
 for x in target:
  if len(prev.get(x['en'],[]))==1:continue
  unique_missing.setdefault(body(x['en']),len(unique_missing)+1)
 assert len(unique_missing)==100,len(unique_missing)
 assert set(manual)==set(unique_missing.values())
 outrows=[];exact_rows=body_rows=new_rows=0;manual_body_old=0
 overrides={};delta=[];manual_tables={};vi_lists={}
 for f in TARGETS:
  rows=[json.loads(line) for line in blobs[f].decode('utf-8').splitlines() if line.strip()]
  new_rows_file=[];manual_row_file=[];vi_list_file=[]
  for row in rows:
   en=row['en'];old_vi=row.get('vi')
   if len(prev.get(en,[]))==1:
    vi=next(iter(prev[en]));typ='reused-exact';exact_rows+=1
   else:
    b=body(en);id=unique_missing[b]
    pfx=RE_PREFIX.match(en)
    vi=(pfx.group(0) if pfx else '')+manual[id]
    # One pattern already exists with the same body from older checkpoint.
    if any(body(v)==manual[id] for v in prev.get(en,set())):typ='reused-body';body_rows+=1
    else:
     typ='new';new_rows+=1
    if b=="Don't do it again!":manual_body_old+=1;typ='reused-body';new_rows-=1;body_rows+=1
   check(en,vi,row['id'])
   row['vi']=vi
   new_rows_file.append(row)
   delta.append(dict(id=row['id'],en=en,vi=vi,ctx=row.get('ctx'),source=f,translation_kind=typ))
   manual_row_file.append((row['id'],en,vi,typ))
   vi_list_file.append((row['id'],vi))
  overrides[f]='\n'.join(json.dumps(r,ensure_ascii=False,separators=(',',':')) for r in new_rows_file).encode('utf-8')+b'\n'
  short=f.rsplit('0046.',1)[1].split('.')[0]
  manual_tables[f'manual_0046_{short}.tsv']=manual_row_file
  vi_lists[f'vi_0046_{short}.txt']=vi_list_file
 assert exact_rows+body_rows+new_rows==720,(exact_rows,body_rows,new_rows)
 assert manual_body_old==1,(manual_body_old,exact_rows,body_rows,new_rows)
 assert new_rows==524,(exact_rows,body_rows,new_rows)
 # Verify all non-target source files still byte-identical.
 merged=blobs.copy();merged.update(overrides)
 tot=count=0
 for name in all_jsonls:
  for line in merged[name].decode('utf-8').splitlines():
   x=json.loads(line);tot+=1
   if x.get('vi'):count+=1
 assert (tot,count)==(55976,32055),(tot,count)
 for name in all_jsonls:
  if name not in TARGETS:assert merged[name]==blobs[name]
 total_patterns=len({body(x['en']) for x in target})
 percent=100*count/tot
 new_patterns=99
 reused_patterns=total_patterns-new_patterns
 print('STATS:',dict(total_patterns=total_patterns,missing_patterns=len(unique_missing),fresh_patterns=new_patterns,prior_patterns=reused_patterns,exact_reused_pages=exact_rows,body_reused_pages=body_rows,new_pages=new_rows,translated=count,total=tot,percent=percent))
 # Construct report artifacts.
 def as_tsv(header,rows):
  out=io.StringIO(newline=''); w=csv.writer(out,delimiter='\t',lineterminator='\n');w.writerow(header);w.writerows(rows);return out.getvalue().encode('utf-8')
 for n,rows in manual_tables.items():merged[n]=as_tsv(('id','en','vi','method'),rows)
 for n,rows in vi_lists.items():merged[n]=as_tsv(('id','vi'),rows)
 ordered=[]
 for b,i in unique_missing.items():
  en=next(x['en'] for x in target if body(x['en'])==b)
  occurrences=sum(1 for x in target if body(x['en'])==b)
  ordered.append((i,en,manual[i],occurrences,'reuse-body' if i==25 else 'new'))
 merged['unique_112.tsv']=as_tsv(('index','english','vietnamese','pages','method'),ordered)
 merged['manual_112.tsv']=TEXT.read_bytes()
 merged['DELTA-112.jsonl']=(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n' for x in delta)).encode()
 new_line=f'**Mới nhất: checkpoint 112 (11/11/2026) — 32.055/55.976 ({percent:.2f}%).** +720 trang thoại NPC (`0046.011`–`0046.016`), 99 mẫu mới, 196 trang tái sử dụng; QA 501 JSONL PASS. Xem `CHECKPOINT-2026-11-11-DOT-112.md`, `QA-112.md`.\n\n'
 merged['README.md']=new_line.encode()+blobs['README.md']
 bang=f'## Checkpoint 112 — 11/11/2026\n\n- Dịch 720 trang `0046.011`–`0046.016`, tăng 31.335 lên 32.055 trên tổng 55.976 ({percent:.2f}%).\n- 100 mẫu thiếu bản Việt nguyên văn; 99 mẫu viết mới, một mẫu tái sử dụng theo phần thân câu; 195 trang dùng lại bản dịch trùng nguyên văn.\n- Chủ đề: tình bạn, tin đồn, hẹn hò, bí mật, học hành, những câu thoại châm chọc ngộ nghĩnh.\n- QA 501 JSONL / 55.976 bản ghi PASS, giữ nguyên 31.335 mục trước đó, 495 JSONL ngoài đợt byte-identical.\n- Giữ nguyên token NDS, kiểm tra độ dài tĩnh <=34 ký tự/đoạn, NFC, không quá 3 ngắt dòng.\n- Chưa test giao diện ROM NDS; các token biến động chiều rộng có thể làm tràn khung.\n- Đợt 113: `0046.017`–`0046.022`.\n\n'
 merged['BAN_GIAO.md']=bang.encode()+blobs['BAN_GIAO.md']
 cp=f'''# Magician’s Quest — Checkpoint 112\n\n**Ngày:** 11/11/2026\n**Repo:** `ronvotri/VH-NDS`, thư mục `Magicians-Quest-Mysterious-Times/`.\n\n- **+720 trang thoại** thuộc `0046.011`–`0046.016` (120 trang/tệp).\n- Tổng tiến độ **32.055 / 55.976 ({percent:.2f}%)**; NPC **28.930 / 52.608**.\n- 141 mẫu nội dung tiếng Anh khác nhau. Tái sử dụng nguyên văn 195 trang; 1 trang tái dùng phần thân; 524 trang sử dụng 99 mẫu dịch mới.\n- Ngữ cảnh: lời đồn học đường, tình cảm, hẹn hò bí mật, tình bạn, ước mơ và phép thuật.\n- Bảo toàn 31.335 bản dịch cũ; 495 tệp ngoài phạm vi không đổi.\n- QA: 501 JSONL / 55.976 dòng PASS; token NDS, 3 ngắt dòng, NFC, 34 ký tự tĩnh/đoạn.\n- ROM/giả lập NDS chưa test trực quan; biến tên nhân vật có thể tràn dòng, cần kiểm tra.\n- Handoff: ZIP, `DELTA-112.jsonl`, `unique_112.tsv`, 6 TSV, 6 danh sách VI, `manual_112.tsv`, `build_112.py`, `QA-112.md`.\n- Đợt kế: `0046.017`–`0046.022` (720 trang).\n'''
 merged['CHECKPOINT-2026-11-11-DOT-112.md']=cp.encode()
 qa=f'''# QA — Magician's Quest Checkpoint 112 (11/11/2026)\n\n- **PASS:** 501 JSONL / 55.976 bản ghi.\n- Tiến độ: **31.335 → 32.055 / 55.976 ({percent:.2f}%)**; +720 trang NPC.\n- 6 tệp `0046.011`–`0046.016` đều đủ 120/120 trang và có `vi` không rỗng.\n- 141 mẫu nội dung, 100 mẫu không có bản dịch trùng nguyên văn ở checkpoint 111, trong đó 99 mẫu dịch thủ công mới, 1 mẫu tái sử dụng phần thân.\n- 524 trang dịch mới; 196 trang tái sử dụng (195 trùng nguyên văn, 1 trùng phần thân).\n- Token NDS và thứ tự: PASS; Unicode NFC: PASS; <=3 `▼`: PASS; <=34 ký tự tĩnh/đoạn: PASS.\n- Không có thay đổi về `id`, `en`, `ctx` hoặc các trường khác ngoài `vi`.\n- 495 tệp JSONL ngoài phạm vi giữ nguyên byte, 31.335 bản dịch cũ giữ nguyên.\n- JSONL parse PASS; ZIP CRC: PASS (sau xuất).\n- Lưu ý: chưa thử nghiệm trực quan trên NDS/giả lập; biến động chiều rộng của các mã động chưa được xác minh.\n'''
 merged['QA-112.md']=qa.encode()
 merged['build_112.py']=pathlib.Path(__file__).read_bytes()
 # Record manifest for git staging: only files changed/added from previous checkpoint.
 changes={n:b for n,b in merged.items() if n not in blobs or blobs[n]!=b}
 assert len([x for x in changes if x in TARGETS])==6
 assert len([x for x in changes if x not in TARGETS])==20,(len(changes),sorted(changes))
 manifest=[]
 for path,data in changes.items():
  sha=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\x00'+data).hexdigest()
  manifest.append(dict(path='Magicians-Quest-Mysterious-Times/'+path,name=path.replace('/','__'),sha=sha,bytes=len(data),newlines=len(data)-len(data.rstrip(b'\n'))))
 (STAGE/'git-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),'utf-8')
 for rel,data in changes.items():
  dest=STAGE/rel.replace('/','__');dest.write_bytes(data)
 with zipfile.ZipFile(OUT,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as zz:
  for rel,data in merged.items():zz.writestr(NEW_ROOT+rel,data)
 with zipfile.ZipFile(OUT) as result:
  assert result.testzip() is None
  assert len([n for n in result.namelist() if '/translation/' in n and n.endswith('.jsonl')])==501
 print('PACKED',OUT,OUT.stat().st_size,'changes',len(changes),'manifest',STAGE/'git-manifest.json')
