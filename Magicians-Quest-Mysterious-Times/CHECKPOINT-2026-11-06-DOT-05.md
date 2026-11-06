# Magician’s Quest: Mysterious Times — Checkpoint Việt hóa 005

**Ngày:** 06/11/2026 · **Kho:** `ronvotri/VH-NDS` · **Thư mục:** `Magicians-Quest-Mysterious-Times/`

## Tiến độ

| Nhóm | Đã có `vi` | Tổng | Đợt 005 |
|---|---:|---:|---:|
| Mở đầu | 106 | 106 | 0 |
| Hệ thống | 1.086 | 1.087 | 0 |
| Vật phẩm | 1.501 | 1.501 | 0 |
| Sổ tay | 432 | 432 | 0 |
| Hội thoại | **589** | **52.608** | **+332** |
| Credit | 0 | 242 | 0 |
| **Tổng** | **3.714** | **55.976** | **+332** |

Lưu ý: số mục `vi` có thể bao gồm những tên riêng được duyệt giữ nguyên; không đồng nghĩa tất cả đều có bản Việt khác nguyên văn.

## Đã dịch trong đợt 005

- `translation/04-thoai/talkfigs__0eng__data__0000.001.jsonl`: 70 trang thoại gặp gỡ / sinh hoạt của nhóm NPC tự tin, thích khoe khoang.
- `translation/04-thoai/talkfigs__0eng__data__0001.001.jsonl`: 73 trang thoại của nhóm NPC rock/metal, vua tự phong, người mê bay chổi, robot.
- `translation/04-thoai/talkfigs__0eng__data__0009.001.jsonl`: 80 trang giới thiệu bạn mới, trò chuyện về đi vắng, thời tiết, sinh nhật.
- `translation/04-thoai/talkfigs__0eng__data__0012.001.jsonl`: 109 trang lời chào của chủ tiệm/nhân viên/người lớn/giáo viên, có hướng dẫn mua đồ.

**Phong cách:** “quẩy banh nóc” nhưng chỉ khi hợp cảnh; nhất quán xưng hô tớ–cậu giữa bạn đồng trang lứa; chủ tiệm / giáo viên theo quan hệ người lớn với học sinh. Chủ tiệm lịch sự có thể dùng tôi–bạn, người lớn tuổi có thể dùng ta–em/ta–cháu theo lời thoại rõ vai. Robot giữ lời nói máy móc.

## Đầu ra

- `DELTA-005.jsonl`: 332 bản ghi mới, chứa nguyên văn EN cùng bản dịch VI để soát.
- `mq_batch_005.py`, `mq_batch_005_extra.py`, `mq_batch_005_more.py`: bản dịch được gắn theo ID dòng của các tệp, thay thế đúng vị trí biến/mã.
- `mq_check_005.py`: đối chiếu checkpoint 004 → 005, ngăn ghi đè bản dịch cũ.
- `QA-005.md`: chứng cứ kiểm tra; `qa_checkpoint.py` PASS.
- ZIP 005 chứa toàn bộ nội dung của ZIP 004 và những tệp cập nhật, không yêu cầu quay lại phiên chat cũ.

## Chất lượng và giới hạn

- 501 tệp JSONL giữ số hàng, ID, nguyên bản tiếng Anh, `ctx` và toàn bộ trường trừ `vi`.
- 332 thay đổi mới nằm trong đúng 4 tệp JSONL; không sửa các mục `vi` đã có.
- Mã điều khiển `$...;`, biến tên `$500;`, `$503'...;`, mã màu và dấu `▼` không bị thay đổi cấu trúc.
- Mỗi đoạn vừa dịch sau khi bỏ mã điều khiển không có dòng văn bản dài quá 34 ký tự; **chưa thể khẳng định vừa màn hình 160 px khi chưa đo đúng font và thử ROM**.
- Không có ROM thương mại trong bản bàn giao; cần ROM Mỹ sạch hợp pháp để dựng và QA hiển thị.

## Việc tiếp theo — đợt 006

Dịch các tệp `talkfigs__0eng__data__0002.001.jsonl` đến `.0008.001.jsonl` theo nhân vật; sau đó mở rộng các trang có tuyến thoại và NPC cụ thể. Không dịch lấp chỗ trống bằng cách đoán vai; không tự ý điền những chuỗi dự phòng tiếng Nhật.