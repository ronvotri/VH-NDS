# Yu-Gi-Oh! World Championship 2008 — Checkpoint C04

**Ngày:** 09/11/2026. **Repo:** `ronvotri/VH-NDS`, dự án độc lập `games/Yu-Gi-Oh-WC2008/`.

## Kết quả

- `C_THOAI_DUEL_07.csv`: **250/250** câu có bản Việt.
- `C_THOAI_DUEL_08.csv`: **212/212** câu có bản Việt.
- Đợt C04: **462/462**, **229 câu đã sửa**, **233 câu máy cũ được đối chiếu và giữ**.
- Nhóm thoại Duel **C hoàn tất bản nháp: 1.962/1.962**.
- Tổng bản dịch mới theo nhóm: A = 2.009; B = 1.618; C = 1.962; **5.589/8.156** câu toàn dự án có bản Việt.
- **2.567** câu thuộc D–G chưa có bản Việt mới; nhóm A vẫn cần duyệt nghĩa cuối.

## QA

- **462/462** câu C04 đạt kiểm tra giới hạn ký tự `toi_da_ky_tu`, mã game và số lượng `\n`, `\r`.
- Importer của dự án xác nhận **5.589/5.589** câu đã dịch hợp lệ; **1 cảnh báo nguồn B05** `story|1486|0` (3 mã xuống dòng, thô 10/8 nhưng hiển thị 7/8). Không xóa mã gốc để ép số ký tự.
- Giữ nguyên hoàn toàn 5 cột nguồn mỗi dòng; chỉ ghi `tieng_Viet_MOI` cho C07 và C08.
- Bảng toàn bộ: `QA/DOI_CHIEU_C04_462.csv`; bảng thay đổi: `QA/C04_CHI_TIET_DA_SUA.csv`.
- JSON `ket_qua_dich.json` đã tổng hợp đúng 5.589 câu có bản Việt.
- Chưa thử hiển thị trực tiếp trong ROM; QA kỹ thuật không có nghĩa đã duyệt ngữ nghĩa cuối.

## Tiếp theo

**D01 – Hướng dẫn**: dịch toàn bộ `D_HUONG_DAN_01.csv` ... `D_HUONG_DAN_07.csv` (649 câu) nếu QA đủ. Sau đó E – Thuật ngữ, F – Menu, G – Hội thoại Duel.
