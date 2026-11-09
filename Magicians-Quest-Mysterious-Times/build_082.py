#!/usr/bin/env python3
"""Reproducibly build Magician's Quest checkpoint 082 from full checkpoint 081.

Usage: python build_082.py --previous /mnt/data/MagiciansQuest-VietHoa-Checkpoint-081.zip \
    --output /mnt/data/MagiciansQuest-VietHoa-Checkpoint-082.zip
"""
from __future__ import annotations
import argparse,collections,csv,hashlib,io,json,pathlib,re,unicodedata,zipfile

BASE=pathlib.Path(__file__).resolve().parent
OLD='MagiciansQuest_081/'
NEW='MagiciansQuest_082/'
TARGET=('0042.017','0042.018')
NEXT=('0042.019','0042.020')
TOTAL=55976
BASE_COUNT=21378
NPC_BASE=18253
TOKEN=re.compile(r"\$\d{3}(?:'[-\d]+)*;")
PREFIX=re.compile(r"^(?:\$(?:024|023|022|034|040|004)(?:'[-\d]+)*;)+")
def body(s):return PREFIX.sub('',s)

def verify(en,vi,label):
    if not isinstance(vi,str) or not vi:raise ValueError('Missing Vietnamese: '+label)
    if vi!=unicodedata.normalize('NFC',vi):raise ValueError('Non-NFC: '+label)
    if TOKEN.findall(en)!=TOKEN.findall(vi):raise ValueError(f'Token mismatch {label}: {TOKEN.findall(en)} != {TOKEN.findall(vi)}')
    if vi.count('▼')>3:raise ValueError('Too many page segments: '+label)
    if any(len(TOKEN.sub('',part))>34 for part in vi.split('▼')):raise ValueError('Static segment too long: '+label)
    if any(x in vi for x in ('\r','\n','\t')):raise ValueError('Control character: '+label)

def build(previous,output):
    manual={}
    for line in (BASE/'mq082_new_translations.txt').read_text('utf-8').splitlines():
        if not line:continue
        num,vi=line.split('|',1);num=int(num)
        if num in manual:raise ValueError('Duplicate key '+str(num))
        manual[num]=vi
    assert len(manual)==113,len(manual)
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
        unique=list(dict.fromkeys(body(row['en']) for s in TARGET for row in sources[s]))
        assert len(unique)==157,len(unique)
        reuse={i:refs[en] for i,en in enumerate(unique,1)}
        assert sum(bool(x) for x in reuse.values())==44
        assert sorted(manual)==[i for i in range(1,len(unique)+1) if not reuse[i]]
        translations={}
        for i,en in enumerate(unique,1):
            vi=manual[i] if i in manual else reuse[i].most_common(1)[0][0]
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
        files[NEW+'DELTA-082.jsonl']=''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in delta).encode('utf-8')
        files[NEW+'mq082_new_translations.txt']=(BASE/'mq082_new_translations.txt').read_bytes()
        files[NEW+'build_082.py']=pathlib.Path(__file__).read_bytes()
        progress=BASE_COUNT+240;npc=NPC_BASE+240;pct=f'{progress/TOTAL*100:.2f}'
        qa=f'''# QA — Magician's Quest Checkpoint 082 (09/11/2026)

- **PASS:** 501 tệp JSONL / 55.976 bản ghi so với checkpoint 081.
- **{BASE_COUNT:,} → {progress:,} / {TOTAL:,} ({pct}%)**: thêm 240 trang thoại NPC, `0042.017` 120/120 và `0042.018` 120/120.
- 157 mẫu EN riêng: **113 mẫu dịch mới**, **44 mẫu tái sử dụng** theo nguyên văn EN đã chuẩn hóa tiền tố.
- Chỉ hai JSONL đích thay đổi; 499 JSONL khác giữ nguyên từng byte.
- Không sửa {BASE_COUNT:,} bản dịch trước; các trường `id`, `en`, `ctx` và metadata không thay đổi.
- Giữ đúng thứ tự mọi token NDS `$...;`; Unicode NFC; tối đa 3 dấu `▼`; không quá 34 ký tự tĩnh mỗi đoạn.
- Không gộp mục, không trộn dự án khác; ZIP CRC PASS và không trùng tên.
- **Chưa kiểm thử ROM:** kiểm tra dòng tĩnh không tương đương đo kích thước glyph/biến động thực tế.
- **Nguồn đợt 083:** `0042.019`, `0042.020` (120 + 120 trang, `vi:null`).
'''
        files[NEW+'QA-082.md']=qa.encode('utf-8')
        note=f'''# Magician's Quest — Checkpoint 082

**Ngày:** 09/11/2026  
**Repo:** `ronvotri/VH-NDS` / `Magicians-Quest-Mysterious-Times/`.

- **+240 trang thoại NPC** tại `0042.017` và `0042.018` (120 mỗi tệp).
- Tổng **{progress:,}/{TOTAL:,} ({pct}%)**, riêng NPC **{npc:,}/52.608**.
- 157 mẫu EN riêng: 113 mẫu mới, 44 mẫu dùng lại; bí ẩn Nessie, Ông Kẹo, Nhân Sư, kỳ lân, rồng, tin đồn và chuyện rừng/hồ.
- Bảo toàn các token biến tên và vật phẩm `$500`, `$530`, `$531`, `$533`, `$507`, mã màu, mã lựa chọn.
- Bàn giao: `DELTA-082.jsonl`, `manual_0042_017.tsv`, `manual_0042_018.tsv`, `mq082_new_translations.txt`, `QA-082.md`, `build_082.py`.
- QA 501 JSONL đạt; chưa kiểm thử hiển thị trên ROM.
- **Đợt tiếp 083:** `0042.019` và `0042.020` (đã có nguồn `vi:null` trong ZIP).
'''
        files[NEW+'CHECKPOINT-2026-11-09-DOT-82.md']=note.encode('utf-8')
        top=f'**Checkpoint mới nhất: 082 (09/11/2026) — {progress:,}/{TOTAL:,} ({pct}%).** +240 NPC (`0042.017`, `0042.018`); 113 mẫu biên tập mới. Xem `CHECKPOINT-2026-11-09-DOT-82.md`, `QA-082.md`. Tiếp `0042.019`, `0042.020`.\n\n'
        files[NEW+'README.md']=(top+files[NEW+'README.md'].decode('utf-8')).encode('utf-8')
        hand=f'''## Checkpoint 082 — 09/11/2026

- +240 trang thoại `0042.017`, `0042.018`; tổng {progress:,}/{TOTAL:,} ({pct}%), NPC {npc:,}/52.608.
- 113 mẫu dịch mới + 44 mẫu tái dùng. QA 501 JSONL / 55.976 bản ghi đạt; 499 JSONL không đổi byte.
- ZIP đầy đủ + TSV EN–VI, delta, script, QA, nguồn cho đợt 083. Chưa kiểm thử ROM thực.
- Tiếp `0042.019` và `0042.020` (240 trang nguồn).

'''
        files[NEW+'BAN_GIAO.md']=(hand+files[NEW+'BAN_GIAO.md'].decode('utf-8')).encode('utf-8')
        count_files=total=old_done=new_done=changed_files=0
        for path in names:
            if '/translation/' not in path or not path.endswith('.jsonl'):continue
            count_files+=1
            new_name=path.replace(OLD,NEW,1)
            original=prev.read(path);written=files[new_name]
            target=any(new_name.endswith(s+'.jsonl') for s in TARGET)
            if not target:assert original==written,path
            else:changed_files+=1
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
        assert (count_files,total,old_done,new_done,changed_files)==(501,TOTAL,BASE_COUNT,progress,2),(count_files,total,old_done,new_done,changed_files)
        for s in NEXT:
            name=NEW+f'translation/04-thoai/talkfigs__0eng__data__{s}.jsonl'
            nxt=[json.loads(l) for l in files[name].decode('utf-8').splitlines()]
            assert len(nxt)==120 and all(row['vi'] is None for row in nxt),s
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
    p.add_argument('--previous',type=pathlib.Path,default=BASE/'MagiciansQuest-VietHoa-Checkpoint-081.zip')
    p.add_argument('--output',type=pathlib.Path,default=BASE/'MagiciansQuest-VietHoa-Checkpoint-082.zip')
    args=p.parse_args();build(args.previous,args.output)
