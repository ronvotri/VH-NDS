# Điểm cần rà — đợt 78–79 (hoi_thoai_079–080)

1. `hoi_thoai_079` dòng 63 (`HOI_d8da3431ac7dc9`): nguồn có `{3:4}Download Quests1:2}`, thiếu dấu ngoặc mở cho thẻ đóng. Hoãn, không tự sửa mã.
2. `hoi_thoai_079` dòng 93 (`HOI_ebcbfc9a81e176`): nguồn có `3:4}and imagen...{1:2}`, thiếu dấu ngoặc mở cho thẻ đầu. Hoãn đến khi đối chiếu ROM.
3. `hoi_thoai_080` dòng 53–75: 23 chuỗi bất thường như `p`, `QQ<CTRL:01><CTRL:01>` và ký tự nửa Nhật. Chưa có căn cứ là thoại; giữ nguyên 23 ID gốc trong `DEFERRED_SOURCE_079_080.json`.
4. Tên Chuyển Sinh, Giọt Chuyển Sinh, Điểm Nice, Lồng Mang Imagen, Cống Imagen, các nút gửi/lấy/thả, mục Không Dây, Tải Về và Trao Đổi cần xem menu NDS.
5. Không mặc định dịch vụ không dây hiện còn hoạt động; đây chỉ là văn bản lời thoại.
6. Giữ tên phép Cầu Nối, phím X/Y/B, trang 40 Sách Pháp Thuật, hướng Đông Nam, Mắt Bão và tên riêng.
7. Gói nguồn có đúng 80 tệp hội thoại, tệp cuối chỉ 75 dòng. Không tạo giả `hoi_thoai_081`.

**Chưa kiểm thử:** font tiếng Việt, giới hạn pixel/byte, ghép ROM và chơi thực tế.
