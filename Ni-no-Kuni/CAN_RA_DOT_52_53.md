# Cần rà — Đợt 52–53: hội thoại 053–054

## Câu đố bắt buộc kiểm tra khi nhập ROM
- `hoi_thoai_053` hàng 111: hướng la bàn. Giữ lời dẫn yêu cầu **tên hướng tiếng Anh viết liền** vì chưa sửa bộ so khớp đáp án. Cần kiểm thử cả tên tiếng Việt nếu thay đổi parser.
- Hàng 119: dãy số Astram và thứ tự hướng đi; giữ yêu cầu chỉ nhập số.
- Hàng 125, 143, 158: tên phép/phù văn phải thử đúng đầu vào của game.
- Hàng 152: tên Imagen chỉ gồm chữ cái, không khoảng trắng/dấu câu.
- `hoi_thoai_054` hàng 14, 17–24: mảnh câu Astram và các manh mối thời tiết.
- `hoi_thoai_054` hàng 34–41: nối số Astram **7–1, 9–7, 9–0, 8–10**, giữ nguyên các số.
- `hoi_thoai_053` hàng 034, 042, 154–157: giữ nguyên các thẻ `{3:4}`, `{1:2}` theo nguồn.

## Thuật ngữ & giao diện
- The Wizard Wars → **Đại chiến Pháp sư** (tạm thống nhất trong nhóm câu đố).
- Magic Master → **Sách Pháp Thuật**; Astram, Haven giữ nguyên.
- Puppet giữ nguyên tên phép tiếng Anh trước khi đối chiếu menu Sách Pháp Thuật.
- Faith → **Niềm Tin**; Confidence → **Tự Tin**; Heart Fragment → **Mảnh Tim**; Give Heart → **Trao Tim**; Hollowed → **Rỗng Tim**.
- Cloud Sweeper → **Chổi Lướt Mây**.
- Lockpick gun → **súng mở khóa** (cần xem hình), Silvervine Cloud Chalet → **Nhà trọ Mây Silvervine** (cần rà tên bảng hiệu), Nightmare → **Ác Mộng**.

## Kho dịch tay 2024
- Hội thoại 053: 0 câu nguồn trùng nguyên văn.
- Hội thoại 054: 1 câu nguồn `That's right!` (dịch tay: “Phải!”, dịch mới: “Chính xác!”). Dùng ngữ cảnh của cảnh để chọn, không nhập đè tự động.

## Trạng thái
360 JSONL hợp lệ, 360 ID mới và không trùng với 9.939 ID trước. Giữ đủ mã bảo vệ, tối đa 3 dòng/48 ký tự theo đếm ký tự. **Chưa nhập ROM, chưa kiểm thử giới hạn byte, font dấu, hình hiển thị hay gameplay.**
