# Magician’s Quest: Mysterious Times — Checkpoint 023

**Ngày:** 07/11/2026  
**Repository:** `ronvotri/VH-NDS`, thư mục `Magicians-Quest-Mysterious-Times/`  
**Baseline:** `MagiciansQuest-VietHoa-Checkpoint-022.zip` (7.625 mục)  
**Mốc mới:** **7.828/55.976 mục (13,98%)**, thêm **203 trang thoại NPC**.

## Tiến độ

| Nhóm | Đã dịch | Tổng | Mới |
|---|---:|---:|---:|
| 00 — Mở đầu | 106 | 106 | 0 |
| 01 — Hệ thống | 1.086 | 1.087 | 0 |
| 02 — Vật phẩm | 1.501 | 1.501 | 0 |
| 03 — Sổ tay | 432 | 432 | 0 |
| 04 — Hội thoại | 4.703 | 52.608 | +203 |
| 05 — Credit | 0 | 242 | 0 |
| **Tổng** | **7.828** | **55.976** | **+203** |

## Đợt 023

- `translation/04-thoai/talkfigs__0eng__data__0025.004.jsonl`: **120 trang**, kể tiếp chuyện tình bạn, lời rủ đi chơi/uống trà/học nhóm, ngỏ lời hẹn hò và triết lý của NPC mê ăn.
- `translation/04-thoai/talkfigs__0eng__data__0025.005.jsonl`: **83 trang**, kết thúc nhánh hẹn giờ ở Điểm Hẹn Hò (10:00, 12:00, 15:00, 18:00, 20:00), lựa chọn bạn thân và lời đồn của bạn bè.
- Bản dịch thủ công: `vi_0025_004.txt` (120 dòng), `vi_0025_005.txt` (83 dòng). Các tệp `manual_0025_004.tsv`, `manual_0025_005.tsv` lưu đầy đủ ID / tiếng Anh / tiếng Việt.
- Công cụ: `apply_023.py`, `qa_023.py`; thay đổi: `DELTA-023.jsonl`; kiểm tra: `QA-023.md`.

## Kiểm thử

- PASS: đối chiếu **501 JSONL / 55.976 bản ghi** với checkpoint 022.
- Chính xác **203 trường `vi` mới**, giữ nguyên 100% trường gốc và các bản dịch trước.
- Mã màu `$000`, mã nhánh `$019`, biến `$500;`, `$503'307;`, `$515;`, biểu cảm `$024/$023/$022` và mã điều khiển khác: số lượng, giá trị và thứ tự tuyệt đối không đổi.
- Unicode NFC, tối đa ba dấu ngắt `▼`, mỗi dòng ≤34 ký tự hiển thị (không tính mã), giới hạn byte theo khai báo nếu có.
- ZIP checkpoint được kiểm tra CRC toàn bộ, đủ 501 JSONL, không có ROM thương mại.
- **Chưa kiểm thử thực tế trong ROM NDS / đo pixel font tiếng Việt**. Kết quả QA là kiểm tra dữ liệu, chưa phải xác nhận hiển thị cuối cùng.

## Bước tiếp theo — đợt 024

- `0026.001` — 120 trang chưa dịch.
- `0026.002` — 120 trang chưa dịch.
- Tiếp tục tính cách NPC, giọng tớ–cậu; chỉ sửa `vi`, kiểm tra mã điều khiển và cập nhật GitHub sau mỗi lô.