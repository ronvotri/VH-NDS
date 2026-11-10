#!/usr/bin/env python3
"""Build Magician's Quest checkpoint 096 from 095, preserving all old content.
Original English and ROM control tokens are kept byte-for-byte inside each JSON field.
Requires only Python standard library and checkpoint 095 ZIP.
"""
import collections
import hashlib
import json
import re
import unicodedata
import zipfile
from pathlib import Path

ROOT = Path('/mnt/data')
PREV = ROOT / 'MagiciansQuest-VietHoa-Checkpoint-095.zip'
OUT = ROOT / 'MagiciansQuest-VietHoa-Checkpoint-096.zip'
STAGE = ROOT / 'MQ096/stage'
STAGE.mkdir(parents=True, exist_ok=True)
OLD = 'MagiciansQuest_095/'
NEW = 'MagiciansQuest_096/'
TALK = 'translation/04-thoai/talkfigs__0eng__data__'
TARGETS = ['0043.022', '0043.023']
NEXT = ['0044.001', '0044.002']
LEAD = re.compile(r"^(?:\$(?:024|023|022|034|040|004)(?:'[-\d]+)*;)+")
TOKEN = re.compile(r"\$\d{3}(?:'[-\d]+)*;")

# Numbered by first occurrence across 0043.022 -> 0043.023.
# Only the 35 genuinely unseen English bodies are translated here.
MANUAL = {
 62: 'Nghe mấy lời đồn quái lạ,▼ai còn dám xuống▼$000\'5;bãi biển$000\'1; nữa chứ...',
 173: 'Phải công nhận, đi chơi▼với cậu vui thật đấy.',
 174: 'Tớ còn đang nghĩ...▼hay là thôi không▼bắt nạt ai nữa nhỉ...',
 175: 'Ý nghĩ lạ đời thật...',
 176: '$500;, lúc bên tớ▼cậu thường nghĩ▼chuyện gì vậy?',
 177: 'Tớ thì vui đến mức▼chẳng nghĩ được▼GÌ SẤT!',
 178: 'Hay là... có khi nào...▼tớ đang... yếu đi?!',
 179: 'Trước giờ, tớ chưa từng▼tin tưởng bất kỳ ai.',
 180: 'Nhưng từ khi cậu▼trở thành bạn gái tớ,▼tớ muốn kết bạn với TẤT CẢ!',
 181: 'Có nên đi khám không nhỉ?',
 182: 'Cậu thấy tớ có▼nhiều tật xấu không?',
 183: 'Cậu phải nhắc tớ nhé,▼chứ tớ có tự nhận ra▼mấy cái đó đâu...',
 184: 'Vì cậu, biết đâu tớ▼sẽ chịu sửa một tật...',
 185: 'Này, cảm ơn nhé, $500;.▼Nhờ cậu, tớ thấy▼tự tin hơn nhiều.',
 186: 'Không phải kiểu tự tin▼đủ sức đấm ai▼vỡ mặt đâu nhé...',
 187: 'Tớ trưởng thành rồi...▼Giờ tớ khoái bày trò▼chọc ghẹo hơn!',
 188: '$500;, cậu có thấy▼dạo này trời tối▼sớm hơn không?',
 189: 'Như có ai dùng phép▼ngôn ngữ để trêu▼chúng ta ấy.',
 190: 'Phải đi tìm thủ phạm▼và cho một bài học▼nhớ đời mới được!',
 191: 'Cứ như mới hôm qua,▼tớ vẫn chỉ chơi▼một mình...',
 192: 'Chắc chẳng ai thích▼chơi với đứa hay▼bắt nạt người khác.',
 193: 'Hồi đó cô đơn lắm...▼Bảo sao nắm đấm tớ▼cứ thích làm quen với mặt ai!',
 194: 'Cậu thấy tớ có▼tật xấu nào không?',
 195: 'Bạn thân thì phải▼giúp nhau chứ, nhỉ?',
 196: 'Biết đâu tớ sẽ▼sửa một tật xấu▼vì cậu... nếu cậu hên!',
 197: 'Ối, nhìn giờ kìa!',
 198: 'Chơi đến đây thôi nhỉ?▼Cậu thấy sao?$019\'6701;',
 199: 'Chơi thêm chút nữa...$019\'6702;',
 200: 'Ừ. Gặp sau nhé!$019\'6703;',
 201: 'Ha ha! Phải thế chứ!$074;',
 202: 'Tớ cũng muốn▼quậy thêm chút nữa!',
 203: 'Được rồi! Hôm nay vui ghê!',
 204: 'Bữa nào lại chơi nữa nhé!',
 205: 'Này, $500;! Tớ vừa▼nhớ ra còn việc▼quan trọng phải làm.',
 206: 'Tớ chuồn đây. $023\'328\'104\'10;Tạm biệt!▼',
}
assert len(MANUAL) == 35

with zipfile.ZipFile(PREV) as zin:
    assert zin.testzip() is None, 'Invalid baseline ZIP CRC'
    oldfiles = {
        name[len(OLD):]: zin.read(name)
        for name in zin.namelist() if name.startswith(OLD) and not name.endswith('/')
    }
assert len(oldfiles) == 1402, len(oldfiles)
jsonl = [name for name in oldfiles if name.startswith('translation/') and name.endswith('.jsonl')]
assert len(jsonl) == 501, len(jsonl)
oldrows = {
    name: [json.loads(line) for line in oldfiles[name].decode('utf8').splitlines() if line.strip()]
    for name in jsonl
}
assert sum(map(len, oldrows.values())) == 55976
assert sum(sum(row.get('vi') is not None for row in rows) for rows in oldrows.values()) == 24729

targetset = {TALK + key + '.jsonl' for key in TARGETS}
prior = collections.defaultdict(collections.Counter)
for name, rows in oldrows.items():
    if name in targetset:
        continue
    for row in rows:
        if isinstance(row.get('en'), str) and isinstance(row.get('vi'), str):
            prior[LEAD.sub('', row['en'])][LEAD.sub('', row['vi'])] += 1

unique = {}
for key in TARGETS:
    name = TALK + key + '.jsonl'
    rows = oldrows[name]
    assert len(rows) == (86 if key == '0043.023' else 120)
    assert all(r['vi'] is None for r in rows)
    for row in rows:
        unique.setdefault(LEAD.sub('', row['en']), None)
assert len(unique) == 206, len(unique)
assert set(MANUAL) == {i for i, en in enumerate(unique, 1) if not prior[en]}, 'Manual/index reuse mismatch'

translations = {}
report = []
for i, en in enumerate(unique, 1):
    isnew = i in MANUAL
    vi = MANUAL[i] if isnew else prior[en].most_common(1)[0][0]
    assert vi and '\n' not in vi, (i, 'missing translation')
    assert TOKEN.findall(en) == TOKEN.findall(vi), (i, en, vi, 'token mismatch')
    assert unicodedata.normalize('NFC', vi) == vi, (i, 'non-NFC')
    assert vi.count('▼') <= 3, (i, 'too many line breaks')
    for segment in vi.split('▼'):
        static = TOKEN.sub('', segment)
        assert len(static) <= 34, (i, 'segment overflow', len(static), static)
        assert not re.search('[“”‘’—–«»…\u3000]', static), (i, 'punctuation', static)
    translations[en] = vi
    report.append((i, en, vi, 'DỊCH MỚI' if isnew else 'TÁI DÙNG'))

patch = {}
changed = []
for key in TARGETS:
    name = TALK + key + '.jsonl'
    rows = []
    for original in oldrows[name]:
        row = original.copy()
        lead = LEAD.match(row['en'])
        row['vi'] = (lead.group(0) if lead else '') + translations[LEAD.sub('', row['en'])]
        assert TOKEN.findall(row['en']) == TOKEN.findall(row['vi']), row['id']
        assert {k:v for k,v in original.items() if k!='vi'} == {k:v for k,v in row.items() if k!='vi'}
        rows.append(row)
    data = ''.join(json.dumps(row, ensure_ascii=False, separators=(',', ':')) + '\n' for row in rows).encode('utf8')
    patch[name] = data
    (STAGE / (key + '.jsonl')).write_bytes(data)
    short = key.replace('.', '_')
    (STAGE / ('manual_' + short + '.tsv')).write_text(
        'id\ten\tvi\tctx\n' + ''.join(f"{r['id']}\t{r['en']}\t{r['vi']}\t{r.get('ctx', '')}\n" for r in rows), encoding='utf8')
    (STAGE / ('vi_' + short + '.txt')).write_text(
        ''.join(f"{r['id']}\t{r['vi']}\n" for r in rows), encoding='utf8')
    changed.extend(rows)
assert len(changed) == 206 and len({r['id'] for r in changed}) == 206
(STAGE / 'DELTA-096.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False, separators=(',', ':')) + '\n' for r in changed), encoding='utf8')
(STAGE / 'unique_096.tsv').write_text('index\ten_body\tvi_body\torigin\n' + ''.join(f'{i}\t{en}\t{vi}\t{origin}\n' for i,en,vi,origin in report), encoding='utf8')
for key in NEXT:
    name = TALK + key + '.jsonl'
    rows = oldrows[name]
    assert len(rows) == 120 and all(row['vi'] is None for row in rows), key
    (STAGE / (key + '.jsonl')).write_bytes(oldfiles[name])

qa = '''# QA — Magician's Quest Checkpoint 096 (10/11/2026)

- **PASS:** 501 JSONL / 55,976 records compared with checkpoint 095.
- **24,729 → 24,935 / 55,976 (44.55%)**: +206 NPC dialogue pages.
- `0043.022`: 120/120; `0043.023`: 86/86.
- 206 unique English bodies, of which 171 reuse prior EN–VI pairs and **35 are new Vietnamese translations**.
- 24,729 previous translated records unchanged; all **499 non-target JSONLs byte-identical**.
- `id`, `en`, `ctx`, all other JSON fields and ordering preserved in target rows.
- Exact NDS control-token sequence preserved in every target; Unicode NFC PASS, max 3 breaks, ≤34 static codepoints per segment.
- ZIP CRC PASS; 501 JSONL parse, 55,976 rows, 24,935 translated; archive reconstruction script provided.
- **In-ROM font rendering and dynamic token expansion have not been tested.**
- Next 097: `0044.001` + `0044.002` (120 pages each), sources included in ZIP.
'''
cp = '''# Magician's Quest — Checkpoint 096

**Date:** 10/11/2026
**Repository:** `ronvotri/VH-NDS` / `Magicians-Quest-Mysterious-Times/`.

- +206 NPC dialogue pages: `0043.022` (120) + `0043.023` (86).
- Total **24,935/55,976 (44.55%)**; NPC **21,810/52,608**.
- 206 unique English bodies: 171 reused; 35 translated manually. Stories include the headless knight, a bully learning friendship, romantic dialogue and saying goodbye.
- Full QA: 501 JSONLs PASS; existing 24,729 translations preserved; all 499 non-target JSONLs byte-identical.
- Handoff: `DELTA-096.jsonl`, `unique_096.tsv`, EN–VI TSVs, `QA-096.md`, `build_096.py`, full ZIP in Library.
- Next 097: `0044.001` and `0044.002` (240 pages, untranslated, staged in ZIP).
- ROM visual test remains outstanding.
'''
(STAGE / 'QA-096.md').write_text(qa, encoding='utf8')
(STAGE / 'CHECKPOINT-2026-11-10-DOT-96.md').write_text(cp, encoding='utf8')
intro_rm = '**Checkpoint mới nhất: 096 (10/11/2026) — 24.935/55.976 (44,55%).** +206 trang thoại NPC (`0043.022`: 120; `0043.023`: 86); 35 mẫu mới, 171 mẫu tái sử dụng; QA 501 JSONL PASS. Tiếp `0044.001` và `0044.002` (240 trang). Xem `CHECKPOINT-2026-11-10-DOT-96.md`, `QA-096.md`.\n\n'
intro_bd = '''## Checkpoint 096 — 10/11/2026

- +206 trang NPC `0043.022` (120) và `0043.023` (86); tổng **24.935/55.976 (44,55%)**, NPC 21.810/52.608.
- 206 mẫu EN riêng: 171 mẫu tái dùng, 35 mẫu dịch mới.
- QA 501 JSONL PASS, không sửa 24.729 bản dịch cũ và 499 JSONL ngoài đợt.
- ZIP đầy đủ, EN–VI TSV, delta, QA, script; chưa test ROM.
- Tiếp đợt 097: `0044.001`, `0044.002` (240 trang).

'''
patch['README.md'] = (intro_rm + oldfiles['README.md'].decode('utf8')).encode('utf8')
patch['BAN_GIAO.md'] = (intro_bd + oldfiles['BAN_GIAO.md'].decode('utf8')).encode('utf8')
for name in ['README.md','BAN_GIAO.md']:
    (STAGE / name).write_bytes(patch[name])
for name in ['QA-096.md','CHECKPOINT-2026-11-10-DOT-96.md','DELTA-096.jsonl','unique_096.tsv',
             'manual_0043_022.tsv','manual_0043_023.tsv','vi_0043_022.txt','vi_0043_023.txt']:
    assert name not in oldfiles, name
    patch[name] = (STAGE / name).read_bytes()
patch['build_096.py'] = Path(__file__).read_bytes()
with zipfile.ZipFile(OUT, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zout:
    for name, payload in sorted({**oldfiles, **patch}.items()):
        zout.writestr(NEW + name, payload)
with zipfile.ZipFile(OUT) as zout:
    names = zout.namelist()
    assert len(names) == len(set(names)) and zout.testzip() is None
    jsonlnames = [name for name in names if name.startswith(NEW + 'translation/') and name.endswith('.jsonl')]
    assert len(jsonlnames) == 501
    total = done = 0
    for name in jsonl:
        if name not in targetset:
            assert zout.read(NEW + name) == oldfiles[name], 'Non-target JSONL altered: '+name
        rows = [json.loads(s) for s in zout.read(NEW + name).decode('utf8').splitlines() if s.strip()]
        total += len(rows)
        done += sum(r.get('vi') is not None for r in rows)
        if name in targetset:
            assert all(r['vi'] is not None for r in rows)
    assert (total, done) == (55976, 24935), (total, done)
print(json.dumps({'status':'PASS', 'path':str(OUT),'bytes':OUT.stat().st_size,
                  'entries':len(names),'jsonl':len(jsonlnames),'records':total,'translated':done,
                  'new_pages':len(changed),'unique':len(unique),'new_unique':len(MANUAL),
                  'reused_unique':len(unique)-len(MANUAL),
                  'sha256':hashlib.sha256(OUT.read_bytes()).hexdigest()},ensure_ascii=False))