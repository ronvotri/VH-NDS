# Jump Ultimate Stars — Checkpoint 051 (Deck và Credits)

Đã dịch 429 ID mới từ ZIP Nhật gốc: 352 tên/mô tả Deck + 77 dòng Credits.

**Tiến độ: 33.175 / 34.919 (95,01%); còn 1.744 ID.**

## Kiểm toán nguồn

- Nguồn đủ 30 tệp JSONL, 34.919 ID không trùng.
- Đã đối chiếu 9.150 ID của CP038–050A với nguồn JA và metadata.
- 429 ID CP051 không trùng CP038–050A và không trùng phạm vi CP001–037 theo các dải row_index đã kiểm tra trên GitHub.
- Nguồn còn lại đúng: 00-he-thong-ten-goi-001 (1.231), 00-he-thong-ten-goi-002 (248), 03-nhiem-vu-luat-001 (dòng 184–448; 265).
- CP050A (10 sửa lỗi quiz/tên thẻ) được giữ nguyên trong bản gộp CP038–051.

## File bàn giao

- `BAN_DICH_051.jsonl`: 429 mục có `id`, `ja`, `vi` và metadata giữ nguyên.
- `BAN_DICH_051.tsv`: so Nhật–Việt và dung lượng UTF-8.
- `BAN_DICH_TONG_HOP_038-051.jsonl`: 9.579 ID bản gộp từ CP038–050A + CP051 (không gồm 23.596 ID CP001–037).
- `NGUON_CHUA_DICH_SAU_051.jsonl`: toàn bộ 1.744 mục còn lại từ nguồn gốc, chưa có bản dịch.
- `QA_051.json`: QA và checksum.

## Cảnh báo kỹ thuật

Tên Deck và tác giả được biên tập giữ thuật ngữ tiếng Anh quen thuộc; 120 nhãn mã deck nội bộ chủ yếu được chuẩn hóa NFKC sang mã Latin. Mọi bản Việt UTF-8 ngắn hơn độ dài trường nguồn khai báo (28/32/48 byte), nhưng **không đảm bảo** ghi trực tiếp vào ROM vì chưa biết mã hóa nhị phân/offset thực tế. Chưa có font Việt tích hợp, đo pixel, patch ROM hay QA gameplay. Không tự xác nhận hoàn thành 100%.

## Tiếp theo

CP052 ưu tiên 265 chuỗi nhiệm vụ còn sót `03-nhiem-vu-luat-001.jsonl` và các chuỗi đầu `00-he-thong-ten-goi-001.jsonl`. Phần tóm tắt manga trong `00` nên dịch theo đoạn liên tục để tránh lộn ngôi và chẻ sai nghĩa.
