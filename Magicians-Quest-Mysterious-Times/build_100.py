#!/usr/bin/env python3
"""Magician's Quest checkpoint-100 builder: edits only 0044.007/.008, preserves original game tokens."""
import json, collections, re, zipfile, hashlib, unicodedata, os
from pathlib import Path
from translate_100 import translations as MANUAL
ROOT=Path('/mnt/data')
SRC=ROOT/'MagiciansQuest-VietHoa-Checkpoint-099.zip'
OUT=ROOT/'MagiciansQuest-VietHoa-Checkpoint-100.zip'
STAGE=ROOT/'MQ100'
OLD='MagiciansQuest_099/'
NEW='MagiciansQuest_100/'
TALK='translation/04-thoai/talkfigs__0eng__data__'
TARGETS=['0044.007','0044.008']
NEXT=['0044.009','0044.010']
LEAD=re.compile(r"^(?:\$(?:024|023|022|034|040|004)(?:'[-\d]+)*;)+")
TOKEN=re.compile(r"\$\d{3}(?:'[-\d]+)*;")
with zipfile.ZipFile(SRC) as zin:
    assert zin.testzip() is None
    oldfiles={name[len(OLD):]:zin.read(name) for name in zin.namelist() if name.startswith(OLD) and not name.endswith('/')}
assert len(oldfiles)==1438, len(oldfiles)
jsonlnames=[name for name in oldfiles if name.startswith('translation/') and name.endswith('.jsonl')]
assert len(jsonlnames)==501
rowsby={name:[json.loads(s) for s in oldfiles[name].decode('utf8').splitlines() if s.strip()] for name in jsonlnames}
assert sum(map(len,rowsby.values()))==55976
assert sum(sum(r.get('vi') is not None for r in rows) for rows in rowsby.values())==25655
prior=collections.defaultdict(collections.Counter)
for name,rows in rowsby.items():
    if name in {TALK+k+'.jsonl' for k in TARGETS}:continue
    for row in rows:
        if isinstance(row.get('en'),str) and isinstance(row.get('vi'),str):
            prior[LEAD.sub('',row['en'])][LEAD.sub('',row['vi'])]+=1
unique={}
for key in TARGETS:
    name=TALK+key+'.jsonl'
    rows=rowsby[name]
    assert len(rows)==120 and all(r.get('vi') is None for r in rows)
    for row in rows:unique.setdefault(LEAD.sub('',row['en']),None)
assert len(unique)==91
assert set(MANUAL)=={i for i,en in enumerate(unique,1) if not prior[en]},('new unique mismatch',set(MANUAL).symmetric_difference({i for i,en in enumerate(unique,1) if not prior[en]}))
assert len(MANUAL)==44
translations={};report=[]
for i,en in enumerate(unique,1):
    is_new=i in MANUAL
    vi=MANUAL[i] if is_new else prior[en].most_common(1)[0][0]
    assert vi and isinstance(vi,str) and '\n' not in vi,(i,'empty')
    assert TOKEN.findall(en)==TOKEN.findall(vi),(i,'token mismatch',en,vi)
    assert unicodedata.normalize('NFC',vi)==vi,(i,'not NFC')
    assert vi.count('▼')<=3,(i,'excess break')
    for seg in vi.split('▼'):
        static=TOKEN.sub('',seg)
        assert len(static)<=34,(i,'overlong',len(static),static)
        assert not re.search('[“”‘’—–«»…\u3000]',static),(i,'punctuation',static)
    translations[en]=vi
    report.append((i,en,vi,'DỊCH MỚI' if is_new else 'TÁI DÙNG'))
patch={};changed=[]
for key in TARGETS:
    name=TALK+key+'.jsonl'; rows=[]
    for old in rowsby[name]:
        row=old.copy(); m=LEAD.match(row['en']);row['vi']=(m.group(0) if m else '')+translations[LEAD.sub('',row['en'])]
        assert TOKEN.findall(row['en'])==TOKEN.findall(row['vi']),row['id']
        assert {k:v for k,v in row.items() if k!='vi'}=={k:v for k,v in old.items() if k!='vi'}
        rows.append(row)
    data=''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in rows).encode('utf8')
    patch[name]=data
    (STAGE/(key+'.jsonl')).write_bytes(data)
    short=key.replace('.','_')
    (STAGE/('manual_'+short+'.tsv')).write_text('id\ten\tvi\tctx\n'+''.join(f"{r['id']}\t{r['en']}\t{r['vi']}\t{r.get('ctx','')}\n" for r in rows),encoding='utf8')
    (STAGE/('vi_'+short+'.txt')).write_text(''.join(f"{r['id']}\t{r['vi']}\n" for r in rows),encoding='utf8')
    changed.extend(rows)
assert len(changed)==240 and len({r['id'] for r in changed})==240
(STAGE/'DELTA-100.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in changed),encoding='utf8')
(STAGE/'unique_100.tsv').write_text('index\ten_body\tvi_body\torigin\n'+''.join(f'{i}\t{en}\t{vi}\t{org}\n' for i,en,vi,org in report),encoding='utf8')
next_files=[]
for key in NEXT:
    name=TALK+key+'.jsonl'
    if name in rowsby and rowsby[name] and all(r['vi'] is None for r in rowsby[name]):
        next_files.append((key,len(rowsby[name])))
        (STAGE/(key+'.jsonl')).write_bytes(oldfiles[name])
qa=f'''# QA — Magician's Quest Checkpoint 100 (10/11/2026)

- **PASS:** 501 JSONL / 55,976 records compared with checkpoint 099.
- **25,655 → 25,895 / 55,976 (46.26%)**: +240 NPC dialogue pages.
- `0044.007`: 120/120; `0044.008`: 120/120.
- 91 unique English dialogue bodies: **47 reused**, **44 manually translated** new phrases (126 records).
- All 25,655 earlier translations preserved; **499 non-target JSONL files byte-identical**.
- Source `id`, `en`, `ctx`, any auxiliary keys and ordering unchanged.
- Exact NDS token sequences preserved, including `'$530'`, `'$533'`, `'$018'`, `'$033'`.
- NFC; up to 3 `▼` line breaks; max 34 static codepoints per segment; ordinary punctuation.
- ZIP integrity (CRC) and full translation count verified.
- **ROM visual QA not completed:** font pixel width, dynamic variable expansion and choice menu layout require a real ROM/emulator check.
- Next 101 candidates: {next_files!r}.
'''
cp=f'''# Magician's Quest — Checkpoint 100

**Date:** 10/11/2026
**Repository:** `ronvotri/VH-NDS` / `Magicians-Quest-Mysterious-Times/`.

- Localized **240 NPC dialogue pages** in `0044.007` and `0044.008`.
- New total: **25,895/55,976 (46.26%)**; NPC **22,770/52,608**.
- 91 distinct English bodies: 47 reused, 44 manually translated; 126 new non-reuse records.
- Themes: school gossip, friendship, romances, scientific research, pranks and conversation rumors.
- QA: 501 JSONLs PASS; 25,655 prior translations untouched; 499 other JSONL files byte-identical; source tokens/order preserved.
- Artifacts: `DELTA-100.jsonl`, `unique_100.tsv`, 2 EN–VI TSV files, `QA-100.md`, `build_100.py`, full checkpoint ZIP.
- Next 101 candidates: {next_files!r}.
- **No in-game ROM display validation yet** (dynamic variable text must be reviewed).
'''
(STAGE/'QA-100.md').write_text(qa,encoding='utf8')
(STAGE/'CHECKPOINT-2026-11-10-DOT-100.md').write_text(cp,encoding='utf8')
intro_rm='**Checkpoint mới nhất: 100 (10/11/2026) — 25.895/55.976 (46,26%).** +240 thoại NPC (`0044.007` + `0044.008`), 44 mẫu mới và 47 mẫu tái sử dụng. QA 501 JSONL PASS. Xem `CHECKPOINT-2026-11-10-DOT-100.md`, `QA-100.md`.\n\n'
intro_bd='''## Checkpoint 100 — 10/11/2026

- +240 trang NPC `0044.007` và `0044.008` (mỗi tệp 120), tổng 25.895/55.976 (46,26%), NPC 22.770/52.608.
- 91 mẫu EN riêng, 47 tái sử dụng, 44 dịch mới. Nội dung: lời đồn trong trường, tình bạn, chuyện hẹn hò, nghiên cứu và nghịch ngợm.
- QA 501 JSONL PASS; bảo toàn 25.655 câu trước và 499 JSONL khác không đổi byte.
- Bàn giao ZIP đầy đủ, bảng EN–VI, delta, QA, script dựng lại; chưa kiểm thử trên ROM NDS.

'''
(STAGE/'README.md').write_text(intro_rm+oldfiles['README.md'].decode('utf8'),encoding='utf8')
(STAGE/'BAN_GIAO.md').write_text(intro_bd+oldfiles['BAN_GIAO.md'].decode('utf8'),encoding='utf8')
for name in ['README.md','BAN_GIAO.md','QA-100.md','CHECKPOINT-2026-11-10-DOT-100.md','DELTA-100.jsonl','unique_100.tsv','manual_0044_007.tsv','manual_0044_008.tsv','vi_0044_007.txt','vi_0044_008.txt']:
    patch[name]=(STAGE/name).read_bytes()
patch['build_100.py']=Path(__file__).read_bytes()
patch['translate_100.py']=(STAGE/'translate.py').read_bytes()
allfiles={**oldfiles,**patch}
assert len(allfiles)==len(oldfiles)+10,(len(allfiles),len(oldfiles))
for n,b in oldfiles.items():
    if n not in patch:assert allfiles[n]==b,n
assert len(jsonlnames)==501
newrows={n:[json.loads(s) for s in allfiles[n].decode('utf8').splitlines() if s.strip()] for n in jsonlnames}
assert sum(map(len,newrows.values()))==55976
assert sum(sum(r.get('vi') is not None for r in rows) for rows in newrows.values())==25895
for n in jsonlnames:
    if n not in {TALK+k+'.jsonl' for k in TARGETS}:assert allfiles[n]==oldfiles[n],n
with zipfile.ZipFile(OUT,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as zout:
    for name in sorted(allfiles):zout.writestr(NEW+name,allfiles[name])
with zipfile.ZipFile(OUT) as chk:
    assert chk.testzip() is None
    assert len(chk.namelist())==len(allfiles)
print(json.dumps({'checkpoint':100,'result':'PASS','files':len(allfiles),'jsonl':len(newrows),'total':55976,'translated':25895,'added':240,'unique':len(unique),'new_phrases':len(MANUAL),'reused_phrases':len(unique)-len(MANUAL),'next':next_files,'sha256':hashlib.sha256(OUT.read_bytes()).hexdigest()},ensure_ascii=False))
