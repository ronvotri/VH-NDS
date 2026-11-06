# Magician’s Quest: Mysterious Times — Checkpoint Việt hóa 007

**Ngày:** 06/11/2026  
**GitHub:** `ronvotri/VH-NDS` → `Magicians-Quest-Mysterious-Times/`  
**Baseline:** checkpoint 006, 4.082/55.976 mục  
**Kết quả:** **4.272/55.976 mục (7,63%)**; **+190 trang hội thoại**.

## Bảng tiến độ

| Nhóm | Đã xử lý | Tổng | Đợt 007 |
|---|---:|---:|---:|
| 00 — Mở đầu | 106 | 106 | 0 |
| 01 — Hệ thống | 1.086 | 1.087 | 0 |
| 02 — Vật phẩm | 1.501 | 1.501 | 0 |
| 03 — Sổ tay | 432 | 432 | 0 |
| 04 — Hội thoại | **1.147** | 52.608 | **+190** |
| 05 — Credit | 0 | 242 | 0 |
| **Tổng** | **4.272** | **55.976** | **+190** |

*Lưu ý:* «đã xử lý» tính cả tên riêng được duyệt và giữ nguyên văn gốc; chưa có nghĩa ROM đã hoàn thành Việt hóa.

## Những phần dịch mới

- `translation/04-thoai/talkfigs__0eng__data__0004.001.jsonl`: **90 trang**, gồm lần đầu gặp, gặp lại, thời tiết, sinh nhật, người mê thời trang, nhà soạn nhạc, nhân vật thích học và các kiểu nói dí dỏm.
- `translation/04-thoai/talkfigs__0eng__data__0005.001.jsonl`: **100 trang**, gồm NPC mê ăn vặt, mê ngủ, đãng trí, thích sách, câu cửa miệng «Ộp ộp», thời tiết và Giờ Bí Ẩn.

Phong cách: lời thoại tinh nghịch, gần gũi Gen Z nhưng có sắc thái riêng, không lạm dụng meme; NPC cùng lứa dùng **tớ – cậu**. Không thêm giới tính hoặc danh xưng khi nguồn không xác định. Mã tên người chơi `$500;`/tên NPC `$503'...;` được bảo toàn.

## Bàn giao và QA

- Có **501 JSONL**, 55.976 mục gốc. Đã đối chiếu tự động từng hàng với checkpoint 006. Chỉ có **190 trường `vi` trước đó rỗng** được điền thêm; không đổi `id`, `en`, `ctx`, cấu trúc file/thứ tự mục, mã điều khiển, Unicode NFC và giới hạn byte.
- **0 lỗi** kỹ thuật; **0 dòng mới** vượt ngưỡng cảnh báo 34 ký tự (đã loại mã điều khiển). Đây chưa phải kiểm thử độ rộng pixel theo đúng font trong ROM.
- `manual_0004.txt`/`manual_0005.txt`: 190 câu đích theo thứ tự JSONL.
- `apply_007.py`: tái dựng 2 JSONL từ checkpoint 006; bảo vệ mã và ngôi xưng.
- `qa_007.py`: đối chiếu 501 tệp, kiểm tra các quy tắc kỹ thuật, xuất `QA-007.md`/`DELTA-007.jsonl`.
- `DELTA-007.jsonl`: 190 dòng thay đổi để review trực tiếp.

## Tiếp theo — đợt 008

Tiếp tục chuỗi NPC `0010.001` và `0011.001` (các nhóm nhân vật nói năng tự tin hoặc rụt rè). Soát kỹ phong cách nhân vật và các mã biến trước khi gán đại từ; giữ nguyên tệp chưa dịch. Cuối mỗi lô, chạy QA + đóng ZIP + cập nhật cùng thư mục GitHub.

**Trạng thái bản vá:** chưa dựng patch ROM hoặc test hiển thị NDS; không phân phối ROM thương mại.