from pathlib import Path
import zipfile,json,re,collections,unicodedata,hashlib,datetime,csv,copy,sys

ROOT=Path('/mnt/data')
WORK=ROOT/'MQ114'; WORK.mkdir(exist_ok=True)
SOURCE=ROOT/'MagiciansQuest-VietHoa-Checkpoint-113.zip'
OUTPUT=ROOT/'MagiciansQuest-VietHoa-Checkpoint-114.zip'
OLDPREFIX='MagiciansQuest_113/'
NEWPREFIX='MagiciansQuest_114/'
TARGETS=['0046.023','0046.024']+[f'0047.{i:03d}' for i in range(1,6)]
NEXT=['0047.%03d'%i for i in range(6,12)]
TOKEN=re.compile(r"\$\d{3}(?:'[-\d]+)*;")
LEAD=re.compile(r"^(?:\$\d{3}(?:'[-\d]+)*;)+")
TRAIL=re.compile(r"(?:\$\d{3}(?:'[-\d]+)*;)+$")

def parse(s):
 m=LEAD.match(s);p=m.group() if m else ''
 body=s[len(p):]
 m=TRAIL.search(body);q=m.group() if m else ''
 if q:body=body[:-len(q)]
 return p,body,q

def vislen(s):return len(TOKEN.sub('',s))

def rewrap(v, limit=34, maxlines=4):
 def wordlines(s):
  words=s.split(' ');out=[];line=''
  for w in words:
   if not w:continue
   test=line+' '+w if line else w
   if line and vislen(test)>limit:
    out.append(line);line=w
   else:line=test
  if line:out.append(line)
  return out
 if all(vislen(x)<=limit for x in v.split('▼')) and v.count('▼')<=maxlines-1:return v
 lines=[]
 for section in v.split('▼'):lines.extend(wordlines(section))
 if len(lines)>maxlines:lines=wordlines(v.replace('▼',' '))
 if len(lines)>maxlines:return v
 return '▼'.join(lines)

z=zipfile.ZipFile(SOURCE)
source_names=z.namelist();transdir=OLDPREFIX+'translation/04-thoai/'
assert all(x.startswith(OLDPREFIX) for x in source_names)
jsonl=[x for x in source_names if x.startswith(OLDPREFIX+'translation/') and x.endswith('.jsonl')]
assert len(jsonl)==501,(len(jsonl))
prior_count=0;all_rows=0;old_english=collections.defaultdict(collections.Counter)
for n in jsonl:
 for line in z.read(n).decode('utf-8-sig').splitlines():
  r=json.loads(line);all_rows+=1
  if r.get('vi'):
   prior_count+=1;old_english[r['en']][r['vi']]+=1
assert all_rows==55976 and prior_count==32775,(all_rows,prior_count)
# Prefer the most common previously accepted translation when the same English is
# translated differently in prior unrelated pages. Speaker tokens remain in EN.
old={en:c.most_common(1)[0][0] for en,c in old_english.items()}
target_paths={t:transdir+f'talkfigs__0eng__data__{t}.jsonl' for t in TARGETS}
for t,n in target_paths.items():assert n in source_names
source_rows={t:[json.loads(x) for x in z.read(target_paths[t]).decode('utf-8-sig').splitlines()] for t in TARGETS}
counts={t:len(rs) for t,rs in source_rows.items()}
assert counts=={'0046.023':120,'0046.024':38,'0047.001':120,'0047.002':120,'0047.003':120,'0047.004':120,'0047.005':120},counts
for t,rs in source_rows.items():
 assert all(r.get('vi') is None for r in rs),t
assert sum(counts.values())==758
unique=list(dict.fromkeys(r['en'] for t in TARGETS for r in source_rows[t]))
fresh=[e for e in unique if e not in old]
assert len(unique)==524 and len(fresh)==444,(len(unique),len(fresh))
manual={}
for i,line in enumerate((WORK/'translation_114.tsv').read_text(encoding='utf-8').splitlines(),1):
 k,v=line.split('\t',1);k=int(k)
 assert k not in manual
 manual[k]=v
assert set(manual)==set(range(len(fresh))),(len(manual),set(range(len(fresh)))-set(manual))
vi_by_en=dict(old);errors=[]
for i,e in enumerate(fresh):
 pre,body,suf=parse(e);toks=TOKEN.findall(body);translation=manual[i]
 if len(toks)!=translation.count('¤'):
  errors.append(('MARKER',i,e,translation));continue
 parts=translation.split('¤')
 v=pre+''.join(part+(toks[j] if j<len(toks) else '') for j,part in enumerate(parts))+suf
 v=rewrap(unicodedata.normalize('NFC',v))
 vi_by_en[e]=v
for i,e in enumerate(unique):
 v=vi_by_en[e]
 if TOKEN.findall(e)!=TOKEN.findall(v):errors.append(('TOKENS',i,e,v))
 if unicodedata.normalize('NFC',v)!=v:errors.append(('NFC',i,v))
 if v.count('▼')>3:errors.append(('LINES',i,v))
 for segment in v.split('▼'):
  if vislen(segment)>34:errors.append(('WIDTH',i,vislen(segment),v))
 if not v.strip():errors.append(('EMPTY',i,e))
if errors:
 for e in errors[:80]:print('ERROR',e)
 raise ValueError(f'{len(errors)} translation QA failures')

changes={};flat=[];n_reuse=0;n_new=0
for t in TARGETS:
 path=target_paths[t];rs=source_rows[t]
 for r in rs:
  r['vi']=vi_by_en[r['en']]
  assert r['vi']
  if r['en'] in old:n_reuse+=1
  else:n_new+=1
  flat.append(r)
 encoded=('\n'.join(json.dumps(x,ensure_ascii=False,separators=(',',':')) for x in rs)+'\n').encode('utf-8')
 changes[path]=encoded
 (WORK/(t+'.jsonl')).write_bytes(encoded)
 with (WORK/('manual_'+t.replace('.','_')+'.tsv')).open('w',encoding='utf-8',newline='') as f:
  f.write('id\ten\tvi\n')
  for r in rs:f.write(f'{r["id"]}\t{r["en"]}\t{r["vi"]}\n')
 with (WORK/('vi_'+t.replace('.','_')+'.txt')).open('w',encoding='utf-8') as f:
  f.write('\n'.join(f'{r["id"]}\t{r["vi"]}' for r in rs)+'\n')
assert len(flat)==758 and n_reuse+n_new==758
assert prior_count+758==33533
assert len(changes)==7
# Before writing the pack, validate that only .vi fields have changed.
for t,rs in source_rows.items():
 before=[json.loads(v) for v in z.read(target_paths[t]).decode().splitlines()]
 assert len(before)==len(rs)
 for b,a in zip(before,rs):
  assert b['vi'] is None
  chk=copy.deepcopy(a);chk['vi']=None
  assert b==chk,(t,b['id'])

with (WORK/'unique_114.tsv').open('w',encoding='utf-8') as f:
 f.write('index\toccurrences\tstatus\ten\tvi\n')
 freq=collections.Counter(r['en'] for r in flat)
 for i,e in enumerate(unique):f.write(f'{i}\t{freq[e]}\t{"reused" if e in old else "new"}\t{e}\t{vi_by_en[e]}\n')
(WORK/'DELTA-114.jsonl').write_text('\n'.join(json.dumps(r,ensure_ascii=False,separators=(',',':')) for r in flat)+'\n',encoding='utf-8')
(WORK/'manual_114.tsv').write_text('index\ttranslation_body\n'+'\n'.join(f'{i}\t{manual[i]}' for i in range(len(fresh)))+'\n',encoding='utf-8')
(WORK/'QA-114.md').write_text(f'''# Magician's Quest — QA checkpoint 114

- **PASS:** 501 tệp JSONL, 55.976 dòng.
- Đã thêm **758 trang thoại NPC**: {', '.join(f'{t} ({counts[t]})' for t in TARGETS)}.
- Mẫu tiếng Anh độc lập: 524; **444 mẫu dịch mới**, 80 mẫu dùng lại.
- Trang theo mẫu: **{n_new} mới**, **{n_reuse} tái sử dụng**.
- Tiến độ: **32.775 → 33.533 / 55.976 (59,91%)**; NPC **30.408 / 52.608**.
- Bảo toàn 32.775 bản dịch trước và 494 tệp JSONL ngoài đợt không đổi byte.
- Giữ nguyên `id`, `en`, `ctx`; chỉ bổ sung trường `vi` ở 758 dòng mới.
- Token `$...;` đúng thứ tự; NFC; tối đa 3 ký tự `▼`; tối đa 34 ký tự tĩnh/đoạn: **PASS**.
- ZIP CRC kiểm tra sau đóng gói; đối chiếu byte ngoài phạm vi: **PASS**.
- **Chưa kiểm tra trên ROM NDS/giả lập**. Chuỗi tên/đồ động có thể gây tràn hiển thị; cần kiểm thử thực tế.
''',encoding='utf-8')
(WORK/'CHECKPOINT-2026-11-12-DOT-114.md').write_text(f'''# Magician's Quest — Checkpoint 114

**Ngày:** 12/11/2026  
**Repo:** `ronvotri/VH-NDS/Magicians-Quest-Mysterious-Times/`

- **+758 trang NPC**, thuộc `0046.023` (120), `0046.024` (38), `0047.001`–`0047.005` (600).
- Tổng: **33.533 / 55.976 (59,91%)**; NPC **30.408 / 52.608**.
- **444 mẫu mới**, 80 mẫu nguyên văn dùng lại, ứng với {n_new} / {n_reuse} trang.
- Chủ đề: cổ tự, Manticore, Griffin, Harpy, Kraken, Golem, người bán diêm, Nhân Sư, tình bạn, chuyện chuyển trường, bài tập và giao dịch nội thất.
- QA 501 JSONL PASS; giữ 32.775 bản dịch trước và 494 tệp ngoài phạm vi không đổi byte.
- Bàn giao ZIP, `DELTA-114.jsonl`, `manual_114.tsv`, `unique_114.tsv`, 7 bảng EN–VI, 7 tệp VI, `QA-114.md`, `build_114.py`.
- Chưa kiểm thử hiển thị thực tế trên ROM NDS.
- Kế tiếp đợt 115: `0047.006`–`0047.011`, 720 trang tiếng Anh đã có sẵn.
''',encoding='utf-8')
for name in ('BAN_GIAO.md','README.md'):
 text=z.read(OLDPREFIX+name).decode('utf-8')
 heading=f'## Cập nhật 114 — 12/11/2026\n\n+758 trang NPC `0046.023`–`0046.024` và `0047.001`–`0047.005`; 444 mẫu dịch mới, 80 tái dùng. Tổng 33.533 / 55.976 (59,91%). QA dữ liệu PASS; chưa test ROM NDS. Xem `CHECKPOINT-2026-11-12-DOT-114.md`, `QA-114.md`.\n\n'
 (WORK/name).write_text(heading+text,encoding='utf-8')

# Pack all prior ZIP files and their original non-target bytes, renamed only at root.
new_files=['CHECKPOINT-2026-11-12-DOT-114.md','QA-114.md','DELTA-114.jsonl','manual_114.tsv','unique_114.tsv','translation_114.tsv','build_114.py']
for t in TARGETS:
 new_files.extend(['manual_'+t.replace('.','_')+'.tsv','vi_'+t.replace('.','_')+'.txt'])
assert len(new_files)==21
with zipfile.ZipFile(OUTPUT,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as out:
 for item in z.infolist():
  name=item.filename
  assert name.startswith(OLDPREFIX)
  relative=name[len(OLDPREFIX):]
  dest=NEWPREFIX+relative
  if name in changes:payload=changes[name]
  elif relative in ('BAN_GIAO.md','README.md'):payload=(WORK/relative).read_bytes()
  else:payload=z.read(item)
  out.writestr(dest,payload,compress_type=zipfile.ZIP_DEFLATED)
 for name in new_files:
  assert (WORK/name).exists(),name
  assert NEWPREFIX+name not in out.namelist()
  out.write(WORK/name,NEWPREFIX+name)
with zipfile.ZipFile(OUTPUT) as v:
 assert v.testzip() is None
 assert len(v.namelist())==len(source_names)+len(new_files)
 for n in source_names:
  rel=n[len(OLDPREFIX):]
  if n not in changes and rel not in ('README.md','BAN_GIAO.md'):
   assert v.read(NEWPREFIX+rel)==z.read(n),rel
 for t in TARGETS:
  p=NEWPREFIX+'translation/04-thoai/talkfigs__0eng__data__'+t+'.jsonl'
  assert sum(bool(json.loads(l).get('vi')) for l in v.read(p).decode().splitlines())==counts[t]
 print('ZIP PASS',len(v.namelist()),'entries',OUTPUT.stat().st_size,'bytes, CRC clean')
print('QA PASS',all_rows,'JSONL 501 old',prior_count,'new',len(flat),'total',prior_count+len(flat))
print('PAGES reuse',n_reuse,'new',n_new,'unique reusable',len(unique)-len(fresh),'unique fresh',len(fresh))
print('SHA256',hashlib.sha256(OUTPUT.read_bytes()).hexdigest())
