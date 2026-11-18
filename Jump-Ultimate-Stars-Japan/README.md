# Jump Ultimate Stars (Japan) — Checkpoint 026

**Đã dịch: 16.329 / 34.919 chuỗi (46.76%).** Đợt này thêm **663 câu**, còn **18.590**.

- Đã hoàn thành `05-thu-vien-nhan-vat-009.jsonl` (12 dòng): phần cuối của Honda và Anzu Mazaki (*Yu-Gi-Oh!*).
- Dịch `06-jquiz-001.jsonl` dòng **0–650** (651 dòng): câu hỏi/đáp án **Bobobo-bo Bo-bobo**, tiếp đến đầu phần **Black Cat**. Checkpoint 027 bắt đầu ở dòng **651**.
- `translation/` có **30 file JSONL** đủ nguồn Nhật, đúng ID, metadata và bản Việt từ CP001–CP026; `vi=null` ở 18.590 câu chưa dịch.
- `BAN_DICH_026.jsonl` gồm đúng 663 câu mới. `BAN_DICH_TONG_HOP_001-026.jsonl` gồm 16.329 câu có bản Việt.
- Giữ nguyên 15.666 bản dịch cũ, không thay tiếng Nhật/ID, không mất token điều khiển. Xem `QA_026.json`.
- `THUAT_NGU.json` có 1497 mục; các tên/skill chưa có bản English xác nhận được đánh dấu QA, không khẳng định là tên chính thức.
- **Giới hạn quan trọng:** câu hỏi J-Quiz có đáp án với hình, dữ liệu cắt giữa ID và vài phần bất thường ở nguồn; **chưa có answer-key QA, chưa kiểm thử game**.
- Có 6329 dòng Việt dài hơn 37 ký tự Unicode trong toàn bộ bản dịch: cần đo bằng font pixel thực tế.

**Không phải bản vá ROM:** chưa chèn font Việt, chưa vá ROM NDS và chưa QA trong trò chơi.

Repo mục tiêu: `ronvotri/VH-NDS`, nhánh `vh/jump-ultimate-stars-japan`, thư mục `Jump-Ultimate-Stars-Japan/`. Trạng thái đồng bộ GitHub phải xác nhận riêng sau khi tải lên và so SHA.
