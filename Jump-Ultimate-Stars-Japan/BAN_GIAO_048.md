# Jump Ultimate Stars — Việt hóa Checkpoint 048 🇻🇳

Ngày 20/11/2026. Dịch **705 chuỗi Nhật–Việt mới**, tổng **31,306/34,919 (89.65%)**; còn **3,613 chuỗi**.

## Phạm vi

- ZIP nguồn gốc: `JumpUltimateStars_Japan_BanGiao_Cloud.zip`, file `translation/06-jquiz-008.jsonl`.
- SHA256 nguồn khớp CP047: `48c26ae8eb63b3d3272741f93683312ff435ac8fc8995479f96a42045acd0dfc`.
- **row_index 1218–1922 (705 ID)**. Manga_code: 13 *Jungle no Ōja Tar-chan* **20**, 22 *Tottemo! Luckyman* **133**, 18 *The Prince of Tennis* **530**, 4 *Katekyo Hitman Reborn!* **22**.
- Kiểm tra quiz `reference/quiz-questions.jsonl` với 3,006 câu; giữ vị trí từng dòng câu hỏi/đáp án, gồm đáp án xuất hiện lặp ở nơi khác.
- **CP049** tiếp từ `06-jquiz-008.jsonl`, `row_index=1923`, `question_index=2760`, phần *Katekyo Hitman Reborn!*.

## Các file

- `BAN_DICH_048.jsonl`: 705 bản ghi, giữ metadata nguồn, chỉ thêm `vi`.
- `BAN_DICH_048.tsv`: bảng đối chiếu Nhật–Việt có vị trí quiz.
- `BAN_DICH_TONG_HOP_038-048.jsonl`: **7.710 ID** riêng CP038–048, đã giữ sửa **Shunrei** của CP046A; không chứa CP001–037.
- `QA_048.json`: kiểm tra ID, SHA, token và vị trí quiz.

## QA và lưu ý

- Giới hạn 37 ký tự Unicode/dòng; dòng dài nhất CP048: **36**.
- Bảo toàn token điều khiển trong từng bản ghi: {'<IDEOSP>': 6, '<PERCENT_FULL>': 1}.
- Không trùng ID với CP038–047. Chỉ cộng 705 ID mới, không tính overlay CP046A.
- Chưa thử bản vá ROM, độ rộng pixel của font, câu trả lời chính xác của quiz hình ảnh, và chưa hoàn tất duyệt thuật ngữ/tên riêng bằng người đọc.
- Tên phiên âm hiếm, một số chữ tên manga tiếng Nhật mang tính chơi chữ; cần QA văn phong và cách viết trước khi phát hành ROM.

## Khôi phục

1. CP001–037: **23.596 ID** theo `PHUC_HOI_TONG_HOP_037.md`.
2. Ghép `BAN_DICH_TONG_HOP_038-048.jsonl`: **7.710 ID**. Tổng cần có **31.306 ID** (23.596 + 7.710).
3. Overlay 037B và 037C chỉ ghi đè `vi` theo ID, không nối mới. CP046A đã có trong bản gộp 038–048.
4. Tiếp theo dịch CP049 từ row 1923.
