# Yu-Gi-Oh! WC2008 — C02 Duel Dialogue QA

- Dữ liệu: `C_THOAI_DUEL_03.csv` và `C_THOAI_DUEL_04.csv`, **250 câu mỗi tệp**; cột `tieng_Viet_MOI` đã điền đủ **500/500**.
- **196 câu** được viết lại từ bản tham khảo, **304 câu** đối chiếu và giữ.
- Giữ nguyên `key`, câu tiếng Anh, `tieng_Viet_hien_tai`, `toi_da_ky_tu`, tên lá; chỉ thay đổi `tieng_Viet_MOI`.
- QA nghiêm ngặt trên C02: **0** vượt giới hạn; **0** mất/đổi token trò chơi; **0** sai số lượng mã `\\n` / `\\r`; **0** thay đổi cột nguồn.
- `check_import.py` trên A01–26, B01–11, C01–04: **4.627/4.627 câu hợp lệ**, còn **1** cảnh báo gốc từ B05 `story|1486|0` (3 ký hiệu xuống dòng, hiển thị 7/8, thô 10/8).
- Tính từ toàn bộ nguồn **8.156** câu, số có bản Việt mới trong cột kết quả **4.627**; còn **3.529 câu** chưa dịch mới; riêng C đã có **1.000/1.962**, còn **962**.
- Đây là QA kỹ thuật và đối chiếu câu; **chưa thử ROM** hay phê duyệt cuối toàn bộ ngữ nghĩa.

Danh sách 196 câu đã thay đổi: `QA/C02_CHI_TIET_DA_SUA.csv`. Bảng đối chiếu đủ 500 câu và checkpoint ZIP tự chứa nằm trong bản bàn giao ChatGPT.
