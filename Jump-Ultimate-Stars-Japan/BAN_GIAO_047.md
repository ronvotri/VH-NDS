# Jump Ultimate Stars — Checkpoint 047 🇻🇳

Ngày 20/11/2026. Dịch **700 chuỗi Nhật–Việt mới**, 
**30.601 / 34.919 (87.63%)**, còn **4.318** chuỗi.

## Phạm vi và nguồn

- Nguồn gốc `JumpUltimateStars_Japan_BanGiao_Cloud.zip`, đường dẫn `translation/06-jquiz-008.jsonl`.
- SHA256 nguồn: `48c26ae8eb63b3d3272741f93683312ff435ac8fc8995479f96a42045acd0dfc` khớp CP046.
- `row_index` **518–1217**: **575 dòng Saint Seiya** (manga_code 16), **125 dòng Jungle no Ouja Tar-chan** (manga_code 13).
- Chỗ nối mới từ **row_index 1218**, câu hỏi `question_index 2628`, manga_code 13.
- Đã xác nhận vị trí từng câu hỏi/đáp án trong `reference/quiz-questions.jsonl` (tổng 3006 quiz).

## File trong gói

- `BAN_DICH_047.jsonl`: 700 ID mới, dữ liệu JA và metadata nguồn gốc giữ nguyên, chỉ thêm `vi`.
- `BAN_DICH_047.tsv`: bảng Nhật–Việt + quiz_context để rà thủ công.
- `BAN_DICH_TONG_HOP_038-047.jsonl`: tổng **7.005 ID** kể từ CP038, đã áp CP046A đính chính **Shunrei**.
- `QA_047.json`: QA tĩnh + SHA256 + flags.

## Nguyên tắc và giới hạn QA

- Giữ **tên nhân vật, manga, skill/item/thuật ngữ** bằng Latin/English quen thuộc; Việt hóa phần hội thoại/quiz.
- Giữ mã token như `<IDEOSP>`, không tự sửa ký hiệu bất thường trong trường `ja`.
- Giới hạn **37 ký tự Unicode mỗi bản Việt**; chưa đo chiều rộng font pixel.
- **Chưa kiểm tra tính đúng/sai đáp án của trò chơi, quiz ảnh và ROM NDS**.
- Nhiều quiz sử dụng ảnh/đáp án tham chiếu lại; tên riêng phiên âm hiếm cần đối chiếu game trước khi phát hành patch ROM.
- Đã áp đính chính 046A (Shunrei) trong bản tổng hợp CP038–047; không cộng thêm ID.

## Khôi phục tiến độ

1. Khôi phục CP001–037 (23.596 ID) theo tài liệu bàn giao 037.
2. Ghép `BAN_DICH_TONG_HOP_038-047.jsonl` (7.005 ID) = tổng **30.601 ID**, đối chiếu trùng theo ID.
3. Các overlay 037B/037C vẫn áp bằng cách **ghi đè `vi` theo ID**, không nối bản ghi mới.
4. Tiếp CP048 từ `06-jquiz-008.jsonl`, row 1218, câu hỏi 2628.
