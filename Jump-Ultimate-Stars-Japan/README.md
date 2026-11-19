# Jump Ultimate Stars (Japan) — Checkpoint 048 🇻🇳

**Tiến độ: 31.306 / 34.919 (89,65%)** — thêm **705 chuỗi Nhật–Việt mới** so với CP047; còn **3.613 chuỗi**.

## Mới nhất — Checkpoint 048 (20/11/2026)

Nguồn gốc: `JumpUltimateStars_Japan_BanGiao_Cloud.zip` → `translation/06-jquiz-008.jsonl`; SHA256 **`48c26ae8eb63b3d3272741f93683312ff435ac8fc8995479f96a42045acd0dfc`** khớp báo cáo CP047.

- `06-jquiz-008.jsonl`: **row_index 1218–1922 (705 ID)**.
- Theo mã manga: *Jungle no Ōja Tar-chan* **20**, *Tottemo! Luckyman* **133**, *The Prince of Tennis* **530**, *Katekyo Hitman Reborn!* **22**.
- **Checkpoint 049 bắt đầu `06-jquiz-008.jsonl`, `row_index=1923`, câu hỏi `question_index=2760`**, phần *Katekyo Hitman Reborn!*.
- [BAN_DICH_048.jsonl](BAN_DICH_048.jsonl) — 705 chuỗi Nhật–Việt mới, bảo toàn ID, JA và metadata.
- [BAN_DICH_048.tsv](BAN_DICH_048.tsv) — bảng đối chiếu trực quan.
- [QA_048.json](QA_048.json) — QA tĩnh và SHA256 bản xuất.
- [BAN_GIAO_048.md](BAN_GIAO_048.md) — phạm vi và hướng dẫn tích hợp.
- [BAN_DICH_TONG_HOP_038-048.jsonl](BAN_DICH_TONG_HOP_038-048.jsonl) — **7.710 ID CP038–048**, bao gồm sửa tên **Shunrei** CP046A; không gồm CP001–037.

## Khôi phục toàn bộ tiến độ

1. Khôi phục CP001–037 (**23.596 ID**) theo [PHUC_HOI_TONG_HOP_037.md](PHUC_HOI_TONG_HOP_037.md).
2. Ghép [BAN_DICH_TONG_HOP_038-048.jsonl](BAN_DICH_TONG_HOP_038-048.jsonl) (**7.710 ID**) bằng ID; tổng phải **31.306 ID duy nhất**.
3. Áp overlay [BAN_DINH_CHINH_037B.jsonl](BAN_DINH_CHINH_037B.jsonl) và [BAN_DINH_CHINH_037C.jsonl](BAN_DINH_CHINH_037C.jsonl) **bằng ghi đè `vi` theo ID**, không nối thành ID mới. Overlay [BAN_DINH_CHINH_046A.jsonl](BAN_DINH_CHINH_046A.jsonl) **đã áp trong bản gộp 038–048**.
4. Tuân thủ [THUAT_NGU.json](THUAT_NGU.json) và [XUNG_HO_NHAN_VAT.md](XUNG_HO_NHAN_VAT.md).

## Trạng thái QA

- **705/705 chuỗi CP048** có `vi` không rỗng, không trùng với 7.005 ID của CP038–047, giới hạn tối đa **37 ký tự Unicode/dòng** (dòng dài nhất CP048: **36**).
- Tất cả `id`, `ja`, `quiz_context` giữ từ nguồn; từng vị trí câu hỏi/đáp án đối chiếu `reference/quiz-questions.jsonl` (**3.006 quiz**).
- Bảo toàn **6 token `<IDEOSP>`** và **1 token `<PERCENT_FULL>`** trong các dòng tương ứng.
- Điểm dừng CP048 nằm **sau câu hỏi hoàn chỉnh 2759**, không cắt giữa nhóm.
- **Chưa kiểm thử đáp án đúng, quiz sử dụng ảnh, độ rộng pixel font, patch ROM hoặc gameplay NDS.** Một số tên riêng romaji ít gặp cần rà thủ công trước khi phát hành.
- Bản CP048 mới là **dữ liệu dịch văn bản**, chưa phải bản vá ROM chơi được.

Repository: `ronvotri/VH-NDS`, nhánh `vh/jump-ultimate-stars-japan`, thư mục `Jump-Ultimate-Stars-Japan/`.
