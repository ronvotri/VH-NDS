#!/usr/bin/env python3
"""Create a complete Magician's Quest checkpoint 065 from original checkpoint 064.
Only fills `vi` for 0041.005 / 0041.006; preserves every other source row byte-identically.
"""
from __future__ import annotations
import sys,collections,hashlib,json,re,unicodedata,zipfile
from pathlib import Path
from mq065_translate import MANUAL_005,MANUAL_006
HERE=Path(__file__).resolve().parent
OLD=Path(sys.argv[1]) if len(sys.argv)>1 else Path('/mnt/data/MagiciansQuest-VietHoa-Checkpoint-064.zip')
NEW=Path(sys.argv[2]) if len(sys.argv)>2 else Path('/mnt/data/MagiciansQuest-VietHoa-Checkpoint-065.zip')
ROOT_OLD='MagiciansQuest_064/'
ROOT_NEW='MagiciansQuest_065/'
TOKEN=re.compile(r"\$\d{3}(?:'[0-9-]+)*;")
PREFIX=re.compile(r"^(?:\$(?:034|024|023|022|004|040)(?:'[0-9-]+)*;)+")
SUFFIX=re.compile(r"(?:\$(?:079|074|019|018|073|033|085)(?:'[0-9-]+)*;)+$")
TARGETS={'0041.005':MANUAL_005,'0041.006':MANUAL_006}

def split_en(en):
    m=PREFIX.match(en)
    pre=m.group(0) if m else ''
    body=en[len(pre):]
    n=SUFFIX.search(body)
    suf=n.group(0) if n else ''
    return pre,body[:-len(suf)] if suf else body,suf

def check(row,vi):
    assert isinstance(vi,str) and vi and unicodedata.normalize('NFC',vi)==vi,(row['id'],'nfc/empty')
    assert TOKEN.findall(vi)==TOKEN.findall(row['en']),(row['id'],'token',TOKEN.findall(row['en']),TOKEN.findall(vi))
    assert vi.count('▼')<=3,(row['id'],'break count')
    assert not any(c in vi for c in '\r\n\t'),(row['id'],'physical break/tab')
    assert all(len(TOKEN.sub('',part))<=34 for part in vi.split('▼')),(row['id'],'width',[(len(TOKEN.sub('',p)),p) for p in vi.split('▼')])

with zipfile.ZipFile(OLD) as zin:
    assert zin.testzip() is None,'source ZIP CRC failure'
    translation={}
    for n in zin.namelist():
        if n.startswith(ROOT_OLD+'translation/') and n.endswith('.jsonl'):
            translation[n]=[json.loads(x) for x in zin.read(n).decode('utf-8').splitlines()]
    assert len(translation)==501,len(translation)
    previous=collections.defaultdict(collections.Counter)
    for rows in translation.values():
        for row in rows:
            if row['vi'] is not None:
                previous[split_en(row['en'])[1]][split_en(row['vi'])[1]]+=1
    total=sum(len(x) for x in translation.values())
    before=sum(sum(r['vi'] is not None for r in rows) for rows in translation.values())
    assert (total,before)==(55976,17412),(total,before)
    changes={};delta=[];stats=[]
    for suf,manual in TARGETS.items():
        rel=f'translation/04-thoai/talkfigs__0eng__data__{suf}.jsonl'
        rows=translation[ROOT_OLD+rel]
        assert len(rows)==120 and all(r['vi'] is None for r in rows),suf
        uniques=list(dict.fromkeys(split_en(row['en'])[1] for row in rows))
        assert len(uniques)==(52 if suf.endswith('005') else 37),(suf,len(uniques))
        assert all(i<len(uniques) for i in manual),suf
        translations={}
        for i,english in enumerate(uniques):
            if i in manual:
                translations[english]=manual[i]
            elif previous[english]:
                translations[english]=previous[english].most_common(1)[0][0]
            else:
                raise AssertionError((suf,i,english,'no translation found'))
        output=[];table=['id\ten\tvi\tctx'];new_pages=old_pages=0
        for row in rows:
            pre,body,tail=split_en(row['en'])
            vn=unicodedata.normalize('NFC',pre+translations[body]+tail)
            check(row,vn)
            o={**row,'vi':vn};output.append(o);delta.append(o)
            table.append('\t'.join(str(o[key]) for key in ('id','en','vi','ctx')))
            if body in [uniques[i] for i in manual]:new_pages+=1
            else:old_pages+=1
        changes[rel]=''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in output).encode('utf-8')
        changes[f'manual_{suf.replace(".","_")}.tsv']=('\n'.join(table)+'\n').encode('utf-8')
        changes[f'vi_{suf.replace(".","_")}.txt']=('\n'.join(split_en(r['vi'])[1] for r in output)+'\n').encode('utf-8')
        stats.append((suf,len(rows),len(uniques),len(manual),old_pages,new_pages))
    assert len(delta)==240
    changes['DELTA-065.jsonl']=''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in delta).encode('utf-8')
    after=before+len(delta)
    assert after==17652
    npc=14287+len(delta)
    pct=after/total*100
    qa=f'''# QA — Magician’s Quest · Đợt 065

- **PASS:** So sánh checkpoint 064 → 065 trên 501 JSONL / 55.976 bản ghi.
- **PASS:** Điền 240 trường `vi` trong `0041.005` và `0041.006` (120/tệp), **17.412 → 17.652/55.976 ({pct:.2f}%)**; NPC **14.287 → {npc}/52.608**.
- **PASS:** 17.412 bản dịch trước giữ nguyên; 499 JSONL còn lại byte-identical; không thay ID/EN/CTX.
- **PASS:** Các mã `$...;` giữ đúng trình tự, Unicode NFC, tối đa 3 `▼`, tối đa 34 ký tự tĩnh trên mỗi đoạn.
- **PASS:** Delta 240 bản ghi, 2 bảng EN–VI, ZIP CRC, và QA chéo checkpoint.
- **CHƯA KIỂM THỬ:** ROM NDS; độ rộng khi biến tên động được thay trong game.
'''
    checkpoint=f'''# Magician’s Quest — Checkpoint 065 (08/11/2026)

- **Tổng:** {after:,}/55.976 ({pct:.2f}%); NPC {npc:,}/52.608.
- **Mới:** 240 trang, `0041.005` và `0041.006` (120 mỗi tệp).
- **Nội dung:** Tương tác tặng vật phẩm, đi chơi, đến trường; tin đồn về quan hệ, bùa yêu, câu cá, bắt bọ, niệm chú và chuyện trò ở trường.
- **QA:** 501 JSONL / 55.976 bản ghi; chỉ điền 240 `vi`, bảo toàn 17.412 bản dịch cũ, ID, EN, CTX và token NDS.
- **Tệp kèm:** `DELTA-065.jsonl`, `QA-065.md`, bảng `manual_0041_005.tsv`, `manual_0041_006.tsv`, script build/QA.
- **GitHub:** `ronvotri/VH-NDS`, thư mục `Magicians-Quest-Mysterious-Times/`.
- **ZIP bàn giao:** `/Dịch giả lập/MagiciansQuest-VietHoa-Checkpoint-065.zip`.
- **Giới hạn:** chưa kiểm thử hiển thị trên ROM NDS, đặc biệt biến động.
- **Tiếp 066:** `0041.007` và `0041.008` (120 trang/tệp), nguồn sẵn trong ZIP.
'''
    readme=f'**Checkpoint mới nhất: 065 (08/11/2026) — {after:,}/55.976 ({pct:.2f}%).** +240 trang thoại (`0041.005`, `0041.006`). QA toàn 501 JSONL PASS; giữ nguyên 17.412 bản dịch cũ. Xem `CHECKPOINT-2026-11-08-DOT-65.md`, `DELTA-065.jsonl`, `QA-065.md`. Tiếp `0041.007`, `0041.008` (120 trang/tệp).\n\n'
    handoff=f'''## Checkpoint 065 — 08/11/2026

- **{after:,}/55.976 ({pct:.2f}%)**, NPC **{npc:,}/52.608**; bổ sung 240 trang tiếng Việt.
- `0041.005` và `0041.006`: 120/120 mỗi tệp. Dùng giọng học trò tớ–cậu, giữ mã NDS.
- QA 501 tệp / 55.976 mục: chỉ thay 240 `vi`; giữ 17.412 bản dịch cũ, EN/ID/CTX, nguyên tệp khác.
- ZIP đầy đủ: `/Dịch giả lập/MagiciansQuest-VietHoa-Checkpoint-065.zip`, chưa kiểm thử ROM.
- Tiếp 066: `0041.007` và `0041.008`, mỗi tệp 120 trang. Nguồn có trong ZIP và stage ở GitHub.

'''
    changes['QA-065.md']=qa.encode('utf-8')
    changes['CHECKPOINT-2026-11-08-DOT-65.md']=checkpoint.encode('utf-8')
    changes['README.md']=(readme+zin.read(ROOT_OLD+'README.md').decode('utf-8')).encode('utf-8')
    changes['BAN_GIAO.md']=(handoff+zin.read(ROOT_OLD+'BAN_GIAO.md').decode('utf-8')).encode('utf-8')
    changes['build_065.py']=Path(__file__).read_bytes()
    changes['qa_065.py']=(HERE/'qa_065.py').read_bytes()
    changes['mq065_translate.py']=(HERE/'mq065_translate.py').read_bytes()
    with zipfile.ZipFile(NEW,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=7) as zout:
        seen=set()
        for member in zin.infolist():
            path=member.filename.removeprefix(ROOT_OLD)
            if not path:continue
            assert path not in seen,('duplicate old',path)
            seen.add(path)
            if member.is_dir():continue
            data=changes.pop(path,zin.read(member))
            zout.writestr(ROOT_NEW+path,data)
        for path,data in changes.items():
            assert path not in seen,('duplicate new',path)
            zout.writestr(ROOT_NEW+path,data)
print('Built',NEW, f'{NEW.stat().st_size:,} bytes', 'total translated:',after,'NPC',npc,'pct',f'{pct:.2f}')
for stat in stats:print('stat suffix/rows/unique/manually translated unique/reused rows/manually translated rows',stat)
print('SHA256',hashlib.sha256(NEW.read_bytes()).hexdigest())
