# Jump Ultimate Stars (Japan) — Việt hóa Checkpoint 043

**Ngày:** 19/11/2026. **Mới dịch:** 709 chuỗi. **Tiến độ:** 27.799/34.919 (79.61%). **Còn:** 7.120.

## Phạm vi

- `translation/06-jquiz-006.jsonl`: dòng **1617–2000** (384 ID), hoàn thành toàn file **006**. Kết thúc câu hỏi 2066 (hai đáp án sau cùng nằm ở đầu file 007).
- `translation/06-jquiz-007.jsonl`: dòng **0–324** (325 ID), kết thúc câu hỏi 2121. Bắt đầu file 007 bằng hai đáp án nối sang từ file 006.
- Nội dung: phần còn lại *Sakigake!! Otokojuku* và loạt câu mở đầu *One Piece* (Luffy, Zoro, Nami, Usopp, Sanji, Going Merry).
- **Checkpoint 044 bắt đầu từ dòng 325 của `06-jquiz-007.jsonl`**, câu hỏi 2122.

## Dữ liệu bàn giao

- `BAN_DICH_043.jsonl`: 709 ID mới.
- `BAN_DICH_043.tsv`: bảng kiểm Nhật–Việt.
- `BAN_DICH_TONG_HOP_038-043.jsonl`: riêng CP038–043, **4.203 ID**, không phải bản gộp CP001–043.
- `QA_043.json`: kiểm tra ID, SHA-256, đối chiếu tiếng Nhật, mã điều khiển, độ dài, nguồn bất thường.

## QA và giới hạn

- QA tĩnh **709/709 ID**: `ja`, `quiz_context`, vị trí câu hỏi–đáp án và thẻ điều khiển giữ nguyên; không trùng ID với CP038–042; không bỏ trống bản Việt; mọi `vi` tối đa 37 ký tự Unicode.
- Tên manga, nhân vật và thuật ngữ chính giữ tên English/romanized. Câu đố dựa vào chữ Hán trông gần nhau phải **giữ nguyên chữ Hán** ở phương án để tránh làm mất khác biệt. Một số tên bị lỗi ký tự trong bản Nhật (`鄧≒傑`, `顎＿洙`, `＾家`) được ghi chú, chưa tự sửa nguyên văn `ja`.
- Khôi phục tổng 001–037 (23.596), nối CP038–043 (4.203) theo ID, áp overlay 037B/037C **bằng thay trường `vi`**, không thêm ID → tổng **27.799 bản dịch duy nhất**.
- **Chưa xác minh đáp án đúng/sai, font tiếng Việt, độ rộng pixel, ROM NDS hoặc gameplay.** Đây là bản dịch text, chưa phải bản vá ROM đã chơi được.
