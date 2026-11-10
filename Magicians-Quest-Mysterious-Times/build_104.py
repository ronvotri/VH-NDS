#!/usr/bin/env python3
"""Build Magician's Quest checkpoint 104: 240 NPC pages, full incremental QA."""
import collections,datetime,hashlib,json,re,unicodedata,zipfile
from pathlib import Path
from translate_104 import translations as MANUAL
ROOT=Path('/mnt/data')
SRC=ROOT/'MagiciansQuest-VietHoa-Checkpoint-103.zip'
OUT=ROOT/'MagiciansQuest-VietHoa-Checkpoint-104.zip'
STAGE=ROOT/'MQ104'; STAGE.mkdir(exist_ok=True)
OLD='MagiciansQuest_103/'
NEW='MagiciansQuest_104/'
TALK='translation/04-thoai/talkfigs__0eng__data__'
TARGETS=['0044.015','0044.016']
NEXT=['0044.017','0044.018']
LEAD=re.compile(r"^(?:\$(?:024|023|022|034|040|004)(?:'[-\d]+)*;)+")
TOKEN=re.compile(r"\$\d{3}(?:'[-\d]+)*;")
with zipfile.ZipFile(SRC) as zin:
    assert zin.testzip() is None
    oldfiles={n.removeprefix(OLD):zin.read(n) for n in zin.namelist() if n.startswith(OLD) and not n.endswith('/')}
jsonlnames=[n for n in oldfiles if n.startswith('translation/') and n.endswith('.jsonl')]
assert len(jsonlnames)==501
rowsby={n:[json.loads(line) for line in oldfiles[n].decode('utf8').splitlines() if line.strip()] for n in jsonlnames}
assert sum(map(len,rowsby.values()))==55976
prior_count=sum(sum(r.get('vi') is not None for r in rows) for rows in rowsby.values())
assert prior_count==26615,prior_count
prior=collections.defaultdict(collections.Counter)
for n,rows in rowsby.items():
    if n in {TALK+k+'.jsonl' for k in TARGETS}:continue
    for row in rows:
        if isinstance(row.get('en'),str) and isinstance(row.get('vi'),str):
            prior[LEAD.sub('',row['en'])][LEAD.sub('',row['vi'])]+=1
unique={}
for k in TARGETS:
    n=TALK+k+'.jsonl';rows=rowsby[n]
    assert len(rows)==120 and all(r.get('vi') is None for r in rows),(n,len(rows))
    for row in rows:
        key=LEAD.sub('',row['en']);unique.setdefault(key,0);unique[key]+=1
assert len(unique)==96,len(unique)
missing={i for i,en in enumerate(unique,1) if en not in prior}
assert missing==set(MANUAL) and len(missing)==11,(missing,set(MANUAL))
translations={};report=[]
for i,en in enumerate(unique,1):
    is_new=i in MANUAL
    vi=MANUAL[i] if is_new else prior[en].most_common(1)[0][0]
    assert vi and isinstance(vi,str) and '\n' not in vi
    assert TOKEN.findall(en)==TOKEN.findall(vi),(i,'token mismatch',en,vi)
    assert unicodedata.normalize('NFC',vi)==vi,(i,'NFC')
    assert vi.count('▼')<=3,(i,'too many breaks',vi)
    for seg in vi.split('▼'):
        static=TOKEN.sub('',seg)
        assert len(static)<=34,(i,'overlong',len(static),static)
        assert not re.search('[“”‘’—–«»…\u3000]',static),(i,'punctuation',static)
    translations[en]=vi
    report.append((i,en,vi,'DỊCH MỚI' if is_new else 'TÁI DÙNG',unique[en]))
patch={};changed=[]
for key in TARGETS:
    n=TALK+key+'.jsonl'; rows=[]
    for old in rowsby[n]:
        row=old.copy(); lead=LEAD.match(row['en'])
        row['vi']=(lead.group(0) if lead else '')+translations[LEAD.sub('',row['en'])]
        assert TOKEN.findall(row['en'])==TOKEN.findall(row['vi']),row['id']
        assert {k:v for k,v in row.items() if k!='vi'}=={k:v for k,v in old.items() if k!='vi'},row['id']
        rows.append(row)
    data=''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in rows).encode('utf8')
    patch[n]=data
    (STAGE/(key+'.jsonl')).write_bytes(data)
    short=key.replace('.','_')
    (STAGE/('manual_'+short+'.tsv')).write_text('id\ten\tvi\tctx\n'+''.join(f"{r['id']}\t{r['en']}\t{r['vi']}\t{r.get('ctx','')}\n" for r in rows),encoding='utf8')
    (STAGE/('vi_'+short+'.txt')).write_text(''.join(f"{r['id']}\t{r['vi']}\n" for r in rows),encoding='utf8')
    changed.extend(rows)
assert len(changed)==240 and len({r['id'] for r in changed})==240
(STAGE/'DELTA-104.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in changed),encoding='utf8')
(STAGE/'unique_104.tsv').write_text('index\ten_body\tvi_body\torigin\tpages\n'+''.join(f'{i}\t{en}\t{vi}\t{org}\t{cnt}\n' for i,en,vi,org,cnt in report),encoding='utf8')
next_files=[]
for key in NEXT:
    n=TALK+key+'.jsonl'
    if n in rowsby and rowsby[n] and all(r['vi'] is None for r in rowsby[n]):
        next_files.append((key,len(rowsby[n])))
        (STAGE/(key+'.jsonl')).write_bytes(oldfiles[n])
assert len(next_files)==2 and sum(n for _,n in next_files)==240,next_files
TOTAL=prior_count+240
PERCENT=TOTAL/55976*100
qa=f'''# QA — Magician's Quest Checkpoint 104 (10/11/2026)

- **PASS:** 501 JSONL / 55.976 records checked against checkpoint 103.
- **26.615 → {TOTAL:,} / 55.976 ({PERCENT:.2f}%)**: +240 NPC dialogue pages.
- `0044.015`: 120/120; `0044.016`: 120/120.
- **96 unique English dialogue bodies**: 85 reused and 11 newly localized.
- All 26.615 existing translations unchanged and 499 non-target JSONLs byte-identical.
- Original `id`, `en`, `ctx`, auxiliary keys and ordering preserved.
- NDS control token sequences preserved for all 240 new records (including `$503`, `$018`, `$032`).
- Unicode NFC, <=3 `▼` separators, max 34 static codepoints/segment, normal punctuation.
- ZIP CRC and full record counts validated. No changes outside Magician's Quest.
- **In-ROM display QA outstanding** (variable expansions and NDS glyph widths not yet tested).
- Next 105: `0044.017` and `0044.018` (120 + 120 pages), staged untranslated.
'''
cp=f'''# Magician's Quest — Checkpoint 104

**Date:** 10/11/2026
**Repository:** `ronvotri/VH-NDS` / `Magicians-Quest-Mysterious-Times/`.

- **+240 NPC pages** from `0044.015` and `0044.016` (120 each).
- Total **{TOTAL:,}/55.976 ({PERCENT:.2f}%)**; NPC **{23490+240:,}/52.608**.
- 96 distinct dialogue bodies: 85 reused, 11 newly localized.
- School gossip, magical research, friendship, devotion, rumors and dating.
- 501 JSONL QA PASS; 499 non-target files byte-identical, 26.615 previous translations preserved.
- Handoff: `DELTA-104.jsonl`, `unique_104.tsv`, EN–VI TSVs, `QA-104.md`, `build_104.py`, full ZIP in Library.
- Next 105: `0044.017` + `0044.018` (240 pages), already in full ZIP.
- **ROM display still untested.**
'''
(STAGE/'QA-104.md').write_text(qa,encoding='utf8')
(STAGE/'CHECKPOINT-2026-11-10-DOT-104.md').write_text(cp,encoding='utf8')
intro_rm=f'**Checkpoint mới nhất: 104 (10/11/2026) — {TOTAL:,}/55.976 ({PERCENT:.2f}%).** +240 trang thoại NPC (`0044.015`, `0044.016`); 11 mẫu dịch mới, 85 tái sử dụng; QA 501 JSONL PASS. Tiếp `0044.017`, `0044.018`. Xem `CHECKPOINT-2026-11-10-DOT-104.md`, `QA-104.md`.\n\n'
intro_bd=f'''## Checkpoint 104 — 10/11/2026

- +240 trang NPC `0044.015` và `0044.016`, tổng {TOTAL:,}/55.976 ({PERCENT:.2f}%).
- 96 mẫu thoại EN: 85 tái sử dụng, 11 biên dịch mới.
- Chủ đề tình bạn, tin đồn trường học, tình cảm và nghiên cứu ma thuật.
- 501 JSONL QA PASS; giữ nguyên 26.615 bản dịch cũ và 499 JSONL ngoài đợt.
- ZIP chứa EN–VI, delta, báo cáo QA, script dựng; chưa kiểm thử ROM NDS.
- Đợt 105: `0044.017` và `0044.018` (240 trang).

'''
(STAGE/'README.md').write_text(intro_rm+oldfiles['README.md'].decode('utf8'),encoding='utf8')
(STAGE/'BAN_GIAO.md').write_text(intro_bd+oldfiles['BAN_GIAO.md'].decode('utf8'),encoding='utf8')
for n in ['README.md','BAN_GIAO.md','QA-104.md','CHECKPOINT-2026-11-10-DOT-104.md','DELTA-104.jsonl','unique_104.tsv','manual_0044_015.tsv','manual_0044_016.tsv','vi_0044_015.txt','vi_0044_016.txt']:
    patch[n]=(STAGE/n).read_bytes()
patch['build_104.py']=Path(__file__).read_bytes()
patch['translate_104.py']=(ROOT/'translate_104.py').read_bytes()
allfiles={**oldfiles,**patch}
newrows={n:[json.loads(s) for s in allfiles[n].decode('utf8').splitlines() if s.strip()] for n in jsonlnames}
assert sum(map(len,newrows.values()))==55976
assert sum(sum(r.get('vi') is not None for r in rows) for rows in newrows.values())==TOTAL
for n in jsonlnames:
    if n not in {TALK+k+'.jsonl' for k in TARGETS}:assert allfiles[n]==oldfiles[n],n
with zipfile.ZipFile(OUT,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as zout:
    for name in sorted(allfiles):zout.writestr(NEW+name,allfiles[name])
with zipfile.ZipFile(OUT) as chk:
    assert chk.testzip() is None
    assert len(chk.namelist())==len(allfiles)
print(json.dumps({'checkpoint':104,'result':'PASS','files':len(allfiles),'jsonl':len(newrows),'total':55976,'translated':TOTAL,'added':240,'unique':len(unique),'new_phrases':len(MANUAL),'reused_phrases':len(unique)-len(MANUAL),'next':next_files,'sha256':hashlib.sha256(OUT.read_bytes()).hexdigest()},ensure_ascii=False))
