# Yu-Gi-Oh! WC2008 — Checkpoint B01 (Cốt truyện)

Ngày: 2026-11-09. Repo: `ronvotri/VH-NDS` → `games/Yu-Gi-Oh-WC2008/`.

## Từ A35 chuyển sang B01
- **300 câu mới**: `translations/story_B01/B_COT_TRUYEN_01.csv` (150) và `B_COT_TRUYEN_02.csv` (150), tiếng Việt ở cột `tieng_Viet_MOI`.
- Kiểm tra từ tiếng Anh gốc, ngôn ngữ tự nhiên theo nhân vật (thầy pháp, quái thú, robot), giữ các mã game và xuống dòng.
- Test `check_import.py` từ ZIP nguồn: **300/300 PASS**, 0 quá `toi_da_ky_tu`, 0 sai mã `@/%`, 0 sai số lượng `\\n/\\r`.
- **Tổng có bản Việt trong cột mới:** 2.309/8.156 (2.009 mô tả A35 + 300 câu B01), trong đó A chưa duyệt ngữ nghĩa toàn bộ. Cốt truyện B còn 1.318/1.618 chưa dịch mới.
- **Không sửa** 26 CSV nhóm A, không sửa 38 CSV nguồn B-G trong `translations/source_B_to_G`; hai CSV mới nằm trong thư mục story_B01 riêng.
- ZIP checkpoint B01 đầy đủ được bàn giao trong cuộc trò chuyện ChatGPT.

## Tiếp B02
Dịch `B_COT_TRUYEN_03.csv` và `B_COT_TRUYEN_04.csv` theo tiếng Anh gốc và đối chiếu file source, sau mỗi đợt lưu cả CSV mới và QA lên GitHub.
