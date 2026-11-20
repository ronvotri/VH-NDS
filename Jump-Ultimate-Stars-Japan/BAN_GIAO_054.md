# Jump Ultimate Stars (Japan) — Checkpoint 054

**Ngày:** 20/11/2026. **Nhánh:** `vh/jump-ultimate-stars-japan` trong `ronvotri/VH-NDS`.

## Đã dịch

- Thêm **484 chuỗi Nhật–Việt** từ `translation/00-he-thong-ten-goi-001.jsonl`, `row_index` **747–1230**, ngữ cảnh `bin/piece.bin`.
- Hoàn thành toàn bộ **tệp 00-he-thong-ten-goi-001.jsonl** từ phần CP052 + CP053 + CP054.
- Nội dung gồm **24 mục giới thiệu manga**: Shaman King, Jungle no Ouja Tar-chan, JoJo's Bizarre Adventure, Slam Dunk, Saint Seiya, Taizo Mote King Saga, The Prince of Tennis, D.Gray-man, Death Note, Dr. Slump, Lucky Man, Dragon Ball, Naruto, Ninku, Hunter × Hunter, Pyu to Fuku! Jaguar, Buso Renkin, Black Cat, Bleach, Hoshin Engi, Fist of the North Star, Bobobo-bo Bo-bobo, Majin Tantei Nogami Neuro, Midori no Makibao.
- Tên nhân vật, địa danh, Skill/thuật ngữ franchise duy trì dạng Latin/English thống nhất; phần thuyết minh dịch gần gũi, không ép ngôi xưng nhân vật khi không phải thoại.
- Tiến độ: **34.671/34.919 ID (99,29%)**; còn **248 chuỗi**.

## Kiểm thử tĩnh

- **484 ID duy nhất**, nối liền từ 747 tới 1230; chưa có bản dịch mới nào trùng ID CP001–053.
- So sánh trực tiếp với ZIP Nhật gốc SHA256 `14e839a35e75f35534a93a1b37ebe42731ea530fbc012267b45bbbed8446f241` (30 JSONL, 34.919 ID).
- Giữ nguyên `id`, `ja`, `file`, `row_index`, `group`, `context`, `uses`; Unicode NFC, không dòng trống; kiểm token điều khiển theo từng ID, bao gồm `<IDEOSP>`.
- Không có `source_fixed_field_bytes` trong lô này, nên **chưa thể chứng minh tương thích dung lượng nhị phân của ROM hoặc pixel font**. Độ dài tiếng Việt tối đa 52 Unicode codepoints trong lô 054.
- Duy trì đúng 10 đính chính CP050A trong bản gộp CP038–054 (**11.075 ID**).
- **Chưa** kiểm thử đáp án J-Quiz, chèn bản vá NDS, cỡ chữ/font hoặc rà soát thủ công toàn bộ 34.919 bản dịch.

## Chú ý nối tệp

Dòng 1230 của `00-he-thong-ten-goi-001.jsonl` kết thúc ở việc ngựa được đặt tên `Midori Makibao`; **dòng 0** của `00-he-thong-ten-goi-002.jsonl` nối tiếp câu ở nguồn Nhật (không phải đoạn giới thiệu manga mới). Bản dịch dòng 1230 cố tình không kết thúc bằng dấu chấm để dễ nối câu khi dịch CP055. Kiểm chứng trực tiếp sau khi chèn text vào ROM.

## Các tệp bàn giao

- `BAN_DICH_054.jsonl`: delta 484 bản dịch, đầy đủ metadata.
- `BAN_DICH_054.tsv`: bảng Nhật–Việt.
- `BAN_DICH_TONG_HOP_038-054.jsonl`: bản gộp 11.075 ID đã sửa CP050A.
- `NGUON_CHUA_DICH_SAU_054.jsonl`: **248 ID Nhật chưa dịch**, từ `00-he-thong-ten-goi-002.jsonl` chỉ mục 0–247.
- `QA_054.json`: kiểm tra nguồn, ID, token, checksum, số liệu, giới hạn còn mở.
- `segments.py`, `draft_054.tsv`, `make_mappings.py`, `build_cp054.py`: tư liệu dựng lại bản dịch, QA tái lập từ ZIP nguồn.

**Checkpoint 055:** dịch 248 dòng cuối tệp `00-he-thong-ten-goi-002.jsonl`, kiểm tra đủ 34.919 ID duy nhất và làm vòng QA sau khi đạt 100%; chưa gọi đó là ROM NDS đã Việt hóa hoàn chỉnh.
