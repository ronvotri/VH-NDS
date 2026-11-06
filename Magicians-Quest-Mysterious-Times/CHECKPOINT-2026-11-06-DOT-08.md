# Magician’s Quest: Mysterious Times — Checkpoint Việt hóa 008

**Ngày:** 06/11/2026  
**GitHub:** `ronvotri/VH-NDS` → `Magicians-Quest-Mysterious-Times/`  
**Baseline:** checkpoint 007, **4.272/55.976** mục  
**Đã xử lý:** **4.450/55.976 (7,95%)**; **+178 trang hội thoại mới**.

## Tiến độ

| Nhóm | Đã xử lý | Tổng | Đợt 008 |
| --- | ---: | ---: | ---: |
| 00 — Mở đầu | 106 | 106 | 0 |
| 01 — Hệ thống | 1.086 | 1.087 | 0 |
| 02 — Vật phẩm | 1.501 | 1.501 | 0 |
| 03 — Sổ tay | 432 | 432 | 0 |
| 04 — Hội thoại | **1.325** | 52.608 | **+178** |
| 05 — Credit | 0 | 242 | 0 |
| **Tổng** | **4.450** | **55.976** | **+178** |

Ghi chú: một phần mục có `vi` là tên riêng được duyệt giữ nguyên bản gốc. Con số tổng không đồng nghĩa ROM đã Việt hóa hoàn thiện hoặc đã được kiểm thử trong game.

## Nội dung đợt 008

- `translation/04-thoai/talkfigs__0eng__data__0010.001.jsonl` — **84 trang**: các NPC lịch thiệp, mê diễn xuất, tự tin hơi quá, thích hóng chuyện, hỏi thăm, thời tiết, Giờ Bí Ẩn và sinh nhật.
- `translation/04-thoai/talkfigs__0eng__data__0011.001.jsonl` — **94 trang**: các NPC rụt rè, dễ ngại, mê sách, chờ hoàng tử, hay bệnh, sợ ma, thích sự yên bình, gặp lại bạn bè và chào theo thời gian.

Phong cách: vui nhộn, gần gũi Gen Z, có điểm nhấn như “hợp cạ”, “rối như tơ vò”, “cả rổ tin”, nhưng không làm sai nét tính cách; ngôi xưng bạn bè **tớ – cậu**, không tự ý gán giới tính hay chức vụ.

## Kiểm soát chất lượng

- **501 JSONL**, toàn bộ **55.976** mục được đối chiếu với checkpoint 007.
- **178 thay đổi**, tất cả là điền `vi` trước đó `null`; không đổi `id`, `en`, `ctx`, thứ tự, tên file hoặc trường kỹ thuật.
- So khớp toàn bộ mã `$...;` đúng thứ tự, gồm `$500;`, `$503'...;`, `$079;` và mã cử chỉ/biểu cảm `$024...`, `$023...`, `$022...`.
- Kiểm tra Unicode NFC, dấu xuống dòng `▼`, byte UTF-8 (khi nguồn khai giới hạn) và không chèn tab/CR/LF ngoài cấu trúc JSONL.
- **0 lỗi; 0 cảnh báo** dòng trên 34 ký tự sau khi lược mã biến (ngưỡng chỉ mang tính cảnh báo).
- **Chưa đo chính xác độ rộng pixel/font NDS** và chưa chạy thử trên ROM USA sạch; không coi bản patch hoàn thiện.

## Tệp nối phiên

- `manual_0010.txt` (84 dòng), `manual_0011.txt` (94 dòng): bản dịch theo thứ tự dòng nguồn.
- `apply_008.py`: chèn chính xác văn bản đích vào checkpoint 007, không sửa dữ liệu ngoài `vi`.
- `qa_008.py`: so sánh tất cả JSONL checkpoint 007 và 008, xuất `QA-008.md` và `DELTA-008.jsonl`.
- `DELTA-008.jsonl`: 178 mục EN/VI có ID/ctx để review.
- Gói ZIP checkpoint 008 chứa nguyên bộ checkpoint 007 cộng hai tệp hội thoại mới và tài liệu.

## Đợt 009

Tiếp tục hội thoại NPC còn trống, ưu tiên khảo sát các cụm `0013`–`0015` theo thứ tự và số lượng, xem từng `ctx` để giữ cá tính/xưng hô. Chỉ thêm bản dịch vào `vi: null`. Mỗi lô phải lưu ZIP, QA và cập nhật đúng thư mục `Magicians-Quest-Mysterious-Times/` trên GitHub. Không phát hành ROM bản quyền.