#!/usr/bin/env python3
"""Rebuild full checkpoint 066 from ZIP 065; only fill `vi` in 0041.007 and 0041.008.

Usage: python build_066.py old065.zip output066.zip
"""
import sys, re, json, zipfile, unicodedata, collections, hashlib
from pathlib import Path
from mq066_translate import MANUAL_007,MANUAL_008
HERE=Path(__file__).resolve().parent
OLD=Path(sys.argv[1]) if len(sys.argv)>1 else Path('/mnt/data/MagiciansQuest-VietHoa-Checkpoint-065.zip')
NEW=Path(sys.argv[2]) if len(sys.argv)>2 else Path('/mnt/data/MagiciansQuest-VietHoa-Checkpoint-066.zip')
ROOT_OLD='MagiciansQuest_065/'
ROOT_NEW='MagiciansQuest_066/'
TOKEN=re.compile(r"\$\d{3}(?:'[0-9-]+)*;")
PREFIX=re.compile(r"^(?:\$(?:034|024|023|022|004|040)(?:['0-9-]+)*;)+")
SUFFIX=re.compile(r"(?:\$(?:079|074|019|018|073|033|085)(?:['0-9-]+)*;)+$")
TARGETS={'0041.007':MANUAL_007,'0041.008':MANUAL_008}

def split(s):
    m=PREFIX.match(s);pre=m.group(0) if m else ''
    body=s[len(pre):];m=SUFFIX.search(body)
    return pre,body[:m.start()] if m else body, m.group(0) if m else ''

def validate(row,vi):
    assert isinstance(vi,str) and vi and unicodedata.normalize('NFC',vi)==vi,(row['id'],'empty / NFC')
    assert TOKEN.findall(row['en'])==TOKEN.findall(vi),(row['id'],'NDS tokens',TOKEN.findall(row['en']),TOKEN.findall(vi))
    assert vi.count('▼')<=3,(row['id'],'break count')
    assert not any(c in vi for c in '\r\n\t'),(row['id'],'raw line break')
    assert all(len(TOKEN.sub('',v))<=34 for v in vi.split('▼')),(row['id'],'static width',[(len(TOKEN.sub('',v)),v) for v in vi.split('▼')])

with zipfile.ZipFile(OLD) as z:
    assert z.testzip() is None,'Input zip CRC failure'
    paths=[p for p in z.namelist() if p.startswith(ROOT_OLD+'translation/') and p.endswith('.jsonl')]
    assert len(paths)==501,len(paths)
    prev=collections.defaultdict(collections.Counter)
    total=old_trans=0
    for p in paths:
        for l in z.read(p).decode('utf-8').splitlines():
            r=json.loads(l);total+=1
            if r['vi'] is not None:
                old_trans+=1
                prev[split(r['en'])[1]].update([split(r['vi'])[1]])
    assert (total,old_trans)==(55976,17652),(total,old_trans)
    changes={};delta=[];stats=[]
    for suffix,manual in TARGETS.items():
        rel=f'translation/04-thoai/talkfigs__0eng__data__{suffix}.jsonl'
        src=[json.loads(x) for x in z.read(ROOT_OLD+rel).decode('utf-8').splitlines()]
        assert len(src)==120 and all(r['vi'] is None for r in src),suffix
        unique=list(dict.fromkeys(split(r['en'])[1] for r in src))
        assert len(unique)==(55 if suffix.endswith('007') else 33),(suffix,len(unique))
        assert all(isinstance(i,int) and 0<=i<len(unique) for i in manual),suffix
        lookup={}
        for i,en in enumerate(unique):
            if i in manual:lookup[en]=manual[i]
            elif prev[en]:lookup[en]=prev[en].most_common(1)[0][0]
            else:raise AssertionError((suffix,i,en,'missing manual translation'))
        out=[];table=['id\ten\tvi\tctx']
        manual_pages=0
        for r in src:
            pre,en,tail=split(r['en'])
            newvi=unicodedata.normalize('NFC',pre+lookup[en]+tail)
            validate(r,newvi)
            rr={**r,'vi':newvi};out.append(rr);delta.append(rr)
            table.append('\t'.join(str(rr[k]) for k in ('id','en','vi','ctx')))
            if en in {unique[i] for i in manual}:manual_pages+=1
        changes[rel]=(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in out)).encode('utf-8')
        changes[f'manual_{suffix.replace(".","_")}.tsv']=('\n'.join(table)+'\n').encode('utf-8')
        changes[f'vi_{suffix.replace(".","_")}.txt']=('\n'.join(split(r['vi'])[1] for r in out)+'\n').encode('utf-8')
        # Newly curated lines from this file can be safely reused in subsequent target file.
        for en,vn in lookup.items():prev[en].update([vn])
        stats.append((suffix,len(src),len(unique),len(manual),manual_pages))
    assert len(delta)==240
    changes['DELTA-066.jsonl']=(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in delta)).encode('utf-8')
    after=old_trans+len(delta);npc=14527+len(delta);pct=100*after/total
    assert (after,npc)==(17892,14767)
    changes['QA-066.md']=f'''# QA — Magician’s Quest · Đợt 066

- **PASS:** Diff checkpoint 065 → 066 trên 501 JSONL / 55.976 bản ghi.
- **PASS:** Điền đúng 240 trường `vi`: `0041.007` 120 và `0041.008` 120. **17.652 → {after:,}/55.976 ({pct:.2f}%)**; thoại NPC **14.527 → {npc:,}/52.608**.
- **PASS:** Giữ 17.652 bản dịch cũ, 499 tệp JSONL khác byte-identical; mọi ID/EN/CTX giữ nguyên.
- **PASS:** Các token `$...;` nguyên thứ tự, Unicode NFC, ≤3 `▼` và ≤34 ký tự tĩnh mỗi đoạn.
- **PASS:** Delta, hai bảng EN–VI, ZIP CRC và QA chéo checkpoint.
- **CHƯA KIỂM THỬ:** Hiển thị trong ROM NDS và độ dài thực tế của biến động.
'''.encode('utf-8')
    changes['CHECKPOINT-2026-11-09-DOT-66.md']=f'''# Magician’s Quest — Checkpoint 066 (09/11/2026)

- **Tổng:** {after:,}/55.976 ({pct:.2f}%); NPC {npc:,}/52.608.
- **Mới:** 240 trang từ `0041.007` và `0041.008` (120/tệp); 88 mẫu câu tính riêng hai tệp.
- **Nội dung:** Hội thoại tin đồn, lời mời đi chơi, tình bạn, mối quan hệ, những lời kháo nhau trong trường.
- **QA:** 501 JSONL; chỉ thêm 240 trường `vi`, giữ nguyên toàn bộ 17.652 bản dịch cũ và ID/EN/CTX/tokens NDS.
- **Kèm:** `DELTA-066.jsonl`, `QA-066.md`, hai bảng `manual_0041_*.tsv`, script build và QA.
- **Lưu ZIP:** `/Dịch giả lập/MagiciansQuest-VietHoa-Checkpoint-066.zip`; GitHub `ronvotri/VH-NDS` trong `Magicians-Quest-Mysterious-Times/`.
- **Giới hạn:** Chưa kiểm thử trên ROM NDS; độ rộng văn bản có biến động cần thử thực tế.
- **Tiếp 067:** `0041.009` và `0041.010` (120 trang/tệp) đã có sẵn trong ZIP và được stage vào GitHub.
'''.encode('utf-8')
    pre_readme=f'**Checkpoint mới nhất: 066 (09/11/2026) — {after:,}/55.976 ({pct:.2f}%).** +240 trang thoại `0041.007`, `0041.008`; QA trên 501 JSONL PASS, bảo toàn 17.652 mục dịch cũ. Xem `CHECKPOINT-2026-11-09-DOT-66.md`, `DELTA-066.jsonl`, `QA-066.md`. Tiếp `0041.009` và `0041.010` (120 trang/tệp).\n\n'
    pre_handoff=f'''## Checkpoint 066 — 09/11/2026

- **{after:,}/55.976 ({pct:.2f}%)**, NPC **{npc:,}/52.608**, thêm 240 mục trong `0041.007`, `0041.008`.
- Giọng học trò tớ–cậu, mã NDS bảo toàn, 499 tệp ngoài đợt byte-identical.
- QA tất cả 501 JSONL / 55.976 bản ghi: giữ 17.652 mục dịch trước, thêm đúng 240 `vi`.
- ZIP đầy đủ: `/Dịch giả lập/MagiciansQuest-VietHoa-Checkpoint-066.zip`; chưa thử ROM thật.
- Tiếp 067: `0041.009`, `0041.010` — nguồn có trong ZIP và stage GitHub.

'''
    changes['README.md']=(pre_readme+z.read(ROOT_OLD+'README.md').decode('utf-8')).encode('utf-8')
    changes['BAN_GIAO.md']=(pre_handoff+z.read(ROOT_OLD+'BAN_GIAO.md').decode('utf-8')).encode('utf-8')
    for srcfile in ['build_066.py','qa_066.py','mq066_translate.py']:
        changes[srcfile]=(HERE/srcfile).read_bytes()
    with zipfile.ZipFile(NEW,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=7) as out:
        seen=set()
        for info in z.infolist():
            if info.is_dir():continue
            assert info.filename.startswith(ROOT_OLD),info.filename
            rel=info.filename[len(ROOT_OLD):]
            assert rel not in seen,('duplicate',rel)
            seen.add(rel)
            out.writestr(ROOT_NEW+rel,changes.pop(rel,z.read(info)))
        for rel,content in changes.items():
            assert rel not in seen,rel
            out.writestr(ROOT_NEW+rel,content)
print('BUILT',NEW,'BYTES',NEW.stat().st_size,'FILES',len(zipfile.ZipFile(NEW).namelist()))
print('STATS',stats,'PROGRESS',after,total,round(pct,2),'NPC',npc)
print('SHA256',hashlib.sha256(NEW.read_bytes()).hexdigest())
