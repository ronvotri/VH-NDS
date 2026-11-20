# Jump Ultimate Stars (Japan) — Việt hóa Checkpoint 052 🇻🇳

**Ngày:** 20/11/2026. **Nhánh GitHub:** `vh/jump-ultimate-stars-japan`, thư mục `Jump-Ultimate-Stars-Japan/`.

## Đợt 052: +505 ID Nhật–Việt

- **265 ID** `03-nhiem-vu-luat-001.jsonl` — dòng **184–448**, hoàn thành toàn bộ 449 dòng trong tệp này (184 dòng đầu đã dịch trước đó). Gồm Final Tower, tên thiên hà, tên manga, tên màn/chế độ, mục tiêu từng thử thách. Các chuỗi có giới hạn **32 hoặc 44 byte**, tất cả bản Việt đều nằm trong hạn mức UTF-8 khai báo.
- **240 ID** `00-he-thong-ten-goi-001.jsonl` — dòng **0–239**, gồm tên nhạc nền, chú thích sân chơi và thông báo hệ thống/Wi-Fi. Tên game, skill và thuật ngữ chính giữ tiếng Anh; văn phong còn lại tự nhiên, gần gũi. Nguồn phần này chưa khai báo giới hạn byte cố định để kiểm trực tiếp.
- **Không tính lại** 10 sửa lỗi CP050A. Giữ nguyên bản dịch CP051 Deck (352) và Credits (77).

**Tiến độ:** 33.175 + 505 = **33.680 / 34.919 ID (96,45%)**. Còn **1.239 ID**, đã xuất lại đúng danh sách nguồn.

| Tệp chưa dịch | Dải dòng còn lại | Số ID |
| --- | --- | ---: |
| `00-he-thong-ten-goi-001.jsonl` | 240–1230 | 991 |
| `00-he-thong-ten-goi-002.jsonl` | 0–247 | 248 |
| **Tổng** | | **1.239** |

## Tệp bàn giao

- `BAN_DICH_052.jsonl`: 505 chuỗi mới, có ID, JA, VI và metadata gốc.
- `BAN_DICH_052.tsv`: bảng Nhật–Việt + số byte từng dòng.
- `BAN_DICH_TONG_HOP_038-052.jsonl`: 10.084 ID CP038–052, đã giữ 10 đính chính CP050A.
- `NGUON_CHUA_DICH_SAU_052.jsonl`: 1.239 bản ghi Nhật chưa dịch, không tự điền `vi`.
- `QA_052.json`: đối chiếu trực tiếp với ZIP Nhật 30 tệp/34.919 ID, kiểm token, giới hạn byte, ID và checksum.
- `TAO_TONG_HOP_052.py`: công cụ tái tạo bản gộp **toàn bộ CP001–052 (33.680 ID)** trực tiếp từ các delta GitHub và đính chính 037B/C, 046A, 050A.

## QA và giới hạn

- Đã kiểm tra: **505/505 ID mới duy nhất**, đúng `ja`, `group`, `file`, `row_index`, metadata; bảo toàn token `<IDEOSP>` và `<PERCENT_FULL>`; NFC; không có bản dịch rỗng; **265/265** dòng trường cố định hợp lệ theo giới hạn UTF-8.
- Phần system không có `source_fixed_field_bytes`, vì vậy **chưa kiểm chứng độ rộng font/pixel** hoặc mã hóa dữ liệu trong ROM.
- Nhật gốc có một số mảnh câu bị cắt/giá trị bất thường, đáng chú ý 03 dòng 185–187 và các câu thử thách 350–351; bản Việt đã dịch theo ngữ cảnh gần kề, cần đối chiếu thực tế khi vá.
- Tên bản nhạc ở 00 dòng 5 (`心糖滅却`) được ghi phiên âm làm việc `Shintou Mekkyaku`; cần xác minh tựa chính thức.
- **Chưa build patch NDS, chèn font hoặc thử đáp án/hiển thị trong game.** QA tĩnh không thay thế kiểm thử gameplay.

**Mốc CP053:** tiếp tục `00-he-thong-ten-goi-001.jsonl` từ dòng 240, giữ nguyên ngữ cảnh đoạn giới thiệu manga trước khi xử lý `00-he-thong-ten-goi-002.jsonl`.
