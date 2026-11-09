# Yu-Gi-Oh! World Championship 2008 (NDS) — Việt hóa

## Đường dẫn riêng
`VH-NDS/games/Yu-Gi-Oh-WC2008/` — hoàn toàn tách khỏi các dự án Ni no Kuni, Magician's Quest và Pokémon Dash.

## Bộ dữ liệu đã đồng bộ
- **26 CSV nền A34**, nằm ở `translations/base_A34/A_MO_TA_LA_BAI_01.csv` đến `...26.csv` (2.009 mô tả).
- **47 bản sửa A35**, lưu ở `translations/A35_patch.json.zlib.b64` (JSON UTF-8 nén zlib rồi mã hóa base64).
- **Bảng thuật ngữ** trong `glossary/`, báo cáo trong `QA/` và hướng dẫn tạo checkpoint trong `checkpoints/`.

### Tạo 26 CSV checkpoint A35 từ GitHub (không cần ZIP ChatGPT)
```bash
python games/Yu-Gi-Oh-WC2008/checkpoints/apply_a35.py \
  games/Yu-Gi-Oh-WC2008/translations/base_A34 \
  out/A35
```
Chương trình tạo đủ 26 CSV với cột `tieng_Viet_MOI` đã cập nhật. Dùng `check_import.py` từ bộ bàn giao để xuất JSON và kiểm tra cấu trúc.

### Trạng thái QA
- Rà 120 dòng ưu tiên ở A35: **47 dòng viết lại**, 73 dòng đối chiếu giữ nguyên.
- **2.009/2.009** mô tả hợp lệ về mã game, độ dài và cấu trúc.
- Chưa kiểm thử ROM thực tế; chưa phải tất cả 2.009 dòng đã duyệt ngữ nghĩa cuối.
- Nhóm B–G được giữ nguyên trong ZIP đầy đủ bàn giao ChatGPT; trên repo hiện tập trung vào **nhóm A**.
- Bản ZIP checkpoint A35 gồm thêm tài liệu và nhóm B–G hiện được cung cấp trong cuộc trò chuyện.

**Quy tắc:** Dịch từ tiếng Anh gốc, giữ mã `@N`, `%d`, `%s`, `\\n`, `\\r`; không vượt `toi_da_ky_tu`, giữ nguyên tên lá bài trong dấu nháy kép, ATK/DEF/LP/Level; A-Counter không được nhầm thành thao tác loại khỏi cuộc chơi.
