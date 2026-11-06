# Magician’s Quest: Mysterious Times — Checkpoint 027

**Ngày:** 07/11/2026  
**Repository:** `ronvotri/VH-NDS`, thư mục `Magicians-Quest-Mysterious-Times/`  
**Baseline:** `MagiciansQuest-VietHoa-Checkpoint-026.zip` (8.528 mục)  
**Mốc mới:** **8.768/55.976 mục (15,66%)**, thêm **240 trang thoại NPC**.

## Tiến độ

| Nhóm | Đã dịch | Tổng | Mới |
|---|---:|---:|---:|
| 00 — Mở đầu | 106 | 106 | 0 |
| 01 — Hệ thống | 1.086 | 1.087 | 0 |
| 02 — Vật phẩm | 1.501 | 1.501 | 0 |
| 03 — Sổ tay | 432 | 432 | 0 |
| 04 — Hội thoại | 5.643 | 52.608 | +240 |
| 05 — Credit | 0 | 242 | 0 |
| **Tổng** | **8.768** | **55.976** | **+240** |

## Nội dung đợt 027

- `translation/04-thoai/talkfigs__0eng__data__0027.002.jsonl`: 120 trang; lời kể NPC nữ về học tập, chuyện yêu, hoa hướng dương, cực quang và trốn tìm.
- `translation/04-thoai/talkfigs__0eng__data__0027.003.jsonl`: 120 trang; Valentine, thời trang, hội chợ, nấu nướng, nghề nghiệp và quan hệ bạn bè.
- Bản dịch tay: `vi_0027_002.txt`, `vi_0027_003.txt`; bảng ID/EN/VI: `manual_0027_002.tsv`, `manual_0027_003.tsv`.
- Công cụ: `apply_027.py` (chèn 240 bản dịch), `qa_027.py` (đối chiếu 501 JSONL với ZIP 026), `DELTA-027.jsonl` (240 thay đổi), `QA-027.md` (báo cáo).
- Bảo toàn thẻ tên NPC `$503'310;`, `$503'307;`, và mã màu `$000'3;Piquard$000'1;` cùng toàn bộ mã biểu cảm.

## Kết quả QA

- PASS: **501 JSONL / 55.976 bản ghi**, so từng bản ghi với checkpoint 026.
- Chỉ bổ sung **240 mục `vi`**; **8.528 bản dịch đã có** và mọi trường nguồn giữ nguyên.
- Mã lệnh giống nguồn theo đúng thứ tự; Unicode NFC; không chèn CR/LF/tab; giới hạn 3 `▼` và tối đa 34 ký tự thấy được/dòng; kiểm tra byte budget nếu có.
- Gói ZIP đầy đủ, không chứa ROM thương mại hoặc patch ROM.
- **Chưa kiểm thử ROM NDS / độ rộng pixel thực tế.** QA chỉ xác nhận cấu trúc và độ dài chuỗi.

## Tiếp theo — đợt 028

- `0027.004` — 120 trang chưa dịch.
- `0027.005` — 81 trang chưa dịch.
- Tổng **201 trang**; giữ giọng NPC, ngôi xưng và mã điều khiển; đồng bộ GitHub sau QA.