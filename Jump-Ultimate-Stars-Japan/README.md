# Jump Ultimate Stars (Japan) — Checkpoint 043 🇻🇳

**Tiến độ: 27.799 / 34.919 (79,61%)** — thêm **709 chuỗi Nhật–Việt mới** từ CP042, còn **7.120 chuỗi**.

## Mới nhất: Checkpoint 043 — 19/11/2026

Nguồn: `JumpUltimateStars_Japan_BanGiao_Cloud.zip` (bảng trích xuất trong `translation/`).

- `06-jquiz-006.jsonl`: **row_index 1617–2000 (384 ID)**, kết thúc toàn file 006 và hoàn thiện câu 2066 sau khi nối tiếp sang đầu file 007.
- `06-jquiz-007.jsonl`: **row_index 0–324 (325 ID)**, kết thúc câu hỏi 2121 (*One Piece*).
- Nội dung: phần cuối *Sakigake!! Otokojuku* và câu đố mở đầu *One Piece* về Luffy, Zoro, Nami, Usopp, Sanji, Going Merry.
- **Checkpoint 044 bắt đầu tại `06-jquiz-007.jsonl`, row_index 325**, câu hỏi 2122.
- [BAN_DICH_043.jsonl](BAN_DICH_043.jsonl) — delta 709 chuỗi với nguyên văn Nhật, ID, ngữ cảnh quiz.
- [QA_043.json](QA_043.json) — QA tĩnh, mã điều khiển, SHA256, ký hiệu khó và các trường hợp tên riêng.
- [BAN_GIAO_043.md](BAN_GIAO_043.md) — hướng dẫn tiếp nối.
- [BAN_DICH_TONG_HOP_038-043.jsonl](BAN_DICH_TONG_HOP_038-043.jsonl) — **chỉ gộp CP038+039+040+041+042+043 (4.203 ID)**, không phải bản gộp CP001–043.

## Khôi phục đủ dữ liệu đã dịch

1. Khôi phục CP001–037 (**23.596 ID**) theo [PHUC_HOI_TONG_HOP_037.md](PHUC_HOI_TONG_HOP_037.md).
2. Ghép theo ID các đợt CP038–043 (**4.203 ID**), kiểm tra tổng **27.799 ID duy nhất**.
3. Áp [BAN_DINH_CHINH_037B.jsonl](BAN_DINH_CHINH_037B.jsonl) và [BAN_DINH_CHINH_037C.jsonl](BAN_DINH_CHINH_037C.jsonl) bằng cách **thay trường `vi` theo ID**; không nối overlay tạo ID trùng.
4. Giữ quy tắc [THUAT_NGU.json](THUAT_NGU.json) và [XUNG_HO_NHAN_VAT.md](XUNG_HO_NHAN_VAT.md).

## Trạng thái QA

- QA tĩnh **709/709 bản ghi**: giữ nguyên `ja`, `id`, `quiz_context`; không trùng ID với CP038–042, không rỗng, giữ thẻ điều khiển.
- Mọi dòng Việt **tối đa 37 ký tự Unicode**; đây không phải kiểm tra độ rộng pixel font.
- Nguồn có một số ký tự bất thường (`≒`, `＿`, `＾`, `；`). Những lựa chọn chỉ khác chữ Hán được bảo toàn để không làm mất khác biệt của câu đố; xem `QA_043.json`.
- Một số bản phiên âm tên riêng còn cần đối chiếu cách viết chính thức khi thử game.
- **Chưa kiểm thử đáp án đúng, font tiếng Việt, ROM NDS, hình minh họa hoặc gameplay thực tế.** Đây là dữ liệu bản dịch text, chưa phải bản vá ROM chơi được.

Repository: `ronvotri/VH-NDS`, nhánh `vh/jump-ultimate-stars-japan`, thư mục `Jump-Ultimate-Stars-Japan/`.
