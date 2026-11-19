# Jump Ultimate Stars (Japan) — Việt hóa Checkpoint 039

**Ngày:** 19/11/2026 · **Nhánh GitHub:** `vh/jump-ultimate-stars-japan` · **Thư mục:** `Jump-Ultimate-Stars-Japan/`

## Kết quả

- **694 mục mới** trong `translation/06-jquiz-005.jsonl`: `row_index` **705–1398** liên tục.
- Đã dịch: **24.991 / 34.919 (71,57%)**; còn **9.928** mục.
- Nội dung: câu đố *Kochikame* (đồn cảnh sát, ban nhạc, sinh nhật Ryotsu) và *Kinnikuman* (Chojin Olympics, Seven Devil Chojin, Muscle Brothers, Robin Mask, Warsman, các tuyệt chiêu và cuộc tranh ngôi vua).
- Nhân vật, tên chiêu, tên nhóm giải đấu: ưu tiên cách viết Latin/English đang dùng trong dự án; còn văn kể/chú giải là tiếng Việt tự nhiên.
- **Checkpoint 040** bắt đầu tại `row_index=1399` của `06-jquiz-005.jsonl`, một câu hỏi mới về Kinnikuman Great.

## Tệp bàn giao

| File | Tác dụng |
| --- | --- |
| `BAN_DICH_039.jsonl` | Bản dịch delta 694 ID mới, bảo toàn `file`, `row_index`, `id`, `ja`, `vi`, `quiz_context` |
| `BAN_DICH_039.tsv` | Bản dễ xem, thuận tiện đối chiếu từng chuỗi |
| `BAN_DICH_TONG_HOP_038-039.jsonl` | **Chỉ gộp hai đợt 038 và 039**: 1.395 ID, KHÔNG phải tổng hợp các đợt 001–039 |
| `QA_039.json` | Thống kê kiểm chứng ID, SHA-256 nguồn Nhật và delta, kiểm tra 37 ký tự |
| `vi_039.txt` | Bảng `row_index|vi` đầu vào đã QA, không cần trích xuất lại |

## Kiểm tra

- ZIP nguồn `JumpUltimateStars_Japan_BanGiao_Cloud.zip` được đọc trực tiếp, SHA-256 của `translation/06-jquiz-005.jsonl` trùng checkpoint 038.
- Có **694/694 ID duy nhất**, chỉ từ các dòng 705–1398, không trùng 701 ID của checkpoint 038; 34.919 ID trong ZIP nguồn cũng duy nhất.
- Từng câu hỏi/đáp án đã đối chiếu với `reference/quiz-questions.jsonl` theo `question_index`, `manga_code`, `role` và `position`, không đổi thứ tự hay xác nhận đáp án đúng/sai.
- **0 chuỗi Việt trống; 0 chuỗi trên 37 ký tự Unicode.** Không đổi token điều khiển.
- Một số chuỗi gốc được tái sử dụng ở nhiều câu hỏi, khiến tệp nguồn hiện tại chỉ chứa **một phần câu hỏi hoặc các đáp án không đầy đủ**. Không tự sáng tác chuỗi ngoài nguồn.
- Các lựa chọn chữ Hán như `にく / 肉 / 米 / 王` được giữ để phân biệt đáp án.
- Tên khó có kiểm tra tham khảo: `擬宝珠夏春都 → Geparuto Giboshi`, `秋本飛飛丸 → Pyunpyunmaru Akimoto`, `汚野 → Kitano`, `ザ・魔雲天 → The Mountain`. Nguồn tham chiếu, mức xác thực và dòng trong `QA_039.json`.

## Ghép dữ liệu không bị sót

1. Khôi phục bản tổng hợp checkpoint 037 theo `PHUC_HOI_TONG_HOP_037.md` (23.596 ID).
2. Thêm delta 038 (`BAN_DICH_038.jsonl`, 701 ID); sau đó thêm delta 039 (`BAN_DICH_039.jsonl`, 694 ID). Kiểm tra mỗi ID chỉ được xuất hiện một lần: tổng là **24.991**.
3. Áp hai bản đính chính `BAN_DINH_CHINH_037B.jsonl` và `BAN_DINH_CHINH_037C.jsonl` bằng cách **ghi đè `vi` theo ID**, tuyệt đối **không nối như ID mới**.
4. Sử dụng đúng glossary và hướng dẫn xưng hô trong nhánh hiện tại.

**Giới hạn QA:** Chưa kiểm thử font Việt, độ rộng pixel, cảnh có hình, đáp án đúng/sai trong game, hoặc ROM patch. Đây là **bản dịch văn bản**, chưa phải bản ROM chơi được.
