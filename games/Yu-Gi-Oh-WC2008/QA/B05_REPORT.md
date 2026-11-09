# Yu-Gi-Oh! WC2008 — B05 QA

- Đã dịch thêm **300 câu** trong B09+B10, nâng cốt truyện lên **1.500/1.618**, còn **118** câu.
- Toàn game: **3.509/8.156** câu có bản Việt ở cột `tieng_Viet_MOI`, bao gồm 2.009 mô tả nhóm A35 chưa duyệt nghĩa cuối.
- **300/300** câu giữ đúng token `@N`, `%d`, `%s` và số mã `\\n`, `\\r`; `check_import.py` cho **300/300 hợp lệ, 1 cảnh báo chiều dài**.
- **299/300** câu không vượt giới hạn ký tự thô. Ngoại lệ duy nhất `story|1486|0`: nguồn đặt `toi_da_ky_tu=8` nhưng có 4 ký hiệu và ba `\\n` bắt buộc, khiến chuỗi CSV tối thiểu dài 10. Bản dịch giữ đủ ba xuống dòng, hiển thị chỉ 7 ký tự. Xem `B05_SOURCE_EXCEPTION.md`.
- Không thay đổi B01–B04, nhóm A, file nguồn gốc và game NDS khác.
- Chưa kiểm thử ROM, QA kỹ thuật không chứng nhận tất cả câu đúng nghĩa cuối.
