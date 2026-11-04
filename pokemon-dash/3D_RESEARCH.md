# Pokémon Dash — hướng nghiên cứu mô hình 3D

Cập nhật 2026-11-04.

## Định dạng thực tế

Tệp mô hình cần xử lý có magic `NITRO RelocMod 1`, không phải `BMD0` / `BTX0`. Không được sử dụng bộ chuyển đổi NSBMD/NSBTX bằng cách đổi đuôi tệp.

Trong 91 tệp `en/*.rel`:
- 88 tệp có trường version `0x200`, 3 tệp `0x400`.
- Các bảng offset/số lượng đọc được, nhưng ý nghĩa pointer/mesh/palette chưa được chứng minh.
- Nhiều chuỗi ASCII ở gần cuối tệp là **nhãn debug/material/model**, không phải văn bản gameplay. Không thay bằng tiếng Việt theo search/replace.
- Không phát hành bản v0.7 nếu chỉ sửa metadata chưa rõ tác dụng.

## Tham khảo

- [liolu/pokemon-dash-decomp](https://github.com/liolu/pokemon-dash-decomp) — dự án giải mã cùng game USA/APDE (chưa xác định bộ giải mã RelocMod tương thích).
- [scurest/apicula](https://github.com/scurest/apicula) — hỗ trợ Nitro NSBMD/BMD0, **không khẳng định** hỗ trợ RelocMod của Dash.
- [jorgecafe/nitrogen](https://github.com/jorgecafe/nitrogen) — hệ công cụ Nitro thông dụng, cần xác minh tương thích trước khi dùng.

## Hướng triển khai

1. Trích `archive.archive` theo NitroFS, kiểm tra off/size/magic; lưu hash từng tệp.
2. Xác định layout của container RelocMod, rồi tách vật liệu, tọa độ/mesh, texture/palette nếu có.
3. Render `en/mdl_pause_title.rel` và `en/mdl_t_goal.rel` thành ảnh; xác minh trên emulator.
4. Thay chữ với cùng kích thước/layout, đóng gói lại archive mà không đổi entry offsets nếu engine yêu cầu.
5. So sánh file archive mới với v0.6 và xác minh tất cả reference; phát hành IPS sau khi chạy thử.

Chưa tìm được tài liệu format đảm bảo sửa trực tiếp an toàn. Trạng thái: **nghiên cứu cấu trúc, chưa có patch 3D**.
