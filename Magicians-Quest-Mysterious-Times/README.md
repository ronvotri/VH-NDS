# Magician’s Quest: Mysterious Times — Việt hóa Nintendo DS

**Checkpoint mới nhất: 021 (07/11/2026) — 7.385 / 55.976 mục (13,19%).** Đợt 021 dịch thêm **194 trang NPC** (`0024.005`: 74, `0025.001`: 120). Xem `CHECKPOINT-2026-11-07-DOT-21.md` và `QA-021.md`.

**Repository chung:** https://github.com/ronvotri/VH-NDS/tree/main/Magicians-Quest-Mysterious-Times

## Nguyên tắc

- Dịch tiếng Việt tự nhiên, hài hước vừa phải, không nhồi meme. Giữ phong cách riêng của từng NPC; giữa các bạn đồng trang lứa dùng **tớ–cậu**.
- Thuật ngữ: **The Emporium → Bách Hóa Tổng Hợp**, **Lovers Point → Điểm Hẹn Hò**.
- Chỉ sửa trường `vi`, giữ nguyên `id`, `en`, `ctx`, mã điều khiển (`$500;`, `$515;`, `$024`, `$023`, `$022`, `$034`, `$019`, `$000`...), thứ tự và nhánh chọn.

## Đợt 021

- `translation/04-thoai/talkfigs__0eng__data__0024.005.jsonl`: **74 trang**, gồm lịch hẹn, bạn bè và các cuộc trò chuyện của NPC ham học.
- `translation/04-thoai/talkfigs__0eng__data__0025.001.jsonl`: **120 trang**, lời thoại NPC xuề xòa, mê nghỉ ngơi, tự trào về sự lười và những cách giải quyết vấn đề oái oăm.
- `vi_0024_005.txt`, `vi_0025_001.txt`: bản dịch tay từng dòng; `manual_0024_005.tsv`, `manual_0025_001.tsv`: bảng ID / English / Vietnamese.
- Công cụ, kiểm thử và nhật ký: `apply_021.py`, `qa_021.py`, `DELTA-021.jsonl`, `QA-021.md`, `CHECKPOINT-2026-11-07-DOT-21.md`, `BAN_GIAO.md`.

**QA PASS:** so với checkpoint 020, kiểm tra đủ 501 JSONL / 55.976 mục, chỉ có 194 trường `vi` mới, không ghi đè dữ liệu cũ. **Chưa kiểm thử thực tế trong ROM NDS**, ZIP không chứa ROM thương mại.

**Đợt 022:** tiếp tục `0025.002` (120 trang) và `0025.003` (120 trang), giữ mã điều khiển và ngôi xưng.