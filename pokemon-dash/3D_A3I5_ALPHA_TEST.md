# Pokémon Dash — thử nghiệm v0.7 Alpha 3D (04/11/2026)

**CHƯA được kiểm thử bằng giả lập/DS; không thay thế bản v0.6 ổn định.**

## Tiến triển

- Vùng dữ liệu raster trong `en/mdl_pause_title.rel` có mẫu byte phù hợp với **A3I5** (3 bit alpha cao + 5 bit chỉ số palette thấp). Đây là giả thuyết mạnh dựa trên phân bố byte; **chưa đọc được khai báo định dạng texture từ engine**.
- Thay `Back to Title` bằng `Về menu` ở bốn glyph copy / hai trạng thái trong **một mô hình**.
- ROM thử APDE kế thừa toàn bộ v0.6. Đã kiểm đúng 16 MiB, mô hình 6144 byte, 318 tài nguyên trong nested archive và patch IPS round-trip.
- **1872 byte** trong mô hình `mdl_pause_title.rel` bị thay; các tệp con khác trong archive giữ nguyên. Không thay bảng palette/pointer/header/mô hình khác.
- Chưa chạy menu tạm dừng trong trò chơi, do môi trường chưa có giả lập DS.

## Checksum

ROM v0.6 đầu vào (SHA-256): `2dd5d75336f3b3479e21bf795e7276b014d89e1fab59ec68c87760eeeba4018d`

ROM v0.7 Alpha đầu ra (SHA-256): `d592391af5d125c902545d143c3bca3bc65acc2986efdd1690c6248fd856a16d`

Đây là **test kỹ thuật**, không gọi v0.7 là bản full.

## Thử nghiệm

1. Sao lưu save; sử dụng ROM v0.6 có checksum trên.
2. Áp `patches/v06_to_v07_alpha_pause_title.ips` vào v0.6, hoặc dùng ROM Alpha đã tạo cục bộ từ ROM của chính bạn.
3. Vào một đường đua, mở **Pause**, quan sát nhãn điều hướng trở về menu: phải hiển thị **Về menu** (gồm cả trạng thái thường/chọn).
4. Kiểm tra không mất nút bấm, không biến màu, không crash khi tiếp tục hoặc rời trận.
5. Nếu lỗi, quay lại v0.6 và ghi ảnh/video lỗi.

Bản vá tương đương được tạo bằng mã Python trong gói thử nghiệm nội bộ; không đưa ROM gốc/ROM đã sửa lên GitHub.

## Kế tiếp

Sau khi xác nhận thử trong game, có thể mở rộng kỹ thuật A3I5 sang `mdl_pause_course.rel`, `mdl_t_goal.rel`, `mdl_t_timesup.rel` và các bảng tên chặng. **Không tự động vá 91 mô hình** khi chưa kiểm tra offset/palette từng mô hình.
