#!/usr/bin/env python3
"""Magician's Quest batch 056. Rebuild from immutable verified checkpoint 055.
Translate source lines in 0040.009 / 0040.010 without altering source IDs, English,
ctx, other JSONL, or NDS code tokens.
"""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import json, re, unicodedata, hashlib

HOME=Path('/mnt/data')
OLD=HOME/'MagiciansQuest-VietHoa-Checkpoint-055.zip'
NEW=HOME/'MagiciansQuest-VietHoa-Checkpoint-056.zip'
ROOT='MagiciansQuest_056'
PREFIX=re.compile(r"^(?:\$(?:024|023|022|034|040)(?:['0-9-]+)*;)+")
TOKEN=re.compile(r"\$\d{3}(?:'[0-9-]+)*;")
SUFFIXES=('0040.009','0040.010')

VI_009='''
Không hẳn.$018'2;
Ra vậy... Hóa ra▼tin đồn cũng có phần đúng.
Nếu chuyện đó sang chảnh▼như tớ nghĩ thì▼nhớ cho tớ tham gia!
Gì cơ? Cậu bảo▼tin đồn KHÔNG đúng à?!
Tớ không thích bị▼dắt mũi thế đâu...$033;
Cậu nghe chưa?▼Mọi người đang đồn rằng...
"Nghe nói $530'0;▼đã $531; rồi làm▼$533; kỳ quặc."
Dù chỉ là lời đồn,▼chắc cũng có chút thật▼trong đó chứ?$018'1;
Đúng vậy.$018'1;
"Nghe nói $530'0;▼đã $531; rồi▼$533; rất cẩn thận."
Tớ nghe loáng thoáng rằng...
"$530'0; siêu ngầu,▼theo lời $533;."
Cậu nghe tin đó chưa?$018'1;
Nghe rồi.$018'1;
Chưa nghe.$018'2;
Cậu biết trước tớ rồi đấy!▼Ước gì cũng có tin đồn▼về TỚ nhỉ...
Vậy là cậu CHƯA biết!
Thấy chưa! Ai bảo tin đồn▼nào cũng xấu!$033;
"$530'0;▼$533;▼vì biết quan tâm."
Cậu biết rồi à?▼Tin đồn ấy chắc▼rầm rộ lắm nhỉ...
"$530'0;▼$533;▼vì hay bày trò."
Vậy là cậu biết rồi.▼Nếu chuyện ấy có thật...
lần sau cậu nên▼cẩn thận hơn một chút.
Nếu đó là thật, lần sau▼cậu nên tế nhị▼hơn đấy!$033;
"$530'0; và $530'1;▼lúc nào cũng $533;▼cùng nhau."
"$530'0; và $530'1;▼đã công khai $533;."
"$530'0; và $530'1;▼$533;."
Pháo hoa hôm đó thế nào?
"$530'0; và $530'1;▼đang bí mật $533;."
"$530'0; khiến $530'1;▼$533;."
Sao cậu không kể tớ nghe?
Chậc chậc...▼Biết làm sao với cậu đây?
"$530'0; và $530'1;▼$533;!"
Nghe vui quá còn gì!
"$533;▼tình bạn thân thiết giữa▼$530'0; và $530'1;."
'''.strip().splitlines()

VI_010='''
Cậu nghe chưa?▼Mọi người đang đồn rằng...
"$530'0; và $530'1;▼$533; nhờ▼mối gắn kết bền chặt."
Dù chỉ là lời đồn,▼chắc cũng có chút thật▼trong đó chứ?$018'1;
Đúng vậy.$018'1;
Không hẳn.$018'2;
Ra vậy... Hóa ra▼tin đồn cũng có phần đúng.
Có tin gì đáng chú ý,▼nhớ báo ngay cho tớ nhé!
Gì cơ? Cậu bảo▼tin đồn KHÔNG đúng à?!
Tớ không thích bị▼dắt mũi thế đâu...$033;
Thật sao?! Vậy là▼không hoàn toàn bịa đặt à?
Sao cậu không kể tớ nghe?
"Hành động đáng ngờ của▼$530'0;▼$533;."
Cứ kể hết cho tớ nghe.▼Tớ kín miệng lắm mà.
Có chuyện gì khó xử,▼cậu cứ đến tìm tớ nhé!
"$530'0; định học hành▼thật chăm để trở thành▼$533;."
Đỉnh thật đấy!▼Tớ ủng hộ hết mình!
Trời ơi, cậu làm sao thế?▼Bớt quá đà lại chút đi!
Chào $500;. Tớ nghe thấy▼chút tin đồn về cậu.
Nghe bảo cậu và $530'1;▼đang yêu nhau say đắm.
Không thể nào là thật!▼Chắc chỉ là hiểu lầm thôi.
Đừng lo. Tớ tin lời cậu...
Chắc cậu và $530'1;▼là bạn rất thân thôi...
Tớ hơi ghen, nhưng có▼bạn tốt cũng đâu phải xấu.
Tớ chỉ mong cậu▼dành thêm thời gian cho tớ...
Ai cũng bảo $530'1;▼từ chối cậu. Thật không?▼Không thể nào...
Dù sao tớ với cậu▼đang hẹn hò mà.▼Nói đó không thật đi.
Ồ, vậy cũng chẳng sao.▼Chỉ là tin đồn thôi...
"$535'0; và $535'1;▼$538;."
Có lẽ...$018'1;
Chắc không.$018'2;
Nếu chuyện đó sang chảnh▼như tớ nghĩ thì▼nhớ cho tớ tham gia!$032;
Tớ không thích bị▼dắt mũi thế đâu...
"$535'0; và $535'1;▼đã $538;."
'''.strip().splitlines()

assert (len(VI_009),len(VI_010))==(35,33)

def jd(d):return json.dumps(d, ensure_ascii=False, separators=(',',':'))
def source_lines(txt): return [json.loads(line) for line in txt.splitlines() if line.strip()]

def template_name(name):
    oldprefix=name.split('/',1)[0]
    return ROOT+'/'+name.split('/',1)[1] if oldprefix.startswith('MagiciansQuest_') else name

with ZipFile(OLD,'r') as old:
    assert old.testzip() is None
    oldnames=old.namelist()
    entries={template_name(n):old.read(n) for n in oldnames}
    def jsonl_path(s):return f'{ROOT}/translation/04-thoai/talkfigs__0eng__data__{s}.jsonl'
    delta=[]; mappings={}
    for suffix,lines in zip(SUFFIXES,[VI_009,VI_010]):
        path=jsonl_path(suffix)
        original=source_lines(entries[path].decode('utf-8'))
        assert len(original)==120 and all(r.get('vi') is None for r in original), (suffix,len(original))
        keys=list(dict.fromkeys(PREFIX.sub('',r['en']) for r in original))
        assert len(keys)==len(lines), (suffix,len(keys),len(lines))
        mapping=dict(zip(keys,lines))
        mappings[suffix]=mapping
        result=[]
        for row in original:
            vi=PREFIX.match(row['en']).group(0) if PREFIX.match(row['en']) else ''
            vi+=mapping[PREFIX.sub('',row['en'])]
            assert TOKEN.findall(row['en']) == TOKEN.findall(vi), (suffix,row['id'],'tokens')
            assert vi==unicodedata.normalize('NFC',vi), (suffix,row['id'],'NFC')
            assert '\r' not in vi and '\n' not in vi and '\t' not in vi, (suffix,row['id'],'control')
            segments=vi.split('▼')
            assert len(segments)<=4 and all(len(TOKEN.sub('',seg))<=34 for seg in segments), (suffix,row['id'],'width',segments)
            new={**row,'vi':vi}
            assert list(new)==list(row)
            result.append(new)
            delta.append({'file':f'04-thoai/talkfigs__0eng__data__{suffix}.jsonl','id':row['id'],'en':row['en'],'old_vi':row['vi'],'vi':vi,'ctx':row['ctx']})
        entries[path]=('\n'.join(jd(r) for r in result)+'\n').encode('utf-8')
        k=suffix.replace('.','_')
        entries[f'{ROOT}/vi_{k}.txt']=('\n'.join(r['vi'] for r in result)+'\n').encode('utf-8')
        entries[f'{ROOT}/manual_{k}.tsv']=('id\ten\tvi\tctx\n'+'\n'.join('\t'.join(map(str,[r['id'],r['en'],r['vi'],r['ctx']])) for r in result)+'\n').encode('utf-8')
    assert len(delta)==240

    docs={
    'QA-056.md':'''# QA — Magician’s Quest · Đợt 056

- **PASS:** so sánh 501 JSONL / 55.976 bản ghi của checkpoint 055 và 056.
- **+240 trang:** `0040.009` (120), `0040.010` (120). Từ **15.312 → 15.552/55.976 (27,78%)**; thoại NPC **12.187 → 12.427/52.608**.
- **PASS:** chỉ thay 240 trường `vi` từ `null` thành bản dịch ở hai tệp đích; toàn bộ ID/EN/CTX không đổi, 15.312 bản dịch cũ giữ nguyên; các tệp JSONL khác giữ nguyên byte.
- **PASS:** mọi token NDS `$...;` (tên động `$500;`, `$530'0;`, `$530'1;`, `$531;`, `$533;`, `$535'0;`, `$535'1;`, `$538;`; lựa chọn `$018'1;`, `$018'2;`, `$032;`, `$033;`; biểu cảm) giữ đúng thứ tự và giá trị.
- **PASS:** NFC, không dòng mới/tab trong trường `vi`, tối đa 3 `▼` và không đoạn văn tĩnh nào dài hơn 34 ký tự sau khi bỏ token điều khiển.
- **PASS:** tính toàn vẹn ZIP, tổng số bản ghi, số tệp, và kiểm đếm bản dịch; script `qa_056.py` có thể chạy lại.
- **Chưa kiểm thử trực tiếp trên ROM NDS** hoặc kiểm thực tế chiều rộng các biến động sau khi game thay tên/hành động.
''',
    'CHECKPOINT-2026-11-08-DOT-56.md':'''# Magician’s Quest: Mysterious Times — Checkpoint 056

**Ngày:** 08/11/2026 · **Repo:** `ronvotri/VH-NDS` / `Magicians-Quest-Mysterious-Times/`

| Tệp | Mục mới | Nội dung |
|---|---:|---|
| `0040.009` | 120 | Hỏi lại về tin đồn, bình phẩm chuyện hành động kỳ lạ, tình bạn và những lời khuyên |
| `0040.010` | 120 | Kiểm chứng tin đồn, giữ bí mật, lời tỏ tình/ghen tuông, hỏi chuyện yêu đương, lựa chọn người chơi |

**Tiến độ:** **15.552/55.976 (27,78%)**, tăng 240 từ checkpoint 055 (15.312); thoại NPC **12.427/52.608**.

**QA:** đối chiếu từng bản ghi của 501 JSONL / 55.976 mục với ZIP 055. Chỉ thay `vi` từ `null` sang tiếng Việt trên 240 bản ghi đích; giữ nguyên 15.312 bản dịch cũ, toàn bộ mã điều khiển và giới hạn dòng tĩnh. ZIP kiểm toàn vẹn PASS. Chưa build/thử trên ROM NDS hoặc kiểm động với tên NPC dài.

**Bàn giao:** ZIP `MagiciansQuest-VietHoa-Checkpoint-056.zip`; bảng `manual_0040_009.tsv` và `manual_0040_010.tsv`; `DELTA-056.jsonl`, `QA-056.md`, `build_056.py`, `qa_056.py`.

**Đợt tiếp 057:** ưu tiên `0040.011` và `0040.012` (120 trang/tệp) đã có trong ZIP nguồn; cần stage lên GitHub.
'''
    }
    for name,txt in docs.items():entries[f'{ROOT}/{name}']=txt.encode('utf-8')
    entries[f'{ROOT}/DELTA-056.jsonl']=('\n'.join(jd(x) for x in delta)+'\n').encode('utf-8')
    update=f'**Checkpoint mới nhất: 056 (08/11/2026) — 15.552 / 55.976 mục (27,78%).** Đợt 056 +240 hội thoại NPC (0040.009 + 0040.010) về kiểm chứng tin đồn, cảm xúc khi hẹn hò và trò chuyện với bạn bè. QA đối chiếu toàn bộ 501 JSONL / 55.976 bản ghi với ZIP 055, giữ nguyên 15.312 bản dịch cũ. Xem `CHECKPOINT-2026-11-08-DOT-56.md`, `QA-056.md`, `DELTA-056.jsonl`. Tiếp đợt 057: `0040.011` và `0040.012`.\n\n'
    for target in ['README.md','BAN_GIAO.md']:
        raw=entries[f'{ROOT}/{target}'].decode('utf-8')
        if target=='BAN_GIAO.md':
            hd='## Checkpoint 056 — 08/11/2026\n\n- **15.552/55.976 (27,78%)**, thoại NPC **12.427/52.608**, +240 bản ghi mới; hoàn thành `0040.009`, `0040.010`.\n- QA toàn bộ 501 JSONL / 55.976 bản ghi so với ZIP 055, chỉ thêm 240 trường `vi` mới; giữ nguyên dữ liệu cũ và tất cả token.\n- ZIP bàn giao đầy đủ ở Thư viện `Dịch giả lập/MagiciansQuest-VietHoa-Checkpoint-056.zip`; chưa test ROM NDS.\n- Tiếp theo: `0040.011`, `0040.012` đã có sẵn trong gói.\n\n'
        else:hd=update
        entries[f'{ROOT}/{target}']=(hd+raw).encode('utf-8')
    entries[f'{ROOT}/build_056.py']=Path(__file__).read_bytes()
    qapath=HOME/'mq_qa_056.py'
    if qapath.exists():entries[f'{ROOT}/qa_056.py']=qapath.read_bytes()

    with ZipFile(NEW,'w',compression=ZIP_DEFLATED,compresslevel=6) as nw:
        for name,data in entries.items():nw.writestr(name,data)
    print('Created',NEW,'entries',len(entries),'delta',len(delta), 'bytes',NEW.stat().st_size)
    print('Old archive SHA256',hashlib.sha256(OLD.read_bytes()).hexdigest())
    print('New archive SHA256',hashlib.sha256(NEW.read_bytes()).hexdigest())
