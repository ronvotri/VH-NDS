#!/usr/bin/env python3
"""Create complete Magician's Quest checkpoint 064 from checkpoint 063.
Preserves all English/ID/context/token fields and every previously translated record.
"""
from __future__ import annotations
import collections, hashlib, json, re, sys, unicodedata, zipfile
from pathlib import Path

HERE=Path(__file__).resolve().parent
OLD=Path(sys.argv[1]) if len(sys.argv)>1 else Path('/mnt/data/MagiciansQuest-VietHoa-Checkpoint-063.zip')
NEW=Path(sys.argv[2]) if len(sys.argv)>2 else Path('/mnt/data/MagiciansQuest-VietHoa-Checkpoint-064.zip')
ROOT_OLD='MagiciansQuest_063/'
ROOT_NEW='MagiciansQuest_064/'
TARGETS=('0041.003','0041.004')
TOKEN=re.compile(r"\$\d{3}(?:'[0-9-]+)*;")
PREFIX=re.compile(r"^(?:\$(?:024|023|022|004)(?:'[0-9-]+)*;)+")
SUFFIX=re.compile(r"(?:\$(?:079|074|019|018|073|033|085)(?:'[0-9-]+)*;)+$")

def split_en(en):
    m=PREFIX.match(en)
    pre=m.group(0) if m else ''
    body=en[len(pre):]
    n=SUFFIX.search(body)
    suf=n.group(0) if n else ''
    return pre, body[:len(body)-len(suf)] if suf else body, suf

def check(row, vi):
    assert isinstance(vi,str) and vi
    assert unicodedata.normalize('NFC',vi)==vi
    assert TOKEN.findall(vi)==TOKEN.findall(row['en']), (row['id'],'tokens',TOKEN.findall(vi),TOKEN.findall(row['en']))
    assert vi.count('▼')<=3,(row['id'],'too many breaks')
    assert not any(x in vi for x in '\r\n\t'),row['id']
    assert all(len(TOKEN.sub('',p))<=34 for p in vi.split('▼')),(row['id'],'width', [(len(TOKEN.sub('',p)),p) for p in vi.split('▼')])

# Unique source-line ordinal numbers, derived from the stable ordered records in the source.
# Deliberately translated by hand; recurring lines are carried from checkpoint 063 instead.
MANUAL_003={
44:'Ở đó tớ có cả đống bạn bè!',
45:'Bọn tớ chơi cùng,▼học cùng nữa...▼Vui hết nấc luôn!',
46:'Bữa sau cậu đến chơi nhé!▼Vui lắm đấy!',
47:'Thế là năm sắp hết rồi.',
48:'Trước giờ đếm ngược,▼cậu muốn làm gì nào?',
49:'Năm nào cũng tổ chức,▼mà tiệc trà xuân▼vẫn vui hết biết!',
50:'Tớ chẳng mê trà đâu,▼nhưng đồ ăn ở đó ngon cực!',
51:'Vui thế này mà cũng giúp▼mình thành phù thủy giỏi hơn à?',
52:'Nếu vậy, ngày nào▼tớ cũng muốn mở tiệc trà!',
53:'Cậu thử thách lòng can đảm▼chưa thế?',
54:'Tớ phải vật lộn mãi▼mới xử lý hết lũ ma.',
55:'Không biết cái $507\'117;▼mà thầy Vlad nhắc đến▼ở đâu nhỉ...',
56:'Tớ lục khắp các phòng rồi.▼Có gì đó sai sai...',
57:'Sẵn sàng thi nấu lẩu nấm▼chưa nào?',
58:'Ôi, mong được ăn▼nấm ngon quá đi...!',
59:'Thầy Oakley bảo đây▼cũng là một phần buổi học,▼nhưng tớ thấy...',
60:'Tớ nghĩ thầy ấy chỉ muốn▼tham gia cho vui thôi!',
61:'Năm nào cũng có,▼nhưng lễ hội tuyết cầu vồng▼vẫn vui hết sảy!',
62:'Hôm trước hiệu trưởng Sol▼có nhắc đến lễ hội...',
63:'Thầy bảo đó là nghi lễ▼quan trọng để đón mùa xuân.',
64:'Không biết nếu làm hỏng▼nghi lễ thì sao nhỉ...',
65:'Ôi không! Lỡ mùa xuân▼không bao giờ đến thì sao?',
66:'Không có mùa xuân▼thì tớ sống sao nổi!',
67:'Này, xin lỗi vì đã gửi▼bức điện tín kỳ quặc nhé.',
68:'Quên chuyện đó đi nhé.▼Bữa nào mình đi chơi lại!',
69:'Mình làm lại từ đầu nhé!',
70:'Tớ chẳng nghe thầy dặn▼phải làm gì trong▼giờ ngoại khóa...',
71:'Mang con bọ nào đó▼đến là được chứ gì?',
}
MANUAL_004={
3:'Phù! Cuối cùng cũng xong▼bài ngoại khóa.▼Thầy tính hành tụi mình à?',
4:'Này, tớ biết bọn mình▼là bạn thân lâu rồi,▼nhưng mà...',
5:'Tớ muốn có chút không gian▼riêng một thời gian.',
6:'Đừng hiểu lầm nhé.▼Đâu phải tớ ghét cậu▼hay gì đâu.',
7:'Chỉ là... cứ dính nhau mãi,▼tớ sợ mình không còn▼biết quý cậu nữa.',
8:'Tạm thời mình cứ chơi▼như bạn bình thường nhé!',
9:'Ê, chào!',
10:'Này, tớ biết mình đã▼hẹn hò lâu rồi, nhưng...',
11:'Tớ không thể tiếp tục▼hẹn hò như thế này nữa.',
12:'Mình vẫn là bạn nhé!▼Nếu cậu đồng ý...',
13:'Sao thế? Cậu cần gì à?',
14:'Giờ tớ chẳng có▼chuyện gì hay để kể.',
}
assert len(MANUAL_003)==28 and len(MANUAL_004)==12

with zipfile.ZipFile(OLD) as zin:
    assert zin.testzip() is None, 'old ZIP CRC failure'
    records={}
    for name in zin.namelist():
        if name.startswith(ROOT_OLD+'translation/') and name.endswith('.jsonl'):
            records[name]=[json.loads(x) for x in zin.read(name).decode().splitlines()]
    assert len(records)==501,len(records)
    prev=collections.defaultdict(collections.Counter)
    for rows in records.values():
        for row in rows:
            if row.get('vi') is not None:
                en_body=split_en(row['en'])[1]
                vi_body=split_en(row['vi'])[1]
                prev[en_body][vi_body]+=1
    before=sum(sum(r['vi'] is not None for r in rows) for rows in records.values())
    assert before==17172,before
    changes={}; delta=[]; manual_stats=[]; mapping={}
    for suffix in TARGETS:
        path=f'translation/04-thoai/talkfigs__0eng__data__{suffix}.jsonl'
        rows=records[ROOT_OLD+path]
        assert len(rows)==120 and all(r['vi'] is None for r in rows),suffix
        seen={}
        for row in rows:
            e=split_en(row['en'])[1]
            if e not in seen:seen[e]=len(seen)+1
        assert len(seen)==(71 if suffix.endswith('003') else 15)
        choices=MANUAL_003 if suffix.endswith('003') else MANUAL_004
        missing=[]
        for e,i in seen.items():
            if i in choices:
                mapping[e]=choices[i]
            elif e not in mapping and not prev[e]:
                missing.append((i,e))
        assert not missing,(suffix,'untranslated new EN',missing)
        manual=['id\ten\tvi\tctx']
        reused=created=0
        output=[]
        for row in rows:
            pre,e,suf=split_en(row['en'])
            if e in mapping:
                body=mapping[e]
                created+=1
            elif prev[e]:
                body=prev[e].most_common(1)[0][0]
                reused+=1
            else:raise AssertionError((row['id'],e))
            val=unicodedata.normalize('NFC',pre+body+suf)
            check(row,val)
            item={**row,'vi':val}
            output.append(item)
            delta.append(item)
            manual.append('\t'.join(str(item[k]) for k in ('id','en','vi','ctx')))
        changes[path]=''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in output).encode('utf-8')
        changes[f'manual_{suffix.replace(".","_")}.tsv']=('\n'.join(manual)+'\n').encode('utf-8')
        changes[f'vi_{suffix.replace(".","_")}.txt']=('\n'.join(split_en(r['vi'])[1] for r in output)+'\n').encode('utf-8')
        manual_stats.append((suffix,len(output),len(seen),reused,created))
    assert len(delta)==240
    changes['DELTA-064.jsonl']=''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in delta).encode('utf-8')
    after=before+len(delta)
    assert after==17412
    npc=14047+len(delta)
    perc=round(after/55976*100,2)
    qa=f'''# QA — Magician’s Quest · Đợt 064

- **PASS:** Đối chiếu checkpoint 063 → 064 trên 501 JSONL / 55.976 bản ghi.
- **PASS:** Điền mới 240 trường `vi` trong `0041.003` và `0041.004` (120/tệp), **17.172 → 17.412/55.976 ({perc:.2f}%)**; thoại NPC **14.047 → {npc}/52.608**.
- **PASS:** Giữ nguyên 17.172 bản dịch cũ; 499 JSONL khác byte-identical, không thay ID/EN/CTX.
- **PASS:** Token `$...;` giữ thứ tự, Unicode NFC, tối đa 3 `▼`, tối đa 34 ký tự tĩnh/đoạn.
- **PASS:** Delta 240 bản ghi, 2 bảng EN–VI, ZIP CRC và QA chéo nguồn cũ.
- **CẦN KIỂM THỬ:** Chưa chạy ROM NDS; độ rộng thực tế sau khi thế biến động chưa xác minh.
'''
    checkpoint=f'''# Magician’s Quest — Checkpoint 064 (08/11/2026)

- **Tổng:** {after:,}/55.976 ({perc:.2f}%); thoại NPC {npc:,}/52.608.
- **Mới:** 240 trang thoại, `0041.003` (120) và `0041.004` (120).
- **Nội dung:** Bình luận về bạn bè, lễ hội trà xuân và tuyết cầu vồng, thử thách lòng can đảm, lẩu nấm, học ngoại khóa, tin nhắn làm hòa, những thay đổi tình bạn và hẹn hò.
- **QA:** 501 tệp / 55.976 bản ghi; giữ 17.172 bản dịch cũ, chỉ bổ sung 240 trường `vi`; đúng token NDS, NFC và giới hạn dòng tĩnh.
- **Đính kèm:** `DELTA-064.jsonl`, `QA-064.md`, `manual_0041_003.tsv`, `manual_0041_004.tsv`, `vi_0041_003.txt`, `vi_0041_004.txt`, script build/QA.
- **GitHub:** `ronvotri/VH-NDS` trong `Magicians-Quest-Mysterious-Times/`.
- **ZIP:** `/Dịch giả lập/MagiciansQuest-VietHoa-Checkpoint-064.zip`.
- **Chưa thử:** Hiển thị trong ROM NDS.
- **Tiếp đợt 065:** `0041.005` và `0041.006` (120 trang/tệp; nguồn đã có trong ZIP).
'''
    readme=f'**Checkpoint mới nhất: 064 (08/11/2026) — {after:,}/55.976 ({perc:.2f}%).** Thêm 240 trang thoại (`0041.003`, `0041.004`); QA 501 JSONL PASS, giữ 17.172 bản dịch cũ. Xem `CHECKPOINT-2026-11-08-DOT-64.md`, `DELTA-064.jsonl`, `QA-064.md`. Tiếp `0041.005`, `0041.006` (120 trang/tệp).\n\n'
    bg=f'''## Checkpoint 064 — 08/11/2026

- Tiến độ **{after:,}/55.976 ({perc:.2f}%)**, thoại NPC **{npc:,}/52.608**; thêm 240 trang.
- Hoàn thành `0041.003` và `0041.004` (120 trang/tệp); giữ nguyên token và giới hạn dòng.
- QA 501 JSONL / 55.976 bản ghi; 17.172 bản dịch cũ không thay, ID/EN/CTX nguyên vẹn.
- ZIP Thư viện: `/Dịch giả lập/MagiciansQuest-VietHoa-Checkpoint-064.zip`; chưa kiểm thử ROM.
- Đợt 065: `0041.005` và `0041.006`, mỗi tệp 120 trang, nguồn đã có trong ZIP.

'''
    changes['QA-064.md']=qa.encode('utf-8')
    changes['CHECKPOINT-2026-11-08-DOT-64.md']=checkpoint.encode('utf-8')
    changes['README.md']=(readme+zin.read(ROOT_OLD+'README.md').decode('utf-8')).encode('utf-8')
    changes['BAN_GIAO.md']=(bg+zin.read(ROOT_OLD+'BAN_GIAO.md').decode('utf-8')).encode('utf-8')
    changes['build_064.py']=Path(__file__).read_bytes()
    changes['qa_064.py']=(HERE/'qa_064.py').read_bytes()
    with zipfile.ZipFile(NEW,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=7) as zout:
        existing=set()
        for member in zin.infolist():
            path=member.filename.removeprefix(ROOT_OLD)
            if not path:continue
            assert path not in existing, ('duplicate old',path)
            existing.add(path)
            if member.is_dir():continue
            content=changes.pop(path,zin.read(member))
            zout.writestr(ROOT_NEW+path,content)
        for path,content in changes.items():
            assert path not in existing, ('duplicate new',path)
            zout.writestr(ROOT_NEW+path,content)
print('Built:',NEW, f'{NEW.stat().st_size:,} bytes', 'translated:',after,'NPC:',npc,'percent:',f'{perc:.2f}')
for x in manual_stats:print('suffix, pages, unique, reused rows, new/manual rows=',x)
print('SHA256:',hashlib.sha256(NEW.read_bytes()).hexdigest())
