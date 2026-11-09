# Yu-Gi-Oh! World Championship 2008 — F02 Menu / Thông báo

- Đợt F02 hoàn tất 500/500 mục: `F_MENU_THONG_BAO_03.csv` (250) và `F_MENU_THONG_BAO_04.csv` (250).
- Dịch và hiệu đính theo tiếng Anh: **444 mục mới khác với bản tham khảo**, **56 mục** đã phù hợp được giữ.
- Phạm vi: tên thử thách, thưởng DP, nhận xét đấu thủ, điều kiện mở thành tích. Giữ nguyên tên riêng lá bài trong dấu ngoặc kép, các mốc LP, số lượt, số lần triệu hồi và kích hoạt.
- QA **500/500 PASS**: 0 dòng quá giới hạn `toi_da_ky_tu`, 0 mất/đổi `@N`/`%d`/`%s`, 0 sai `\\n`/`\\r`; chỉ cột `tieng_Viet_MOI` thay đổi so với source.
- Check importer A–F02 trong checkpoint ZIP: **7.478 mục hợp lệ**, 1 cảnh báo nguồn cũ từ B05 `story|1486|0` (đã ghi nhận trước).
- Toàn bộ game: **7.478/8.156** mục có bản Việt mới, còn 678 (F 257, G 421). Các nhóm A–E và F01 giữ nguyên.
- Bảng QA: `QA/DOI_CHIEU_F02_500.csv`; những mục sửa: `QA/F02_CHI_TIET_DA_SUA.csv`.
- Checkpoint `YGO_WC2008_CHECKPOINT_F02_MENU_1000.zip` chứa 200 tệp, JSON hợp nhất và QA; được bàn giao qua ChatGPT.
- Chưa kiểm thử hiển thị trong ROM; đây là hoàn tất bản nháp có QA kỹ thuật.

Tiếp theo F03: F_MENU_THONG_BAO_05.csv và F_MENU_THONG_BAO_06.csv (257 mục) để khép lại nhóm F. Sau đó G (421 mục).
