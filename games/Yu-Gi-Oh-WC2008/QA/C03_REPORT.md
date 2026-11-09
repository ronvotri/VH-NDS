# QA C03 — Yu-Gi-Oh! World Championship 2008

- C03 xử lý **500/500 câu**, gồm 250 câu trong mỗi tệp C05 và C06.
- **236 câu sửa** từ bản Việt tham khảo; **264 câu được đối chiếu và giữ**.
- 0 câu trống, 0 câu vượt `toi_da_ky_tu`, 0 lỗi mã `@`/`%`, 0 sai số lượng mã `\\n`/`\\r`.
- Đối chiếu với CSV nguồn GitHub: tất cả cột `key`, `ten_la_bai_EN`, `tieng_Anh`, `tieng_Viet_hien_tai` và `toi_da_ky_tu` không bị thay đổi.
- Mã ký tự NEL (U+0085) trong tiếng Anh nguồn `talk|1506|0` được giữ nguyên, không nhầm với mã xuống dòng của trò chơi.
- Công cụ `check_import.py` trên toàn bộ dữ liệu đã dịch A+B+C01–C03: **5.127 câu hợp lệ**, 1 cảnh báo cũ B05 (`story|1486|0`).
- Tổng nhóm C đã có bản Việt: **1.500/1.962**, còn 462. Toàn bộ game có bản Việt: **5.127/8.156**, còn 3.029.
- Chưa kiểm thử ROM hoặc duyệt nghĩa cuối toàn bộ nội dung.

Bảng đủ 500 câu: `QA/DOI_CHIEU_C03_500.csv`. Bảng 236 câu sửa: `QA/C03_CHI_TIET_DA_SUA.csv`.
