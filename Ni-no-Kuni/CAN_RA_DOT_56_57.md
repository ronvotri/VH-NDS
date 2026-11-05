# Các điểm cần rà — đợt 56–57 (`hoi_thoai_057–058`)

## Sáu nhãn tạm hoãn (KHÔNG đưa vào hội thoại)

- `hoi_thoai_057` hàng **57**: `(Dummy) Temporary Text 1012`.
- `hoi_thoai_058` hàng **103–107**: `(Dummy) Temporary Text 8` đến `(Dummy) Temporary Text 12`.
- Cả 6 mục được giữ lại trong báo cáo QA, không tự suy đoán lời thoại để thay thế.

## Cần xác nhận trước khi đóng patch

1. `Spring Lock` → **Mở Khóa** (tên phép tạm). Kiểm tra trực tiếp giao diện bảng phép và glyph. Nhãn nguồn có `{3:4}...{1:2}` đã giữ nguyên mã.
2. `Gate` → **Mở Cổng** (theo thuật ngữ cũ). Sách Pháp Thuật chỉ dẫn khoảng **trang 21**, không đổi số trang vì đó là gợi ý người chơi.
3. `Scepter` → **Vương Trượng** (dụng cụ gãi lưng hình vương trượng ở tiệm Leila), xem nhãn và ảnh minh họa.
4. `Starey Sherry` → **Sherry Ngó Hoài** (biệt danh do người dân đặt cho cô bé hay nhìn qua cửa sổ). Dùng một dạng nhất quán trong ba đoạn lặp; kiểm tra trong ngữ cảnh phụ đề.
5. `Crown Morton`, Nhà tưởng niệm Morton, Bảo tàng Hotroit, “Hotroit Ngày Nay”, nhà nghỉ Lilli: các tên có thể xuất hiện ở biển hiệu/hình vẽ; kiểm tra để đồng bộ.
6. Truyện tuyến **Sherry – Mary – Claude – Rachel** nhạy cảm, tránh giọng bông đùa khi nhắc đến bạo hành lời nói, mất người thân và sự thu mình của Sherry; Oliver dùng tớ/cậu với bạn, cháu/cô/chú với người lớn.
7. Khi Shizuku gọi Oliver **Nhóc Mít Ướt**, xác nhận biệt danh đồng nhất với phần lời thoại đầu game.

## Soát nguồn

- Tổng **360** mục nguồn, dịch **354**, hoãn **6** nhãn thử nghiệm.
- 3 dòng nguồn tiếng Anh trùng hoàn toàn kho dịch tay 2024: `hoi_thoai_057` hàng 96; `hoi_thoai_058` hàng 18, 118. Chỉ dùng đối chiếu; không chép đè máy móc.
- Bản JSONL hợp lệ, không trùng ID với kho 10.659 mục cũ, mã điều khiển khớp; ngắt dòng sơ bộ **tối đa 3 dòng × 48 ký tự hiển thị/dòng**. Chưa xác minh độ rộng glyph thực tế hay giới hạn byte NDS.
- **Chưa ghép ROM, chưa kiểm thử font tiếng Việt, UI hoặc chạy giả lập/phần cứng.**
