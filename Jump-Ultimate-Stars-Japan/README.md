# Jump Ultimate Stars (Japan) — Checkpoint 050 🇻🇳

**Tiến độ: 32.746 / 34.919 (93,78%)** — thêm **735 chuỗi Nhật–Việt mới** so với CP049; còn **2.173 chuỗi**.

## Mới nhất — Checkpoint 050 (20/11/2026)

Nguồn Nhật: `JumpUltimateStars_Japan_BanGiao_Cloud.zip` → `translation/06-jquiz-009.jsonl`; SHA256 `ad517ab9020ebaaaf24d3b0be0bca8b6bbd1c9f975f1c3b745f1b249fd23d1e1`.

- `06-jquiz-009.jsonl`: **row_index 616–1350 (735 ID)** — hoàn tất tệp 009 và toàn bộ J-Quiz đến câu hỏi **3005**.
- Theo manga code: *Yu Yu Hakusho* **405 ID**, *Yu-Gi-Oh!* **330 ID**.
- [BAN_DICH_050.jsonl](BAN_DICH_050.jsonl) — 735 chuỗi Nhật–Việt mới, bảo toàn ID, JA và metadata.
- [BAN_DICH_050.tsv](BAN_DICH_050.tsv) — bảng đối chiếu Nhật–Việt.
- [QA_050.json](QA_050.json) — báo cáo nguồn/ID/vị trí quiz/token/SHA256 và các giới hạn chưa kiểm thử.
- [BAN_GIAO_050.md](BAN_GIAO_050.md) — hướng dẫn nối tiếp.
- [BAN_DICH_TONG_HOP_038-050.jsonl](BAN_DICH_TONG_HOP_038-050.jsonl) — **9.150 ID CP038–050**, đã giữ sửa tên Shunrei trong CP046A; không gồm CP001–037.

## Các nguồn còn lại — Checkpoint 051

Xem chi tiết [KIEM_TOAN_CON_LAI_051.md](KIEM_TOAN_CON_LAI_051.md), gồm:

- `07-deck-001.jsonl`: **352 dòng nguồn**.
- `08-credit-001.jsonl`: **77 dòng nguồn**.
- **1.744 dòng chênh** giữa tổng số dòng nguồn trước CP038 (**25.340**) và số ID bàn giao CP001–037 (**23.596**). Cần phục hồi CP001–037 và **so ID chính xác** để tìm vị trí thiếu; chưa tính là đã dịch.
- Tổng **352 + 77 + 1.744 = 2.173**. Khi dịch Deck và Credits, cần kiểm cả `source_fixed_field_bytes`, không áp máy móc giới hạn 37 ký tự Unicode của quiz.

## Khôi phục tiến độ

1. Khôi phục CP001–037 (**23.596 ID**) theo [PHUC_HOI_TONG_HOP_037.md](PHUC_HOI_TONG_HOP_037.md).
2. Ghép bản gộp CP038–050 (**9.150 ID**) theo ID, từ chối trùng; tổng **32.746 ID duy nhất**.
3. Áp [BAN_DINH_CHINH_037B.jsonl](BAN_DINH_CHINH_037B.jsonl) và [BAN_DINH_CHINH_037C.jsonl](BAN_DINH_CHINH_037C.jsonl) **bằng ghi đè trường `vi` theo ID**, không cộng thêm ID.
4. [BAN_DINH_CHINH_046A.jsonl](BAN_DINH_CHINH_046A.jsonl) đã được áp trong bản gộp 038–050 (tên **Shunrei**).
5. Giữ tên và xưng hô theo [THUAT_NGU.json](THUAT_NGU.json) và [XUNG_HO_NHAN_VAT.md](XUNG_HO_NHAN_VAT.md).

## QA

- **735/735** ID CP050 không trùng với CP038–049, nguyên văn JA/ID/quiz_context khớp `reference/quiz-questions.jsonl` (3.006 quiz). Giữ 5 token `<IDEOSP>`.
- Bản Việt không rỗng, không quá **37 Unicode codepoints** (dòng dài nhất đúng 37).
- Một số đáp án giữ Hán tự trong ngoặc để phân biệt chữ đồng âm ở tên địa danh/đảo.
- **Chưa xác minh đáp án đúng/sai, hình quiz, font pixel, patch ROM hoặc gameplay NDS**; những thuật ngữ hiếm cần duyệt thêm trước khi phát hành.

Repository: `ronvotri/VH-NDS`, nhánh `vh/jump-ultimate-stars-japan`, thư mục `Jump-Ultimate-Stars-Japan/`.
