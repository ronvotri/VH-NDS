# Magician’s Quest: Mysterious Times — Checkpoint 022

**Ngày:** 07/11/2026  
**Repository:** `ronvotri/VH-NDS`, thư mục `Magicians-Quest-Mysterious-Times/`  
**Baseline:** `MagiciansQuest-VietHoa-Checkpoint-021.zip` (7.385 mục)  
**Mốc mới:** **7.625/55.976 mục (13,62%)**, thêm **240 trang thoại NPC**.

## Tiến độ

| Nhóm | Đã dịch | Tổng | Mới |
|---|---:|---:|---:|
| 00 — Mở đầu | 106 | 106 | 0 |
| 01 — Hệ thống | 1.086 | 1.087 | 0 |
| 02 — Vật phẩm | 1.501 | 1.501 | 0 |
| 03 — Sổ tay | 432 | 432 | 0 |
| 04 — Hội thoại | 4.500 | 52.608 | +240 |
| 05 — Credit | 0 | 242 | 0 |
| **Tổng** | **7.625** | **55.976** | **+240** |

## Đợt 022

- `translation/04-thoai/talkfigs__0eng__data__0025.002.jsonl`: **120 trang**; tâm sự về việc mượn đồ, học hành, tán tỉnh bằng món ngọt, chuyện mùa và đồ ăn. Nhiều mẩu thoại sử dụng cách nói nông thôn trong bản Anh, chuyển thành tiếng Việt xuề xòa, vui vẻ, không dùng phương ngữ quá đặc thù.
- `translation/04-thoai/talkfigs__0eng__data__0025.003.jsonl`: **120 trang**; sưu tầm vật dụng kỳ lạ, ngủ nướng, sở thích, hẹn hò, tình bạn và sinh nhật; giữ các nhánh trả lời.
- Bản dịch gốc do người biên dịch viết: `vi_0025_002.txt`, `vi_0025_003.txt` (120 dòng/tệp). Bảng đối chiếu `manual_0025_002.tsv`, `manual_0025_003.tsv` (ID / EN / VI).
- Script: `apply_022.py`, `qa_022.py`; bản chênh lệch: `DELTA-022.jsonl`, báo cáo `QA-022.md`.

## QA

- PASS — đối chiếu toàn bộ **501 JSONL / 55.976 bản ghi** với checkpoint 021.
- Chính xác **240 mục mới**, chỉ đổi trường `vi`; không sửa ID, tiếng Anh, ngữ cảnh, thứ tự hoặc bản dịch cũ.
- Giữ nguyên thứ tự mã biểu cảm `$024`/`$023`/`$022`, tên nhân vật `$500;`, `$503'...;`, lệnh nhánh `$019'...;`; chuẩn Unicode NFC, không CR/LF/tab, tối đa 34 ký tự không kể mã/đoạn và 3 dấu `▼`.
- Kiểm tra giới hạn byte khai báo. ZIP toàn bộ được giải thử bằng CRC.
- **Chưa có ROM NDS sạch để build/test:** không xác nhận độ rộng glyph pixel, cách ngắt chữ sau khi thay tên dài và UI thật. ZIP chỉ chứa nội dung dịch, công cụ và nhật ký; không chứa ROM thương mại.

## Bước tiếp — đợt 023

- `0025.004`: 120 trang chưa dịch.
- `0025.005`: 83 trang chưa dịch.
- Tiếp tục giữ giọng tự nhiên, tớ–cậu; dịch cả nhánh lựa chọn; ưu tiên QA theo trường `vi` và cập nhật cùng repository.