# Yu-Gi-Oh! World Championship 2008 (Nintendo DS) — Việt hóa

Đường dẫn riêng: `VH-NDS/games/Yu-Gi-Oh-WC2008/`. Không ghi đè các dự án `Magicians-Quest-Mysterious-Times/`, `Ni-no-Kuni/`, `pokemon-dash/`.

## Dữ liệu trong repo
- `translations/base_A34/`: **26 CSV nhóm A** (2.009 mô tả lá bài đã có bản Việt, mức A34).
- `translations/A35_patch.json.zlib.b64`: **47 bản sửa A35**, dạng JSON UTF-8 nén zlib, mã hóa base64. Các bản sửa thay thế đúng `key`; 73 dòng còn lại trong danh sách A35 đã được đối chiếu và giữ nguyên.
- `translations/source_B_to_G/`: **38 CSV nguồn nhóm B–G** (cốt truyện, thoại Duel, hướng dẫn, thuật ngữ, menu và hội thoại). Bản dịch mới trong cột `tieng_Viet_MOI` chưa được điền; không tính là phần đã hoàn thành.
- `glossary/`: bảng thuật ngữ Yu-Gi-Oh! riêng.
- `QA/`: script kiểm tra độ dài, mã và sinh JSON.
- `checkpoints/`: script phục hồi bản A35 và nhật ký.

### Tạo checkpoint A35 từ repo
```bash
python games/Yu-Gi-Oh-WC2008/checkpoints/apply_a35.py games/Yu-Gi-Oh-WC2008/translations/base_A34 out/A35
python games/Yu-Gi-Oh-WC2008/QA/check_import.py out/A35
```
Đầu ra: 26 CSV A35 và `out/A35/ket_qua_dich.json`. Các nguồn B–G được giữ nguyên trong `source_B_to_G` để dịch theo tiếng Anh gốc trong các đợt tiếp theo.

## Tiến độ và lưu ý
- A35: **120 dòng rà, 47 dòng sửa, 73 dòng giữ nguyên**.
- QA: **2.009/2.009** dòng nhóm A hợp lệ về mã và giới hạn ký tự.
- **Đây không phải bản duyệt ngữ nghĩa cuối hoặc đã thử trong ROM.**
- Chỉ sửa cột `tieng_Viet_MOI`; giữ nguyên `key`, mã `@N`, `%d`, `%s`, `\\n`, `\\r` và tên lá bài tiếng Anh.
- ATK/DEF/LP/Level giữ nguyên; Type = Tộc, Attribute = Thuộc tính; gỡ Bộ đếm không phải loại lá khỏi cuộc chơi.
- ZIP checkpoint A35 đầy đủ đã được bàn giao qua cuộc trò chuyện ChatGPT, cùng bảng so sánh và danh sách ưu tiên A36.
