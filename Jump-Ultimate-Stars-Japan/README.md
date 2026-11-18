# Jump Ultimate Stars — Checkpoint 018

Dịch trực tiếp từ bản Nhật AJUJ; giữ tên nhân vật, manga, Item, Skill, thuật ngữ chính bằng English/phiên âm; hội thoại và lời kể bằng tiếng Việt tự nhiên, hài vừa đủ.

## Tiến độ
- **11.202 / 34.919** ID đã có bản Việt (**32,08%**); còn **23.717** chưa dịch.
- Checkpoint 018: **600 ID mới**, giữ nguyên **10.602 câu** Checkpoint 017.
- Hoàn thành `05-thu-vien-nhan-vat-003.jsonl`, các dòng 645–944.
- Tiếp tục `05-thu-vien-nhan-vat-004.jsonl`, các dòng 0–299.
- **Điểm tiếp theo:** `05-thu-vien-nhan-vat-004.jsonl`, `row_index=300`.

## Dữ liệu GitHub
- `BAN_DICH_018.jsonl`: 600 câu mới, giữ `file`, `row_index`, `id`, `ja`, `vi`.
- `BAN_DICH_TONG_HOP_001-018.jsonl`: đủ 11.202 câu Việt hóa đã hợp nhất.
- `THUAT_NGU.json`: **1.367 mục**, có thêm thuật ngữ Gintama, Hunter × Hunter, Hokuto và Hoshin.
- `XUNG_HO_NHAN_VAT.md`: cập nhật cách xưng hô theo từng tác phẩm.
- `QA_018.json`: kết quả kiểm tra tĩnh.

## Dữ liệu nguồn đầy đủ
ZIP `JumpUltimateStars_VietHoa_Checkpoint_018.zip` bàn giao trong cuộc trò chuyện gồm toàn bộ 30 file trong `translation/`, đủ 34.919 chuỗi. Những chuỗi chưa dịch có `vi=null`. Bản GitHub là các file sai biệt/hợp nhất để tiết kiệm dung lượng; dùng ZIP làm nguồn đầy đủ khi làm tiếp.

## Kết quả kiểm tra và giới hạn
- 34.919 ID duy nhất; **0 lỗi mã điều khiển và placeholder, 0 câu cũ bị ghi đè**.
- **3.385** đoạn dài hơn 37 ký tự cần QA độ rộng khi tích hợp font thực tế.
- **Chưa chèn ROM, chưa tích hợp font Việt, chưa kiểm thử máy NDS.** Đây chưa phải patch chơi được.
