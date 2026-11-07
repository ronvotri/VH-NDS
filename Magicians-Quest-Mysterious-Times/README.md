# Magician’s Quest: Mysterious Times — Việt hóa Nintendo DS

**Checkpoint mới nhất: 035 (07/11/2026) — 10.568 / 55.976 mục (18,88%).** Đợt 035 dịch thêm **240 trang thoại NPC** (`0030.003`: 120; `0030.004`: 120). Xem `CHECKPOINT-2026-11-07-DOT-35.md` và `QA-035.md`.

**Repository chung:** https://github.com/ronvotri/VH-NDS/tree/main/Magicians-Quest-Mysterious-Times

## Nguyên tắc

- Giọng Việt tự nhiên, tinh nghịch đúng tính cách, không lạm dụng meme; bạn bè dùng **tớ–cậu**.
- Thuật ngữ: **The Emporium → Bách Hóa Tổng Hợp**; **Lovers' Point → Điểm Hẹn Hò**; tên riêng thống nhất.
- Chỉ thêm trường `vi`; giữ nguyên `id`, `en`, `ctx` và thứ tự, mã biểu cảm, tên người chơi `$500;`, `$503'...;`, mã lựa chọn `$019'...;`, mã màu `$000'...;`.

## Đợt 035

- `translation/04-thoai/talkfigs__0eng__data__0030.003.jsonl`: 120 trang, cha mẹ, bốn mùa, hoa cỏ, sách vở, chuyện câu cá, mơ ước và tình bạn.
- `translation/04-thoai/talkfigs__0eng__data__0030.004.jsonl`: 120 trang, suy nghĩ về sự tử tế, sự ngưỡng mộ, tương lai, tình bạn và các lời mời đi chơi / trà / học nhóm.
- Tệp dịch tay `vi_0030_003_raw.txt`, `vi_0030_004_raw.txt`, tệp gắn mã `vi_0030_003.txt`, `vi_0030_004.txt`, đối chiếu `manual_0030_003.tsv`, `manual_0030_004.tsv`.
- `wrap_035.py`, `apply_035.py`, `qa_035.py`, `DELTA-035.jsonl`, `QA-035.md`, `CHECKPOINT-2026-11-07-DOT-35.md`.

**QA PASS:** 501 JSONL / 55.976 bản ghi; +240 `vi`, 10.328 bản dịch trước giữ nguyên. **Chưa thử trực tiếp trong ROM NDS.** ZIP không chứa ROM thương mại.

**Đợt 036:** `0030.005` và `0031.001` (xác minh 120 trang mỗi tệp).