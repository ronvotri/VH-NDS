# Magician’s Quest: Mysterious Times — Việt hóa Nintendo DS

**Checkpoint mới nhất: 022 (07/11/2026) — 7.625/55.976 mục (13,62%).** Đợt 022 dịch thêm **240 trang NPC** (`0025.002`: 120, `0025.003`: 120). Xem `CHECKPOINT-2026-11-07-DOT-22.md` và `QA-022.md`.

**Repository chung:** https://github.com/ronvotri/VH-NDS/tree/main/Magicians-Quest-Mysterious-Times

## Quy tắc

- Văn phong tiếng Việt tự nhiên, dí dỏm vừa phải, không nhồi meme; nhân vật đồng trang lứa dùng **tớ–cậu**. Giữ mỗi NPC có một nét riêng.
- Thuật ngữ: **The Emporium → Bách Hóa Tổng Hợp**, **Lovers Point → Điểm Hẹn Hò**.
- Chỉ sửa `vi`. Không động vào `id`, `en`, `ctx`, thứ tự và mã kỹ thuật (`$500;`, `$503'...;`, `$019`, `$024`, `$023`, `$022`, `$000`...).

## Đợt 022

- `translation/04-thoai/talkfigs__0eng__data__0025.002.jsonl` — 120 trang.
- `translation/04-thoai/talkfigs__0eng__data__0025.003.jsonl` — 120 trang.
- `vi_0025_002.txt` / `vi_0025_003.txt` là bản dịch tay, một trang mỗi dòng; `manual_0025_002.tsv` / `manual_0025_003.tsv` chứa ID / EN / VI.
- `apply_022.py` tái áp dụng vào baseline 021; `qa_022.py` kiểm tra 501 JSONL; `DELTA-022.jsonl` lưu 240 thay đổi.

**QA PASS:** 501 tệp / 55.976 mục; 240 trường `vi` mới, không ghi đè dữ liệu cũ. **Chưa kiểm thử thực tế trong ROM NDS**; ZIP không chứa ROM thương mại.

**Đợt 023:** `0025.004` (120 trang), `0025.005` (83 trang).