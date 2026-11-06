# Magician’s Quest: Mysterious Times — Checkpoint 026

**Ngày:** 07/11/2026  
**Repository:** `ronvotri/VH-NDS`, thư mục `Magicians-Quest-Mysterious-Times/`  
**Baseline:** `MagiciansQuest-VietHoa-Checkpoint-025.zip` (8.308 mục)  
**Mốc mới:** **8.528/55.976 mục (15,24%)**, thêm **220 trang thoại NPC**.

## Tiến độ

| Nhóm | Đã dịch | Tổng | Mới |
|---|---:|---:|---:|
| 00 — Mở đầu | 106 | 106 | 0 |
| 01 — Hệ thống | 1.086 | 1.087 | 0 |
| 02 — Vật phẩm | 1.501 | 1.501 | 0 |
| 03 — Sổ tay | 432 | 432 | 0 |
| 04 — Hội thoại | 5.403 | 52.608 | +220 |
| 05 — Credit | 0 | 242 | 0 |
| **Tổng** | **8.528** | **55.976** | **+220** |

## Nội dung đợt 026

- `translation/04-thoai/talkfigs__0eng__data__0026.005.jsonl`: **100 trang**, lời mời trò chuyện, lịch hẹn Điểm Hẹn Hò, kết bạn đặc biệt, kể chuyện về `$515;`.
- `translation/04-thoai/talkfigs__0eng__data__0027.001.jsonl`: **120 trang**, NPC nữ kể chuyện đeo cà vạt, nấu ăn, mua sắm, picnic Rừng Nấm, chăm sóc nhà cửa, bạn bè và trường lớp.
- Bản dịch tay `vi_0026_005.txt`, `vi_0027_001.txt`; đối chiếu ID/source/vi trong `manual_0026_005.tsv` và `manual_0027_001.tsv`.
- Script áp dụng `apply_026.py`, QA `qa_026.py`, thay đổi `DELTA-026.jsonl` (**220 bản ghi**), báo cáo `QA-026.md`.
- Đã chuẩn hóa tên địa điểm **Điểm Hẹn Hò** và giữ biến `$500;`, `$515;`, `$503'309;`, `$503'310;` cùng mã màu và mã chọn nhánh đúng thứ tự.

## Kết quả QA

- PASS: **501 JSONL và 55.976 bản ghi** đối chiếu trực tiếp với checkpoint 025.
- Đúng **220 mục `vi` mới**; các trường nguồn, ID, ctx và 8.308 bản dịch cũ không thay đổi.
- Mã điều khiển đồng nhất; chuẩn Unicode NFC; không CR/LF/tab trong `vi`, tối đa 3 `▼` và 34 ký tự/dòng không tính mã lệnh. Giữ byte budget nếu có.
- ZIP đầy đủ dữ liệu các đợt, không chứa ROM thương mại.
- **Chưa kiểm thử trong ROM NDS / độ rộng pixel thực tế**. Đây là QA cấu trúc và độ dài văn bản.

## Tiếp theo — đợt 027

- `0027.002` — 120 trang chưa dịch.
- `0027.003` — 120 trang chưa dịch.
- Tổng 240 trang; giữ xưng hô và mã điều khiển, cập nhật GitHub sau khi QA.