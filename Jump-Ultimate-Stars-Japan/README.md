# Jump Ultimate Stars – Checkpoint 017

Bản Nhật AJUJ. Dịch trực tiếp từ tiếng Nhật, giữ Item, Skill và tên đặc trưng bằng English/Latin; nội dung thoại/truyện dùng tiếng Việt gần gũi, vừa phải.

## Tiến độ
- **10.602/34.919** chuỗi có bản Việt (**30,36%**), còn **24.317**.
- Đợt mới: **658** chuỗi từ Dr. Slump, Eyeshield 21 và Gintama; trước đó 9.944.
- File `05-thu-vien-nhan-vat-002.jsonl`: đã xong 13 dòng cuối (950–962).
- File `05-thu-vien-nhan-vat-003.jsonl`: đã dịch 645 dòng đầu (0–644). Tiếp từ dòng **645**.

## Dữ liệu
- `translation/`: 30 file JSONL có đủ ID/ja gốc; `vi=null` nếu chưa dịch.
- `BAN_DICH_017.jsonl`: 658 bản dịch mới có file, row_index, ID, ja và vi.
- `BAN_DICH_TONG_HOP_001-017.jsonl`: 10.602 câu hợp nhất.
- `THUAT_NGU.json`: 1352 mục, tên chiêu chưa xác nhận có nhãn QA.
- `XUNG_HO_NHAN_VAT.md`: quy tắc vai vế, tên manga và xưng hô.
- `QA_017.json` và `CAU_DAI_CAN_SOI_017.tsv`: báo cáo QA tĩnh và các dòng cần kiểm tra độ dài.

## Giới hạn
- 0 ID trùng/mất, 0 lỗi `<IDEOSP>`/thẻ biến, 0 câu cũ bị ghi đè theo đối chiếu ZIP 016.
- **3139** đoạn dài hơn 37 ký tự Unicode cần rà sau tích hợp font, chưa đo chiều rộng pixel thật.
- **Chưa chèn ROM, chưa hỗ trợ font Việt, chưa thử trên máy NDS**. Đây chưa phải patch chơi được.
