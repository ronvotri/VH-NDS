# Jump Ultimate Stars (NDS, Japan) — Việt hóa AJUJ

**Checkpoint 012 • 18/11/2026**

## Tiến độ

- **7.321 / 34.919 chuỗi (20,97%)** — 610 chuỗi mới so với CP011, còn **27.598** chuỗi chưa dịch.
- Phần mới: 309 dòng `04-koma-chieu-thuc-002.jsonl` (1055–1363) và 301 dòng `04-koma-chieu-thuc-003.jsonl` (0–300).
- Giữ nguyên toàn bộ 6.711 câu Checkpoint 011, mã ID, câu `ja` gốc và mã điều khiển.
- **Đã hoàn thành toàn bộ văn bản Koma/Skill file 002.**

## Các tệp thật đã đồng bộ trên GitHub

- [BAN_DICH_012.jsonl](BAN_DICH_012.jsonl): **610 bản dịch mới** kèm `file`, `row_index`, `id`, `ja`, `vi`.
- [BAN_DICH_TONG_HOP_001-012.jsonl](BAN_DICH_TONG_HOP_001-012.jsonl): **7.321 bản dịch hợp nhất** (đã lưu trên GitHub).
- [THUAT_NGU.json](THUAT_NGU.json): **781 mục** thuật ngữ và tên Skill; dạng phiên âm chưa xác minh tên English chính thức được ghi `working_romanization_qa`.
- [XUNG_HO_NHAN_VAT.md](XUNG_HO_NHAN_VAT.md): quy tắc xưng hô theo nhân vật/nhóm manga và mức độ xác thực.
- [QA_012.json](QA_012.json): kết quả QA tĩnh.

**ZIP trong cuộc chat `JumpUltimateStars_VietHoa_Checkpoint_012.zip` là bản bàn giao đầy đủ.** ZIP chứa toàn bộ 30 file trong `translation/`, tức cả các câu chưa dịch có `vi=null`; GitHub giữ bản sai biệt và hợp nhất theo ID để dễ theo dõi. **Không có ROM trong ZIP.**

## Quy tắc dịch và chất lượng

Dịch từ tiếng Nhật; giữ tên nhân vật, manga, Item, Skill, Koma, Deck, J-Soul, Special Soul, thuộc tính; phần thoại, hướng dẫn và mô tả thì Việt hóa tự nhiên, Gen Z vừa phải và đúng tính cách từng manga. Không tự gán người nói khi dữ liệu thiếu speaker. Bảo toàn thẻ điều khiển `<IDEOSP>`, `<B0A>`, `<PERCENT_FULL>` và biến.

**QA tĩnh:** kiểm tra 34.919 ID, đúng thứ tự thẻ, placeholder, Unicode NFC, bảo toàn bản dịch cũ: **0 lỗi**. Có **1.486** chuỗi dài trên 37 ký tự Unicode cần xem trên màn hình; đây không phải đo độ rộng pixel hay QA runtime.

**Chưa tích hợp font tiếng Việt, chưa chèn trở lại ROM, chưa tạo patch chơi được trên máy NDS/giả lập.**

## Checkpoint tiếp theo

Tiếp tục `04-koma-chieu-thuc-003.jsonl` từ **dòng 301** (Near, Mello và các nhân vật tiếp theo), không dịch lại ID đã hoàn thành.
