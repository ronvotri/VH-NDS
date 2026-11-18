# Jump Ultimate Stars (Japan) — Checkpoint 015

Bản Nhật AJUJ. Dịch từ dữ liệu Nhật gốc trong ZIP **Checkpoint 014**, không chứa ROM.

- **Đã Việt hóa: 9.294 / 34.919 chuỗi (26,62%)**. Còn **25.625** chuỗi `vi=null`.
- **Mới đợt 015: 612 chuỗi**: `05-thu-vien-nhan-vat-001.jsonl` dòng **655–966** (312, hoàn thành file 001) và `05-thu-vien-nhan-vat-002.jsonl` dòng **0–299** (300).
- Manga: **Bleach / Buso Renkin / Cobra / Captain Tsubasa / Dragon Ball**.
- `translation/`: đầy đủ **30 tệp JSONL** gồm trường `ja`, `vi`, `id`, `context`, `group`, `uses` gốc.
- `BAN_DICH_015.jsonl`: chỉ các câu mới với ID + JP + VI; `BAN_DICH_TONG_HOP_001-015.jsonl`: toàn bộ 9.294 câu đã dịch.
- `THUAT_NGU.json`: giữ tên nhân vật, Skill, Item, Koma, thuật ngữ chính bằng Latin/English; tên chưa chuẩn có cờ cần xác minh.
- `XUNG_HO_NHAN_VAT.md`: quy tắc xưng hô theo cảnh và nhân vật, tránh lạm dụng slang trong manga nghiêm túc.
- `QA_015.json`: so sánh lại 34.919 ID, nội dung Nhật/metadata không sửa, 8.682 `vi` cũ không ghi đè, thứ tự thẻ điều khiển không sai, Unicode NFC.
- **Điểm tiếp Checkpoint 016**: `05-thu-vien-nhan-vat-002.jsonl` dòng **300** (tiếp nhóm Vegeta).

**Cảnh báo:** Những câu bị cắt ở ranh giới giữa ID và giữa hai file phải được kiểm tra độ dài khi có font Việt. Dòng >37 ký tự chỉ là danh sách QA, không phải giới hạn pixel. Chưa chèn ROM, chưa kiểm tra gameplay trên NDS thật.
