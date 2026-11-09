# Yu-Gi-Oh! WC2008 — Checkpoint B03 (2026-11-09)

## Kết quả dịch
- Đợt B03: **300 câu mới** trong `translations/story_B03/B_COT_TRUYEN_05.csv` (150) và `B_COT_TRUYEN_06.csv` (150).
- Cốt truyện đã dịch: **900/1.618**, còn 718.
- Tổng có bản Việt `tieng_Viet_MOI` trong toàn bộ 8.156 câu: **2.909/8.156** (2.009 A35 + 900 phần B).
- Mô tả nhóm A35 đã qua QA kỹ thuật nhưng chưa duyệt nghĩa cuối; không sửa nhóm A trong B03.
- Đã giữ nguyên toàn bộ B01+B02, các nguồn B07-B11, C–G, cùng các game NDS khác.

## QA
- **300/300 PASS**: Không vượt `toi_da_ky_tu`, không thiếu mã @/% hoặc mã xuống dòng `\\n` / `\\r`.
- Chỉ cột `tieng_Viet_MOI` của B05 và B06 được cập nhật; `key`, tên, tiếng Anh gốc, tiếng Việt máy tham khảo và giới hạn không đổi.
- Nhật ký đối chiếu: `QA/DOI_CHIEU_COT_TRUYEN_B03_300.csv`.
- ZIP checkpoint tự chứa đầy đủ: `YGO_WC2008_CHECKPOINT_B03_COT_TRUYEN_900.zip` bàn giao trong cuộc trò chuyện.
- Chưa kiểm thử hiển thị trên ROM.

## Tiếp theo
B04: Dịch `B_COT_TRUYEN_07.csv` và `B_COT_TRUYEN_08.csv`, tiếp tục QA và commit độc lập trong thư mục Yu-Gi-Oh!.
