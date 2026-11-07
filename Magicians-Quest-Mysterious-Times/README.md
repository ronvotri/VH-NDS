# Magician’s Quest: Mysterious Times — Việt hóa Nintendo DS

**Checkpoint mới nhất: 034 (07/11/2026) — 10.328 / 55.976 mục (18,45%).** Đợt 034 dịch thêm **240 trang thoại NPC** (`0030.001`: 120; `0030.002`: 120). Xem `CHECKPOINT-2026-11-07-DOT-34.md` và `QA-034.md`.

**Repository chung:** https://github.com/ronvotri/VH-NDS/tree/main/Magicians-Quest-Mysterious-Times

## Nguyên tắc

- Tiếng Việt tự nhiên, tinh nghịch đúng tính cách nhân vật, không lạm dụng meme; bạn bè dùng **tớ–cậu**.
- Thuật ngữ: **The Emporium → Bách Hóa Tổng Hợp**; **Lovers' Point → Điểm Hẹn Hò**; tên riêng nhất quán.
- Chỉ điền `vi`, giữ nguyên `id`, `en`, `ctx`, thứ tự mục; mã biểu cảm, `$500;`, `$515;`, `$503'...;`, mã lựa chọn `$019'...;` và mã màu `$000'...;` bất biến.

## Đợt 034

- `translation/04-thoai/talkfigs__0eng__data__0030.001.jsonl`: 120 trang, NPC kể chuyện làm bánh, hoa, tình bạn, trường lớp, thói quen đãng trí và bài học về sự tự tin.
- `translation/04-thoai/talkfigs__0eng__data__0030.002.jsonl`: 120 trang, các chuyện về cư xử với bạn, học tập, công việc, nghề nghiệp, gia đình và tình yêu đầu đời.
- `vi_0030_001_raw.txt`, `vi_0030_002_raw.txt`: bản dịch thủ công; `vi_0030_001.txt`, `vi_0030_002.txt`: bản có token và ngắt dòng; `manual_0030_001.tsv`, `manual_0030_002.tsv`: đối chiếu EN/VI/ID.
- `apply_034.py`, `qa_034.py`, `DELTA-034.jsonl`, `QA-034.md`, `CHECKPOINT-2026-11-07-DOT-34.md`.

**QA PASS:** 501 tệp JSONL / 55.976 bản ghi; +240 `vi`, toàn bộ 10.088 bản dịch trước giữ nguyên. **Chưa kiểm thử hiển thị trong ROM NDS.** ZIP không chứa ROM thương mại.

**Đợt 035:** `0030.003` và `0030.004` (mỗi tệp 120 trang).