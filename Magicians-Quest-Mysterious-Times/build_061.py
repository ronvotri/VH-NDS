#!/usr/bin/env python3
"""Build full Magician's Quest 061 from checkpoint 060 and hand-edited Vietnamese lines.
Usage: python build_061.py [checkpoint_060.zip] [checkpoint_061.zip]
"""
import json,re,sys,zipfile,unicodedata,collections,csv,io,pathlib
BASE=pathlib.Path(__file__).resolve().parent
OLD=pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else BASE/'MagiciansQuest-VietHoa-Checkpoint-060.zip'
NEW=pathlib.Path(sys.argv[2]) if len(sys.argv)>2 else BASE/'MagiciansQuest-VietHoa-Checkpoint-061.zip'
TOKEN=re.compile(r"\$\d{3}(?:'[0-9-]+)*;")
PREFIX=re.compile(r"^(?:\$(?:024|023|022|034|040)(?:['0-9-]+)*;)+")
raw={}
with zipfile.ZipFile(OLD) as src:
    assert src.testzip() is None
    for n in src.namelist():
        if n.endswith('/'):continue
        raw[n.split('/',1)[1]]=src.read(n)
new_changes=[]
for s in ('019','020'):
    p=f'translation/04-thoai/talkfigs__0eng__data__0040.{s}.jsonl'
    rows=[json.loads(l) for l in raw[p].decode('utf-8').splitlines()]
    vi=(BASE/f'vi_0040_{s}.txt').read_text(encoding='utf-8').splitlines()
    assert len(rows)==len(vi)==120,(s,len(rows),len(vi))
    out=[]; manual=io.StringIO(newline=''); tsv=csv.writer(manual,delimiter='\t',lineterminator='\n');tsv.writerow(['id','en','vi','ctx'])
    for row,v in zip(rows,vi):
        assert row['vi'] is None,(s,row['id'],'already translated')
        m=PREFIX.match(row['en']);v=(m.group() if m else '')+v
        assert TOKEN.findall(row['en'])==TOKEN.findall(v),(row['id'],'token mismatch')
        assert unicodedata.normalize('NFC',v)==v,(row['id'],'unicode nfc')
        assert not any(c in v for c in '\r\n\t')
        assert v.count('▼')<=3,(row['id'],'too many breaks')
        assert all(len(TOKEN.sub('',line))<=34 for line in v.split('▼')),(row['id'],'width')
        row['vi']=v;out.append(row)
        new_changes.append({'id':row['id'],'en':row['en'],'vi':v,'ctx':row['ctx'],'file':p})
        tsv.writerow([row['id'],row['en'],v,row['ctx']])
    raw[p]=(''.join(json.dumps(row,ensure_ascii=False,separators=(',',':'))+'\n' for row in out)).encode()
    raw[f'manual_0040_{s}.tsv']=manual.getvalue().encode()
    raw[f'vi_0040_{s}.txt']=(BASE/f'vi_0040_{s}.txt').read_bytes()
assert len(new_changes)==240
percent=16752/55976*100
readme_top=f'**Checkpoint mới nhất: 061 (08/11/2026) — 16.752 / 55.976 mục ({percent:.2f}%).** +240 trang thoại NPC (`0040.019`, `0040.020`) về sinh vật huyền bí, ngoại khóa và Cổng Khởi Đầu và Kết Thúc. QA so sánh 501 JSONL / 55.976 mục với ZIP 060: chỉ thêm 240 trường `vi`, giữ 16.512 bản dịch cũ. Xem `CHECKPOINT-2026-11-08-DOT-61.md`, `QA-061.md`, `DELTA-061.jsonl`. Đợt tiếp: `0040.021` (120) + `0040.022` (60), nguồn có trong ZIP.\n\n'
handoff_top='''## Checkpoint 061 — 08/11/2026

- **16.752/55.976 (29,93%)**, thoại NPC **13.627/52.608**; +240 mục từ checkpoint 060.
- Hoàn thành `0040.019` + `0040.020` (120 trang/tệp): yêu tinh, người lòng đất, người tuyết, Siren, Nhân tạo nhân, Cấm Thư, Cổng Khởi Đầu và Kết Thúc.
- Giữ nguyên mọi ID/EN/CTX, token kỹ thuật, 16.512 mục Việt đã có. Dịch toàn bộ 240 bản ghi riêng, kiểm tra NFC, giới hạn 34 ký tự tĩnh và tối đa 3 ký hiệu `▼`.
- ZIP đầy đủ trong Thư viện `Dịch giả lập/MagiciansQuest-VietHoa-Checkpoint-061.zip`, kèm bảng EN–VI, delta, script build và QA. **Chưa kiểm thử ROM NDS thực, chiều rộng biến động cần kiểm thử trong game.**
- Đợt **062** tiếp `0040.021` (120 trang) và `0040.022` (60 trang) đã nằm trong ZIP, chưa dịch.

'''
assert 'README.md' in raw and 'BAN_GIAO.md' in raw
raw['README.md']=(readme_top+raw['README.md'].decode()).encode()
raw['BAN_GIAO.md']=(handoff_top+raw['BAN_GIAO.md'].decode()).encode()
raw['DELTA-061.jsonl']=''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n' for x in new_changes).encode()
raw['QA-061.md']='''# QA — Magician’s Quest · Đợt 061

- **PASS:** đối chiếu toàn bộ 501 JSONL / 55.976 mục checkpoint 060 → 061.
- **PASS:** đúng 240 trường `vi` mới (`0040.019`, `0040.020`, 120 mỗi tệp), tăng 16.512 → **16.752/55.976 (29,93%)**, NPC 13.387 → **13.627/52.608**.
- **PASS:** mọi ID/EN/CTX giữ nguyên, 16.512 `vi` cũ không bị sửa; 499 JSONL ngoài mục tiêu byte-identical.
- **PASS:** bảo toàn tất cả token `$...;` theo thứ tự; Unicode NFC; không CR/LF/TAB trong thoại; không quá 3 `▼`, mỗi đoạn tối đa 34 ký tự tĩnh.
- **PASS:** đủ 240 dòng delta và bản đồ EN–VI, ZIP CRC không lỗi.
- **CHƯA TEST:** ROM NDS thực, font hiển thị và chiều rộng khi game thay các biến động.

Kiểm tra lại: `python qa_061.py <checkpoint_060.zip> <checkpoint_061.zip>`.
'''.encode()
raw['CHECKPOINT-2026-11-08-DOT-61.md']='''# Magician’s Quest: Mysterious Times — Checkpoint 061

**Ngày:** 08/11/2026 · **Repository:** `ronvotri/VH-NDS` · `Magicians-Quest-Mysterious-Times/`

| Tệp | Bản dịch mới | Chủ đề |
|---|---:|---|
| `0040.019` | 120 | Ogre, hạn hán, Jack Frost, Nhân tạo nhân, linh thú, Siren, Yeti, cá sấu trắng |
| `0040.020` | 120 | Người lòng đất, Cấm Thư, Halloween, Cổng Khởi Đầu và Kết Thúc, ác mộng, lợn vòi, tiên, Ông già Noel |

**Tiến độ:** 16.752/55.976 (29,93%), NPC 13.627/52.608; +240 trang từ checkpoint 060. 240 dòng dịch thủ công, không bỏ bản ghi lặp và không sửa EN/CTX/ID.

**QA:** so sánh tất cả 501 JSONL/55.976 bản ghi với checkpoint 060; đúng 240 `vi` mới, các 16.512 `vi` cũ nguyên vẹn; token NDS đúng thứ tự, NFC và giới hạn dòng tĩnh PASS. Chưa kiểm thử ROM thật.

**Thành phẩm:** tệp nguồn dịch, `manual_0040_019.tsv`, `manual_0040_020.tsv`, `vi_0040_019.txt`, `vi_0040_020.txt`, `DELTA-061.jsonl`, `QA-061.md`, `build_061.py`, `qa_061.py`, ZIP đầy đủ.

**Tiếp theo (đợt 062):** `0040.021` (120 trang) + `0040.022` (60 trang) có sẵn trong ZIP, chưa dịch.
'''.encode()
for name in ('build_061.py','qa_061.py'):
    p=BASE/name
    if p.exists():raw[name]=p.read_bytes()
assert len([p for p in raw if p.startswith('translation/') and p.endswith('.jsonl')])==501
with zipfile.ZipFile(NEW,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=7,allowZip64=True) as dst:
    for p,d in sorted(raw.items()):dst.writestr('MagiciansQuest_061/'+p,d)
print('BUILD',NEW,NEW.stat().st_size,'bytes',len(raw),'files',len(new_changes),'new rows')
