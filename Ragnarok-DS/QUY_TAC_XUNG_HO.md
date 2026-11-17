# Ragnarok DS — Bảng xưng hô và cách dịch

## Nguyên tắc bắt buộc

1. **Xem trước và sau ít nhất một cảnh** trước khi ấn định ngôi xưng; kiểm tra ai nói, ai nghe, tính chất mối quan hệ và diễn biến cảm xúc.
2. **Không lấy tên gọi riêng làm căn cứ giới tính/tuổi tác.** Với `<CFFFB>` (người nói động), không điền tên nhân vật tự đoán.
3. Danh xưng nói chuyện có thể thay đổi theo tình huống. Xưng hô là **cặp quan hệ**, không phải nhãn cố định toàn game. Cặp chưa xác nhận ghi `pending-context`.
4. Với người dân, lính, chủ cửa hàng, NPC chưa rõ thông tin: lời lịch sự ngắn gọn, hạn chế cố gán anh/chị/em/ông/bà.
5. Vui vẻ, Gen Z ở nơi thích hợp; không biến cảnh đau buồn hay sinh tử thành câu đùa. Phải ưu tiên nghĩa gốc, tính cách, tính liền mạch.
6. Giữ nguyên tên riêng, Job, item, skill, quái và thuật ngữ Ragnarok chính. Vai trò *chung* (Soldier, Researcher, Girl, Adventurer) trong nhãn người nói có thể dịch sang tiếng Việt.

## Phiên cảnh mở đầu (đã đối chiếu bản tiếng Anh)

| Vai trò trong nguồn | Tên hiển thị Việt | Định hướng giọng / xưng hô | Trạng thái |
|---|---|---|---|
| Soldier | Lính | Mệnh lệnh ngắn, gắt; nói trống hoặc dùng “ngươi” với người truy đuổi | pilot |
| Researcher | Nhà nghiên cứu | “tôi/anh” khi trao đổi với Adventurer; bảo vệ cô bé, chưa xác minh quan hệ | pilot |
| Adventurer | Mạo hiểm giả | “tôi/anh” với Researcher, cứng cỏi khi đối đầu lính, lời dặn cô bé mềm hơn | pilot |
| Girl | Cô bé | Ít nói, ngập ngừng; có thể “dạ” khi đáp người lớn; chưa gán tên hay quan hệ | pilot |
| Nhân vật chính (độc thoại bên mộ) | Tên động, không tự đặt | Với mẹ “con/mẹ”, khi nhắc cha gọi “bố”; khi gặp Girl chưa rõ tuổi/quan hệ nên “tôi/cậu” tạm thời | pilot |
| Lucifi, Lisir, Viselc, Attar, Bughill, Gabera, Marie, Aldo… | Giữ nguyên tên | Chưa xác minh đủ quan hệ/ngôi xưng từ các cảnh đã rà; cần đọc mạch từng nhân vật | pending-context |

## Thuật ngữ

- Giữ: Novice, Swordsman, Magician, Wizard, Acolyte, Merchant, Knight, Priest, Guild, Job, Zeny, Prontera, Geffen, Juno, Morocc (đúng cách viết trong nguồn DS), HP/SP/ATK/DEF.
- Giữ các tên item/skill đi kèm mã màu như `<CFFF1>Clean Stone<CFFF4>`, `<CFFF2>Yusidra Caves<CFFF4>`.
- Dịch các nhãn UI mang nghĩa thường: “Save” → “Lưu”; “Continue” → “Tiếp tục”; “Touch the screen” → “Chạm vào màn hình”. 
- “Mount”, “Eq” và những nhãn ảnh còn đa nghĩa: tạm giữ gốc chờ kiểm tra giả lập, không tự khẳng định “Cưỡi/Gắn”.

## QA

- Các mã `<CFFFD>`, `<CFFFC>`, `<C3000>` và mã màu **không** phải dấu câu. Không thêm/bớt/đổi thứ tự.
- Không tự đổi dấu dòng thật; giữ nguyên nhịp tách mã và cấu trúc UI.
- Trước mỗi đợt bổ sung xưng hô, cập nhật tình trạng `pending-context / pilot / confirmed`.
- Font NDS chưa có đủ glyph tiếng Việt, nên chưa thể khẳng định chữ vừa khung.
