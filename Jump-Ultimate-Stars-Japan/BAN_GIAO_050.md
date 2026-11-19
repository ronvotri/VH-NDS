# Jump Ultimate Stars — Checkpoint 050 🇻🇳

**Ngày 20/11/2026.** Hoàn thành **735 chuỗi Nhật–Việt**. Tổng **32.746 / 34.919 (93.78%)**, còn **2.173**.

## Phạm vi dịch

- Tệp gốc: `translation/06-jquiz-009.jsonl` trong `JumpUltimateStars_Japan_BanGiao_Cloud.zip` — SHA256 `ad517ab9020ebaaaf24d3b0be0bca8b6bbd1c9f975f1c3b745f1b249fd23d1e1` (đã đối chiếu CP049).
- **row_index 616–1350**, tổng 735 ID; hết file **06-jquiz-009.jsonl**.
- Manga code 38 (*Yu Yu Hakusho*): **405**; manga code 37 (*Yu-Gi-Oh!*): **330**.
- Từ câu hỏi **2884** đến **3005**, là câu cuối của J-Quiz; CP050 kết thúc sau đáp án 3 của quiz 3005.
- Một số đáp án đảo chữ Hán / chơi chữ giữ Hán tự trong ngoặc để tránh câu trả lời bị trùng phiên âm, xem `QA_050.json`.

## Tệp đóng gói

- `BAN_DICH_050.jsonl` — 735 bản ghi nguồn kèm trường `vi` đã dịch.
- `BAN_DICH_050.tsv` — tra cứu Nhật–Việt kèm vị trí quiz.
- `BAN_DICH_TONG_HOP_038-050.jsonl` — **9.150 ID** của CP038–050, **không bao gồm CP001–037**; giữ sửa tên Shunrei của CP046A.
- `QA_050.json` — nguồn SHA, kết quả kiểm thử tĩnh và các điểm cần duyệt lại.

## QA và hạn chế

- Đã so khớp **735/735 ID** với nguồn Nhật và câu hỏi tham chiếu `reference/quiz-questions.jsonl` (**3.006 quiz**). Không trùng ID với 8.415 ID của CP038–049; bản Việt không rỗng và không vượt 37 ký tự Unicode (tối đa 37).
- Giữ nguyên các token điều khiển như `<IDEOSP>`; không thay ID, `ja` hoặc `quiz_context`.
- **Chưa xác minh các đáp án đúng**, câu quiz dùng ảnh, tên riêng ít gặp với từ điển chuẩn, độ rộng font pixel hay bản vá ROM NDS. Đây là dữ liệu dịch văn bản, chưa phải ROM chơi được.

## Khôi phục và phiên kế tiếp

1. Khôi phục CP001–037: **23.596 ID** theo `PHUC_HOI_TONG_HOP_037.md`.
2. Ghép bản tổng hợp CP038–050: **9.150 ID** theo ID duy nhất ⇒ **32.746 ID** toàn bộ.
3. Áp QA overlay 037B và 037C bằng ghi đè `vi` theo ID; sửa Shunrei 046A đã có trong bản gộp này.
4. **CP051**: file `06-jquiz-009.jsonl` đã hết, chọn nhóm dữ liệu chưa dịch khác trong ZIP. Còn 2.173 chuỗi.
