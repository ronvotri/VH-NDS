#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Batch 071 of Magician's Quest: Mysterious Times NDS localization.
Reuses translations on exact English match and fixes 4 faulty color-code placements
in THIS batch only. Does not alter historic translations.
"""
import collections
import datetime
import hashlib
import json
import pathlib
import re
import unicodedata
import zipfile

BASE = pathlib.Path('/mnt/data')
INZIP = BASE / 'MagiciansQuest-VietHoa-Checkpoint-070.zip'
OUTZIP = BASE / 'MagiciansQuest-VietHoa-Checkpoint-071.zip'
OLDROOT = 'MagiciansQuest_070/'
NEWROOT = 'MagiciansQuest_071/'
SUFFIXES = ('0041.017', '0041.018')
NEXT = ('0041.019', '0041.020')
PRE = re.compile(r"^(?:\$\d{3}(?:[\d'-]+)?;)+")
TOK = re.compile(r"\$\d{3}(?:[\d'-]+)?;")
# 240 distinct matching old English entries. Fix only these four items:
CORRECTIONS = {
    107: 'Bức $000\'3;tượng đá$000\'1; đâu thể▼tự dưng đứng dậy bỏ đi!▼Chuyện gì đã xảy ra?',
    109: 'Bức $000\'3;tượng đá$000\'1; ấy▼biến đi đâu rồi nhỉ?',
    114: 'Bức $000\'3;tượng đá$000\'1; ấy▼đã trở về chỗ cũ▼trong sảnh rồi.',
}
# The original English for 144 starts with a color code attached to Minotaur.
# Reorder the *entire* Vietnamese page to color Minotaur, not "Khóa".
FULL_CORRECTIONS = {
    144: 'Khóa huấn luyện của▼$000\'3;Minotaur$000\'1;▼đã kết thúc...'
}

def unpack_zip(path, root):
    with zipfile.ZipFile(path) as z:
        assert z.testzip() is None, f'ZIP CRC error: {path}'
        return {n.removeprefix(root): z.read(n) for n in z.namelist() if n.startswith(root) and not n.endswith('/')}

def read_rows(data):
    return [json.loads(x) for x in data.decode('utf8').splitlines()]

def serialize_rows(rows):
    return ''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in rows)

def verify_static(en, vi, desc):
    assert TOK.findall(en) == TOK.findall(vi), ('TOKEN',desc,TOK.findall(en),TOK.findall(vi))
    assert unicodedata.normalize('NFC',vi) == vi, ('NFC',desc)
    static_lines=[len(TOK.sub('',s)) for s in vi.split('▼')]
    assert len(static_lines)<=4, ('BREAKS',desc,len(static_lines))
    assert max(static_lines)<=34, ('WIDTH',desc,static_lines)
    assert not vi.endswith((' ','\n','\r','\t')), ('TRAIL_SPACE',desc)


def main():
    entries = unpack_zip(INZIP, OLDROOT)
    jsonpaths = sorted(p for p in entries if p.startswith('translation/') and p.endswith('.jsonl'))
    assert len(jsonpaths) == 501, len(jsonpaths)
    oldrows = {p:read_rows(entries[p]) for p in jsonpaths}
    assert sum(len(v) for v in oldrows.values()) == 55976
    oldtranslated=sum(x['vi'] is not None for rows in oldrows.values() for x in rows)
    assert oldtranslated==18852, oldtranslated

    pool=collections.defaultdict(collections.Counter)
    for rows in oldrows.values():
        for r in rows:
            if r['vi'] is not None:
                pool[PRE.sub('',r['en'])][PRE.sub('',r['vi'])]+=1

    sources = {s:oldrows[f'translation/04-thoai/talkfigs__0eng__data__{s}.jsonl'] for s in SUFFIXES}
    assert all(len(sources[s])==120 for s in SUFFIXES)
    assert all(r['vi'] is None for rows in sources.values() for r in rows)
    keys=list(dict.fromkeys(PRE.sub('',r['en']) for s in SUFFIXES for r in sources[s]))
    assert len(keys)==240, len(keys)
    assert set(CORRECTIONS)|set(FULL_CORRECTIONS)=={107,109,114,144}
    unmatched=[(i,k) for i,k in enumerate(keys) if k not in pool]
    assert not unmatched, unmatched[:20]

    lookup={}
    for i,k in enumerate(keys):
        reuse=pool[k].most_common(1)[0][0]
        vi=CORRECTIONS.get(i,reuse)
        if i not in FULL_CORRECTIONS:
            verify_static(k,vi,('unique',i))
        lookup[k]=vi

    updates={}
    changes=[]
    manual={}
    for s in SUFFIXES:
        result=[]
        for r in sources[s]:
            key=PRE.sub('',r['en'])
            i=keys.index(key)
            prefix=r['en'][:len(r['en'])-len(key)]
            vi=FULL_CORRECTIONS.get(i,prefix+lookup[key])
            verify_static(r['en'],vi,r['id'])
            assert r['vi'] is None
            newer=dict(r,vi=vi)
            result.append(newer)
            changes.append(dict(newer,file=f'translation/04-thoai/talkfigs__0eng__data__{s}.jsonl'))
        path=f'translation/04-thoai/talkfigs__0eng__data__{s}.jsonl'
        updates[path]=serialize_rows(result).encode('utf8')
        short=s.replace('.','_')
        manual[f'manual_{short}.tsv']='id\ten\tvi\tctx\n'+''.join('\t'.join([r['id'],r['en'],r['vi'],str(r.get('ctx',''))])+'\n' for r in result)
        manual[f'vi_{short}.txt']=''.join(r['vi']+'\n' for r in result)

    for next_s in NEXT:
        path=f'translation/04-thoai/talkfigs__0eng__data__{next_s}.jsonl'
        assert path in oldrows and len(oldrows[path])==120 and all(r['vi'] is None for r in oldrows[path])

    newentries = dict(entries)
    newentries.update(updates)
    newentries.update({p:v.encode('utf8') for p,v in manual.items()})
    newentries['DELTA-071.jsonl']=serialize_rows(changes).encode('utf8')
    stamp='2026-11-09'
    progress='19.092 / 55.976 (34,11%)'
    npc='15.967 / 52.608'
    checkpoint=f'''# Magician's Quest: Mysterious Times — checkpoint 071

- Ngày: 09/11/2026
- Tổng tiến độ: **{progress}**, tăng **240** so với checkpoint 070.
- Hội thoại NPC: **{npc}**.
- Phạm vi: `0041.017` và `0041.018` (120 trang/tệp).
- **240 mẫu tiếng Anh khác nhau**, cả 240 khớp chính xác nguồn đã dịch trong checkpoint 070. **236 mẫu dùng nguyên bản cũ**, **4 mẫu chỉnh vị trí / thiếu token tô màu tại lần xuất hiện mới** (chỉ 071).
- Thoại về nhà ma, Nhân sư, kỳ lân, rồng, người ngoài hành tinh, Krampus, Minotaur, người sói, Jack Frost, chuyện học đường và bạn bè.
- Giữ đúng cách xưng hô và giọng NPC; không lạm dụng tiếng lóng.
- Mã `$...;` và `▼` giữ nguyên thứ tự; không thay ID, EN hoặc CTX.
- Đã so sánh đầy đủ 501 JSONL / 55.976 bản ghi: chỉ điền 240 trường `vi` còn trống, giữ nguyên 18.852 bản dịch cũ.
- Unicode NFC, token, tối đa 34 ký tự tĩnh mỗi đoạn, tối đa 3 dấu `▼` trên trang.
- Chưa thử hiển thị trên ROM NDS; tên động được thay tại runtime có thể làm tràn ô chữ.
- Nguồn tiếp theo: `0041.019` và `0041.020` (120 trang/tệp, vẫn `vi:null`).
'''
    handoff=f'''## Checkpoint 071 — 09/11/2026

- Đã dịch `0041.017` + `0041.018`: **+240 trang**, tổng **{progress}**, thoại NPC **{npc}**.
- 240 mẫu EN đã có bản dịch trước; tái sử dụng 236 mẫu, chỉnh mã màu cho 4 mẫu trong đợt mới. Không đụng bản dịch cũ.
- QA so sánh 501 JSONL: 18.852 → 19.092, chỉ 240 trường `vi` mới; không đổi ID, EN, CTX, 499 tệp dịch khác.
- ZIP đầy đủ: `/Dịch giả lập/MagiciansQuest-VietHoa-Checkpoint-071.zip`.
- Chưa thử trên ROM NDS. Tiếp `0041.019` và `0041.020` (120 trang/tệp).

'''
    readme=f'''**Checkpoint mới nhất: 071 (09/11/2026) — {progress}.** Tăng 240 trang thoại NPC (`0041.017`, `0041.018`). Xem `CHECKPOINT-2026-11-09-DOT-71.md`, `QA-071.md` và `DELTA-071.jsonl`. Nguồn đợt 072 đã sẵn: `0041.019` + `0041.020`.

'''
    newentries['CHECKPOINT-2026-11-09-DOT-71.md']=checkpoint.encode('utf8')
    newentries['README.md']=(readme+entries['README.md'].decode('utf8')).encode('utf8')
    newentries['BAN_GIAO.md']=(handoff+entries['BAN_GIAO.md'].decode('utf8')).encode('utf8')
    newentries['mq071_translate.py']=pathlib.Path(__file__).read_bytes()

    changeset=[]
    total=0;oldtotal=0
    for p in jsonpaths:
        old=oldrows[p]
        new=read_rows(newentries[p])
        assert len(old)==len(new),('ROWCOUNT',p)
        for i,(a,b) in enumerate(zip(old,new)):
            assert list(a.keys())==list(b.keys()),('KEYS',p,i)
            assert all(a[k]==b[k] for k in a if k!='vi'),('SOURCE_CHANGED',p,i)
            oldtotal += a['vi'] is not None
            total += b['vi'] is not None
            if a['vi']!=b['vi']:
                changeset.append((p,i))
                assert a['vi'] is None and isinstance(b['vi'],str),('WRONG_VI_CHANGE',p,i)
                assert p in updates,('WRONG_FILE',p)
                verify_static(b['en'],b['vi'],(p,i))
        if p not in updates:
            assert newentries[p]==entries[p],('BYTE_CHANGED',p)
    assert oldtotal==18852 and total==19092 and len(changeset)==240,(oldtotal,total,len(changeset))
    assert len(set(p for p,i in changeset))==2

    qa=f'''# QA — Magician's Quest checkpoint 071

- **PASS**: kiểm tra đầy đủ {len(jsonpaths)} JSONL / 55.976 bản ghi.
- Từ checkpoint 070 sang 071: **18.852 → 19.092**, đúng 240 `vi` mới.
- Chỉ thay trường `vi` của `0041.017` (120 bản ghi) và `0041.018` (120); mọi ID, EN, CTX và 18.852 `vi` cũ giữ nguyên, 499 tệp JSONL khác giống hệt từng byte.
- 240 mẫu EN khác nhau đều trùng chính xác nội dung đã dịch trước đó (không tính prefix engine). 236 mẫu tái dùng nguyên văn, 4 mẫu sửa vị trí mã màu ở các trang 071 (ID mẫu 107, 109, 114, 144).
- Mã `$...;` so khớp thứ tự 100%; Unicode NFC; tối đa 34 ký tự tĩnh/đoạn sau khi loại mã, không quá 3 `▼`/trang.
- `0041.019` và `0041.020` đã có trong ZIP, 120 dòng/tệp, toàn bộ `vi:null`.
- **Giới hạn**: chưa kiểm thử trong ROM Nintendo DS hoặc sau khi thay thế biến tên runtime.
'''
    newentries['QA-071.md']=qa.encode('utf8')
    with zipfile.ZipFile(OUTZIP,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p,data in sorted(newentries.items()):
            z.writestr(NEWROOT+p,data)
    with zipfile.ZipFile(OUTZIP) as z:
        assert z.testzip() is None
        assert len(z.namelist())==len(newentries)
        assert len([n for n in z.namelist() if n.startswith(NEWROOT+'translation/') and n.endswith('.jsonl')])==501
    digest=hashlib.sha256(OUTZIP.read_bytes()).hexdigest()
    print('PASS',OUTZIP,'file_count',len(newentries),'bytes',OUTZIP.stat().st_size,'sha256',digest)
    print('old',oldtotal,'new',total,'changes',len(changeset),'distinct EN',len(keys),'reused intact',len(keys)-len(CORRECTIONS)-len(FULL_CORRECTIONS),'color fixes',len(CORRECTIONS)+len(FULL_CORRECTIONS))

    # Staging files for atomic GitHub commit, all from validated newentries.
    stage=BASE/'mq071stage'
    stage.mkdir(exist_ok=True)
    staging=[
        f'translation/04-thoai/talkfigs__0eng__data__{SUFFIXES[0]}.jsonl',
        f'translation/04-thoai/talkfigs__0eng__data__{SUFFIXES[1]}.jsonl',
        'manual_0041_017.tsv','manual_0041_018.tsv',
        'DELTA-071.jsonl','QA-071.md','CHECKPOINT-2026-11-09-DOT-71.md','mq071_translate.py',
        f'translation/04-thoai/talkfigs__0eng__data__{NEXT[0]}.jsonl',
        f'translation/04-thoai/talkfigs__0eng__data__{NEXT[1]}.jsonl',
        'README.md','BAN_GIAO.md','vi_0041_017.txt','vi_0041_018.txt'
    ]
    for i,p in enumerate(staging):
        f=stage/f'{i:02}.txt'
        f.write_bytes(newentries[p])
        assert f.stat().st_size>0
    (stage/'manifest.json').write_text(json.dumps({'paths':staging,'files':[{'p':p,'length':len(newentries[p]),'lines':newentries[p].count(b'\n')} for p in staging]},ensure_ascii=False,indent=2),encoding='utf8')
    print('STAGING',len(staging),'staged files ready')

if __name__=='__main__':main()
