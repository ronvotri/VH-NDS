#!/usr/bin/env python3
"""Magician's Quest additive checkpoint 076 based on 075.

python build_076.py --previous MagiciansQuest-VietHoa-Checkpoint-075.zip --output MagiciansQuest-VietHoa-Checkpoint-076.zip
"""
from __future__ import annotations
import argparse, collections, csv, hashlib, io, json, pathlib, re, unicodedata, zipfile
BASE=pathlib.Path(__file__).resolve().parent
OLD='MagiciansQuest_075/'
NEW='MagiciansQuest_076/'
TARGET=('0042.005','0042.006')
NEXT=('0042.007','0042.008')
TOTAL=55976
BASE_COUNT=19938
TOKEN=re.compile(r"\$\d{3}(?:'[-\d]+)*;")
PREFIX=re.compile(r"^(?:\$(?:024|023|022|034|040)(?:'[-\d]+)*;)+")
BODY=lambda s:PREFIX.sub('',s)


def manual_translations():
    out={}
    for line in (BASE/'mq076_new_translations.txt').read_text('utf-8').splitlines():
        if not line.strip():continue
        k,s=line.split('|',1);i=int(k)
        if i in out: raise ValueError('Duplicate index '+k)
        out[i]=s
    assert len(out)==49,(len(out),out.keys())
    return out


def verify(en,vi,label):
    if not vi or vi=='REUSE':raise ValueError('Empty VI '+label)
    if vi!=unicodedata.normalize('NFC',vi):raise ValueError('Not NFC '+label)
    if TOKEN.findall(en)!=TOKEN.findall(vi):raise ValueError(f'Token mismatch {label}: EN {TOKEN.findall(en)} VI {TOKEN.findall(vi)}')
    if vi.count('▼')>3:raise ValueError('Too many breaks '+label)
    for seg in vi.split('▼'):
        static=TOKEN.sub('',seg)
        if len(static)>34:raise ValueError(f'Long segment {label} length {len(static)}: {static!r}')


def run(previous,output):
    additions=manual_translations()
    with zipfile.ZipFile(previous) as old:
        assert old.testzip() is None
        files={n.replace(OLD,NEW,1):old.read(n) for n in old.namelist() if n.startswith(OLD)}
        reference=collections.defaultdict(list)
        for n,raw in files.items():
            if '/translation/' not in n or not n.endswith('.jsonl'):continue
            for line in raw.decode('utf-8').splitlines():
                r=json.loads(line)
                if r['vi'] is not None:reference[BODY(r['en'])].append((BODY(r['vi']),r['id']))
        sources={}
        for s in TARGET:
            n=NEW+f'translation/04-thoai/talkfigs__0eng__data__{s}.jsonl'
            sources[s]=[json.loads(l) for l in files[n].decode('utf-8').splitlines()]
            assert len(sources[s])==120 and all(r['vi'] is None for r in sources[s])
        rows=[r for s in TARGET for r in sources[s]]
        unique=list(dict.fromkeys(BODY(r['en']) for r in rows))
        assert len(rows)==240 and len(unique)==74,(len(rows),len(unique))
        assert sorted(additions)==sorted(set(range(1,75))-set(i for i,key in enumerate(unique,1) if reference.get(key))), 'Manual index list does not match unmatched sentences'
        translated={};reused=[]
        for i,key in enumerate(unique,1):
            if i in additions:vi=additions[i]
            else:
                can=[v for v,rid in reference[key] if TOKEN.findall(key)==TOKEN.findall(v)]
                if not can:raise ValueError(f'No safe previous translation for {i}')
                vi=collections.Counter(can).most_common(1)[0][0]
                reused.append(i)
            verify(key,vi,f'pattern {i:03d}')
            translated[key]=vi
        assert len(reused)==25,(len(reused),reused)
        delta=[]
        for s in TARGET:
            sheet=io.StringIO();csvout=csv.writer(sheet,delimiter='\t',lineterminator='\n')
            csvout.writerow(('id','en','vi','ctx'))
            for r in sources[s]:
                en=r['en'];prefix=en[:len(en)-len(BODY(en))]
                vi=prefix+translated[BODY(en)]
                verify(en,vi,r['id'])
                r['vi']=vi
                csvout.writerow((r['id'],r['en'],r['vi'],r['ctx']))
                delta.append(r.copy())
            f=NEW+f'translation/04-thoai/talkfigs__0eng__data__{s}.jsonl'
            files[f]=''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in sources[s]).encode('utf-8')
            files[NEW+f'manual_{s.replace(".","_")}.tsv']=sheet.getvalue().encode('utf-8')
            files[NEW+f'vi_{s.replace(".","_")}.txt']=''.join(f'{r["id"]}\t{r["vi"]}\n' for r in sources[s]).encode('utf-8')
        files[NEW+'DELTA-076.jsonl']=''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in delta).encode('utf-8')
        files[NEW+'mq076_new_translations.txt']=(BASE/'mq076_new_translations.txt').read_bytes()
        files[NEW+'build_076.py']=pathlib.Path(__file__).read_bytes()
        progress=BASE_COUNT+len(delta)
        qa=f'''# QA — Checkpoint 076 (09/11/2026)

- **PASS:** 501 tệp JSONL / 55.976 bản ghi, đối chiếu byte và trường dữ liệu với checkpoint 075.
- **{BASE_COUNT:,} → {progress:,} / 55.976 ({progress/TOTAL*100:.2f}%)**, tăng đúng 240 trang thoại NPC.
- `0042.005`: 120/120; `0042.006`: 120/120.
- **74 mẫu tiếng Anh riêng** (loại trừ tiền tố mã màu): **49 mẫu dịch mới, 25 mẫu tái sử dụng** theo dữ liệu đã dịch.
- Chỉ đúng 2 JSONL thay đổi trường `vi`; **499 JSONL khác byte-identical** sau khi chuẩn hóa đường dẫn gốc ZIP.
- Toàn bộ 19.938 trường dịch trước được giữ nguyên; bảo toàn `id`, `en`, `ctx` và tất cả trường phi-`vi`.
- Toàn bộ token `$...;` đúng thứ tự, chuẩn Unicode NFC; tối đa 3 dấu `▼` và 34 ký tự tĩnh/đoạn.
- Không sửa, không gộp các ID hoặc các bản ghi trùng nhau.
- File ZIP CRC toàn vẹn và không chứa dự án khác.
- Chưa kiểm thử trực tiếp trên ROM NDS; giới hạn trên chỉ là độ dài văn bản tĩnh, không phải độ rộng glyph/biến động.
- Đợt 077 tiếp theo: `0042.007` + `0042.008`, 120 trang/tệp.
'''
        files[NEW+'QA-076.md']=qa.encode('utf-8')
        checkpoint=f'''# Magician's Quest — Checkpoint 076

**Ngày:** 09/11/2026
**Repository:** `ronvotri/VH-NDS`, thư mục `Magicians-Quest-Mysterious-Times/`.

**Hoàn thành:** `0042.005` và `0042.006`, mỗi tệp 120 trang, nâng tổng tiến độ lên **{progress:,}/55.976 ({progress/TOTAL*100:.2f}%)**, thoại NPC **17.053/52.608**.

**Nội dung:** lựa chọn giao tiếp, lời mời chơi/đến trường, lời đồn, các lời thoại NPC có tính cách châm biếm và tự phụ; 49 mẫu biên tập mới + 25 mẫu giữ lại từ các checkpoint trước. Xưng hô bạn bè tớ–cậu, tránh lạm dụng meme.

**Kèm theo:** `manual_0042_005.tsv`, `manual_0042_006.tsv`, `DELTA-076.jsonl`, `mq076_new_translations.txt`, `build_076.py`, `QA-076.md`.

**Đợt 077:** `0042.007` và `0042.008`, nguồn tiếng Anh đã nằm trong ZIP và chưa có trường dịch.

**Lưu ý:** QA trên JSONL/ZIP PASS; chưa kiểm thử hiển thị trong ROM NDS.
'''
        files[NEW+'CHECKPOINT-2026-11-09-DOT-76.md']=checkpoint.encode('utf-8')
        top=f'**Checkpoint mới nhất: 076 (09/11/2026) — {progress:,}/55.976 ({progress/TOTAL*100:.2f}%).** +240 trang thoại (`0042.005`, `0042.006`). Xem `CHECKPOINT-2026-11-09-DOT-76.md`, `QA-076.md`. Đợt tiếp: `0042.007` + `0042.008`.\n\n'
        files[NEW+'README.md']=(top+files[NEW+'README.md'].decode('utf-8')).encode('utf-8')
        intro=f'''## Checkpoint 076 — 09/11/2026

- +240 trang thoại từ `0042.005`, `0042.006`; tổng **{progress:,}/55.976 ({progress/TOTAL*100:.2f}%)**, thoại NPC **17.053/52.608**.
- 49 mẫu mới, 25 mẫu tái sử dụng; QA 501 JSONL / 55.976 bản ghi PASS. 499 JSONL khác giữ byte-identical.
- ZIP `MagiciansQuest-VietHoa-Checkpoint-076.zip` đầy đủ; chưa thử trên ROM NDS.
- Tiếp `0042.007` và `0042.008` (240 trang chưa dịch, nguồn có sẵn).

'''
        files[NEW+'BAN_GIAO.md']=(intro+files[NEW+'BAN_GIAO.md'].decode('utf-8')).encode('utf-8')
        # Full corpus audit against the previous checkpoint.
        count_files=total=old_done=new_done=changed_files=0
        for name in old.namelist():
            if '/translation/' not in name or not name.endswith('.jsonl'):continue
            count_files+=1
            destination=name.replace(OLD,NEW,1)
            a_bytes=old.read(name);b_bytes=files[destination]
            target=any(destination.endswith(s+'.jsonl') for s in TARGET)
            if not target:assert a_bytes==b_bytes,name
            else:changed_files+=1
            a=[json.loads(x) for x in a_bytes.decode('utf-8').splitlines()]
            b=[json.loads(x) for x in b_bytes.decode('utf-8').splitlines()]
            assert len(a)==len(b),(name,len(a),len(b))
            for oldr,newr in zip(a,b):
                total+=1
                assert oldr.keys()==newr.keys(),oldr['id']
                assert all(oldr[k]==newr[k] for k in oldr if k!='vi'),oldr['id']
                old_done+=oldr['vi'] is not None
                new_done+=newr['vi'] is not None
                if oldr['vi'] is not None:assert oldr['vi']==newr['vi'],oldr['id']
                elif target:assert newr['vi'] and TOKEN.findall(oldr['en'])==TOKEN.findall(newr['vi'])
                else:assert newr['vi'] is None
        assert (count_files,total,old_done,new_done,changed_files)==(501,TOTAL,BASE_COUNT,BASE_COUNT+240,2),(count_files,total,old_done,new_done,changed_files)
        output.parent.mkdir(parents=True,exist_ok=True)
        with zipfile.ZipFile(output,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=7,allowZip64=True) as out:
            for name,raw in sorted(files.items()):out.writestr(name,raw)
    with zipfile.ZipFile(output) as out:
        assert out.testzip() is None
        assert len(out.namelist())==len(set(out.namelist()))
        print('PASS: Archive CRC, 501 JSONL, 55,976 rows, 499 unchanged files, +240 VI. Files:',len(out.namelist()))
    print('TOTAL',progress,'/',TOTAL, 'PERCENT',f'{progress/TOTAL*100:.2f}', 'SIZE',output.stat().st_size,'SHA256',hashlib.sha256(output.read_bytes()).hexdigest())

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--previous',type=pathlib.Path,default=BASE/'MagiciansQuest-VietHoa-Checkpoint-075.zip')
    ap.add_argument('--output',type=pathlib.Path,default=BASE/'MagiciansQuest-VietHoa-Checkpoint-076.zip')
    args=ap.parse_args()
    run(args.previous,args.output)
