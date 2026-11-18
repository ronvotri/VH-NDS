# Jump Ultimate Stars (Japan) — Việt hóa NDS

**Checkpoint 006 — 18/11/2026** · Bản Nhật AJUJ · Nhánh `vh/jump-ultimate-stars-japan`

## Tiến độ

- **3.238 / 34.919** chuỗi đã Việt hóa (**9,27%**). Còn **31.681** chuỗi `vi=null`.
- Đợt 006: **621 bản dịch mới**, gồm `02-thoai-tro-giup-002.jsonl` dòng 0–360 (**361**) và `04-koma-chieu-thuc-001.jsonl` dòng 704–963 (**260**).
- Giữ nguyên 2.617 bản dịch từ Checkpoint 001–005, không chỉnh sửa ID, trường Nhật gốc, nguồn hay mã điều khiển.

## Dữ liệu GitHub

- [BAN_DICH_006.jsonl](BAN_DICH_006.jsonl): 621 câu mới, mỗi câu chứa `file`, `row_index`, `id`, `ja`, `vi`.
- [BAN_DICH_TONG_HOP_001-006.jsonl](BAN_DICH_TONG_HOP_001-006.jsonl): toàn bộ 3.238 câu đã dịch từ đầu dự án, không trùng ID.
- [THUAT_NGU.json](THUAT_NGU.json): 258 mục; tên Skill chưa xác thực English chính thức được gắn nhãn `romanized_japanese_qa` / `provisional_literal_jp_qa`.
- [XUNG_HO_NHAN_VAT.md](XUNG_HO_NHAN_VAT.md): quy tắc ngôi xưng, giọng Info Character và các nhóm manga.
- [QA_006.json](QA_006.json): kết quả QA ID/cấu trúc/tokens.

## ZIP bàn giao

`JumpUltimateStars_VietHoa_Checkpoint_006.zip` được bàn giao qua ChatGPT, chứa toàn bộ **30 file `translation/*.jsonl`**, 3.238 bản dịch trong ngữ cảnh và 31.681 dòng chưa dịch (`vi=null`). GitHub đang lưu các file **bản dịch sai biệt theo ID** và file hợp nhất, **không chứa cả 30 file nguồn**.

## Quy tắc

Dịch trực tiếp từ Nhật. Giữ tên nhân vật, manga, Item, Skill, Koma, Deck, J-Soul và tên thuộc tính game bằng tiếng Anh; còn lời giải thích, nhiệm vụ, thoại thì dùng tiếng Việt tự nhiên, vui đúng nhân vật. Giữ chuẩn thứ tự và số lượng `<IDEOSP>`, `<Bxx>`, `<PERCENT_FULL>`, biến printf.

**QA tự động:** 34.919 ID, 0 lỗi cấu trúc/mã, không ghi đè bản dịch cũ. **657 đoạn** dài hơn 37 ký tự Unicode cần kiểm tra hiển thị khi có font Việt. **Chưa chèn font/chỉnh ROM, chưa kiểm tra độ rộng pixel hoặc chơi trên NDS, và chưa có patch chơi được.**
