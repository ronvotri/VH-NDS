# Jump Ultimate Stars (Japan) — Việt hóa NDS

**Checkpoint 002 — 18/11/2026** · Bản Nhật AJUJ · nhánh `vh/jump-ultimate-stars-japan`

## Tiến độ

- **833/34.919 chuỗi đã dịch**, còn **34.086** chuỗi chưa dịch (`vi=null`).
- Checkpoint 001: 316 câu. Checkpoint 002: **517 câu mới**.
- Hướng dẫn: 281/281 (**hoàn thành phần văn bản hướng dẫn**).
- Trợ giúp/menu: 231/1.448 câu trong file 001.
- Luật/nhiệm vụ: 184/449 câu trong file 001.
- Koma/Ability: 137/1.369 câu trong file 001.

## Dữ liệu thật trên GitHub

- [BAN_DICH_001.jsonl](BAN_DICH_001.jsonl): 316 bản dịch đợt 001 kèm ID và câu Nhật gốc.
- [BAN_DICH_002.jsonl](BAN_DICH_002.jsonl): 517 bản dịch **mới** đợt 002.
- [BAN_DICH_TONG_HOP_001-002.jsonl](BAN_DICH_TONG_HOP_001-002.jsonl): 833 bản dịch hợp nhất, có `file`, `row_index`, `id`, `ja`, `vi`.
- [THUAT_NGU.json](THUAT_NGU.json): thuật ngữ khóa, và tên kỹ năng dịch sát Nhật có đánh dấu *provisional* (không giả là tên English chính thức).
- [XUNG_HO_NHAN_VAT.md](XUNG_HO_NHAN_VAT.md): quy tắc ngôi xưng theo người nói/người nghe; không tự suy nhân vật khi thiếu bằng chứng.
- [QA_002.json](QA_002.json): mốc kiểm tra cấu trúc.

**Quan trọng:** GitHub hiện lưu bản **sai biệt** để nhẹ và dễ kiểm chứng. ZIP **JumpUltimateStars_VietHoa_Checkpoint_002.zip** được bàn giao trong ChatGPT chứa **đầy đủ 30 file `translation/*.jsonl`** cùng ID/trường `ja` gốc; các dòng chưa dịch được để `vi=null`. Nếu tiếp tục, ưu tiên ZIP bàn giao, không dịch lại các ID đã có.

## Quy tắc

Dịch trực tiếp từ tiếng Nhật. Giữ tiếng Anh tên nhân vật/manga, Item, Skill, Koma, Deck, J-Soul, Special Soul, ba thuộc tính Strength/Knowledge/Laughter; Việt hóa lời hướng dẫn, luật, mô tả và thoại. Giữ chính xác mọi thẻ `<B0A>`, `<IDEOSP>`, `<PERCENT_FULL>` và định dạng biến. Chỉ dùng tiếng Việt Unicode NFC.

**QA công cụ:** Đã kiểm tra toàn bộ 34.919 ID, **0 lỗi** thẻ/mã. Có 82 đoạn dịch dài hơn 37 ký tự Unicode cần soi khi lên màn hình; đây **không phải** kết quả đo pixel. **Chưa có font Việt/ROM writer và chưa chèn ROM, chưa thử gameplay trên NDS. Không phải patch chơi được.**
