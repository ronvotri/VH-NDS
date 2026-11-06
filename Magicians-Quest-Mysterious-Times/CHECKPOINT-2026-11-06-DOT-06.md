# Magician’s Quest: Mysterious Times — Checkpoint Việt hóa 006

**Ngày:** 06/11/2026 · **Kho:** `ronvotri/VH-NDS` · **Thư mục:** `Magicians-Quest-Mysterious-Times/`

## Tiến độ xác minh

| Nhóm | Đã có `vi` | Tổng | Mục mới đợt 006 |
|---|---:|---:|---:|
| Mở đầu | 106 | 106 | 0 |
| Hệ thống | 1.086 | 1.087 | 0 |
| Vật phẩm | 1.501 | 1.501 | 0 |
| Sổ tay | 432 | 432 | 0 |
| Hội thoại | 957 | 52.608 | **368** |
| Credit | 0 | 242 | 0 |
| **Tổng** | **4.082** | **55.976** | **368** |

Một số mục tên riêng được giữ nguyên có trường `vi`, nên số trên là mục đã xử lý chứ không phải số chuỗi tiếng Anh đã hoàn toàn thay đổi.

## Nội dung đợt 006

Đã dịch trọn 5 cụm hội thoại gặp gỡ, lâu ngày gặp lại, chào hỏi trong ngày, trò chuyện về thời tiết, Giờ Bí Ẩn và sinh nhật:

- `talkfigs__0eng__data__0002.001.jsonl` — **75** trang: NPC thích kiếm tiền, trêu chọc, robot và các lời chào.
- `talkfigs__0eng__data__0003.001.jsonl` — **65** trang: nhóm mạnh miệng, lém lỉnh, những câu thoại hổ báo trong khuôn khổ vui vẻ.
- `talkfigs__0eng__data__0006.001.jsonl` — **61** trang: NPC lịch sự, mê đồ đẹp, đôi lúc khắt khe.
- `talkfigs__0eng__data__0007.001.jsonl` — **91** trang: NPC tốt bụng nhưng thích thử trí nhớ bằng màn giả vờ quên tên.
- `talkfigs__0eng__data__0008.001.jsonl` — **76** trang: NPC thích ca hát, mê hóng chuyện, chăm dưỡng da, nóng tính.

Các nhóm cùng trang lứa lấy `tớ – cậu` làm mặc định; robot có câu mẫu máy móc; người cá tính giữ giọng riêng nhưng không tự ý đổi vai hay dùng từ tục. Thuật ngữ `Mystery Time` nhất quán dùng **Giờ Bí Ẩn** ở phần vừa dịch.

## QA và bàn giao

- Đối chiếu 501 tệp JSONL checkpoint 005: **PASS**. Chỉ trường `vi` trước đó rỗng được bổ sung.
- Mã điều khiển `$...;`, biến tên `$500;`, `$503'...;`, giới hạn byte, Unicode NFC và ngắt `▼` giữ nguyên; không có dòng mới vượt ngưỡng cảnh báo 34 ký tự sau khi bỏ mã lệnh.
- **Chưa kiểm thử pixel-width và màn hình thật NDS**. Vẫn cần build từ ROM USA sạch hợp pháp và kiểm tra trực tiếp.
- `manual_0002.txt` ... `manual_0008.txt` (5 tệp): bản dịch thuần, theo đúng thứ tự hàng.
- `apply_006.py`: dựng lại 5 JSONL từ checkpoint 005, chỉ điền `vi` trống.
- `qa_006.py`: kiểm tra tổng thể, tạo `DELTA-006.jsonl`, `QA-006.md`.
- `DELTA-006.jsonl`: 368 bản ghi mới, chứa EN/VI và ID để tiếp nối, không lẫn các đợt.

## Mục tiếp theo — đợt 007

Tiếp tục các tệp `talkfigs__0eng__data__0004.001.jsonl` (90 mục) và `0005.001.jsonl` (100 mục), sau đó mở rộng các tuyến thoại có ngữ cảnh rõ. Không tự động dịch chuỗi Nhật dự phòng hoặc gán ngôi xưng khi chưa nhận diện vai.