# Magician’s Quest: Mysterious Times — Việt hóa Nintendo DS

**Checkpoint mới nhất: 050 (08/11/2026) — 14.149 / 55.976 mục (25.28%).** Đợt 050 dịch thêm **240 trang NPC** (`0033.018`, `0033.019`): hiệp sĩ mất thân học Ngôn ngữ Phép thuật, bắt Manticore, vụ Griffin mất kho báu, cướp biển, Harpy luyện hát và cô bé bán diêm. Xem `CHECKPOINT-2026-11-08-DOT-50.md`, `QA-050.md`, `DELTA-050.jsonl`. **Nguồn đợt 051:** `0033.020` (120) và `0033.021` (83).

**Checkpoint mới nhất: 049 (08/11/2026) — 13.909 / 55.976 mục (24,85%).** Đợt 049 dịch thêm **240 trang NPC** (`0033.016`, `0033.017`): đoàn xiếc ma và thử thách Nhà Ma, nhạc công lang thang, ông già Noel phát quà, Chồn Gió và hiệp sĩ bị mất thân. Xem `CHECKPOINT-2026-11-08-DOT-49.md`, `QA-049.md`, `DELTA-049.jsonl`. **Nguồn đợt 050:** `0033.018`, `0033.019`.

**Checkpoint mới nhất: 048 (08/11/2026) — 13.669 / 55.976 mục (24,42%).** Đợt 048 dịch thêm **240 trang thoại NPC** (`0033.014`, `0033.015`): các trang thất lạc của Cấm Thư, Halloween cho kẹo, cổng thời gian và cuộc gặp hiệu trưởng đời trước, Ác Mộng và lợn vòi ăn giấc mơ. Xem `CHECKPOINT-2026-11-08-DOT-48.md`, `QA-048.md`, `DELTA-048.jsonl`. Nguồn đợt 049: `0033.016`, `0033.017`.

**Checkpoint mới nhất: 047 (07/11/2026) — 13.429 / 55.976 mục (23,99%).** Đợt 047 dịch thêm **240 trang NPC** (`0033.012`, `0033.013`): nàng tiên cá, siren, Yeti, Cerberus, người bạn tránh mặt đám đông, khách du lịch lòng đất và Cấm Thư. Xem `CHECKPOINT-2026-11-07-DOT-47.md`, `QA-047.md`, `DELTA-047.jsonl`. Nguồn đợt 048: `0033.014`, `0033.015`.

**Checkpoint mới nhất: 046 (07/11/2026) — 13.189 / 55.976 mục (23,56%).** Đợt 046 dịch thêm **240 trang NPC** (`0033.010`, `0033.011`): quỷ khổng lồ chơi đuổi bắt, Jack Frost đi tìm ba món ăn, linh thú được triệu hồi và nàng tiên cá mất giọng. Xem `CHECKPOINT-2026-11-07-DOT-46.md`, `QA-046.md`, `DELTA-046.jsonl`. Nguồn đợt 047: `0033.012`, `0033.013`.

**Checkpoint mới nhất: 045 (07/11/2026) — 12.949 / 55.976 mục (23,13%).** Đợt 045 dịch thêm **240 trang NPC** (`0033.008`, `0033.009`): Minotaur kết thúc khóa rèn luyện, Gremlin phá máy và vụ mất tủ tại dinh thự ma do Thuyền trưởng Dot gây ra. Xem `CHECKPOINT-2026-11-07-DOT-45.md`, `QA-045.md`, `DELTA-045.jsonl`. Nguồn đợt 046: `0033.010`, `0033.011`.

**Checkpoint mới nhất: 044 (07/11/2026) — 12.709 / 55.976 mục (22,70%).** Đợt 044 dịch thêm **240 trang thoại NPC** (`0033.006` và `0033.007`, mỗi tệp 120): tượng quỷ đá tìm cách chống ngủ gật, Krampus kiểm tra trẻ ngoan, Minotaur mở trại rèn luyện. Xem `CHECKPOINT-2026-11-07-DOT-44.md`, `QA-044.md`, `DELTA-044.jsonl`.

**Checkpoint 043 (07/11/2026) — 12.469 / 55.976 mục (22,28%).** Đợt 043 dịch thêm **240 trang NPC** (`0033.004` và `0033.005`, mỗi tệp 120): rồng hồi phục, người sao Hỏa nói ngược chữ, kẻ song trùng từ thế giới gương, bùa phản phép và người sói. Xem `CHECKPOINT-2026-11-07-DOT-43.md`, `QA-043.md`, `DELTA-043.jsonl`.

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

## Đợt 040 — Lời thoại các giáo viên

- Đã dịch `0032.003` (120) và `0032.004` (120); **tổng 11.749/55.976 (20,99%)**.
- `vi_0032_003_raw.txt`, `vi_0032_004_raw.txt` là bản dịch thô. `vi_0032_003.txt`, `vi_0032_004.txt` là bản cuối có mã game và ngắt dòng; bảng EN/VI trong `manual_0032_003.tsv`, `manual_0032_004.tsv`.
- `apply_040.py`, `qa_040.py`, `QA-040.md`, `DELTA-040.jsonl`, `CHECKPOINT-2026-11-07-DOT-40.md`.
- **QA PASS:** 501 JSONL/55.976 bản ghi, chỉ thêm 240 `vi` mới, giữ 11.509 bản dịch cũ. **Chưa test trên ROM NDS**.
- Đã stage trước **hai tệp nguồn tiếng Anh chưa dịch** của đợt 041 (`0032.005`, `0033.001`) lên GitHub.

**Đợt 041 tiếp theo:** `0032.005` + `0033.001` (120 + 120 = 240 trang).

## Đợt 041

- Đã dịch `0032.005` (120 trang) và `0033.001` (120 trang), giữ tông cô–em cho giáo viên, ta–em cho các hiệu trưởng, lão–nhóc cho cướp biển.
- Có `manual_0032_005.tsv`, `manual_0033_001.tsv`, `vi_0032_005_raw.txt`, `vi_0033_001_raw.txt`, bản đã ngắt dòng, `apply_041.py`, `qa_041.py` và `DELTA-041.jsonl`.
- **QA PASS:** toàn bộ 501 tệp JSONL và 55.976 bản ghi; +240 `vi` mới, 11.749 bản dịch cũ giữ nguyên. Chưa thử ROM thực tế.

**Đợt 042:** `0033.002` và `0033.003`, dự kiến 240 trang. Nguồn hai tệp tiếp theo đã stage lên GitHub.

## Đợt 042 — Cướp biển, Nhân Sư, ông M và rồng

- Đã dịch `0033.002` và `0033.003` (**120 + 120 = 240 trang**), từ **11.989** lên **12.229/55.976 mục (21,85%)**.
- Nhân vật: cướp biển (lão–nhóc), thần hoa, Nhân Sư (ta–em), ông M/quái rương và rồng bị thương.
- `vi_0033_002_raw.txt`, `vi_0033_003_raw.txt`, `vi_0033_002.txt`, `vi_0033_003.txt`, bảng song ngữ `manual_0033_002.tsv`, `manual_0033_003.tsv`; `DELTA-042.jsonl`, `apply_042.py`, `qa_042.py`, `QA-042.md` và `CHECKPOINT-2026-11-07-DOT-42.md`.
- **QA PASS:** 501 JSONL/55.976 bản ghi, 240 mục mới, 11.989 bản dịch cũ bảo toàn. **Chưa thử ROM NDS.** ZIP không chứa ROM thương mại.
- GitHub có sẵn nguồn cho đợt 043: `0033.004` + `0033.005` (240 trang).


## Đợt 043 — Rồng, người sao Hỏa, kẻ song trùng và người sói

- Đã dịch `0033.004` (120) và `0033.005` (120), tổng **12.469/55.976 (22,28%)**.
- Giữ nguyên phép nói ngược của người sao Hỏa; đầy đủ mã lựa chọn, tên động, bùa phản phép và bộ đếm vật phẩm.
- Có bảng EN–VI, bản dịch thô, bản cuối, `apply_043.py`, `qa_043.py`, `QA-043.md`, `DELTA-043.jsonl` và `CHECKPOINT-2026-11-07-DOT-43.md`.
- **QA PASS:** 501 JSONL, 55.976 mục, 240 `vi` mới, 12.229 bản dịch cũ giữ nguyên. **Chưa thử ROM NDS**.
- Đợt 044 tiếp tục `0033.006` + `0033.007`, tổng 240 trang; bản nguồn có trong ZIP và được đưa sẵn lên GitHub.