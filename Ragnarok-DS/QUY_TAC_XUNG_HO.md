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


## Đợt 006 — Yusidra, Golden Eagle và Dark Knight

| Nhân vật / cặp quan hệ | Ngôi xưng | Ngữ cảnh |
|---|---|---|
| Aldo ↔ Rodia | anh/em | Đã xác nhận tình yêu qua lời Rodia; các hồi tưởng dùng cùng cặp ngôi, không gán tính yêu đương cho Zane |
| Zane ↔ Aldo/Rodia | tôi/cậu | Đồng đội và lời hy sinh đánh lạc hướng rồng |
| Aldo ↔ nhân vật chính và party | tôi/các cậu | Nghiêm túc khi kể tai nạn; giữ khả năng Rodia còn sống |
| Nhân vật chính ↔ Chỉ huy | tôi/thưa ngài; Chỉ huy dùng ta/cậu | Cảnh đăng ký Guild, nhận trách nhiệm Guildmaster |
| Nhân viên Kafra ↔ nhân vật chính | tôi/bạn | Hướng dẫn quản lý item, party và Guild; giữ Kafra Services / Kafra Inc. |
| Edwin/Fiona ↔ nhóm | tôi/cậu, đôi khi các cậu | Ban đầu kiêu ngạo, sau vụ tấn công chuyển giọng đau buồn; tuyệt đối không làm trò trước chuyện Fiona bị thương |
| Nhân vật chính ↔ cô bé (<CFFFA>) | tôi/cậu | Không tự đặt tên/giới tính; cô bé nổi giận khi nhóm mua thanh kiếm mà không hỏi ý |
| Dark Knight ↔ nhân vật chính | ta/ngươi | Uy hiếp, không tự gán danh tính liên quan đến cha; lời nhân vật chính về bố vẫn là hồi tưởng |
| Mysterious Man ↔ Underling | ta/ngươi | Nhãn vai trò dịch “Người đàn ông bí ẩn”, “Thuộc hạ”, chưa xác minh danh tính |
| Yolanda ↔ nhóm | tôi/các cậu | Popi là tên riêng của người thân được nhắc; không áp đặt thông tin ngoài cảnh |

**Khoá thuật ngữ đợt 006:** Rodia, Zane, Edwin, Fiona, Arunafeltz, Golden Eagle, Emperium, Guild, Guildmaster, Kafra Inc., Kafra Services, Letter to Aldo, Rusty Legendary Sword, Dark Knight, Yusidra Caves, Frione Tear.

**QA:** Không sửa thứ tự hay số lượng token `<CFFFB>`, `<CFFFA>`, `<CFFFD>`, `<CFFFC>` và mã màu; còn chờ font tiếng Việt và kiểm tra giới hạn ô thoại.


## Đợt 007 — Popi, Gales, Juno và Somatology Laboratory

- **Yolanda → nhóm:** tôi/mọi người; gọi Popi là người nhà, đừng để nhân vật tiết lộ Popi là chó trước cảnh vòng cổ.
- **Nhân vật chính – Lisir:** tôi/cậu; Lisir lo lắng khi trở lại Ant Hell vì ký ức về cha mẹ. Tranh cãi vui về phần thưởng không làm giảm nỗi sợ.
- **Lucifi – Lisir:** tôi/cô; Lisir đùa Lucifi già, Lucifi tự nhận mới ngoài hai mươi. Khi cô bé gặp nguy, chuyển sang giọng khẩn trương.
- **Nhân vật chính – cô bé (`<CFFFA>`):** tôi/cậu; cô bé bắt đầu nhận biết vui, buồn, giận dỗi. Không gán danh tính trước khi game tiết lộ.
- **Nhân vật chính – bố mẹ:** nhân vật chính kể về bố và mẹ, gọi “bố”, “mẹ”; đoạn bệnh mất của mẹ phải nghiêm túc. Không biến mâu thuẫn với bố thành lời thoại gây cười.
- **Gales ↔ nhóm/cô bé:** tôi/các cậu, tôi/cô; tự nhận từng làm ở cơ sở nghiên cứu và muốn bảo vệ cô bé. Nhóm nghi ngờ ông sau cái bẫy, nhưng **chưa khẳng định động cơ thật**.
- **Viselc ↔ nhóm:** tôi/cậu, suy xét bằng chứng, không kết luận khi chưa đủ thông tin. **Skal ↔ nhóm:** tôi/cậu, tự tin và đòi High Orc Helm đổi Card Key.
- **Nhãn vai trò thường:** Researcher → Nhà nghiên cứu; Security → Bảo vệ; Captain → Đội trưởng; giữ nguyên tên riêng/thuật ngữ gameplay: High Orc Helm, High Orc, Card Key, File F, Gales, Juno, Somatology Laboratory, Ant Hell, Frione, Guild, Golden Eagle Guild.

**QA:** Đã giữ nguyên trình tự các mã `<CFFFB>`, `<CFFFA>`, `<CFFFD>`, `<CFFFC>`, mã màu và mã khác; 0 lỗi cấu trúc. Font và khung thoại trên NDS chưa kiểm thử.


## Đợt 008 — Glast Heim, Dark Knight, Arma, Hồng y

| Cặp / nhân vật | Ngôi xưng | Ghi chú |
|---|---|---|
| Nhân vật chính ↔ Dark Knight khi chưa nhận ra | tôi/ông, lời chất vấn | Không để lộ quan hệ cha–con trước thời điểm nhân vật nhận ra |
| Nhân vật chính ↔ Father sau tiết lộ | con/bố | Cảnh xin lỗi, giằng xé, trăng trối và nỗi đau mất cha phải giữ trang trọng |
| Arma (từng dùng tên Gales) ↔ nhóm | ta/ngươi | Lộ danh tính, ngạo mạn; giữ tổ chức Destiny of the Great Gods |
| Lucifi ↔ nhân vật chính | tôi/cậu | Bạn thân, động viên trực diện; không cà khịa khi nhân vật đang tang thương |
| Lisir ↔ nhân vật chính | tôi/cậu | Đồng cảm mất bố mẹ, kéo bạn trở lại với trách nhiệm cứu cô bé |
| Viselc ↔ nhóm | tôi/cậu, tôi/các cậu | Suy luận chứng cứ, giải thích tôn giáo và thân thế vị Hồng y |
| Cardinal (Hồng y) ↔ nhóm | ta/ngươi | Cuồng tín, đau khổ vì con gái; không biện hộ cho ý định hủy diệt nhân loại |
| <CFFFA> (cô bé) | tên động, không tự đặt tên | Nhân vật chính công nhận cô là một con người chứ không phải công cụ |

**Tên/thuật ngữ khóa:** Arma, Gales, Glast Heim, Geffen Bridge, Ymir's Heart Piece, Broken Sword, Destiny of the Great Gods / Destiny of Great Gods (hai biến thể nguồn), Althena, Freya, Arunafeltz Faith.

**Cảnh báo đầu vào:** Tại `05-hoi-thoai-006.jsonl`, mục thứ 240 (index 239) có đoạn nguồn `Headdress" is here.Dark Knight` nối dính nhãn người nói. Đây là lỗi văn bản gốc, không thay đổi token để tránh lỗi chèn ROM. Cần xem trực tiếp cảnh khi patch.

**QA:** Cấu trúc/mã game đạt; chưa thể bảo đảm chữ vừa khung hoặc font tiếng Việt hiển thị đúng trên NDS.


## Đợt 009 — Cứu cô bé, hồi tưởng bố mẹ và NPC

| Cặp nhân vật | Ngôi xưng | Ghi chú |
|---|---|---|
| Nhân vật chính ↔ cô bé (`<CFFFA>`) | tôi/cậu | Đoạn tỏ tình, lựa chọn sống/chết giữ cảm xúc, không chế lời meme |
| Nhân vật chính ↔ bố và mẹ | con/bố, con/mẹ | Hồi tưởng bố mẹ giải thích cách cứu cô bé; người bố quyết đoán, mẹ dịu dàng |
| Gales ↔ Father (hồi tưởng) | tôi/anh | Bàn về `Ymir's Heart Piece`; khác thái độ của Arma ở tuyến phản diện |
| Hồng y ↔ party | ta/ngươi | Giọng cuồng tín, lạnh lùng; nhãn Cardinal dịch Hồng y |
| Lucifi ↔ nhân vật chính/Lisir | tôi/cậu | Động viên ở cao trào, sau đó mới đùa chuyện cưới xin |
| Lisir ↔ party | tôi/cậu | Ham tiền, chọc ghẹo trong đoạn hậu truyện; nghiêm khi cứu người |
| Viselc ↔ party | tôi/cậu | Lịch sự, điềm tĩnh |
| Guildmaster → người chơi | tôi/bạn | Hướng dẫn đổi Job và Limit Break, không đoán giới tính |

**Khoá thuật ngữ:** Ymir's Heart Piece, Mirage Tower, Card Key, High Orc Helm, F File, Limit Break, Acolyte, Priest, Job Level, Base Level, Gardi, Miko, Skol/Skal (viết khác nhau trong dữ liệu USA).

**Cảnh báo nguồn:** Một số lời thoại được xếp không theo mạch truyện, không sắp lại ID. Nguồn có dấu hiệu nhãn người nói dính câu ở index 123, 203, 211, 234, 240 của tệp 007. Giữ nguyên mã và số phân trang; chưa QA độ rộng chữ trên NDS.


## Đợt 010 — Guildmaster, Tavern Master, Kafra Staff và Dark Knight

- **Guildmaster → người chơi:** `Guildmaster` được giữ nguyên theo các đợt trước, dùng `tôi/bạn`. Các thủ tục Job rõ ràng, đôi lúc pha trò nhẹ đúng nghề: Merchant đùa về làm giàu, Assassin dùng giọng kín đáo, Priest trang trọng.
- **Tavern Master → người chơi:** nhãn `Chủ quán`, dùng `tôi/bạn`, hướng dẫn nhận, báo cáo và bỏ nhiệm vụ. Đừng nhầm vai trò này với một nhân vật có tên riêng.
- **Suspicious Man → người chơi:** nhãn `Gã khả nghi`, dùng `ta/ngươi` khi gợi ý con đường Dark Knight. Chưa đủ dữ liệu để xác nhận danh tính người này; không gán trùng nhân vật truyện.
- **Kafra Staff → người chơi:** nhãn `Nhân viên Kafra`, giọng lịch sự `tôi/bạn`.
- **Skal:** giữ nguyên tên, `High Orc Helm`, `High Orcs`, `El Mes Gorge - North` và mã màu đi kèm.
- **Tên riêng:** Reidun, Dorothea, Nissa, Birget, Kalle, Aila giữ nguyên. Các tính cách ngắn `Brave`, `Calm`, `Cowardly` và mô tả nhân viên thì Việt hóa.
- **Điều kiện:** nguồn nói `over 30` và `at least 30` ở những ngữ cảnh khác nhau. Không tự sửa đồng loạt; phải đối chiếu logic code khi patch ROM.
- **Limit Break:** quay lại Novice cấp 1, nhận điểm chỉ số thưởng; tăng mức tối đa Job cấp cao thêm 10 mỗi lần. Trình bày đủ thông tin, không xóa mã chỉ để rút dòng.
- **QA:** 0 lỗi cấu trúc, nhưng chưa đo chiều rộng từng chuỗi bằng font Việt và chưa xác nhận trên máy NDS.


## Đợt 011 — Đổi Job, Kafra, NPC Prontera

- **Guildmaster → người chơi:** `tôi/cậu`, hướng dẫn nghề nghiêm túc. Job Thief châm chọc nhẹ, Taekwon Kid gọi “châu chấu con”, Wizard khích lệ học phép; không tự đoán giới tính người chơi.
- **Mysterious Woman → người chơi:** `tôi/cậu`, giọng bí ẩn và cười “hê hê”; khi giải thích Shaman hoặc Limit Break phải chính xác điều kiện Base Level/Job Level.
- **Kafra Staff → người chơi:** `tôi/bạn`, lịch sự; menu bản đồ và thông báo lưu game phải rõ ràng. Tên địa danh có màu giữ nguyên theo bản USA.
- **Chủ nhà trọ, tiệm vật phẩm/vũ khí và Blacksmith → người chơi:** `tôi/bạn`, đùa có chừng mực ở câu nguyên tác hài về mua sắm, cháy túi hoặc cường hóa thất bại.
- **Commander → nhân vật chính:** `tôi/cậu`, giọng trực tiếp và tin tưởng.
- **Milika ↔ nhân vật chính:** `tôi/cậu`; Milika thiếu tự tin vì liên tục làm hỏng đồ, người chơi động viên; không tự gán quan hệ khác.
- **Vai trò NPC vô danh:** Man/Woman/Guy/Old Man/Girl Việt hóa nhãn; không suy đoán tuổi/giới tính của nhân vật chính.
- **Ngoại lệ dữ liệu:** bản USA có `Guildmaster<C3000><CFFFD>` xen giữa trang ở mục 43 của tệp 009; câu Kafra có `<CFFFC>` ở cuối. Đã giữ đúng mã; cần xem trên ROM khi vá.
- **QA kỹ thuật:** dòng `100% failure` của Milika chứa `% f` bị bộ kiểm tra xem là placeholder; bản Việt dùng `100% fail` để không làm thay đổi token. Chưa kiểm tra font hay tràn chữ.
