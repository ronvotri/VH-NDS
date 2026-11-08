#!/usr/bin/env python3
"""Rebuild full Magician's Quest Vietnamese checkpoint 062 from checkpoint 061.
Usage: python build_062.py [checkpoint061.zip] [output062.zip]
Keep vi_0040_021.txt and vi_0040_022.txt next to this script.
"""
from __future__ import annotations
import collections, json, re, sys, unicodedata, zipfile
from pathlib import Path
HERE=Path(__file__).resolve().parent
OLD=Path(sys.argv[1]) if len(sys.argv)>1 else HERE/'MagiciansQuest-VietHoa-Checkpoint-061.zip'
NEW=Path(sys.argv[2]) if len(sys.argv)>2 else HERE/'MagiciansQuest-VietHoa-Checkpoint-062.zip'
TOKEN=re.compile(r"\$\d{3}(?:'[0-9-]+)*;")
PREFIX=re.compile(r"^((?:\$(?:024|023|022)(?:'[0-9-]+)*;)+)")
SUFFIX=re.compile(r"((?:\$(?:079|074|019)(?:'[0-9-]+)*;)+)$")
ROOT_OLD='MagiciansQuest_061/'
ROOT_NEW='MagiciansQuest_062/'
TARGETS=['0040.021','0040.022']
EXPECT=[120,60]
translations={}
manual={}
delta=[]
changed_content={}
with zipfile.ZipFile(OLD) as zin:
    old_list=zin.namelist()
    assert len([n for n in old_list if n.startswith(ROOT_OLD+'translation/') and n.endswith('.jsonl')])==501
    for suf,n_exp in zip(TARGETS,EXPECT):
        path=f'translation/04-thoai/talkfigs__0eng__data__{suf}.jsonl'
        records=[json.loads(s) for s in zin.read(ROOT_OLD+path).decode('utf-8').splitlines()]
        texts=(HERE/f'vi_{suf.replace("0040.","0040_")}.txt').read_text(encoding='utf-8').splitlines()
        assert len(records)==len(texts)==n_exp,(suf,len(records),len(texts))
        man=['id\ten\tvi\tctx']
        for r,body in zip(records,texts):
            assert r['vi'] is None,(r['id'],'already translated')
            pre=PREFIX.match(r['en']);post=SUFFIX.search(r['en'])
            value=(pre.group(1) if pre else '')+body+(post.group(1) if post else '')
            value=unicodedata.normalize('NFC',value)
            assert value and not any(c in value for c in '\r\n\t')
            assert TOKEN.findall(r['en'])==TOKEN.findall(value),(suf,r['id'],'token mismatch',TOKEN.findall(r['en']),TOKEN.findall(value))
            assert value.count('▼')<=3,(suf,r['id'],'breaks')
            assert all(len(TOKEN.sub('',segment))<=34 for segment in value.split('▼')),(suf,r['id'],'width',value)
            r['vi']=value
            delta.append(dict(r))
            man.append('\t'.join(str(r[key]) for key in ('id','en','vi','ctx')))
        changed_content[path]=(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in records)).encode('utf-8')
        manual[f'manual_{suf.replace("0040.","0040_")}.tsv']='\n'.join(man)+'\n'
    translated_before=16752
    translated_after=translated_before+180
    percentage=translated_after/55976*100
    assert round(percentage,2)==30.25,percentage
    qa=f'''# QA — Magician’s Quest · Đợt 062

- **PASS:** Đối chiếu checkpoint 061 → 062 trên toàn bộ 501 JSONL, 55.976 bản ghi.
- **PASS:** 180 trường `vi` mới: `0040.021` (120) và `0040.022` (60); tiến độ **16.752 → 16.932/55.976 (30,25%)**; NPC **13.627 → 13.807/52.608**.
- **PASS:** Bảo toàn `id`, `en`, `ctx`; 16.752 câu Việt cũ không bị sửa; 499 JSONL ngoài mục tiêu byte-identical.
- **PASS:** Token NDS theo đúng thứ tự, Unicode NFC, không CR/LF/TAB trong thoại, tối đa 3 `▼`, mỗi đoạn không quá 34 ký tự tĩnh (không tính token).
- **PASS:** 180 dòng delta, hai bảng đối chiếu EN–VI, ZIP CRC nguyên vẹn.
- **CHƯA THỬ:** ROM NDS và chiều rộng thực tế sau khi các biến động được thay bằng tên nhân vật.

Chạy lại: `python qa_062.py <checkpoint061.zip> <checkpoint062.zip>`.
'''
    handoff=f'''# Magician’s Quest — Checkpoint 062 (08/11/2026)

- **Tiến độ:** 16.932 / 55.976 (30,25%), trong đó 13.807 / 52.608 trang thoại NPC.
- **Đợt 062:** 180 trang mới. `talkfigs__0eng__data__0040.021.jsonl` 120/120 và `0040.022.jsonl` 60/60.
- **Nội dung:** Giấc mơ và quà, Chồn Gió, Vòng Bí Ẩn, Harpy tập hát, cô bé bán diêm, Griffin, Kraken, Golem; sau đó chuyện tình bạn, hẹn hò và các lựa chọn đi chơi.
- **Kỹ thuật:** 501 JSONL / 55.976 bản ghi QA PASS; giữ nguyên 16.752 bản dịch cũ; token, Unicode NFC, ngắt trang, giới hạn 34 ký tự tĩnh đều PASS. Chưa kiểm thử trong ROM NDS.
- **Tệp đính kèm:** `DELTA-062.jsonl`, `QA-062.md`, `manual_0040_021.tsv`, `manual_0040_022.tsv`, `vi_0040_021.txt`, `vi_0040_022.txt`, `build_062.py`, `qa_062.py`.
- **Kho lưu:** GitHub `ronvotri/VH-NDS`, thư mục `Magicians-Quest-Mysterious-Times`; ZIP tại Thư viện `/Dịch giả lập/MagiciansQuest-VietHoa-Checkpoint-062.zip`.
- **Đợt 063 tiếp:** `0041.001.jsonl` và `0041.002.jsonl`, 120 trang mỗi tệp; nguồn đã có trong checkpoint 062.
'''
    readme_intro='**Checkpoint mới nhất: 062 (08/11/2026) — 16.932/55.976 mục (30,25%).** Đã dịch thêm 180 trang NPC (`0040.021` 120, `0040.022` 60), QA toàn bộ 501 JSONL PASS, giữ 16.752 bản dịch cũ. Xem `CHECKPOINT-2026-11-08-DOT-62.md`, `DELTA-062.jsonl`, `QA-062.md`. Tiếp theo `0041.001` và `0041.002` (120 trang mỗi tệp).\n\n'
    bangiao_intro='## Checkpoint 062 — 08/11/2026\n\n- 16.932 / 55.976 mục (30,25%); thoại NPC 13.807 / 52.608; tăng 180 mục.\n- Hoàn tất `0040.021` (120/120) và `0040.022` (60/60).\n- QA toàn bộ 501 JSONL, chỉ đổi 180 trường `vi`; giữ nguyên ID/EN/CTX/token và toàn bộ 16.752 bản dịch cũ.\n- ZIP: Thư viện `/Dịch giả lập/MagiciansQuest-VietHoa-Checkpoint-062.zip`; chưa kiểm thử ROM.\n- Tiếp theo: `0041.001` và `0041.002` (120 trang/tệp), nguồn nằm trong ZIP.\n\n'
    new_files={**changed_content,**{name:text.encode() for name,text in manual.items()},
        'DELTA-062.jsonl':(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in delta)).encode(),
        'QA-062.md':qa.encode(),
        'CHECKPOINT-2026-11-08-DOT-62.md':handoff.encode(),
        'README.md':(readme_intro+zin.read(ROOT_OLD+'README.md').decode()).encode(),
        'BAN_GIAO.md':(bangiao_intro+zin.read(ROOT_OLD+'BAN_GIAO.md').decode()).encode()}
    for suf in TARGETS:
        new_files['vi_'+suf.replace('0040.','0040_')+'.txt']=(HERE/('vi_'+suf.replace('0040.','0040_')+'.txt')).read_bytes()
    for script in ('build_062.py','qa_062.py'):
        new_files[script]=(HERE/script).read_bytes()
    NEW.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(NEW,'w') as zout:
        for info in zin.infolist():
            name=info.filename
            assert name.startswith(ROOT_OLD)
            relative=name[len(ROOT_OLD):]
            data=new_files.pop(relative, None)
            if data is None:data=zin.read(name)
            info.filename=ROOT_NEW+relative
            zout.writestr(info,data)
        for rel,data in new_files.items():
            zout.writestr(ROOT_NEW+rel,data,compress_type=zipfile.ZIP_DEFLATED,compresslevel=6)
print(f'Built {NEW} ({NEW.stat().st_size:,} bytes); 180 pages added, 16,932/55,976')
