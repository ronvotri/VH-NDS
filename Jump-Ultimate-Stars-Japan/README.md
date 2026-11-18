# Jump Ultimate Stars (Japan) — Việt hóa Checkpoint 019

ROM Nhật AJUJ; bản bàn giao **chỉ dữ liệu dịch, không có ROM/patch NDS**. Dịch trực tiếp từ tiếng Nhật, giữ tên nhân vật/Skill/Item/Stand/thuật ngữ quan trọng bằng tiếng Anh hoặc phiên âm, giọng Gen Z tiết chế.

## Tiến độ
- **11.851 / 34.919** ID dịch (33,94%), còn **23.068** chuỗi chưa dịch.
- Mới dịch **649 ID** từ `05-thu-vien-nhan-vat-004.jsonl` dòng **300–948**, hoàn thành toàn bộ file 004.
- Nhóm nội dung: Hoshin Engi, Ichigo 100%, I''s, JoJo, Steel Ball Run, Kochikame.
- Đã bảo toàn **11.202** bản dịch cũ, chỉ điền những `vi=null`.

## Nội dung
- `translation/`: 30 file JSONL hoàn chỉnh theo ID (`vi=null` nếu chưa dịch).
- `BAN_DICH_019.jsonl`: 649 câu mới, có đường dẫn file, dòng, ID, Nhật và Việt.
- `BAN_DICH_TONG_HOP_001-019.jsonl`: bản hợp nhất 11.851 câu đã dịch.
- `THUAT_NGU.json`, `XUNG_HO_NHAN_VAT.md`: thuật ngữ và quy tắc xưng hô cập nhật.
- `QA_019.json` cùng `CAU_DAI_CAN_SOI_019.tsv`: báo cáo QA và danh sách dòng cần kiểm tra độ rộng.

## Kiểm thử
- Công cụ kiểm tra 34.919 ID: **0 lỗi mã điều khiển, 0 ID thiếu/trùng, 0 câu cũ bị ghi đè**.
- 3674 đoạn dịch dài hơn 37 ký tự Unicode, **chưa được đo pixel trên màn hình**.
- Chưa tích hợp font tiếng Việt hoặc chèn dữ liệu vào ROM; **chưa kiểm tra gameplay trên NDS**.
- Điểm tiếp tục Checkpoint 020: `05-thu-vien-nhan-vat-005.jsonl`, dòng 0.
