# Jump Ultimate Stars — Việt hóa Checkpoint 045

**Ngày 19/11/2026.** Hoàn thành **701 chuỗi mới**; tổng tiến độ **29198/34919 (83.62%)**, còn **5721 ID**.

## Phạm vi

- Nguồn thật: ZIP `JumpUltimateStars_Japan_BanGiao_Cloud.zip`, file `translation/06-jquiz-007.jsonl`, row_index **1023–1723**.
- **Pyu to Fuku! Jaguar** (manga_code 27): dòng 1023–1381, **359 mục**. Phần câu đố về Piyohiko, Jaguar, Hammer, khoa Sáo.
- **Rokudenashi Blues** (manga_code 40): dòng 1382–1513, **132 mục**.
- **Rurouni Kenshin** (manga_code 39): dòng 1514–1723, **210 mục**; kết thúc câu hỏi 2363 sau lựa chọn cuối.
- **Checkpoint 046 bắt đầu tại** `06-jquiz-007.jsonl` **row_index 1724** (câu hỏi 2364).

## Tệp bàn giao

- `BAN_DICH_045.jsonl`: 701 chuỗi Nhật–Việt, bảo toàn ID, metadata và `quiz_context`.
- `BAN_DICH_045.tsv`: đối chiếu từng dòng.
- `BAN_DICH_TONG_HOP_038-045.jsonl`: **5.602 ID** gộp CP038–CP045, **không gồm** CP001–037.
- `QA_045.json`: QA tự động, SHA256, ký tự lạ từ nguồn và danh sách phương án để lại Hán tự.

## QA đã thực hiện

- **701/701 ID** mới không trùng trong lô hay với **4.901** chuỗi CP038–044.
- Mọi `ja`, `id`, `group`, `context`, `uses`, `quiz_context` được giữ nguyên nguồn và **đối chiếu từng vị trí** với `reference/quiz-questions.jsonl` trong ZIP.
- Các mã điều khiển như `<IDEOSP>` giữ nguyên; không có chuỗi Việt trống, chuỗi quá **37 ký tự Unicode** hay lỗi U+FFFD.
- Câu hỏi 2241 và 232x có phương án dùng chung ID từ nhóm trước, nên vẫn bảo toàn file nguồn; không tự bịa phương án bị thiếu.
- **9 dòng** giữ chữ Hán để phân biệt tên hoặc đáp án có dạng dễ gây nhầm. **1 dòng** được đánh dấu vì ký hiệu bất thường từ nguyên bản.
- **Chưa kiểm thử đáp án đúng, độ rộng pixel font, màn hình game hay ROM NDS.** Đây là gói dữ liệu dịch text, không phải patch ROM chơi được.

## Phục hồi đầy đủ

1. Khôi phục CP001–037 (**23.596 ID**) bằng `PHUC_HOI_TONG_HOP_037.md`.
2. Nối bản tổng hợp CP038–045 (**5.602 ID**) theo ID, kiểm tra đủ **29198 ID**.
3. Áp `BAN_DINH_CHINH_037B.jsonl` và `BAN_DINH_CHINH_037C.jsonl` bằng **cập nhật trường `vi` theo ID**, không nối trùng các bản ghi.
