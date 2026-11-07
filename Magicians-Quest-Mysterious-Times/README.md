# Magician’s Quest: Mysterious Times — Việt hóa Nintendo DS

**Checkpoint mới nhất: 036 (07/11/2026) — 10.808 / 55.976 mục (19,31%).** Đợt 036 dịch thêm **240 trang thoại NPC** (`0030.005`: 120; `0031.001`: 120). Xem `CHECKPOINT-2026-11-07-DOT-36.md` và `QA-036.md`.

**Repository chung:** https://github.com/ronvotri/VH-NDS/tree/main/Magicians-Quest-Mysterious-Times

## Nguyên tắc

- Tiếng Việt tự nhiên, nghịch ngợm vừa đủ, giữ đúng tính cách nhân vật; bạn bè mặc định **tớ–cậu**. Với nhân vật nhút nhát, giữ cảm xúc mà không chế giễu.
- Thuật ngữ: **The Emporium → Bách Hóa Tổng Hợp**; **Lovers' Point → Điểm Hẹn Hò**. Tên người/NPC giữ nguyên trong token `$500;`, `$515;`, `$503'...;`.
- Chỉ thêm `vi` ở các bản ghi chưa dịch; giữ `id`, `en`, `ctx`, thứ tự và các mã như `$019'...;`, `$024'...;`, `$000'...;`, `$074;`.

## Đợt 036

- `translation/04-thoai/talkfigs__0eng__data__0030.005.jsonl`: 120 trang, trò chuyện/hẹn hò/dạo chơi, lựa chọn thời gian đến Điểm Hẹn Hò và chuyện giữ lời hứa.
- `translation/04-thoai/talkfigs__0eng__data__0031.001.jsonl`: 120 trang, một NPC nhút nhát kể về sở thích ngày nghỉ, bạn bè, các lần lỡ lời và nỗi lo làm người khác buồn.
- `vi_0030_005_raw.txt`, `vi_0031_001_raw.txt`: bản dịch tay; `vi_0030_005.txt`, `vi_0031_001.txt`: có ngắt dòng; `manual_0030_005.tsv`, `manual_0031_001.tsv`: bảng đối chiếu EN–VI theo ID.
- `apply_036.py`, `qa_036.py`, `DELTA-036.jsonl`, `QA-036.md`, `CHECKPOINT-2026-11-07-DOT-36.md`.

**QA PASS:** 501 tệp JSONL / 55.976 bản ghi, 240 mục dịch mới, 10.568 mục dịch cũ giữ nguyên. **Chưa kiểm thử trong ROM NDS**. Gói ZIP không chứa ROM thương mại.

**Đợt 037:** `0031.002` (120 trang) và `0031.003` (120 trang).