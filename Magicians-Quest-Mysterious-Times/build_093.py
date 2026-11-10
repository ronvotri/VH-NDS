#!/usr/bin/env python3
"""Rebuild/check Magician's Quest Vietnamese checkpoint 093 from the full checkpoint 092 ZIP.
Offline, stdlib only. Source of meaning is English, previously accepted Vietnamese body
is reused only for exact matches, and six English bodies are newly localized.
"""
import collections
import hashlib
import json
import re
import unicodedata
import zipfile
from pathlib import Path

ROOT = Path('/mnt/data')
PREV = ROOT / 'MagiciansQuest-VietHoa-Checkpoint-092.zip'
OUT = ROOT / 'MagiciansQuest-VietHoa-Checkpoint-093.zip'
STAGE = ROOT / 'MQ093' / 'stage'
STAGE.mkdir(parents=True, exist_ok=True)
OLD_PREFIX = 'MagiciansQuest_092/'
NEW_PREFIX = 'MagiciansQuest_093/'
TALK = 'translation/04-thoai/talkfigs__0eng__data__'
TARGETS = ['0043.016', '0043.017']
NEXT = ['0043.018', '0043.019']
LEAD = re.compile(r"^(?:\$(?:024|023|022|034|040|004)(?:'[-\d]+)*;)+")
TOKEN = re.compile(r"\$\d{3}(?:'[-\d]+)*;")

# Manually reviewed Vietnamese, identified by stable ordinal position of the 72
# distinct English body strings in 0043.016 + 0043.017.
NEW = {
    9: 'Cứ thân thiết rồi▼vui vẻ suốt ngày là sao?▼Họ đâu biết...',
    10: 'thế nào là▼sợ xanh mặt...',
    24: 'Cậu đến đúng lúc đấy!▼Bọn tớ vừa nhắc đến▼chuyện hay ho lắm...',
    58: 'Khá bất ngờ đấy!▼Nhưng ai cũng có▼con đường riêng mà...',
    59: 'Xin lỗi, $500;! Tớ không▼thể kể chuyện đó đâu.',
    60: 'Có những chuyện▼không biết vẫn hơn...',
}

with zipfile.ZipFile(PREV) as zin:
    assert zin.testzip() is None, 'Baseline ZIP has invalid CRC'
    oldfiles = {
        n[len(OLD_PREFIX):]: zin.read(n)
        for n in zin.namelist()
        if n.startswith(OLD_PREFIX) and not n.endswith('/')
    }
assert len(oldfiles) >= 1360, len(oldfiles)
jsonls = [n for n in oldfiles if n.startswith('translation/') and n.endswith('.jsonl')]
assert len(jsonls) == 501, len(jsonls)
oldrows = {
    n: [json.loads(line) for line in oldfiles[n].decode('utf8').splitlines() if line.strip()]
    for n in jsonls
}
assert sum(len(r) for r in oldrows.values()) == 55976
assert sum(sum(rec.get('vi') is not None for rec in rs) for rs in oldrows.values()) == 24009

prior = collections.defaultdict(collections.Counter)
for n, rows in oldrows.items():
    if n in {TALK + x + '.jsonl' for x in TARGETS}:
        continue
    for rec in rows:
        if rec.get('vi') is not None and isinstance(rec.get('en'), str):
            prior[LEAD.sub('', rec['en'])][LEAD.sub('', rec['vi'])] += 1

unique = dict()
for key in TARGETS:
    recs = oldrows[TALK + key + '.jsonl']
    assert len(recs) == 120 and all(rec['vi'] is None for rec in recs)
    for rec in recs:
        unique.setdefault(LEAD.sub('', rec['en']), None)
assert len(unique) == 72, len(unique)
assert len(NEW) == 6
translation = {}
report = []
for i, en in enumerate(unique, 1):
    if i in NEW:
        assert not prior[en], f'New pattern {i} unexpectedly has prior translation'
        vi = NEW[i]
        origin = 'MỚI'
    else:
        assert prior[en], f'Exact prior Vietnamese translation missing at {i}: {en}'
        vi = prior[en].most_common(1)[0][0]
        origin = 'TÁI DÙNG'
    assert vi and '\n' not in vi, (i, vi)
    assert unicodedata.normalize('NFC', vi) == vi, (i, 'NFC')
    assert TOKEN.findall(en) == TOKEN.findall(vi), (i, 'token mismatch', en, vi)
    assert vi.count('▼') <= 3, (i, 'break overflow')
    for segment in vi.split('▼'):
        static = TOKEN.sub('', segment)
        assert len(static) <= 34, (i, 'segment too long', len(static), static)
        assert not re.search('[“”‘’—–«»…\u3000]', static), (i, 'nonstandard punctuation', static)
    report.append((i, en, vi, origin))
    translation[en] = vi
assert sum(r[3] == 'MỚI' for r in report) == 6

patch = {}
changed = []
for key in TARGETS:
    filename = TALK + key + '.jsonl'
    newrows = []
    for rec in oldrows[filename]:
        rr = rec.copy()
        lead = LEAD.match(rec['en'])
        rr['vi'] = (lead.group(0) if lead else '') + translation[LEAD.sub('', rec['en'])]
        assert TOKEN.findall(rec['en']) == TOKEN.findall(rr['vi']), rr['id']
        assert {k:v for k,v in rr.items() if k != 'vi'} == {k:v for k,v in rec.items() if k != 'vi'}
        newrows.append(rr)
    data = ''.join(json.dumps(r, ensure_ascii=False, separators=(',', ':')) + '\n' for r in newrows).encode('utf8')
    patch[filename] = data
    (STAGE / (key + '.jsonl')).write_bytes(data)
    short = key.replace('.', '_')
    (STAGE / ('manual_' + short + '.tsv')).write_text(
        'id\ten\tvi\tctx\n' + ''.join(f"{r['id']}\t{r['en']}\t{r['vi']}\t{r.get('ctx','')}\n" for r in newrows), encoding='utf8'
    )
    (STAGE / ('vi_' + short + '.txt')).write_text(
        ''.join(r['id'] + '\t' + r['vi'] + '\n' for r in newrows), encoding='utf8'
    )
    changed.extend(newrows)
assert len(changed) == 240 and len({rec['id'] for rec in changed}) == 240
(STAGE / 'DELTA-093.jsonl').write_text(
    ''.join(json.dumps(r, ensure_ascii=False, separators=(',', ':')) + '\n' for r in changed), encoding='utf8'
)
(STAGE / 'unique_093.tsv').write_text(
    'index\ten_body\tvi_body\torigin\n' +
    ''.join(f'{i}\t{en}\t{vi}\t{origin}\n' for i, en, vi, origin in report), encoding='utf8'
)
# Prepare the next untranslated sources without introducing invented translations.
for key in NEXT:
    filename = TALK + key + '.jsonl'
    rows = oldrows[filename]
    assert len(rows) == 120 and all(r['vi'] is None for r in rows)
    (STAGE / (key + '.jsonl')).write_bytes(oldfiles[filename])

qa = '''# QA — Magician's Quest Checkpoint 093 (10/11/2026)

- **PASS:** 501 JSONL / 55,976 records, checkpoint 092 baseline.
- **24,009 -> 24,249 / 55,976 (43.32%)**: +240 NPC pages.
- `0043.016`: 120/120; `0043.017`: 120/120.
- **72 unique English body patterns:** 66 reused exactly from existing reviewed Vietnamese; 6 localized newly.
- Existing 24,009 translations unchanged; 499 non-target JSONLs byte-identical.
- 240 target records preserve original `id`, `en`, `ctx`, other fields, and ordering.
- Exact NDS control tokens preserved, including `$500`, `$530`, `$532`, `$533`, and `$000`.
- Unicode NFC, at most 3 `▼` breaks, 34 static Unicode characters per segment.
- ZIP CRC PASS; 501 JSONL parse; translated total 24,249.
- **Not ROM tested:** variable expansion and actual glyph widths require emulator/hardware checks.
- Next batch 094: `0043.018`, `0043.019` (120 untranslated pages each).
'''
cp = '''# Magician's Quest — Checkpoint 093

**Date:** 10/11/2026
**Repository:** `ronvotri/VH-NDS` / `Magicians-Quest-Mysterious-Times/`.

- Translated **240 NPC dialogue pages** from `0043.016` and `0043.017` (120 each).
- Total **24,249/55,976 (43.32%)**; NPC **21,124/52,608**.
- 72 unique English patterns: 6 newly edited, 66 reused from already translated records.
- Rumor dialogue, school friends, dating, magic, cave lake sounds and the mysterious Nessie.
- All 501 JSONL passed QA, 499 non-target JSONL byte-identical. Not tested in ROM.
- Handoff: `DELTA-093.jsonl`, `unique_093.tsv`, two EN–VI TSVs, `QA-093.md`, `build_093.py`, full ZIP in Library.
- Next 094: `0043.018` and `0043.019` (240 untranslated pages already in ZIP).
'''
(STAGE / 'QA-093.md').write_text(qa, encoding='utf8')
(STAGE / 'CHECKPOINT-2026-11-10-DOT-93.md').write_text(cp, encoding='utf8')
intro_rm = '**Checkpoint mới nhất: 093 (10/11/2026) — 24.249/55.976 (43,32%).** +240 NPC (`0043.016`, `0043.017`); 6 mẫu mới, 66 mẫu tái dùng; QA 501 JSONL PASS. Tiếp `0043.018`, `0043.019` (240 trang). Xem `CHECKPOINT-2026-11-10-DOT-93.md`, `QA-093.md`.\n\n'
intro_handoff = '''## Checkpoint 093 — 10/11/2026

- +240 trang NPC `0043.016` và `0043.017`; tổng 24.249/55.976 (43,32%), NPC 21.124/52.608.
- 72 mẫu EN riêng: 6 dịch mới, 66 tái dùng; QA 501 JSONL PASS; giữ nguyên 24.009 bản dịch trước.
- ZIP đầy đủ, EN–VI, delta, QA và script dựng lại; chưa kiểm thử ROM.
- Đợt 094: `0043.018` và `0043.019` (120 trang mỗi tệp).

'''
patch['README.md'] = (intro_rm + oldfiles['README.md'].decode('utf8')).encode('utf8')
patch['BAN_GIAO.md'] = (intro_handoff + oldfiles['BAN_GIAO.md'].decode('utf8')).encode('utf8')
for fn in ['README.md', 'BAN_GIAO.md']:
    (STAGE / fn).write_bytes(patch[fn])
for fn in ['QA-093.md', 'CHECKPOINT-2026-11-10-DOT-93.md', 'DELTA-093.jsonl', 'unique_093.tsv',
           'manual_0043_016.tsv', 'manual_0043_017.tsv', 'vi_0043_016.txt', 'vi_0043_017.txt']:
    assert fn not in oldfiles, fn
    patch[fn] = (STAGE / fn).read_bytes()
patch['build_093.py'] = Path(__file__).read_bytes()
with zipfile.ZipFile(OUT, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zout:
    for filename, payload in sorted({**oldfiles, **patch}.items()):
        zout.writestr(NEW_PREFIX + filename, payload)
with zipfile.ZipFile(OUT) as zout:
    names = zout.namelist()
    assert len(names) == len(set(names)), 'Duplicate archive entry'
    assert zout.testzip() is None, 'ZIP CRC failed'
    checks = [n for n in names if n.startswith(NEW_PREFIX + 'translation/') and n.endswith('.jsonl')]
    assert len(checks) == 501
    total = translated = 0
    target_set = {TALK + k + '.jsonl' for k in TARGETS}
    for n in jsonls:
        if n not in target_set:
            assert zout.read(NEW_PREFIX + n) == oldfiles[n], f'Non-target changed: {n}'
        rows = [json.loads(line) for line in zout.read(NEW_PREFIX + n).decode('utf8').splitlines() if line.strip()]
        total += len(rows)
        translated += sum(r.get('vi') is not None for r in rows)
        if n in target_set:
            assert len(rows) == 120 and all(r.get('vi') is not None for r in rows)
    assert total == 55976 and translated == 24249, (total, translated)
    for key in TARGETS:
        assert zout.read(NEW_PREFIX + TALK + key + '.jsonl') == (STAGE / (key + '.jsonl')).read_bytes()
print(json.dumps({'status': 'PASS', 'zip': str(OUT), 'bytes': OUT.stat().st_size,
                  'files': len(names), 'jsonl': 501, 'total': total, 'translated': translated,
                  'new_pages': len(changed), 'unique': len(unique), 'new_patterns': len(NEW),
                  'reused_patterns': len(unique) - len(NEW),
                  'sha256': hashlib.sha256(OUT.read_bytes()).hexdigest()}, ensure_ascii=False))