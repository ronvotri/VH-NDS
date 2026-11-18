# Jump Ultimate Stars (Japan) — Việt hóa NDS

**Checkpoint 010 — 18/11/2026** · bản Nhật AJUJ · nhánh `vh/jump-ultimate-stars-japan`

## Tiến độ

- **6.022 / 34.919 chuỗi đã dịch (17,25%)**, còn **28.897** chuỗi có `vi=null`.
- Checkpoint 009: 5.369 câu. Checkpoint 010: **653 câu mới**.
- **453** câu của `02-thoai-tro-giup-003.jsonl` (dòng 505–957), hoàn thành toàn bộ file này.
- **200** câu của `04-koma-chieu-thuc-002.jsonl` (dòng 166–365), tiếp theo từ **dòng 366**.
- Nhóm vừa làm: hướng dẫn/Info Character, Jaguar, Dr. Slump, Muhyo & Roji, Neuro, Kenshiro.

## File thực tế trên GitHub

- [BAN_DICH_010.jsonl](BAN_DICH_010.jsonl): 653 dòng mới có `file`, `row_index`, `id`, `ja`, `vi`.
- [BAN_DICH_TONG_HOP_001-010.jsonl](BAN_DICH_TONG_HOP_001-010.jsonl): **6.022 bản dịch hợp nhất**.
- [THUAT_NGU.json](THUAT_NGU.json): 412 mục, nêu rõ tên Skill nào chỉ là English tạm/romanized.
- [XUNG_HO_NHAN_VAT.md](XUNG_HO_NHAN_VAT.md): phân nhóm giọng và mức xác nhận người nói.
- [QA_010.json](QA_010.json): kiểm tra cấu trúc, mã đặc biệt, ID và tiến độ.

ZIP bàn giao `JumpUltimateStars_VietHoa_Checkpoint_010.zip` trong cuộc chat chứa **đủ 30 JSONL** thuộc thư mục `translation/` cùng các file tài liệu và công cụ QA. Chưa dịch vẫn để `vi=null`, không xóa thông tin gốc. GitHub lưu bản sai biệt và bản dịch hợp nhất; để nối tiếp đầy đủ cần lấy ZIP bàn giao làm nền.

## Nguyên tắc

Dịch trực tiếp từ Nhật; giữ tên nhân vật/manga, Item, Skill và thuật ngữ chính bằng English hoặc romanized. Lời thoại gần gũi, hài vừa phải; xưng hô theo người nói/người nghe và độ tin cậy, không tự gán tên speaker. Không thay các mã `<B0A>`, `<IDEOSP>`, `<PERCENT_FULL>`, biến.

**QA tĩnh:** Đã đối chiếu toàn bộ 34.919 ID, **0 lỗi thay đổi dữ liệu gốc, ghi đè câu trước, mất ID, thẻ điều khiển**. Còn **1.051** đoạn dịch dài hơn 37 ký tự Unicode cần kiểm tra hiển thị; đây **không phải** phép đo pixel. Chưa có font Việt, chưa chèn ROM, chưa test gameplay trên NDS; **chưa phải patch chơi được**.
