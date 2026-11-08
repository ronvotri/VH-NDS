#!/usr/bin/env python3
"""Magician's Quest: batch 057, from immutable checkpoint 056.
Manual translation for unique English texts; reuses prior edited Vietnamese
for byte-identical English dialogue bodies. Retains all IDs, token order,
meta and prior JSONL unchanged.
"""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import json, re, unicodedata

HOME=Path('/mnt/data')
OLD=HOME/'MagiciansQuest-VietHoa-Checkpoint-056.zip'
NEW=HOME/'MagiciansQuest-VietHoa-Checkpoint-057.zip'
ROOT='MagiciansQuest_057'
PREFIX=re.compile(r"^(?:\$(?:024|023|022|034|040)(?:['0-9-]+)*;)+")
TOKEN=re.compile(r"\$\d{3}(?:'[0-9-]+)*;")
TARGETS=('0040.011','0040.012')

def jd(x):return json.dumps(x,ensure_ascii=False,separators=(',',':'))
def parsed(blob):return [json.loads(x) for x in blob.decode('utf8').splitlines() if x.strip()]
def get_body(s):return PREFIX.sub('',s)
def strip_tech(s):return PREFIX.sub('',s)
def relname(s):return ROOT+'/'+s.split('/',1)[1]
def pth(s):return f'{ROOT}/translation/04-thoai/talkfigs__0eng__data__{s}.jsonl'

# Index is 1-based position in unique EN-body order in each source file.
# Repeated lines/instances intentionally retain their own IDs and records.
MANUAL_011={
 10:"Nhắn họ rằng tớ luôn▼sẵn lòng nghe họ▼tâm sự nhé?$032;",
 11:'"$535\'0; và $535\'1;▼trông thật hạnh phúc,▼$538;."',
 12:'"$530\'0; và $530\'1;▼$533; hợp nhau quá mức,▼cứ như đang diễn vậy."',
 13:"Cậu nghe chưa?▼Có người đang đồn rằng...",
 14:'"$535\'0; và $535\'1;▼lúc nào cũng bên nhau.▼Tớ nghĩ $538;!"',
 15:'"Nghe nói $535\'0;▼đã $531; và trông▼rất $538;."',
 16:'"Nghe nói $535\'0;▼đã $531; và dùng▼$538; kỳ lạ."',
 17:'"Nghe nói $535\'0;▼đã $531; rồi làm▼$538; kỳ quặc."',
 18:'"Nghe nói $535\'0;▼đã $531; rồi▼$538; rất cẩn thận."',
 20:'"$535\'0; siêu ngầu,▼theo lời $538;."',
 24:'Cậu biết trước tớ rồi đấy!▼Ước gì cũng có tin đồn▼về TỚ nhỉ...$032;',
 26:'Thấy chưa! Ai bảo▼tin đồn nào cũng xấu!',
 27:'"$535\'0;▼$538;▼vì biết quan tâm."',
 28:'Cậu biết rồi à?▼Tin đồn đó chắc phải▼rầm rộ lắm nhỉ...$032;',
 29:'"$535\'0;▼$538;▼vì hay bày trò."',
 30:'Biết phải làm gì với họ đây?!$032;',
 31:'Biết phải làm gì với họ đây?!',
 32:'"$535\'0; và $535\'1;▼lúc nào cũng $538;▼cùng nhau."',
 33:'Ghen tị quá đi!$032;',
 34:'Chẳng vui chút nào!',
 35:'"$535\'0; và $535\'1;▼đã công khai $538;."',
}
MANUAL_012={
 5:'Thế... cậu nghĩ họ▼thích pháo hoa hôm đó không?$032;',
 9:'"$535\'0; và $535\'1;▼lén lút $538;."',
 11:'"$535\'0; khiến $535\'1;▼$538;."',
 15:'Nghe cũng vui đấy chứ!$032;',
 16:'"$538;▼tình bạn thân thiết giữa▼$535\'0; và $535\'1;."',
 17:'Cứ kể tớ nghe đi.▼Tớ giữ kín như bưng!$032;',
 18:'"$535\'0; và $535\'1;▼$538; nhờ mối▼gắn kết bền chặt."',
 19:'Nếu có gì mới, hợp mốt,▼nhớ kể tớ nghe hết nhé!$032;',
 20:'Chắc có lý do gì đó...▼Thôi thì tớ sẽ▼giữ im lặng vậy.$032;',
 21:'"Hành động đáng ngờ của▼$535\'0;▼$538;."',
 22:'Cậu nghe chưa?▼Mọi người đang kháo nhau...',
 23:'Tớ nghe cậu định▼chăm chỉ học để mai này▼trở thành $538;...',
 24:'Đó là tin đồn đấy.▼Có thật không?$018\'1;',
 25:'Sốc thật đấy! Nhưng▼tớ chắc chắn sẽ▼ủng hộ họ!$032;',
 26:'Này, chào cậu!▼Đoán xem tớ vừa nghe▼được chuyện gì nào!',
}

with ZipFile(OLD) as old:
    assert old.testzip() is None
    entries={relname(n):old.read(n) for n in old.namelist() if not n.endswith('/')}
    reuse={}
    for s in ('0040.009','0040.010'):
        for row in parsed(entries[pth(s)]):
            reuse[get_body(row['en'])]=strip_tech(row['vi'])
    delta=[]
    for suffix,custom in zip(TARGETS,(MANUAL_011,MANUAL_012)):
        rows=parsed(entries[pth(suffix)])
        assert len(rows)==120 and all(r['vi'] is None for r in rows),suffix
        uniq=list(dict.fromkeys(get_body(r['en']) for r in rows))
        assert len(uniq)==(36 if suffix.endswith('011') else 26)
        mapping={}
        for i,key in enumerate(uniq,1):
            if i in custom: trans=custom[i]
            else:
                if key not in reuse: raise ValueError(f'Missing translation {suffix} line {i}: {key}')
                trans=reuse[key]
            assert trans==unicodedata.normalize('NFC',trans)
            assert TOKEN.findall(key)==TOKEN.findall(trans), (suffix,i,'mismatched control token',key,trans)
            assert len(trans.split('▼'))<=4,(suffix,i,'too many lines')
            assert all(len(TOKEN.sub('',v))<=34 for v in trans.split('▼')),(suffix,i,'width',trans)
            mapping[key]=trans
        assert len(mapping)==len(uniq)
        reuse.update(mapping) # allow exact matches from 0040.011 within 0040.012
        out=[]
        for r in rows:
            prefix=PREFIX.match(r['en'])
            prefix=prefix.group(0) if prefix else ''
            val=prefix+mapping[get_body(r['en'])]
            assert TOKEN.findall(r['en'])==TOKEN.findall(val),(suffix,r['id'])
            assert val==unicodedata.normalize('NFC',val)
            assert '\n' not in val and '\r' not in val and '\t' not in val
            assert len(val.split('▼'))<=4 and all(len(TOKEN.sub('',z))<=34 for z in val.split('▼'))
            out.append({**r,'vi':val})
            delta.append({'file':f'04-thoai/talkfigs__0eng__data__{suffix}.jsonl','id':r['id'],'en':r['en'],'old_vi':None,'vi':val,'ctx':r['ctx']})
        entries[pth(suffix)]=('\n'.join(jd(r) for r in out)+'\n').encode('utf8')
        ident=suffix.replace('.','_')
        entries[f'{ROOT}/vi_{ident}.txt']=('\n'.join(r['vi'] for r in out)+'\n').encode('utf8')
        entries[f'{ROOT}/manual_{ident}.tsv']=('id\ten\tvi\tctx\n'+'\n'.join('\t'.join(map(str,(r['id'],r['en'],r['vi'],r['ctx']))) for r in out)+'\n').encode('utf8')
        print(f'{suffix}: {len(rows)} pages, {len(uniq)} unique EN templates, new manual {len(custom)}')
    assert len(delta)==240
    entries[f'{ROOT}/DELTA-057.jsonl']=('\n'.join(jd(r) for r in delta)+'\n').encode('utf8')
    progress=15552+240
    pct=progress/55976*100
    details='''# Magician’s Quest: Mysterious Times — Checkpoint 057

**Ngày:** 08/11/2026 · **Repo:** `ronvotri/VH-NDS` · `Magicians-Quest-Mysterious-Times/`

| Tệp | Trang mới | Nội dung |
|---|---:|---|
| `0040.011` | 120 | Tin đồn về hai người bạn, đi chơi cùng nhau, các hành động đáng ngờ, đối thoại biết/chưa biết tin |
| `0040.012` | 120 | Tin đồn tình yêu, pháo hoa, niềm tin, phép thuật, chuyện học và phản ứng giữ bí mật |

**Tiến độ:** **15.792/55.976 (28,21%)**, tăng 240 từ checkpoint 056 (15.552); hội thoại NPC **12.667/52.608**.

**Thành phẩm:** 2 JSONL có trường `vi`, 2 bảng `manual_0040_011.tsv` và `manual_0040_012.tsv`, `vi_0040_011.txt`, `vi_0040_012.txt`, `DELTA-057.jsonl`, `QA-057.md`, `build_057.py`, `qa_057.py`.

**QA:** Đối chiếu toàn bộ 501 JSONL/55.976 bản ghi với ZIP checkpoint 056, giữ 15.552 bản dịch cũ, chỉ bổ sung 240 trường `vi` mới; các trường `id/en/ctx` và token game không thay. Không thay hay gộp bản ghi lặp. Giới hạn tĩnh 34 ký tự/đoạn, tối đa 3 `▼`/trang.

**Chưa test trực tiếp trên ROM NDS**; cần kiểm width của tên/hành động động trong game. Tệp nguồn đợt 058: `0040.013` và `0040.014` đã giữ nguyên trong ZIP 057.
'''
    qa='''# QA — Magician’s Quest · Đợt 057

- **PASS**: so sánh 501 JSONL / 55.976 mục checkpoint 056 và 057.
- **+240 mục**: `0040.011` và `0040.012`, 120 mục/tệp, **15.552 → 15.792/55.976 (28,21%)**; NPC **12.427 → 12.667/52.608**.
- **PASS**: chỉ thay `vi` ở 240 dòng từ `null` thành tiếng Việt, giữ nguyên 15.552 bản dịch cũ và tất cả bản ghi ngoài hai tệp đích theo từng byte.
- **PASS**: mọi mã điều khiển `$...;` có cùng giá trị, thứ tự; gồm `$535'0;`, `$535'1;`, `$538;`, `$530'0;`, `$530'1;`, `$531;`, `$533;`, `$018'1;`, `$018'2;`, `$032;` và các mã biểu cảm.
- **PASS**: NFC, không `CR/LF/TAB` trong `vi`, tối đa 3 dấu `▼` và 34 ký tự văn bản tĩnh mỗi đoạn sau bỏ token.
- **PASS**: kiểm tra ZIP CRC/toàn vẹn và tổng 501 JSONL / 55.976 mục.
- **Cần kiểm thử thật trên ROM NDS**: chiều rộng chữ và giá trị tên/hành động động sau render, giới hạn bộ font.

Chạy lại: `python qa_057.py /mnt/data/MagiciansQuest-VietHoa-Checkpoint-056.zip /mnt/data/MagiciansQuest-VietHoa-Checkpoint-057.zip`.
'''
    entries[f'{ROOT}/CHECKPOINT-2026-11-08-DOT-57.md']=details.encode('utf8')
    entries[f'{ROOT}/QA-057.md']=qa.encode('utf8')
    entries[f'{ROOT}/README.md']=(f'**Checkpoint mới nhất: 057 (08/11/2026) — 15.792 / 55.976 mục (28,21%).** +240 trang NPC (`0040.011`, `0040.012`) với tin đồn, hỏi đáp, chuyện tình cảm/học tập. Xem `CHECKPOINT-2026-11-08-DOT-57.md`, `QA-057.md`, `DELTA-057.jsonl`. ZIP checkpoint 057 lưu Thư viện `Dịch giả lập/`. Nguồn tiếp 058: `0040.013` và `0040.014`.\n\n'+entries[f'{ROOT}/README.md'].decode('utf8')).encode('utf8')
    entries[f'{ROOT}/BAN_GIAO.md']=(f'## Checkpoint 057 — 08/11/2026\n\n- Tổng **15.792/55.976 (28,21%)**, hội thoại NPC **12.667/52.608**; thêm 240 trang (`0040.011`/`0040.012`, 120 trang/tệp).\n- Tái dùng bản dịch trùng từ các đợt trước, biên tập những câu mới. Mọi mã `$...;` giữ nguyên thứ tự và giá trị.\n- QA đối chiếu 501 JSONL / 55.976 bản ghi checkpoint 056 và 057: chỉ điền 240 `vi`, giữ 15.552 bản dịch cũ, không thay id/en/ctx hay các tệp khác.\n- Bàn giao đủ `manual_0040_011.tsv`, `manual_0040_012.tsv`, `DELTA-057.jsonl`, `QA-057.md`, `build_057.py`, `qa_057.py` và ZIP. Chưa test thực tế trên ROM.\n- Đợt tiếp 058: `0040.013` và `0040.014` đã nằm trong ZIP.\n\n'+entries[f'{ROOT}/BAN_GIAO.md'].decode('utf8')).encode('utf8')
    entries[f'{ROOT}/build_057.py']=Path(__file__).read_bytes()
    entries[f'{ROOT}/qa_057.py']=(HOME/'qa_057.py').read_bytes()

    with ZipFile(NEW,'w',ZIP_DEFLATED,compresslevel=6) as z:
        for n,data in sorted(entries.items()):z.writestr(n,data)
    with ZipFile(NEW) as z:assert z.testzip() is None
    print(f'Wrote {NEW}, files={len(entries)}, bytes={NEW.stat().st_size}, progress={progress}/{55976} ({pct:.2f}%)')
