# Magician’s Quest: Mysterious Times — Việt hóa Nintendo DS

**Checkpoint mới nhất: 039 (07/11/2026) — 11.509 / 55.976 mục (20,56%).** Đợt 039 dịch thêm **240 trang NPC** (`0032.001`: 120; `0032.002`: 120), gồm bốn sự kiện theo mùa. Xem `CHECKPOINT-2026-11-07-DOT-39.md`, `QA-039.md` và `DELTA-039.jsonl`.

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

**Đợt 038:** `0031.004` (120 trang) và `0031.005` (101 trang).


## Đợt 037

+240 trang thoại `0031.002` và `0031.003`. Xem `CHECKPOINT-2026-11-07-DOT-37.md`, `QA-037.md`, `DELTA-037.jsonl`. Đợt 038: `0031.004` (120) + `0031.005` (101).

## Đợt 038

- Đã dịch `0031.004` (120 trang) và `0031.005` (101 trang), giữ giọng nhút nhát, chân thành; lời mời hẹn hò và các giờ lựa chọn đều giữ nguyên mã phân nhánh.
- `vi_0031_004_raw.txt`, `vi_0031_005_raw.txt`: bản dịch tay; `vi_0031_004.txt`, `vi_0031_005.txt`: hoàn chỉnh có mã; `manual_0031_004.tsv`, `manual_0031_005.tsv`: bảng song ngữ.
- `apply_038.py`, `qa_038.py`, `DELTA-038.jsonl`, `QA-038.md`, `CHECKPOINT-2026-11-07-DOT-38.md`.
- **QA PASS:** 501 JSONL/55.976 bản ghi, 221 trang mới, 11.048 trang cũ giữ nguyên. **Chưa thử ROM NDS**. ZIP không chứa ROM thương mại.

**Đợt 039:** `0032.001` và `0032.002` (dự kiến 240 trang).

## Đợt 039 — Sự kiện bốn mùa

- `0032.001` (120 trang): **Tiệc trà mùa xuân**, đánh giá cách tiếp khách; **Hội thi thử gan mùa hè** (Nhà Ma, phép xì hơi); mở đầu **Hội thi lẩu nấm**.
- `0032.002` (120 trang): hái nấm, lựa chọn lẩu an toàn, chấm điểm lẩu; **Lễ hội tuyết cầu vồng**, pha lê bảy màu và nghi thức chuyển mùa.
- `vi_0032_001_source.txt`, `vi_0032_002_source.txt`: bản dịch tay từng dòng; `vi_0032_001.txt`, `vi_0032_002.txt`: bản ghép mã và ngắt dòng; `manual_0032_001.tsv`, `manual_0032_002.tsv`: bảng song ngữ.
- `apply_039.py`: áp bản dịch có thể chạy lại mà không ghi đè khác biệt; `qa_039.py`: kiểm tra toàn bộ so với ZIP 038; `DELTA-039.jsonl`, `QA-039.md`, `CHECKPOINT-2026-11-07-DOT-39.md`.
- **QA PASS:** chỉ thêm 240 bản dịch, bảo toàn 11.269 bản cũ và mã điều khiển, 501 tệp JSONL, 55.976 bản ghi. **Chưa thử ROM NDS**. ZIP không chứa ROM thương mại.
- GitHub cũng lưu trước **hai tệp nguồn chưa dịch** `0032.003` và `0032.004` để phiên tiếp theo có thể tự nối tiếp nếu ZIP không đính kèm được.

**Đợt 040 tiếp theo:** `0032.003` và `0032.004` (120 + 120 = 240 trang).