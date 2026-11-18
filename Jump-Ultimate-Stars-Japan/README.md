# Jump Ultimate Stars (Japan) — Việt hóa NDS

**Checkpoint 013 — 18/11/2026** • Bản Nhật AJUJ • Nhánh `vh/jump-ultimate-stars-japan`

## Tiến độ

- **8.027/34.919 chuỗi đã dịch (22,99%)**, còn **26.892** chuỗi `vi=null`.
- Checkpoint 012: **7.321**; Checkpoint 013: **706 câu mới**.
- Đã hoàn tất `04-koma-chieu-thuc-003.jsonl` dòng 301–1006; ba file Koma/Skill đều đã được xử lý.
- **Tiếp theo:** `05-thu-vien-nhan-vat-001.jsonl`, bắt đầu từ dòng 0; xác minh `vi=null` trước khi ghi.

## Dữ liệu thật

- [BAN_DICH_013.jsonl](BAN_DICH_013.jsonl): 706 câu mới, mỗi dòng có `file`, `row_index`, `id`, `ja`, `vi`.
- [BAN_DICH_TONG_HOP_001-013.jsonl](BAN_DICH_TONG_HOP_001-013.jsonl): **8.027** câu hợp nhất, toàn bộ mốc 001–013, không trùng ID.
- [THUAT_NGU.json](THUAT_NGU.json): **1.273** mục khóa tên người/Skill/thuật ngữ, mục phiên âm chưa kiểm chứng được đánh dấu QA.
- [XUNG_HO_NHAN_VAT.md](XUNG_HO_NHAN_VAT.md): phân biệt ngôi xưng theo người nói/quan hệ từng manga, không tự áp kiểu xưng hô cho nhãn Skill.
- [QA_013.json](QA_013.json): dữ liệu kiểm tra tĩnh.

GitHub giữ các file sai biệt và hợp nhất để dễ đối chiếu. **ZIP `JumpUltimateStars_VietHoa_Checkpoint_013.zip`** được bàn giao trong cuộc trò chuyện có **đầy đủ 30 file `translation/*.jsonl`** cùng dữ liệu `ja` gốc và các dòng còn thiếu `vi=null`.

## Quy tắc và trạng thái QA

Dịch trực tiếp từ tiếng Nhật. Giữ tên nhân vật/manga, Item, Skill và thuật ngữ đặc trưng bằng tiếng Anh hoặc Latin. Việt hóa nội dung kể chuyện và mô tả theo ngôi phù hợp. Giữ đúng trình tự mã `<B0A>`, `<IDEOSP>`, `<PERCENT_FULL>` và placeholder.

**QA tĩnh:** 34.919 ID bảo toàn, 0 lỗi mã điều khiển/placeholder/NFC, 0 bản dịch cũ bị ghi đè. **1.597** đoạn dài hơn 37 ký tự Unicode cần kiểm tra hiển thị (chưa đo pixel).

**Chưa có font Việt, chưa chèn ROM, chưa thử trên NDS. Dữ liệu này chưa phải patch chơi được.**
