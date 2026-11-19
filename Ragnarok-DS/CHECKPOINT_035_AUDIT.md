# Ragnarok DS — Checkpoint 035 (19/11/2026)

## Tiến độ đã xác nhận trên GitHub

- Nhánh: `vh/ragnarok-ds-usa` của `ronvotri/VH-NDS`.
- Tổng nguồn: **14.616** ID (33 JSONL).
- Patch 001–026: **11.386** ID (30 tệp).
- Patch 027–029: **1.136** ID (422 + 439 + 275), đã đồng bộ và đối chiếu SHA với ZIP.
- Patch 034: **80** ID mô tả Item.
- Patch 035: **80** ID mô tả trang bị, `02-vat-pham-001.jsonl` chỉ số gốc 241–320 (tức mục 242–321 nếu đếm từ 1).
- Tổng **12.682 ID duy nhất (86,76%)**, còn **1.934** ID chưa xử lý.

## Đối chiếu xung đột

Đã đọc trực tiếp 30 tệp patch 001–026 và 5 patch 027/028/029/034/035. Tập 1.296 ID mới không trùng với bất kỳ ID nào của 11.386 mục trước đó:
- Đối chiếu nhóm 001–006 (2.903 ID): 0 trùng.
- Đối chiếu nhóm 007–016 (3.687 ID): 0 trùng.
- Đối chiếu nhóm 017–026 (4.796 ID): 0 trùng.
- Các ID mới: 1.296 duy nhất.

**Không nhập PATCH-DOT030:** 815 ID nhóm hệ thống và credit đã dịch trong checkpoint 001–002. Giữ bản cũ, không ghi đè.

## QA

- Checkpoint 035 được chạy bằng `tools/check_handoff.py` gốc trên 33 JSONL với các patch 027–029 và 034–035 (1.296 bản dịch cục bộ): `source_rows=14616`, `translated=1296`, `errors=[]`.
- 80 mục mới có cùng thứ tự mã điều khiển NDS với nguồn, không đoạn chữ mới nào vượt 36 ký tự Unicode giữa các mã.
- Blob SHA của các patch trên GitHub khớp byte-level với ZIP:
  - 027: `08dbceca1ba7adc64a280d02d30dc9b8782ff40a`
  - 028: `5c378293dd52887cea4baba27d0ae793413b8445`
  - 029: `092a7806d64b0dc36c0d780cf6a07c8a90e97bc3`
  - 034: `efb224594694d220ac7183a6cf46bd1e31a22dc4`
  - 035: `f030199cf5d4d23d29d8078d023525cf2b743bb8`
- Chưa có ROM tiếng Việt; chưa nhúng font Việt, chưa test glyph trong giả lập hay máy NDS, chưa chỉnh text trong ảnh.
