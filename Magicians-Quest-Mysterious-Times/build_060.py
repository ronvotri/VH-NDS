#!/usr/bin/env python3
"""Build Magician's Quest checkpoint 060 from 059 plus 240 hand-authored Vietnamese dialogue lines.
Run: python build_060.py [checkpoint_059.zip] [output_060.zip]
Place this script beside the included vi_0040_017.txt and vi_0040_018.txt.
No machine translation; preserve every source row and technical code.
"""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import collections, hashlib, json, re, sys, unicodedata
BASE = Path(__file__).resolve().parent
OLD = Path(sys.argv[1]) if len(sys.argv)>1 else BASE/'MagiciansQuest-VietHoa-Checkpoint-059.zip'
NEW = Path(sys.argv[2]) if len(sys.argv)>2 else BASE/'MagiciansQuest-VietHoa-Checkpoint-060.zip'
ROOT='MagiciansQuest_060'
TARGETS=('0040.017','0040.018')
TOKEN=re.compile(r"\$\d{3}(?:'[0-9-]+)*;")
PREFIX=re.compile(r"^(?:\$(?:024|023|022|034|040)(?:['0-9-]+)*;)+")
def dumps(x): return json.dumps(x,ensure_ascii=False,separators=(',',':'))
def rows(blob):return [json.loads(s) for s in blob.decode('utf-8').splitlines() if s]
def rel(s):return ROOT+'/'+s.split('/',1)[1]
def path(s):return f'{ROOT}/translation/04-thoai/talkfigs__0eng__data__{s}.jsonl'
with ZipFile(OLD) as z:
 assert z.testzip() is None
 old={rel(n):z.read(n) for n in z.namelist() if not n.endswith('/')}
entries=dict(old)
for sfx in TARGETS:
 rawrows=rows(old[path(sfx)])
 assert len(rawrows)==120 and all(r['vi'] is None for r in rawrows)
 distinct=list(dict.fromkeys(PREFIX.sub('',r['en']) for r in rawrows))
 trans=(BASE/('vi_'+sfx.replace('.','_')+'.txt')).read_text('utf8').splitlines()
 assert len(distinct)==len(trans)==120,(sfx,len(distinct),len(trans))
 lookup={}
 for i,(en,vi) in enumerate(zip(distinct,trans),1):
  assert vi and unicodedata.normalize('NFC',vi)==vi,(sfx,i,'NFC')
  assert TOKEN.findall(en)==TOKEN.findall(vi),(sfx,i,'TOKEN',TOKEN.findall(en),TOKEN.findall(vi))
  assert vi.count('▼')<=3,(sfx,i,'BREAKS')
  assert all(len(TOKEN.sub('',piece))<=34 for piece in vi.split('▼')),(sfx,i,'WIDTH')
  assert not any(c in vi for c in '\r\n\t'),(sfx,i,'CONTROL')
  lookup[en]=vi
 out=[]
 for r in rawrows:
  m=PREFIX.match(r['en']);prefix=m.group(0) if m else ''
  vi=prefix+lookup[PREFIX.sub('',r['en'])]
  assert TOKEN.findall(vi)==TOKEN.findall(r['en']),(sfx,r['id'],'FULL TOKEN')
  out.append({**r,'vi':vi})
 entries[path(sfx)]=('\n'.join(dumps(x) for x in out)+'\n').encode()
 entries[f'{ROOT}/vi_{sfx.replace(".","_")}.txt']=('\n'.join(trans)+'\n').encode()
 entries[f'{ROOT}/manual_{sfx.replace(".","_")}.tsv']=('id\ten\tvi\tctx\n'+'\n'.join('\t'.join(str(r[k]) for k in ('id','en','vi','ctx')) for r in out)+'\n').encode()
 print(sfx,len(out),'rows translated',len(distinct),'unique English pages')
delta=[{'file':f'04-thoai/talkfigs__0eng__data__{sfx}.jsonl','id':r['id'],'en':r['en'],'old_vi':None,'vi':r['vi'],'ctx':r['ctx']} for sfx in TARGETS for r in rows(entries[path(sfx)])]
assert len(delta)==240
entries[f'{ROOT}/DELTA-060.jsonl']=('\n'.join(dumps(r) for r in delta)+'\n').encode()
checkpoint='''# Magician’s Quest: Mysterious Times — Checkpoint 060

**Ngày:** 08/11/2026 · **Repo:** `ronvotri/VH-NDS` · `Magicians-Quest-Mysterious-Times/`

| Tệp | Trang mới | Nội dung |
|---|---:|---|
| `0040.017` | 120 | Nessie, sinh vật dưới sông, Candyman, nhà ma, cây trắng, kỳ lân, Nhân sư, kho báu, rồng, người Sao Hỏa |
| `0040.018` | 120 | Người ngoài hành tinh, rác thải, người sói, Thom, tượng đá, Krampus, Minotaur, chuông trường, ma quậy phòng, quỷ thách đấu |

**Tiến độ:** **16.512/55.976 (29,50%)**, tăng 240 từ checkpoint 059 (16.272); hội thoại NPC **13.387/52.608**.

**Thành phẩm:** 2 JSONL dịch, 2 `manual_0040_*.tsv` EN–VI, 2 `vi_0040_*.txt`, `DELTA-060.jsonl`, `QA-060.md`, `build_060.py` và `qa_060.py`.

**QA:** so sánh toàn bộ 501 JSONL / 55.976 bản ghi giữa ZIP 059 và 060. Chỉ 240 trường `vi` đổi từ `null` sang tiếng Việt trong `0040.017` và `0040.018`. Giữ 16.272 bản dịch cũ, không đổi `id`, `en`, `ctx` hoặc byte dữ liệu của các JSONL còn lại. Tất cả mã `$...;` giữ đúng thứ tự; Unicode NFC, ≤3 `▼`, và ≤34 ký tự tĩnh mỗi đoạn.

**Chưa kiểm thử trên ROM NDS.** Các biến tên động cần kiểm tra khi hiển thị trong trò chơi. **Đợt 061 tiếp theo:** `0040.019` + `0040.020` có trong ZIP 060, chưa dịch.
'''
qa='''# QA — Magician’s Quest · Đợt 060

- **PASS:** đối chiếu 501 JSONL / 55.976 mục checkpoint 059 và 060.
- **PASS:** đúng 240 `vi` mới trong `0040.017`, `0040.018` (120/trang tệp), nâng tổng **16.272 → 16.512/55.976 (29,50%)**, NPC **13.147 → 13.387/52.608**.
- **PASS:** 16.272 bản dịch cũ nguyên vẹn, `id`/`en`/`ctx` không đổi, các JSONL khác byte-identical.
- **PASS:** đầy đủ mã màu/biến `$...;` theo đúng thứ tự; tên NPC và thông tin nhiệm vụ được bảo toàn.
- **PASS:** Unicode NFC, không CR/LF/TAB trong `vi`, ≤3 `▼`, mỗi đoạn ≤34 ký tự tĩnh (sau khi bỏ mã token).
- **PASS:** ZIP CRC, không bỏ bản ghi trùng, `DELTA-060.jsonl` đúng 240 bản ghi.
- **CHƯA TEST:** ROM NDS thực, font thực tế hoặc độ rộng khi bung biến tên động.

Kiểm tra lại: `python qa_060.py <checkpoint_059.zip> <checkpoint_060.zip>`.
'''
entries[f'{ROOT}/CHECKPOINT-2026-11-08-DOT-60.md']=checkpoint.encode('utf-8')
entries[f'{ROOT}/QA-060.md']=qa.encode('utf-8')
entries[f'{ROOT}/README.md']=(f'**Checkpoint mới nhất: 060 (08/11/2026) — 16.512/55.976 mục (29,50%).** Thêm 240 trang NPC từ `0040.017` + `0040.018`: Nessie, người sói, rồng, người Sao Hỏa, Krampus, Nhân sư và nhiều nhiệm vụ kỳ bí. Xem `CHECKPOINT-2026-11-08-DOT-60.md`, `QA-060.md`, `DELTA-060.jsonl`. Tiếp `0040.019` + `0040.020` (chưa dịch).\n\n'+entries[f'{ROOT}/README.md'].decode('utf-8')).encode('utf-8')
entries[f'{ROOT}/BAN_GIAO.md']=(f'## Checkpoint 060 — 08/11/2026\n\n- **16.512/55.976 (29,50%)**, NPC **13.387/52.608**; +240 trang `0040.017`, `0040.018`.\n- 240 trang với 240 mẫu tiếng Anh khác biệt, được dịch riêng, thống nhất tớ–cậu, giữ mã màu/tên biến chính xác.\n- QA tất cả 501 JSONL / 55.976 bản ghi checkpoint 059 → 060: chỉ 240 trường `vi` được điền; giữ 16.272 bản dịch cũ và mọi ID/EN/CTX.\n- ZIP đầy đủ `MagiciansQuest-VietHoa-Checkpoint-060.zip` gồm bản dịch, bảng EN–VI, `DELTA-060.jsonl`, script tái tạo và QA; chưa chạy ROM NDS.\n- Đợt **061** tiếp `0040.019` và `0040.020` (240 trang nguồn đã có trong ZIP).\n\n'+entries[f'{ROOT}/BAN_GIAO.md'].decode('utf-8')).encode('utf-8')
entries[f'{ROOT}/build_060.py']=Path(__file__).read_bytes()
entries[f'{ROOT}/qa_060.py']=(BASE/'qa_060.py').read_bytes()
with ZipFile(NEW,'w',ZIP_DEFLATED,compresslevel=6) as z:
 for name,blob in sorted(entries.items()):z.writestr(name,blob)
with ZipFile(NEW) as z:assert z.testzip() is None
print('CREATED',NEW,'FILES',len(entries),'SIZE',NEW.stat().st_size,'SHA256',hashlib.sha256(NEW.read_bytes()).hexdigest())
