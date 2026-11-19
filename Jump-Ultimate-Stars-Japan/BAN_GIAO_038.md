# Jump Ultimate Stars — Việt hóa Checkpoint 038

**Ngày:** 2026-11-19. **Nhánh:** `vh/jump-ultimate-stars-japan`.

## Đã hoàn thành

- **701 ID mới** từ `translation/06-jquiz-005.jsonl`, `row_index` **4–704**, dựa trên ZIP bàn giao gốc người dùng vừa tải lên.
- Bắt đầu câu hỏi số 1371 về người phát hành Weekly Shonen Jump, tiếp nội dung Kochikame và kết thúc trọn câu hỏi 1489 về robot của Kanbei Ryotsu.
- Tiến độ: **24.297 / 34.919** (69.58%); còn **10.622** ID chưa dịch.
- Lần sau bắt đầu **dòng 705** cùng file.

## Kiểm tra

- 701/701 ID trùng khớp ZIP nguồn và thuộc toàn bộ 34.919 ID duy nhất.
- 701 mục liền mạch, không trùng ID hoặc trống bản dịch; tối đa **37 Unicode codepoints**/dòng Việt.
- `quiz_context`, vị trí dòng/đáp án, và thứ tự lựa chọn được xác minh với `reference/quiz-questions.jsonl`.
- Không sửa nội dung `ja`, không tự đoán đáp án đúng.
- Giữ nguyên mã điều khiển; tất cả bản dịch không vượt ngưỡng 37 ký tự thử nghiệm. **Ngưỡng 37 không phải giới hạn pixel đã chứng thực trong game.**

## Cần xem lại / QA trong ROM

- Các dòng 440, 441, 593 có ký tự `≪` ngay **trong nguyên văn nguồn**, cần kiểm tra byte, encoding hoặc ảnh J-Quiz gốc trước khi quyết định chỉnh.
- Các lựa chọn 499–502 đều đọc Keiichi nhưng dùng **bốn chữ Hán khác nhau**; giữ chữ Hán để người chơi còn phân biệt các đáp án.
- Một số câu hỏi và đáp án dùng chung giữa nhiều câu, hoặc bị thiếu đoạn khi chỉ xem theo JSONL. Khi kiểm thử cần ghép theo `quiz_context` và hình minh họa; đánh giá dịch theo từng dòng chỉ là QA tĩnh.
- Font tiếng Việt chưa được chèn, chưa build ROM và chưa thử trên giả lập/3DS.

## Tệp

- `BAN_DICH_038.jsonl`: bản dịch delta chính thức, định dạng như các checkpoint trước.
- `BAN_DICH_038.tsv`: bản đối chiếu dễ đọc.
- `QA_038.json`: số liệu QA và SHA-256 của source/delta.
- `BAN_GIAO_038.md`: báo cáo checkpoint.

**Bản dịch này là nguồn text, không phải ROM được Việt hóa.** Không nối chồng `BAN_DICH_038.jsonl` với một tệp đã chứa checkpoint 038.
