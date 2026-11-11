#!/usr/bin/env python3
"""Reproducible Checkpoint 111 build from Checkpoint 110 + 108 hand edited patterns.
No ROM, patch, font, or game binaries are modified by this script.
"""
import zipfile, json, csv, hashlib, re, unicodedata, collections, pathlib, sys
from manual_111 import TRANSLATIONS

HOME=pathlib.Path(__file__).resolve().parent
SRC=HOME/'MagiciansQuest-VietHoa-Checkpoint-110.zip'
OUT=HOME/'MagiciansQuest-VietHoa-Checkpoint-111.zip'
STAGE=HOME/'MQ111'
STAGE.mkdir(exist_ok=True)
OLD_ROOT='MagiciansQuest_110/'
ROOT='MagiciansQuest_111/'
TARGET_NAMES=[f'talkfigs__0eng__data__0046.{i:03}.jsonl' for i in range(5,11)]
TARGET_KEYS=['translation/04-thoai/'+name for name in TARGET_NAMES]
TOKENS=re.compile(r"\$\d{3}(?:'\d+)*;")
STYLE=re.compile(r"^(?:(?:\$024|\$023|\$022|\$034)[^;]*;)+")

z=zipfile.ZipFile(SRC)
assert z.testzip() is None
old_content={n[len(OLD_ROOT):]:z.read(n) for n in z.namelist() if n.startswith(OLD_ROOT) and not n.endswith('/')}
old_jsonl=[n for n in old_content if n.startswith('translation/') and n.endswith('.jsonl')]
assert len(old_jsonl)==501,(len(old_jsonl),old_jsonl[-10:])

# Build exact match translations from prior data; do not overwrite any nonempty translation.
reuse={}
for name in old_jsonl:
 for raw in old_content[name].decode('utf-8').splitlines():
  row=json.loads(raw)
  if row.get('vi') and row.get('en'):
   reuse.setdefault(row['en'],row['vi'])

before=[json.loads(line) for file in old_jsonl for line in old_content[file].decode('utf-8').splitlines()]
assert len(before)==55976,len(before)
old_nonempty=sum(bool(row.get('vi')) for row in before)
assert old_nonempty==30615,old_nonempty

patterns={}
all_rows=[]
for key in TARGET_KEYS:
 orig=[json.loads(raw) for raw in old_content[key].decode('utf-8').splitlines()]
 assert len(orig)==120 and all(not x.get('vi') for x in orig)
 all_rows.extend(orig)
 for r in orig:
  patterns.setdefault(r['en'],len(patterns)+1)
assert len(all_rows)==720
assert len(patterns)==134

new_vi={}
new_patterns=set()
reused_patterns=set()
for en,ordinal in patterns.items():
 if en in reuse:
  new_vi[en]=reuse[en]
  reused_patterns.add(en)
 else:
  assert ordinal in TRANSLATIONS,(ordinal,en)
  pfx=STYLE.match(en)
  vi=(pfx.group(0) if pfx else '')+TRANSLATIONS[ordinal]
  new_vi[en]=vi
  new_patterns.add(en)
assert len(new_patterns)==108 and len(reused_patterns)==26,(len(new_patterns),len(reused_patterns))
assert len(TRANSLATIONS)==108

def qa_pair(en,vi):
 assert isinstance(vi,str) and vi
 assert TOKENS.findall(en)==TOKENS.findall(vi),(en,vi)
 assert vi==unicodedata.normalize('NFC',vi),vi
 assert vi.count('▼')<=3,(vi,vi.count('▼'))
 for seg in vi.split('▼'):
  visible=TOKENS.sub('',seg)
  assert len(visible)<=34,(vi,len(visible),visible)
 assert not any('\ud800'<=x<='\udfff' for x in vi)
 assert not any(x in vi for x in ['\u200b','\ufeff','\u2060'])
for en,vi in new_vi.items():qa_pair(en,vi)

# Apply to exactly 6 target files, leaving all EN/ID/CTX intact.
files=dict(old_content)
changes=[]
counts=[]
for key in TARGET_KEYS:
 data=[json.loads(raw) for raw in old_content[key].decode('utf-8').splitlines()]
 tally=collections.Counter()
 for row in data:
  en=row['en']
  row['vi']=new_vi[en]
  assert row['vi']
  tally['new' if en in new_patterns else 'reused']+=1
  changes.append({'id':row['id'],'en':en,'vi':row['vi'],'ctx':row['ctx']})
 files[key]=(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in data)).encode('utf-8')
 counts.append((key,tally))
assert len(changes)==720
assert sum(x['new'] for k,x in counts)==534
assert sum(x['reused'] for k,x in counts)==186

# Write supplementary ready-to-use text files.
def put(rel,text):
 b=text.encode('utf-8')
 files[rel]=b
 path=STAGE/rel
 path.parent.mkdir(exist_ok=True,parents=True)
 path.write_bytes(b)

def tsv(rows):
 import io
 s=io.StringIO(newline='');w=csv.writer(s,delimiter='\t',lineterminator='\n')
 for row in rows:w.writerow(row)
 return s.getvalue()

unique_rows=[['pattern_number','occurrences','source','en','vi']]
occ=collections.Counter(x['en'] for x in changes)
for en,idx in patterns.items():
 unique_rows.append([idx,occ[en],'NEW' if en in new_patterns else 'REUSED',en,new_vi[en]])
put('unique_111.tsv',tsv(unique_rows))
put('DELTA-111.jsonl',''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in changes))
for name,key in zip(TARGET_NAMES,TARGET_KEYS):
 rows=[json.loads(line) for line in files[key].decode('utf-8').splitlines()]
 stem=name.rsplit('data__',1)[-1].replace('.jsonl','').replace('.','_')
 put(f'manual_{stem}.tsv',tsv([['id','en','vi','ctx']]+[[r['id'],r['en'],r['vi'],r['ctx']] for r in rows]))
 put(f'vi_{stem}.txt',''.join(r['id']+'\t'+r['vi']+'\n' for r in rows))

progress=f'{old_nonempty+len(changes):,}/{len(before):,} ({(old_nonempty+len(changes))/len(before)*100:.2f}%)'
print('PROGRESS',progress)
checkpoint='''# Magician’s Quest – Checkpoint 111

**Ngày:** 11/11/2026
**Repo:** `ronvotri/VH-NDS`, thư mục `Magicians-Quest-Mysterious-Times/`.

- Đã dịch **720 trang thoại** thuộc `0046.005`–`0046.010` (120 trang/tệp).
- Tổng tiến độ **31.335/55.976 (55,98%)**, nhóm NPC **28.210/52.608**.
- 134 mẫu thoại tiếng Anh riêng biệt: **108 mẫu dịch mới** (534 trang), **26 mẫu tái sử dụng** (186 trang).
- Nội dung: chia tay, chuyện tặng quà, lời đồn, tình bạn, học đường và quan hệ nhân vật.
- Bảo toàn 30.615 mục đã dịch từ checkpoint 110; 495 JSONL ngoài phạm vi không đổi byte.
- Kiểm tra token NDS, NFC, ngắt dòng, giới hạn 34 ký tự tĩnh và JSONL hoàn tất.
- ROM/giả lập NDS chưa kiểm thử hiển thị font và độ rộng biến động.
- Tệp bàn giao: `DELTA-111.jsonl`, `unique_111.tsv`, 6 bảng TSV, 6 danh sách VI, `QA-111.md`, `manual_111.py`, `build_111.py`.
- Đợt 112 đề xuất bắt đầu từ `0046.011`.
'''
qa=f'''# QA — Magician's Quest Checkpoint 111 (11/11/2026)

- **PASS**: 501 JSONL / 55,976 records across full checkpoint.
- **30,615 → 31,335 / 55,976 (55.98%)**: +720 NPC pages in six files `0046.005`–`0046.010`.
- 134 distinct English bodies: 108 newly translated (534 pages), 26 reused (186 pages).
- 30,615 prior nonempty Vietnamese entries unchanged; 495 non-target JSONL files byte-identical.
- Original `id`, `en`, `ctx` and ancillary fields unchanged for all rows.
- Exact order of NDS tokens maintained; Unicode NFC; <=3 `▼` per translated page; <=34 static codepoints per display segment.
- CSV/TSV and JSONL parse success; full ZIP CRC PASS.
- Caveat: visual test in an actual NDS ROM / emulator and dynamic-variable widths **not yet verified**.
'''
put('CHECKPOINT-2026-11-11-DOT-111.md',checkpoint)
put('QA-111.md',qa)
put('README.md',f'**Mới nhất: checkpoint 111 (11/11/2026) — 31.335 / 55.976 (55,98%).** +720 trang NPC `0046.005`–`0046.010`; QA 501 JSONL PASS. Xem `CHECKPOINT-2026-11-11-DOT-111.md` và `QA-111.md`.\n\n'+files['README.md'].decode('utf-8'))
put('BAN_GIAO.md','## Đợt 111 — 11/11/2026\n\n- +720 trang NPC `0046.005`–`0046.010`. Tổng 31.335/55.976 (55,98%).\n- 108 mẫu dịch mới trên 534 trang; 26 mẫu tái sử dụng trên 186 trang.\n- Giữ 30.615 câu Việt cũ; QA token, giới hạn và toàn bộ 501 JSONL PASS. Chưa thử hiển thị trong ROM NDS.\n\n'+files['BAN_GIAO.md'].decode('utf-8'))
put('manual_111.py',(HOME/'mq111_new_manual.py').read_text(encoding='utf-8'))
put('build_111.py',pathlib.Path(__file__).read_text(encoding='utf-8'))

# Full archive, preserve original zip metadata where relevant.
original_meta={n[len(OLD_ROOT):]:info for n in z.namelist() if (info:=z.getinfo(n)) and n.startswith(OLD_ROOT) and not n.endswith('/')}
with zipfile.ZipFile(OUT,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6,allowZip64=True) as output:
 for rel,data in files.items():
  if rel in original_meta:
   m=original_meta[rel]
   info=zipfile.ZipInfo(ROOT+rel,date_time=m.date_time)
   info.compress_type=zipfile.ZIP_DEFLATED
   info.external_attr=m.external_attr
  else:
   info=zipfile.ZipInfo(ROOT+rel,date_time=(2026,11,11,14,0,0));info.compress_type=zipfile.ZIP_DEFLATED
  output.writestr(info,data)

# Comprehensive ZIP validation (after reopening saved artifact).
with zipfile.ZipFile(OUT) as check:
 assert check.testzip() is None
 keys=[n[len(ROOT):] for n in check.namelist() if n.startswith(ROOT+'translation/') and n.endswith('.jsonl')]
 assert len(keys)==501
 all_updated=[]
 for key in keys:
  v=check.read(ROOT+key)
  for ln in v.decode('utf-8').splitlines():
   row=json.loads(ln)
   assert row['id'] and row['en']
   all_updated.append(row)
 assert len(all_updated)==55976
 assert sum(bool(r.get('vi')) for r in all_updated)==31335
 for k in old_jsonl:
  oldrows=[json.loads(x) for x in old_content[k].decode('utf-8').splitlines()]
  newrows=[json.loads(x) for x in check.read(ROOT+k).decode('utf-8').splitlines()]
  assert len(oldrows)==len(newrows)
  for a,b in zip(oldrows,newrows):
   assert {x:y for x,y in a.items() if x!='vi'}=={x:y for x,y in b.items() if x!='vi'},k
   if a.get('vi'):assert b['vi']==a['vi'],(k,a['id'])
   if k in TARGET_KEYS:qa_pair(b['en'],b['vi'])
  if k not in TARGET_KEYS:assert check.read(ROOT+k)==old_content[k]
 print('ZIP CRC PASS',OUT.stat().st_size,'bytes,',len(check.namelist()),'archive files')

# Save a git manifest with exact blob SHAs, for later connector upload.
def git_hash(data):return hashlib.sha1(b'blob '+str(len(data)).encode('ascii')+b'\0'+data).hexdigest()
changed_rel=TARGET_KEYS+['BAN_GIAO.md','README.md','CHECKPOINT-2026-11-11-DOT-111.md','QA-111.md','DELTA-111.jsonl','unique_111.tsv','manual_111.py','build_111.py']+[f'manual_0046_{i:03}.tsv' for i in range(5,11)]+[f'vi_0046_{i:03}.txt' for i in range(5,11)]
assert len(changed_rel)==26,len(changed_rel)
manifest=[{'path':'Magicians-Quest-Mysterious-Times/'+p,'name':p.replace('/','__'),'sha':git_hash(files[p]),'bytes':len(files[p]),'newlines':len(files[p])-len(files[p].rstrip(b'\n'))} for p in changed_rel]
for x,p in zip(manifest,changed_rel):
 val=STAGE/x['name'];val.write_bytes(files[p]);assert git_hash(val.read_bytes())==x['sha']
(STAGE/'git-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
print('FILES FOR GIT',len(manifest),'REST unchanged',len(old_jsonl)-len(TARGET_KEYS))
print('STAGE',STAGE,'ZIP',OUT)
