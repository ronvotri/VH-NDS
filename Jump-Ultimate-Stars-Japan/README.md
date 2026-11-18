# Jump Ultimate Stars (Japan) — Checkpoint 009

Bản Nhật **AJUJ**, ngày 18/11/2026; tiếp từ Checkpoint 008, không chứa ROM.

- Tổng: **5,369 / 34.919** chuỗi (15.38%), còn **29,550** dòng `vi=null`.
- Mới dịch đợt 009: **671 chuỗi**.
  - 505 dòng trợ giúp ở `02-thoai-tro-giup-003.jsonl`, dòng 0–504.
  - 166 dòng Koma/Skill ở `04-koma-chieu-thuc-002.jsonl`, dòng 0–165 (Bobobo, Kochikame, Gintama, Reborn).
- Bảo toàn **4.698 bản dịch cũ**, toàn bộ ID, JA, metadata (`context`, `uses`, v.v.) và thẻ điều khiển. Không xóa/đổi dữ liệu chưa dịch.
- Kết quả QA tĩnh: 34.919 ID duy nhất, **0 lỗi**. Có **971** câu trên 37 ký tự Unicode cần kiểm tra tràn màn hình về sau.

## Nội dung ZIP

- `translation/`: 30 file JSONL nguồn và trường `vi`, chưa dịch là `null`.
- `BAN_DICH_009.jsonl`: 671 bản dịch mới (kèm `file`, `row_index`, `id`, `ja`, `vi`).
- `BAN_DICH_TONG_HOP_001-009.jsonl`: 5.369 bản dịch hợp nhất.
- `THUAT_NGU.json`: bảng thuật ngữ có trạng thái xác minh.
- `XUNG_HO_NHAN_VAT.md`: xưng hô theo giọng nói và độ tin cậy, không gán speaker tùy tiện.
- `QA_009.json`, `CAU_DAI_CAN_SOI_009.tsv`: báo cáo và những câu có nguy cơ tràn.
- `tools/check_translations.py`: công cụ kiểm tra tĩnh.

**Quy tắc:** Tên nhân vật, manga, Item, Skill và thuật ngữ chính giữ English/romanized; Việt hóa nội dung trò chơi từ JA gốc. Giữ tất cả mã `<B0A>`, `<IDEOSP>`, `<PERCENT_FULL>`; không coi tên Skill tạm là localized chính thức.

**Chưa có font Việt/ROM writer, chưa tích hợp hoặc kiểm thử gameplay. Đây là dữ liệu dịch, không phải patch chơi được.**
