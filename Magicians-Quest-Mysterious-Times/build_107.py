#!/usr/bin/env python3
"""Magician's Quest NDS batch 107: 0045.001-0045.008, 960 dialogue pages."""
import collections,hashlib,json,re,unicodedata,zipfile,functools
from pathlib import Path
from translate_107 import translations as MANUAL
ROOT=Path('/mnt/data'); SRC=ROOT/'MagiciansQuest-VietHoa-Checkpoint-106.zip'; OUT=ROOT/'MagiciansQuest-VietHoa-Checkpoint-107.zip'; STAGE=ROOT/'MQ107';STAGE.mkdir(exist_ok=True)
OLD='MagiciansQuest_106/'; NEW='MagiciansQuest_107/'
TALK='translation/04-thoai/talkfigs__0eng__data__'
TARGETS=[f'0045.{i:03d}' for i in range(1,9)]
NEXT=[f'0045.{i:03d}' for i in range(9,15)]
LEAD=re.compile(r"^(?:\$(?:024|023|022|034|040|004)(?:'[-\d]+)*;)+")
TOKEN=re.compile(r"\$\d{3}(?:'[-\d]+)*;")
with zipfile.ZipFile(SRC) as z:
 assert z.testzip() is None
 oldfiles={n.removeprefix(OLD):z.read(n) for n in z.namelist() if n.startswith(OLD) and not n.endswith('/')}
jsonlnames=[n for n in oldfiles if n.startswith('translation/') and n.endswith('.jsonl')]
rowsby={n:[json.loads(line) for line in oldfiles[n].decode('utf8').splitlines() if line.strip()] for n in jsonlnames}
assert len(jsonlnames)==501 and sum(map(len,rowsby.values()))==55976
prior_count=sum(sum(r.get('vi') is not None for r in rows) for rows in rowsby.values());assert prior_count==27531,prior_count
prior=collections.defaultdict(collections.Counter)
targetset={TALK+x+'.jsonl' for x in TARGETS}
for n,rows in rowsby.items():
 if n in targetset:continue
 for r in rows:
  if isinstance(r.get('en'),str) and isinstance(r.get('vi'),str):
   prior[LEAD.sub('',r['en'])][LEAD.sub('',r['vi'])]+=1
unique=collections.Counter()
for key in TARGETS:
 n=TALK+key+'.jsonl';rows=rowsby[n]
 assert len(rows)==120 and all(r.get('vi') is None for r in rows),(key,len(rows))
 for r in rows:unique[LEAD.sub('',r['en'])]+=1
missing={i for i,e in enumerate(unique,1) if e not in prior}
assert len(unique)==445 and missing==set(MANUAL) and len(missing)==341,(len(unique),sorted(missing-set(MANUAL)),sorted(set(MANUAL)-missing))

# NDS soft-break layout: max four lines, 34 static codepoints/segment.
# Tokens are nonprintable controls and must stay intact and in exact sequence.
def wrap_vi(s,desired=30,maxlen=34):
 s=unicodedata.normalize('NFC',s.replace('▼',' ')); assert '\n' not in s
 words=s.split()
 if not words:return s
 def static_len(t):return len(TOKEN.sub('',t))
 lines=[];i=0
 while i<len(words):
  a=[]
  while i<len(words):
   c=' '.join(a+[words[i]])
   limit=26 if re.search(r"\$(?:500|501|502|503|504|505|506|507)(?:'[-\d]+)*;",c) else desired
   if not a or static_len(c)<=limit:a.append(words[i]);i+=1
   else:break
  lines.append(' '.join(a))
 if len(lines)>4 or any(static_len(line)>maxlen for line in lines):
  @functools.lru_cache(None)
  def best(start,nlines):
   if start==len(words):return (0,[])
   if nlines==0:return (10**9,[])
   bestval=(10**9,[])
   for end in range(start+1,len(words)+1):
    line=' '.join(words[start:end]);n=static_len(line)
    if n>maxlen:break
    if re.search(r"\$(?:500|501|502|503|504|505|506|507)(?:'[-\d]+)*;",line) and n>31:continue
    nextval,rest=best(end,nlines-1)
    score=max(0,n-31)*16+(maxlen-n)**2//8+nextval
    if score<bestval[0]:bestval=(score,[line]+rest)
   return bestval
  score,better=best(0,4)
  if score>=10**9:raise ValueError('UNWRAPPABLE: '+repr(s)+' suggested '+repr(lines))
  lines=better
 return '▼'.join(lines)

localized={};report=[]
for i,en in enumerate(unique,1):
 is_new=i in MANUAL
 raw=MANUAL[i] if is_new else prior[en].most_common(1)[0][0]
 vi=wrap_vi(raw) if is_new else raw
 assert isinstance(vi,str) and vi and '\n' not in vi
 assert TOKEN.findall(en)==TOKEN.findall(vi),(i,'TOKEN_MISMATCH',en,vi,TOKEN.findall(en),TOKEN.findall(vi))
 assert unicodedata.normalize('NFC',vi)==vi
 assert vi.count('▼')<=3,(i,'too many breaks',vi)
 for seg in vi.split('▼'):
  stat=TOKEN.sub('',seg)
  assert len(stat)<=34,(i,'OVERLONG',len(stat),stat)
  assert not re.search('[“”‘’—–«»…\u3000]',stat),(i,'PUNCT',stat)
 localized[en]=vi
 report.append((i,en,vi,'DỊCH MỚI' if is_new else 'TÁI DÙNG',unique[en]))
patch={};changed=[]
for key in TARGETS:
 name=TALK+key+'.jsonl';rows=[]
 for old in rowsby[name]:
  row=old.copy();lead=LEAD.match(old['en']);prefix=lead.group(0) if lead else ''
  row['vi']=prefix+localized[LEAD.sub('',old['en'])]
  assert TOKEN.findall(row['en'])==TOKEN.findall(row['vi']),(key,row['id'])
  assert {k:v for k,v in old.items() if k!='vi'}=={k:v for k,v in row.items() if k!='vi'}
  rows.append(row)
 patch[name]=''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in rows).encode('utf8')
 (STAGE/(key+'.jsonl')).write_bytes(patch[name])
 short=key.replace('.','_')
 (STAGE/('manual_'+short+'.tsv')).write_text('id\ten\tvi\tctx\n'+''.join(f"{r['id']}\t{r['en']}\t{r['vi']}\t{r.get('ctx','')}\n" for r in rows),encoding='utf8')
 (STAGE/('vi_'+short+'.txt')).write_text(''.join(f"{r['id']}\t{r['vi']}\n" for r in rows),encoding='utf8')
 changed.extend(rows)
assert len(changed)==960 and len({r['id'] for r in changed})==960
(STAGE/'DELTA-107.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in changed),encoding='utf8')
(STAGE/'unique_107.tsv').write_text('index\ten_body\tvi_body\torigin\tpages\n'+''.join(f'{i}\t{en}\t{vi}\t{org}\t{cnt}\n' for i,en,vi,org,cnt in report),encoding='utf8')
next_files=[]
for key in NEXT:
 n=TALK+key+'.jsonl';rs=rowsby.get(n)
 if rs and all(r.get('vi') is None for r in rs):
  next_files.append((key,len(rs)));(STAGE/(key+'.jsonl')).write_bytes(oldfiles[n])
TOTAL=prior_count+960;PERCENT=100*TOTAL/55976
qa=f'''# QA — Magician's Quest Checkpoint 107 (11/11/2026)

- **PASS:** 501 JSONL / 55,976 records compared with checkpoint 106.
- **27,531 → {TOTAL:,} / 55,976 ({PERCENT:.2f}%)**: +960 pages NPC across eight files `0045.001` to `0045.008` (120 each).
- **445 unique English dialogue bodies**: 104 reused from earlier translations, 341 manually localized new phrases.
- 27,531 earlier translated pages preserved; 493 non-target JSONLs byte-identical.
- Original row ID, source text, ctx, aux keys, ordering and exact NDS control-token sequence preserved.
- Unicode NFC, <=3 `▼` separators, <=34 static codepoints per segment and ordinary punctuation validated.
- ZIP CRC, 501 JSONL parse and 55,976 total records verified.
- **Not ROM tested:** dynamic placeholder widths, font glyph coverage and actual NDS layout remain outstanding.
- Next: `0045.009` onward, with six upcoming English source files staged in ZIP.
'''
cp=f'''# Magician's Quest — Checkpoint 107

**Date:** 11/11/2026
**Repository:** `ronvotri/VH-NDS` / `Magicians-Quest-Mysterious-Times/`.

- +960 NPC pages across eight dialogue files `0045.001`–`0045.008`.
- Total **{TOTAL:,}/55,976 ({PERCENT:.2f}%)**; NPC **{24406+960:,}/52,608**.
- 445 unique English dialogue patterns: 341 manually translated, 104 reused from older checkpoints.
- Topics: meals, friendship, moving schools, birthday, exchanges, student life, academic quizzes, sickness, rumors, dating and food-related jokes.
- All 27,531 older translations unchanged; 493 other JSONLs byte-identical; 501 JSONL QA PASS.
- Deliverables: `DELTA-107.jsonl`, `unique_107.tsv`, 8 manual EN–VI TSVs, `QA-107.md`, `build_107.py`, `translate_107.py` and full ZIP.
- Next 108: `0045.009` onward, with English source files staged.
- **In-ROM rendering QA outstanding.**
'''
(STAGE/'QA-107.md').write_text(qa,encoding='utf8');(STAGE/'CHECKPOINT-2026-11-11-DOT-107.md').write_text(cp,encoding='utf8')
intro_rm=f'**Checkpoint mới nhất: 107 (11/11/2026) — {TOTAL:,}/55.976 ({PERCENT:.2f}%).** +960 NPC (`0045.001`–`0045.008`), 341 mẫu dịch mới và 104 mẫu tái sử dụng, QA 501 JSONL PASS. Tiếp `0045.009` trở đi. Xem `CHECKPOINT-2026-11-11-DOT-107.md`, `QA-107.md`.\n\n'
intro_bd=f'''## Checkpoint 107 — 11/11/2026

- Gom 8 tệp `0045.001`–`0045.008`, +960 trang thoại NPC. Tổng {TOTAL:,}/55.976 ({PERCENT:.2f}%).
- Dịch thủ công 341 mẫu riêng, tái dùng 104 mẫu có sẵn. Nội dung học đường, bạn bè, ẩm thực, sinh nhật, chuyển trường, phép thuật và tin đồn.
- QA 501 JSONL PASS, giữ nguyên 27.531 bản cũ, 493 JSONL ngoài đợt bất biến.
- ZIP chứa bảng EN–VI, delta, QA, script dựng lại; chưa thử hiển thị trực tiếp trong ROM NDS.
- Đợt 108: tiếp `0045.009`–`0045.014` (nguồn tiếng Anh đã chuẩn bị trong ZIP).

'''
(STAGE/'README.md').write_text(intro_rm+oldfiles['README.md'].decode('utf8'),encoding='utf8')
(STAGE/'BAN_GIAO.md').write_text(intro_bd+oldfiles['BAN_GIAO.md'].decode('utf8'),encoding='utf8')
for n in ['README.md','BAN_GIAO.md','QA-107.md','CHECKPOINT-2026-11-11-DOT-107.md','DELTA-107.jsonl','unique_107.tsv']:
 patch[n]=(STAGE/n).read_bytes()
for k in TARGETS:
 short=k.replace('.','_')
 for pref,suf in [('manual_','.tsv'),('vi_','.txt')]:
  name=pref+short+suf;patch[name]=(STAGE/name).read_bytes()
patch['build_107.py']=Path(__file__).read_bytes();patch['translate_107.py']=(ROOT/'translate_107.py').read_bytes()
allfiles={**oldfiles,**patch}
newrows={n:[json.loads(s) for s in allfiles[n].decode('utf8').splitlines() if s.strip()] for n in jsonlnames}
assert sum(map(len,newrows.values()))==55976
assert sum(sum(r.get('vi') is not None for r in rows) for rows in newrows.values())==TOTAL
for n in jsonlnames:
 if n not in targetset:assert allfiles[n]==oldfiles[n],n
with zipfile.ZipFile(OUT,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as zout:
 for name in sorted(allfiles):zout.writestr(NEW+name,allfiles[name])
with zipfile.ZipFile(OUT) as chk:
 assert chk.testzip() is None
 assert len(chk.namelist())==len(allfiles)
print(json.dumps({'checkpoint':107,'result':'PASS','files':len(allfiles),'jsonl':len(newrows),'total':55976,'translated':TOTAL,'added':960,'unique':len(unique),'new_phrases':len(MANUAL),'reused_phrases':len(unique)-len(MANUAL),'next':next_files,'sha256':hashlib.sha256(OUT.read_bytes()).hexdigest()},ensure_ascii=False))
