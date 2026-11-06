# Magician’s Quest: Mysterious Times — Việt hóa Nintendo DS

**Checkpoint mới nhất: 018 (07/11/2026) — 6.711 / 55.976 mục (11,99%).** Thêm **186 trang NPC** (`0023.004` = 120, `0023.005` = 66). Đọc `CHECKPOINT-2026-11-07-DOT-18.md` và `QA-018.md`.

**Repository chung:** https://github.com/ronvotri/VH-NDS/tree/main/Magicians-Quest-Mysterious-Times

## Nguyên tắc

- Giọng tự nhiên, tinh nghịch, có nét hài Gen Z nhưng không nhồi meme. Bạn cùng lứa **tớ–cậu**; người lớn/giáo viên theo đúng vai; không tự thêm giới tính.
- Thuật ngữ: **The Emporium → Bách Hóa Tổng Hợp**, **Lovers Point → Điểm Hẹn Hò**.
- Chỉ thay trường `vi`, giữ bất biến trường `en`, `id`, `ctx`, thứ tự tệp, các mã lệnh `$019`, `$500`, `$515`, `$079`, `$024`/`$023`/`$022`, màu `$000` và nhánh lựa chọn.

## Tệp đợt 018

- `translation/04-thoai/talkfigs__0eng__data__0023.004.jsonl`: 120 trang mới.
- `translation/04-thoai/talkfigs__0eng__data__0023.005.jsonl`: 66 trang mới.
- `vi_0023_004.txt`, `vi_0023_005.txt`: bản dịch tay; `manual_0023_004.tsv`, `manual_0023_005.tsv`: đối chiếu ID.
- `apply_018.py`, `qa_018.py`, `DELTA-018.jsonl`, `QA-018.md`, `CHECKPOINT-2026-11-07-DOT-18.md`.

**QA:** PASS, 501 tệp JSONL và 55.976 bản ghi; 186 `vi` mới, không ghi đè. **Chưa test thực tế trên ROM NDS**. ZIP là gói bàn giao văn bản/kỹ thuật, không phải ROM/patch.

**Đợt 019:** khảo sát `0024.001` và nhóm tiếp theo.