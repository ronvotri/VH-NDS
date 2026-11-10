#!/usr/bin/env python3
"""Build MQ checkpoint 106 from checkpoint105; four target files, 436 pages."""
import collections, hashlib, json, re, unicodedata, zipfile, datetime, textwrap
from pathlib import Path
from translate_106 import translations as MANUAL
ROOT=Path('/mnt/data'); SRC=ROOT/'MagiciansQuest-VietHoa-Checkpoint-105.zip'; OUT=ROOT/'MagiciansQuest-VietHoa-Checkpoint-106.zip'; STAGE=ROOT/'MQ106';STAGE.mkdir(exist_ok=True)
OLD='MagiciansQuest_105/';NEW='MagiciansQuest_106/'
TALK='translation/04-thoai/talkfigs__0eng__data__'
TARGETS=['0044.019','0044.020','0044.021','0044.022']
NEXT=['0045.001','0045.002']
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
assert prior_count==27095,prior_count
prior=collections.defaultdict(collections.Counter)
for n,rows in rowsby.items():
    if n in {TALK+k+'.jsonl' for k in TARGETS}:continue
    for row in rows:
        if isinstance(row.get('en'),str) and isinstance(row.get('vi'),str):
            prior[LEAD.sub('',row['en'])][LEAD.sub('',row['vi'])]+=1
unique={}
for key in TARGETS:
    n=TALK+key+'.jsonl';rows=rowsby[n]
    assert len(rows)==(76 if key.endswith('022') else 120) and all(r.get('vi') is None for r in rows),(n,len(rows))
    for r in rows:
        e=LEAD.sub('',r['en']); unique[e]=unique.get(e,0)+1
assert len(unique)==436,len(unique)
missing={i for i,en in enumerate(unique,1) if en not in prior}
assert missing==set(MANUAL) and len(missing)==432,(missing-set(MANUAL),set(MANUAL)-missing)

# Tokens are indivisible. A soft wrap may only occur between words, never inside tokens or names.
# Most body text already has no explicit line-breaks; lay it out for NDS four-line page.
# We use a conservative max 31 static Unicode codepoints per line, ignoring control codes.
# For lines with variable substitutions, target is <=26 static characters.
def wrap_vi(s,desired=30,maxlen=34):
    s=unicodedata.normalize('NFC',s.replace('▼',' '))
    assert '\n' not in s
    words=s.split()
    if not words:return s
    def static_len(text):return len(TOKEN.sub('',text))
    # Tokens by themselves have dynamic display widths; reserve space on these lines.
    limits=[]
    i=0
    while i<len(words):
        current=[]
        while i<len(words):
            cand=' '.join(current+[words[i]])
            # Keep colored tokens with their text rather than separating prefixes when possible.
            # Dynamic placeholders (name/item) reserve extra room to avoid visual overflow.
            limit=desired
            if re.search(r"\$(?:500|501|502|503|504|505|506|507)(?:'[-\d]+)*;",cand):limit=26
            if not current or static_len(cand)<=limit:
                current.append(words[i]);i+=1
            else:break
        limits.append(' '.join(current))
    if len(limits)>4:
        # Repaginate optimally into four lines of <=34 chars, prioritizing short even lines.
        import functools
        @functools.lru_cache(None)
        def best(start,lines):
            if start==len(words):return (0,[])
            if lines==0:return (10**9,[])
            win=(10**9,[])
            for end in range(start+1,len(words)+1):
                line=' '.join(words[start:end]); n=static_len(line)
                if n>maxlen:break
                if re.search(r"\$(?:500|501|502|503|504|505|506|507)(?:'[-\d]+)*;",line) and n>31:continue
                nxt,b=best(end,lines-1)
                score=(max(0,n-31)*16)+((maxlen-n)**2)//8+nxt
                if score<win[0]:win=(score,[line]+b)
            return win
        val,better=best(0,4)
        if val>=10**9:
            raise ValueError('UNWRAPPABLE: '+repr(s)+' initial '+repr(limits))
        limits=better
    return '▼'.join(limits)

translations={};report=[]
for i,en in enumerate(unique,1):
    new=i in MANUAL
    raw=MANUAL[i] if new else prior[en].most_common(1)[0][0]
    vi=wrap_vi(raw) if new else raw
    assert vi and isinstance(vi,str) and '\n' not in vi
    assert TOKEN.findall(en)==TOKEN.findall(vi),(i,'token mismatch',en,vi)
    assert unicodedata.normalize('NFC',vi)==vi,(i,'NFC')
    assert vi.count('▼')<=3,(i,'too many breaks',vi)
    for seg in vi.split('▼'):
        stat=TOKEN.sub('',seg)
        assert len(stat)<=34,(i,'overlong',len(stat),stat)
        assert not re.search('[“”‘’—–«»…\u3000]',stat),(i,'punctuation',stat)
    translations[en]=vi
    report.append((i,en,vi,'DỊCH MỚI' if new else 'TÁI DÙNG',unique[en]))
patch={};changed=[]
for key in TARGETS:
    n=TALK+key+'.jsonl';rows=[]
    for old in rowsby[n]:
        row=old.copy(); m=LEAD.match(row['en']); prefix=m.group(0) if m else ''
        row['vi']=prefix+translations[LEAD.sub('',row['en'])]
        assert TOKEN.findall(row['en'])==TOKEN.findall(row['vi']),row['id']
        assert {k:v for k,v in row.items() if k!='vi'}=={k:v for k,v in old.items() if k!='vi'},row['id']
        rows.append(row)
    patch[n]=''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in rows).encode('utf8')
    (STAGE/(key+'.jsonl')).write_bytes(patch[n])
    short=key.replace('.','_')
    (STAGE/('manual_'+short+'.tsv')).write_text('id\ten\tvi\tctx\n'+''.join(f"{r['id']}\t{r['en']}\t{r['vi']}\t{r.get('ctx','')}\n" for r in rows),encoding='utf8')
    (STAGE/('vi_'+short+'.txt')).write_text(''.join(f"{r['id']}\t{r['vi']}\n" for r in rows),encoding='utf8')
    changed.extend(rows)
assert len(changed)==436 and len({r['id'] for r in changed})==436
(STAGE/'DELTA-106.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in changed),encoding='utf8')
(STAGE/'unique_106.tsv').write_text('index\ten_body\tvi_body\torigin\tpages\n'+''.join(f'{i}\t{en}\t{vi}\t{org}\t{cnt}\n' for i,en,vi,org,cnt in report),encoding='utf8')
next_files=[]
for key in NEXT:
    n=TALK+key+'.jsonl'
    if n in rowsby and rowsby[n] and all(r['vi'] is None for r in rowsby[n]):
        next_files.append((key,len(rowsby[n]))); (STAGE/(key+'.jsonl')).write_bytes(oldfiles[n])
TOTAL=prior_count+436;PERCENT=100*TOTAL/55976
qa=f'''# QA — Magician's Quest Checkpoint 106 (11/11/2026)

- **PASS:** 501 JSONL / 55,976 records checked against checkpoint 105.
- **27,095 → {TOTAL:,} / 55,976 ({PERCENT:.2f}%)**: +436 NPC dialogue pages, all remaining pages from `0044`.
- `0044.019`: 120/120; `0044.020`: 120/120; `0044.021`: 120/120; `0044.022`: 76/76.
- **436 unique English dialogue bodies**: 4 reused and 432 manually localized.
- All 27,095 existing translations unchanged and 497 non-target JSONLs byte-identical.
- Original `id`, `en`, `ctx`, auxiliary keys and ordering preserved.
- Exact NDS control token sequences preserved for all 436 added records.
- Unicode NFC, max 3 `▼` separators, max 34 static codepoints per segment, ordinary punctuation.
- Full ZIP CRC, JSONL parsing, unique IDs, record count and translated count validated.
- **Not yet tested in ROM:** font widths, variable expansions, natural line breaks, and game rendering on NDS/emulator.
- Next: `0045.001` and `0045.002`, plus later `0045` files. English sources included in ZIP.
'''
cp=f'''# Magician's Quest — Checkpoint 106

**Date:** 11/11/2026
**Repository:** `ronvotri/VH-NDS` / `Magicians-Quest-Mysterious-Times/`.

- +436 NPC pages across `0044.019`, `0044.020`, `0044.021`, `0044.022` — finished remaining `0044` sequence.
- Total **{TOTAL:,}/55,976 ({PERCENT:.2f}%)**; NPC **{23970+436:,}/52,608**.
- 436 distinct English dialogue bodies: 4 reused, 432 manually localized.
- Themes: school bell, ghosts, homunculi, mermaids, Siren, yeti, forbidden tome, dreams, other worlds, Christmas, UFO, mystery circles, golem, friendship and magical puzzles.
- QA PASS for 501 JSONLs; 497 non-target JSONLs byte-identical; all 27,095 prior translated entries preserved.
- Handoff: `DELTA-106.jsonl`, `unique_106.tsv`, four EN–VI TSVs, `QA-106.md`, `translate_106.py`, `build_106.py`, full ZIP.
- Next 107: start `0045.001` onward; English sources staged in ZIP.
- **In-ROM display QA remains outstanding.**
'''
(STAGE/'QA-106.md').write_text(qa,encoding='utf8')
(STAGE/'CHECKPOINT-2026-11-11-DOT-106.md').write_text(cp,encoding='utf8')
intro_rm=f'**Checkpoint mới nhất: 106 (11/11/2026) — {TOTAL:,}/55.976 ({PERCENT:.2f}%).** +436 thoại NPC (bốn tệp `0044.019`–`0044.022`); 432 mẫu dịch mới, 4 tái sử dụng; QA 501 JSONL PASS. Hoàn thành cụm `0044`, tiếp `0045.001` trở đi. Xem `CHECKPOINT-2026-11-11-DOT-106.md`, `QA-106.md`.\n\n'
intro_bd=f'''## Checkpoint 106 — 11/11/2026

- +436 trang NPC, gom cả 4 tệp `0044.019` đến `0044.022`, hoàn tất cụm 0044.
- Tổng {TOTAL:,}/55.976 ({PERCENT:.2f}%), 432 mẫu dịch tay, 4 mẫu tái dùng.
- Hội thoại học đường, yêu đương, ma quái, sinh vật huyền bí, phép thuật, câu đố, âm nhạc.
- QA 501 JSONL PASS; bảo toàn 27.095 bản dịch cũ, 497 JSONL ngoài đợt nguyên byte.
- ZIP chứa bảng EN–VI, delta, QA, script dựng; chưa thử hiển thị trên ROM thực tế.
- Đợt 107 sẽ tiếp cụm `0045`.

'''
(STAGE/'README.md').write_text(intro_rm+oldfiles['README.md'].decode('utf8'),encoding='utf8')
(STAGE/'BAN_GIAO.md').write_text(intro_bd+oldfiles['BAN_GIAO.md'].decode('utf8'),encoding='utf8')
for n in ['README.md','BAN_GIAO.md','QA-106.md','CHECKPOINT-2026-11-11-DOT-106.md','DELTA-106.jsonl','unique_106.tsv']:
    patch[n]=(STAGE/n).read_bytes()
for k in TARGETS:
    short=k.replace('.','_')
    for pref,suf in [('manual_','.tsv'),('vi_','.txt')]:
        name=pref+short+suf;patch[name]=(STAGE/name).read_bytes()
patch['build_106.py']=Path(__file__).read_bytes();patch['translate_106.py']=(ROOT/'translate_106.py').read_bytes()
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
print(json.dumps({'checkpoint':106,'result':'PASS','files':len(allfiles),'jsonl':len(newrows),'total':55976,'translated':TOTAL,'added':436,'unique':len(unique),'new_phrases':len(MANUAL),'reused_phrases':len(unique)-len(MANUAL),'next':next_files,'sha256':hashlib.sha256(OUT.read_bytes()).hexdigest()},ensure_ascii=False))
