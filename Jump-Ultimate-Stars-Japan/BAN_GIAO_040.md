# Jump Ultimate Stars (Japan) — Việt hóa Checkpoint 040

**Ngày:** 2026-11-19. **Nguồn:** `JumpUltimateStars_Japan_BanGiao_Cloud.zip`, trực tiếp `translation/06-jquiz-005.jsonl` và `translation/06-jquiz-006.jsonl`.

## Tiến độ

- Hoàn thành **700 chuỗi mới**, tăng từ **24.991** lên **25.691 / 34.919 (73.57%)**; còn **9.228**.
- `06-jquiz-005.jsonl`: **482 chuỗi**, `row_index=1399–1880`. **Hoàn thành toàn bộ 1.881 dòng của file 005** kể từ các checkpoint trước.
- `06-jquiz-006.jsonl`: **218 chuỗi**, `row_index=0–217`. Tiếp tục các câu *Muhyo & Roji*.
- **Checkpoint 041 bắt đầu từ `06-jquiz-006.jsonl`, `row_index=218`**.

## Thành phần bàn giao

- `BAN_DICH_040.jsonl`: delta Nhật–Việt **700 bản ghi**, giữ `file`, `row_index`, `id`, `ja` và `quiz_context`.
- `BAN_DICH_040.tsv`: bảng dễ đọc.
- `BAN_DICH_TONG_HOP_038-040.jsonl`: bản gộp từ **CP038–CP040 (2.095 ID)**; không chứa CP001–CP037.
- `QA_040.json`: báo cáo QA và SHA256.
- `vi_040.txt`: text tiếng Việt theo thứ tự delta.

## Nguyên tắc QA

- Từng câu Nhật được đọc trong source gốc, map theo `id`; không đảo trật tự câu hỏi và đáp án.
- `quiz_context` được đối chiếu `reference/quiz-questions.jsonl` theo `question_index`, role và position.
- **700/700** chuỗi có `vi` khác rỗng, không trùng ID; không trùng 1.395 ID CP038–039.
- Tên kỹ năng và nhân vật giữ bằng English/romanization; các phương án tên có chữ Hán gần giống được giữ nguyên để phân biệt đáp án.
- Có dấu hiệu trích xuất không chuẩn ở ký hiệu `≠`, `‰`, `Å`, `≪`; xem danh sách trong QA trước khi sửa.
- Độ dài tối đa: **37 codepoints**; **chưa kiểm tra độ rộng chữ theo font Nintendo DS**.
- Không đoán phương án đúng, không bổ sung các dòng thiếu ở nguồn.

## Cách phục hồi

Khôi phục CP001–037 theo `PHUC_HOI_TONG_HOP_037.md`; cộng `BAN_DICH_038.jsonl`, `BAN_DICH_039.jsonl`, `BAN_DICH_040.jsonl` theo ID, chặn trùng, để có **25.691** ID. Áp `BAN_DINH_CHINH_037B/C.jsonl` bằng cách thay trường `vi`, không append overlay thành ID mới.

**Đây là bản dịch dữ liệu văn bản, chưa phải ROM patch chơi được. Chưa test font/âm thanh/gameplay hay tính đúng của đáp án Quiz.**
