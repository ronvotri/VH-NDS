# Jump Ultimate Stars — Việt hóa Checkpoint 041 🇻🇳

**Ngày:** 19/11/2026  ·  **Nhánh:** `vh/jump-ultimate-stars-japan`  ·  **Game:** Jump Ultimate Stars (Japan)

## Kết quả

- **701 chuỗi mới** từ `translation/06-jquiz-006.jsonl` trong ZIP gốc, `row_index` **218–918**.
- Chủ đề: đoạn cuối *Muhyo & Roji*, chuỗi câu đố *Naruto* và mở đầu *Jigoku Sensei Nube*.
- **26.392/34.919** chuỗi dịch (**75,58%**), còn **8.527**.
- Điểm tiếp tục CP042: `06-jquiz-006.jsonl`, **row_index 919**.

## Các tệp

- `BAN_DICH_041.jsonl`: delta 701 dòng Nhật/Việt, giữ `file`, `row_index`, `id`, `ja`, `quiz_context`.
- `BAN_DICH_041.tsv`: trình bày dễ đọc để kiểm tra.
- `QA_041.json`: chi tiết số lượng, SHA256, mã điều khiển, vị trí câu hỏi/đáp án, dòng cần kiểm tra.
- `BAN_DICH_TONG_HOP_038-041.jsonl`: chỉ **2.796 ID** thuộc bốn checkpoint 038–041, **không bao gồm CP001–037**.

## QA và điểm cần lưu ý

- Đã đối chiếu **701/701** ID và nguyên văn `ja` với ZIP nguồn; đồng thời đối chiếu vai trò và vị trí các đáp án bằng `reference/quiz-questions.jsonl`.
- Không có ID trùng trong bộ delta hay bản gộp CP038–041; không có bản Việt trống; không chuỗi nào vượt 37 Unicode codepoint.
- **Không suy đoán đáp án đúng**; tham chiếu gốc chỉ bảo toàn thứ tự đáp án, không quy định đáp án chính xác.
- Một số câu hỏi trong game dùng lại ID từ checkpoint khác. Nếu chỉ nhìn delta, có thể thiếu một số lựa chọn; không tự tạo câu thay thế.
- Các chữ Hán/nhãn lựa chọn dễ đồng âm được giữ kèm bản đọc để không mất sự khác nhau giữa đáp án. Ký hiệu nguồn `∴`/`〈` được ghi lại trong `QA_041.json` để đối chiếu font gốc.
- Chưa kiểm thử độ rộng pixel font, ký tự Việt, hình minh họa hay gameplay ROM NDS; **đây là dữ liệu dịch, không phải patch ROM**.

## Khôi phục

1. Khôi phục CP001–037 (23.596 ID) theo `PHUC_HOI_TONG_HOP_037.md`.
2. Ghép CP038 (+701), CP039 (+694), CP040 (+700), CP041 (+701) bằng `id` và kiểm tra **26.392 ID độc nhất**.
3. Áp `BAN_DINH_CHINH_037B.jsonl` và `BAN_DINH_CHINH_037C.jsonl` dưới dạng overlay ghi đè trường `vi`; **không nối thêm thành ID mới**.
4. Tuân thủ `THUAT_NGU.json`, `XUNG_HO_NHAN_VAT.md`; khi dịch CP042 bắt đầu đúng `row_index 919`.
