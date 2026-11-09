# Yu-Gi-Oh! World Championship 2008 — D01 Hướng dẫn (2026-11-09)

- Nhóm D: **649/649 câu** có bản Việt trong `tieng_Viet_MOI`; **482 câu** chỉnh khác bản máy tham khảo, **167 câu** giữ sau đối chiếu.
- Tệp: `translations/tutorial_D01/D_HUONG_DAN_01.csv` ... `07.csv`, 6 × 100 + 49 câu.
- QA từng dòng: **649/649 PASS**. Không câu nào vượt `toi_da_ky_tu`, không sai mã @N/%d/%s, không mất `\\n`/`\\r`, không thay đổi các cột nguồn.
- Đã đối chiếu riêng cả 7 tệp với nguồn `translations/source_B_to_G` trên GitHub. Chỉ cột bản Việt mới được điền.
- Tệp `check_import.py` chạy trên A+B+C+D: **6.238 hợp lệ**, một cảnh báo gốc từ B05 (`story|1486|0`, độ dài ký tự thô 10/8 nhưng hiển thị 7/8 do ba mã `\\n`). Nhóm D không có cảnh báo.
- Các thuật ngữ chuẩn: Triệu hồi, Phép, Bẫy, Mộ, Sân, Chuỗi, Bộ đếm Phép, Hiệu ứng Nhanh, Tộc và Thuộc tính; giữ tên thẻ trong ngoặc vuông.
- Tổng game hiện **6.238/8.156** câu đã có bản Việt, còn **1.918** câu ở nhóm E (240), F (1.257) và G (421).
- ZIP checkpoint D01 đầy đủ (183 file), JSON nhập game và bảng đối chiếu 649 câu cùng lịch sử sửa 482 câu được bàn giao trong ChatGPT.
- Bản dịch đã qua QA **kỹ thuật**, chưa có kiểm thử ROM hoặc duyệt nghĩa cuối toàn bộ.
- Không sửa dữ liệu A–C hay game khác trong repo.

**Tiếp theo:** nhóm E — Thuật ngữ Duel, 240 câu trong 4 CSV.
