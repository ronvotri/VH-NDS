# Pokémon Dash 3D — phát hiện mới khi xem trực tiếp RelocMod

Ngày 04/11/2026. Game APDE, tiếp từ ROM Việt hóa v0.6.

## Kết quả đã xác nhận

Đã tạo được ảnh xem thử của **91 tệp `en/*.rel`** bằng cách đọc một vùng byte theo **linear 8-bit grayscale**, thường từ offset thăm dò `0x400`, chiều rộng thăm dò `256` pixel. Trên ảnh thấy rõ chữ như `Back to Title`, `Back to Course`, `GOAL!!`, `TIME'S UP!` và các tên đường đua. Một số file có nhiều bản chữ lặp do các trạng thái hiển thị khác nhau.

Đây là phát hiện về **cách quan sát dữ liệu**, chưa đủ chứng minh đây là texture pixel thô của máy DS. Không được kết luận offset `0x400` hoặc width `256` đúng cho mọi file, càng không thể coi việc thay mấy byte là an toàn trong game.

### Bằng chứng thực nghiệm

- `mdl_pause_title.rel`: xem thử `0x400`, 256×16 hiển thị `Back to Title`, có 4 bản chữ lặp (các trạng thái/bản sao cần xác minh).
- `mdl_pause_course.rel`: nhìn thấy `Back to Course`.
- `mdl_t_goal.rel`: xem `0x400`, rộng 256 px thấy `GOAL!!`.
- `mdl_t_timesup.rel`: thấy `TIME'S UP!`.
- Mẫu thử `Back to Title` → `Về menu` đã thay ảnh thô trong **bản mô hình thử**, không đổi chiều dài file. Chỉ xác minh ảnh xem trước, **chưa chèn ROM, chưa thử gameplay**.

## Bảng dịch đã thống nhất

| Chữ xuất hiện | Dịch dự kiến | Tình trạng |
| --- | --- | --- |
| Back to Title | Về menu | Preview thử, chưa vá ROM |
| Back to Course | Trở lại đường đua | Chưa vá |
| Continue | Tiếp tục | Chưa vá |
| Retry | Thử lại | Chưa vá |
| GOAL!! | VỀ ĐÍCH! | Chưa vá |
| TIME'S UP! | HẾT GIỜ! | Chưa vá |
| Replay | Phát lại | Chưa vá |
| Best Record | Kỷ lục | Chưa vá |
| Zigzag Road | Đường Zigzag | Đã duyệt cho 2D, 3D chưa vá |

**Danh sách 91 tệp:** 69 gán được gợi ý tiếng Việt từ tên cúp/đường đua đã thống nhất hoặc các nhãn đã xem, 22 chưa phân loại chắc chắn. Đây không phải số bản dịch hoàn tất.

## Tái tạo

1. Dùng công cụ `tools/audit_dash_archive.py` hoặc `tools/audit_rel_models.py` với ROM USA/APDE gốc để trích archive vào thư mục riêng.
2. Chạy `tools/rel_visual_inventory.py <thu_muc_91_file_rel> --out out` (yêu cầu Pillow và NumPy) để xuất các sheet ảnh và CSV.
3. Không đưa hình/ROM/REL sở hữu bản quyền lên GitHub; chỉ lưu công cụ và báo cáo nghiên cứu.

## Việc cần hoàn thành trước v0.7

- Chứng minh bảng pointer/relocation trỏ tới pixel buffer; xác định offset, chiều rộng, palette, UV thật cho mỗi nhóm mô hình.
- Thử một nhãn trong giả lập, kiểm tra các trạng thái bình thường/được chọn và không vỡ mô hình.
- Chỉ sau khi kiểm thử thành công mới tạo IPS/ROM v0.7.

**Trạng thái: nghiên cứu 3D có tiến triển; bản thử nghiệm ổn định vẫn là v0.6.**
