#!/usr/bin/env python3
"""Create delta, checkpoint documentation, and progress summary for batch 054."""
from pathlib import Path
from zipfile import ZipFile
import json
ROOT=Path(__file__).resolve().parent
OLD=Path('/mnt/data/MagiciansQuest-VietHoa-Checkpoint-053.zip')
SUFFIXES=('0040.005','0040.006')
with ZipFile(OLD) as z:
    prev={k.split('/translation/',1)[1]:[json.loads(s) for s in z.read(k).decode('utf8').splitlines() if s.strip()] for k in z.namelist() if '/translation/' in k and k.endswith('.jsonl')}
changed=[]
for suffix in SUFFIXES:
    rel=f'04-thoai/talkfigs__0eng__data__{suffix}.jsonl'
    now=[json.loads(line) for line in (ROOT/'translation'/rel).read_text(encoding='utf8').splitlines()]
    for a,b in zip(prev[rel],now):
        if a.get('vi')!=b['vi']:
            changed.append({'file':rel,'id':b['id'],'en':b['en'],'old_vi':a.get('vi'),'vi':b['vi'],'ctx':b['ctx']})
assert len(changed)==240
(ROOT/'DELTA-054.jsonl').write_text('\n'.join(json.dumps(item,ensure_ascii=False,separators=(',',':')) for item in changed)+'\n',encoding='utf8')
q='''# QA — Magician’s Quest · Đợt 054

- **PASS:** so sánh từng bản ghi của 501 JSONL / 55.976 mục với ZIP checkpoint 053.
- **+240 trang:** `0040.005` (120) và `0040.006` (120). Tổng **14.832 → 15.072/55.976 (26,93%)**; thoại NPC **11.707 → 11.947/52.608**.
- **PASS:** chỉ đổi trường `vi` của 240 bản ghi đích. Tất cả tệp JSONL ngoài hai tệp này byte-identical với checkpoint 053; 14.832 bản dịch cũ không đổi.
- **PASS:** bảo toàn mã `$...;` theo thứ tự và giá trị, kể cả `$530'0;`, `$530'1;`, `$531;`, `$532;` (thành phần tin đồn động), mã biểu cảm `$024;`/`$023;`/`$022;`, mã lựa chọn `$019;` và kết thúc `$079;`/`$073;`.
- **PASS:** chuẩn Unicode NFC; không tab/CR/LF trong `vi`; tối đa ba dấu `▼`, độ rộng văn bản hiển thị mỗi đoạn không quá 34 ký tự; giới hạn UTF-8 nếu có khai báo.
- **Lưu ý:** các thành phần biến động chưa xác nhận chiều dài sau thay giá trị thực trong game. Chưa chạy ROM NDS và chưa đo độ rộng pixel của glyph trong giả lập.

Chạy lại: `python qa_054.py /mnt/data/MagiciansQuest-VietHoa-Checkpoint-053.zip`.
'''
(ROOT/'QA-054.md').write_text(q,encoding='utf8')
c='''# Magician’s Quest: Mysterious Times — Checkpoint 054

**Ngày:** 08/11/2026  
**Repository:** `ronvotri/VH-NDS`, `Magicians-Quest-Mysterious-Times/`  
**Mốc trước:** checkpoint 053 — **14.832/55.976 (26,50%)**  
**Mốc mới:** **15.072/55.976 (26,93%)**, +240 trang; NPC **11.947/52.608**.

## Nội dung Việt hóa

| Tệp | Số trang | Nội dung |
|---|---:|---|
| `translation/04-thoai/talkfigs__0eng__data__0040.005.jsonl` | 120 | Chia tay người yêu nhưng giữ tình bạn; giao diện nói chuyện, quà tặng, đi chơi và đi học; nhận xét tình cảm và sinh hoạt giữa các NPC |
| `translation/04-thoai/talkfigs__0eng__data__0040.006.jsonl` | 120 | Các biến thể tin đồn có tên NPC động: bạn bè đi chơi, niệm chú, câu cá, âm nhạc, nhặt rác, nghịch ngợm, hẹn hò và quà tặng |
| **Tổng** | **240** | Giữ kiểu xưng hô tớ–cậu; nhân vật có nét tự phụ về vẻ lịch lãm, nhưng vẫn dễ thương |

## Tệp bàn giao

- `vi_0040_005_raw.txt`, `vi_0040_006_raw.txt`: bản dịch đã biên tập. Mã `¤` được dùng làm chỗ trống cho token động rồi được lắp lại theo đúng thứ tự xuất hiện từ tiếng Anh.
- `build_raw_054.py` chứa 53 và 45 mẫu câu được soạn và nhân vào **đúng từng bản ghi** tương ứng; không gộp hoặc xóa trang trùng. `apply_054.py` ghép lại token, chia dòng giao diện và điền `vi`.
- `vi_0040_005.txt`, `vi_0040_006.txt`: chuỗi cuối đầy đủ mã NDS; `manual_0040_005.tsv` và `manual_0040_006.tsv`: bảng ID/EN/VI/CTX.
- `DELTA-054.jsonl` chỉ gồm 240 thay đổi; `qa_054.py` và `QA-054.md` chứa kiểm định so với bản 053.
- **QA PASS:** 501 JSONL / 55.976 bản ghi, trường dữ liệu khác không đổi; mã điều khiển đúng, Unicode và giới hạn dòng đạt.
- Nguồn **đợt 055**: `0040.007` và `0040.008` (120 + 120) vẫn chưa dịch; có trong ZIP và được chuẩn bị lên GitHub.

**Giới hạn kiểm thử:** chưa chạy game trên ROM NDS; chưa kiểm chiều rộng thực khi tên NPC động được thay vào đoạn tin đồn. ZIP không chứa ROM thương mại.
'''
(ROOT/'CHECKPOINT-2026-11-08-DOT-54.md').write_text(c,encoding='utf8')
for filename,entry in [
    ('README.md','**Checkpoint mới nhất: 054 (08/11/2026) — 15.072 / 55.976 mục (26,93%).** Đợt 054 thêm 240 trang thoại NPC (`0040.005`, `0040.006`): chia tay giữ tình bạn, lời mời tặng quà/đi chơi và tin đồn động về tình cảm, phép thuật, câu cá, nhặt rác. Xem `CHECKPOINT-2026-11-08-DOT-54.md`, `QA-054.md`, `DELTA-054.jsonl`. **Nguồn đợt 055:** `0040.007` và `0040.008` (120 + 120 trang).\n\n'),
    ('BAN_GIAO.md','## Checkpoint 054 — 08/11/2026\n\n- Tổng: **15.072/55.976 mục (26,93%)**; thoại NPC **11.947/52.608**, tăng 240 mục so với 053.\n- Hoàn thành `0040.005` và `0040.006`, mỗi tệp 120 trang. Các câu lặp vẫn giữ đủ bản ghi theo thứ tự; bản dịch dùng ngôi tớ–cậu và sắc thái lịch lãm/tự phụ của NPC.\n- Biến tin đồn `$530\'0;`, `$530\'1;`, `$531;`, `$532;` được bảo toàn theo thứ tự từ bản tiếng Anh. Chưa kiểm độ rộng sau khi game thay các giá trị dài.\n- `vi_0040_005_raw.txt`, `vi_0040_006_raw.txt`, `build_raw_054.py`, `apply_054.py`, các bảng `manual_*`, `DELTA-054.jsonl`, `QA-054.md`, `qa_054.py`, `CHECKPOINT-2026-11-08-DOT-54.md`.\n- QA PASS đối chiếu 501 JSONL / 55.976 mục với checkpoint 053; chỉ thêm 240 `vi`. Chưa thử trên ROM NDS.\n- Tiếp theo: `0040.007` + `0040.008` (240 trang); hai tệp nguồn đã có trong ZIP.\n\n')]:
    path=ROOT/filename
    src=path.read_text(encoding='utf8')
    path.write_text(entry+src,encoding='utf8')
print('Updated 054 delta, QA, checkpoint docs, README and handoff')