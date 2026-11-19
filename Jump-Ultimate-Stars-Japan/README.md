# Jump Ultimate Stars (Japan) — Checkpoint 042 🇻🇳

**Tiến độ: 27.090 / 34.919 (77,58%)** — thêm **698 chuỗi Nhật–Việt mới** từ CP041, còn **7.829 chuỗi**.

## Mới nhất: Checkpoint 042 — 19/11/2026

- Nguồn: `JumpUltimateStars_Japan_BanGiao_Cloud.zip` → `translation/06-jquiz-006.jsonl`.
- Hoàn thành **row_index 919–1616 (698 ID)**: J-Quiz về *Jigoku Sensei Nube*, *Ninku*, *Majin Tantei Nōgami Neuro* và mở đầu *Sakigake!! Otokojuku*.
- Kết thúc **đủ câu hỏi 2003** (hiệu trưởng Heihachi Edajima), không cắt đôi cụm phương án.
- **Checkpoint 043 bắt đầu `06-jquiz-006.jsonl`, row_index 1617**, câu 2004.
- [BAN_DICH_042.jsonl](BAN_DICH_042.jsonl) — 698 câu Nhật–Việt với ID và vị trí quiz gốc.
- [QA_042.json](QA_042.json) — QA tĩnh, SHA256, các tên/ký tự cần đối chiếu.
- [BAN_GIAO_042.md](BAN_GIAO_042.md) — hướng dẫn bàn giao và khôi phục.
- [BAN_DICH_TONG_HOP_038-042.jsonl](BAN_DICH_TONG_HOP_038-042.jsonl) — chỉ gộp **038+039+040+041+042 (3.494 ID)**, **không phải bản gộp 001–042**.

## Phục hồi đủ tiến độ

1. Khôi phục CP001–037 (**23.596 ID**) theo [PHUC_HOI_TONG_HOP_037.md](PHUC_HOI_TONG_HOP_037.md).
2. Ghép CP038 (+701), CP039 (+694), CP040 (+700), CP041 (+701), CP042 (+698) theo ID; xác nhận tổng **27.090 ID duy nhất**.
3. Áp sửa QA [BAN_DINH_CHINH_037B.jsonl](BAN_DINH_CHINH_037B.jsonl) và [BAN_DINH_CHINH_037C.jsonl](BAN_DINH_CHINH_037C.jsonl) **bằng thay trường `vi` theo ID**, tuyệt đối không nối các overlay thành ID mới.
4. Giữ quy tắc [THUAT_NGU.json](THUAT_NGU.json) và [XUNG_HO_NHAN_VAT.md](XUNG_HO_NHAN_VAT.md).

## Trạng thái QA

- QA tĩnh CP042: **698/698 ID độc nhất**, không rỗng, khớp nguyên văn `ja` trong ZIP, giữ nguyên `quiz_context`, các nhãn trả lời và mã điều khiển.
- Mọi bản Việt tối đa **37 ký tự Unicode**, **chưa phải kiểm tra độ rộng pixel**.
- Tên riêng Ninku có ký tự lỗi `藍｜` trong nguồn Nhật; bản dịch dùng **Aicho** với nguồn gốc được giữ nguyên trong trường `ja`. Các phương án đồng âm/khó đọc giữ chữ Hán để chưa phá lựa chọn đáp án.
- **Chưa kiểm thử câu trả lời đúng, ảnh minh họa, font tiếng Việt, gameplay hay ROM patch NDS.**

Đây là **tài liệu và dữ liệu dịch văn bản**, chưa phải ROM đã vá và chơi được.

Repo: `ronvotri/VH-NDS`, nhánh `vh/jump-ultimate-stars-japan`, thư mục `Jump-Ultimate-Stars-Japan/`.
