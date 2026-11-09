#!/usr/bin/env python3
"""Magician's Quest: additive checkpoint 075 from checkpoint 074.

Usage: python build_075.py --previous MagiciansQuest-VietHoa-Checkpoint-074.zip --output MagiciansQuest-VietHoa-Checkpoint-075.zip
Place mq075_translations.txt alongside script; mappings are numbered 001–091.
"""
from __future__ import annotations
import argparse
import collections
import csv
import hashlib
import io
import json
import pathlib
import re
import unicodedata
import zipfile

OLD='MagiciansQuest_074/'
NEW='MagiciansQuest_075/'
BATCH=('0042.003','0042.004')
NEXT=('0042.005','0042.006')
TOKEN=re.compile(r"\$\d{3}(?:'[-\d]+)*;")
PREFIX=re.compile(r"^(?:\$(?:024|023|022|034|040)(?:'[-\d]+)*;)+")
BASE=pathlib.Path(__file__).resolve().parent
BASE_COUNT=19698
TOTAL=55976


def body(s: str) -> str:
    return PREFIX.sub('',s)


def load_manual() -> dict[int,str]:
    m={}
    for line in (BASE/'mq075_translations.txt').read_text(encoding='utf-8').splitlines():
        if not line.strip(): continue
        i,vi=line.split('|',1)
        i=int(i)
        if i in m:raise ValueError(f'Duplicate manual index {i}')
        m[i]=vi
    assert sorted(m)==list(range(1,92)), 'Expected exactly 91 unique English patterns'
    return m


def verify_vi(en: str, vi: str, id: str):
    if not vi or vi=='REUSE': raise ValueError('Empty target: '+id)
    if unicodedata.normalize('NFC',vi)!=vi: raise ValueError('Not NFC: '+id)
    if TOKEN.findall(en)!=TOKEN.findall(vi):
        raise ValueError(f'Token mismatch {id}: {TOKEN.findall(en)!r} / {TOKEN.findall(vi)!r}')
    if vi.count('▼')>3: raise ValueError('Too many ▼: '+id)
    for seg in vi.split('▼'):
        if len(TOKEN.sub('',seg))>34: raise ValueError(f'Long segment {id}: {seg!r}')


def build(previous: pathlib.Path, output: pathlib.Path):
    mapping=load_manual()
    with zipfile.ZipFile(previous) as orig:
        if orig.testzip() is not None: raise ValueError('Previous archive CRC failed')
        files={name.replace(OLD,NEW,1):orig.read(name) for name in orig.namelist() if name.startswith(OLD)}
        ref=collections.defaultdict(list)
        for name,raw in files.items():
            if '/translation/' in name and name.endswith('.jsonl'):
                for line in raw.decode('utf-8').splitlines():
                    r=json.loads(line)
                    if r['vi'] is not None:
                        ref[body(r['en'])].append((body(r['vi']),r['id']))
        source_by_s={}
        for s in BATCH:
            path=NEW+f'translation/04-thoai/talkfigs__0eng__data__{s}.jsonl'
            source_by_s[s]=[json.loads(x) for x in files[path].decode().splitlines()]
            assert len(source_by_s[s])==120
            assert all(r['vi'] is None for r in source_by_s[s])
        rows=[r for s in BATCH for r in source_by_s[s]]
        unique=list(dict.fromkeys(body(r['en']) for r in rows))
        assert len(rows)==240 and len(unique)==91
        i_by_body={key:i for i,key in enumerate(unique,1)}
        translations={}
        reused=[]
        for i,key in enumerate(unique,1):
            text=mapping[i]
            if text=='REUSE':
                candidates=[(vi,rid) for vi,rid in ref.get(key,[]) if TOKEN.findall(vi)==TOKEN.findall(key)]
                if not candidates:raise ValueError(f'REUSE {i} not available')
                text=candidates[0][0]
                reused.append(i)
            verify_vi(key,text,f'unique #{i}')
            translations[key]=text
        assert len(reused)==10
        delta=[]
        for s in BATCH:
            sheet=io.StringIO()
            w=csv.writer(sheet,delimiter='\t',lineterminator='\n')
            w.writerow(['id','en','vi','ctx'])
            for r in source_by_s[s]:
                en=r['en']
                prefix=en[:len(en)-len(body(en))]
                vi=prefix+translations[body(en)]
                verify_vi(en,vi,r['id'])
                r['vi']=vi
                w.writerow([r['id'],r['en'],r['vi'],r['ctx']])
                delta.append(dict(r))
            name=NEW+f'translation/04-thoai/talkfigs__0eng__data__{s}.jsonl'
            files[name]=(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in source_by_s[s])).encode('utf-8')
            files[NEW+f'manual_{s.replace(".","_")}.tsv']=sheet.getvalue().encode('utf-8')
            files[NEW+f'vi_{s.replace(".","_")}.txt']=(''.join(f'{r["id"]}\t{r["vi"]}\n' for r in source_by_s[s])).encode('utf-8')
        files[NEW+'DELTA-075.jsonl']=(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in delta)).encode('utf-8')
        files[NEW+'mq075_translations.txt']=(BASE/'mq075_translations.txt').read_bytes()
        files[NEW+'build_075.py']=pathlib.Path(__file__).read_bytes()
        qp=f'''# QA — Checkpoint 075 (09/11/2026)

- **PASS**: 501 tệp JSONL / 55.976 bản ghi, đối chiếu checkpoint 074.
- **19.698 → 19.938 / 55.976 ({19938/55976*100:.2f}%)**, tăng 240 trang thoại NPC.
- `0042.003`: 120/120; `0042.004`: 120/120.
- 240 trang có **91 mẫu tiếng Anh riêng**, **81 mẫu biên tập mới**, **10 mẫu tái sử dụng** bản dịch đã có.
- Ngoài hai tệp đích, **499 JSONL giữ byte-identical** (sau khi đổi tên thư mục gốc ZIP).
- Toàn bộ **19.698 bản dịch cũ giữ nguyên**; chỉ 240 trường `vi` từ null sang bản Việt.
- Bảo toàn mọi `id`, `en`, `ctx`, các mã NDS `$...;` theo đúng thứ tự, NFC, tối đa 3 dấu `▼` và 34 ký tự tĩnh/đoạn.
- CRC ZIP hoàn chỉnh; thư mục riêng `MagiciansQuest_075/`.
- **Chưa thử trên ROM NDS; chưa xác minh độ rộng chữ/biến động thực tế trên màn hình.**
- Đợt sau: `0042.005` và `0042.006` (120 trang/tệp, nguồn đã có trong ZIP này).
'''
        files[NEW+'QA-075.md']=qp.encode('utf-8')
        cp=f'''# Magician's Quest — Checkpoint 075

**Ngày:** 09/11/2026
**Repo:** `https://github.com/ronvotri/VH-NDS` — thư mục `Magicians-Quest-Mysterious-Times/`.

Đã dịch `0042.003` và `0042.004` (240/240 trang), nâng dự án lên **19.938/55.976 ({19938/55976*100:.2f}%)**; thoại NPC **16.813/52.608**.
Giọng xưng hô bạn bè **tớ–cậu**, giữ chất hơi tự phụ của NPC, lời thoại tự nhiên, không lạm dụng meme. Tên riêng và tiền **Ritch** giữ theo nguồn.

**Bàn giao:** `manual_0042_003.tsv`, `manual_0042_004.tsv`, `DELTA-075.jsonl`, `mq075_translations.txt`, `build_075.py`, `qa_075.py` và `QA-075.md`.

**Nguồn đợt 076:** `translation/04-thoai/talkfigs__0eng__data__0042.005.jsonl` và `...0042.006.jsonl`, mỗi tệp 120 bản ghi chưa dịch. Không lẫn game khác, chỉ cập nhật dự án Magician's Quest.

**Lưu ý QA:** Hoàn tất kiểm tra tĩnh; chưa xác minh thực tế trên ROM NDS.
'''
        files[NEW+'CHECKPOINT-2026-11-09-DOT-75.md']=cp.encode('utf-8')
        intro='**Checkpoint mới nhất: 075 (09/11/2026) — 19.938 / 55.976 (35,62%).** +240 trang thoại NPC (`0042.003`, `0042.004`). Xem `CHECKPOINT-2026-11-09-DOT-75.md` và `QA-075.md`. Đợt tiếp: `0042.005` + `0042.006` (240 trang nguồn đã có).\n\n'
        files[NEW+'README.md']=(intro+files[NEW+'README.md'].decode('utf-8')).encode('utf-8')
        intro2='''## Checkpoint 075 — 09/11/2026

- Đã dịch `0042.003` và `0042.004`: +240 trang; **19.938 / 55.976 (35,62%)**; hội thoại NPC **16.813 / 52.608**.
- 81 mẫu mới, 10 mẫu tái sử dụng; QA 501 JSONL / 55.976 bản ghi, 499 tệp giữ byte-identical, không thay 19.698 bản dịch trước.
- ZIP đầy đủ `MagiciansQuest-VietHoa-Checkpoint-075.zip` lưu tại Thư viện `/Dịch giả lập`; chưa thử hiển thị trên ROM.
- Tiếp `0042.005` và `0042.006` (120 trang/tệp) đã có nguồn.

'''
        files[NEW+'BAN_GIAO.md']=(intro2+files[NEW+'BAN_GIAO.md'].decode('utf-8')).encode('utf-8')
        files[NEW+'qa_075.py']=(BASE/'qa_075.py').read_bytes()
        nj=total=before=after=changed=0
        for oldname in orig.namelist():
            if not ('/translation/' in oldname and oldname.endswith('.jsonl')):continue
            nj+=1
            newname=oldname.replace(OLD,NEW,1)
            raw_before=orig.read(oldname)
            raw_after=files[newname]
            is_batch=any(newname.endswith(f'{s}.jsonl') for s in BATCH)
            if not is_batch: assert raw_before==raw_after,oldname
            else:changed+=1
            a=[json.loads(t) for t in raw_before.decode().splitlines()]
            b=[json.loads(t) for t in raw_after.decode().splitlines()]
            assert len(a)==len(b),(oldname,len(a),len(b))
            for x,y in zip(a,b):
                total+=1
                assert x.keys()==y.keys()
                assert all(x[k]==y[k] for k in x if k!='vi'),x['id']
                before+=x['vi'] is not None
                after+=y['vi'] is not None
                if x['vi'] is not None: assert x['vi']==y['vi']
                elif not is_batch:assert y['vi'] is None
                else:assert y['vi'] and TOKEN.findall(x['en'])==TOKEN.findall(y['vi'])
        assert (nj,total,before,after,changed)==(501,TOTAL,BASE_COUNT,BASE_COUNT+240,2),(nj,total,before,after,changed)
        output.parent.mkdir(parents=True,exist_ok=True)
        with zipfile.ZipFile(output,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=7,allowZip64=True) as out:
            for name in sorted(files):out.writestr(name,files[name])
    with zipfile.ZipFile(output) as z:
        assert z.testzip() is None
        print('PASS',len(z.namelist()),'files',output.stat().st_size,'bytes',hashlib.sha256(output.read_bytes()).hexdigest())
    print('COMPLETED: 19,938 / 55,976; batch 240; 81 new patterns + 10 reused; 501 JSONL QA PASS')

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--previous',type=pathlib.Path,default=BASE/'MagiciansQuest-VietHoa-Checkpoint-074.zip')
    parser.add_argument('--output',type=pathlib.Path,default=BASE/'MagiciansQuest-VietHoa-Checkpoint-075.zip')
    args=parser.parse_args();build(args.previous,args.output)
