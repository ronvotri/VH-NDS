#!/usr/bin/env python3
"""Checkpoint 110: manually localize 475 distinct English NPC dialogue bodies.
Preserve all non-target JSONL byte-for-byte; enforce NDS token order and line limits.
"""
from pathlib import Path
import zipfile, json, collections, re, hashlib, unicodedata
ROOT=Path('/mnt/data');SRC=ROOT/'MagiciansQuest-VietHoa-Checkpoint-109.zip'; OUT=ROOT/'MagiciansQuest-VietHoa-Checkpoint-110.zip'
STAGE=ROOT/'MQ110';STAGE.mkdir(exist_ok=True)
OLD='MagiciansQuest_109/';NEW='MagiciansQuest_110/'
TALK='translation/04-thoai/talkfigs__0eng__data__'
TARGETS=['0045.021','0045.022']+[f'0046.{i:03d}' for i in range(1,5)]
NEXT=[f'0046.{i:03d}' for i in range(5,11)]
TOK=re.compile(r"\$\d{3}(?:'[-\d]+)*;")
LEAD=re.compile(r"^(?:\$(?:024|023|022|034|040|004)(?:'[-\d]+)*;)+")
TAIL=re.compile(r"(?:\$(?:079|073|032|033)(?:'[-\d]+)*;)+$")
def gitsha(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def static_len(s):return len(TOK.sub('',s))
def wrap(s):
 words=s.replace('▼',' ').split()
 if not words:raise ValueError('Empty translation')
 long=[w for w in words if static_len(w)>34]
 if long:raise ValueError(f'Overwide words: {long!r} from {s!r}')
 lines=[];line=''
 for w in words:
  candidate=line+' '+w if line else w
  if line and static_len(candidate)>34:lines.append(line);line=w
  else:line=candidate
 if line:lines.append(line)
 if len(lines)>4:raise ValueError(f'{len(lines)} lines, {s!r}, {lines!r}')
 return '▼'.join(lines)
manual_lines=(ROOT/'MQ110_TRANSLATIONS.tsv').read_text(encoding='utf8').splitlines()
assert len(manual_lines)==475
MANUAL={}
for raw in manual_lines:
 idx,v=raw.split('\t',1)
 assert int(idx)==len(MANUAL)+1
 MANUAL[int(idx)]=v
with zipfile.ZipFile(SRC) as z:
 assert z.testzip() is None
 files={n.removeprefix(OLD):z.read(n) for n in z.namelist() if n.startswith(OLD) and not n.endswith('/')}
jsnames=[n for n in files if n.startswith('translation/') and n.endswith('.jsonl')]
rowsby={n:[json.loads(s) for s in files[n].decode('utf8').splitlines()] for n in jsnames}
assert len(jsnames)==501 and sum(map(len,rowsby.values()))==55976
oldtotal=sum(sum(r.get('vi') is not None for r in rs) for rs in rowsby.values())
assert oldtotal==29931,oldtotal
keys=[TALK+x+'.jsonl' for x in TARGETS]
for k in keys:assert k in rowsby and all(r.get('vi') is None for r in rowsby[k]),k
prior=collections.defaultdict(collections.Counter)
for n,rs in rowsby.items():
 if n in keys:continue
 for r in rs:
  if isinstance(r.get('en'),str) and isinstance(r.get('vi'),str):prior[r['en']][r['vi']]+=1
known={en:c.most_common(1)[0][0] for en,c in prior.items()}
targetrows=[r for k in keys for r in rowsby[k]]
unique=list(dict.fromkeys(r['en'] for r in targetrows if r['en'] not in known))
assert len(unique)==len(MANUAL)==475
manual={en:MANUAL[i] for i,en in enumerate(unique,1)}
problems=[]
def to_vi(en):
 if en in known:return known[en],'TÁI DÙNG'
 pre=LEAD.match(en).group() if LEAD.match(en) else ''
 end=TAIL.search(en).group() if TAIL.search(en) else ''
 body=manual[en]
 if end and body.endswith(end):body=body[:-len(end)]
 translated=pre+wrap(body)+end
 if TOK.findall(en)!=TOK.findall(translated):
  raise AssertionError(f'Wrong token sequence, id {unique.index(en)+1}\nEN {en}\nVI {translated}\nEN tokens {TOK.findall(en)}\nVI tokens {TOK.findall(translated)}')
 if unicodedata.normalize('NFC',translated)!=translated:raise ValueError('Non-NFC '+str(unique.index(en)+1))
 if translated.count('▼')>3 or any(static_len(p)>34 for p in translated.split('▼')):raise ValueError('Too long '+str(unique.index(en)+1))
 if any(c in translated for c in ['“','”','…','—','–','\xa0']):raise ValueError('Nonstandard punctuation '+str(unique.index(en)+1))
 return translated,'DỊCH MỚI'
# First validate all unique translations and report without stopping at first issue.
for i,en in enumerate(unique,1):
 try:to_vi(en)
 except Exception as exc:problems.append((i,str(exc)))
if problems:
 print('QA problems',len(problems))
 for idx,p in problems:print('##',idx,p)
 raise SystemExit(2)
newfiles=dict(files);delta=[];usage=collections.Counter()
for x in TARGETS:
 n=TALK+x+'.jsonl';out=[]
 for r0 in rowsby[n]:
  r=dict(r0);v,origin=to_vi(r['en']);r['vi']=v
  assert r['vi'] and all(r[f]==v for f,v in r0.items() if f!='vi')
  assert TOK.findall(r['en'])==TOK.findall(r['vi'])
  assert r['vi'].count('▼')<=3 and all(static_len(s)<=34 for s in r['vi'].split('▼'))
  usage[origin]+=1;out.append(r)
  delta.append({'id':r['id'],'en':r['en'],'vi':r['vi'],'file':n,'origin':origin,'ctx':r.get('ctx')})
 newfiles[n]=(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in out)).encode('utf8')
 newfiles['manual_'+x.replace('.','_')+'.tsv']=('id\ten\tvi\tctx\torigin\n'+''.join('\t'.join(str(y) for y in [r['id'],r['en'],r['vi'],r.get('ctx',''),to_vi(r['en'])[1]])+'\n' for r in out)).encode('utf8')
 newfiles['vi_'+x.replace('.','_')+'.txt']=(''.join(r['id']+'\t'+r['vi']+'\n' for r in out)).encode('utf8')
assert len(delta)==684 and usage['DỊCH MỚI']==633 and usage['TÁI DÙNG']==51,usage
assert all(newfiles[n]==files[n] for n in jsnames if n not in keys)
newfiles['DELTA-110.jsonl']=(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in delta)).encode('utf8')
ct=collections.Counter(r['en'] for r in delta)
newfiles['unique_110.tsv']=('index\ten_body\tvi_body\torigin\tpages\n'+''.join('\t'.join(str(v) for v in [i,en,to_vi(en)[0],'DỊCH MỚI',ct[en]])+'\n' for i,en in enumerate(unique,1))).encode('utf8')
newtotal=oldtotal+684;pc=100*newtotal/55976
assert newtotal==30615
qa=f'''# QA — Magician's Quest Checkpoint 110 (11/11/2026)\n\n- **PASS:** 501 JSONL / 55,976 records checked against checkpoint 109.\n- **29,931 → 30,615 / 55,976 ({pc:.2f}%)**: +684 NPC pages in `0045.021`, `0045.022`, `0046.001`–`0046.004`.\n- **475 new distinct English dialogue patterns**, used on 633 pages; 51 pages reused from prior checkpoints.\n- All 29,931 prior translations were preserved; 495 non-target JSONL files byte-identical.\n- English sources, row ID, ctx and metadata preserved.\n- Exact control-token sequence, color spans, choice code, player-name placeholders preserved.\n- NFC Unicode, <=3 `▼` per target translation, <=34 static Unicode codepoints per displayed segment.\n- 501 JSONL parse success, 55,976 records and ZIP CRC checked after build.\n- **Not tested in ROM:** font glyph coverage and dynamic placeholder width require visual NDS testing.\n- Next 111: `0046.005`–`0046.010` (720 pages, English source staged).\n'''
cp=f'''# Magician's Quest — Checkpoint 110\n\n**Date:** 11/11/2026\n**Repository:** `ronvotri/VH-NDS` / `Magicians-Quest-Mysterious-Times/`\n\n- **+684 NPC pages** across six files `0045.021` (120), `0045.022` (84), `0046.001`–`0046.004` (120 each).\n- Total **30,615/55,976 ({pc:.2f}%)**, NPC **27,490/52,608**.\n- 475 unique English dialogue patterns translated manually; used on 633 pages; 51 pages reused.\n- Topics: fairy tales, the forest, rumors, Santa, magical creatures, romance, housing, exchanges, spells and school quizzes.\n- 501 JSONL QA PASS. All 29,931 prior translations and 495 non-target files preserved.\n- Hand-off: full ZIP, `DELTA-110.jsonl`, `unique_110.tsv`, 6 TSVs, 6 VI sheets, `QA-110.md`, `build_110.py`, `MQ110_TRANSLATIONS.tsv`.\n- Next: `0046.005`–`0046.010`, 720 pages staged from English source.\n- **In-ROM NDS visual QA still pending.**\n'''
head=f'''## Checkpoint 110 — 11/11/2026\n\n- +684 NPC pages (`0045.021`–`0045.022`, `0046.001`–`0046.004`).\n- **30,615/55,976 ({pc:.2f}%)**, +475 manually localized EN patterns covering 633 pages; 51 reused.\n- 501 JSONL QA PASS; all old translations preserved, ROM layout still untested.\n- Next 111: `0046.005`–`0046.010` (720 pages).\n\n'''
newfiles['QA-110.md']=qa.encode()
newfiles['CHECKPOINT-2026-11-11-DOT-110.md']=cp.encode()
newfiles['BAN_GIAO.md']=(head+files['BAN_GIAO.md'].decode('utf8')).encode('utf8')
newfiles['README.md']=(f'**Checkpoint mới nhất: 110 (11/11/2026) — 30.615/55.976 ({pc:.2f}%).** +684 NPC pages; QA 501 JSONL PASS. Xem `CHECKPOINT-2026-11-11-DOT-110.md`, `QA-110.md`.\n\n'+files['README.md'].decode('utf8')).encode('utf8')
newfiles['build_110.py']=Path(__file__).read_bytes()
newfiles['MQ110_TRANSLATIONS.tsv']=(ROOT/'MQ110_TRANSLATIONS.tsv').read_bytes()
for x in NEXT:
 n=TALK+x+'.jsonl';assert n in rowsby and len(rowsby[n])==120 and all(r.get('vi') is None for r in rowsby[n]),x
with zipfile.ZipFile(OUT,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for k,v in sorted(newfiles.items()):z.writestr(NEW+k,v)
with zipfile.ZipFile(OUT) as z:
 assert z.testzip() is None
 rebuilt={n.removeprefix(NEW):z.read(n) for n in z.namelist()}
 names=[n for n in rebuilt if n.startswith('translation/') and n.endswith('.jsonl')]
 assert len(names)==501
 assert sum(len(rebuilt[n].splitlines()) for n in names)==55976
 assert all(rebuilt[n]==files[n] for n in jsnames if n not in keys)
 assert sum(sum(json.loads(s).get('vi') is not None for s in rebuilt[n].decode('utf8').splitlines()) for n in names)==newtotal
 for n in names:
  for s in rebuilt[n].decode('utf8').splitlines():json.loads(s)
 for x in NEXT:assert rebuilt[TALK+x+'.jsonl']==files[TALK+x+'.jsonl']
# Stage modified files and exact source slices for next batch on GitHub.
for n,v in newfiles.items():
 if n not in files or v!=files[n]:
  name=Path(n).name.replace('talkfigs__0eng__data__','') if n.startswith('translation/') else Path(n).name
  (STAGE/name).write_bytes(v)
for x in NEXT:(STAGE/(x+'.jsonl')).write_bytes(newfiles[TALK+x+'.jsonl'])
modified=[]
for n,v in newfiles.items():
 if n not in files or v!=files[n]:
  modified.append({'path':'Magicians-Quest-Mysterious-Times/'+n,'name':Path(n).name.replace('talkfigs__0eng__data__','') if n.startswith('translation/') else Path(n).name,'sha':gitsha(v),'bytes':len(v),'newlines':len(v)-len(v.rstrip(b'\n'))})
for x in NEXT:
 n=TALK+x+'.jsonl';v=newfiles[n]
 modified.append({'path':'Magicians-Quest-Mysterious-Times/'+n,'name':x+'.jsonl','sha':gitsha(v),'bytes':len(v),'newlines':len(v)-len(v.rstrip(b'\n'))})
(STAGE/'git-manifest.json').write_text(json.dumps(modified,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'output':str(OUT),'bytes':OUT.stat().st_size,'zip_entries':len(newfiles),'prior':oldtotal,'total':newtotal,'percent':round(pc,2),'new_unique':len(unique),'new_pages':usage['DỊCH MỚI'],'reused_pages':usage['TÁI DÙNG'],'github_files':len(modified),'next':NEXT},ensure_ascii=False,indent=2))
