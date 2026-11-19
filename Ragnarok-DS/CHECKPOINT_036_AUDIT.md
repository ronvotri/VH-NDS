# Ragnarok DS — Checkpoint 036 (20/11/2026)

## Dữ liệu GitHub
- PATCH-DOT001…026: **11.386 ID**.
- PATCH-DOT027: 422 ID, DOT028: 439 ID, DOT029: 275 ID.
- PATCH-DOT034: 80 ID, DOT035: 80 ID, DOT036: 80 ID.
- Tổng hợp không trùng ID: **12.762/14.616 = 87,31%**; chưa xử lý **1.854 ID**.
- Patch 030 không được nhập vì 815 ID hệ thống và credit đã xử lý từ đợt 001–002.

## Đợt 036
- File `02-vat-pham-001.jsonl`, mục **322–401** (đếm từ 1), 80 ID.
- Katar, sách, mũi tên, khiên, mũ giáp và phụ kiện đầu.
- 4 mục `Book of …` là tên Item được giữ nguyên tiếng Anh.
- QA nguồn trên ZIP: `source_rows=14616`, `translated=1376` (chỉ patch 027–029,034–036 trong ZIP), `unfinished=13240`, `errors=[]`.
- QA riêng 80 mục: trùng ID = 0; mã NDS sai = 0; đoạn chữ trên 36 ký tự giữa mã ngắt = 0.
- PATCH-DOT036 Git blob SHA: `55365e1b986ac8b6ffd0a7c9b82b7bb81b944f54` (đã so khớp ZIP byte-level).

## Phần chưa dịch
- Item: 834 ID.
- Job / Skill: 475 ID.
- Quest: 545 ID.
- Tổng: 1.854 ID.

## Cần QA sau cùng
- ZIP cục bộ KHÔNG chứa 11.386 patch 001–026, phải ghép từ GitHub để có 33 JSONL tích lũy toàn dự án.
- Chưa đo glyph/font tiếng Việt thực tế, chưa nhúng font, chưa vá ROM, chưa sửa asset chữ trong ảnh và chưa kiểm thử trên NDS.
