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


## Đợt 002: cặp xưng hô đã rà theo nguồn

| Cảnh / cặp quan hệ | Xưng hô | Ghi chú |
|---|---|---|
| Nhân vật chính ↔ cô bé chưa rõ danh tính (Yusidra Caves) | tôi/cậu | Không tự đặt tên; vẫn giữ <CFFFB> và <CFFFA> trong dữ liệu |
| Nhân vật chính ↔ mẹ (ký ức) | con/mẹ | Nhắc cha là “bố”; cảnh nghiêm túc, không thêm meme |
| Nhân viên Kafra → người chơi | bạn | Giọng hướng dẫn lịch sự; đây là vai trò NPC chung, không mặc định một cá nhân |
| Cô bé → nhân vật chính | tôi/cậu, đôi lúc “dạ/vâng” | Nhân vật chưa hiểu nhiều khái niệm, diễn đạt ngập ngừng |

**Chưa xác minh đến hết đợt 002:** Viselc/Lisir/Lucifi và các quan hệ chưa xuất hiện trong mạch đó. Đợt 003 đã kiểm tra riêng Lucifi; Viselc và Lisir vẫn chờ ngữ cảnh. Không suy luận từ tên nhân vật.


## Đợt 003 — người nói và xưng hô đã xác minh theo cảnh

| Cặp / vai trò | Xưng hô định hướng | Lưu ý |
|---|---|---|
| Nhân vật chính ↔ cô bé | tôi/cậu | Không gán tuổi/quan hệ; mã động <CFFFB>/<CFFFA> giữ nguyên |
| Nhân vật chính → Lucifi | tôi/anh | Ngại nhận là bạn, cáu nhẹ khi bị trêu; tránh cố định đại từ giới tính |
| Lucifi → nhân vật chính, cô bé | tôi/cậu, hai cậu | Thoải mái, lầy nhưng vẫn trách nhiệm |
| Lucifi → chỉ huy | tôi/thưa ngài | Lời báo cáo trang trọng, được chuyển thành cởi mở khi ở cùng đội |
| Chỉ huy → Lucifi | ta/cậu | Quyết định phân công, tính chất cấp trên – cấp dưới |
| Nhân vật chính ↔ Olav | cháu/ông | Olav là cha nuôi Colm, tuổi cao; cảnh giúp đỡ nghiêm túc |
| Nhân vật chính → Colm (10 tuổi) | tôi/em | Không gán giới tính nhân vật chính; Colm xưng em, gọi cha là bố |
| Olav → nhóm | ông/các cháu | Cảnh xúc động, không tạo meme |

Tính cách đã xác nhận từ nguồn: **Lucifi** trêu ghẹo, tận tâm, dùng màn giả bị thương để thử đồng đội; **nhân vật chính** hay chối lòng tốt dù vẫn giúp người; **cô bé** ít hiểu khái niệm, đặc biệt chuyện bạn bè/cảm ơn; **Olav** hết lòng vì Colm. Giữ nguyên tên các đơn vị/địa danh/item: Order of Knights, Order, Prontera Culvert, Prontera Woods, West Prontera Woods, Dog Tag, White Peach, Guild.

**Kỹ thuật:** chưa kiểm tra khung thoại NDS thật. Không được sửa mã màu, dấu phân trang <CFFFC>, ngắt lời <CFFFD>, tên động <CFFFB>/<CFFFA> hoặc ID để rút ngắn văn bản.


## Đợt 004 — Mạch Geffen / Mjolnir / Emperium

- **Nhân vật chính – Lucifi:** tôi/cậu; trêu nhau về chuyện đỏ mặt, Lucifi sợ ma nhưng thật lòng lo đồng đội. Khi nghiêm túc, Lucifi khuyên đừng liều mạng để mạnh hơn.
- **Nhân vật chính – Viselc:** nhân vật chính xưng tôi, gọi anh; Viselc xưng tôi, gọi cậu, điềm đạm và lịch sự.
- **Colm – Olav:** Colm xưng con, gọi bố; nhân vật chính xưng cháu, gọi ông với Olav. Không đổi tên item White Peach.
- **Lughill – Attar:** thuộc hạ gọi Lughill là đại ca; khi bị chất vấn họ xin tha mạng, không giảm nhẹ mức độ phạm tội.
- **Dark Knight – nhân vật chính:** Dark Knight tự xưng ta, gọi nhóc/ngươi; nhân vật chính tức giận đáp ta/ngươi, khác hẳn lối tôi/cậu với Lucifi.
- **Người đàn ông bí ẩn – Dark Knight:** ta/ngươi theo quan hệ ra lệnh – thuộc hạ. Danh tính và quan hệ khác chưa được tự suy đoán.
- **Mẹ – nhân vật chính:** mẹ/con; hồi ức đau buồn giữ nghiêm túc, không thêm tiếng lóng.
- **Cô bé chưa rõ danh tính:** tôi/cậu, mô tả cảm xúc theo lời gốc; các thẻ `<CFFFA>`/`<CFFFB>` vẫn là tên động, không viết tên cố định.

Tình trạng đã qua QA cấu trúc, chưa kiểm chứng khung chữ và font Việt trên NDS thật.


## Đợt 005 — Morocc, Lisir, Popi, Frione và Emperium

- **Nhân vật chính – Lucifi:** tôi/cậu, nói đùa vừa phải; Lucifi nghiêm khi nhắc việc gây nguy hiểm cho đồng đội. Lucifi – Chỉ huy: lời kính trọng “thưa ngài”, “rõ”.
- **Nhân vật chính – Viselc:** tôi/cậu, có thể gọi Viselc là anh; đoàn buôn gọi Viselc là ngài.
- **Nhân vật chính – Lisir:** tôi/cô, tôi/cậu tùy câu gốc và giọng người nói; Lisir nóng nảy, hiếu thắng, ham tiền, nhưng những đoạn về cha mẹ mất trong Ant Hell phải nghiêm túc.
- **Yolanda:** tôi/mọi người, lời nhờ tìm Popi lịch sự; **Popi là chú chó**. Không sửa tên riêng.
- **Aldo:** tôi/cậu với Lucifi và người chơi; khi nhắc Freya và Odin, không thêm nội dung ngoài bản USA.
- **Golden Eagle Guild:** giữ nguyên tên Guild; nhãn vai trò chung như “Man with Red Bandana”, “Pretentious Woman” có thể Việt hóa thành “Gã quấn khăn đỏ”, “Quý bà kiêu kỳ”.
- **Nhân vật chính – cô bé với mã <CFFFA>:** tôi/cậu; không thay mã tên động bằng tên cố định.
- Nhân vật chưa chứng thực quan hệ vẫn giữ mức **pending-context**. Dùng `<CFFFD>`/`<CFFFC>` và các mã màu đúng thứ tự nguồn; đã QA cấu trúc, chưa test chữ vừa khung.
