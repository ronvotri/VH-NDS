# Các điểm cần rà — đợt 54–55 (`hoi_thoai_055–056`)

## Ưu tiên kiểm thử khi ghép ROM

1. **Các tên phép mới (tạm dịch):** `Cloudburst` → **Mưa Trút** (Sách Pháp Thuật trang 48); `Thunderstorm` → **Bão Sét** (trang 49); `Quake` → **Chấn Động** (trang 57); `Fortune’s Fool` → **Trò Đùa Số Phận** (trang 45). So với tên phép trong menu và hình sách, tránh lệch chức năng.
2. **Khái niệm mới:** `Dark Mist` → **Sương Đen**; `Summon` → **Triệu Hồi**; `Imagen Orb` → **Ngọc Cầu Imagen**; `Medallions` → **Huy Chương**. Cần xác minh tên hiển thị, chữ trên ảnh và menu trước phát hành.
3. **Câu đố 7 chương:** giữ số **7**, thứ tự chương, màu **đỏ/xanh**, tên chữ **Astram** và hướng dẫn hình Huy Chương. Phần đáp án nhập vào có thể vẫn dùng mã chữ gốc; cần kiểm thử đủ đáp án trước khi dịch logic so khớp.
4. **Ghi chú nguồn không phải thoại game:** đợt 54 có 6 mục nguồn chứa `(NOTE: ...)` tại vị trí **124, 125, 128, 129, 147, 148**. Đã loại những đoạn biên tập tiếng Anh khỏi phần lời thoại tiếng Việt; vẫn giữ nội dung chỉ đường thực sự được nhân vật nói. Cần đối chiếu bản gốc nếu engine thực sự hiển thị NOTE (khả năng thấp).
5. **Ngôi xưng / bối cảnh:** Sazara ↔ Oliver dùng **ta/cháu**; Viper tình cảm chân thành, không chọc cười ở cảnh suýt mất người yêu; Shizuku vui vẻ nhưng không bỡn cợt khi cứu Claude; Claude/Rachel dùng **anh/em**. Tên riêng **Shadaar**, **Jabou** được giữ khác nhau như dữ liệu DS.
6. **Địa danh:** Trail Coast, Bikini, Haven, Lâu Đài Arcano, Thung Lũng Ma, Nghĩa Địa Tàu, Hotroit, đường Morton/Crown Morton cần tra lại danh mục địa danh UI nếu phát sinh bất nhất.
7. **Dịch tay 2024:** không tìm thấy câu nguồn tiếng Anh trùng hoàn toàn với hai tệp mới; không tự chép đè từ bản khác.

## QA dữ liệu

- 360/360 câu được dịch, không hoãn; ID mới không trùng 10.299 ID cũ.
- JSONL hợp lệ, mã điều khiển như `{3:4}` và `{1:2}` giữ nguyên theo câu nguồn.
- Bố cục ký tự sơ bộ tối đa 3 dòng × 48 ký tự nhìn thấy/dòng; **chưa xác nhận số byte, glyph font Việt, độ rộng thực trên NDS**.
- **Chưa ghép ROM hoặc chạy game**; không xem bộ tệp JSONL là bản vá chơi được.
