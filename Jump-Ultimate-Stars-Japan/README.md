# Jump Ultimate Stars (Japan) — Việt hóa NDS (AJUJ)

**Checkpoint 004 — 18/11/2026** | Nhánh `vh/jump-ultimate-stars-japan`

## Tiến độ thật

- **2.008/34.919 câu** đã Việt hóa (5,75%). Còn **32.911** câu.
- Checkpoint 001: 316 câu; 002: 517 câu; 003: 571 câu; **004: 604 câu mới**.
- Đợt 004: `02-thoai-tro-giup-001.jsonl` dòng 609–980 (372 câu); `04-koma-chieu-thuc-001.jsonl` dòng 330–561 (232 câu).
- Dịch từ Nhật `ja`; chỉ điền vào `vi=null`; không sửa 1.404 câu cũ.

## Tệp trên GitHub

- [BAN_DICH_001.jsonl](BAN_DICH_001.jsonl) / [002](BAN_DICH_002.jsonl) / [003](BAN_DICH_003.jsonl) / [004](BAN_DICH_004.jsonl): các đợt riêng, có `file`, `row_index`, `id`, `ja`, `vi`.
- [BAN_DICH_TONG_HOP_001-004.jsonl](BAN_DICH_TONG_HOP_001-004.jsonl): **2.008 câu hợp nhất**, không trùng ID.
- [THUAT_NGU.json](THUAT_NGU.json): **208 mục**, Skill chưa xác minh tên chính thức gắn nhãn `provisional_literal_jp_qa`.
- [XUNG_HO_NHAN_VAT.md](XUNG_HO_NHAN_VAT.md): quy tắc thoại Info Character và manga.
- [QA_004.json](QA_004.json): thống kê QA tĩnh.

**ZIP `JumpUltimateStars_VietHoa_Checkpoint_004.zip` trong cuộc chat** chứa đủ 30 file nguồn `translation/*.jsonl`, tổng 34.919 ID; chưa dịch là `vi=null`. GitHub giữ các bản dịch **delta** kèm ID để quản lý nhẹ và không phát hành ROM. Khi tiếp tục, ưu tiên ZIP checkpoint gần nhất và ghép theo ID.

## Quy tắc Việt hóa

Giữ tên nhân vật, manga, Item, Skill, Koma, Deck, J-Power, Special Soul và thuật ngữ chính bằng tiếng Anh. Việt hóa hướng dẫn, luật, mô tả, thoại bằng tiếng Việt tự nhiên; chỉ pha hài nơi đúng giọng nhân vật. Các thẻ `<B0A>`, `<IDEOSP>`, `<PERCENT_FULL>` và biến định dạng phải giữ đúng số lượng/thứ tự. Giữ ID/JA/metadata gốc.

**QA:** 34.919 ID duy nhất, 0 lỗi mã điều khiển hoặc ghi đè bản dịch trước, 260 đoạn trên 37 ký tự Unicode cần kiểm tra độ rộng thực tế khi có font. **Chưa có font Việt/ROM writer, chưa chèn ROM và chưa QA gameplay NDS — không phải patch chơi được.**
