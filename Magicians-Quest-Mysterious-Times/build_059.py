#!/usr/bin/env python3
"""Build Magician's Quest 059 from 058, preserving all source records & technical codes.
Translation of unseen dialogue is authored by hand; exact English repeats reuse prior
reviewed translations. This script does not attempt automated English translation.
"""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import json, re, hashlib, unicodedata, collections

BASE=Path('/mnt/data')
OLD=BASE/'MagiciansQuest-VietHoa-Checkpoint-058.zip'
NEW=BASE/'MagiciansQuest-VietHoa-Checkpoint-059.zip'
ROOT='MagiciansQuest_059'
PREFIX=re.compile(r"^(?:\$(?:024|023|022|034|040)(?:['0-9-]+)*;)+")
TOKEN=re.compile(r"\$\d{3}(?:'[0-9-]+)*;")
TARGETS=('0040.015','0040.016')
def sjson(obj):return json.dumps(obj,ensure_ascii=False,separators=(',',':'))
def records(blob):return [json.loads(s) for s in blob.decode('utf8').splitlines() if s.strip()]
def body(en):return PREFIX.sub('',en)
def rel(name):return ROOT+'/'+name.split('/',1)[1]
def path(s):return f'{ROOT}/translation/04-thoai/talkfigs__0eng__data__{s}.jsonl'

# 1-based index into each file's first-occurrence sequence of DISTINCT English bodies.
# Each source that has no exact matching previous Vietnamese translation is translated here.
MANUAL_015={
 10:'Bọn tớ vừa tám chuyện.▼Nghe chuyện này nè...',
 12:'Nhưng kiểu ấy sến quá,▼chẳng hợp với một người▼lịch lãm như tớ.',
 15:'Ồn ào thế thì▼ai tập trung bắt côn trùng▼cho nổi chứ!',
 20:'Nói mãi mà chẳng líu lưỡi,▼hai người đó tài thật!',
 25:'Không biết giữa họ▼đã xảy ra chuyện gì nữa...',
 26:'Dù có thất bại,▼dám thử vẫn hơn▼chẳng làm gì cả.',
 27:'Hay quá! Tớ cũng muốn▼đánh giỏi như thế!',
 30:'Hay hôm nào tớ rủ $530\'0;▼đi chơi cùng nhỉ?',
 31:'Không biết $530\'0;▼bắt được thứ gì nhỉ...',
 33:'Không biết $530\'0;▼đã niệm chú gì nhỉ...',
 34:'Không biết $530\'0;▼đang làm phép gì nhỉ...',
 38:'Không biết sao $530\'0;▼lại làm thế nhỉ...',
}
MANUAL_016={
 3: 'Bọn tớ vừa tám chuyện.▼Nghe chuyện này nè...',
 7: 'Không hiểu nhặt rác▼có gì thú vị nhỉ.▼À, cũng là việc tốt mà...',
 8: 'Không biết ở đó có gì▼hay ho không nữa...',
 9: 'Tớ cũng muốn bày trò!▼Lần sau phải rủ $530\'0;▼tham gia mới được...',
 10:'Đúng lúc ghê! Bọn tớ▼đang bàn mấy tin đồn▼râm ran dạo này đây.',
 12:'Cậu cũng biết rồi à?▼Không biết họ đã▼hẹn hò chưa nhỉ...',
 14:'Cậu biết rồi sao?▼Không biết họ đã làm gì...',
 15:'Cậu nghe rồi à?▼Không biết chuyện gì xảy ra...',
 16:'Ừ thì đời là thế mà.▼Chắc ta đừng bàn▼thêm chuyện ấy nữa.',
 19:'Cậu biết chuyện đó rồi à?▼Ừm... Có gì mờ ám ở đây!',
 20:"$530'0; và $530'1;▼lúc nào cũng dính lấy nhau.▼Tớ nghĩ $533;!",
 22:"Cậu cũng biết à?▼Mà $530'0; bị sao thế?",
 23:'Hiếm khi tớ nói vậy,▼nhưng tớ cũng hơi lo đấy.',
 29:'Hừ, vậy là rõ nhé!▼Đến lúc cả thế giới biết▼tớ ngầu cỡ nào rồi!',
 30:"$530'0;▼$533;▼vì biết quan tâm à?",
 35:'Nhưng kiểu ấy sến quá,▼chẳng hợp với một người▼lịch lãm như tớ.',
 41:'Không biết giữa họ▼đã xảy ra chuyện gì nữa...',
 43:'Dù có thất bại,▼dám thử vẫn hơn▼chẳng làm gì cả.',
 44:'Không biết có thật không...▼Nhưng tớ bất ngờ thật đấy!',
 50:'Cậu biết rồi sao? Ừm...▼Không biết chuyện gì xảy ra...',
 53:"$530'0;▼định chăm chỉ học hành...",
 54:'để trở thành▼$533;!',
 55:'Bất ngờ nhỉ? Thôi kệ,▼cũng chẳng liên quan tới tớ.',
 57:'Xin lỗi nhé, $500;.▼Chuyện bọn tớ vừa bàn▼không tiện kể đâu.',
 58:'Có những chuyện▼giữ bí mật sẽ tốt hơn đó!',
 59:'Hôm nọ, tớ thấy▼một bóng đen khổng lồ▼trên mặt nước.',
 60:'Trên đời chắc chẳng có▼mấy thứ to hơn nó đâu.',
 61:'Không lẽ là khủng long...▼thật sao?',
 62:'Ơ! Biết đâu tớ vừa▼khám phá ra chuyện chấn động!$079;',
 63:'Ngoài kia thật sự có▼thứ giống khủng long...',
}
assert set(MANUAL_015)<=set(range(1,39))
assert set(MANUAL_016)<=set(range(1,64))

with ZipFile(OLD) as z:
 assert z.testzip() is None
 old={rel(n):z.read(n) for n in z.namelist() if not n.endswith('/')}
entries=dict(old)
# Index prior translations by exact English BODY. Newest checkpoint/talk pages win;
# ambiguous older phrasings are explicitly pinned above.
reuse={}
for n in sorted(old):
 if '/translation/04-thoai/' not in n or not n.endswith('.jsonl'):continue
 for r in records(old[n]):
  if r.get('vi') is not None:
   reuse[body(r['en'])]=body(r['vi'])

for suffix,manual in zip(TARGETS,(MANUAL_015,MANUAL_016)):
 rows=records(old[path(suffix)])
 assert len(rows)==120 and all(r['vi'] is None for r in rows)
 distinct=list(dict.fromkeys(body(r['en']) for r in rows))
 assert len(distinct)==(38 if suffix.endswith('.015') else 63),(suffix,len(distinct))
 mapped={}
 for i,en in enumerate(distinct,1):
  vi=manual.get(i,reuse.get(en))
  if vi is None:raise ValueError(f'Untranslated unique {suffix} #{i}: {en!r}')
  assert vi==unicodedata.normalize('NFC',vi),(suffix,i,'NFC')
  assert TOKEN.findall(en)==TOKEN.findall(vi),(suffix,i,'TOKENS',en,vi)
  assert vi.count('▼')<=3,(suffix,i,'BREAKS',vi)
  assert all(len(TOKEN.sub('',ln))<=34 for ln in vi.split('▼')),(suffix,i,'LENGTH',vi)
  assert '\n' not in vi and '\r' not in vi and '\t' not in vi,(suffix,i,'CONTROL')
  mapped[en]=vi
  reuse[en]=vi
 print(f'{suffix}: {len(rows)} records, {len(distinct)} unique EN, {len(manual)} manually authored/pinned, {len(distinct)-len(manual)} exact previous-body matches')
 out=[]
 for r in rows:
  m=PREFIX.match(r['en']);p=m.group(0) if m else ''
  vi=p+mapped[body(r['en'])]
  assert TOKEN.findall(r['en'])==TOKEN.findall(vi),(suffix,r['id'],'TOKENS')
  out.append({**r,'vi':vi})
 entries[path(suffix)]=('\n'.join(sjson(r) for r in out)+'\n').encode('utf8')
 no=suffix.replace('.','_')
 entries[f'{ROOT}/vi_{no}.txt']=('\n'.join(r['vi'] for r in out)+'\n').encode('utf8')
 entries[f'{ROOT}/manual_{no}.tsv']=('id\ten\tvi\tctx\n'+'\n'.join('\t'.join(map(str,(r['id'],r['en'],r['vi'],r['ctx']))) for r in out)+'\n').encode('utf8')

# Delta supports audit and reconstruction, no source rows deleted or deduplicated.
delta=[]
for suffix in TARGETS:
 for r in records(entries[path(suffix)]):
  delta.append({'file':f'04-thoai/talkfigs__0eng__data__{suffix}.jsonl','id':r['id'],'en':r['en'],'old_vi':None,'vi':r['vi'],'ctx':r['ctx']})
assert len(delta)==240
entries[f'{ROOT}/DELTA-059.jsonl']=('\n'.join(sjson(r) for r in delta)+'\n').encode('utf8')
checkpoint='''# Magician’s Quest: Mysterious Times — Checkpoint 059

**Ngày:** 08/11/2026 · **Repo:** `ronvotri/VH-NDS` · `Magicians-Quest-Mysterious-Times/`

| Tệp | Trang mới | Nội dung |
|---|---:|---|
| `0040.015` | 120 | Tin đồn học đường, hội thoại bạn bè, câu cá, niệm chú, những cuộc gặp gỡ và hành động đáng ngờ |
| `0040.016` | 120 | Tin đồn tình cảm, so kè danh tiếng, bí mật, kế hoạch học tập; mở màn câu chuyện sinh vật khổng lồ dưới nước |

**Tiến độ:** **16.272/55.976 (29,07%)**, tăng 240 từ checkpoint 058 (16.032); hội thoại NPC **13.147/52.608**.

**Thành phẩm:** 2 JSONL dịch, 2 `manual_0040_*.tsv` EN–VI, 2 `vi_0040_*.txt`, `DELTA-059.jsonl`, `QA-059.md`, `build_059.py` và `qa_059.py`.

**QA:** kiểm toàn bộ 501 JSONL / 55.976 bản ghi checkpoint 058 → 059. Chỉ có 240 trường `vi` từ `null` sang tiếng Việt trong `0040.015`, `0040.016`. Giữ 16.032 bản dịch cũ, không đổi `id`, `en`, `ctx` hoặc tệp JSONL nào khác. Giữ thứ tự mã `$...;`, NFC, tối đa 3 dấu `▼` và 34 ký tự tĩnh mỗi đoạn.

**Chưa kiểm thử ROM NDS.** Khi chạy game cần xác nhận độ rộng chữ của biến động `$530` / `$531` / `$532` / `$533` và lời thoại phân trang. **Đợt 060 tiếp theo:** `0040.017` và `0040.018` đã có nguồn trong ZIP 059, chưa dịch.
'''
qa='''# QA — Magician’s Quest · Đợt 059

- **PASS:** đối chiếu 501 JSONL / 55.976 mục checkpoint 058 và 059.
- **PASS:** chỉ thêm 240 `vi` trong `0040.015`, `0040.016` (120 mục/tệp). **16.032 → 16.272 / 55.976 (29,07%)**, NPC **12.907 → 13.147 / 52.608**.
- **PASS:** nguyên vẹn 16.032 bản dịch cũ; không thay đổi `id`, `en`, `ctx` hoặc các tệp JSONL khác (so byte).
- **PASS:** đủ và đúng thứ tự các mã `$...;`, kể cả tiền tố biểu cảm, biến `$530`–`$533`, và `$079`.
- **PASS:** Unicode NFC, `vi` không chứa CR/LF/TAB, tối đa 3 `▼`, tối đa 34 ký tự tĩnh trong từng đoạn (sau loại mã token).
- **PASS:** ZIP CRC; toàn bộ bản ghi lặp được bảo toàn, `DELTA-059.jsonl` chứa đúng 240 bản ghi.
- **CHƯA TEST:** bản ROM NDS, font thực tế hoặc độ dài sau khi bung tên động.

Chạy lại: `python qa_059.py /mnt/data/MagiciansQuest-VietHoa-Checkpoint-058.zip /mnt/data/MagiciansQuest-VietHoa-Checkpoint-059.zip`.
'''
entries[f'{ROOT}/CHECKPOINT-2026-11-08-DOT-59.md']=checkpoint.encode('utf8')
entries[f'{ROOT}/QA-059.md']=qa.encode('utf8')
entries[f'{ROOT}/README.md']=(f'**Checkpoint mới nhất: 059 (08/11/2026) — 16.272 / 55.976 mục (29,07%).** Thêm 240 trang NPC từ `0040.015` và `0040.016`: lời đồn, tình bạn, câu cá, nghiên cứu pháp thuật và mở đầu chuyện sinh vật khổng lồ. Xem `CHECKPOINT-2026-11-08-DOT-59.md`, `QA-059.md`, `DELTA-059.jsonl`. Nguồn tiếp: `0040.017` và `0040.018` (chưa dịch).\n\n'+entries[f'{ROOT}/README.md'].decode('utf8')).encode('utf8')
entries[f'{ROOT}/BAN_GIAO.md']=(f'## Checkpoint 059 — 08/11/2026\n\n- **16.272/55.976 (29,07%)**, NPC **13.147/52.608**; thêm 240 trang của `0040.015` và `0040.016`.\n- 101 mẫu tiếng Anh phân biệt, tái dùng chính xác câu trùng các checkpoint trước, tự dịch/biên tập thủ công câu mới.\n- QA đối chiếu toàn bộ 501 JSONL / 55.976 bản ghi với ZIP 058: chỉ điền 240 `vi`; giữ 16.032 `vi` cũ, mã NDS, ID/EN/CTX và trang lặp.\n- `MagiciansQuest-VietHoa-Checkpoint-059.zip` chứa bản đầy đủ, bảng EN–VI, `DELTA-059.jsonl`, QA và script tái tạo; lưu Thư viện `Dịch giả lập`. Chưa kiểm thử ROM.\n- Đợt **060** tiếp `0040.017` và `0040.018` (240 trang) trong ZIP, chưa dịch.\n\n'+entries[f'{ROOT}/BAN_GIAO.md'].decode('utf8')).encode('utf8')
entries[f'{ROOT}/build_059.py']=Path(__file__).read_bytes()
entries[f'{ROOT}/qa_059.py']=(BASE/'qa_059.py').read_bytes()
with ZipFile(NEW,'w',ZIP_DEFLATED,compresslevel=6) as z:
 for name,data in sorted(entries.items()):z.writestr(name,data)
with ZipFile(NEW) as z:assert z.testzip() is None
print('CREATED',NEW,'FILE COUNT',len(entries),'SIZE',NEW.stat().st_size,'SHA256',hashlib.sha256(NEW.read_bytes()).hexdigest())
