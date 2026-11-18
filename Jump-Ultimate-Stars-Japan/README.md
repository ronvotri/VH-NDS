# Jump Ultimate Stars (Japan) — Checkpoint 028

**Đã dịch: 17.615 / 34.919 chuỗi (50,45%).** Đợt này thêm **674 ID**, còn **17.304**.

- Dịch `06-jquiz-001.jsonl` dòng **1263–1930** (**668 ID**), hoàn tất file J-Quiz 001. Nội dung phần cuối *Bleach*, *Buso Renkin* và *Space Adventure Cobra*.
- Dịch nối `06-jquiz-002.jsonl` dòng **0–5** (**6 ID**) để khép câu hỏi 322, không tạo sai ngữ cảnh giữa file. **CP029 bắt đầu file 002 dòng 6**, câu hỏi 323.
- `translation/` có đủ 30 file JSONL với ID, nguồn Nhật, metadata, quiz_context và các bản dịch CP001–CP028.
- `BAN_DICH_028.jsonl` gồm 674 bản dịch mới; `BAN_DICH_TONG_HOP_001-028.jsonl` gồm đúng **17.615 câu**.
- Giữ nguyên toàn bộ 16.941 bản dịch trước, không sửa `ja`, `id`, `quiz_context`, vị trí lựa chọn, số lượng dòng. QA tự động ở `QA_028.json`.
- `THUAT_NGU.json` có **1526 mục**, một số tên Latin chưa xác minh chính thức được ghi chú trong tài liệu xưng hô.
- Duy trì toàn bộ thẻ game; kiểm tra lỗi Unicode NFC và các placeholder.
- Có **6412** chuỗi Việt dài hơn 37 ký tự Unicode, cần đo bề rộng pixel thật khi có font NDS.
- Câu hỏi dựa hình và đáp án **chưa** được QA trong game. Một số chuỗi nguồn là nửa câu/đáp án do tái dùng ID; không tự điền đáp án.

**Chưa phải ROM NDS đã Việt hóa**: chưa font, chưa chèn, chưa patch và chưa gameplay QA.

Repo: `ronvotri/VH-NDS`, nhánh `vh/jump-ultimate-stars-japan`, thư mục `Jump-Ultimate-Stars-Japan/`. Chỉ ghi nhận cập nhật GitHub sau khi xác minh qua GitHub trực tiếp.
