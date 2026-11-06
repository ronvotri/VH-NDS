# Magician’s Quest: Mysterious Times — Việt hóa Nintendo DS

Repository chung: [ronvotri/VH-NDS](https://github.com/ronvotri/VH-NDS/tree/main/Magicians-Quest-Mysterious-Times). Mỗi game nằm thư mục riêng.

**Checkpoint mới nhất: 017 (06/11/2026) — 6.525/55.976 mục (11,66%).** Đợt này dịch tay **240 trang NPC** thuộc `0023.002` và `0023.003`. Xem `CHECKPOINT-2026-11-06-DOT-17.md`.

## Văn phong & thuật ngữ

- Dịch thoại **tự nhiên, vui và tinh nghịch kiểu Gen Z**, ví dụ đã duyệt: **“Em mê tụ tập, quẩy banh nóc với bạn bè!”**. Không nhồi meme.
- Người dẫn chuyện già **ta–em**, giáo viên **thầy/cô–em**, bạn bè **tớ–cậu**, thông báo hệ thống dùng **bạn**.
- Tên địa điểm **The Emporium → Bách Hóa Tổng Hợp**, **Lovers’ Point → Điểm Hẹn Hò**; giữ màu tên với mã `$000'...;`.
- Không thay đổi tên NPC hay tự thêm giới tính nếu bản nguồn không xác định.

## Tệp đợt 017

- `translation/04-thoai/talkfigs__0eng__data__0023.002.jsonl`: 120 câu mới.
- `translation/04-thoai/talkfigs__0eng__data__0023.003.jsonl`: 120 câu mới.
- `manual_0023_002.tsv`, `manual_0023_003.tsv`: lời dịch tay từng trang.
- `apply_017.py`, `qa_017.py`: áp dịch, bảo toàn mã và kiểm tra 501 tệp với checkpoint 016.
- `DELTA-017.jsonl`, `QA-017.md`, `CHECKPOINT-2026-11-06-DOT-17.md`: nhật ký và báo cáo.

**QA: PASS, 0 lỗi**, chỉ 240 trường `vi` mới được thay; chưa thử trực tiếp trong ROM NDS. Checkpoint ZIP không chứa ROM.

**Đợt 018:** tiếp tục `0023.004` rồi `0023.005` sau khi kiểm tra số trang chưa dịch; rà các tên riêng và câu liên tục giữa các tệp trước khi điền `vi`.