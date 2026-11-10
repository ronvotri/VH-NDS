#!/usr/bin/env python3
"""Magician's Quest NDS checkpoint 091 from full checkpoint 090 ZIP.

Preserves all prior JSONL records except `0043.012` and `0043.013`,
reuses already-approved exact EN-body translations, and applies a manually
reviewed EN→VI mapping for 44 unique English texts. Requires only stdlib.
"""
import collections, json, re, os, zipfile, hashlib, unicodedata
from pathlib import Path

ROOT=Path('/mnt/data')
PREV=ROOT/'MagiciansQuest-VietHoa-Checkpoint-090_2.zip'
OUT=ROOT/'MagiciansQuest-VietHoa-Checkpoint-091.zip'
STAGE=ROOT/'MQ091'/'stage'
STAGE.mkdir(exist_ok=True)
TARGETS=['0043.012','0043.013']
PREFIX='MagiciansQuest_090/'
NEW_PREFIX='MagiciansQuest_091/'
TALK='translation/04-thoai/talkfigs__0eng__data__'
LEAD=re.compile(r"^(?:\$(?:024|023|022|034|040|004)(?:'[-\d]+)*;)+")
TOKEN=re.compile(r"\$\d{3}(?:'[-\d]+)*;")

# These keys are positions in the ordered unique-English list of both files,
# printed by inspect.py. Every entry not in this map must exist verbatim in
# the old approved translation, so no generative fallback is allowed.
NEW={
 7: 'Cậu tính vượt mặt tớ▼hay gì hả?!$032;',
 9: 'Có ai đang cố▼vượt mặt tớ đây mà!',
 15: 'Này, tớ vừa nghe▼một người bạn kể chuyện.',
 18: 'Dám tình tứ trước mặt TỚ à?▼Coi chừng đấy nhé!$032;',
 23: 'Ủa, pháo hoa đâu rồi?$032;',
 32: 'Người ta đồn thế đấy.▼Thật không?$018\'1;',
 33: 'Bất ngờ chưa?$032;',
 34: 'Đã làm thì làm▼cho ra trò nhé!$032;',
 35: 'Chán phèo.',
 36: 'Ê, tớ vừa nghe▼tin đồn động trời!',
 37: 'Hai cậu vừa lén▼đi hẹn hò, đúng không?',
 38: 'Ngọt ngào rồi▼tay trong tay nữa chứ...',
 39: 'Dám làm thế trước mặt tớ▼thì coi chừng đấy!',
 40: 'Hai cậu cứ lén lút▼niệm bùa yêu, đúng không?',
 41: 'Hai cậu cứ suốt ngày▼nói lời mật ngọt▼với nhau, đúng chứ?',
 42: 'Nghe nói hai cậu▼ăn chung, còn đút▼cho nhau nữa...',
 43: 'Mà làm thế trước mặt tớ,▼tớ ăn sạch cả hai▼suất luôn đấy!',
 44: 'Rồi sao nữa?▼Định cưới nhau luôn hả?!',
 45: 'Hai cậu còn đọc▼nhật ký của nhau nữa à?',
 46: 'Đọc trước mặt tớ đi,▼rồi chuẩn bị viết▼di chúc luôn nhé!',
 47: 'Thế cậu là người hầu▼bé nhỏ của $503\'567; à?',
 48: 'Dám làm thế trước mặt tớ,▼tớ bắt cả hai▼hầu tớ luôn!',
 49: 'Giờ hai cậu tính▼rủ nhau bỏ trốn à?!',
 50: 'Đừng để tớ bắt gặp,▼không thì có cánh▼cũng khó thoát!',
 51: 'Hai cậu trao nhẫn▼cho nhau rồi à?',
 52: 'Hai cậu ở bên nhau▼đến tận sáng luôn hả?!',
 53: 'Hai cậu đang âm mưu▼trò đùa gì đấy?!',
 54: 'Lần sau phải rủ TỚ!▼Không thì khóc▼đến sáng đấy!',
 55: 'Nghe bảo hai cậu▼định chia tay à?',
 56: 'Muốn tâm sự thì nói tớ nghe,▼nhưng nói nhanh lên nhé.',
 57: 'Ê! Có tin đồn sốc lắm!▼Cậu biết gì không?',
 58: 'Nghe đồn hai cậu▼hẹn hò như người lớn...',
 59: 'Hai cậu làm gì đó▼bí mật lúc riêng tư...',
 60: 'Ê, đừng nhìn tớ!▼Tớ chỉ nghe đồn thôi!',
 61: 'Có bí mật gì▼thì mau kể tớ nghe!',
 62: 'Nghe đồn cậu▼hơi không chung thủy...',
 63: 'Có tin đồn hai cậu▼đang lén hẹn hò...',
 64: 'Thật không?▼Hai cậu định chia tay à?!',
 65: 'Ê, hai cậu ổn chứ?',
 66: 'Nghe nói $503\'567;▼đang giận dỗi kìa!',
 67: 'Nghe nói hai cậu▼đang cãi nhau.▼Yêu quá hóa cãi à?',
 68: 'Hai cậu chia tay▼thật rồi hả?!',
 69: 'Chia tay có đau không?▼Rốt cuộc cái gì▼bị chia ra vậy?',
 70: 'Hai cậu không thèm▼nói chuyện với nhau nữa à?',
}

with zipfile.ZipFile(PREV) as z:
    if z.testzip() is not None: raise AssertionError('Previous ZIP CRC failed')
    oldfiles={n[len(PREFIX):]:z.read(n) for n in z.namelist() if n.startswith(PREFIX) and not n.endswith('/')}
assert len(oldfiles)>1000,len(oldfiles)
jsonls=[n for n in oldfiles if n.startswith('translation/') and n.endswith('.jsonl')]
assert len(jsonls)==501,len(jsonls)
old_rows={name:[json.loads(line) for line in oldfiles[name].decode('utf-8').splitlines() if line.strip()] for name in jsonls}
assert sum(len(x) for x in old_rows.values())==55976
assert sum(sum(r.get('vi') is not None for r in x) for x in old_rows.values())==23529

count=collections.defaultdict(collections.Counter)
for name,rows in old_rows.items():
    if name in {TALK+k+'.jsonl' for k in TARGETS}:continue
    for r in rows:
        if r.get('vi') is not None:
            count[LEAD.sub('',r['en'])][LEAD.sub('',r['vi'])]+=1
uni=collections.OrderedDict()
for key in TARGETS:
    for r in old_rows[TALK+key+'.jsonl']:
        k=LEAD.sub('',r['en'])
        uni.setdefault(k,None)
assert len(uni)==70,len(uni)
newdict={}
for i,k in enumerate(uni,1):
    if i in NEW:
        assert not count[k],f'Marked new but earlier translation exists: {i}'
        newdict[k]=NEW[i]
    else:
        assert count[k],f'Missing old approved translation at unique index {i}'
        newdict[k]=count[k].most_common(1)[0][0]
assert len(NEW)==44
report=[]
for i,(en,vi) in enumerate(newdict.items(),1):
    assert isinstance(vi,str) and vi and '\n' not in vi,(i,vi)
    assert unicodedata.normalize('NFC',vi)==vi,(i,vi)
    assert TOKEN.findall(en)==TOKEN.findall(vi),(i,en,vi,'tokens')
    assert vi.count('▼')<=3,(i,vi,'break count')
    for segment in vi.split('▼'):
        static=TOKEN.sub('',segment)
        assert len(static)<=34,(i,len(static),static,vi)
        assert not re.search(r'[“”‘’—–«»…\u3000]',static),(i,vi,'nonstandard punctuation')
    report.append((i,en,vi,'MỚI' if i in NEW else 'TÁI DÙNG'))

patch={}
updated_rows=[]
for key in TARGETS:
    name=TALK+key+'.jsonl'; orig=old_rows[name]
    assert len(orig)==120 and all(r['vi'] is None for r in orig)
    new=[]
    for r in orig:
        nr=r.copy();nr['vi']=LEAD.match(r['en']).group(0)+newdict[LEAD.sub('',r['en'])] if LEAD.match(r['en']) else newdict[r['en']]
        assert TOKEN.findall(r['en'])==TOKEN.findall(nr['vi']),(r['id'],nr['vi'])
        assert len(nr['vi'].split('▼'))<=4
        new.append(nr)
    assert all({k:v for k,v in r.items() if k!='vi'}=={k:v for k,v in s.items() if k!='vi'} for r,s in zip(orig,new))
    patch[name]=(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in new)).encode('utf8')
    (STAGE/(key+'.jsonl')).write_bytes(patch[name])
    (STAGE/('manual_'+key.replace('.','_')+'.tsv')).write_text('id\ten\tvi\tctx\n'+''.join(f"{r['id']}\t{r['en']}\t{r['vi']}\t{r.get('ctx','')}\n" for r in new),encoding='utf8')
    (STAGE/('vi_'+key.replace('.','_')+'.txt')).write_text(''.join(r['id']+'\t'+r['vi']+'\n' for r in new),encoding='utf8')
    updated_rows.extend(new)
assert len(updated_rows)==240
assert len({r['id'] for r in updated_rows})==240
assert set(patch)=={TALK+x+'.jsonl' for x in TARGETS}
assert all(n not in patch or patch[n]!=oldfiles[n] for n in patch)
(STAGE/'DELTA-091.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in updated_rows),encoding='utf8')
(STAGE/'unique_091.tsv').write_text('index\ten_body\tvi_body\torigin\n'+''.join(f'{i}\t{en}\t{vi}\t{origin}\n' for i,en,vi,origin in report),encoding='utf8')

# Prepare untouched 120-row sources for the following 092 batch.
for key in ['0043.014','0043.015']:
    fn=TALK+key+'.jsonl'
    assert len(old_rows[fn])==120 and all(r['vi'] is None for r in old_rows[fn]),key
    (STAGE/(key+'.jsonl')).write_bytes(oldfiles[fn])

qa='''# QA — Magician's Quest Checkpoint 091 (10/11/2026)

- **PASS:** 501 JSONL / 55,976 records; checkpoint 090 baseline.
- **23,529 → 23,769 / 55,976 (42.46%)**: +240 NPC pages.
- 0043.012: 120/120; 0043.013: 120/120.
- **70 unique EN patterns:** 26 reused from earlier, 44 manually translated.
- Existing 23,529 translations unchanged; 499 non-target JSONLs byte-identical.
- 240 target rows: fields, English, IDs, context, order preserved, VI filled.
- Exact game token order preserved ($503/$535/$538/$018/$032 etc.).
- Unicode NFC, at most 3 ▼ breaks and <=34 static codepoints per segment checked.
- ZIP CRC PASS, all 501 JSONL parsed, total count unchanged; script reproducible.
- **ROM font width / variable expansion not yet verified in emulator.**
- Next 092: 0043.014, 0043.015 (120 untranslated pages each).
'''
cp='''# Magician's Quest — Checkpoint 091

**Date:** 10/11/2026
**Repository:** `ronvotri/VH-NDS` / `Magicians-Quest-Mysterious-Times/`

- Translated 240 NPC pages from `0043.012` and `0043.013` (120 each).
- Total **23,769/55,976 (42.46%)**, NPC **20,644/52,608**.
- 70 unique texts: 44 new translations, 26 previously approved EN-body translations reused.
- Dialogue: rumors, dating, breakup and NPC reactions; youthful, consistent tớ–cậu speech.
- Full 501 JSONL QA PASS, all old 23,529 translations preserved.
- Files: `DELTA-091.jsonl`, `unique_091.tsv`, two manual EN–VI TSVs,
  `QA-091.md`, `build_091.py`, full 091 ZIP stored in Library.
- Next 092: `0043.014` and `0043.015` (240 untranslated pages; staged on GitHub).
- ROM font and dynamic substitution not yet tested.
'''
(STAGE/'QA-091.md').write_text(qa,encoding='utf8')
(STAGE/'CHECKPOINT-2026-11-10-DOT-91.md').write_text(cp,encoding='utf8')
readme_intro='**Checkpoint mới nhất: 091 (10/11/2026) — 23.769/55.976 (42,46%).** +240 NPC (`0043.012`, `0043.013`); 44 mẫu dịch mới, 26 mẫu tái sử dụng; QA 501 JSONL PASS. Xem `CHECKPOINT-2026-11-10-DOT-91.md` và `QA-091.md`. Tiếp `0043.014`, `0043.015` (240 trang).\n\n'
handoff_intro='''## Checkpoint 091 — 10/11/2026

- +240 trang NPC `0043.012` và `0043.013`; tổng 23.769/55.976 (42,46%), NPC 20.644/52.608.
- 70 mẫu EN riêng: 44 dịch mới, 26 tái sử dụng. QA 501 JSONL PASS; giữ nguyên 23.529 bản dịch trước.
- ZIP đầy đủ, bảng EN–VI, delta, QA và script bàn giao trong Thư viện/GitHub; chưa kiểm thử ROM.
- Đợt 092: `0043.014` + `0043.015` (120 trang mỗi tệp).

'''
patch['README.md']=(readme_intro+oldfiles['README.md'].decode('utf8')).encode('utf8')
patch['BAN_GIAO.md']=(handoff_intro+oldfiles['BAN_GIAO.md'].decode('utf8')).encode('utf8')
for fn in ['README.md','BAN_GIAO.md']:(STAGE/fn).write_bytes(patch[fn])

for fn in ['QA-091.md','CHECKPOINT-2026-11-10-DOT-91.md','DELTA-091.jsonl','unique_091.tsv','manual_0043_012.tsv','manual_0043_013.tsv','vi_0043_012.txt','vi_0043_013.txt']:
    assert fn not in oldfiles,fn
    patch[fn]=(STAGE/fn).read_bytes()
# This script is itself part of ZIP/repo for reconstructing the checkpoint.
patch['build_091.py']=Path(__file__).read_bytes()

def check_zip_record(z):
    names=z.namelist()
    assert len(names)==len(set(names))
    assert z.testzip() is None
    checknames=[n for n in names if n.startswith(NEW_PREFIX+'translation/') and n.endswith('.jsonl')]
    assert len(checknames)==501,len(checknames)
    allr={}
    for fn in checknames:
        rows=[json.loads(x) for x in z.read(fn).decode('utf8').splitlines() if x.strip()]
        allr[fn.replace(NEW_PREFIX,'')]=rows
    assert sum(map(len,allr.values()))==55976
    assert sum(sum(r['vi'] is not None for r in rows) for rows in allr.values())==23769
    for fn in jsonls:
        if fn not in {TALK+k+'.jsonl' for k in TARGETS}:
            assert z.read(NEW_PREFIX+fn)==oldfiles[fn],f'Other file changed: {fn}'
    for fn in {TALK+k+'.jsonl' for k in TARGETS}:
        assert len(allr[fn])==120 and all(r['vi'] is not None for r in allr[fn])
    return len(names)

with zipfile.ZipFile(OUT,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for filename,content in sorted({**oldfiles,**patch}.items()):
        z.writestr(NEW_PREFIX+filename,content)
with zipfile.ZipFile(OUT) as z:total=check_zip_record(z)
# Roundtrip: extract target file from ZIP and compare to staged.
for key in TARGETS:
    with zipfile.ZipFile(OUT) as z:
        assert z.read(NEW_PREFIX+TALK+key+'.jsonl')==(STAGE/(key+'.jsonl')).read_bytes()

print(json.dumps({'status':'PASS','files':total,'jsonl':501,'records':55976,'translated':23769,'new_pages':240,'unique_en':70,'new_unique':len(NEW),'reused_unique':70-len(NEW),'zip':str(OUT),'size':OUT.stat().st_size,'sha256':hashlib.sha256(OUT.read_bytes()).hexdigest()},ensure_ascii=False))