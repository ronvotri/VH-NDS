# Jump Ultimate Stars (Japan) — Checkpoint 046 🇻🇳

**Tiến độ: 29.901 / 34.919 (85,63%)** — thêm **703 chuỗi Nhật–Việt mới** so với CP045; còn **5.018 chuỗi**.

## Mới nhất — Checkpoint 046 (20/11/2026)

Nguồn gốc đã kiểm tra: `JumpUltimateStars_Japan_BanGiao_Cloud.zip` → `translation/` (dữ liệu trích xuất thực tế).

- `06-jquiz-007.jsonl`: **row_index 1724–1908 (185 ID)**, phần cuối *Rurouni Kenshin*, mở đầu *Slam Dunk*. Đã hết tệp 007.
- `06-jquiz-008.jsonl`: **row_index 0–517 (518 ID)**, nối câu hỏi về giày của Sakuragi, kết thúc phần *Slam Dunk*, tiếp *Shaman King* và mở đầu *Saint Seiya*.
- Theo mã manga trong nguồn: *Rurouni Kenshin* **100 ID**, *Slam Dunk* **256 ID**, *Shaman King* **296 ID**, *Saint Seiya* **51 ID**.
- **Checkpoint 047 bắt đầu tại `06-jquiz-008.jsonl`, `row_index=518`**, câu hỏi tiếp theo về *Saint Seiya*.
- [BAN_DICH_046.jsonl](BAN_DICH_046.jsonl) — bản dịch mới 703 mục, bảo toàn nguyên văn Nhật và metadata.
- [QA_046.json](QA_046.json) — QA tĩnh nguyên văn, ID, vị trí quiz, SHA256 và ký hiệu bất thường.
- [BAN_GIAO_046.md](BAN_GIAO_046.md) — hướng dẫn và lưu ý kiểm thử.
- [BAN_DICH_TONG_HOP_038-046.jsonl](BAN_DICH_TONG_HOP_038-046.jsonl) — **6.305 ID riêng của CP038–046**, **không phải bản gộp 001–046**.

## Khôi phục toàn bộ tiến độ

1. Khôi phục CP001–037 (**23.596 ID**) theo [PHUC_HOI_TONG_HOP_037.md](PHUC_HOI_TONG_HOP_037.md).
2. Ghép bản tổng hợp CP038–046 (**6.305 ID**) theo ID, từ chối trùng ID. Tổng cần có **29.901 bản ghi duy nhất**.
3. Áp sửa QA [BAN_DINH_CHINH_037B.jsonl](BAN_DINH_CHINH_037B.jsonl) và [BAN_DINH_CHINH_037C.jsonl](BAN_DINH_CHINH_037C.jsonl) **bằng ghi đè trường `vi` theo ID**; không nối thêm các overlay.
4. Giữ quy tắc [THUAT_NGU.json](THUAT_NGU.json), [XUNG_HO_NHAN_VAT.md](XUNG_HO_NHAN_VAT.md).

## Trạng thái QA

- **703/703 ID** không trùng, không rỗng, không trùng với các đợt 038–045; trường gốc `ja`, `id`, `quiz_context` và metadata khác được giữ từ ZIP.
- Đối chiếu từng vị trí câu hỏi–đáp án với `reference/quiz-questions.jsonl`, bảo toàn token như `<IDEOSP>`.
- Bản Việt không vượt **37 ký tự Unicode/dòng**; đây không phải QA chiều rộng font pixel.
- Có **4 dòng nguồn Nhật** chứa ký hiệu cần xem lại và **1 đáp án** tạm giữ Hán tự để phân biệt với lựa chọn khác. Tên phiên âm Latin cần soát lại khi tích hợp ROM.
- **Chưa kiểm thử đáp án đúng, hình minh họa, font tiếng Việt, ROM hay gameplay NDS.** Đây là **dữ liệu dịch văn bản**, chưa phải ROM patch chơi được.

Repository: `ronvotri/VH-NDS`, nhánh `vh/jump-ultimate-stars-japan`, thư mục `Jump-Ultimate-Stars-Japan/`.
