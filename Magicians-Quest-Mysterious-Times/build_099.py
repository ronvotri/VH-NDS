#!/usr/bin/env python3
"""Rebuild Magician's Quest checkpoint 099 from checkpoint 098 ZIP; NDS text data only."""
from pathlib import Path
import collections
import hashlib
import json
import re
import unicodedata
import zipfile
from translate import translations as MANUAL

ROOT=Path('/mnt/data')
PREV=ROOT/'MagiciansQuest-VietHoa-Checkpoint-098.zip'
OUT=ROOT/'MagiciansQuest-VietHoa-Checkpoint-099.zip'
STAGE=ROOT/'MQ099/stage'
STAGE.mkdir(parents=True,exist_ok=True)
OLD='MagiciansQuest_098/'
NEW='MagiciansQuest_099/'
TALK='translation/04-thoai/talkfigs__0eng__data__'
TARGETS=['0044.005','0044.006']
NEXT=['0044.007','0044.008']
LEAD=re.compile(r"^(?:\$(?:024|023|022|034|040|004)(?:'[-\d]+)*;)+")
TOKEN=re.compile(r"\$\d{3}(?:'[-\d]+)*;")

with zipfile.ZipFile(PREV) as zin:
    assert zin.testzip() is None
    oldfiles={n[len(OLD):]:zin.read(n) for n in zin.namelist() if n.startswith(OLD) and not n.endswith('/')}
assert len(oldfiles)==1429,len(oldfiles)
jsonlnames=[n for n in oldfiles if n.startswith('translation/') and n.endswith('.jsonl')]
assert len(jsonlnames)==501,len(jsonlnames)
rowsby={n:[json.loads(line) for line in oldfiles[n].decode('utf8').splitlines() if line.strip()] for n in jsonlnames}
assert sum(map(len,rowsby.values()))==55976
assert sum(sum(r.get('vi') is not None for r in rows) for rows in rowsby.values())==25415

targetnames={TALK+k+'.jsonl' for k in TARGETS}
prior=collections.defaultdict(collections.Counter)
for name,rows in rowsby.items():
    if name in targetnames: continue
    for row in rows:
        if isinstance(row.get('en'),str) and isinstance(row.get('vi'),str):
            prior[LEAD.sub('',row['en'])][LEAD.sub('',row['vi'])]+=1
unique={}
for key in TARGETS:
    name=TALK+key+'.jsonl'
    rows=rowsby[name]
    assert len(rows)==120 and all(r['vi'] is None for r in rows),(key,'unexpected source')
    for row in rows: unique.setdefault(LEAD.sub('',row['en']),None)
assert len(unique)==75,len(unique)
assert set(MANUAL)=={i for i,en in enumerate(unique,1) if not prior[en]},('reuse mismatch',sorted(set(MANUAL).symmetric_difference({i for i,en in enumerate(unique,1) if not prior[en]})))
assert len(MANUAL)==58

translations={}
report=[]
for i,en in enumerate(unique,1):
    new=i in MANUAL
    vi=MANUAL[i] if new else prior[en].most_common(1)[0][0]
    assert isinstance(vi,str) and vi and '\n' not in vi,(i,'missing')
    assert TOKEN.findall(en)==TOKEN.findall(vi),(i,'token mismatch',en,vi)
    assert unicodedata.normalize('NFC',vi)==vi,(i,'non-NFC')
    assert vi.count('▼')<=3,(i,'too many breaks')
    for seg in vi.split('▼'):
        static=TOKEN.sub('',seg)
        assert len(static)<=34,(i,'overlength',len(static),static)
        assert not re.search('[“”‘’—–«»…\u3000]',static),(i,'unusual punctuation',static)
    translations[en]=vi
    report.append((i,en,vi,'DỊCH MỚI' if new else 'TÁI DÙNG'))

patch={}
changed=[]
for key in TARGETS:
    name=TALK+key+'.jsonl'
    rows=[]
    for old in rowsby[name]:
        row=old.copy()
        m=LEAD.match(row['en'])
        row['vi']=(m.group(0) if m else '')+translations[LEAD.sub('',row['en'])]
        assert TOKEN.findall(row['en'])==TOKEN.findall(row['vi']),row['id']
        assert {k:v for k,v in old.items() if k!='vi'}=={k:v for k,v in row.items() if k!='vi'}
        rows.append(row)
    data=''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in rows).encode('utf8')
    patch[name]=data
    (STAGE/(key+'.jsonl')).write_bytes(data)
    short=key.replace('.','_')
    (STAGE/('manual_'+short+'.tsv')).write_text('id\ten\tvi\tctx\n'+''.join(f"{r['id']}\t{r['en']}\t{r['vi']}\t{r.get('ctx','')}\n" for r in rows),encoding='utf8')
    (STAGE/('vi_'+short+'.txt')).write_text(''.join(f"{r['id']}\t{r['vi']}\n" for r in rows),encoding='utf8')
    changed.extend(rows)
assert len(changed)==240 and len({r['id'] for r in changed})==240
(STAGE/'DELTA-099.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in changed),encoding='utf8')
(STAGE/'unique_099.tsv').write_text('index\ten_body\tvi_body\torigin\n'+''.join(f'{i}\t{en}\t{vi}\t{org}\n' for i,en,vi,org in report),encoding='utf8')
for key in NEXT:
    name=TALK+key+'.jsonl'
    rows=rowsby[name]
    assert len(rows)==120 and all(row['vi'] is None for row in rows)
    (STAGE/(key+'.jsonl')).write_bytes(oldfiles[name])

qa='''# QA — Magician's Quest Checkpoint 099 (10/11/2026)

- **PASS:** 501 JSONL / 55,976 records compared with checkpoint 098.
- **25,415 → 25,655 / 55,976 (45.83%)**: +240 NPC dialogue pages.
- `0044.005`: 120/120; `0044.006`: 120/120.
- 75 unique English dialogue bodies: **17 reused** previously translated pairs, **58 manually translated** new lines.
- All 25,415 earlier translations preserved; **499 non-target JSONLs byte-identical**.
- `id`, `en`, `ctx`, additional JSON fields and ordering preserved.
- Exact NDS token sequences preserved; Unicode NFC PASS; max 3 breaks and 34 static codepoints per segment.
- ZIP CRC PASS; full JSONL parse and total/translated counts PASS.
- **Not verified inside ROM:** font width and dynamic variable expansion still require device/emulator QA.
- Next 100: `0044.007` and `0044.008`, 120 English pages each (not translated).
'''
cp='''# Magician's Quest — Checkpoint 099

**Date:** 10/11/2026
**Repository:** `ronvotri/VH-NDS` / `Magicians-Quest-Mysterious-Times/`.

- +240 NPC pages: `0044.005` and `0044.006` (120 each).
- Total: **25,655/55,976 (45.83%)**; NPC **22,530/52,608**.
- 75 unique English body patterns: 17 reused, 58 newly localized.
- Content: scholarly pupil, gift-giving, play invitations, school gossip, magic and experiments, friendship and jealousy.
- QA PASS: 501 JSONL files; 25,415 existing translations unchanged, 499 non-target JSONLs byte-identical; NDS token and static line width checked.
- Handoff: `DELTA-099.jsonl`, `unique_099.tsv`, two TSVs, `QA-099.md`, `build_099.py`, full ZIP in Library.
- Next 100: `0044.007` and `0044.008` (240 pages, English untranslated, included in ZIP).
- ROM visual validation remains outstanding.
'''
(STAGE/'QA-099.md').write_text(qa,encoding='utf8')
(STAGE/'CHECKPOINT-2026-11-10-DOT-99.md').write_text(cp,encoding='utf8')
intro_rm='**Checkpoint mới nhất: 099 (10/11/2026) — 25.655/55.976 (45,83%).** +240 trang thoại NPC (`0044.005` + `0044.006`); 58 mẫu mới, 17 mẫu tái sử dụng; QA 501 JSONL PASS. Đợt 100: `0044.007` và `0044.008` (240 trang). Xem `CHECKPOINT-2026-11-10-DOT-99.md`, `QA-099.md`.\n\n'
intro_bd='''## Checkpoint 099 — 10/11/2026

- +240 trang NPC `0044.005` và `0044.006`, tổng **25.655/55.976 (45,83%)**, NPC 22.530/52.608.
- 75 mẫu EN riêng, 17 tái dùng, 58 dịch mới; thoại học sinh ham nghiên cứu, quà tặng, lời đồn và tình bạn.
- QA 501 JSONL PASS; giữ 25.415 bản dịch cũ; 499 JSONL ngoài đợt không đổi byte.
- Bàn giao ZIP đầy đủ, EN–VI, delta, QA và script; chưa kiểm thử trực tiếp ROM NDS.
- Đợt 100: `0044.007` và `0044.008`, 120 trang mỗi tệp.

'''
(STAGE/'README.md').write_text(intro_rm+oldfiles['README.md'].decode('utf8'),encoding='utf8')
(STAGE/'BAN_GIAO.md').write_text(intro_bd+oldfiles['BAN_GIAO.md'].decode('utf8'),encoding='utf8')

# Add/update only the 2 target JSONLs and handoff artifacts.
for name in ['README.md','BAN_GIAO.md','QA-099.md','CHECKPOINT-2026-11-10-DOT-99.md','DELTA-099.jsonl','unique_099.tsv',
             'manual_0044_005.tsv','manual_0044_006.tsv','vi_0044_005.txt','vi_0044_006.txt']:
    patch[name]=(STAGE/name).read_bytes()
patch['build_099.py']=Path(__file__).read_bytes()
allfiles={**oldfiles,**patch}
assert len(allfiles)==len(oldfiles)+9,(len(allfiles),len(oldfiles))
assert allfiles.keys()>=oldfiles.keys()
for n,b in oldfiles.items():
    if n not in patch: assert allfiles[n]==b,(n,'unintended change')

# Full QA of every JSONL and exact preservation of 499 non-target translation files.
newrows={n:[json.loads(line) for line in allfiles[n].decode('utf8').splitlines() if line.strip()] for n in jsonlnames}
assert len(newrows)==501 and sum(map(len,newrows.values()))==55976
assert sum(sum(r.get('vi') is not None for r in rows) for rows in newrows.values())==25655
for n in jsonlnames:
    if n not in targetnames: assert allfiles[n]==oldfiles[n],n
with zipfile.ZipFile(OUT,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as zout:
    for name in sorted(allfiles):
        zout.writestr(NEW+name,allfiles[name])
with zipfile.ZipFile(OUT) as test:
    assert test.testzip() is None
    assert len(test.namelist())==len(allfiles)
    assert all(test.read(NEW+name)==data for name,data in allfiles.items())
print(json.dumps({'status':'PASS','checkpoint':99,'files':len(allfiles),'jsonl_files':len(newrows),'records':55976,'translated':25655,'new_pages':240,'unique':len(unique),'reused':len(unique)-len(MANUAL),'new_unique':len(MANUAL),'zip_bytes':OUT.stat().st_size,'sha256':hashlib.sha256(OUT.read_bytes()).hexdigest()},ensure_ascii=False))