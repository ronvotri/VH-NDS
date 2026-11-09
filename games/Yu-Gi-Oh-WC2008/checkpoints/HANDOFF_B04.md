# Yu-Gi-Oh! WC2008 — checkpoint B04 (2026-11-09)

- Nhánh `main`, repo `ronvotri/VH-NDS`, thư mục độc lập `games/Yu-Gi-Oh-WC2008/`.
- B04: **300 câu mới** trong `translations/story_B04/B_COT_TRUYEN_07.csv` (150) và `B_COT_TRUYEN_08.csv` (150).
- Nhóm B: **1.200/1.618** câu có bản dịch mới, còn **418**. Toàn game: **3.209/8.156** câu có bản Việt (2.009 mô tả A35 + 1.200 cốt truyện). Chưa phải số câu đã duyệt ngữ nghĩa cuối.
- QA B04: 300/300 PASS; 0 vượt `toi_da_ky_tu`, 0 sai token @/% và mã `\\n`, `\\r`.
- Chỉ sửa cột `tieng_Viet_MOI` ở B07–B08, không sửa `key`, tiếng Anh gốc, bản Việt tham khảo hay giới hạn. Mọi file trong ZIP B03 giữ nguyên byte trừ B07 và B08.
- Báo cáo đối chiếu: `QA/DOI_CHIEU_COT_TRUYEN_B04_300.csv`.
- ZIP B04 tự chứa đầy đủ A35+B01+B02+B03+B04, gồm 146 tệp, đã bàn giao trên ChatGPT.
- Tên riêng, cơ chế 3 trận liên tục, giới hạn LP, 3 trận trong thử thách 5 bộ bài và tên các lá có mã game được bảo toàn.
- Chưa kiểm thử trên ROM.

**B05 tiếp theo:** `B_COT_TRUYEN_09.csv` và `B_COT_TRUYEN_10.csv` (300 câu), đưa cốt truyện lên **1.500/1.618**, còn 118.
