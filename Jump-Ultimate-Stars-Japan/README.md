# Jump Ultimate Stars (Japan) — Checkpoint 045 🇻🇳

**Tiến độ: 29.198 / 34.919 (83,62%)** — thêm **701 chuỗi Nhật–Việt mới** so với CP044, còn **5.721 chuỗi**.

## Mới nhất — Checkpoint 045 (19/11/2026)

- Nguồn gốc thực tế: `JumpUltimateStars_Japan_BanGiao_Cloud.zip` → `translation/06-jquiz-007.jsonl`.
- Hoàn thành **row_index 1023–1723**, **701 ID mới**, dừng sau đủ 4 phương án câu đố 2363 để không cắt ngang câu hỏi.
- Chủ đề: *Pyu to Fuku! Jaguar* **359 ID** (1023–1381), *Rokudenashi Blues* **132 ID** (1382–1513), *Rurouni Kenshin* **210 ID** (1514–1723).
- **Checkpoint 046 tiếp tục tại `06-jquiz-007.jsonl`, `row_index=1724`**, câu hỏi 2364 (*Rurouni Kenshin*).
- [BAN_DICH_045.jsonl](BAN_DICH_045.jsonl) — delta mới 701 bản ghi Nhật–Việt.
- [QA_045.json](QA_045.json) — QA đối chiếu 3.006 câu hỏi gốc, SHA256, vị trí phương án, các ký hiệu nguồn cần xem lại.
- [BAN_GIAO_045.md](BAN_GIAO_045.md) — tài liệu bàn giao.
- [BAN_DICH_TONG_HOP_038-045.jsonl](BAN_DICH_TONG_HOP_038-045.jsonl) — chỉ là **bản gộp CP038–045 (5.602 ID)**, **không bao gồm CP001–037**.

## Phục hồi đủ tiến độ

1. Khôi phục CP001–037 (**23.596 ID**) theo [PHUC_HOI_TONG_HOP_037.md](PHUC_HOI_TONG_HOP_037.md).
2. Nối bản gộp CP038–045 (**5.602 ID**), từ chối trùng ID; tổng phải **29.198 ID**.
3. Áp QA overlay [BAN_DINH_CHINH_037B.jsonl](BAN_DINH_CHINH_037B.jsonl) và [BAN_DINH_CHINH_037C.jsonl](BAN_DINH_CHINH_037C.jsonl) bằng **thay giá trị `vi` theo ID**, tuyệt đối không thêm bản ghi tạo ID trùng.
4. Tuân thủ [THUAT_NGU.json](THUAT_NGU.json) và [XUNG_HO_NHAN_VAT.md](XUNG_HO_NHAN_VAT.md).

## QA và giới hạn

- **701/701 ID mới** độc nhất, không trùng với CP038–044, không rỗng, `ja`, `id`, `group`, `context`, `uses`, `quiz_context` bảo toàn đúng từ ZIP.
- Đã đối chiếu mỗi ID và vị trí câu hỏi / phương án với tệp nguồn `reference/quiz-questions.jsonl`. Các mã điều khiển như `<IDEOSP>` được bảo toàn.
- Bản Việt không vượt **37 ký tự Unicode/dòng**, **chưa phải QA độ rộng font pixel**.
- **9 bản ghi** giữ nguyên Hán tự để phân biệt đáp án/tên khó và **1 dòng nguồn** có ký tự bất thường; xem [QA_045.json](QA_045.json). Tên phiên âm chưa mặc định là tên bản địa hóa chính thức.
- **Chưa kiểm tra đáp án đúng, font tiếng Việt trên NDS, hình minh họa hay ROM/gameplay thực tế.** Đây là dữ liệu bản dịch, chưa phải bản vá ROM chơi được.

Repo: `ronvotri/VH-NDS`, nhánh `vh/jump-ultimate-stars-japan`, thư mục `Jump-Ultimate-Stars-Japan/`.
