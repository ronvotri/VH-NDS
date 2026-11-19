# Jump Ultimate Stars (Japan) — Checkpoint 041 🇻🇳

**Tiến độ: 26.392 / 34.919 (75,58%)** — thêm **701 chuỗi Nhật–Việt mới** từ CP040, còn **8.527 chuỗi**.

## Mới nhất: Checkpoint 041 — 19/11/2026

- Dữ liệu nguồn: `JumpUltimateStars_Japan_BanGiao_Cloud.zip` → `translation/06-jquiz-006.jsonl`.
- Hoàn thành **row_index 218–918 (701 ID)**: đoạn cuối *Muhyo & Roji*, phần quiz *Naruto*, mở đầu *Jigoku Sensei Nube*.
- **Checkpoint 042 bắt đầu tại `06-jquiz-006.jsonl`, row_index 919**.
- [BAN_DICH_041.jsonl](BAN_DICH_041.jsonl) — 701 chuỗi, giữ nguyên ID Nhật, metadata vị trí câu hỏi và đáp án.
- [QA_041.json](QA_041.json) — xác minh ID, thẻ điều khiển, đối chiếu `reference/quiz-questions.jsonl` và dòng có ký tự cần xem lại.
- [BAN_GIAO_041.md](BAN_GIAO_041.md) — mốc tiếp nối và lưu ý QA.
- [BAN_DICH_TONG_HOP_038-041.jsonl](BAN_DICH_TONG_HOP_038-041.jsonl) — gộp 4 đợt 038+039+040+041, tổng **2.796 ID**; **không phải bản gộp 001–041**.

## Phục hồi toàn bộ

1. Khôi phục CP001–037 (**23.596 ID**) theo [PHUC_HOI_TONG_HOP_037.md](PHUC_HOI_TONG_HOP_037.md).
2. Ghép CP038 (**701**), CP039 (**694**), CP040 (**700**) và CP041 (**701**) bằng ID; xác nhận tổng **26.392 ID duy nhất**.
3. Áp [BAN_DINH_CHINH_037B.jsonl](BAN_DINH_CHINH_037B.jsonl) và [BAN_DINH_CHINH_037C.jsonl](BAN_DINH_CHINH_037C.jsonl) **bằng cách thay thế trường `vi` của ID tương ứng**, không nối thêm bản ghi mới.
4. Giữ quy tắc trong [THUAT_NGU.json](THUAT_NGU.json) và [XUNG_HO_NHAN_VAT.md](XUNG_HO_NHAN_VAT.md).

## Kiểm thử và giới hạn

- QA tĩnh CP041: **701/701** dòng khớp nguyên văn tiếng Nhật; không trùng ID, không bỏ trống bản Việt; không vượt **37 ký tự Unicode**/dòng; bảo toàn các mã dạng `<IDEOSP>`.
- Đã kiểm tra vị trí câu hỏi và đáp án theo nguồn tham chiếu `reference/quiz-questions.jsonl`; một số đáp án được game dùng lại ở nhiều câu hỏi, không sáng tác thêm dữ liệu bị thiếu.
- Đánh dấu các ký hiệu bất thường từ bản Nhật (`∴`, `〈`) và các lựa chọn giữ chữ Hán để đối chiếu font/ảnh khi QA ROM.
- **Chưa xác minh đáp án đúng, độ rộng pixel font Việt, hình minh họa hoặc gameplay.** Đây là dữ liệu bản dịch; **không phải bản vá ROM NDS đã hoàn thiện**.

Repository: `ronvotri/VH-NDS`, nhánh `vh/jump-ultimate-stars-japan`, thư mục `Jump-Ultimate-Stars-Japan/`.
