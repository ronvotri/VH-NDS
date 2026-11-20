# Jump Ultimate Stars (Japan) — Checkpoint 054 (24 manga)

**Tiến độ: 34.671 / 34.919 (99,29%)** — thêm **484 chuỗi Nhật–Việt** trong CP054; còn **248 chuỗi**.

## Mới nhất — Checkpoint 054: hoàn tất 00-he-thong-ten-goi-001 (20/11/2026)

**+484 ID mới, 34.671/34.919 ID (99,29%).** Dịch toàn bộ 24 mục giới thiệu manga còn lại trong `00-he-thong-ten-goi-001.jsonl`, dòng **747–1230**, đối chiếu trực tiếp ZIP Nhật gốc. Tệp 001 đã hoàn tất. Giữ nguyên ID/JA/context/tokens, bao gồm `<IDEOSP>`. Chưa xác minh font và patch ROM.

- [BAN_DICH_054.jsonl](BAN_DICH_054.jsonl) — 484 bản dịch mới.
- [BAN_DICH_054.tsv](BAN_DICH_054.tsv) — bảng Nhật–Việt, byte UTF-8.
- [QA_054.json](QA_054.json) / [BAN_GIAO_054.md](BAN_GIAO_054.md) — QA tĩnh và bàn giao.
- [NGUON_CHUA_DICH_SAU_054.jsonl](NGUON_CHUA_DICH_SAU_054.jsonl) — **248 ID cuối**, chỉ ở `00-he-thong-ten-goi-002.jsonl`, dòng **0–247**.
- [build_cp054.py](build_cp054.py), [make_mappings.py](make_mappings.py), [draft_054.tsv](draft_054.tsv), [segments.py](segments.py) — quy trình QA/tái dựng dữ liệu có thể kiểm tra.
- Bản gộp CP038–054 (**11.075 ID**, giữ 10 đính chính CP050A) nằm trong ZIP CP054. Trên GitHub có thể dựng từ các delta/overlay qua script.

**Checkpoint 055:** dịch 248 dòng nguồn cuối, sau đó kiểm toán toàn bộ 34.919 ID, vòng rà ngữ nghĩa và tích hợp ROM riêng. Tệp nguồn 002 bắt đầu bằng phần nối câu chuyện Makibao ở cuối tệp 001.

## Mới nhất — Checkpoint 053: hệ thống & giới thiệu manga (20/11/2026)

Hoàn thành **507 chuỗi** trong `00-he-thong-ten-goi-001.jsonl`, từ `row_index=240` đến **746**, liền mạch và đối chiếu ZIP Nhật gốc. Mảng gồm: giao tiếp DS/Wi-Fi/Deck (92); tên manga/cảnh (60); nhân vật (42); địa danh (90); đoạn giới thiệu manga (223). Đã phân biệt **Ichitaka Seto** và **Itsuki Akiba** theo glossary.

- [BAN_DICH_053.jsonl](BAN_DICH_053.jsonl) — 507 bản ghi mới, không lặp CP052.
- [BAN_DICH_053.tsv](BAN_DICH_053.tsv) — bảng Nhật–Việt và số byte UTF-8.
- [QA_053.json](QA_053.json) / [BAN_GIAO_053.md](BAN_GIAO_053.md) — QA và hướng dẫn bàn giao.
- [NGUON_CHUA_DICH_SAU_053.jsonl](NGUON_CHUA_DICH_SAU_053.jsonl) — chính xác **732 bản ghi Nhật chưa dịch**.
- [TAO_TONG_HOP_053.py](TAO_TONG_HOP_053.py) — script dựng bản gộp toàn bộ CP001–053 từ delta/overlay khi chạy trong repo. Bản gộp CP038–053 (**10.591 ID**) được đính kèm trong ZIP CP053; đã giữ 10 đính chính CP050A.

**Tiếp CP054:** `00-he-thong-ten-goi-001.jsonl`, dòng **747–1230 (484 ID)**; sau đó `00-he-thong-ten-goi-002.jsonl` **0–247 (248 ID)**. Giữ mạch giới thiệu manga, tên riêng và ngữ cảnh. Phần `00` không khai báo giới hạn byte cố định: đã QA ID/JA/token/NFC, nhưng **chưa xác minh độ rộng pixel, font hoặc patch ROM NDS**.

## Mới nhất — Checkpoint 052: nhiệm vụ + hệ thống (20/11/2026)

**+505 ID mới, 33.680/34.919 ID dịch (96,45%).** Hoàn thành 265 dòng còn sót (`row_index=184–448`) trong `03-nhiem-vu-luat-001.jsonl`, và dịch 240 dòng đầu (`row_index=0–239`) của `00-he-thong-ten-goi-001.jsonl`. Bản dịch theo ZIP Nhật gốc, giữ ID, JA, metadata, ngữ cảnh và token.

- [BAN_DICH_052.jsonl](BAN_DICH_052.jsonl) — 505 chuỗi đã dịch; không trùng checkpoint cũ.
- [BAN_DICH_052.tsv](BAN_DICH_052.tsv) — đối chiếu Nhật/Việt và byte UTF-8.
- [QA_052.json](QA_052.json) / [BAN_GIAO_052.md](BAN_GIAO_052.md) — kết quả QA/bàn giao.
- [NGUON_CHUA_DICH_SAU_052.jsonl](NGUON_CHUA_DICH_SAU_052.jsonl) — **1.239 dòng Nhật còn lại**, không tự tạo tiếng Việt.
- [TAO_TONG_HOP_052.py](TAO_TONG_HOP_052.py) — khôi phục bản gộp đầy đủ CP001–052 từ tất cả delta/overlay trên nhánh này; trong ZIP CP052 có bản gộp CP038–052 (10.084 ID).
- [BAN_DINH_CHINH_050A.jsonl](BAN_DINH_CHINH_050A.jsonl) — các đính chính cũ được bảo toàn.

**Còn lại:** 991 dòng (`00-he-thong-ten-goi-001.jsonl`, 240–1230) + 248 dòng (`00-he-thong-ten-goi-002.jsonl`, 0–247). **Tệp nhiệm vụ 03 đã dịch hết.** QA tĩnh pass cho 505 ID; 265 trường cố định đều không quá 32/44 byte. Chưa có bản vá ROM, kiểm byte cho các trường hệ thống không khai báo độ dài, QA độ rộng font hay xác minh màn hình thực tế.

## Mới nhất — Checkpoint 051: Deck + Credits (20/11/2026)

Đã mở và kiểm tra lại `JumpUltimateStars_Japan_BanGiao_Cloud.zip`: **30 tệp nguồn, 34.919 ID duy nhất**. Hoàn thành **352 chuỗi Deck** và **77 chuỗi Credits** từ nguồn Nhật, không đổi metadata gốc. Lô dịch `BAN_DICH_051.jsonl` là **429 ID mới**, khác 10 mục đính chính CP050A.

- [BAN_DICH_051.jsonl](BAN_DICH_051.jsonl) — 429 bản ghi tiếng Việt.
- [BAN_DICH_051.tsv](BAN_DICH_051.tsv) — bảng Nhật/Việt và byte UTF-8.
- [QA_051.json](QA_051.json) và [BAN_GIAO_051_DECK_CREDIT.md](BAN_GIAO_051_DECK_CREDIT.md) — QA và bàn giao bản dịch.
- [BAN_DINH_CHINH_050A.jsonl](BAN_DINH_CHINH_050A.jsonl) — 10 sửa lỗi CP050A vẫn được giữ nguyên.

**1.744 ID chưa dịch đã định vị chính xác trong ZIP nguồn:**
`00-he-thong-ten-goi-001.jsonl` (1.231); `00-he-thong-ten-goi-002.jsonl` (248); `03-nhiem-vu-luat-001.jsonl` dòng 184–448 (265). Tổng 1.231 + 248 + 265 = 1.744. Dự án chưa có patch ROM/kiểm thử font NDS. Chiều dài UTF-8 của các dòng CP051 không vượt dung lượng trường khai báo, nhưng chưa chứng minh tính tương thích mã hóa nhị phân.

## Đính chính CP050A (lịch sử sửa lỗi quiz) trong CP051 (20/11/2026)

**10 dòng sửa có xác minh; 0 ID dịch mới.** Phục hồi câu hỏi và bốn đáp án về mẹ Hiei (842–846), tách hai câu hỏi Kurama/Raizen (847–849), sửa hai tên thẻ Yu-Gi-Oh! theo nguồn chính thức (1230, 1350). Dữ liệu `ja`, `id`, `quiz_context`, thứ tự đáp án và số liệu **32.746/34.919** không đổi.

- [BAN_DINH_CHINH_050A.jsonl](BAN_DINH_CHINH_050A.jsonl) — ghi đè chỉ trường `vi` của 10 ID, không cộng ID.
- [AP_DINH_CHINH_050A.py](AP_DINH_CHINH_050A.py) — script tái tạo merged có sửa; tệp merged cũ chưa được sửa trực tiếp.
- [QA_050A.json](QA_050A.json) và [BAN_GIAO_051.md](BAN_GIAO_051.md) — QA, hướng dẫn bàn giao.

**Lưu ý lịch sử:** Đây là tình trạng ở lượt đính chính CP050A. ZIP Nhật hiện đã truy cập được, và 429 ID Deck/Credits đã được dịch trong CP051 ở mục mới nhất.

## Mới nhất — Checkpoint 050 (20/11/2026)

Nguồn Nhật: `JumpUltimateStars_Japan_BanGiao_Cloud.zip` → `translation/06-jquiz-009.jsonl`; SHA256 `ad517ab9020ebaaaf24d3b0be0bca8b6bbd1c9f975f1c3b745f1b249fd23d1e1`.

- `06-jquiz-009.jsonl`: **row_index 616–1350 (735 ID)** — hoàn tất tệp 009 và toàn bộ J-Quiz đến câu hỏi **3005**.
- Theo manga code: *Yu Yu Hakusho* **405 ID**, *Yu-Gi-Oh!* **330 ID**.
- [BAN_DICH_050.jsonl](BAN_DICH_050.jsonl) — 735 chuỗi Nhật–Việt mới, bảo toàn ID, JA và metadata.
- [BAN_DICH_050.tsv](BAN_DICH_050.tsv) — bảng đối chiếu Nhật–Việt.
- [QA_050.json](QA_050.json) — báo cáo nguồn/ID/vị trí quiz/token/SHA256 và các giới hạn chưa kiểm thử.
- [BAN_GIAO_050.md](BAN_GIAO_050.md) — hướng dẫn nối tiếp.
- [BAN_DICH_TONG_HOP_038-050.jsonl](BAN_DICH_TONG_HOP_038-050.jsonl) — **9.150 ID CP038–050**, đã giữ sửa tên Shunrei trong CP046A; không gồm CP001–037.

## Chuẩn bị Checkpoint 051 — kiểm toán ID (chưa dịch thêm)

Đã bổ sung [AUDIT_CP051.py](AUDIT_CP051.py) và cập nhật
[KIEM_TOAN_CON_LAI_051.md](KIEM_TOAN_CON_LAI_051.md) với kết quả đối chiếu
CP001–050: các dải row_index được xử lý liên tục, 26 tệp nguồn đã có
bản dịch. Cần ZIP Nhật gốc để xác định 1.744 ID nghi thuộc hai tệp
chưa được xử lý và dịch 429 ID Deck/Credits. **Tiến độ vẫn là
32.746/34.919; không có chuỗi dịch mới trong bước kiểm toán này.**

## Các nguồn còn lại — Checkpoint 051

Xem chi tiết [KIEM_TOAN_CON_LAI_051.md](KIEM_TOAN_CON_LAI_051.md), gồm:

- `07-deck-001.jsonl`: **352 dòng nguồn**.
- `08-credit-001.jsonl`: **77 dòng nguồn**.
- **1.744 dòng chênh** giữa tổng số dòng nguồn trước CP038 (**25.340**) và số ID bàn giao CP001–037 (**23.596**). Cần phục hồi CP001–037 và **so ID chính xác** để tìm vị trí thiếu; chưa tính là đã dịch.
- Tổng **352 + 77 + 1.744 = 2.173**. Khi dịch Deck và Credits, cần kiểm cả `source_fixed_field_bytes`, không áp máy móc giới hạn 37 ký tự Unicode của quiz.

## Khôi phục tiến độ

1. Khôi phục CP001–037 (**23.596 ID**) theo [PHUC_HOI_TONG_HOP_037.md](PHUC_HOI_TONG_HOP_037.md).
2. Ghép bản gộp CP038–050 (**9.150 ID**) theo ID, từ chối trùng; tổng **32.746 ID duy nhất**.
3. Áp [BAN_DINH_CHINH_037B.jsonl](BAN_DINH_CHINH_037B.jsonl) và [BAN_DINH_CHINH_037C.jsonl](BAN_DINH_CHINH_037C.jsonl) **bằng ghi đè trường `vi` theo ID**, không cộng thêm ID.
4. [BAN_DINH_CHINH_046A.jsonl](BAN_DINH_CHINH_046A.jsonl) đã được áp trong bản gộp 038–050 (tên **Shunrei**).
5. Giữ tên và xưng hô theo [THUAT_NGU.json](THUAT_NGU.json) và [XUNG_HO_NHAN_VAT.md](XUNG_HO_NHAN_VAT.md).

## QA

- **735/735** ID CP050 không trùng với CP038–049, nguyên văn JA/ID/quiz_context khớp `reference/quiz-questions.jsonl` (3.006 quiz). Giữ 5 token `<IDEOSP>`.
- Bản Việt không rỗng, không quá **37 Unicode codepoints** (dòng dài nhất đúng 37).
- Một số đáp án giữ Hán tự trong ngoặc để phân biệt chữ đồng âm ở tên địa danh/đảo.
- **Chưa xác minh đáp án đúng/sai, hình quiz, font pixel, patch ROM hoặc gameplay NDS**; những thuật ngữ hiếm cần duyệt thêm trước khi phát hành.

Repository: `ronvotri/VH-NDS`, nhánh `vh/jump-ultimate-stars-japan`, thư mục `Jump-Ultimate-Stars-Japan/`.
