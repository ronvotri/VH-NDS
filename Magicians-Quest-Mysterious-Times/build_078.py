#!/usr/bin/env python3
"""Build additive Magician's Quest checkpoint 078 from complete checkpoint 077.
Run: python build_078.py --previous /mnt/data/MagiciansQuest-VietHoa-Checkpoint-077.zip \
                        --output /mnt/data/MagiciansQuest-VietHoa-Checkpoint-078.zip
"""
from __future__ import annotations
import argparse,collections,csv,hashlib,io,json,pathlib,re,unicodedata,zipfile

BASE=pathlib.Path(__file__).resolve().parent
OLD='MagiciansQuest_077/'
NEW='MagiciansQuest_078/'
TARGET=('0042.009','0042.010')
NEXT=('0042.011','0042.012')
TOTAL=55976
BASE_COUNT=20418
NPC_BASE=17293
TOKEN=re.compile(r"\$\d{3}(?:'[-\d]+)*;")
PREFIX=re.compile(r"^(?:\$(?:024|023|022|034|040|004)(?:'[-\d]+)*;)+")
def body(s):return PREFIX.sub('',s)

def verify(en,vi,label):
    if not isinstance(vi,str) or not vi:raise ValueError('Missing Vietnamese '+label)
    if vi!=unicodedata.normalize('NFC',vi):raise ValueError('Non-NFC '+label)
    if TOKEN.findall(en)!=TOKEN.findall(vi):raise ValueError(f'Token mismatch {label}: {TOKEN.findall(en)} != {TOKEN.findall(vi)}')
    if vi.count('▼')>3:raise ValueError('Too many line breaks '+label)
    if any(len(TOKEN.sub('',s))>34 for s in vi.split('▼')):raise ValueError('Static segment too long '+label)
    if '\r' in vi or '\n' in vi or '\t' in vi:raise ValueError('Control char '+label)

def build(previous,output):
    additions={}
    for line in (BASE/'mq078_new_translations.txt').read_text('utf-8').splitlines():
        if not line:continue
        num,vi=line.split('|',1);num=int(num)
        if num in additions:raise ValueError('Duplicate manual key '+str(num))
        additions[num]=vi
    assert len(additions)==20
    with zipfile.ZipFile(previous) as prev:
        assert prev.testzip() is None
        names=prev.namelist()
        assert len(names)==len(set(names)) and all(n.startswith(OLD) for n in names)
        files={n.replace(OLD,NEW,1):prev.read(n) for n in names}
        refs=collections.defaultdict(collections.Counter)
        for name,payload in files.items():
            if '/translation/' not in name or not name.endswith('.jsonl'):continue
            for line in payload.decode('utf-8').splitlines():
                row=json.loads(line)
                if isinstance(row['vi'],str):
                    en=body(row['en']);vi=body(row['vi'])
                    if TOKEN.findall(en)==TOKEN.findall(vi):refs[en][vi]+=1
        sources={}
        for s in TARGET:
            path=NEW+f'translation/04-thoai/talkfigs__0eng__data__{s}.jsonl'
            rows=[json.loads(l) for l in files[path].decode('utf-8').splitlines()]
            assert len(rows)==120 and all(r['vi'] is None for r in rows),s
            sources[s]=rows
        unique=list(dict.fromkeys(body(r['en']) for s in TARGET for r in sources[s]))
        assert len(unique)==50,len(unique)
        reuse={i:refs[en] for i,en in enumerate(unique,1)}
        assert sum(bool(x) for x in reuse.values())==30
        assert sorted(additions)==[i for i in range(1,len(unique)+1) if not reuse[i]]
        translations={}
        for i,en in enumerate(unique,1):
            vi=additions[i] if i in additions else reuse[i].most_common(1)[0][0]
            verify(en,vi,f'pattern {i}')
            translations[en]=vi
        delta=[]
        for s in TARGET:
            buf=io.StringIO();w=csv.writer(buf,delimiter='\t',lineterminator='\n')
            w.writerow(('id','en','vi','ctx'))
            for row in sources[s]:
                en=row['en'];prefix=en[:len(en)-len(body(en))]
                vi=prefix+translations[body(en)]
                verify(en,vi,row['id'])
                row['vi']=vi
                w.writerow((row['id'],en,vi,row['ctx']))
                delta.append(row.copy())
            files[NEW+f'translation/04-thoai/talkfigs__0eng__data__{s}.jsonl']=''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in sources[s]).encode('utf-8')
            files[NEW+f'manual_{s.replace(".","_")}.tsv']=buf.getvalue().encode('utf-8')
            files[NEW+f'vi_{s.replace(".","_")}.txt']=''.join(r['id']+'\t'+r['vi']+'\n' for r in sources[s]).encode('utf-8')
        files[NEW+'DELTA-078.jsonl']=''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in delta).encode('utf-8')
        files[NEW+'mq078_new_translations.txt']=(BASE/'mq078_new_translations.txt').read_bytes()
        files[NEW+'build_078.py']=pathlib.Path(__file__).read_bytes()
        progress=BASE_COUNT+240;npc=NPC_BASE+240;pct=f'{progress/TOTAL*100:.2f}'
        qa=f'''# QA — Magician's Quest Checkpoint 078 (09/11/2026)

- **PASS:** 501 tệp JSONL / 55.976 bản ghi so với checkpoint 077.
- **{BASE_COUNT:,} → {progress:,} / {TOTAL:,} ({pct}%)**: thêm 240 mục NPC, `0042.009` 120/120 và `0042.010` 120/120.
- 50 mẫu câu gốc riêng: **20 mẫu biên tập mới**, **30 mẫu tái sử dụng** từ các checkpoint trước theo nội dung EN chuẩn hóa tiền tố.
- Chỉ hai JSONL đích thay đổi; 499 JSONL khác giữ nguyên từng byte.
- Không chỉnh sửa {BASE_COUNT:,} bản dịch cũ; mọi trường `id`, `en`, `ctx` và metadata giữ nguyên.
- Đúng thứ tự và nội dung mọi token NDS `$...;`; Unicode NFC; tối đa 3 dấu `▼` và 34 ký tự tĩnh mỗi đoạn.
- Không gộp bản ghi, không trộn project khác. ZIP CRC PASS; không tên trùng.
- **Chưa kiểm thử ROM:** kiểm tra độ dài tĩnh không thay thế phép đo độ rộng glyph thực hoặc độ dài biến động.
- **Nguồn đợt 079**: `0042.011` và `0042.012` (120+120 trang, `vi:null`).
'''
        files[NEW+'QA-078.md']=qa.encode('utf-8')
        note=f'''# Magician's Quest — Checkpoint 078

**Ngày:** 09/11/2026  
**Repository:** `ronvotri/VH-NDS` / `Magicians-Quest-Mysterious-Times/`.

- **Thêm 240 trang NPC** trong `0042.009` và `0042.010` (120 mỗi tệp).
- **Tổng {progress:,}/{TOTAL:,} ({pct}%)**, thoại NPC **{npc:,}/52.608**.
- 50 mẫu câu riêng: 20 mẫu mới, 30 mẫu dùng lại chính xác EN.
- Nội dung: tin đồn học đường, yêu đương, chuyện hội hè, tương tác NPC có tính cách thích thu phí và lời khuyên bạn bè.
- Xưng hô tự nhiên; bảo toàn mọi biến động `$500;`, `$530;`, `$533;`, lựa chọn `$018` và tiền tố hiển thị.
- Gồm `DELTA-078.jsonl`, TSV EN–VI, `mq078_new_translations.txt`, `QA-078.md`, `build_078.py`.
- QA toàn bộ PASS; chưa thử trong ROM NDS.
- **Tiếp đợt 079:** `0042.011` + `0042.012` đã có nguồn `vi:null` trong ZIP.
'''
        files[NEW+'CHECKPOINT-2026-11-09-DOT-78.md']=note.encode('utf-8')
        top=f'**Checkpoint mới nhất: 078 (09/11/2026) — {progress:,}/{TOTAL:,} ({pct}%).** +240 NPC (`0042.009` và `0042.010`). Xem `CHECKPOINT-2026-11-09-DOT-78.md`, `QA-078.md`. Tiếp: `0042.011`, `0042.012`.\n\n'
        files[NEW+'README.md']=(top+files[NEW+'README.md'].decode('utf-8')).encode('utf-8')
        hand=f'''## Checkpoint 078 — 09/11/2026

- Hoàn thành `0042.009`, `0042.010`: +240 trang; tổng {progress:,}/{TOTAL:,} ({pct}%), NPC {npc:,}/52.608.
- 20 mẫu dịch mới + 30 mẫu tái dùng. Toàn bộ 501 JSONL / 55.976 bản ghi PASS; 499 JSONL không đổi byte.
- ZIP đầy đủ, TSV EN–VI, delta, QA, script tái dựng. Chưa thử ROM thực.
- Tiếp đợt 079: `0042.011` và `0042.012` (240 trang nguồn).

'''
        files[NEW+'BAN_GIAO.md']=(hand+files[NEW+'BAN_GIAO.md'].decode('utf-8')).encode('utf-8')
        count_files=total=old_done=new_done=changed=0
        for path in names:
            if '/translation/' not in path or not path.endswith('.jsonl'):continue
            count_files+=1;new_name=path.replace(OLD,NEW,1)
            original=prev.read(path);written=files[new_name]
            target=any(new_name.endswith(s+'.jsonl') for s in TARGET)
            if not target:assert original==written,path
            else:changed+=1
            before=[json.loads(s) for s in original.decode('utf-8').splitlines()]
            after=[json.loads(s) for s in written.decode('utf-8').splitlines()]
            assert len(before)==len(after),path
            for a,b in zip(before,after):
                total+=1
                assert a.keys()==b.keys() and all(a[k]==b[k] for k in a if k!='vi'),a['id']
                old_done+=a['vi'] is not None;new_done+=b['vi'] is not None
                if a['vi'] is not None:assert a['vi']==b['vi'],a['id']
                elif target:verify(a['en'],b['vi'],a['id'])
                else:assert b['vi'] is None,a['id']
        assert (count_files,total,old_done,new_done,changed)==(501,TOTAL,BASE_COUNT,progress,2),(count_files,total,old_done,new_done,changed)
        for s in NEXT:
            name=NEW+f'translation/04-thoai/talkfigs__0eng__data__{s}.jsonl'
            nextrows=[json.loads(l) for l in files[name].decode('utf-8').splitlines()]
            assert len(nextrows)==120 and all(r['vi'] is None for r in nextrows),s
        output.parent.mkdir(parents=True,exist_ok=True)
        with zipfile.ZipFile(output,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=7,allowZip64=True) as out:
            for n,raw in sorted(files.items()):out.writestr(n,raw)
    with zipfile.ZipFile(output) as out:
        assert out.testzip() is None
        assert len(out.namelist())==len(set(out.namelist()))
        print(f'PASS ZIP CRC, {count_files} JSONL, {total} rows, 499 files byte-identical, +240 pages; zip entries {len(out.namelist())}')
    print('TOTAL',progress,'/',TOTAL,'PERCENT',pct,'NPC',npc,'SIZE',output.stat().st_size,'SHA256',hashlib.sha256(output.read_bytes()).hexdigest())

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--previous',type=pathlib.Path,default=BASE/'MagiciansQuest-VietHoa-Checkpoint-077.zip')
    p.add_argument('--output',type=pathlib.Path,default=BASE/'MagiciansQuest-VietHoa-Checkpoint-078.zip')
    args=p.parse_args();build(args.previous,args.output)
