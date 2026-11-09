# Yu-Gi-Oh! WC2008 — F01: Menu & Thông báo

- Ngày 2026-11-09. Repository: `ronvotri/VH-NDS`; thư mục độc lập `games/Yu-Gi-Oh-WC2008/`.
- Hai tệp CSV: `translations/menu_F01/F_MENU_THONG_BAO_01.csv`, `F_MENU_THONG_BAO_02.csv`; **250 mục mỗi tệp**.
- Điền đủ **500/500** mục vào `tieng_Viet_MOI`. Đối chiếu tiếng Anh gốc: **151 mục sửa** và **349 mục đã phù hợp được giữ**.
- QA F01: **500/500 PASS**; 0 dòng trống/vượt `toi_da_ky_tu`; 0 thay mã game `@N`, `%d/%s`; 0 sai số `\\n`, `\\r`. Năm cột dữ liệu nguồn giữ nguyên, đã kiểm tra đối chiếu bằng CSV nguồn GitHub.
- Nội dung: menu Bộ bài/Bộ bài phụ, Công thức, Danh sách Cấm/Giới hạn, đấu đơn/đấu ba ván, mạng Nintendo Wi-Fi Connection, danh sách bạn bè và trang tùy chỉnh nhân vật.
- Công cụ nhập `check_import.py` chạy trên A–E + F01: **6.978 mục hợp lệ**, có **1 cảnh báo metadata nguồn B05** (dòng `story|1486|0` có mã xuống dòng, đã ghi nhận trước).
- Tiến độ toàn game: **6.978/8.156** có bản Việt mới; còn **1.178** mục (F: 757, G: 421). Bản dịch A–E giữ nguyên; không thay đổi game khác.
- ZIP checkpoint tự chứa `YGO_WC2008_CHECKPOINT_F01_MENU_500.zip`, chứa 195 tệp, JSON nhập game cùng bảng QA, đã bàn giao trong ChatGPT.
- QA kỹ thuật đạt không có nghĩa mọi câu đã kiểm thử ROM hoặc duyệt ngữ nghĩa cuối.

Tiếp F02: `F_MENU_THONG_BAO_03.csv` và `F_MENU_THONG_BAO_04.csv` (500 mục).
