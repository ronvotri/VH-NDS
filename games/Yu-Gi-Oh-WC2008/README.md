# Yu-Gi-Oh! World Championship 2008 (NDS) — Việt hóa

Dự án độc lập trong `ronvotri/VH-NDS`, KHÔNG dùng chung tập tin với Ni no Kuni, Magician's Quest hay Pokémon Dash.

## Cấu trúc
- `translations/`: các bản sửa nội dung; `A35_patch.json.zlib.b64` chứa đủ 47 cập nhật cho đợt A35 (JSON UTF-8 nén zlib, mã hóa base64).
- `glossary/`: quy tắc thuật ngữ riêng của Yu-Gi-Oh!
- `QA/`: báo cáo đối chiếu, kiểm tra token, giới hạn ký tự.
- `checkpoints/`: hướng dẫn phục hồi và nhật ký checkpoint.

## Trạng thái
- 26 CSV nhóm A chứa 2.009 mô tả đã có bản Việt; checkpoint mới nhất là **A35**, hiệu đính 47/120 dòng trong danh sách ưu tiên.
- 2.009/2.009 mô tả qua kiểm tra kỹ thuật; KHÔNG đồng nghĩa 2.009 dòng đã hoàn thiện về nghĩa.
- Nhóm B–G chưa thay đổi trong đợt A35.
- **Quan trọng:** Vì các CSV nền A34 rất lớn, commit khởi tạo này lưu bản *delta A35* và tài liệu, **chưa chứa trọn 26 CSV nền**. ZIP A35 đầy đủ được bàn giao trong cuộc trò chuyện ChatGPT; không được hiểu repo này đã chứa toàn bộ bản dịch.

Nguồn nghĩa phải là câu tiếng Anh trong game, bản tiếng Việt máy cũ chỉ để tham khảo. Giữ mã `@N`, `%d`, `%s`, `\n`, `\r` và giới hạn ký tự; tên lá bài trong dấu nháy kép giữ tiếng Anh.
