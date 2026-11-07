# Magician’s Quest: Mysterious Times — Việt hóa Nintendo DS

**Checkpoint mới nhất: 029 (07/11/2026) — 9.209 / 55.976 mục (16,45%).** Đợt 029 dịch thêm **240 trang thoại NPC** (`0028.001`: 120; `0028.002`: 120). Xem `CHECKPOINT-2026-11-07-DOT-29.md` và `QA-029.md`.

**Repository chung:** https://github.com/ronvotri/VH-NDS/tree/main/Magicians-Quest-Mysterious-Times

## Nguyên tắc

- Tiếng Việt tự nhiên, tinh nghịch và hài đúng tính cách nhân vật, không lạm dụng meme; bạn bè dùng **tớ–cậu**.
- Thuật ngữ: **The Emporium → Bách Hóa Tổng Hợp**; **Lovers' Point → Điểm Hẹn Hò**; tên riêng nhất quán.
- Chỉ thêm trường `vi`; không đổi `id`, `en`, `ctx` hay thứ tự mục. Giữ nguyên mã biểu cảm, biến tên `$500;`, `$515;`, `$503'...;` và mã màu `$000'...;`.

## Đợt 029

- `translation/04-thoai/talkfigs__0eng__data__0028.001.jsonl`: 120 trang, NPC mê thời trang và ước thành minh tinh: ngày nghỉ, mua sắm, trang điểm, fan hâm mộ và các pha tự làm mình quê.
- `translation/04-thoai/talkfigs__0eng__data__0028.002.jsonl`: 120 trang, nối tiếp phong cách NPC: chuyện học, chữ rune, chọn nghề, bạn trai, thần tượng, mốt quần áo và những giấc mơ nổi tiếng.
- `vi_0028_001.txt`, `vi_0028_002.txt`: tiếng Việt đã ngắt dòng; `vi_0028_001_raw.txt`, `vi_0028_002_raw.txt`: bản dịch tay trước ngắt dòng; `manual_0028_001.tsv`, `manual_0028_002.tsv`: ID / English / Việt.
- `wrap_029.py`, `apply_029.py`, `qa_029.py`, `DELTA-029.jsonl`, `QA-029.md`, `CHECKPOINT-2026-11-07-DOT-29.md`, `BAN_GIAO.md`.

**QA PASS:** 501 tệp JSONL / 55.976 bản ghi, đúng 240 trường `vi` mới; không ghi đè các mục đã dịch. **Chưa thử hiển thị trong ROM NDS**. ZIP không chứa ROM thương mại.

**Đợt 030:** tiếp tục `0028.003` (120 trang) và `0028.004` (120 trang).