# Jump Ultimate Stars (Japan) — Checkpoint 038

**Tiến độ: 24.297 / 34.919 (69,58%)** — mới dịch **701 ID**, còn **10.622 ID**.

## Checkpoint mới nhất — 038 (2026-11-19)

- Nguồn: ZIP bàn giao `JumpUltimateStars_Japan_BanGiao_Cloud.zip`, trực tiếp tệp `translation/06-jquiz-005.jsonl`.
- Đã đối chiếu chính xác 4 ID đầu của file với checkpoint 037; dịch mới **row_index 4–704** (**701 ID**).
- Nội dung: câu đố ban biên tập Weekly Shonen Jump và *Kochikame*; kết thúc toàn bộ câu hỏi 1489 (robot của Kanbei Ryotsu).
- **Bắt đầu checkpoint 039 từ row_index 705 của `06-jquiz-005.jsonl`.**
- [BAN_DICH_038.jsonl](BAN_DICH_038.jsonl) — delta 701 chuỗi Nhật/Việt, với ID và `quiz_context` giữ nguyên.
- [QA_038.json](QA_038.json) — QA đối chiếu tất cả 34.919 ID nguồn, SHA-256 và các dòng cần kiểm tra.
- [BAN_GIAO_038.md](BAN_GIAO_038.md) — tình trạng tiếp nối và giới hạn thử nghiệm.
- QA tĩnh: **701/701** mục không trống/không trùng, đúng thứ tự và vị trí đáp án J-Quiz theo `reference/quiz-questions.jsonl`; không có dòng `vi` dài trên 37 ký tự Unicode. Chưa đo độ rộng pixel hoặc kiểm thử ROM.
- Nguồn có ký tự bất thường ở các dòng 236, 440, 441, 593; các phương án 499–502 giữ chữ Hán để phân biệt đồng âm. Xem `QA_038.json`.

## Các checkpoint trước và khôi phục

- CP037 hoàn thành **23.596 / 34.919**; `06-jquiz-004.jsonl` dòng 1258–1929 và `06-jquiz-005.jsonl` dòng 0–3.
- Dùng [PHUC_HOI_TONG_HOP_037.md](PHUC_HOI_TONG_HOP_037.md) để khôi phục 001–037, rồi **ghép thêm** `BAN_DICH_038.jsonl` theo ID (từ chối trùng ID) để đủ 24.297 bản dịch.
- Áp overlay [BAN_DINH_CHINH_037B.jsonl](BAN_DINH_CHINH_037B.jsonl) và [BAN_DINH_CHINH_037C.jsonl](BAN_DINH_CHINH_037C.jsonl) bằng cách **ghi đè trường `vi` theo ID**; không nối thêm overlay vào dữ liệu tổng hợp.
- Bảng thuật ngữ có 1.797 mục, kèm `XUNG_HO_NHAN_VAT.md`.

**Chưa có ROM patch hoàn thiện; chưa kiểm thử font Việt, gameplay, hay đáp án đúng.** Không tính nội dung chưa được trích xuất (animation/texture/video) là đã Việt hóa.

Đích: `ronvotri/VH-NDS`, nhánh `vh/jump-ultimate-stars-japan`, thư mục `Jump-Ultimate-Stars-Japan/`.
