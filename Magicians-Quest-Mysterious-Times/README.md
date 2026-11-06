# Magician’s Quest: Mysterious Times — Việt hóa Nintendo DS

Repository chung: [ronvotri/VH-NDS](https://github.com/ronvotri/VH-NDS/tree/main/Magicians-Quest-Mysterious-Times). Mỗi game nằm thư mục riêng.

**Checkpoint mới nhất: 016 (06/11/2026) — 6.285/55.976 mục (11,23%).** Đợt này dịch tay **240 trang NPC** thuộc `0022.005` và `0023.001`. Xem `CHECKPOINT-2026-11-06-DOT-16.md`.

## Văn phong & thuật ngữ

- Dịch thoại **tự nhiên, vui và tinh nghịch kiểu Gen Z**, ví dụ đã duyệt: **“Em mê tụ tập, quẩy banh nóc với bạn bè!”**. Không nhồi meme.
- Người dẫn chuyện già **ta–em**, giáo viên **thầy/cô–em**, bạn bè **tớ–cậu**, thông báo hệ thống dùng **bạn**.
- Tên địa điểm **The Emporium → Bách Hóa Tổng Hợp**, **Lovers’ Point → Điểm Hẹn Hò**; giữ màu tên với mã `$000'...;`.
- Không thay đổi tên NPC hay tự thêm giới tính nếu bản nguồn không xác định.

## Tệp đợt 016

- `translation/04-thoai/talkfigs__0eng__data__0022.005.jsonl`: 120 câu mới.
- `translation/04-thoai/talkfigs__0eng__data__0023.001.jsonl`: 120 câu mới.
- `manual_0022_005.tsv`, `manual_0023_001.tsv`: lời dịch tay từng trang.
- `apply_016.py`, `qa_016.py`: áp dịch, bảo toàn mã và kiểm tra 501 tệp với checkpoint 015.
- `DELTA-016.jsonl`, `QA-016.md`, `CHECKPOINT-2026-11-06-DOT-16.md`: nhật ký và báo cáo.

**QA: PASS, 0 lỗi**, chỉ 240 trường `vi` mới được thay; chưa thử trực tiếp trong ROM NDS. Checkpoint ZIP không chứa ROM.

**Đợt 017:** đọc và dịch tiếp `0023.002`, `0023.003` nếu có; kiểm tra ID, mã tên và đoạn thoại theo ngữ cảnh trước khi đổi `vi`.