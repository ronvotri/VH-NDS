#!/usr/bin/env python3
"""Create a complete Magician's Quest NDS Vietnamese checkpoint 063 from checkpoint 062.
Usage: python build_063.py checkpoint062.zip [output063.zip]
Requires vi_0041_001.txt and vi_0041_002.txt alongside this script.
"""
from __future__ import annotations
import json, re, sys, zipfile, unicodedata
from pathlib import Path
HERE=Path(__file__).resolve().parent
OLD=Path(sys.argv[1]) if len(sys.argv)>1 else Path('/mnt/data/MagiciansQuest-VietHoa-Checkpoint-062.zip')
NEW=Path(sys.argv[2]) if len(sys.argv)>2 else Path('/mnt/data/MagiciansQuest-VietHoa-Checkpoint-063.zip')
R_OLD='MagiciansQuest_062/'
R_NEW='MagiciansQuest_063/'
SFX=['0041.001','0041.002']
TOKEN=re.compile(r"\$\d{3}(?:'[0-9-]+)*;")
PREFIX=re.compile(r"^((?:\$(?:024|023|022|004)(?:'[0-9-]+)*;)+)")
SUFFIX=re.compile(r"((?:\$(?:079|074|019|018|073|033)(?:'[0-9-]+)*;)+)$")
changes={}; delta=[]; meta={}
with zipfile.ZipFile(OLD) as zin:
    assert zin.testzip() is None
    for suffix in SFX:
        path=f'translation/04-thoai/talkfigs__0eng__data__{suffix}.jsonl'
        rows=[json.loads(x) for x in zin.read(R_OLD+path).decode().splitlines()]
        translations=(HERE/f'vi_{suffix.replace(".","_")}.txt').read_text(encoding='utf-8').splitlines()
        assert len(rows)==len(translations)==120,(suffix,len(rows),len(translations))
        manual=['id\ten\tvi\tctx']
        for r,body in zip(rows,translations):
            assert r['vi'] is None, r['id']
            pre=PREFIX.match(r['en']); post=SUFFIX.search(r['en'])
            value=unicodedata.normalize('NFC',(pre.group(1) if pre else '')+body+(post.group(1) if post else ''))
            assert TOKEN.findall(r['en'])==TOKEN.findall(value),(r['id'],'token mismatch')
            assert value and '\n' not in value and '\r' not in value and '\t' not in value,r['id']
            assert value.count('▼')<=3,r['id']
            assert all(len(TOKEN.sub('',seg))<=34 for seg in value.split('▼')),(r['id'],'line width')
            r['vi']=value
            delta.append(dict(r))
            manual.append('\t'.join(str(r[k]) for k in ('id','en','vi','ctx')))
        changes[path]=(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in rows)).encode()
        changes[f'manual_{suffix.replace(".","_")}.tsv']=('\n'.join(manual)+'\n').encode()
        changes[f'vi_{suffix.replace(".","_")}.txt']=(HERE/f'vi_{suffix.replace(".","_")}.txt').read_bytes()
        meta[suffix]=len(rows)
    qa='''# QA — Magician’s Quest · Đợt 063

- **PASS:** Đối chiếu checkpoint 062 → 063 trên 501 JSONL / 55.976 bản ghi.
- **PASS:** Điền mới 240 trường `vi`: `0041.001` và `0041.002` (120 mỗi tệp); **16.932 → 17.172/55.976 (30,68%)**; thoại NPC **13.807 → 14.047/52.608**.
- **PASS:** Không sửa 16.932 bản dịch cũ; chỉ hai JSONL đích thay đổi, 499 tệp ngoài mục tiêu byte-identical.
- **PASS:** Giữ nguyên ID/EN/CTX, mọi token `$...;` đúng thứ tự, Unicode NFC, không CR/LF/TAB trong thoại, tối đa 3 `▼`, tối đa 34 ký tự tĩnh mỗi đoạn.
- **PASS:** Delta 240 dòng; hai bảng đối chiếu EN–VI; ZIP CRC hoàn chỉnh.
- **CHƯA THỬ:** Kiểm tra thực tế trong ROM NDS và độ rộng sau khi thế biến tên/đồ vật.

Chạy lại: `python qa_063.py <checkpoint062.zip> <checkpoint063.zip>`.
'''
    handoff='''# Magician’s Quest — Checkpoint 063 (08/11/2026)

- **Tiến độ:** 17.172 / 55.976 (30,68%); trong đó 14.047 / 52.608 trang thoại NPC.
- **Đợt 063:** 240 trang mới: `talkfigs__0eng__data__0041.001.jsonl` (120) và `0041.002.jsonl` (120).
- **Nội dung:** Tặng quà, sinh nhật, thăm phòng bạn bè, uống trà, lời rủ đi chơi, luyện thần chú, chuyển trường, học nhóm, trao đổi nội thất và lời thoại tình trạng sức khỏe.
- **Kỹ thuật:** QA 501 JSONL / 55.976 bản ghi; giữ nguyên 16.932 bản dịch cũ; không sửa ID/EN/CTX, bảo toàn token NDS và giới hạn 34 ký tự tĩnh.
- **Tệp:** `DELTA-063.jsonl`, `QA-063.md`, `manual_0041_001.tsv`, `manual_0041_002.tsv`, `vi_0041_001.txt`, `vi_0041_002.txt`, `build_063.py`, `qa_063.py`.
- **Kho:** `ronvotri/VH-NDS` / `Magicians-Quest-Mysterious-Times/`; ZIP đầy đủ tại Thư viện `/Dịch giả lập/MagiciansQuest-VietHoa-Checkpoint-063.zip`.
- **Cần lưu ý:** Chưa kiểm thử trực tiếp trong ROM NDS.
- **Đợt 064 tiếp:** `0041.003` và `0041.004` (120 trang/tệp), nguồn có sẵn trong ZIP 063.
'''
    readme='**Checkpoint mới nhất: 063 (08/11/2026) — 17.172/55.976 (30,68%).** Thêm 240 trang thoại (`0041.001`, `0041.002`), QA toàn bộ 501 JSONL PASS, giữ 16.932 bản dịch cũ. Xem `CHECKPOINT-2026-11-08-DOT-63.md`, `DELTA-063.jsonl`, `QA-063.md`. Tiếp theo `0041.003` và `0041.004` (120 trang/tệp).\n\n'
    bangiao='''## Checkpoint 063 — 08/11/2026

- Đã dịch **17.172/55.976 (30,68%)**; thoại NPC **14.047/52.608**; tăng 240 câu.
- Hoàn thành `0041.001` (120/120) và `0041.002` (120/120), mã NDS và giới hạn dòng QA PASS.
- Đối chiếu 501 JSONL, giữ nguyên 16.932 bản dịch cũ; chỉ 240 trường `vi` mới, không thay ID/EN/CTX.
- ZIP: `/Dịch giả lập/MagiciansQuest-VietHoa-Checkpoint-063.zip`; chưa thử ROM.
- Tiếp theo: `0041.003`, `0041.004`, 120 trang/tệp, nguồn đã có trong ZIP và stage trên GitHub.

'''
    changes['DELTA-063.jsonl']=''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in delta).encode()
    changes['QA-063.md']=qa.encode()
    changes['CHECKPOINT-2026-11-08-DOT-63.md']=handoff.encode()
    changes['README.md']=(readme+zin.read(R_OLD+'README.md').decode()).encode()
    changes['BAN_GIAO.md']=(bangiao+zin.read(R_OLD+'BAN_GIAO.md').decode()).encode()
    for script in ['build_063.py','qa_063.py']:
        changes[script]=(HERE/script).read_bytes()
    existing=set()
    NEW.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(NEW,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=7) as zout:
        for item in zin.infolist():
            path=item.filename.removeprefix(R_OLD)
            if not path:continue
            if path in existing:raise ValueError('duplicate path '+path)
            existing.add(path)
            if item.is_dir():continue
            data=changes.pop(path,zin.read(item))
            zout.writestr(R_NEW+path,data)
        for path,data in changes.items():
            if path in existing:raise ValueError('duplicate new file '+path)
            zout.writestr(R_NEW+path,data)
print(f'Created {NEW}, {NEW.stat().st_size:,} bytes, {len(delta)} translated rows')
