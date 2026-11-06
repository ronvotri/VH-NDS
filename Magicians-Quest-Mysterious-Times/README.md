# Magician’s Quest: Mysterious Times — Việt hóa Nintendo DS

Kho dự án: [ronvotri/VH-NDS/Magicians-Quest-Mysterious-Times](https://github.com/ronvotri/VH-NDS/tree/main/Magicians-Quest-Mysterious-Times)

**Checkpoint mới nhất: 012 (06/11/2026) — 5.377/55.976 mục, tương đương 9,61%.** Đợt này thêm 240 trang thoại `0021.002`–`0021.003` và đồng nhất tên cửa hàng **Bách Hóa Tổng Hợp** ở 6 mục đã dịch.

## Quy tắc

- Văn phong ngộ nghĩnh, gần gũi Gen Z, có miếng hài đúng bối cảnh. Màn mở đầu có câu được duyệt: “Em mê tụ tập, quẩy banh nóc với bạn bè!”.
- Tôn trọng quan hệ nhân vật: người dẫn chuyện lớn tuổi ta–em; thầy cô–em khi xác minh vai; bạn bè tớ–cậu; hệ thống dùng ngôi trung tính.
- Chỉ sửa trường `vi`; không động vào `id`, `en`, `ctx`, các mã `$...;`, dấu `▼`, chữ điều khiển, thứ tự file, cấu trúc hoặc giới hạn byte.
- Không lưu ROM thương mại lên GitHub. Bản vá cần ROM sạch bản Mỹ YNNE hợp pháp do người dùng sở hữu.

## Checkpoint và công cụ

- [CHECKPOINT-2026-11-06-DOT-12.md](CHECKPOINT-2026-11-06-DOT-12.md): tiến độ và hướng dẫn nối phiên.
- [QA-012.md](QA-012.md): kiểm thử cấu trúc 501 tệp, 55.976 bản ghi.
- `translation/04-thoai/talkfigs__0eng__data__0021.002.jsonl` và `.003.jsonl`: 240 bản dịch mới.
- `manual_0021_002.txt`, `manual_0021_003.txt`: bản gõ tay gốc.
- `DELTA-012.jsonl`: 240 bản dịch mới + 6 chỉnh thuật ngữ.
- `TERM-CORRECTIONS-012.jsonl`, `THUAT-NGU-012.md`: chuẩn hóa The Emporium → Bách Hóa Tổng Hợp.
- `apply_012.py`, `normalize_terms_012.py`, `qa_012.py`: áp và kiểm tra thay đổi so với checkpoint 011.

**Tình trạng:** QA cấu trúc đạt, **chưa kiểm thử trong ROM NDS**. Ưu tiên tiếp `0021.004` (120 trang) rồi `0021.005` (68 trang).