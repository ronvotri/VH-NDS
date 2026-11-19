# Jump Ultimate Stars (Japan) — Checkpoint 040 🇻🇳

**Tiến độ: 25.691 / 34.919 (73,57%)**. Checkpoint 040 hoàn thành **700 ID mới**; còn **9.228**.

## Mới nhất: Checkpoint 040 — 19/11/2026

Nguồn: bản ZIP gốc `JumpUltimateStars_Japan_BanGiao_Cloud.zip`, bảng trích xuất trong `translation/`.

- `06-jquiz-005.jsonl`: **row_index 1399–1880 (482 ID)**, hoàn tất file 005 (1.881 mục nguồn). Chủ đề: *Kinnikuman*, *Makibao*, *Muhyo & Roji*.
- `06-jquiz-006.jsonl`: **row_index 0–217 (218 ID)**, các câu hỏi tiếp theo về *Muhyo & Roji*.
- **Checkpoint 041 bắt đầu tại `06-jquiz-006.jsonl`, row_index 218.**
- [BAN_DICH_040.jsonl](BAN_DICH_040.jsonl) — bản dịch CP040, 700 mục tiếng Nhật–Việt.
- [BAN_DICH_TONG_HOP_038-040.jsonl](BAN_DICH_TONG_HOP_038-040.jsonl) — chỉ là bản gộp **CP038+CP039+CP040 (2.095 ID)**; không chứa 001–037.
- [QA_040.json](QA_040.json) — kiểm tra vị trí câu hỏi, đáp án, ID, mã điều khiển, số ký tự, ký hiệu lạ và SHA256.
- [BAN_GIAO_040.md](BAN_GIAO_040.md) — tài liệu bàn giao.

## Quy trình phục hồi và kiểm tra

1. Khôi phục CP001–037 (23.596 mục) theo [PHUC_HOI_TONG_HOP_037.md](PHUC_HOI_TONG_HOP_037.md).
2. Ghép theo ID các file `BAN_DICH_038.jsonl` (+701), `BAN_DICH_039.jsonl` (+694), `BAN_DICH_040.jsonl` (+700), kiểm tra **25.691 ID độc nhất**.
3. Áp overlay `BAN_DINH_CHINH_037B.jsonl` và `BAN_DINH_CHINH_037C.jsonl` bằng cách **thay trường `vi` theo ID**, không nối thêm tạo ID mới.
4. Bảo toàn metadata `quiz_context` và quy ước trong [THUAT_NGU.json](THUAT_NGU.json), [XUNG_HO_NHAN_VAT.md](XUNG_HO_NHAN_VAT.md).

**QA tĩnh CP040:** 700/700 ID không trùng, khớp chính xác `ja` của nguồn và `reference/quiz-questions.jsonl`, giữ thẻ điều khiển, tất cả bản Việt tối đa 37 ký tự Unicode. Một số ký hiệu bất thường (`≠`, `‰`, `Å`, `≪`) và tên phương án có chữ Hán giống nhau cần kiểm tra hình ảnh/ROM trước khi sửa.

**Chưa kiểm chứng đáp án đúng, độ rộng font pixel, hình trong game hoặc bản vá ROM NDS. Bản dịch là dữ liệu text, không phải ROM patch chơi được.**

Repo `ronvotri/VH-NDS` · nhánh `vh/jump-ultimate-stars-japan` · thư mục `Jump-Ultimate-Stars-Japan/`.
