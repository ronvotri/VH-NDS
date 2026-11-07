#!/usr/bin/env python3
"""Write transparent batch 053 change log and handoff docs from validated JSONL."""
from pathlib import Path
import json
from zipfile import ZipFile
root=Path(__file__).resolve().parent
old='/mnt/data/MagiciansQuest-VietHoa-Checkpoint-052.zip'
rel_paths=['04-thoai/talkfigs__0eng__data__0040.003.jsonl','04-thoai/talkfigs__0eng__data__0040.004.jsonl']
changes=[]
with ZipFile(old) as z:
 for rel in rel_paths:
  src=[json.loads(s) for s in z.read('MagiciansQuest_052/translation/'+rel).decode('utf8').splitlines() if s]
  target=[json.loads(s) for s in (root/'translation'/rel).read_text().splitlines() if s]
  assert len(src)==len(target)==120
  for a,b in zip(src,target):
   assert not a['vi'] and b['vi']
   changes.append(dict(file=rel,id=b['id'],en=b['en'],old_vi=a.get('vi'),vi=b['vi'],ctx=b.get('ctx')))
assert len(changes)==240
(root/'DELTA-053.jsonl').write_text('\n'.join(json.dumps(x,ensure_ascii=False,separators=(',',':')) for x in changes)+'\n',encoding='utf8')
(root/'QA-053.md').write_text('''# QA — Magician’s Quest · Đợt 053

- **PASS:** đối chiếu toàn bộ **501 tệp JSONL / 55.976 bản ghi** của checkpoint 052 với checkpoint 053.
- **+240 trang dịch:** `0040.003` (120) và `0040.004` (120). Tổng **14.592 → 14.832 / 55.976 (26,50%)**; thoại NPC **11.467 → 11.707 / 52.608**.
- **PASS:** tất cả dữ liệu `id`, `en`, `ctx` và trường khác giữ nguyên; mọi tệp JSONL không thuộc đích đều byte-identical; 14.592 bản dịch cũ không thay đổi.
- **PASS:** bảo toàn mã `$...;` theo thứ tự và giá trị (kể cả biến tên `$500;`, `$515;`, vật phẩm `$507'84;`, nhánh `$073;`); chuẩn NFC; không chèn tab/CR/LF; tối đa 3 dấu `▼` và 34 ký tự hiển thị mỗi dòng; kiểm tra giới hạn byte nếu khai báo.
- **PASS:** 120/120 trang mỗi tệp có bản dịch. Lời thoại lặp theo nhánh game được giữ cùng bản dịch nhưng không gộp/bỏ record.
- **Chưa kiểm thử trực tiếp trên ROM Nintendo DS**; QA này là kiểm tra cấu trúc và giao diện tĩnh.

Chạy lại: `python qa_053.py /mnt/data/MagiciansQuest-VietHoa-Checkpoint-052.zip`.
''',encoding='utf8')
(root/'CHECKPOINT-2026-11-08-DOT-53.md').write_text('''# Magician’s Quest: Mysterious Times — Checkpoint 053

**Ngày:** 08/11/2026  
**Repository:** `ronvotri/VH-NDS`, thư mục `Magicians-Quest-Mysterious-Times/`  
**Mốc trước:** checkpoint 052 — **14.592/55.976 (26,07%)**  
**Mốc mới:** **14.832/55.976 (26,50%)** — +240 mục; hội thoại NPC **11.707/52.608**.

## Nội dung đợt 053

| Tệp | Số trang | Nội dung |
|---|---:|---|
| `translation/04-thoai/talkfigs__0eng__data__0040.003.jsonl` | 120 | Tâm sự về bạn học `$515;`, chuyện hẹn hò, Điểm Hẹn Hò, những hoạt động bạn bè, sự kiện mùa và thư điện tín xin lỗi |
| `translation/04-thoai/talkfigs__0eng__data__0040.004.jsonl` | 120 | Hoạt động ngoại khóa, chia tay bạn thân để trân trọng tình bạn, chào hỏi và đối thoại kết thúc hẹn hò |
| **Tổng** | **240** | Ngôi xưng bạn bè `tớ–cậu`; tính cách kiêu kỳ nhưng duyên dáng; giữ thoại lặp trong các nhánh |

## Bàn giao và kiểm chứng

- `vi_0040_003_raw.txt`, `vi_0040_004_raw.txt`: 120 dòng dịch có biên tập mỗi tệp; ký hiệu `¤` là vị trí của mã động không thuộc tiền tố biểu cảm.
- `build_raw_053.py` tái tạo những nhóm thoại lặp nguyên bản ở `0040.004`; `apply_053.py` gắn mã game, ngắt dòng và không ghi đè bản dịch không khớp.
- `vi_0040_003.txt`, `vi_0040_004.txt`: kết quả cuối; `manual_0040_003.tsv`, `manual_0040_004.tsv`: bảng đối chiếu ID/EN/VI/CTX.
- `DELTA-053.jsonl`: đúng 240 bản ghi mới; `QA-053.md`, `qa_053.py`: báo cáo và công cụ kiểm tra đối chiếu checkpoint 052.
- QA PASS: **501 JSONL, 55.976 bản ghi**, toàn bộ dữ liệu cũ giữ nguyên; mã điều khiển, Unicode, ngắt dòng và giới hạn byte (nếu có) được xác minh.
- Nguồn đợt **054**: `0040.005` và `0040.006` (120 trang mỗi tệp), có sẵn trong ZIP checkpoint 053 và đưa lên GitHub với trường `vi:null`.

Chưa test chạy ROM NDS; ZIP không chứa ROM thương mại.
''',encoding='utf8')
readme=root/'README.md'
s=readme.read_text(encoding='utf8')
readme.write_text('**Checkpoint mới nhất: 053 (08/11/2026) — 14.832 / 55.976 mục (26,50%).** Đợt 053 thêm **240 trang thoại NPC** (`0040.003`, `0040.004`): tình bạn, Điểm Hẹn Hò, hoạt động mùa, điện tín xin lỗi, buổi ngoại khóa và chia tay bạn thân/người yêu. Xem `CHECKPOINT-2026-11-08-DOT-53.md`, `QA-053.md`, `DELTA-053.jsonl`. **Nguồn đợt 054:** `0040.005` và `0040.006` (120 + 120 trang).\n\n'+s,encoding='utf8')
hand=root/'BAN_GIAO.md'
s=hand.read_text(encoding='utf8')
hand.write_text('''## Mốc mới nhất — Checkpoint 053 (08/11/2026)

- **14.832/55.976 (26,50%)**, +240 mục thoại NPC; **11.707/52.608** trang thoại có bản dịch.
- `0040.003` / `0040.004` mỗi tệp 120 trang: những câu nói chuyện về tình bạn, hẹn hò, lễ hội, ngoại khóa, chia tay; giữ mã tên động `$500;` / `$515;` nguyên thứ tự.
- Nguồn đợt 054 đã có trong `translation/04-thoai/`: `0040.005`, `0040.006` (mỗi tệp 120 dòng, chưa dịch). Mở `CHECKPOINT-2026-11-08-DOT-53.md` và `QA-053.md` để nối tiếp.
- Kiểm tra tĩnh 501 JSONL / 55.976 bản ghi PASS; **chưa chạy thử trên ROM**.

---

'''+s,encoding='utf8')
print('Changes',len(changes),'and documents created')