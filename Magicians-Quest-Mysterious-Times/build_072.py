#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reproducible Magician's Quest checkpoint 072 from full checkpoint 071.

This batch contains an entire second set of 240 NPC pages whose English strings
match earlier translated strings. Reuse the exact approved Vietnamese string,
excluding only the new page's leading actor/portrait engine prefix, and reinstate
that page's own original prefix. Avoid splitting color-code $000'3; by preserving
it as part of the text, not the leading engine prefix.
"""
from __future__ import annotations
import argparse
import collections
import hashlib
import json
import pathlib
import re
import unicodedata
import zipfile

BASE = pathlib.Path('/mnt/data')
OLDZIP = BASE/'MagiciansQuest-VietHoa-Checkpoint-071.zip'
NEWZIP = BASE/'MagiciansQuest-VietHoa-Checkpoint-072.zip'
ROOT_OLD='MagiciansQuest_071/'
ROOT_NEW='MagiciansQuest_072/'
TARGETS=('0041.019','0041.020')
NEXT=('0041.021','0041.022')
ENGINE_PREFIX=re.compile(r"^(?:\$(?:024|023|022|034|040)(?:[\d'-]+)?;)+")
TOK=re.compile(r"\$\d{3}(?:[\d'-]+)?;")
DATE='2026-11-09'

def parse_jsonl(data:bytes):
    return [json.loads(line) for line in data.decode('utf-8').splitlines()]

def emit_jsonl(rows):
    return ''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in rows).encode('utf-8')

def verify(en:str,vi:str,ref:str):
    assert TOK.findall(en)==TOK.findall(vi),(ref,'token difference',TOK.findall(en),TOK.findall(vi))
    assert unicodedata.normalize('NFC',vi)==vi,(ref,'non NFC')
    assert vi.count('▼')<=3,(ref,'too many breaks')
    static=[len(TOK.sub('',segment)) for segment in vi.split('▼')]
    assert max(static)<=34,(ref,'overlong',static)
    assert vi.rstrip()==vi,(ref,'trailing whitespace')


def main():
    with zipfile.ZipFile(OLDZIP) as z:
        assert z.testzip() is None,'old archive CRC failed'
        old={n[len(ROOT_OLD):]:z.read(n) for n in z.namelist() if n.startswith(ROOT_OLD) and not n.endswith('/')}
    json_files=sorted(n for n in old if n.startswith('translation/') and n.endswith('.jsonl'))
    assert len(json_files)==501,(len(json_files),'jsonl count')
    oldrows={path:parse_jsonl(old[path]) for path in json_files}
    assert sum(map(len,oldrows.values()))==55976
    oldtotal=sum(row['vi'] is not None for rows in oldrows.values() for row in rows)
    assert oldtotal==19092,oldtotal
    pool=collections.defaultdict(collections.Counter)
    for rows in oldrows.values():
        for row in rows:
            if row['vi'] is not None:
                en=ENGINE_PREFIX.sub('',row['en'])
                vi=ENGINE_PREFIX.sub('',row['vi'])
                pool[en][vi]+=1
    changes=[]
    new=dict(old)
    records_by_suffix={}
    for suffix in TARGETS:
        path=f'translation/04-thoai/talkfigs__0eng__data__{suffix}.jsonl'
        originals=oldrows[path]
        assert len(originals)==120
        assert all(r['vi'] is None for r in originals)
        processed=[]
        for orig in originals:
            key=ENGINE_PREFIX.sub('',orig['en'])
            assert key in pool,(orig['id'],'no prior translation')
            assert len(pool[key])==1,(orig['id'],'conflicting prior translations')
            old_vi=next(iter(pool[key]))
            page_prefix=orig['en'][:len(orig['en'])-len(key)]
            vi=page_prefix+old_vi
            verify(orig['en'],vi,orig['id'])
            modified=dict(orig)
            modified['vi']=vi
            processed.append(modified)
            changes.append(dict(modified,file=path))
        records_by_suffix[suffix]=processed
        new[path]=emit_jsonl(processed)
        short=suffix.replace('.','_')
        new[f'manual_{short}.tsv']=('id\ten\tvi\tctx\n'+''.join('\t'.join([r['id'],r['en'],r['vi'],str(r.get('ctx',''))])+'\n' for r in processed)).encode('utf-8')
        new[f'vi_{short}.txt']=(''.join(r['vi']+'\n' for r in processed)).encode('utf-8')
    assert len(changes)==240
    assert len(set(ENGINE_PREFIX.sub('',r['en']) for r in changes))==240
    for suffix,expected in [('0041.021',120),('0041.022',6)]:
        path=f'translation/04-thoai/talkfigs__0eng__data__{suffix}.jsonl'
        assert len(oldrows[path])==expected and all(r['vi'] is None for r in oldrows[path])
    new['DELTA-072.jsonl']=emit_jsonl(changes)
    percentage=19332/55976*100
    pct=f'{percentage:.2f}'.replace('.',',')
    context=f'''# Magician's Quest: Mysterious Times — Checkpoint 072

- Ngày: {DATE}
- Tiến độ: **19.332/55.976 ({pct}%)**, +240 trang so với 071.
- Hội thoại NPC: **16.207/52.608**.
- Hoàn tất `0041.019` và `0041.020`, mỗi tệp 120/120 trang.
- 240 bản ghi có 240 câu EN khác nhau trong phạm vi đợt; **tất cả 240 đều đã được dịch ở checkpoint cũ**. Tái sử dụng văn phong được duyệt, không nhận là 240 câu mới viết.
- Tệp `0041.019`: tiên cá, Siren, người tuyết, thú trắng, Cấm Thư, Halloween, cổng thế giới và những giấc mơ.
- Tệp `0041.020`: giấc mơ, ma quỷ, các bí ẩn trong trường, người bạn kỳ lạ và những vòng phép.
- Giữ toàn bộ mã `$...;` theo thứ tự, không quá 3 `▼`, tối đa 34 ký tự tĩnh mỗi đoạn; không đổi EN, ID, CTX.
- So sánh toàn bộ 501 JSONL / 55.976 bản ghi trước và sau: giữ nguyên 19.092 bản dịch cũ; chỉ thêm đúng 240 trường `vi` trong hai tệp.
- Chưa kiểm thử ROM thật hoặc tên động sau khi runtime chèn biến `$500;`.
- Đợt 073: `0041.021` (120 trang) và `0041.022` (6 trang), nguồn đã sẵn trong ZIP.
'''
    qa=f'''# QA — Magician's Quest checkpoint 072

- **PASS**: 501 JSONL, 55.976 bản ghi; ZIP không lỗi CRC.
- 19.092 → 19.332 trường `vi` đã dịch: đúng **240** bản ghi mới.
- Chỉ thay `vi` trong `0041.019` (120) và `0041.020` (120); 499 JSONL khác giữ nguyên từng byte.
- Giữ nguyên 19.092 bản dịch cũ; tất cả ID, EN, CTX và thứ tự bản ghi không đổi.
- 240/240 câu EN có bản dịch trùng khớp trước đó (sau khi bỏ **chỉ** prefix actor/portrait `$024/$023/$022/$034/$040`), không đổi vị trí các token tô màu `$000'3;`.
- 240/240 dòng dịch mới: thứ tự token `$...;`, Unicode NFC, tối đa 34 ký tự tĩnh/đoạn, tối đa 3 dấu `▼` đều PASS.
- Tiếp theo: `0041.021` 120 trang và `0041.022` 6 trang, hiện `vi:null`.
- **Giới hạn:** chưa kiểm thử sau khi đóng gói vào ROM NDS hoặc mở rộng biến tên runtime.
'''
    new['CHECKPOINT-2026-11-09-DOT-72.md']=context.encode('utf-8')
    new['QA-072.md']=qa.encode('utf-8')
    new['README.md']=(f'**Checkpoint mới nhất: 072 (09/11/2026) — 19.332 / 55.976 ({pct}%).** +240 trang thoại NPC (`0041.019`, `0041.020`) bằng cách tái dùng 240 bản dịch đã kiểm tra từ đợt trước. Xem `CHECKPOINT-2026-11-09-DOT-72.md`, `QA-072.md`, `DELTA-072.jsonl`. Đợt 073: `0041.021` + `0041.022` (120 + 6 trang).\n\n'+old['README.md'].decode()).encode('utf-8')
    new['BAN_GIAO.md']=(f'## Checkpoint 072 — 09/11/2026\n\n- Đã dịch `0041.019` + `0041.020`: **240/240 trang**, **19.332 / 55.976 ({pct}%)**, NPC **16.207 / 52.608**.\n- 240 bản ghi dùng lại câu dịch trùng chính xác từ checkpoint cũ; giữ prefix riêng theo trang, không đổi mã trong câu.\n- QA 501 JSONL: chỉ thêm 240 `vi`, giữ 19.092 bản dịch trước và toàn bộ ID/EN/CTX.\n- ZIP đầy đủ: `/Dịch giả lập/MagiciansQuest-VietHoa-Checkpoint-072.zip`.\n- Chưa kiểm thử trên ROM. Tiếp `0041.021` (120) và `0041.022` (6).\n\n'+old['BAN_GIAO.md'].decode()).encode('utf-8')
    # Preserve all 501 records, verifying every record and every other file byte-for-byte.
    for path in json_files:
        oldr=oldrows[path]
        newr=parse_jsonl(new[path])
        assert len(newr)==len(oldr)
        for a,b in zip(oldr,newr):
            assert a['id']==b['id'] and a['en']==b['en'] and a.get('ctx')==b.get('ctx')
            assert set(a)==set(b)
            if a['vi'] is not None: assert a==b
            elif path not in (f'translation/04-thoai/talkfigs__0eng__data__{t}.jsonl' for t in TARGETS):assert a==b
        if path not in [f'translation/04-thoai/talkfigs__0eng__data__{t}.jsonl' for t in TARGETS]:
            assert old[path]==new[path],('byte mismatch',path)
    newtotal=sum(x['vi'] is not None for path in json_files for x in parse_jsonl(new[path]))
    assert newtotal==19332,newtotal
    # Include reproducibility script inside the ZIP.
    this_file=pathlib.Path(__file__)
    if this_file.exists():new['build_072.py']=this_file.read_bytes()
    with zipfile.ZipFile(NEWZIP,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for path,data in sorted(new.items()):z.writestr(ROOT_NEW+path,data)
    with zipfile.ZipFile(NEWZIP) as z:
        assert z.testzip() is None,'output archive CRC failed'
        assert len(z.namelist())==len(new)
    print(json.dumps(dict(checkpoint='072',old=oldtotal,new=newtotal,delta=len(changes),jsonl=len(json_files),records=sum(map(len,oldrows.values())),archive=str(NEWZIP),entries=len(new),bytes=NEWZIP.stat().st_size,sha256=hashlib.sha256(NEWZIP.read_bytes()).hexdigest(),next={'0041.021':120,'0041.022':6}),ensure_ascii=False,indent=2))

if __name__=='__main__':main()
