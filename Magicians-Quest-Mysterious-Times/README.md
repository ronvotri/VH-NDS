# Magician's Quest: Mysterious Times (NDS) — Việt hóa tiếng Việt

Dự án con thuộc kho [ronvotri/VH-NDS](https://github.com/ronvotri/VH-NDS). Tất cả tài liệu, bảng dịch và checkpoint nằm trong thư mục riêng để không lẫn với các game khác.

## Checkpoint mới nhất: 005 (06/11/2026)

- **3.714/55.976 mục đã điền `vi`**, tăng **332** so với đợt 004.
- Mở đầu: 106/106. Hệ thống: 1.086/1.087. Vật phẩm: 1.501/1.501. Sổ tay: 432/432. Hội thoại: 589/52.608. Credit: 0/242.
- Chưa thử trực tiếp trên ROM, không khẳng định đã vá game thành công. Tên riêng được giữ nguyên có thể vẫn tính là `vi`.

## Quy ước bắt buộc

- Giọng thoại vui nhộn, thân thiện Gen Z, không cố chèn tiếng lóng. Mẫu duyệt: **“Em mê tụ tập, quẩy banh nóc với bạn bè!”**.
- Bạn cùng trang lứa: **tớ – cậu**; người dẫn chuyện lớn tuổi: **ta – em**; giáo viên: xưng theo chức danh khi xác định được vai; hệ thống trung tính.
- Không đổi ID, `en`, `ctx`, thứ tự, mã điều khiển, biến tên, ngắt trang và byte giới hạn. Chỉ bổ sung `vi` còn trống. Dịch chuỗi Nhật dự phòng phải xác minh sẽ hiển thị, không tự đoán.

## Cấu trúc

- [`CHECKPOINT-2026-11-06-DOT-05.md`](CHECKPOINT-2026-11-06-DOT-05.md): trạng thái và bước tiếp.
- [`QUY_UOC_DICH_VI.md`](QUY_UOC_DICH_VI.md): luật về ngôi xưng, thuật ngữ, tông giọng.
- [`translation/`](translation/): JSONL (trường `id`, `en`, `vi`, `ctx`, giới hạn byte khi có).
- [`DELTA-005.jsonl`](DELTA-005.jsonl): 332 cặp dịch mới để audit/ghép.
- [`mq_batch_005.py`](mq_batch_005.py), [`mq_batch_005_extra.py`](mq_batch_005_extra.py), [`mq_batch_005_more.py`](mq_batch_005_more.py): các lô lời thoại với biến ký hiệu được ghép nguyên vẹn.
- [`mq_check_005.py`](mq_check_005.py), [`QA-005.md`](QA-005.md): kiểm tra so với 004 (pass).
- `BAN_GIAO.md`, `mqpatch.py`, `mqhandoff.py`: hướng dẫn quy trình build, cần ROM sạch USA hợp pháp. Không đăng ROM thương mại.

Dịch tiếp từ **005**, không quay lại checkpoint 001–004 để dịch trùng hay ghi đè.