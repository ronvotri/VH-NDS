# Magician’s Quest: Mysterious Times — Việt hóa Nintendo DS

**Checkpoint mới nhất: 023 (07/11/2026) — 7.828 / 55.976 mục (13,98%).** Đợt 023 dịch thêm **203 trang NPC** (`0025.004`: 120, `0025.005`: 83). Xem `CHECKPOINT-2026-11-07-DOT-23.md` và `QA-023.md`.

**Repository chung:** https://github.com/ronvotri/VH-NDS/tree/main/Magicians-Quest-Mysterious-Times

## Nguyên tắc

- Dịch tiếng Việt tự nhiên, hài hước vừa phải, không nhồi meme. Giữ phong cách riêng từng NPC; với bạn bè đồng trang lứa dùng **tớ–cậu**.
- Thuật ngữ thống nhất: **The Emporium → Bách Hóa Tổng Hợp**, **Lovers Point → Điểm Hẹn Hò**.
- Chỉ sửa trường `vi`; giữ nguyên `id`, `en`, `ctx`, mã điều khiển, thứ tự và nhánh lựa chọn. Chừa chỗ cho biến tên `$500;`, `$515;`, `$503;`.

## Đợt 023

- `translation/04-thoai/talkfigs__0eng__data__0025.004.jsonl`: 120 trang, lời rủ chơi, học nhóm, chia tay và hẹn hò.
- `translation/04-thoai/talkfigs__0eng__data__0025.005.jsonl`: 83 trang, Điểm Hẹn Hò, chọn giờ gặp và mối quan hệ NPC.
- `vi_0025_004.txt`, `vi_0025_005.txt`: bản dịch tay từng trang; `manual_0025_004.tsv`, `manual_0025_005.tsv`: ID / English / Vietnamese.
- `apply_023.py`, `qa_023.py`, `DELTA-023.jsonl`, `QA-023.md`, `CHECKPOINT-2026-11-07-DOT-23.md` và `BAN_GIAO.md`.

**QA PASS:** 501 JSONL / 55.976 mục, chỉ 203 trường `vi` mới, không ghi đè dữ liệu cũ. **Chưa kiểm thử thực tế trên ROM NDS**. ZIP checkpoint không chứa ROM thương mại.

**Đợt 024:** tiếp tục `0026.001` (120 trang) và `0026.002` (120 trang).