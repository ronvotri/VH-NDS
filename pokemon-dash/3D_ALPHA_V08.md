# Pokémon Dash — v0.8 Alpha (Pause / Continue)

Ngày: 2026-11-04. **ĐÂY LÀ BẢN THỬ KỸ THUẬT, CHƯA CHƠI THỬ TRÊN DS/MELONDS.**

## Thực hiện

- Bắt đầu từ đúng **v0.7 Alpha** (kế thừa 2D v0.6).
- Vá thêm **`en/mdl_pause_tudukeru.rel`**, đổi nhãn `Continue` → **`Tiếp tục`**.
- Thay 4 ảnh chữ ở bốn trạng thái / vùng lặp; vẽ font pixel 7 hàng để tránh lỗi khi ép font thông thường, giữ dấu sắc và nặng ở mức hiển thị thử nghiệm.
- Tệp mô hình dài **4096 byte**; có **1139 byte khác bản trước**, giới hạn trong vùng raster `0x400..0xAFF`. Bảng relocation bắt đầu từ `0xB60` và không được sửa.
- **317/318 tệp khác trong archive không thay đổi**; phần model `mdl_pause_title.rel` từ v0.7 vẫn giữ nguyên.
- Tái tạo IPS từ v0.7 và IPS tích lũy từ v0.6 đều **byte-for-byte PASS**.
- Đây là dữ liệu chữ được xem thử, **không phải screenshot gameplay hay khẳng định cấu trúc texture A3I5 đã chứng minh**.

## SHA-256

- v0.6: `2dd5d75336f3b3479e21bf795e7276b014d89e1fab59ec68c87760eeeba4018d`
- v0.7 Alpha: `d592391af5d125c902545d143c3bca3bc65acc2986efdd1690c6248fd856a16d`
- v0.8 Alpha: `635353b74025daf83e9a4d0a121e24896696fa0c2e8cf644c444e60ab57f0b3b`

## GitHub

Bản vá: [patches/v07_to_v08_alpha_pause_continue.ips](patches/v07_to_v08_alpha_pause_continue.ips), Git blob SHA `66697d7f070deb8d5509d40939ecd44bd1f430b4`. **KHÔNG có ROM gốc/ROM đã chỉnh trong repo.**

Áp IPS vào **v0.7 Alpha có đúng SHA trên**. Không áp trực tiếp vào ROM gốc hoặc v0.6; gói tải riêng trong ChatGPT có bản vá tích lũy v0.6 → v0.8.

## QA cần làm trên giả lập

1. Vào trận, nhấn Pause.
2. Kiểm tra nhãn **Về menu** và **Tiếp tục**, cả màu thường/được chọn. Quan sát dấu và vị trí.
3. Thử chọn Tiếp tục / Về menu; xác nhận không crash hoặc mất điều khiển.
4. Nếu chữ không dễ đọc, ưu tiên sửa lại art pixel; nếu engine lỗi, quay về v0.6 và xem lại texture layout.

**Chưa được gọi là bản stable hoặc full 100%.** Chưa vá các model khác như `mdl_pause_retry`, `mdl_t_goal`, `mdl_t_timesup`; không được sử dụng chung vùng nhớ model từ các tệp khác mà chưa đo lại ranh giới.
