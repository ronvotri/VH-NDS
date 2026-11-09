#!/usr/bin/env python3
"""Reproducible additive checkpoint 077: 0042.007 and 0042.008.

python build_077.py --previous MagiciansQuest-VietHoa-Checkpoint-076.zip --output MagiciansQuest-VietHoa-Checkpoint-077.zip
"""
from __future__ import annotations
import argparse, collections, csv, hashlib, io, json, pathlib, re, unicodedata, zipfile

BASE=pathlib.Path(__file__).resolve().parent
OLD='MagiciansQuest_076/'
NEW='MagiciansQuest_077/'
TARGET=('0042.007','0042.008')
NEXT=('0042.009','0042.010')
TOTAL=55976
BASE_COUNT=20178
NPC_BASE=17053
TOKEN=re.compile(r"\$\d{3}(?:'[-\d]+)*;")
PREFIX=re.compile(r"^(?:\$(?:024|023|022|034|040)(?:'[-\d]+)*;)+")
def body(s):return PREFIX.sub('',s)


def verify(en,vi,label):
    if not isinstance(vi,str) or not vi or vi=='REUSE':raise ValueError('Empty VI '+label)
    if vi!=unicodedata.normalize('NFC',vi):raise ValueError('Not NFC '+label)
    if TOKEN.findall(en)!=TOKEN.findall(vi):raise ValueError(f'Token mismatch {label}: EN {TOKEN.findall(en)} VI {TOKEN.findall(vi)}')
    if vi.count('▼')>3:raise ValueError('Too many breaks '+label)
    for seg in vi.split('▼'):
        static=TOKEN.sub('',seg)
        if len(static)>34:raise ValueError(f'Segment > 34 {label}: len {len(static)} {static!r}')


def run(previous,output):
    additions={}
    for l in (BASE/'mq077_new_translations.txt').read_text('utf-8').splitlines():
        if not l.strip():continue
        k,vi=l.split('|',1)
        k=int(k)
        if k in additions:raise ValueError('Repeated manual key '+str(k))
        additions[k]=vi
    assert len(additions)==25, (len(additions),list(additions))
    with zipfile.ZipFile(previous) as prev:
        assert prev.testzip() is None
        names=prev.namelist()
        assert all(n.startswith(OLD) for n in names),'Archive has a foreign root'
        files={n.replace(OLD,NEW,1):prev.read(n) for n in names}
        refs=collections.defaultdict(list)
        for n,raw in files.items():
            if '/translation/' not in n or not n.endswith('.jsonl'):continue
            for l in raw.decode('utf-8').splitlines():
                r=json.loads(l)
                if r['vi'] is not None:
                    refs[body(r['en'])].append((body(r['vi']),r['id']))
        sources={}
        for s in TARGET:
            key=NEW+f'translation/04-thoai/talkfigs__0eng__data__{s}.jsonl'
            sources[s]=[json.loads(l) for l in files[key].decode('utf-8').splitlines()]
            assert len(sources[s])==120 and all(r['vi'] is None for r in sources[s]),s
        rows=[r for s in TARGET for r in sources[s]]
        unique=list(dict.fromkeys(body(r['en']) for r in rows))
        assert len(rows)==240 and len(unique)==77,(len(rows),len(unique))
        reusable={i:collections.Counter(v for v,_ in refs[key] if TOKEN.findall(key)==TOKEN.findall(v))
                  for i,key in enumerate(unique,1)}
        assert len([i for i,v in reusable.items() if v])==52
        assert sorted(additions)==[i for i in range(1,78) if not reusable[i]],'Manual indices mismatch'
        translations={}
        for i,key in enumerate(unique,1):
            vi=additions[i] if i in additions else reusable[i].most_common(1)[0][0]
            verify(key,vi,f'pattern {i:03d}')
            translations[key]=vi
        delta=[]
        for s in TARGET:
            buf=io.StringIO();csvout=csv.writer(buf,delimiter='\t',lineterminator='\n')
            csvout.writerow(('id','en','vi','ctx'))
            for r in sources[s]:
                en=r['en'];pre=en[:len(en)-len(body(en))]
                vi=pre+translations[body(en)]
                verify(en,vi,r['id'])
                r['vi']=vi
                csvout.writerow((r['id'],en,vi,r['ctx']))
                delta.append(r.copy())
            files[NEW+f'translation/04-thoai/talkfigs__0eng__data__{s}.jsonl']=''.join(
                json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in sources[s]).encode('utf-8')
            files[NEW+f'manual_{s.replace(".","_")}.tsv']=buf.getvalue().encode('utf-8')
            files[NEW+f'vi_{s.replace(".","_")}.txt']=''.join(
                f'{r["id"]}\t{r["vi"]}\n' for r in sources[s]).encode('utf-8')
        files[NEW+'DELTA-077.jsonl']=''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in delta).encode('utf-8')
        files[NEW+'mq077_new_translations.txt']=(BASE/'mq077_new_translations.txt').read_bytes()
        files[NEW+'build_077.py']=pathlib.Path(__file__).read_bytes()
        progress=BASE_COUNT+len(delta)
        npc=NPC_BASE+len(delta)
        pct=f'{progress/TOTAL*100:.2f}'
        qa=f'''# QA — Magician's Quest Checkpoint 077 (09/11/2026)

- **PASS:** đối chiếu 501 tệp JSONL / 55.976 bản ghi với checkpoint 076.
- **{BASE_COUNT:,} → {progress:,} / 55.976 ({pct}%)**: bổ sung đúng 240 bản dịch NPC.
- `0042.007`: 120/120; `0042.008`: 120/120.
- **77 mẫu câu tiếng Anh riêng**, loại trừ tiền tố lệnh NDS; **25 mẫu biên tập mới, 52 mẫu tái sử dụng** theo nội dung tiếng Anh chính xác.
- Chỉ đúng hai JSONL đích thay đổi trường `vi`; **499 JSONL còn lại giữ nguyên từng byte**.
- Giữ nguyên {BASE_COUNT:,} bản dịch đã có trước đó, mọi `id`, `en`, `ctx`, và trường nguồn khác.
- Mỗi bản dịch mới giữ nguyên thứ tự và nội dung của token `$...;`, Unicode NFC, tối đa 3 dấu `▼`, tối đa 34 ký tự tĩnh trên mỗi đoạn.
- Không gộp trang, không đổi cấu trúc bản ghi, không lẫn dữ liệu game khác.
- ZIP CRC PASS (`testzip()`), danh sách tệp không trùng lặp.
- **Chưa thử trên ROM NDS:** độ dài tĩnh không phản ánh bề rộng chữ thực tế hay nội dung của biến động.
- **Đợt 078:** `0042.009` và `0042.010` (120+120 nguồn tiếng Anh, chưa dịch).
'''
        files[NEW+'QA-077.md']=qa.encode('utf-8')
        checkpoint=f'''# Magician's Quest — Checkpoint 077

**Ngày:** 09/11/2026  
**Repository:** `ronvotri/VH-NDS`, chỉ thư mục `Magicians-Quest-Mysterious-Times/`.

- **Dịch mới 240 trang thoại:** `0042.007` và `0042.008` (120 trang/tệp).
- **Tổng tiến độ {progress:,}/55.976 ({pct}%).** Hội thoại NPC **{npc:,}/52.608**.
- **77 mẫu câu riêng:** 25 mẫu viết mới, 52 mẫu tái sử dụng đúng theo câu nguồn đã dịch ở checkpoint cũ.
- **Nội dung:** các tin đồn, chuyện học đường, cảm nhận về bạn bè, lựa chọn trả lời, NPC tính cách kiêu ngạo.
- Văn phong tự nhiên, hài hước vừa phải; bạn bè xưng tớ–cậu, không tự thêm meme hoặc thay token động.
- QA đầy đủ trong `QA-077.md`; kèm TSV EN–VI, `DELTA-077.jsonl`, `mq077_new_translations.txt`, `build_077.py`.
- **Đợt tiếp theo 078:** `0042.009` + `0042.010` đã có trong kho dữ liệu ZIP, `vi:null`.
- Chưa kiểm thử hiển thị trực tiếp trên ROM Nintendo DS.
'''
        files[NEW+'CHECKPOINT-2026-11-09-DOT-77.md']=checkpoint.encode('utf-8')
        top=f'**Checkpoint mới nhất: 077 (09/11/2026) — {progress:,}/55.976 ({pct}%).** +240 trang thoại (`0042.007`, `0042.008`). Xem `CHECKPOINT-2026-11-09-DOT-77.md`, `QA-077.md`. Đợt tiếp: `0042.009` + `0042.010`.\n\n'
        files[NEW+'README.md']=(top+files[NEW+'README.md'].decode('utf-8')).encode('utf-8')
        intro=f'''## Checkpoint 077 — 09/11/2026

- +240 trang thoại từ `0042.007`, `0042.008`; tổng **{progress:,}/55.976 ({pct}%)**, thoại NPC **{npc:,}/52.608**.
- 25 mẫu viết mới + 52 mẫu tái sử dụng. QA 501 JSONL / 55.976 bản ghi PASS; 499 JSONL khác nguyên byte.
- ZIP `MagiciansQuest-VietHoa-Checkpoint-077.zip` là checkpoint đầy đủ, gồm mã tái tạo, bảng EN–VI, delta, QA.
- Chưa thử trong ROM NDS. Tiếp `0042.009` và `0042.010` (240 trang nguồn chưa dịch).

'''
        files[NEW+'BAN_GIAO.md']=(intro+files[NEW+'BAN_GIAO.md'].decode('utf-8')).encode('utf-8')
        # Strict corpus audit against previous archive.
        count_files=total=old_done=new_done=changed_files=0
        for name in names:
            if '/translation/' not in name or not name.endswith('.jsonl'):continue
            count_files+=1
            dest=name.replace(OLD,NEW,1)
            old_bytes=prev.read(name);new_bytes=files[dest]
            target=any(dest.endswith(s+'.jsonl') for s in TARGET)
            if not target:assert old_bytes==new_bytes,name
            else:changed_files+=1
            a=[json.loads(x) for x in old_bytes.decode('utf-8').splitlines()]
            b=[json.loads(x) for x in new_bytes.decode('utf-8').splitlines()]
            assert len(a)==len(b),(name,len(a),len(b))
            for ar,br in zip(a,b):
                total+=1
                assert ar.keys()==br.keys() and all(ar[k]==br[k] for k in ar if k!='vi'),ar['id']
                old_done+=ar['vi'] is not None
                new_done+=br['vi'] is not None
                if ar['vi'] is not None:assert ar['vi']==br['vi'],ar['id']
                elif target:verify(ar['en'],br['vi'],ar['id'])
                else:assert br['vi'] is None,ar['id']
        assert (count_files,total,old_done,new_done,changed_files)==(501,TOTAL,BASE_COUNT,BASE_COUNT+240,2), (count_files,total,old_done,new_done,changed_files)
        for s in NEXT:
            n=NEW+f'translation/04-thoai/talkfigs__0eng__data__{s}.jsonl'
            nxt=[json.loads(l) for l in files[n].decode('utf-8').splitlines()]
            assert len(nxt)==120 and all(r['vi'] is None for r in nxt),s
        output.parent.mkdir(parents=True,exist_ok=True)
        with zipfile.ZipFile(output,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=7,allowZip64=True) as out:
            for n,raw in sorted(files.items()):out.writestr(n,raw)
    with zipfile.ZipFile(output) as out:
        assert out.testzip() is None
        assert len(out.namelist())==len(set(out.namelist()))
        print('PASS: ZIP CRC, 501 JSONL, 55,976 rows, 499 old files identical, +240 translations. Files',len(out.namelist()))
    print('TOTAL',progress,'/',TOTAL, 'PERCENT',pct,'SIZE',output.stat().st_size,'SHA256',hashlib.sha256(output.read_bytes()).hexdigest())

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--previous',type=pathlib.Path,default=BASE/'MagiciansQuest-VietHoa-Checkpoint-076.zip')
    ap.add_argument('--output',type=pathlib.Path,default=BASE/'MagiciansQuest-VietHoa-Checkpoint-077.zip')
    args=ap.parse_args()
    run(args.previous,args.output)
