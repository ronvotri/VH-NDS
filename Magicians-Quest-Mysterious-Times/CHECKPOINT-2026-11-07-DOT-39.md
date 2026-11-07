# Magician’s Quest: Mysterious Times — Checkpoint 039

**Ngày:** 07/11/2026  
**Repository:** `ronvotri/VH-NDS`, thư mục `Magicians-Quest-Mysterious-Times/`  
**Baseline:** `MagiciansQuest-VietHoa-Checkpoint-038.zip` (11.269 mục đã dịch)  
**Mốc mới:** **11.509 / 55.976 mục (20,56%)**, +240 trang thoại.

## Tiến độ

| Nhóm | Đã dịch | Tổng | Mới |
|---|---:|---:|---:|
| 00 — Mở đầu | 106 | 106 | 0 |
| 01 — Hệ thống | 1.086 | 1.087 | 0 |
| 02 — Vật phẩm | 1.501 | 1.501 | 0 |
| 03 — Sổ tay | 432 | 432 | 0 |
| 04 — Hội thoại NPC | 8.384 | 52.608 | +240 |
| 05 — Credit | 0 | 242 | 0 |
| **Tổng** | **11.509** | **55.976** | **+240** |

## Nội dung dịch đợt 039

- `translation/04-thoai/talkfigs__0eng__data__0032.001.jsonl` — **120 mục**: hướng dẫn và đánh giá tiệc trà mùa xuân, nhà kính/quảng trường, lòng hiếu khách; hội thi thử gan mùa hè tại Nhà Ma (19:00–03:00, dùng phép xì hơi), dẫn nhập hội thi lẩu nấm.
- `translation/04-thoai/talkfigs__0eng__data__0032.002.jsonl` — **120 mục**: thi lẩu nấm tại Rừng Nấm, cảnh báo nấm độc, chấm thành tích; lễ hội tuyết cầu vồng và nghi thức pha lê bảy màu, tập quan sát sự chuyển mùa.
- Ngôi xưng cho người tổ chức lớn tuổi: **ta–các em**; mô tả sự kiện chính xác, lời thoại dí dỏm giữ chừng mực.
- `vi_0032_001_source.txt`, `vi_0032_002_source.txt` — bản dịch thủ công; `vi_0032_001_raw.txt`, `vi_0032_002_raw.txt` — bản chưa tự ghép mã; `vi_0032_001.txt`, `vi_0032_002.txt` — bản cuối.
- `manual_0032_001.tsv`, `manual_0032_002.tsv` — đối chiếu song ngữ EN/VI; `apply_039.py`, `qa_039.py`, `DELTA-039.jsonl`, `QA-039.md`.

## QA

- **PASS:** đối chiếu toàn bộ 501 JSONL / 55.976 bản ghi với checkpoint 038, chỉ thêm 240 trường `vi` ở hai tệp đích.
- Giữ nguyên 11.269 bản dịch cũ, các trường kỹ thuật, ID, EN, context, token và mã lựa chọn.
- Giới hạn tĩnh: Unicode NFC, ≤3 dấu `▼`, ≤34 ký tự hiển thị/dòng (chưa tính ký tự do biến trong game thay).
- **Chưa thử ROM thật** hoặc xác nhận độ rộng pixel/nhánh rẽ in-game.

## Đợt 040 tiếp theo

- `0032.003` — 120 trang chưa dịch.
- `0032.004` — 120 trang chưa dịch.
- Tổng **240 trang**; hai tệp nguồn cũng được đưa lên GitHub để hỗ trợ nối tiếp mà không phải tìm ZIP.