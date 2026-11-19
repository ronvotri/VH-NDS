# Jump Ultimate Stars — Checkpoint 047: chờ nguồn Nhật

**Chưa hoàn thành bản dịch mới. Tiến độ vẫn là 29.901 / 34.919 (85,63%), còn 5.018 chuỗi.**

- Tiếp tục từ `06-jquiz-008.jsonl`, `row_index=518`, phần *Saint Seiya*.
- File nguồn có 2.012 dòng; SHA256 từ CP046: `48c26ae8eb63b3d3272741f93683312ff435ac8fc8995479f96a42045acd0dfc`.
- Điểm nối CP046: dòng 513–517, `question_index=2490`, manga code `16`, ID cuối `JUS-9250794ffc0f5ee63d3d`.
- Nguồn Nhật gốc: `JumpUltimateStars_Japan_BanGiao_Cloud.zip`. Phiên hiện tại xác định được bản ZIP trong Library nhưng quyền xuất raw bytes bị từ chối. Repo hiện lưu các bản dịch đến CP046, không chứa file source Nhật chưa dịch.
- **Không tự dựng JA, ID hoặc `quiz_context`** từ kiến thức manga: tránh sai thứ tự quiz / hỏng dữ liệu patch.

## Khi đọc được nguồn

1. Giải nén ZIP gốc, tìm duy nhất `06-jquiz-008.jsonl` (kể cả ZIP lồng nhau), kiểm SHA256 và mốc cuối dòng 517.
2. Dịch từ dòng 518 theo trọn bộ câu hỏi, tối đa 37 Unicode codepoints mỗi câu, theo `THUAT_NGU.json` và `XUNG_HO_NHAN_VAT.md`.
3. Giữ nguyên ID, JA, metadata, `quiz_context` và token điều khiển; kiểm trùng ID CP001–046.
4. Sinh `BAN_DICH_047.jsonl`, TSV, `QA_047.json`, bản gộp CP038–047; chỉ cập nhật tiến độ README sau khi QA dữ liệu hoàn tất.
5. QA tĩnh **không đồng nghĩa** đã kiểm thử đáp án, pixel font hay ROM NDS.
