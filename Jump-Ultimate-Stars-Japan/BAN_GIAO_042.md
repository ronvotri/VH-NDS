# Jump Ultimate Stars — Việt hóa Checkpoint 042 🇻🇳

**Ngày:** 19/11/2026. **Đã dịch:** **27,090/34,919 (77.58%)**. **Mới:** **+698**. **Còn:** 7,829.

## Nội dung

- Nguồn gốc: `JumpUltimateStars_Japan_BanGiao_Cloud.zip` → `translation/06-jquiz-006.jsonl` (2,001 mục).
- Đã dịch `06-jquiz-006.jsonl` từ **row_index 919 đến 1616** (698 mục), bao gồm *Jigoku Sensei Nube*, *Ninku*, *Majin Tantei Nogami Neuro* và câu đố mở đầu *Sakigake!! Otokojuku*.
- Kết thúc **trọn câu hỏi 2003**; **CP043 bắt đầu từ row_index 1617**, câu đố 2004 về hiệu trưởng Heihachi Edajima.
- Chỉ dịch `vi`, giữ nguyên `ja`, `id`, `quiz_context` và thứ tự mọi lựa chọn có trong nguồn. Không bổ sung đáp án thiếu ở câu hỏi dùng chung.

## Danh sách tệp

- `BAN_DICH_042.jsonl`: 698 mục dịch mới.
- `BAN_DICH_042.tsv`: dạng bảng, dễ rà Nhật–Việt.
- `QA_042.json`: số lượng, QA, SHA256 và các ký tự cần kiểm tra.
- `BAN_DICH_TONG_HOP_038-042.jsonl`: bản gộp riêng **038–042**, 3494 ID **không phải tổng hợp 001–042**.

## QA & phục hồi

- 698/698 chuỗi Việt không rỗng, không trùng, khớp nguồn ZIP về văn bản Nhật và `quiz_context`.
- Không có bản Việt vượt **37 ký tự Unicode**; số ký tự không thay thế kiểm tra độ rộng pixel.
- Dữ liệu gốc có tên bị lỗi ký tự `藍｜`; dịch theo tên nhân vật *Aicho* được xác nhận từ các nguồn truyện, **không thay nguyên văn Nhật**. Tên kanji khác giữ nguyên khi cách đọc chưa chắc hoặc đáp án chỉ khác mặt chữ.
- Chiêu thức, tên nhân vật manga được giữ theo tên English/romanized khi có thể; cần rà thuật ngữ và tên chiêu chưa được địa phương hóa chính thức trên máy thật.
- Khôi phục 001–037 (23.596 ID), nối CP038–042 theo ID và sau đó áp overlay đính chính 037B/037C bằng thay `vi` (không nối tạo ID trùng) → tổng **27,090 ID**.

**Chưa kiểm thử đáp án đúng, font/độ rộng pixel, hình minh họa hoặc ROM NDS. Tệp này là bản dịch text, chưa phải ROM patch chơi được.**
