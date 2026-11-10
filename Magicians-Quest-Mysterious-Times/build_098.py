#!/usr/bin/env python3
"""Rebuild Magician's Quest checkpoint 098 from checkpoint 097 ZIP; source-data only."""
import collections
import hashlib
import json
import re
import unicodedata
import zipfile
from pathlib import Path

ROOT=Path('/mnt/data')
PREV=ROOT/'MagiciansQuest-VietHoa-Checkpoint-097.zip'
OUT=ROOT/'MagiciansQuest-VietHoa-Checkpoint-098.zip'
STAGE=ROOT/'MQ098/stage'
STAGE.mkdir(exist_ok=True,parents=True)
OLD='MagiciansQuest_097/'
NEW='MagiciansQuest_098/'
TALK='translation/04-thoai/talkfigs__0eng__data__'
TARGETS=['0044.003','0044.004']
NEXT=['0044.005','0044.006']
LEAD=re.compile(r"^(?:\$(?:024|023|022|034|040|004)(?:'[-\d]+)*;)+")
TOKEN=re.compile(r"\$\d{3}(?:'[-\d]+)*;")

# New Vietnamese translation for unique English body indices, ordered by first appearance.
MANUAL={
 1:'Vẫn phải đến trường chứ!▼Trốn học là chuyện▼không thể chấp nhận!$079;',
 3:'Tớ đang nghĩ xem▼nên làm gì đây.$079;',
 4:'Xin lỗi, giờ cậu▼để tớ yên một lát nhé?$079;',
 5:'C-chào $500;...▼C-có chuyện gì thế?▼Cậu muốn nói chuyện à?$079;',
 6:'Nguy to rồi, $500;!▼Chạy đi... MAU LÊN!',
 47:'Tớ có nhiều bạn bè▼trong thị trấn lắm.',
 48:'Bọn tớ hay đi chơi▼và học cùng nhau.▼Vui cực!',
 49:'Này $500;, lần sau▼cậu tham gia cùng nhé?',
 50:'Hôm nay là ngày▼cuối cùng của năm rồi.',
 51:'Cứ đến dịp cuối năm...',
 52:'tớ lại muốn biết▼mình đã làm được▼điều gì đó...',
 53:'để háo hức đón▼năm mới nào!',
 54:'Tiệc trà mùa xuân▼diễn ra suôn sẻ nhỉ?',
 55:'Trà tớ pha ngon đến mức▼người khó tính nhất▼cũng phải khen!',
 56:'Bữa tiệc có bao kiểu người,▼mỗi người một tính,▼một gu thưởng trà...',
 57:'nên tớ pha trà dựa trên▼dữ liệu thu thập▼từ tất cả bọn họ.',
 58:'Nhưng chẳng ai chịu▼uống lúc trà đạt▼nhiệt độ hoàn hảo...',
 59:'thế là tớ bực mình▼và nổi cáu với họ.',
 60:'Phục vụ mọi người▼đúng là khó thật!',
 61:'$500;, cậu có thể▼vượt qua lễ hội▼ma quái không nhỉ?',
 62:'Tớ nhát gan lắm,▼nhưng mà...',
 63:'Tớ sẽ cố hết sức!',
 64:'Đôi khi hai chân tớ▼cứ chẳng chịu▼nghe lời mới khổ!',
 65:'Cậu có đi hái nấm không?',
 66:'Theo nghiên cứu của tớ,▼nấm thích nơi rất ẩm,▼nhưng mà...',
 67:'điều đó CÓ LUÔN▼đúng không nhỉ?',
 68:'Thế thì nấm phải mọc▼ngay dưới mắt▼mấy bạn hay khóc rồi!',
 69:'Càng nghiên cứu, tớ càng▼thấy thế giới có bao điều▼chẳng thể hiểu nổi.',
 71:"Mấy $507'84; đẹp quá đi!",
 72:'Thật khó tin, thứ▼đẹp đến thế lại có thể▼rơi từ trời xuống!',
 73:'Chắc vậy nên▼mới khó tìm đến thế.',
 74:'Xin lỗi vì đã gửi cậu▼bức điện tín kỳ quặc...',
 75:'Nếu cậu chịu quên đi,▼tớ vẫn muốn▼làm bạn với cậu.',
 76:"Mình làm lại từ đầu nhé?$079;$073'702'1;",
 77:'Lớp ngoại khóa▼vui thật đấy!',
 78:'Cậu có gặp khó khăn▼với dự án đang làm▼không, $500;?$079;',
 79:'Lớp ngoại khóa kết thúc rồi.▼Tiếc quá, tớ thích lắm!',
 80:'Bọn mình đã rất vui,▼nhưng chắc cần xa nhau▼một thời gian.',
 81:'Tớ sợ cứ thế này,▼chúng ta sẽ sớm▼chán nhau mất.',
 82:"Nếu cậu tin bọn mình sẽ ổn,▼hãy nói nhé. Mình lại▼làm bạn thân!$079;$073'702'1;",
 83:"Ừm...$079;$073'700'2'1;",
 84:"Ừm...$079;$073'700'3'1;",
 85:"Khi cậu thấy ổn,▼nói tớ biết nhé.▼Mình hẹn hò lại!$079;$073'702'1;",
 86:"Cậu muốn gì nào?▼Có chuyện muốn hỏi sao?$085;$019'1674;",
 87:'Xin lỗi, giờ tớ▼chẳng nghĩ ra chuyện gì▼thú vị để kể cả.$079;',
}
with zipfile.ZipFile(PREV) as zin:
    assert zin.testzip() is None
    oldfiles={n[len(OLD):]:zin.read(n) for n in zin.namelist() if n.startswith(OLD) and not n.endswith('/')}
assert len(oldfiles)==1420,len(oldfiles)
jsonlnames=[n for n in oldfiles if n.startswith('translation/') and n.endswith('.jsonl')]
assert len(jsonlnames)==501,len(jsonlnames)
rowsby={n:[json.loads(line) for line in oldfiles[n].decode('utf8').splitlines() if line.strip()] for n in jsonlnames}
assert sum(map(len,rowsby.values()))==55976
assert sum(sum(r.get('vi') is not None for r in rows) for rows in rowsby.values())==25175

targetnames={TALK+k+'.jsonl' for k in TARGETS}
prior=collections.defaultdict(collections.Counter)
for name, rows in rowsby.items():
    if name in targetnames: continue
    for row in rows:
        if isinstance(row.get('en'),str) and isinstance(row.get('vi'),str):
            prior[LEAD.sub('',row['en'])][LEAD.sub('',row['vi'])]+=1

unique={}
for key in TARGETS:
    name=TALK+key+'.jsonl'
    rows=rowsby[name]
    assert len(rows)==120 and all(r['vi'] is None for r in rows)
    for row in rows: unique.setdefault(LEAD.sub('',row['en']),None)
assert len(unique)==91,len(unique)
assert set(MANUAL)=={i for i,en in enumerate(unique,1) if not prior[en]},'reuse mismatch'
assert len(MANUAL)==45

translations={}
report=[]
for i,en in enumerate(unique,1):
    new=i in MANUAL
    vi=MANUAL[i] if new else prior[en].most_common(1)[0][0]
    assert vi and '\n' not in vi,(i,'missing')
    assert TOKEN.findall(en)==TOKEN.findall(vi),(i,'TOKEN',en,vi)
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
(STAGE/'DELTA-098.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in changed),encoding='utf8')
(STAGE/'unique_098.tsv').write_text('index\ten_body\tvi_body\torigin\n'+''.join(f'{i}\t{en}\t{vi}\t{org}\n' for i,en,vi,org in report),encoding='utf8')
for key in NEXT:
    name=TALK+key+'.jsonl'
    rows=rowsby[name]
    assert len(rows)==120 and all(row['vi'] is None for row in rows)
    (STAGE/(key+'.jsonl')).write_bytes(oldfiles[name])

qa='''# QA — Magician's Quest Checkpoint 098 (10/11/2026)

- **PASS:** 501 JSONL / 55,976 records compared with checkpoint 097.
- **25,175 → 25,415 / 55,976 (45.40%)**: +240 NPC dialogue pages.
- `0044.003`: 120/120; `0044.004`: 120/120.
- 91 unique English dialogue bodies: **46 reused existing EN–VI pairs**, **45 manually translated**.
- All 25,175 earlier translations preserved; **499 non-target JSONLs byte-identical**.
- `id`, `en`, `ctx`, additional JSON fields and ordering preserved.
- Exact NDS token sequences preserved; Unicode NFC PASS; max 3 breaks and 34 static codepoints per segment.
- ZIP CRC PASS; full JSONL parse and total/translated counts PASS.
- **Not verified inside ROM:** font width and dynamic variable expansion still require device/emulator QA.
- Next 099: `0044.005` and `0044.006`, 120 English pages each (not translated).
'''
cp='''# Magician's Quest — Checkpoint 098

**Date:** 10/11/2026
**Repository:** `ronvotri/VH-NDS` / `Magicians-Quest-Mysterious-Times/`.

- +240 NPC pages: `0044.003` and `0044.004` (120 each).
- Total: **25,415/55,976 (45.40%)**; NPC **22,290/52,608**.
- 91 unique English body patterns: 46 reused, 45 new localized lines.
- Content: scholarly student, year-end, spring tea party, spookfest, mushroom research, telegram apology, friendships and relationships.
- QA PASS: 501 JSONL files; 25,175 existing translations unchanged, 499 non-target JSONLs byte-identical; tokens and static line width checked.
- Handoff: `DELTA-098.jsonl`, `unique_098.tsv`, two TSVs, `QA-098.md`, `build_098.py`, full ZIP in Library.
- Next 099: `0044.005` and `0044.006` (240 pages, English unlocalized, included in ZIP).
- ROM visual validation remains outstanding.
'''
(STAGE/'QA-098.md').write_text(qa,encoding='utf8')
(STAGE/'CHECKPOINT-2026-11-10-DOT-98.md').write_text(cp,encoding='utf8')
intro_rm='**Checkpoint mới nhất: 098 (10/11/2026) — 25.415/55.976 (45,40%).** +240 trang thoại NPC (`0044.003` + `0044.004`); 45 mẫu mới, 46 mẫu tái sử dụng; QA 501 JSONL PASS. Đợt 099: `0044.005` và `0044.006` (240 trang). Xem `CHECKPOINT-2026-11-10-DOT-98.md`, `QA-098.md`.\n\n'
intro_bd='''## Checkpoint 098 — 10/11/2026

- +240 trang NPC `0044.003` và `0044.004`, tổng **25.415/55.976 (45,40%)**, NPC 22.290/52.608.
- 91 mẫu EN riêng, 46 tái dùng, 45 dịch mới; thoại học đường, tiệc trà, lễ hội, học ngoại khóa.
- QA 501 JSONL PASS, giữ nguyên 25.175 bản dịch cũ và 499 JSONL ngoài đợt.
- Bàn giao ZIP, bảng EN–VI, DELTA-098, QA-098, script; chưa test trên ROM.
- Đợt 099: `0044.005` và `0044.006` (240 trang).

'''
patch['README.md']=(intro_rm+oldfiles['README.md'].decode('utf8')).encode('utf8')
patch['BAN_GIAO.md']=(intro_bd+oldfiles['BAN_GIAO.md'].decode('utf8')).encode('utf8')
for name in ['README.md','BAN_GIAO.md']:(STAGE/name).write_bytes(patch[name])
for n in ['QA-098.md','CHECKPOINT-2026-11-10-DOT-98.md','DELTA-098.jsonl','unique_098.tsv','manual_0044_003.tsv','manual_0044_004.tsv','vi_0044_003.txt','vi_0044_004.txt']:
    assert n not in oldfiles,n
    patch[n]=(STAGE/n).read_bytes()
patch['build_098.py']=Path(__file__).read_bytes()
with zipfile.ZipFile(OUT,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as zout:
    for name,data in sorted({**oldfiles,**patch}.items()):zout.writestr(NEW+name,data)
with zipfile.ZipFile(OUT) as zout:
    assert zout.testzip() is None
    entries=zout.namelist()
    assert len(set(entries))==len(entries)
    jsonlnames=[n for n in entries if n.startswith(NEW+'translation/') and n.endswith('.jsonl')]
    assert len(jsonlnames)==501
    total=translated=0
    for name in rowsby:
        if name not in targetnames:assert zout.read(NEW+name)==oldfiles[name],name
        rows=[json.loads(s) for s in zout.read(NEW+name).decode('utf8').splitlines() if s.strip()]
        total+=len(rows);translated+=sum(r.get('vi') is not None for r in rows)
        if name in targetnames:assert all(r['vi'] is not None for r in rows)
    assert (total,translated)==(55976,25415),(total,translated)
print(json.dumps({'status':'PASS','file':str(OUT),'size_bytes':OUT.stat().st_size,'archive_files':len(entries),'jsonl':len(jsonlnames),'records':total,'translated':translated,'batch_pages':len(changed),'unique':len(unique),'new_unique':len(MANUAL),'reused_unique':len(unique)-len(MANUAL),'sha256':hashlib.sha256(OUT.read_bytes()).hexdigest()},ensure_ascii=False))