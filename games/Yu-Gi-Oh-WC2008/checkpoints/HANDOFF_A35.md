# Handoff A35 — 2026-11-09

**Repo**: `ronvotri/VH-NDS`, dự án `games/Yu-Gi-Oh-WC2008/`.

**Dữ liệu có thể khôi phục hoàn toàn từ repo:** `translations/base_A34` (2.009 câu nhóm A) + `translations/A35_patch.json.zlib.b64` (47 thay đổi A35), `checkpoints/apply_a35.py`, `QA/check_import.py`.

**Nguồn nhóm B–G**: 38 CSV trong `translations/source_B_to_G`, chưa có bản dịch mới. Không trộn với các thư mục game khác.

**QA A35**: 120 dòng đối chiếu; 47 dòng sửa; 73 dòng giữ nguyên; 2.009/2.009 dòng đạt kiểm tra kỹ thuật và không vượt `toi_da_ky_tu`. Chưa thử ROM.

**Tiếp theo**: A36 ưu tiên 120 mô tả nhóm A chưa được rà kỹ theo danh sách `QA/DOT_A36_UU_TIEN.csv` trong ZIP bàn giao A35; sau đó tiếp B–G.

Không gắn nhãn "đã dịch xong toàn bộ" khi mới chỉ có bản dịch nháp nhiều dòng.
