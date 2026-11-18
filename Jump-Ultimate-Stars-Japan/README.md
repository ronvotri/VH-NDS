# Jump Ultimate Stars (Japan) — Việt hóa NDS

**Checkpoint 011 — 18/11/2026** · ROM gốc Nhật AJUJ · nhánh `vh/jump-ultimate-stars-japan`

## Tiến độ
- **6.711 / 34.919 chuỗi** (19,22%) đã dịch; **28.208** chuỗi còn `vi=null`.
- Checkpoint 010 có 6.022 câu, đợt **011 dịch mới 689 câu**, từ dòng 366–1054 của `04-koma-chieu-thuc-002.jsonl`.
- Tiếp theo bắt đầu từ **dòng 1055** cùng file (Yoruichi, Byakuya, Aizen; các manga tiếp theo).

## Bản dịch trên GitHub
- [BAN_DICH_011.jsonl](BAN_DICH_011.jsonl): **689** bản dịch mới, kèm `file`, `row_index`, `id`, `ja`, `vi`.
- [BAN_DICH_TONG_HOP_001-011.jsonl](BAN_DICH_TONG_HOP_001-011.jsonl): **6.711** bản dịch hợp nhất.
- [THUAT_NGU.json](THUAT_NGU.json): **586** thuật ngữ, đánh dấu các tên tiếng Anh/phiên âm chưa xác minh.
- [XUNG_HO_NHAN_VAT.md](XUNG_HO_NHAN_VAT.md): quy tắc xưng hô theo nhân vật, quan hệ và tình huống, không tự gán người nói.
- [QA_011.json](QA_011.json): báo cáo QA tĩnh.

ZIP bàn giao **JumpUltimateStars_VietHoa_Checkpoint_011.zip** trong chat chứa đầy đủ **30 file JSONL** (34.919 ID), cùng bản dịch hợp nhất; các chuỗi chưa xử lý để `vi=null`. GitHub giữ bản sai biệt và bản hợp nhất, không chứa ROM.

## Quy tắc và QA
Dịch trực tiếp từ Nhật. Giữ tên nhân vật, manga, Item, Skill, Koma, Deck, J-Soul, Special Soul bằng tiếng Anh hoặc phiên âm nhất quán. Dịch hội thoại, mô tả, hướng dẫn sang tiếng Việt tự nhiên, hài nhẹ phù hợp tính cách. Bảo toàn thẻ `<IDEOSP>`, `<B0A>`, `<PERCENT_FULL>` và biến.

**QA tĩnh:** 34.919 ID, 0 lỗi mã/thẻ, 0 ghi đè 6.022 câu cũ, 0 thay đổi Nhật gốc. Có **1.308** đoạn dịch dài hơn 37 ký tự Unicode cần kiểm tra giao diện thực tế (không phải đo pixel).

**Chưa tích hợp font Việt, chưa chèn lại vào ROM, chưa QA trực tiếp trên máy NDS. Đây chưa phải patch ROM chơi được.**
