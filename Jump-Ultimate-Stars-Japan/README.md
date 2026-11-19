# Jump Ultimate Stars (Japan) — Checkpoint 035

**Tiến độ: 22,318/34.919 câu (63.91%)**, thêm **656 câu** từ CP034; còn **12,601**.

- J-Quiz `06-jquiz-004.jsonl`: **dòng 0–655**, từ **Hokuto no Ken / Fist of the North Star** sang **Hoshin Engi**. Checkpoint 036 bắt đầu từ dòng **656**.
- Không thay đổi **21.662 câu cũ**, bất kỳ `ja`/ID/metadata/`quiz_context` nào; giữ nguyên thứ tự `question_line` và `answer_option` và mọi thẻ game.
- Bàn giao: **30 file JSONL** trong `translation/`; `BAN_DICH_035.jsonl` (656 câu mới), `BAN_DICH_TONG_HOP_001-035.jsonl` (22,318 câu), thuật ngữ, xưng hô, QA, danh sách câu dài.
- QA tĩnh trên **34.919 ID** đạt 0 lỗi cấu trúc. Bảng thuật ngữ **1705 mục** (thêm 42 mục).
- **6815 đoạn trên 37 ký tự Unicode** cần kiểm tra hiển thị ở font NDS.
- Nguồn có dấu hiệu hỏng ký tự ở một số câu, mục thiếu tên hoặc câu hỏi không đủ đáp án; lưu trong `QA_035.json`, không tự bịa nội dung.

**Chưa có patch ROM hoặc QA gameplay.**

Repo đích: `ronvotri/VH-NDS` nhánh `vh/jump-ultimate-stars-japan`, thư mục `Jump-Ultimate-Stars-Japan/`. Chỉ xác nhận đồng bộ sau khi GitHub đọc lại cho SHA khớp.
