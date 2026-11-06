# Magician’s Quest: Mysterious Times — Việt hóa Nintendo DS

**Checkpoint mới nhất: 020 (07/11/2026) — 7.191 / 55.976 mục (12,85%).** Thêm **240 trang NPC** (`0024.003` = 120, `0024.004` = 120). Xem `CHECKPOINT-2026-11-07-DOT-20.md`, `QA-020.md`.

**Repository chung:** https://github.com/ronvotri/VH-NDS/tree/main/Magicians-Quest-Mysterious-Times

## Nguyên tắc

- Tiếng Việt tự nhiên, dí dỏm, tinh nghịch vừa phải, không cố nhồi meme. Bạn cùng lứa **tớ–cậu**, giữ giọng NPC theo hoàn cảnh.
- Thuật ngữ: **The Emporium → Bách Hóa Tổng Hợp**, **Lovers Point → Điểm Hẹn Hò**.
- Chỉ sửa `vi`, giữ nguyên `en`, `id`, `ctx`, các mã lệnh (`$500;`, `$024`, `$023`, `$022`, `$019`, `$000`...), thứ tự tệp và nhánh lựa chọn.

## Đợt 020

- `translation/04-thoai/talkfigs__0eng__data__0024.003.jsonl` — 120 trang: máy móc, điêu khắc băng, trò bàn cờ, sưu tầm bi ve, các nghiên cứu của NPC thích khoa học.
- `translation/04-thoai/talkfigs__0eng__data__0024.004.jsonl` — 120 trang: bạn bè, ăn trưa, học nhóm, uống trà, những lời mời và nhánh chọn hẹn hò/kết bạn thân.
- `vi_0024_003.txt`, `vi_0024_004.txt`: bản dịch tay theo đúng thứ tự trang; `manual_0024_003.tsv`, `manual_0024_004.tsv`: ID + English + Vietnamese.
- Công cụ/tài liệu: `apply_020.py`, `qa_020.py`, `DELTA-020.jsonl`, `QA-020.md`, `CHECKPOINT-2026-11-07-DOT-20.md`.

**QA: PASS** — đối chiếu đủ 501 JSONL và 55.976 bản ghi, 240 trường `vi` mới, không ghi đè. **Chưa kiểm thử hiển thị trong ROM NDS**, ZIP không chứa ROM thương mại.

**Đợt 021:** tiếp tục `0024.005` (74 trang) và `0025.001` (120 trang), bảo toàn mã điều khiển và ngôi xưng.