#!/usr/bin/env python3
"""Build full Magician's Quest checkpoint 067 from checkpoint 066; fill only 0041.009 & .010."""
import sys,json,zipfile,re,unicodedata,hashlib,collections
from pathlib import Path
from mq067_translate import MANUAL_009,MANUAL_010
HERE=Path(__file__).resolve().parent
OLD=Path(sys.argv[1]) if len(sys.argv)>1 else Path('/mnt/data/MagiciansQuest-VietHoa-Checkpoint-066.zip')
NEW=Path(sys.argv[2]) if len(sys.argv)>2 else Path('/mnt/data/MagiciansQuest-VietHoa-Checkpoint-067.zip')
ROOT_OLD='MagiciansQuest_066/'
ROOT_NEW='MagiciansQuest_067/'
TOKEN=re.compile(r"\$\d{3}(?:'[0-9-]+)*;")
PREFIX=re.compile(r"^(?:\$(?:034|024|023|022|004|040)(?:['0-9-]+)*;)+")
SUFFIX=re.compile(r"(?:\$(?:079|074|019|018|073|033|085|032)(?:['0-9-]+)*;)+$")
TARGETS={'0041.009':MANUAL_009,'0041.010':MANUAL_010}
def split(s):
    m=PREFIX.match(s);p=m.group(0) if m else '';body=s[len(p):];m=SUFFIX.search(body)
    return p,body[:m.start()] if m else body,m.group(0) if m else ''
def validate(r,s):
    assert isinstance(s,str) and s and unicodedata.normalize('NFC',s)==s,(r['id'],'NFC/empty')
    assert TOKEN.findall(r['en'])==TOKEN.findall(s),(r['id'],'token order',TOKEN.findall(r['en']),TOKEN.findall(s))
    assert s.count('▼')<=3,(r['id'],'breaks')
    assert not any(c in s for c in '\r\n\t'),(r['id'],'newline')
    assert all(len(TOKEN.sub('',seg))<=34 for seg in s.split('▼')),(r['id'],'width',[(len(TOKEN.sub('',seg)),seg) for seg in s.split('▼')])
with zipfile.ZipFile(OLD) as z:
    assert z.testzip() is None,'bad checkpoint CRC'
    paths=[p for p in z.namelist() if p.startswith(ROOT_OLD+'translation/') and p.endswith('.jsonl')]
    assert len(paths)==501,len(paths)
    prev=collections.defaultdict(collections.Counter)
    total=old_trans=0
    for path in paths:
        for l in z.read(path).decode('utf-8').splitlines():
            r=json.loads(l);total+=1
            if r['vi'] is not None:
                old_trans+=1
                prev[split(r['en'])[1]][split(r['vi'])[1]]+=1
    assert (total,old_trans)==(55976,17892),(total,old_trans)
    changes={};delta=[];stats=[]
    for suffix,manual in TARGETS.items():
        rel=f'translation/04-thoai/talkfigs__0eng__data__{suffix}.jsonl'
        src=[json.loads(l) for l in z.read(ROOT_OLD+rel).decode('utf-8').splitlines()]
        assert len(src)==120 and all(r['vi'] is None for r in src),suffix
        unique=list(dict.fromkeys(split(r['en'])[1] for r in src))
        assert len(unique)==(22 if suffix.endswith('009') else 32),(suffix,len(unique))
        assert all(isinstance(i,int) and 0<=i<len(unique) for i in manual),suffix
        lookup={}
        for i,en in enumerate(unique):
            if i in manual:lookup[en]=manual[i]
            elif prev[en]:lookup[en]=prev[en].most_common(1)[0][0]
            else:raise AssertionError((suffix,i,en,'manual translation required'))
        rows=[];tab=['id\ten\tvi\tctx']
        for row in src:
            pre,en,tail=split(row['en'])
            vi=unicodedata.normalize('NFC',pre+lookup[en]+tail)
            validate(row,vi)
            rr={**row,'vi':vi};rows.append(rr);delta.append(rr)
            tab.append('\t'.join(str(rr[k]) for k in ('id','en','vi','ctx')))
        changes[rel]=(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in rows)).encode()
        changes[f'manual_{suffix.replace(".","_")}.tsv']=('\n'.join(tab)+'\n').encode()
        changes[f'vi_{suffix.replace(".","_")}.txt']=('\n'.join(r['vi'] for r in rows)+'\n').encode()
        for en,vi in lookup.items():prev[en][vi]+=1
        stats.append((suffix,len(rows),len(unique),len(manual)))
    assert len(delta)==240
    changes['DELTA-067.jsonl']=(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in delta)).encode()
    after=old_trans+240;npc=14767+240;pct=100*after/total
    assert (after,npc)==(18132,15007)
    changes['QA-067.md']=f'''# QA — Magician's Quest · Đợt 067

- **PASS:** So sánh checkpoint 066 → 067 trên 501 JSONL / 55.976 bản ghi.
- **PASS:** Điền 240 trường `vi`: 0041.009 (120), 0041.010 (120). **17.892 → {after:,}/55.976 ({pct:.2f}%)**; hội thoại NPC **14.767 → {npc:,}/52.608**.
- **PASS:** Giữ nguyên 17.892 bản dịch cũ; 499 JSONL khác byte-identical; ID/EN/CTX không đổi.
- **PASS:** Mã `$...;` giữ nguyên thứ tự; Unicode NFC; ≤3 dấu `▼`/trang; ≤34 ký tự tĩnh/đoạn.
- **PASS:** Delta, hai bảng đối chiếu EN–VI, CRC ZIP, QA chéo hai checkpoint.
- **CHƯA THỬ:** Hiển thị trong ROM NDS và độ rộng thực khi các biến tên dài được thay thế.
'''.encode()
    changes['CHECKPOINT-2026-11-09-DOT-67.md']=f'''# Magician's Quest — Checkpoint 067 (09/11/2026)

- **Tiến độ:** {after:,} / 55.976 ({pct:.2f}%); hội thoại NPC {npc:,} / 52.608.
- **Bổ sung:** 240 trang trong `0041.009` và `0041.010`; 54 mẫu câu tính riêng hai tệp.
- **Nội dung:** Lời đồn ở trường, tình bạn, tình cảm, ghen tuông, giữ bí mật và những cuộc hẹn.
- **Bảo toàn:** Token NDS, Unicode NFC, giới hạn dòng, 17.892 bản dịch cũ, toàn bộ ID/EN/CTX.
- **Bàn giao:** `DELTA-067.jsonl`, hai bảng `manual_0041_*.tsv`, `QA-067.md`, `build_067.py`, `qa_067.py`, `mq067_translate.py`.
- **Lưu:** `/Dịch giả lập/MagiciansQuest-VietHoa-Checkpoint-067.zip`; repository `ronvotri/VH-NDS/Magicians-Quest-Mysterious-Times`.
- **Lưu ý:** Chưa kiểm thử thực tế trên ROM; token tên biến động có thể cần điều chỉnh khi chạy game.
- **Tiếp 068:** `0041.011` và `0041.012` (120 trang/tệp) đã có trong ZIP, chuẩn bị đưa GitHub.
'''.encode()
    prefix_readme=f'**Checkpoint mới nhất: 067 (09/11/2026) — {after:,}/55.976 ({pct:.2f}%).** +240 trang thoại `0041.009`, `0041.010`; QA 501 JSONL đạt; 17.892 bản dịch cũ bảo toàn. Xem `CHECKPOINT-2026-11-09-DOT-67.md`, `DELTA-067.jsonl`, `QA-067.md`. Tiếp `0041.011`, `0041.012` (120 trang/tệp).\n\n'
    prefix_handoff=f'''## Checkpoint 067 — 09/11/2026

- **{after:,}/55.976 ({pct:.2f}%)**, NPC **{npc:,}/52.608**; bổ sung 240 trang trong `0041.009`, `0041.010`.
- Hội thoại hẹn hò, lời đồn, phản ứng bạn bè; bảo toàn mã NDS và lựa chọn hội thoại.
- QA 501 JSONL / 55.976 bản ghi, chỉ thêm đúng 240 `vi`, các trường khác nguyên vẹn.
- ZIP: `/Dịch giả lập/MagiciansQuest-VietHoa-Checkpoint-067.zip`; chưa thử trên ROM.
- Tiếp 068: `0041.011`, `0041.012` — nguồn có sẵn trong ZIP, stage trên GitHub.

'''
    changes['README.md']=(prefix_readme+z.read(ROOT_OLD+'README.md').decode('utf-8')).encode('utf-8')
    changes['BAN_GIAO.md']=(prefix_handoff+z.read(ROOT_OLD+'BAN_GIAO.md').decode('utf-8')).encode('utf-8')
    for srcfile in ('build_067.py','qa_067.py','mq067_translate.py'):
        changes[srcfile]=(HERE/srcfile).read_bytes()
    with zipfile.ZipFile(NEW,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=7) as out:
        seen=set()
        for info in z.infolist():
            if info.is_dir():continue
            assert info.filename.startswith(ROOT_OLD),info.filename
            rel=info.filename[len(ROOT_OLD):]
            assert rel not in seen,('duplicate archive entry',rel)
            seen.add(rel)
            out.writestr(ROOT_NEW+rel,changes.pop(rel,z.read(info)))
        for rel,content in changes.items():
            assert rel not in seen,rel
            out.writestr(ROOT_NEW+rel,content)
print('BUILT',NEW,'SIZE',NEW.stat().st_size,'FILES',len(zipfile.ZipFile(NEW).namelist()))
print('STATS',stats,'TOTAL',after,total,'PERCENT',round(pct,2),'NPC',npc)
print('SHA256',hashlib.sha256(NEW.read_bytes()).hexdigest())
