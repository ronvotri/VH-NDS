# Jump Ultimate Stars — Việt hóa Checkpoint 046

**20/11/2026.** Hoàn thành **703 chuỗi mới**, tổng cộng **29901/34919 (85.63%)**, còn **5018 chuỗi**.

## Phạm vi dịch

- Nguồn ZIP **JumpUltimateStars_Japan_BanGiao_Cloud.zip**; `606-jquiz-007.jsonl` **row_index 1724–1908** (**185 ID**), phần cuối *Rurouni Kenshin* và mở đầu *Slam Dunk*.
- `606-jquiz-008.jsonl` **row_index 0–517** (**518 ID**), nối câu hỏi giày của Sakuragi từ file 007, hoàn tất *Slam Dunk*, tiếp *Shaman King* và mở đầu *Saint Seiya*.
- **Checkpoint 047 bắt đầu `606-jquiz-008.jsonl`, row_index 518** (câu tiếp theo về *Saint Seiya*).

## Tệp

- `BAN_DICH_046.jsonl`: **703 ID mới**, đủ JA, VI, quiz_context.
- `BAN_DICH_046.tsv`: đối chiếu trực quan mỗi dòng.
- `BAN_DICH_TONG_HOP_038-046.jsonl`: **6.305 ID** của CP038–046; **không gồm** CP001–037.
- `QA_046.json`: kết quả QA, SHA256, các ký hiệu nguyên bản cần xem lại.

## QA

- **703/703** ID không trùng, không có bản Việt rỗng hoặc quá 37 ký tự Unicode.
- Đối chiếu nguyên văn `ja` và metadata trên từng dòng với `reference/quiz-questions.jsonl`, bảo toàn vị trí câu hỏi–đáp án và token điều khiển.
- **4** dòng nguyên tác có ký hiệu bất thường; **1** đáp án giữ Hán tự tránh nhập nhằng. Xem QA JSON.
- Tên người/chiêu thức bằng Latin theo quy ước của dự án; cần kiểm tra tên chính thức và độ rộng font khi vá ROM.
- **Chưa kiểm tra đúng/sai đáp án, font pixel, gameplay NDS hay bản patch ROM.** Đây là dữ liệu dịch text.

## Phục hồi

1. Khôi phục CP001–037 (23.596 ID) bằng `PHUC_HOI_TONG_HOP_037.md`.
2. Ghép bản gộp CP038–046 (**6.305 ID**) theo ID → phải đủ **29901 ID**.
3. Áp overlay QA 037B/C bằng **ghi đè `vi` theo ID**, không nối thành ID mới.
