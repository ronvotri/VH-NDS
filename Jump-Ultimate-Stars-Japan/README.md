# Jump Ultimate Stars (Japan) — Checkpoint 049 🇻🇳

**Tiến độ: 32.011 / 34.919 (91,67%)** — thêm **705 chuỗi Nhật–Việt mới** so với CP048; còn **2.908 chuỗi**.

## Mới nhất — Checkpoint 049 (20/11/2026)

Nguồn Nhật gốc: `JumpUltimateStars_Japan_BanGiao_Cloud.zip`. Đã kiểm SHA256 của từng JSONL trước khi dịch.

- `06-jquiz-008.jsonl`: **row_index 1923–2011 (89 ID)**, SHA256 `48c26ae8eb63b3d3272741f93683312ff435ac8fc8995479f96a42045acd0dfc`, hoàn tất tệp 008.
- `06-jquiz-009.jsonl`: **row_index 0–615 (616 ID)**, SHA256 `ad517ab9020ebaaaf24d3b0be0bca8b6bbd1c9f975f1c3b745f1b249fd23d1e1`, nối câu hỏi *Bazooka 10 Năm* qua ranh giới file.
- Mã manga: *Katekyo Hitman Reborn!* **409 ID**, *Taizō Mote King Saga* **273 ID**, *Yu Yu Hakusho* **23 ID**.
- **Checkpoint 050 bắt đầu `06-jquiz-009.jsonl`, `row_index=616`, `question_index=2884`**, phần *Yu Yu Hakusho*.
- [BAN_DICH_049.jsonl](BAN_DICH_049.jsonl) — 705 bản ghi mới, bảo toàn ID, JA và metadata gốc.
- [BAN_DICH_049.tsv](BAN_DICH_049.tsv) — đối chiếu vị trí câu hỏi–đáp án.
- [QA_049.json](QA_049.json) — SHA, QA tĩnh, ghi chú trường hợp cần duyệt tên riêng.
- [BAN_GIAO_049.md](BAN_GIAO_049.md) — bàn giao và mốc CP050.
- [BAN_DICH_TONG_HOP_038-049.jsonl](BAN_DICH_TONG_HOP_038-049.jsonl) — **8.415 ID CP038–049**, đã giữ bản sửa tên Shunrei từ CP046A. **Không chứa CP001–037.**

## Khôi phục toàn bộ tiến độ

1. Khôi phục CP001–037 (**23.596 ID**) theo [PHUC_HOI_TONG_HOP_037.md](PHUC_HOI_TONG_HOP_037.md).
2. Ghép bản gộp CP038–049 (**8.415 ID**) theo ID, từ chối trùng, phải có tổng **32.011 bản ghi duy nhất**.
3. Áp overlay QA [BAN_DINH_CHINH_037B.jsonl](BAN_DINH_CHINH_037B.jsonl) và [BAN_DINH_CHINH_037C.jsonl](BAN_DINH_CHINH_037C.jsonl) **bằng ghi đè `vi` theo ID**, không nối thêm bản ghi.
4. Overlay [BAN_DINH_CHINH_046A.jsonl](BAN_DINH_CHINH_046A.jsonl) **đã nằm trong** bản gộp CP038–049; không cộng thêm ID. Duy trì thuật ngữ theo [THUAT_NGU.json](THUAT_NGU.json) và [XUNG_HO_NHAN_VAT.md](XUNG_HO_NHAN_VAT.md).

## Trạng thái QA

- **705/705 ID** CP049 giữ nguyên JA, ID, quiz_context và metadata so với nguồn. Vị trí từng câu hỏi–đáp án đã đối chiếu `reference/quiz-questions.jsonl` (3.006 câu quiz).
- Không trùng ID với 7.710 ID của CP038–048. Không có câu Việt rỗng hay vượt **37 ký tự Unicode/dòng**, bảo toàn 4 token `<IDEOSP>`.
- Điểm dừng CP049 **sau khi kết thúc câu hỏi 2883**, không cắt nhóm; nối sang CP050 ở câu hỏi 2884.
- Một số tên riêng đồng âm, tên skill chưa có bản English xác minh và từ chơi chữ trong *Taizō Mote King Saga* cần soát khi vá ROM; đã ghi trong `QA_049.json`.
- **Chưa xác minh đáp án đúng/sai, độ rộng pixel font, giao diện quiz có ảnh, patch ROM hay gameplay NDS.** QA tĩnh không đồng nghĩa hoàn tất bản chơi được.

Repository: `ronvotri/VH-NDS`, nhánh `vh/jump-ultimate-stars-japan`, thư mục `Jump-Ultimate-Stars-Japan/`.
