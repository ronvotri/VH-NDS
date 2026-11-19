# Jump Ultimate Stars (Japan) — Checkpoint 047 🇻🇳

**Tiến độ: 30.601 / 34.919 (87,63%)** — thêm **700 chuỗi Nhật–Việt mới** so với CP046; còn **4.318 chuỗi**.

## Mới nhất — Checkpoint 047 (20/11/2026)

Nguồn: `JumpUltimateStars_Japan_BanGiao_Cloud.zip` → `translation/06-jquiz-008.jsonl`; SHA256 `48c26ae8eb63b3d3272741f93683312ff435ac8fc8995479f96a42045acd0dfc` xác minh khớp CP046.

- `06-jquiz-008.jsonl`: **row_index 518–1217 (700 ID)**, trong đó *Saint Seiya* **575 ID** và *Jungle no Ōja Tar-chan* **125 ID**.
- Đối chiếu `reference/quiz-questions.jsonl` để giữ đúng vị trí câu hỏi/đáp án; không tự thay đáp án đúng.
- **CP048 bắt đầu `06-jquiz-008.jsonl`, `row_index=1218`, `question_index=2628`** (*Jungle no Ōja Tar-chan*).
- [BAN_DICH_047.jsonl](BAN_DICH_047.jsonl) — 700 chuỗi mới, giữ JA/ID/metadata từ nguồn.
- [BAN_DICH_047.tsv](BAN_DICH_047.tsv) — bảng Nhật–Việt thuận tiện soát.
- [QA_047.json](QA_047.json) — 700/700 ID qua QA tĩnh, SHA256, ranh giới quiz, token và nguồn bất thường.
- [BAN_GIAO_047.md](BAN_GIAO_047.md) — bàn giao, giới hạn QA và mốc tiếp.
- [BAN_DICH_TONG_HOP_038-047.jsonl](BAN_DICH_TONG_HOP_038-047.jsonl) — **7.005 ID riêng CP038–047**, đã tích hợp sửa tên Shunrei ở CP046A. **Không gồm** CP001–037.

## Khôi phục toàn bộ tiến độ

1. Khôi phục CP001–037 (**23.596 ID**) theo [PHUC_HOI_TONG_HOP_037.md](PHUC_HOI_TONG_HOP_037.md).
2. Ghép bản tổng hợp CP038–047 (**7.005 ID**) theo ID, từ chối trùng ID; tổng phải **30.601 bản ghi**.
3. Áp overlay [BAN_DINH_CHINH_037B.jsonl](BAN_DINH_CHINH_037B.jsonl) và [BAN_DINH_CHINH_037C.jsonl](BAN_DINH_CHINH_037C.jsonl) **bằng ghi đè `vi` theo ID**, không cộng bản ghi. Sửa CP046A **đã có** trong bản gộp 038–047 nên không cần áp lại; với file CP046 cũ, có thể dùng [BAN_DINH_CHINH_046A.jsonl](BAN_DINH_CHINH_046A.jsonl).
4. Duy trì [THUAT_NGU.json](THUAT_NGU.json) và [XUNG_HO_NHAN_VAT.md](XUNG_HO_NHAN_VAT.md).

## Trạng thái QA

- **700/700** chuỗi CP047: JA, ID, metadata và `quiz_context` giữ từ nguồn; đối chiếu đúng các vị trí trong `reference/quiz-questions.jsonl`.
- Không có ID trùng với 6.305 ID CP038–046; `vi` không rỗng và tối đa **37 ký tự Unicode/dòng** (thực tế CP047 tối đa **36**).
- Token điều khiển như `<IDEOSP>` được giữ nguyên. Nguồn Nhật tại `row_index=936` có ký hiệu `≪` bất thường, giữ nguyên trường JA và báo trong QA.
- **Chưa kiểm tra đáp án đúng/sai, bản hiển thị quiz có ảnh, font pixel, bản vá ROM hay gameplay NDS.** Tên phiên âm hiếm cần rà trước khi phát hành patch hoàn chỉnh.
- Bản gộp 038–047 đã đổi `春麗` từ `Chun-Li` thành **Shunrei** (đính chính CP046A).

Repository: `ronvotri/VH-NDS`, nhánh `vh/jump-ultimate-stars-japan`, thư mục `Jump-Ultimate-Stars-Japan/`.
