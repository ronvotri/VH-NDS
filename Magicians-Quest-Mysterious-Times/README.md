# Magician’s Quest: Mysterious Times — Việt hóa Nintendo DS

**Checkpoint mới nhất: 030 (07/11/2026) — 9.449 / 55.976 mục (16,88%).** Đợt 030 dịch thêm **240 trang thoại NPC** (`0028.003`: 120; `0028.004`: 120). Xem `CHECKPOINT-2026-11-07-DOT-30.md` và `QA-030.md`.

**Repository chung:** https://github.com/ronvotri/VH-NDS/tree/main/Magicians-Quest-Mysterious-Times

## Nguyên tắc

- Tiếng Việt tự nhiên, tinh nghịch và hài đúng tính cách nhân vật, không lạm dụng meme; bạn bè dùng **tớ–cậu**.
- Thuật ngữ: **The Emporium → Bách Hóa Tổng Hợp**; **Lovers' Point → Điểm Hẹn Hò**; tên riêng nhất quán.
- Chỉ thêm trường `vi`; không đổi `id`, `en`, `ctx` hay thứ tự mục. Giữ nguyên mã biểu cảm, biến tên `$500;`, `$515;`, `$503'...;`, mã lựa chọn `$019'...;` và mã màu `$000'...;`.

## Đợt 030

- `translation/04-thoai/talkfigs__0eng__data__0028.003.jsonl`: 120 trang, cô nàng mê thời trang kể chuyện phối đồ, thần tượng, quần bò cũ, thân phận người hâm mộ, bài thơ và tình bạn.
- `translation/04-thoai/talkfigs__0eng__data__0028.004.jsonl`: 120 trang, các tình huống bị hiểu lầm khi trang điểm, rủ đi chơi, uống trà, học nhóm, làm lành, hẹn tại Điểm Hẹn Hò và lời tỏ tình nhiều lựa chọn.
- `vi_0028_003.txt`, `vi_0028_004.txt`: tiếng Việt đã ngắt dòng; `vi_0028_003_raw.txt`, `vi_0028_004_raw.txt`: bản dịch tay trước ngắt dòng; `manual_0028_003.tsv`, `manual_0028_004.tsv`: ID / English / Việt.
- `wrap_030.py`, `apply_030.py`, `qa_030.py`, `DELTA-030.jsonl`, `QA-030.md`, `CHECKPOINT-2026-11-07-DOT-30.md`, `BAN_GIAO.md`.

**QA PASS:** 501 tệp JSONL / 55.976 bản ghi, đúng 240 trường `vi` mới; không ghi đè các mục đã dịch. **Chưa thử hiển thị trong ROM NDS**. ZIP không chứa ROM thương mại.

**Đợt 031:** tiếp tục `0028.005` (91 trang) và `0029.001` (120 trang).