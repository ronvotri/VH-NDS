# Ragnarok DS — Checkpoint 037 (20/11/2026)

## Trạng thái xác minh
- Patch 001–026: **11.386 ID**.
- Patch 027–029: **1.136 ID**.
- Patch 034–036: **240 ID**.
- Patch 037: **834 ID mới**, không trùng với 12.762 ID trên nhánh trước đó.
- Tổng cộng: **13.596/14.616 (93,02%)**, còn **1.020 ID**.
- KHÔNG sử dụng patch 030: 815 dòng hệ thống và credit của đợt đó đã có trong patch 001–002.

## Hoàn tất nhóm Item
- File: `02-vat-pham-001.jsonl`, **1.074/1.074 ID** đã xử lý.
- Đợt 034–036 đã xử lý 240 mục 162–401; đợt 037 bổ sung **834 mục** ở các vùng 1–161 và 402–1074.
- Trong 834 mục mới, **228 mục Việt hóa khác tiếng Anh gốc**, **606 mục giữ nguyên** vì là tên Item, Card, quái vật, nhãn chỉ số hoặc thuật ngữ game.
- Nội dung mới: hiệu ứng Card, giáp và phụ kiện, vật phẩm cốt truyện, bản đồ, thông báo sử dụng Item, nguyên liệu và tên quái.
- Tên Item/Job/Skill/quái và các thuật ngữ quan trọng giữ bằng tiếng Anh theo quy ước dự án.

## QA
- Patch 037: **834 ID duy nhất**, 0 xung đột ID với 001–029, 034–036 (đối chiếu 30+6 file patch trực tiếp từ GitHub).
- Giữ nguyên mã điều khiển `<Cxxxx>` theo đúng thứ tự: **0 lỗi**.
- Giữ nguyên placeholder `キャラクター名`, `○○`, chuỗi định dạng `%...`: **0 lỗi**.
- Không có mảnh mới dài hơn 36 ký tự Unicode giữa hai mã ngắt: **0 cảnh báo**.
- Bộ kiểm tra `tools/check_handoff.py` chạy với 33 JSONL nguồn/đích trong ZIP bàn giao: `source_rows=14616`, `translated=2210` (chỉ 027–029,034–037), `unfinished=12406`, `errors=[]`.
- GitHub blob SHA patch 037: `b44295c8d02d7c2de65310d07dc8d594c236b149`; đã xác minh khớp byte-level với patch trong ZIP.
- 11.386 bản dịch 001–026 không nằm trong 33 JSONL của ZIP; chúng có trên GitHub và cần được ghép lại khi muốn xuất bản tích lũy hoàn chỉnh.

## Còn lại
- `03-nghe-ky-nang-001.jsonl`: **475** mục Job/Skill.
- `04-nhiem-vu-001.jsonl`: **545** mục Quest.
- Tổng còn thiếu: **1.020** mục.
- Chưa nhúng font tiếng Việt, chưa vá ROM, chưa kiểm thử hiển thị thực tế trên NDS và chưa sửa asset chữ vẽ trực tiếp trong ảnh.
