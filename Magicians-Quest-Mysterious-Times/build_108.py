#!/usr/bin/env python3
"""Magician's Quest checkpoint 108 — six 0045 dialogue slices (720 pages)."""
import collections, hashlib, json, re, unicodedata, zipfile
from pathlib import Path
from translate_108 import translations as MANUAL
ROOT=Path('/mnt/data'); SRC=ROOT/'MagiciansQuest-VietHoa-Checkpoint-107.zip';OUT=ROOT/'MagiciansQuest-VietHoa-Checkpoint-108.zip'; STAGE=ROOT/'MQ108';STAGE.mkdir(exist_ok=True)
OLD='MagiciansQuest_107/'; NEW='MagiciansQuest_108/'
TALK='translation/04-thoai/talkfigs__0eng__data__'
TARGETS=[f'0045.{i:03d}' for i in range(9,15)]; NEXT=[f'0045.{i:03d}' for i in range(15,21)]
LEAD=re.compile(r"^(?:\$(?:024|023|022|034|040|004)(?:'[-\d]+)*;)+")
TOK=re.compile(r"\$\d{3}(?:'[-\d]+)*;")

with zipfile.ZipFile(SRC) as z:
 assert z.testzip() is None
 oldfiles={n.removeprefix(OLD):z.read(n) for n in z.namelist() if n.startswith(OLD) and not n.endswith('/')}
jsonlnames=[n for n in oldfiles if n.startswith('translation/') and n.endswith('.jsonl')]
rowsby={n:[json.loads(line) for line in oldfiles[n].decode('utf8').splitlines() if line.strip()] for n in jsonlnames}
assert len(jsonlnames)==501 and sum(map(len,rowsby.values()))==55976
prior_count=sum(sum(r.get('vi') is not None for r in rows) for rows in rowsby.values())
assert prior_count==28491,prior_count
sourcekeys={TALK+x+'.jsonl' for x in TARGETS}
for key in sourcekeys:
 assert key in rowsby and len(rowsby[key])==120 and all(r.get('vi') is None for r in rowsby[key]), key
prior=collections.defaultdict(collections.Counter)
for n,rows in rowsby.items():
 if n in sourcekeys:continue
 for r in rows:
  if isinstance(r.get('en'),str) and isinstance(r.get('vi'),str):
   prior[r['en']][r['vi']]+=1
known={en:c.most_common(1)[0][0] for en,c in prior.items()}
targetrows=[r for x in TARGETS for r in rowsby[TALK+x+'.jsonl']]
unique=list(dict.fromkeys(r['en'] for r in targetrows if r['en'] not in known))
assert len(targetrows)==720 and len(unique)==129,(len(targetrows),len(unique))
assert set(MANUAL)==set(range(1,len(unique)+1))
manual={en:MANUAL[i] for i,en in enumerate(unique,1)}

def static_len(text):return len(TOK.sub('',text))
def wrap(text):
 """Wrap translated words into up to four NDS text segments; tokens count as zero width."""
 words=text.split()
 assert words and all(static_len(word)<=34 for word in words),text
 pieces=[];line=''
 for word in words:
  cand=(line+' '+word if line else word)
  if static_len(cand)>34 and line:
   pieces.append(line);line=word
  else:line=cand
 if line:pieces.append(line)
 assert len(pieces)<=4,(text,pieces)
 return '▼'.join(pieces)

def to_vi(en):
 if en in known:return known[en], 'TÁI DÙNG'
 lead=LEAD.match(en).group() if LEAD.match(en) else ''
 new=lead+wrap(manual[en])
 assert TOK.findall(en)==TOK.findall(new),(en,new)
 assert new.count('▼')<=3
 for segment in new.split('▼'):
  assert static_len(segment)<=34,(en,new,segment)
 assert unicodedata.normalize('NFC',new)==new
 assert all(c not in new for c in ['“','”','…','—','–',' '])
 return new,'DỊCH MỚI'

delta=[];usage=collections.Counter();outfiles=dict(oldfiles)
for x in TARGETS:
 k=TALK+x+'.jsonl';out=[]
 for r in rowsby[k]:
  before=dict(r)
  vi,origin=to_vi(r['en']);r['vi']=vi
  assert r['vi'] and all(r[key]==val for key,val in before.items() if key!='vi')
  assert TOK.findall(r['en'])==TOK.findall(vi),(r['id'],vi)
  assert unicodedata.normalize('NFC',vi)==vi
  assert vi.count('▼')<=3 and all(static_len(y)<=34 for y in vi.split('▼'))
  usage[origin]+=1;out.append(r)
  delta.append({'id':r['id'],'en':r['en'],'vi':vi,'file':k,'origin':origin,'ctx':r.get('ctx')})
 outfiles[k]=(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in out)).encode('utf8')
 path=f'manual_{x.replace(".","_")}.tsv'
 outfiles[path]=('id\ten\tvi\tctx\torigin\n'+''.join('\t'.join(str(y) for y in [r['id'],r['en'],r['vi'],r.get('ctx',''),to_vi(r['en'])[1]])+'\n' for r in out)).encode('utf8')
 outfiles[f'vi_{x.replace(".","_")}.txt']=(''.join(r['id']+'\t'+r['vi']+'\n' for r in out)).encode('utf8')

assert len(delta)==720
new_count=sum(sum(r.get('vi') is not None for r in rowsby[name]) for name in rowsby if name not in sourcekeys)+720
assert new_count==29211
# Assert no non-target old data modified in ZIP; byte-for-byte preserving 495 files.
assert all(outfiles[n]==oldfiles[n] for n in jsonlnames if n not in sourcekeys)
assert usage=={'TÁI DÙNG':303,'DỊCH MỚI':417},usage
assert len(set(r['en'] for r in delta if r['origin']=='DỊCH MỚI'))==129
outfiles['DELTA-108.jsonl']=(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in delta)).encode('utf8')
ct=collections.Counter(r['en'] for r in delta)
col=[]
for i,en in enumerate(unique,1):
 vi,_=to_vi(en)
 col.append('\t'.join(str(x) for x in [i,en,vi,'DỊCH MỚI',ct[en]]))
outfiles['unique_108.tsv']=('index\ten_body\tvi_body\torigin\tpages\n'+'\n'.join(col)+'\n').encode('utf8')

pc=(29211/55976)*100
qa=f'''# QA — Magician's Quest Checkpoint 108 (11/11/2026)

- **PASS:** 501 JSONL / 55,976 records verified against checkpoint 107.
- **28,491 → 29,211 / 55,976 ({pc:.2f}%)**: +720 NPC dialogue pages across `0045.009`–`0045.014` (six files, 120 each).
- 303 pages reused by exact English match, 417 pages using **129 hand-localized new phrases**.
- Earlier 28,491 translated pages preserved, and 495 non-target JSONLs byte-identical.
- Source EN, row IDs, ctx, other metadata, and original ordering preserved.
- Exact NDS control-token sequence preserved, including dynamic placeholders and dialogue choices.
- Unicode NFC, <=3 `▼` separators, <=34 static codepoints per segment, plain punctuation validated.
- ZIP CRC, 501 JSONL parse and 55,976 total records verified.
- **Not tested in ROM:** font metrics, dynamic placeholder widths, speaker portraits, and on-device layout require visual QA.
- Next: `0045.015`–`0045.020` (six source files staged, 720 pages).
'''
cp=f'''# Magician's Quest — Checkpoint 108

**Date:** 11/11/2026
**Repository:** `ronvotri/VH-NDS` / `Magicians-Quest-Mysterious-Times/`.

- **+720 NPC pages** in six files `0045.009`–`0045.014`.
- Total **29,211/55,976 ({pc:.2f}%)**; NPC **26,086/52,608**.
- 129 distinct newly translated English dialogues, applied to 417 pages; 303 pages reused from older checkpoints.
- Dialogue themes: friendship rumors, teasing, secret dates, breakups, meals, jealousy, family, fantasy gossip and gentle food-based jokes.
- 501 JSONL QA PASS; 495 non-target JSONLs byte-identical, 28,491 earlier translations preserved.
- Deliverables: `DELTA-108.jsonl`, `unique_108.tsv`, 6 manual EN–VI TSVs, QA and replay scripts, full ZIP.
- Next 109: `0045.015`–`0045.020` (720 pages; English sources staged).
- **In-ROM display QA remains untested.**
'''
head=f'''## Checkpoint 108 — 11/11/2026

- +720 NPC pages (`0045.009`–`0045.014`), 29,211/55,976 ({pc:.2f}%).
- 129 original Vietnamese dialogue translations / 417 page uses; 303 exact-source reuses.
- QA 501 JSONL PASS; all preceding 28,491 translations preserved; not ROM tested.
- Next: `0045.015`–`0045.020` (720 pages).

'''
outfiles['QA-108.md']=qa.encode('utf8');outfiles['CHECKPOINT-2026-11-11-DOT-108.md']=cp.encode('utf8')
outfiles['BAN_GIAO.md']=(head+oldfiles['BAN_GIAO.md'].decode('utf8')).encode('utf8')
outfiles['README.md']=('**Checkpoint mới nhất: 108 (11/11/2026) — 29.211/55.976 ('+f'{pc:.2f}'.replace('.',',')+'%).** +720 thoại NPC (6 tệp `0045.009`–`0045.014`); QA 501 JSONL PASS. Xem `CHECKPOINT-2026-11-11-DOT-108.md` và `QA-108.md`.\n\n'+oldfiles['README.md'].decode('utf8')).encode('utf8')
outfiles['build_108.py']=Path(__file__).read_bytes();outfiles['translate_108.py']=Path('/mnt/data/translate_108.py').read_bytes()
# Stage next raw source slices already in the checkpoint 107 ZIP.
for x in NEXT:
 key=TALK+x+'.jsonl'
 assert key in outfiles and len(rowsby[key])==120 and all(r['vi'] is None for r in rowsby[key])
# Full verification of rebuilt bundle.
with zipfile.ZipFile(OUT,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for n,v in sorted(outfiles.items()):z.writestr(NEW+n,v)
with zipfile.ZipFile(OUT) as z:
 assert z.testzip() is None
 newer={n.removeprefix(NEW):z.read(n) for n in z.namelist()}
 assert len([n for n in newer if n.startswith('translation/') and n.endswith('.jsonl')])==501
 assert sum(len(newer[n].decode('utf8').splitlines()) for n in jsonlnames)==55976
 for n in jsonlnames:
  if n not in sourcekeys:assert newer[n]==oldfiles[n]
  for line in newer[n].decode('utf8').splitlines():json.loads(line)
 assert sum(sum(json.loads(x).get('vi') is not None for x in newer[n].decode('utf8').splitlines()) for n in jsonlnames)==29211
 for x in TARGETS:
  n=TALK+x+'.jsonl'
  prev=rowsby[n]; now=[json.loads(x) for x in newer[n].decode('utf8').splitlines()]
  assert len(now)==len(prev)==120
  for a,b in zip(prev,now):
   assert a.keys()==b.keys() and all(a[k]==b[k] for k in a if k!='vi') and b['vi']
 for x in NEXT:assert newer[TALK+x+'.jsonl']==oldfiles[TALK+x+'.jsonl']
for n,v in outfiles.items():
 if n not in oldfiles or v!=oldfiles[n]:
  fn=STAGE/Path(n).name
  if n.startswith('translation/'):
   fn=STAGE/Path(n).name.replace('talkfigs__0eng__data__','')
  fn.write_bytes(v)
# Calculate git blob SHA in manifest for exact byte-matching before push.
def gitsha(b):return hashlib.sha1(b'blob '+str(len(b)).encode('ascii')+b'\0'+b).hexdigest()
modified=[]
for n,v in outfiles.items():
 if n not in oldfiles or v!=oldfiles[n]:modified.append({'path':'Magicians-Quest-Mysterious-Times/'+n,'name':Path(n).name.replace('talkfigs__0eng__data__','') if n.startswith('translation/') else Path(n).name,'sha':gitsha(v),'bytes':len(v),'newlines':len(v)-len(v.rstrip(b'\n'))})
assert len(modified)==(6+6+6+2+1+5),len(modified) # 26: six JSONL, six TSV, six vi, two scripts, unique, delta, QA, checkpoint, README and handoff
(STAGE/'git-manifest.json').write_text(json.dumps(modified,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'output':str(OUT),'bytes':OUT.stat().st_size,'files':len(outfiles),'jsonls':len(jsonlnames),'previous':prior_count,'total':new_count,'percentage':round(pc,2),'unique_new':len(unique),'new_pages':usage['DỊCH MỚI'],'reused_pages':usage['TÁI DÙNG'],'modified':len(modified),'next':NEXT},ensure_ascii=False,indent=2))
