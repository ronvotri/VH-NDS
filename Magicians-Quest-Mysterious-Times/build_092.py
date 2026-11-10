#!/usr/bin/env python3
"""Rebuild Magician's Quest NDS checkpoint 092 from full 091 ZIP, stdlib only.
Every page translation comes either from a manually reviewed English-body mapping
or from the most common already-approved matching translated body. Strict token QA.
"""
import collections, json, re, zipfile, hashlib, unicodedata
from pathlib import Path
ROOT=Path('/mnt/data')
PREV=ROOT/'MagiciansQuest-VietHoa-Checkpoint-091.zip'
OUT=ROOT/'MagiciansQuest-VietHoa-Checkpoint-092.zip'
STAGE=ROOT/'MQ092'/'stage'
STAGE.mkdir(parents=True,exist_ok=True)
PREFIX='MagiciansQuest_091/'
NEW_PREFIX='MagiciansQuest_092/'
TALK='translation/04-thoai/talkfigs__0eng__data__'
TARGETS=['0043.014','0043.015']
LEAD=re.compile(r"^(?:\$(?:024|023|022|034|040|004)(?:'[-\d]+)*;)+")
TOKEN=re.compile(r"\$\d{3}(?:'[-\d]+)*;")
# Numbered positions in the stable ordered English unique-body list of target files.
# Nonlisted entries are required to have an exact existing translated English body.
NEW={
 1:'Tại cả hai cứng đầu quá!▼Để tớ chỉ cách▼nói chuyện bằng nắm đấm!',
 2:'Đang có chuyện thú vị▼về cậu lan khắp nơi đấy!',
 3:'Nghe nói hai cậu▼đang tranh giành▼cùng một người...',
 4:'Tranh giành người khác à?▼Hợp gu tớ quá!',
 5:'Hay đấy!▼Đấu tay ba luôn đi!',
 6:'Hai cậu đính hôn rồi à?',
 7:'Giờ tính cưới luôn hả?▼Đường dài phía trước đấy.',
 9:'Gần đây cậu thi▼bắt côn trùng hả?',
 10:'Nghe vui đấy!',
 11:'Sao không rủ tớ?▼Tớ bực như bị▼bọ đốt ấy!',
 12:'Dạo này cậu thi▼câu cá với ai à?',
 13:'Sao chẳng rủ tớ?▼Chuyện này có mùi▼hơi tanh đấy...',
 14:'Nghe nói hai cậu thân lắm,▼sắp lập nhóm song ca luôn...',
 15:'Hai cậu hợp nhau đến mức▼người ta bảo chắc là▼sinh đôi thất lạc...',
 16:'Hai cậu suốt ngày đi cùng,▼nghe đồn sắp dọn▼về ở chung đấy...',
 19:'Thân nhau thì tốt,▼nhưng người ta đồn▼hai cậu thân hơi quá đấy.',
 21:'Nghe đồn cậu chẳng▼chơi với ai ngoài▼$503\'567;...',
 22:'Tớ nghi có chuyện▼từ lâu rồi mà...',
 23:'Cãi nhau với người yêu▼rồi bị đá phải không?!',
 24:'Nghe bảo sau chia tay▼cậu định lên đường▼chữa lành trái tim.',
 25:'Nghe bảo cậu sắp▼chuyển trường...',
 26:'Mất một người bạn▼thì buồn lắm.',
 27:'Cậu nhất định phải đi sao?',
 28:'Nghe đồn cậu đang niệm bùa▼để thống trị cả thế giới...',
 29:'Nghe đồn cậu là▼người ngoài hành tinh...',
 30:'Nghe đồn có ma▼đang ám cậu...',
 31:'Cậu giấu chuyện gì▼đúng không?',
 32:'Người ta đồn cậu là▼anh hùng trong truyền thuyết...',
 33:'Nghe đồn cậu▼đang thích ai đó...',
 34:'Nghe đồn cậu▼thật ra là con bọ...',
 35:'Hay quá! Giẫm bẹp cậu▼giờ dễ hơn bao giờ hết!',
 36:'Nghe bảo cậu mộng du▼rồi rơi tõm xuống sông...',
 37:'Người ta đồn▼cậu kỳ quặc lắm...',
 38:'Nghe nói cậu▼sợ bị cù lắm...',
 39:'Nghe đồn cậu giàu tới mức▼thức khuya đếm tiền mãi...',
 40:'Hừm... Chắc tớ phải▼tăng phí bảo kê thôi...',
 41:'Nghe đồn cậu làm hải tặc▼đi săn kho báu rồi!',
 42:'Nghe đồn cậu đào hố▼trong rừng rồi khóc...',
 43:'Sao thế? Muốn khóc thêm▼thì tớ giúp được đấy...',
 44:'Tớ nghe chuyện▼về cậu rồi nhé...',
 45:'Cậu lại phá được▼vụ án nữa à?',
 46:'Không thể tin nổi!',
 47:'Sao không phải là tớ?▼Nắm đấm tớ▼mạnh nhất thế giới mà!',
 49:'Thôi thì...▼cố hết sức là được.',
 50:'Nghe nói cậu▼ngoan lắm đấy...',
 51:'Giờ cậu định làm▼đại ca giang hồ hả?!',
 52:'Chúc may mắn!▼Đừng thua nhé!▼Tớ sẽ cổ vũ cho cậu!',
 53:'Tớ nghe đồn▼ở trường đấy!',
 59:'Bọn tớ vừa tán dóc▼một chút. Cậu phải nghe này!'
}
with zipfile.ZipFile(PREV) as z:
    assert z.testzip() is None,'Baseline ZIP CRC invalid'
    oldfiles={n[len(PREFIX):]:z.read(n) for n in z.namelist() if n.startswith(PREFIX) and not n.endswith('/')}
assert len(oldfiles)>=1350,len(oldfiles)
jsonls=[n for n in oldfiles if n.startswith('translation/') and n.endswith('.jsonl')]
assert len(jsonls)==501,len(jsonls)
old_rows={n:[json.loads(t) for t in oldfiles[n].decode('utf8').splitlines() if t.strip()] for n in jsonls}
assert sum(map(len,old_rows.values()))==55976
assert sum(sum(r.get('vi') is not None for r in v) for v in old_rows.values())==23769
oldcount=collections.defaultdict(collections.Counter)
for n,rows in old_rows.items():
    if n in {TALK+x+'.jsonl' for x in TARGETS}:continue
    for r in rows:
        if r.get('vi') is not None and isinstance(r.get('en'),str):
            oldcount[LEAD.sub('',r['en'])][LEAD.sub('',r['vi'])]+=1
unique=collections.OrderedDict()
for key in TARGETS:
    rows=old_rows[TALK+key+'.jsonl']
    assert len(rows)==120 and all(r.get('vi') is None for r in rows)
    for r in rows:unique.setdefault(LEAD.sub('',r['en']),None)
assert len(unique)==62,len(unique)
assert len(NEW)==49,len(NEW)
translation={}
report=[]
for i,en in enumerate(unique,1):
    if i in NEW:
        assert not oldcount[en],f'Unique index {i}: formerly translated; should reuse instead'
        vi=NEW[i]
        origin='MỚI'
    else:
        assert oldcount[en],f'Unique index {i}: prior translation unavailable'
        vi=oldcount[en].most_common(1)[0][0]
        origin='TÁI DÙNG'
    assert vi and '\n' not in vi,(i,vi)
    assert unicodedata.normalize('NFC',vi)==vi,(i,'unicode')
    assert TOKEN.findall(en)==TOKEN.findall(vi),(i,'changed tokens',en,vi)
    assert vi.count('▼')<=3,(i,'breaks',vi)
    for seg in vi.split('▼'):
        static=TOKEN.sub('',seg)
        assert len(static)<=34,(i,len(static),static)
        assert not re.search('[“”‘’—–«»…\u3000]',static),(i,'punctuation')
    report.append((i,en,vi,origin));translation[en]=vi
assert sum(r[3]=='MỚI' for r in report)==49
patch={};changed=[]
for key in TARGETS:
    n=TALK+key+'.jsonl';orig=old_rows[n]
    new=[]
    for r in orig:
        rr=r.copy();lead=LEAD.match(r['en']);rr['vi']=(lead.group(0) if lead else '')+translation[LEAD.sub('',r['en'])]
        assert TOKEN.findall(r['en'])==TOKEN.findall(rr['vi']),(r['id'],rr['vi'])
        assert {k:v for k,v in rr.items() if k!='vi'}=={k:v for k,v in r.items() if k!='vi'}
        new.append(rr)
    payload=(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in new)).encode('utf8')
    patch[n]=payload
    (STAGE/(key+'.jsonl')).write_bytes(payload)
    name=key.replace('.','_')
    (STAGE/('manual_'+name+'.tsv')).write_text('id\ten\tvi\tctx\n'+''.join(f"{r['id']}\t{r['en']}\t{r['vi']}\t{r.get('ctx','')}\n" for r in new),encoding='utf8')
    (STAGE/('vi_'+name+'.txt')).write_text(''.join(r['id']+'\t'+r['vi']+'\n' for r in new),encoding='utf8')
    changed.extend(new)
assert len(changed)==240 and len({r['id'] for r in changed})==240
(STAGE/'DELTA-092.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in changed),encoding='utf8')
(STAGE/'unique_092.tsv').write_text('index\ten_body\tvi_body\torigin\n'+''.join(f'{i}\t{en}\t{vi}\t{origin}\n' for i,en,vi,origin in report),encoding='utf8')
# Stage the untouched following 093 sources.
for key in ['0043.016','0043.017']:
    fn=TALK+key+'.jsonl'
    assert len(old_rows[fn])==120 and all(r['vi'] is None for r in old_rows[fn]),key
    (STAGE/(key+'.jsonl')).write_bytes(oldfiles[fn])
qa='''# QA — Magician's Quest Checkpoint 092 (10/11/2026)

- **PASS:** 501 JSONL / 55,976 records, checkpoint 091 baseline.
- **23,769 -> 24,009 / 55,976 (42.89%)**: +240 NPC pages.
- `0043.014`: 120/120; `0043.015`: 120/120.
- **62 unique English patterns:** 13 reused from earlier, 49 newly translated.
- Existing 23,769 translations unchanged; 499 non-target JSONLs byte-identical.
- 240 target rows: `id`, `en`, `ctx`, other fields and ordering preserved.
- Exact NDS control tokens preserved, including dynamic `$503`, `$530`, `$532`, `$531`.
- Unicode NFC, at most 3 `▼` breaks, max 34 static codepoints per segment.
- ZIP CRC PASS; all 501 JSONL parse; translated count 24,009.
- **Not ROM tested:** variable expansion and font width require emulator/hardware verification.
- Next batch 093: `0043.016`, `0043.017` (120 untranslated pages each).
'''
cp='''# Magician's Quest — Checkpoint 092

**Date:** 10/11/2026
**Repository:** `ronvotri/VH-NDS` / `Magicians-Quest-Mysterious-Times/`.

- Translated 240 NPC pages from `0043.014` and `0043.015` (120 each).
- Total **24,009/55,976 (42.89%)**; NPC **20,884/52,608**.
- 62 unique EN texts: 49 newly translated, 13 reused exactly from approved past dialogue.
- Rumors about friendship, engagement, fishing, bug-catching, transferring schools, superheroes, and treasure hunting.
- QA 501 JSONL PASS; no old translations or other game files changed.
- Handoff: `DELTA-092.jsonl`, `unique_092.tsv`, two EN–VI TSVs, `QA-092.md`, `build_092.py`, ZIP in Library.
- Next 093: `0043.016`, `0043.017` (240 pages) untranslated and staged.
- ROM font and dynamic substitution not yet tested.
'''
(STAGE/'QA-092.md').write_text(qa,encoding='utf8')
(STAGE/'CHECKPOINT-2026-11-10-DOT-92.md').write_text(cp,encoding='utf8')
rm_intro='**Checkpoint mới nhất: 092 (10/11/2026) — 24.009/55.976 (42,89%).** +240 NPC (`0043.014`, `0043.015`); 49 mẫu mới, 13 mẫu tái dùng; QA 501 JSONL PASS. Tiếp `0043.016`, `0043.017` (240 trang). Xem `CHECKPOINT-2026-11-10-DOT-92.md` và `QA-092.md`.\n\n'
bd_intro='''## Checkpoint 092 — 10/11/2026

- +240 trang NPC `0043.014` và `0043.015`; tổng 24.009/55.976 (42,89%), NPC 20.884/52.608.
- 62 mẫu EN riêng: 49 dịch mới, 13 tái dùng. QA 501 JSONL PASS; giữ nguyên 23.769 bản dịch trước.
- ZIP đầy đủ, bảng EN–VI, delta, QA và script trong Thư viện/GitHub; chưa kiểm thử ROM.
- Đợt 093: `0043.016` và `0043.017` (120 trang mỗi tệp).

'''
patch['README.md']=(rm_intro+oldfiles['README.md'].decode('utf8')).encode('utf8')
patch['BAN_GIAO.md']=(bd_intro+oldfiles['BAN_GIAO.md'].decode('utf8')).encode('utf8')
for fn in ['README.md','BAN_GIAO.md']:(STAGE/fn).write_bytes(patch[fn])
for fn in ['QA-092.md','CHECKPOINT-2026-11-10-DOT-92.md','DELTA-092.jsonl','unique_092.tsv','manual_0043_014.tsv','manual_0043_015.tsv','vi_0043_014.txt','vi_0043_015.txt']:
    assert fn not in oldfiles,fn
    patch[fn]=(STAGE/fn).read_bytes()
patch['build_092.py']=Path(__file__).read_bytes()
with zipfile.ZipFile(OUT,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for filename,payload in sorted({**oldfiles,**patch}.items()):z.writestr(NEW_PREFIX+filename,payload)
with zipfile.ZipFile(OUT) as z:
    names=z.namelist()
    assert len(names)==len(set(names))
    assert z.testzip() is None
    checks=[n for n in names if n.startswith(NEW_PREFIX+'translation/') and n.endswith('.jsonl')]
    assert len(checks)==501
    total=done=0
    target_names={TALK+k+'.jsonl' for k in TARGETS}
    for n in jsonls:
        if n not in target_names:assert z.read(NEW_PREFIX+n)==oldfiles[n],f'Changed outside target: {n}'
        rows=[json.loads(t) for t in z.read(NEW_PREFIX+n).decode('utf8').splitlines() if t.strip()]
        total+=len(rows);done+=sum(r.get('vi') is not None for r in rows)
        if n in target_names:assert len(rows)==120 and all(r.get('vi') is not None for r in rows)
    assert total==55976 and done==24009,(total,done)
    assert all(z.read(NEW_PREFIX+TALK+key+'.jsonl')==(STAGE/(key+'.jsonl')).read_bytes() for key in TARGETS)
print(json.dumps({'status':'PASS','zip':str(OUT),'bytes':OUT.stat().st_size,'files':len(names),'jsonl':501,'total':total,'translated':done,'new_pages':240,'unique':len(unique),'new_unique':len(NEW),'reused_unique':len(unique)-len(NEW),'sha256':hashlib.sha256(OUT.read_bytes()).hexdigest()},ensure_ascii=False))