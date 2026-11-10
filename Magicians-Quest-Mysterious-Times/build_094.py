#!/usr/bin/env python3
"""Rebuild Magician's Quest Vietnamese checkpoint 094 from checkpoint 093.
No network dependencies, stdlib only, preserve all original strings and tokens.
"""
import collections
import hashlib
import json
import re
import unicodedata
import zipfile
from pathlib import Path

ROOT = Path('/mnt/data')
PREV = ROOT / 'MagiciansQuest-VietHoa-Checkpoint-093.zip'
OUT = ROOT / 'MagiciansQuest-VietHoa-Checkpoint-094.zip'
STAGE = ROOT / 'MQ094/stage'
STAGE.mkdir(parents=True, exist_ok=True)
OLD = 'MagiciansQuest_093/'
NEW = 'MagiciansQuest_094/'
TALK = 'translation/04-thoai/talkfigs__0eng__data__'
TARGETS = ['0043.018', '0043.019']
NEXT = ['0043.020', '0043.021']
LEAD = re.compile(r"^(?:\$(?:024|023|022|034|040|004)(?:'[-\d]+)*;)+")
TOKEN = re.compile(r"\$\d{3}(?:'[-\d]+)*;")

with zipfile.ZipFile(PREV) as zin:
    assert zin.testzip() is None, 'Invalid CRC baseline'
    oldfiles = {
        n[len(OLD):]: zin.read(n)
        for n in zin.namelist() if n.startswith(OLD) and not n.endswith('/')
    }
assert len(oldfiles) >= 1380, len(oldfiles)
jsonl = [n for n in oldfiles if n.startswith('translation/') and n.endswith('.jsonl')]
assert len(jsonl) == 501, len(jsonl)
oldrows = {
    name: [json.loads(line) for line in oldfiles[name].decode('utf8').splitlines() if line.strip()]
    for name in jsonl
}
assert sum(map(len, oldrows.values())) == 55976
assert sum(sum(r.get('vi') is not None for r in rows) for rows in oldrows.values()) == 24249

prior = collections.defaultdict(collections.Counter)
targetset = {TALK + x + '.jsonl' for x in TARGETS}
for name, rows in oldrows.items():
    if name in targetset:
        continue
    for r in rows:
        if isinstance(r.get('en'), str) and isinstance(r.get('vi'), str):
            prior[LEAD.sub('', r['en'])][LEAD.sub('', r['vi'])] += 1

unique = {}
for key in TARGETS:
    rows = oldrows[TALK + key + '.jsonl']
    assert len(rows) == 120 and all(r['vi'] is None for r in rows)
    for r in rows:
        unique.setdefault(LEAD.sub('', r['en']), None)
assert len(unique) == 239, len(unique)
report = []
translated_bodies = {}
for i, en in enumerate(unique, 1):
    assert prior[en], f'No prior Vietnamese for pattern {i}: {en}'
    vi = prior[en].most_common(1)[0][0]
    assert vi and '\n' not in vi
    assert TOKEN.findall(en) == TOKEN.findall(vi), (i, 'token mismatch')
    assert unicodedata.normalize('NFC', vi) == vi
    assert vi.count('▼') <= 3
    for segment in vi.split('▼'):
        static = TOKEN.sub('', segment)
        assert len(static) <= 34, (i, 'segment overflow', static)
        assert not re.search('[“”‘’—–«»…\u3000]', static), (i, 'punctuation', static)
    translated_bodies[en] = vi
    report.append((i, en, vi, 'TÁI DÙNG'))

patch = {}
changed = []
for key in TARGETS:
    name = TALK + key + '.jsonl'
    rows = []
    for original in oldrows[name]:
        row = original.copy()
        match = LEAD.match(row['en'])
        row['vi'] = (match.group(0) if match else '') + translated_bodies[LEAD.sub('', row['en'])]
        assert TOKEN.findall(row['en']) == TOKEN.findall(row['vi']), row['id']
        assert {k: v for k, v in row.items() if k != 'vi'} == {k: v for k, v in original.items() if k != 'vi'}
        rows.append(row)
    data = ''.join(json.dumps(r, ensure_ascii=False, separators=(',', ':')) + '\n' for r in rows).encode('utf8')
    patch[name] = data
    (STAGE / (key + '.jsonl')).write_bytes(data)
    short = key.replace('.', '_')
    (STAGE / ('manual_' + short + '.tsv')).write_text(
        'id\ten\tvi\tctx\n' + ''.join(f"{r['id']}\t{r['en']}\t{r['vi']}\t{r.get('ctx', '')}\n" for r in rows),
        encoding='utf8'
    )
    (STAGE / ('vi_' + short + '.txt')).write_text(
        ''.join(f"{r['id']}\t{r['vi']}\n" for r in rows), encoding='utf8'
    )
    changed.extend(rows)
assert len(changed) == 240 and len({x['id'] for x in changed}) == 240
(STAGE / 'DELTA-094.jsonl').write_text(
    ''.join(json.dumps(r, ensure_ascii=False, separators=(',', ':')) + '\n' for r in changed), encoding='utf8'
)
(STAGE / 'unique_094.tsv').write_text(
    'index\ten_body\tvi_body\torigin\n' +
    ''.join(f'{i}\t{en}\t{vi}\t{origin}\n' for i, en, vi, origin in report), encoding='utf8'
)
for key in NEXT:
    name = TALK + key + '.jsonl'
    rows = oldrows[name]
    assert len(rows) == 120 and all(r['vi'] is None for r in rows), key
    (STAGE / (key + '.jsonl')).write_bytes(oldfiles[name])

qa = '''# QA — Magician's Quest Checkpoint 094 (10/11/2026)

- **PASS:** 501 JSONL / 55,976 records compared with checkpoint 093.
- **24,249 → 24,489 / 55,976 (43.75%)**: +240 NPC dialogue pages.
- `0043.018`: 120/120; `0043.019`: 120/120.
- **239 unique English body patterns, all 239 exactly reused from previously translated records**; 0 new distinct strings.
- All 24,249 earlier translations unchanged; 499 non-target JSONLs byte-identical.
- Original `id`, `en`, `ctx`, other fields and ordering preserved.
- NDS control tokens preserved in exact order, including `$500`, `$079`, `$000` formatting controls.
- Unicode NFC, at most 3 `▼` separators, at most 34 static Unicode codepoints per segment, standard punctuation.
- ZIP CRC PASS; full 501 JSONL parse; 55,976 records with 24,489 translated.
- **Not ROM tested:** expansion of runtime variables and font glyph widths require emulator/real NDS checks.
- Next batch 095: `0043.020` and `0043.021` (120 untranslated pages each).
'''
cp = '''# Magician's Quest — Checkpoint 094

**Date:** 10/11/2026
**Repository:** `ronvotri/VH-NDS` / `Magicians-Quest-Mysterious-Times/`.

- Translated **240 NPC dialogue pages** from `0043.018` and `0043.019` (120 each).
- Total **24,489/55,976 (43.75%)**; NPC **21,364/52,608**.
- 239 unique English bodies: all have exact-match Vietnamese from earlier checkpoints, no new phrase was fabricated.
- Topics include Candyman, the river, school mysteries, Captain Dot, Sphinx, Krampus, Minotaur and other side quests.
- QA PASS across 501 JSONLs; 499 non-target JSONLs byte-identical; no in-ROM test yet.
- Handoff: `DELTA-094.jsonl`, `unique_094.tsv`, two EN–VI TSVs, `QA-094.md`, `build_094.py` and full ZIP in Library.
- Next 095: `0043.020`, `0043.021`, 240 untranslated pages already in ZIP.
'''
(STAGE / 'QA-094.md').write_text(qa, encoding='utf8')
(STAGE / 'CHECKPOINT-2026-11-10-DOT-94.md').write_text(cp, encoding='utf8')
intro_rm = '**Checkpoint mới nhất: 094 (10/11/2026) — 24.489/55.976 (43,75%).** +240 trang thoại NPC (`0043.018`, `0043.019`); 239 mẫu trùng được tái dùng, 0 mẫu mới; QA 501 JSONL PASS. Tiếp `0043.020`, `0043.021` (240 trang). Xem `CHECKPOINT-2026-11-10-DOT-94.md`, `QA-094.md`.\n\n'
intro_ban = '''## Checkpoint 094 — 10/11/2026

- +240 trang NPC `0043.018` và `0043.019`; tổng 24.489/55.976 (43,75%), NPC 21.364/52.608.
- 239 mẫu thoại EN riêng đều có bản Việt từ checkpoint trước, không có mẫu mới.
- QA 501 JSONL PASS; giữ nguyên 24.249 bản dịch cũ và 499 tệp ngoài đợt.
- ZIP đầy đủ, bảng EN–VI, delta, báo cáo QA, script dựng lại; chưa thử ROM.
- Đợt 095: `0043.020` và `0043.021` (120 trang mỗi tệp).

'''
patch['README.md'] = (intro_rm + oldfiles['README.md'].decode('utf8')).encode('utf8')
patch['BAN_GIAO.md'] = (intro_ban + oldfiles['BAN_GIAO.md'].decode('utf8')).encode('utf8')
for name in ['README.md', 'BAN_GIAO.md']:
    (STAGE / name).write_bytes(patch[name])
for name in ['QA-094.md', 'CHECKPOINT-2026-11-10-DOT-94.md', 'DELTA-094.jsonl', 'unique_094.tsv',
             'manual_0043_018.tsv', 'manual_0043_019.tsv', 'vi_0043_018.txt', 'vi_0043_019.txt']:
    assert name not in oldfiles, name
    patch[name] = (STAGE / name).read_bytes()
patch['build_094.py'] = Path(__file__).read_bytes()
with zipfile.ZipFile(OUT, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zout:
    for name, payload in sorted({**oldfiles, **patch}.items()):
        zout.writestr(NEW + name, payload)
with zipfile.ZipFile(OUT) as zout:
    names = zout.namelist()
    assert len(names) == len(set(names)), 'Duplicate zip entry'
    assert zout.testzip() is None
    assert len([n for n in names if n.startswith(NEW + 'translation/') and n.endswith('.jsonl')]) == 501
    total = done = 0
    for name in jsonl:
        if name not in targetset:
            assert zout.read(NEW + name) == oldfiles[name], f'Non-target JSONL changed: {name}'
        rows = [json.loads(x) for x in zout.read(NEW + name).decode('utf8').splitlines() if x.strip()]
        total += len(rows)
        done += sum(r.get('vi') is not None for r in rows)
        if name in targetset:
            assert len(rows) == 120 and all(r['vi'] is not None for r in rows)
    assert (total, done) == (55976, 24489), (total, done)
    for key in TARGETS:
        assert zout.read(NEW + TALK + key + '.jsonl') == (STAGE / (key + '.jsonl')).read_bytes()
print(json.dumps({'status': 'PASS', 'path': str(OUT), 'bytes': OUT.stat().st_size,
                  'entries': len(names), 'jsonl': len(jsonl), 'records': total, 'translated': done,
                  'new_pages': len(changed), 'unique_patterns': len(unique), 'new_unique': 0,
                  'reused_unique': len(unique), 'sha256': hashlib.sha256(OUT.read_bytes()).hexdigest()}, ensure_ascii=False))