# Ragnarok DS (USA) — Việt hóa NDS

Nhánh độc lập `vh/ragnarok-ds-usa` của kho `VH-NDS`. Không trộn với các dự án Ni no Kuni, Magician’s Quest hoặc Ragnarok Odyssey ACE.

## Trạng thái mới nhất — Checkpoint 037 (20/11/2026)

- **13.596/14.616 ID đã xử lý (93,02%)**; còn **1.020** ID.
- **Nhóm Item hoàn tất 1.074/1.074 mục**: patch 034–036 có 240 mục, patch 037 bổ sung 834 mục (228 bản Việt hóa khác tiếng Anh, 606 tên Item/Card/quái/thuật ngữ được chủ động giữ nguyên).
- Đã đồng bộ patch 027–029 và 034–037; SHA patch 037 `b44295c8d02d7c2de65310d07dc8d594c236b149` khớp với ZIP bàn giao. Đối chiếu với 12.762 ID trên nhánh trước đó: **0 trùng ID**.
- **Không áp dụng patch 030** vì nội dung hệ thống/credit đã được xử lý ở đợt 001–002.
- Còn **475 Job/Skill** và **545 Quest**. Chi tiết: [CHECKPOINT_037_AUDIT.md](CHECKPOINT_037_AUDIT.md).
- Chưa nhúng font tiếng Việt, chưa vá ROM hoặc kiểm thử bằng NDS.

## Nguồn dữ liệu
- Bàn giao: `RagnarokDS_USA_BanGiao_Cloud.zip` (ROM USA, mã YRBE).
- Tổng 14.616 mục trong 33 tệp JSONL: 14.597 chuỗi và 19 nhãn ảnh; không bao gồm ROM.
- Đợt 001: 304 mục đã điền `vi` (219 bản Việt khác nguồn, 85 mục giữ nguyên), 14.312 mục còn `null`.
- Kiểm tra bằng `tools/check_handoff.py`: 14.616 ID; **0 lỗi**, chưa bật `--require-complete` vì đây là bản dịch từng phần.

## Quy ước
- Giữ nguyên **tên riêng, tên Job, item, skill, quái, địa điểm, tên Guild, Zeny, HP, SP, ATK, DEF và thuật ngữ gameplay chủ chốt**. 
- Việt hóa thông báo, hội thoại, mô tả, hướng dẫn, credit và nhãn UI không phải thuật ngữ chính.
- Giọng tự nhiên, gần gũi, điểm hài vừa phải; cảnh bi kịch phải được tôn trọng. Không thêm meme làm sai tính cách.
- Giữ nguyên **ID, trường en, thứ tự JSONL và mọi thẻ <Cxxxx>**, biến dạng %s/%d và ngắt dòng mã hóa.
- Ngôi xưng dựa trên lời thoại lân cận, không đoán quan hệ/tuổi/giới tính.
- Không tự sửa/đăng ROM thương mại. Chưa có font Việt, chưa patch và chưa test giả lập/máy thật.

## Tập tin bàn giao

Bản ZIP đầy đủ của đợt 001 đã được xuất trong phiên ChatGPT, gồm toàn bộ 33 JSONL với `vi=null` cho phần chưa dịch, `THUAT_NGU.json`, `QUY_TAC_XUNG_HO.md`, `DANH_BA_NHAN_VAT.json`, `BAO_CAO.txt` và `PATCH-DOT001.jsonl`.


## Checkpoint 002 — 18/11/2026

- **Đợt 002 thêm 759 ID:** +669 hệ thống và +90 hội thoại đầu game.
- **Tổng cộng 1.063/14.616 mục:** 922 bản Việt khác nguồn, 141 mục giữ nguyên tiếng Anh, 13.553 mục chưa xử lý.
- **QA chính thức:** 0 lỗi ID và mã điều khiển, không thay `en` hoặc các trường ngữ cảnh; chưa test font/máy thật.
- Đợt 002 ở `translation/PATCH-DOT002.jsonl`; đợt 001 ở 5 tệp `PATCH-DOT001-*.jsonl`. Công cụ `tools/apply_patches.py` sẽ tự áp dụng **cả hai** theo ID.
- Bộ ZIP đủ 33 JSONL đã xuất riêng trong phiên trò chuyện, kèm `THUAT_NGU.json`, hồ sơ xưng hô, báo cáo QA. Không đưa ROM lên GitHub.

## Checkpoint 003 — 18/11/2026

- **+266 ID** mới trong `translation/PATCH-DOT003.jsonl`, hoàn thành **05-hoi-thoai-001.jsonl: 441/441**.
- **Tích lũy tại mốc 003: 1.329/14.616 mục (9,09%)**, 1.186 bản dịch khác EN và 143 mục giữ nguyên thuật ngữ; 13.287 mục đang `vi=null`.
- Cảnh: lập Guild, nhiệm vụ tại Prontera Culvert, gặp Lucifi, giúp ông Olav tìm Colm (10 tuổi), White Peach.
- Điều chỉnh xưng hô theo cặp: người chơi–Lucifi **tôi/anh** (Lucifi dùng **tôi/cậu**), Olav **ông/cháu**, Colm **em/tôi** khi nói chuyện với người chơi không xác định giới tính, chỉ huy–thuộc cấp trang trọng.
- `tools/check_handoff.py` báo **14.616 source rows, 1.329 translated, 13.287 unfinished, 0 errors**.
- Đây vẫn là bản dữ liệu JSONL, **chưa có font tiếng Việt và chưa patch ROM**.

## Checkpoint 004 — 18/11/2026

- **+489 ID**, hoàn thành toàn bộ `05-hoi-thoai-002.jsonl` (489/489, trước đó vi=null). Bản mới nằm tại `translation/PATCH-DOT004.jsonl`.
- **Tích lũy 1.818/14.616 mục (12,44%)**: 1.664 mục khác bản EN, 154 mục đã rà và giữ nguyên; còn 12.798 mục chưa xử lý.
- Ngữ cảnh: đoàn tụ Colm/Olav, săn kho báu ở Geffen, trò lừa của Lughill/Attar, hồn ma Aghill, Viselc trợ chiến, Dark Knight và ký ức về mẹ, tìm Emperium để lập Guild.
- Bảo toàn tên nhân vật, item/Job/skill/địa điểm, tiêu biểu: White Peach, Dog Tag, Emperium, Prontera, Geffen, Mjolnir Dead Pit, Order of Knights, Guild. Mã điều khiển, màu và tên động được giữ nguyên.
- **QA 0 lỗi:** kiểm 14.616 ID, giữ `en`, không thêm/bớt mã điều khiển. Chưa thử font Việt, hiển thị trên NDS hay patch ROM.
- Bộ ZIP checkpoint 004 tích lũy đủ 33 tệp JSONL, có patch mới và báo cáo QA.

## Checkpoint 005 — 18/11/2026

- **+550 ID** mới, hoàn thành `05-hoi-thoai-003.jsonl` (550/550). Patch tại `translation/PATCH-DOT005.jsonl`.
- **Tích lũy 2.368/14.616 mục (16,20%)**: 2.204 mục dịch khác EN, 164 mục được kiểm tra và giữ nguyên, 12.248 mục chưa dịch.
- Bao gồm cảnh Lucifi khuyên người chơi, đoàn buôn Viselc, Lisir, Popi/Yolanda, Golden Eagle Guild, Frione/Frione Tear, Aldo, Emperium và Order of Knights. Giữ nguyên tên, item, skill và thuật ngữ chính.
- QA chính thức: **14.616 ID, 2.368 mục có `vi`, 12.248 mục `vi=null`, 0 lỗi**. Đối chiếu với nguồn `RagnarokDS_USA_BanGiao_Cloud.zip`; không đổi `en`, ID, mã điều khiển.
- **Chưa kiểm tra font tiếng Việt, tràn dòng trên NDS, patch ROM hay máy thật**.

## Checkpoint 006 — 18/11/2026

- **+535 mục** (525 câu dịch khác EN, 10 mục chỉ có tên hoặc lời gọi được giữ nguyên), hoàn thành `05-hoi-thoai-004.jsonl` (535/535). Tệp GitHub: `translation/PATCH-DOT006.jsonl`.
- **Tích lũy 2.903/14.616 mục (19,86%)**, 2.729 bản khác tiếng Anh, 174 mục giữ nguyên sau rà, 11.713 mục `vi=null`.
- Cảnh truyện: Aldo–Rodia–Zane gặp rồng; Emperium ở Yusidra Caves; lập Guild và Kafra; Golden Eagle, Edwin, Fiona; món Rusty Legendary Sword; Dark Knight; mở đầu nhiệm vụ Yolanda/Popi.
- **QA nguồn chính thức** (bản `tools/check_handoff.py` từ bộ bàn giao): 14.616 ID, 2.903 mục có `vi`, 11.713 chưa dịch, **0 lỗi** điều khiển/placeholder/ID. Đã đối chiếu phiên bản JSONL tích lũy của checkpoint 005; không sửa `en`.
- Chưa build ROM, chưa thay font, chưa kiểm tra kích thước tiếng Việt trên NDS hoặc giả lập.

## Checkpoint 007 — 18/11/2026

- **+485 ID** trong `translation/PATCH-DOT007.jsonl`, hoàn thành `05-hoi-thoai-005.jsonl` (485/485).
- **Tích lũy 3.388/14.616 mục (23,18%)**: 3.205 mục khác bản tiếng Anh, 183 mục được giữ nguyên; **11.228 mục chưa dịch (`vi=null`)**.
- Câu chuyện: Popi/Yolanda, Golden Eagle Guild; Lisir và Lucifi; người chơi kể về cha mẹ; Gales gặp lại cô bé; chuyến đi Juno tìm Skal đổi High Orc Helm lấy Card Key; Somatology Laboratory ở Lighthalzen, File F, cú bẫy và cuộc tìm kiếm cô bé.
- **QA:** trình `tools/check_handoff.py` của gói nguồn xác nhận đủ 14.616 ID, không đổi `en`, không đổi thứ tự mã điều khiển/placeholder, **0 lỗi**. Bản ZIP checkpoint 007 chứa đủ 33 JSONL và file thuật ngữ/xưng hô.
- **Chưa** thêm font tiếng Việt, patch ROM hay kiểm thử giả lập/máy thật; độ rộng dòng vẫn cần kiểm chứng.

## Checkpoint 008 — 18/11/2026

- **+461 ID** trong `translation/PATCH-DOT008.jsonl`, hoàn thành `05-hoi-thoai-006.jsonl` (461/461), trong đó 454 bản dịch khác tiếng Anh và 7 mục giữ nguyên tên/mã.
- **Tích lũy 3.849/14.616 mục (26,33%)**: 3.659 bản khác EN, 190 mục giữ nguyên; còn **10.767 mục chưa dịch** (`vi=null`).
- Tuyến truyện: Arma lộ danh tính, Glast Heim; Dark Knight và người cha; Ymir's Heart Piece; nhóm động viên nhân vật chính vượt bi kịch; Cardinal/Hồng y, Destiny of the Great Gods và kế hoạch hồi sinh Freya/Althena.
- **QA gốc `tools/check_handoff.py`: 14.616 ID, 3.849 bản có `vi`, 10.767 mục trống, 0 lỗi cấu trúc**. Giữ trường `en`, mã màu, tên động và token NDS không thay đổi.
- **Cảnh báo nguồn đã ghi nhận:** mục thứ 240 của file 006 (ID `RDS-c6841bc81e9fbac4b907`, xem bản ZIP/QA) bị dính tên người nói ngay sau `Headdress" is here.Dark Knight`. Bản dịch bảo toàn số/thứ tự mã; cần kiểm tra thủ công khi patch ROM.
- Chưa thay font, chưa làm ROM, chưa test giả lập/NDS hoặc kiểm tra glyph tràn khung. Mọi phát biểu đạt QA chỉ áp dụng **cấu trúc dữ liệu**.

## Checkpoint 009 — 18/11/2026

- **+328 ID mới**, hoàn thành `05-hoi-thoai-007.jsonl` (328/328), lưu ở `translation/PATCH-DOT009.jsonl`.
- **Tích lũy 4.177/14.616 mục (28,58%)**: 3.981 bản có `vi` khác `en`, 196 mục kiểm tra và giữ nguyên; còn 10.439 mục `vi=null`.
- Nội dung: nghi lễ hồi sinh Nữ thần, cô bé mong được sống, lựa chọn của nhân vật chính, hồi tưởng Father/Mother và Gales về Ymir's Heart Piece, hậu truyện và lời thoại NPC/Job/Limit Break.
- **QA nguồn chính thức:** 14.616 ID, 4.177 bản dịch, 10.439 chưa dịch, **0 lỗi**. Bảo toàn `en`, tên động, placeholder, mã màu và thứ tự các mã game.
- Cảnh báo nguồn: tệp 007 có nhãn người nói dính vào nội dung tại các index 123, 203, 211, 234, 240 (0-based); không thay token, cần xem lại khi patch ROM. Nguồn USA dùng cả `Skol` và `Skal`; giữ đúng nguyên văn mỗi vị trí.
- Chưa thay font tiếng Việt, chưa patch ROM, chưa thử giả lập/máy NDS hoặc đo tràn khung chữ.

## Checkpoint 010 — 18/11/2026

- **+161 mục** trong `translation/PATCH-DOT010.jsonl`, hoàn thành `05-hoi-thoai-008.jsonl` (161/161), gồm 155 bản dịch khác tiếng Anh và 6 tên riêng giữ nguyên.
- **Tích lũy 4.338/14.616 mục (29,68%)**; 10.278 mục `vi=null`. Giữ nguyên toàn bộ 4.177 bản ghi đã có từ checkpoint 009.
- Phần này là hội thoại chức năng, không phải tuyến cốt truyện mới: đổi Job, Limit Break (điều kiện Base Level/Job Level), Tavern Master giao/nhận nhiệm vụ, Guild Menu/Kafra, nhân viên và tính cách.
- `Guildmaster` giữ nguyên nhãn để đồng bộ đợt trước; `Tavern Master` → `Chủ quán`, `Suspicious Man` → `Gã khả nghi`, `Kafra Staff` → `Nhân viên Kafra`. Ngôi xưng tương ứng tôi/bạn, ta/ngươi, tôi/bạn.
- Giữ nguyên item/Job/skill, các thẻ game và mã màu. Lưu ý bản USA có khi ghi điều kiện `over 30` và lúc `at least 30`: giữ đúng từng vị trí, chưa kiểm chứng cơ chế bằng mã chương trình.
- **QA bằng chính `tools/check_handoff.py` trong gói bàn giao:** 14.616 source rows, 4.338 mục có `vi`, 10.278 chưa dịch, **0 errors** về cấu trúc, ID và mã điều khiển.
- Chưa đo độ rộng glyph tiếng Việt trên khung NDS, chưa patch ROM, chưa test giả lập/máy thật. Bản ZIP checkpoint 010 đã có `QA_KHUNG_CHU_010.json` ghi những dòng dài nên chú ý.
- **Kế tiếp:** `05-hoi-thoai-009.jsonl` có 244 mục.

## Checkpoint 011 — 18/11/2026

- **244/244 mục** của `05-hoi-thoai-009.jsonl` đã xử lý, trong đó 227 bản Việt khác EN, 17 mục giữ nguyên; patch: `translation/PATCH-DOT011.jsonl`.
- **Tích lũy 4.582/14.616 mục (31,35%)**; **10.034 mục `vi=null`**. Không ghi đè 4.338 mục đã có của checkpoint 010.
- Nội dung: Limit Break của Priest/Shaman/Knight/Assassin/Taekwon Kid/Wizard; giao diện Kafra, shop và bản đồ thị trấn; nhiệm vụ Jellopies của Milika tại Prontera. Tên Job, item, skill, địa danh quan trọng giữ nguyên.
- **QA bằng `tools/check_handoff.py` của nguồn gốc:** 14.616 source rows, 4.582 translated, 10.034 unfinished, **0 errors**. Không đổi ID, mã điều khiển, `en` và placeholder. Bản tích lũy có 33 JSONL.
- Lưu ý một dòng nguồn `100% failure` bị QA nhận diện `% f` là placeholder định dạng; bản Việt dùng `100% fail` (cách nói Gen Z) và giữ `% f` nguyên khối, không sửa script/nguồn.
- Tại file 009 có nhãn người nói dính giữa trang ở mục 43 và một phân trang trống cuối câu của Kafra; mã vẫn được bảo toàn. Chưa patch ROM, chưa bổ sung font, chưa đo độ rộng dòng trên NDS.
- **Kế tiếp:** `05-hoi-thoai-010.jsonl`.

## Checkpoint 012 — 18/11/2026

- **+332/332 mục** trong `05-hoi-thoai-010.jsonl` (331 thay đổi bản Anh, 1 tên động giữ nguyên), patch: `translation/PATCH-DOT012.jsonl`.
- **Tích lũy 4.914/14.616 mục (33,62%)**, 9.702 mục `vi=null`. Các đợt 001–011 được giữ nguyên.
- Nhiệm vụ phụ: Milika tìm 10 Jellopies từ Porings, Knight cần 10 Red Herbs từ Spores, Roni cần 5 Iron Ore từ Thief Bugs, Chủ quán gửi 10 Empty Bottles cho Jade tại Morocc, Shiva tìm Mastela Fruit giúp mẹ, Sherry nghiên cứu phép, khu rừng thiêng gần Glast Heim, Jack quảng cáo tiệm vũ khí Geffen, Liam mở Secret Pathway, Joyce tìm 10 Monster Hides từ Desert Wolves.
- Thuật ngữ và vai trò: Giữ nguyên tên item/skill/Job/quái/địa danh, Việt hóa nhãn NPC vô danh như `Mysterious Old Woman` thành “Bà lão bí ẩn”, `Swordswoman` thành “Nữ kiếm sĩ”. Trường hợp `Boss` chỉ trong bối cảnh thợ mộc qua cổng được dịch “Đội trưởng thợ”.
- **QA từ `tools/check_handoff.py` nguồn:** 14.616 source rows, 4.914 mục xử lý, 9.702 mục chưa dịch, **0 lỗi cấu trúc**. Không đổi `en`, ID, màu, tên động và chuỗi token.
- Có **5 mục** tăng độ dài ký tự đáng kể, cần đo glyph và khung thoại sau khi có font Việt; chưa kiểm thử trên NDS hoặc build ROM.
- Một số câu gốc có phân trang rỗng và `<C3000>` nằm giữa nội dung; giữ nguyên thay vì tự sửa logic định dạng.
- **Kế tiếp:** `05-hoi-thoai-011.jsonl`.

## Checkpoint 013 — 18/11/2026

- **+425 mục** trong `05-hoi-thoai-011.jsonl` (423 khác nguồn EN, 2 lời gọi giữ nguyên), patch tại `translation/PATCH-DOT013.jsonl`.
- **Tích lũy 5.339/14.616 mục (36,53%)**, còn 9.277 mục `vi=null`. Toàn bộ 4.914 bản dịch checkpoint 012 được kiểm tra và giữ nguyên.
- Nội dung: Daksten/10 Zargons, Sedi/Pocket Watch, Lily–Hodril/Little Evil Horn, Dogerel/Skull, Sa'ab/vật liệu nghiên cứu, Karen/Laimis Flower, vòng giao hàng Rich–Holland–George–Wade, thanh kiếm bị nguyền của Stefan, Viselc/Attar dọn sạt lở, Magician lấy Wing Staff.
- Quy tắc: giữ tên người, quái, Job, skill/item và địa danh bằng tiếng Anh; các nhãn vai trò chung `Sister` → `Nữ tu`, `Judge` → `Giám khảo`. Karen gọi người chơi trung tính, không gán giới tính nhân vật có tên động.
- **QA:** `tools/check_handoff.py` của gói nguồn kiểm tra đủ 14.616 ID, 5.339 mục đã dịch, 9.277 chưa dịch, **0 errors** về ID, `en`, placeholder và mã game. Không thay thứ tự `<CFFFD>`, `<CFFFC>`, `<C3000>`, mã màu, tên động.
- ZIP tích lũy có 33 JSONL, patch 013, bảng thuật ngữ, ma trận xưng hô, QA và danh bạ. Chưa thay font, chưa patch ROM và **chưa xác nhận độ rộng câu trên máy NDS**.
- **Kế tiếp:** `05-hoi-thoai-012.jsonl` còn **354 mục**.

## Checkpoint 014 — 18/11/2026

- Hoàn thành **354/354 mục** của `05-hoi-thoai-012.jsonl`, tất cả là bản Việt khác câu gốc. GitHub patch: `translation/PATCH-DOT014.jsonl`.
- **Tích lũy 5.693/14.616 mục (38,95%)**, **8.923 mục `vi=null`**. 5.339 mục có trước được bảo toàn 100%.
- Nội dung: Setsuna thử Thief tại Ant Hell (Black Carpet/Assassin's Dagger), Jiro thử Archer hạ Owl Baron (Rudra's Bow), Marco tìm 4 item thưởng Grand Cross, Jim thử Taekwon hạ Grizzly (Megingjard), Gordon thu mua đá quý, Lime/Shina sửa hộp nhạc, Allen nhờ tìm hộp thời gian, Brent nhờ Four-Leaf Clover, Sarah nhờ cứu bố Marlon ở Mjolnir Dead Pit.
- **QA bộ nguồn `tools/check_handoff.py`: 14.616 source rows, 5.693 translated, 8.923 unfinished, `errors=[]`**. Đã so khớp đúng thứ tự mã NDS, màu, tên động; không đổi ID/EN.
- **Cảnh báo cần kiểm tra in-game:** ID ở index 312 của file 012 gọi nhân vật Brent là `Marvin` trong thoại nguồn, hiện giữ nguyên nguyên tác. Ở index 336 và 342, Sarah nói `be a man`; không suy luận giới tính nhân vật trong các cảnh khác.
- Bản ZIP checkpoint 014 có 33 JSONL tích lũy, patch 014, bảng thuật ngữ, ma trận ngôi xưng, danh bạ, báo cáo QA; **chưa** phải ROM Việt hóa, chưa nhúng font hoặc kiểm thử trên NDS.
- **Đợt kế tiếp:** `05-hoi-thoai-013.jsonl` còn **465 mục**, mở bằng cảnh Marlon/Joshua bị quái vây.

## Checkpoint 015 — 18/11/2026

- **465/465 mục** hoàn thành trong `05-hoi-thoai-013.jsonl`: 459 bản dịch khác nguồn và 6 mục giữ nguyên. Patch tại `translation/PATCH-DOT015.jsonl`.
- **Tích lũy 6.158/14.616 mục (42,13%)**, còn 8.458 mục `vi=null`. Không ghi đè 5.693 mục đã có ở checkpoint 014.
- Nội dung nguồn USA: Sarah–Marlon/Joshua, Éclair từ nhẫn cưới mẹ Sarah; nhóm rơi xuống đường tắt giữa El Mes Gorge và Mt. Mjolnir; Rouche kiểm tra mật khẩu `Trust` và chỉ cửa sau Somatology Laboratory; Sonya nhờ cứu bố khỏi giày bị nguyền bằng Aquamarine; Sopborough/Card; cứu ba thợ mỏ tại Mjolnir Dead Pit - 2F; Yolanda tìm vợ cho chó Popi; Rolek xin gia nhập Guild.
- **QA chính thức `tools/check_handoff.py` từ bộ nguồn:** `source_rows=14616`, `translated=6158`, `unfinished=8458`, `errors=[]`. Bảo toàn toàn bộ EN, ID, thứ tự mã phân trang, màu, tên động và placeholder.
- **Ghi chú khi patch ROM:** Có những NPC viết nhãn người nói nối trực tiếp với `<CFFFD>` thay vì `<C3000>` (Old Lady/Young Man), không tự thêm mã. Mật khẩu `Trust` vẫn là tiếng Anh; `Nerdvana` là chơi chữ độc đáo của Sopborough, giữ nguyên.
- Bản ZIP checkpoint 015 gồm 33 JSONL tích lũy, patch, thuật ngữ, danh bạ, ma trận ngôi xưng và QA. Chưa thay font hoặc test tiếng Việt trên NDS thật/giả lập.
- **Kế tiếp:** `05-hoi-thoai-014.jsonl` có 432 mục, bắt đầu với Sopborough.

## Checkpoint 016 — 18/11/2026

- **432/432 mục** được xử lý trong `05-hoi-thoai-014.jsonl`, gồm 429 bản Việt khác nguồn và 3 mục giữ nguyên. Patch: `translation/PATCH-DOT016.jsonl`.
- **Tích lũy 6.590/14.616 mục (45,09%)**, còn 8.026 mục `vi=null`. Đã giữ nguyên 6.158 mục của checkpoint 015.
- Tuyến truyện: Sopborough thử thách Wolf Card; Julietta kể chuyện tình cảm, vượt tự ti và xin gia nhập Guild; Cliff và Wandering Swordsman thử thách; Malone và Banished Magician; Rick cùng bài kiểm tra Thieves Guild/Mimic; Zeeter săn dơi đỏ; Lisir viếng mộ bố mẹ; Martha đóng giả ma khiến Lucifi bỏ chạy.
- **QA:** chạy công cụ gốc `tools/check_handoff.py`: `source_rows=14616`, `translated=6590`, `unfinished=8026`, `errors=[]`. Không sửa trường `en`, ID, thứ tự mã NDS, tên động hoặc placeholder.
- **Cảnh báo nguồn USA:** Index 176, 369 và 417 của file 014 có thẻ `<C3000>` xuất hiện ngay giữa lời thoại. Index 203 có chuỗi `COLOR_RED>Mimic<CFFF4>` bị thiếu dấu mở mã màu. Bản Việt không tự thay mã; cần xem lại khi patch ROM.
- Giữ nguyên tên riêng, item, skill, Job và địa danh tiếng Anh; vai trò không tên `Wandering Swordsman` → “Swordsman lang thang”, `Banished Magician` → “Magician bị trục xuất”, `Ghost` → “Hồn ma”.
- **Chưa** bổ sung font tiếng Việt, patch ROM hoặc kiểm chứng chiều rộng chữ trên giả lập/NDS thật.
- **Đợt 017:** tiếp tục `05-hoi-thoai-015.jsonl`, **464 mục** chưa dịch.

## Checkpoint 017 — 18/11/2026

- Hoàn thành **464/464 mục** `05-hoi-thoai-015.jsonl`, lưu patch tại `translation/PATCH-DOT017.jsonl`.
- **Tích lũy 7.054/14.616 mục (48,26%)**, còn 7.562 mục `vi=null`; 6.590 mục đã có của checkpoint 016 được giữ nguyên.
- Nội dung: Order dựng nhiệm vụ ma giả để luyện Lucifi; Lucifi kể trò ma trùm chăn hồi nhỏ; điều ước Mt. Mjolnir cùng cô bé; Attar nối lại việc tìm kho báu Aghill, Walter vòi Topaz, Raul cho tra cứu sách; Barghill tìm Diamond 1ct. từ Remover, vừa lễ độ vừa dọa; Ashley gọi Mjolnir Dead Pit sai là “mule knee”; Master Phuong săn Minorous; Gabera trách Lisir thiếu đồng cảm, thưởng tiền và công nhận bậc Buddy.
- **QA chính thức từ `tools/check_handoff.py`**: `source_rows=14616`, `translated=7054`, `unfinished=7562`, `errors=[]`. Mã NDS được giữ đúng thứ tự và **đúng dòng**, không chỉ khớp số lượng. Giữ nguyên `en`, ID và tên động.
- Có **4 mục** vượt ngưỡng cảnh báo độ dài tương đối (chỉ so số ký tự; chưa đo glyph), ghi trong ZIP ở `QA_KHUNG_CHU_017.json`.
- Nguồn USA có thẻ `<C3000>` chen trong lời thoại tại index 80, 163, 180, 183, 300 của file 015. Bản dịch bảo toàn các vị trí mã; cần xác minh trực tiếp khi vá ROM.
- **Chưa build ROM hoặc font tiếng Việt**, chưa kiểm tra tràn khung trên NDS/giả lập.
- **Đợt 018:** `05-hoi-thoai-016.jsonl` còn **594 mục**, bắt đầu ở cảnh Gabera chỉ dẫn thử thách trên Geffen Bridge.

## Checkpoint 018 — 18/11/2026

- **+594 mục, hoàn thành toàn bộ `05-hoi-thoai-016.jsonl`** (576 bản Việt khác EN, 18 mục giữ nguyên ký hiệu/tên); patch: `translation/PATCH-DOT018.jsonl`.
- **Tích lũy 7.648/14.616 mục (52,33%)**; còn **6.968 mục `vi=null`**. 7.054 bản ghi cũ được giữ nguyên dữ liệu.
- Mạch truyện: Gabera ép Lisir đấu Natsume tại Geffen Bridge, Guildmaster làm nhân chứng; Natsume dùng phép biến hình chưa hoàn chỉnh; Gabera hướng dẫn bí thuật Transformation, ba năm đầu biến thành Poring, khoảng mười năm luyện tập mới có cơ hội thành rồng. Đoạn tiếp theo Viselc kể chuyện hai bạn thân Pott–Mof bị nhầm là Thief ở Prontera, điều tra Prontera Culvert và minh oan cho bạn.
- **QA chính thức bằng `tools/check_handoff.py` gốc:** `source_rows=14616`, `translated=7648`, `unfinished=6968`, `errors=[]`. Kiểm đủ tên động, thứ tự tag màu, dấu ngắt trang và placeholder; không sửa `en`, ID hay context.
- **Hai điểm bất thường của nguồn USA:** index 135 có `<C3000>` giữa nội dung câu "May I borrow Lisir..."; index 273 có trang rỗng sau `<CFFFC>`. Bản dịch giữ nguyên thứ tự/mã, chưa sửa engine.
- **4 mục có cảnh báo độ dài theo số ký tự**, cần đo đúng font NDS để biết có tràn khung hay không; không khẳng định đã kiểm thử máy thật.
- Các tên riêng/Job/item/quái/kỹ năng giữ tiếng Anh, bổ sung `Transform`, `Transformation`, `Pott`, `Mof`, `Lilac`; nhãn `Young Woman` → "Cô gái trẻ".
- **Chưa có bản ROM Việt hóa tích hợp**, chưa nhúng font tiếng Việt hoặc QA hiển thị trên NDS.
- **Đợt 019:** tệp `05-hoi-thoai-017.jsonl` có **478 mục** chưa dịch, tiếp tuyến điều tra của Lilac.

## Checkpoint 019 — 18/11/2026

- Hoàn thành toàn bộ **478 mục** của `05-hoi-thoai-017.jsonl` (474 mục khác nguyên tác, 4 câu/tên giữ nguyên). Patch: `translation/PATCH-DOT019.jsonl`.
- **Tích lũy 8.126/14.616 mục (55,60%)**, còn 6.490 mục chưa dịch (`vi=null`); **7.648 mục** checkpoint 018 không thay đổi.
- Nội dung: Lilac và Viselc hợp tác điều tra đoàn buôn bị tấn công; Akari cảnh báo nguy cơ vu oan tại Morocc; nhóm bị phép ác mộng tại East Prontera Woods, cô bé hé lộ hai người đàn ông trong ký ức; Lisir cho người chơi uống thuốc tăng chiều cao khiến lời nói thành giọng quý tộc; tìm 2 Panaceas + 5 Holy Waters để giải; Viselc hợp tác Merchant diệt kiến Ant Hell/Gold Thief Bug, khôi phục ốc đảo và đối phó cơn sốt trẻ em do phấn hoa ở Eternal Sands.
- **QA của nguồn gốc `tools/check_handoff.py`**: `source_rows=14616`, `translated=8126`, `unfinished=6490`, `errors=[]`. Giữ nguyên `en`, ID, context, uses, group, token tên động, mã màu và thứ tự trang.
- Source USA index **422**: nhãn `Moroccan<CFFFD>` không có `<C3000>`; nhãn được dịch “Người Morocc” nhưng không chèn/sửa thẻ game.
- **4 mục cảnh báo độ dài ký tự**, không phải lỗi đã xác nhận trên khung NDS; dữ liệu còn cần bổ sung font và kiểm thử ROM/giả lập/máy thật.
- Trong ZIP checkpoint 019 có đủ 33 JSONL tích lũy, patch, glossary, danh bạ nhân vật, bảng xưng hô và QA.
- **Đợt 020:** bắt đầu `05-hoi-thoai-018.jsonl` với **412 mục** chưa dịch, mở đầu bằng Merchant Morocc cảm ơn nhóm.

## Checkpoint 020 — 18/11/2026

- **+412 mục** hoàn thành `05-hoi-thoai-018.jsonl` (403 bản Việt khác EN, 9 mục chỉ có tên hoặc thẻ giữ nguyên), patch `translation/PATCH-DOT020.jsonl`.
- **Tích lũy 8.538/14.616 mục (58,42%)**, còn **6.078 mục `vi=null`**; 8.126 mục đã xử lý ở checkpoint 019 không thay đổi.
- Mạch truyện: Merchant Morocc trả ơn và mời Đội trưởng thợ mở rộng Guild; Lisir giận dỗi bỏ đi đến Mjolnir Dead Pit tìm mặt dây chuyền mà người thuê đã có trong túi; Lucifi đến cứu. Lilac bị kẻ chủ mưu phản bội; Akari tiết lộ Larks hy sinh khi nhờ Viselc bảo vệ Lilac; Viselc chọn bỏ qua để giữ thể diện Morocc. Order nhờ Lucifi cứu đứa trẻ trúng độc ở East Prontera Woods; Attar thuê tìm Treasure Map tại Eternal Sands; Sohee trong Prontera Culvert và ông lão khả nghi thu thập item để phục hồi linh hồn của kiếm.
- **QA từ `tools/check_handoff.py` nguồn:** `source_rows=14616`, `translated=8538`, `unfinished=6078`, `errors=[]`. Dữ liệu ID, `en`, `group`, `context`, `uses`, tên động, mã màu, mã phân trang không bị thay đổi.
- **Đã rà cảnh báo dòng dài:** không còn mục nào vượt ngưỡng độ dài tương đối của riêng batch 020 sau khi biên tập; vẫn có nhiều dòng cần đo font thực để xác nhận hiển thị trên NDS.
- **Mã bất thường trong nguồn USA:** index 3, 65, 103, 124, 190, 231, 337 có `<C3000>` trong phần thân hội thoại; các nhãn `Child` và `Maintenance Crew` không có `<C3000>`. Giữ nguyên cấu trúc; không tự sửa engine.
- **Cảnh báo nội dung:** bản USA hiển thị thông báo nhận `Ogre Tooth` ngay trong tuyến linh hồn kiếm; giữ nguyên item và đánh dấu cần đối chiếu bằng game-test, không tự chữa lỗi nguồn.
- ZIP checkpoint 020 có 33 tệp JSONL tích lũy, patch mới, glossary, danh bạ, quy tắc xưng hô và QA. **Chưa tạo ROM, chưa nhúng font Việt, chưa test giả lập/NDS thật**.
- **Đợt 021:** `05-hoi-thoai-019.jsonl` còn **414 mục**, mở đầu bằng Sogard và nhiệm vụ tuyến thương lộ.

## Checkpoint 021 — 18/11/2026

- **+414 mục**, hoàn thành `05-hoi-thoai-019.jsonl` (412 câu Việt khác nguồn, 2 câu giữ nguyên); patch tại `translation/PATCH-DOT021.jsonl`.
- **Tích lũy 8.952/14.616 mục (61,25%)**, **5.664 mục `vi=null`**. Toàn bộ 8.538 bản ghi checkpoint 020 được giữ nguyên.
- Nội dung: Sogard nhờ cứu Dan ở `Sograt Desert - North` và diệt quái hệ Hỏa trên tuyến thương lộ; Dan xin gia nhập Guild; Lisir được Gabera thử thách với `Book of Abstinence` rồi trở thành Wizard; Viselc điều tra Nikol và thu thập `Assassin Registry` để lên Assassin; Lucifi tiêu diệt boss tại `Prontera Culvert` rồi trở thành Knight; các câu thoại thành viên động ở cuối file.
- **QA chính thức gói nguồn:** `tools/check_handoff.py` trả `source_rows=14616`, `translated=8952`, `unfinished=5664`, `errors=[]`. Giữ nguyên ID, `en`, `group`, `context`, `uses` và tất cả mã NDS.
- Các điều kiện khi đổi Job vẫn đầy đủ: phải có Lisir/Viselc/Lucifi trong party thích hợp, chừa khoảng trống trong inventory để nhận lại trang bị tháo ra khi đổi Job; không sửa nguyên tắc sát hạch.
- **Điểm bất thường từ bản USA:** index 350 của tệp 019 có `<C3000>` nằm giữa câu `Lucifi becoming a Knight`; bản Việt giữ nguyên vị trí này. Nguồn có các trang trong hội thoại Lisir xen nhau theo event; không tự đổi thứ tự ID.
- Đánh dấu **2 mục** có cảnh báo độ dài Unicode tương đối, cần đo bằng font NDS; đây không phải lỗi tràn chữ đã xác nhận.
- ZIP checkpoint 021 gồm 33 JSONL tích lũy, patch mới, thuật ngữ, hồ sơ xưng hô, danh bạ và QA. **Chưa build ROM, nhúng font Việt hoặc kiểm thử giả lập/NDS thật.**
- **Đợt 022:** tiếp `05-hoi-thoai-020.jsonl`.

## Checkpoint 022 — 18/11/2026

- **+461/461 ID** của `05-hoi-thoai-020.jsonl` đã xử lý, gồm 459 mục dịch khác bản tiếng Anh và 2 mục giữ nguyên. Patch: `translation/PATCH-DOT022.jsonl`.
- **Tích lũy 9.413/14.616 mục (64,40%)**; còn **5.203 mục `vi=null`**. Không ghi đè 8.952 mục đã có ở checkpoint 021.
- Nội dung: thành viên động `<CFFF8>` và mức Buddy; Swordsman Guild thử thách hai người tại West Prontera Woods; Magician Guild tuần tra Geffen Bridge; Thieves Guild giao bản tin; Acolyte Guild dẹp mùi hôi Prontera Culvert bằng kẹp mũi; Archer Guild đi săn **4 Peco Peco** tại East Prontera Woods; Biger yêu cầu hai người đại diện Merchant Guild chốt hợp đồng ở Juno.
- **QA gốc `tools/check_handoff.py`**: `source_rows=14616`, `translated=9413`, `unfinished=5203`, `errors=[]`. Tất cả ID, `en`, `group`, `context`, `uses`, tên động, màu và thứ tự mã NDS đều hợp lệ.
- **Độ dài trong tệp mới:** không có phần nội dung lời thoại nào vượt 36 ký tự Unicode sau khi bỏ mã điều khiển (`QA_KHUNG_CHU_022.json`); **không** suy ra chắc chắn vừa khung hiển thị, cần đo glyph sau khi thêm font Việt.
- **Lỗi/bất thường nguồn USA giữ nguyên:** index 113 có `<C3000>` trong thân câu; index 249–256 dùng nhãn `Guild Member` nhưng không có `<C3000>`; index 460 có trang cuối không có `<CFFFD>`; `Guild Worker <C3000>` đôi chỗ có khoảng trắng. Không tự thêm/bỏ mã.
- Tên Job, item, skill, monster, địa danh và bậc quan hệ giữ tiếng Anh; nhãn NPC vô danh dịch `Guild Worker` → “Nhân viên Guild”, `Thieves Guild Worker` → “Nhân viên Thieves Guild”, `Guild Member` → “Thành viên Guild”.
- ZIP checkpoint 022 có 33 JSONL, patch, thuật ngữ, danh bạ NPC, bảng ngôi xưng và báo cáo QA; vẫn **chưa nhúng font hay patch ROM, chưa test giả lập/NDS**.
- **Đợt 023** tiếp `05-hoi-thoai-021.jsonl` với **454 mục**.

## Checkpoint 023 — 18/11/2026

- **+454 mục**, hoàn thành toàn bộ `05-hoi-thoai-021.jsonl` (454/454). Patch: `translation/PATCH-DOT023.jsonl`.
- **Tích lũy 9.867/14.616 mục (67,51%)**; còn **4.749 mục `vi=null`**. Giữ nguyên 9.413 bản dịch đã hoàn thành trước đó.
- Tuyến truyện: Biger giao Merchant Guild lấy 15 Zargon từ Beetles và 5 Ogre Tooth từ Hi Orcs; Guy tổ chức bài kiểm tra Taekwon Kid phối hợp hai người ở Mt. Mjolnir - East; Clay trao kiếm Executioner gia truyền khi giao 20 Garlets; Sopborough sưu tầm Alice Card rồi trao Dark Lord Card; Attar tìm kho báu Aghill và thần khí Mjolnir, khu hầm sập và hồn ma xuất hiện; Misha gửi người chơi đến Somatology Laboratory và trả Rosario; Gin trao Knight's Spirit.
- **QA chính thức nguồn gốc `tools/check_handoff.py`**: `source_rows=14616`, `translated=9867`, `unfinished=4749`, `errors=[]`. Giữ nguyên ID, EN và thứ tự mã NDS, tên động, màu và placeholder.
- **Độ dài:** sau khi biên tập batch 023, không có phần chữ nào dài quá 36 ký tự Unicode giữa các mã ngắt. Chưa đo độ rộng font thật hoặc xác nhận bằng giả lập/NDS.
- **Bất thường từ bản USA:** index 83, 172, 348 có `<C3000>` chen trong nội dung; index 406 chỉ chứa `Misha<C3000><CFFFD>` (không có lời). Bảo toàn nguồn; không tự thêm/bỏ mã.
- Đã bổ sung thuật ngữ/nhãn NPC về Guy, Clay, Sopborough, Executioner, Garlets, Andre, Alice Card, Mjolnir, Rosario và Knight's Spirit; trong ZIP checkpoint 023 có 33 JSONL, patch, 374 thuật ngữ, ma trận ngôi xưng, danh bạ và QA.
- **Chưa build ROM hay bổ sung font tiếng Việt**, cần kiểm thử giả lập và máy NDS thật.
- **Đợt 024:** tiếp `05-hoi-thoai-022.jsonl`.

## Checkpoint 024 — 18/11/2026

- **+511/511 mục** trong `05-hoi-thoai-022.jsonl`, 510 bản Việt khác EN và 1 mục giữ nguyên (mã/tên). Patch `translation/PATCH-DOT024.jsonl`.
- **Tích lũy 10.378/14.616 mục (71,00%)**, còn **4.238 mục `vi=null`**. Giữ nguyên toàn bộ **9.867 mục** của checkpoint 023.
- Nội dung theo thứ tự gốc: Nhận `Knight's Spirit` và lên `Buddy`; Gin nhờ đội có Knight hạ `Hydrolancer` tại `El Mes Gorge - South` để nhận Job Exp. Marie giao đội có Wizard ngăn Young Magician triệu hồi hàng nghìn ác quỷ tại `Somatology Laboratory`, tặng `Wizard's Spirit`; cô ta chạy trốn và tái phạm. Fritz nhờ Assassin xử lý trùm cướp ở `Sograt Desert - South`; trùm cướp được tha nhưng dùng bom chớp trốn thoát, sau quay lại; phần thưởng `Assassin's Spirit`. Jenny giao Priest tìm nguồn ma tại `Somatology Laboratory` và trao `Priest's Spirit`.
- Tên nhân vật, item, skill, Job, địa danh, quái chính giữ nguyên theo quy tắc. Chỉ Việt hóa vai trò không phải tên riêng: `Young Magician` → `Magician trẻ`, `Bandit Boss` → `Trùm cướp`, `Underling` → `Đàn em`.
- **QA chính thức bộ nguồn `tools/check_handoff.py`**: `source_rows=14616`, `translated=10378`, `unfinished=4238`, `errors=[]`. Không đổi `en`, ID, `uses`, `group`, `context` hay thứ tự mã tên động/định dạng.
- **Độ dài file 022:** 0 phần lời thoại vượt 36 ký tự Unicode giữa các dấu ngắt; 2 cảnh báo dài tương đối tại index 182 và 418 (chưa kết luận tràn khung). **Chưa đo glyph thực, chưa nhúng font hoặc vá ROM NDS**.
- ZIP checkpoint 024 có 33 tệp JSONL tích lũy, patch mới, 385 thuật ngữ, quy tắc xưng hô, danh bạ nhân vật và báo cáo QA.
- **Đợt 025:** tiếp `05-hoi-thoai-023.jsonl` với **517 mục** đang `vi=null`.

## Checkpoint 025 — 18/11/2026

- **+517/517 mục**, dịch hết `05-hoi-thoai-023.jsonl` (513 mục có chữ Việt khác EN, 4 mục giữ nguyên). Patch: `translation/PATCH-DOT025.jsonl`.
- **Tích lũy 10.895/14.616 mục (74,54%)**; còn **3.721 mục `vi=null`**. 10.378 mục có trước được bảo toàn đúng từng tệp/ID.
- Nội dung theo nguồn: Jenny nhờ Priest dọn ma ở `Somatology Laboratory` lần nữa; Jazz yêu cầu Hunter săn `Vagabond Wolf` rồi trao `Hunter's Spirit`; Bughill của Merchant Guild giao nhiệm vụ 6 đá quý (`Sapphire`, `Topaz`, `Sardonyx`, `Aquamarine`, `Opal`, `Emerald`) + kiếm `Flamberge` trị giá `30000 zenies` tới nhà trọ `Juno` cùng Blacksmith, trao `Blacksmith's Spirit`; Master Li sợ tối nhờ người chơi và Taekwon Master đi đấu với học trò cũ `Immortal Fighter` ở `Mjolnir Dead Pit`, trao `Taekwon Master's Spirit`.
- **QA chính thức `tools/check_handoff.py`:** `source_rows=14616`, `translated=10895`, `unfinished=3721`, `errors=[]`. Giữ nguyên ID, `en`, context, uses, group, thứ tự mã NDS, biến tên động và mã màu.
- **Cảnh báo nguồn:** index 300, 302, 304 của file 023 ghi nhãn `Begell` thay vì `Bughill`, không có `<C3000>` đi kèm. Giữ nguyên theo nguyên tác, chưa thay font/kiểm thử ROM.
- **QA độ dài:** 0 phần chữ vượt 36 ký tự Unicode giữa các mã ngắt (chưa đo độ rộng glyph). Có 8 cảnh báo tương đối, một số do tên động được tính không chính xác; đều chưa phải lỗi tràn khung đã xác nhận.
- ZIP checkpoint 025 có 33 JSONL tích lũy, patch 025, 398 thuật ngữ, quy tắc xưng hô, danh bạ nhân vật và báo cáo QA. **Chưa tạo ROM hay bổ sung font tiếng Việt**.
- **Đợt 026:** `05-hoi-thoai-024.jsonl` có **491 mục** chưa dịch.

## Checkpoint 026 — 18/11/2026

- **491/491 mục** hoàn thành trong `05-hoi-thoai-024.jsonl`: 478 bản Việt khác EN, 13 mục chỉ giữ nguyên tên/ký hiệu. Patch: `translation/PATCH-DOT026.jsonl`.
- **Tích lũy 11.386/14.616 mục (77,90%)**, còn **3.230 mục `vi=null`**. Không thay đổi **10.895 mục** checkpoint 025.
- Nội dung: cuộc tái đấu của Immortal Fighter; Allen và Kate đọc thư trong hộp thời gian; Nina tự xưng Merchant Chính Nghĩa, đánh đuổi Hoodlum và xin vào Guild; Chỉ huy điều tra Dark Knight ở Glast Heim và trao Bloody Sword; Dark Magician thử thách đổi Job Dark Knight/nhận Tyrfing; Phụ nữ bí ẩn chỉ trình tự bốn nơi **Eternal Sands → East Prontera Woods → Mt. Mjolnir - East → Ant Hell** để nhận Yggdrasil Branch; Shaman ở Yusidra Caves giảng về sức mạnh, nỗi sợ mất bạn bè và trao Ancient Shaman Documents.
- **QA chính thức nguồn `tools/check_handoff.py`**: `source_rows=14616`, `translated=11386`, `unfinished=3230`, `errors=[]`. Giữ nguyên ID, `en`, context, uses, group, thứ tự mã, tên động và màu NDS. Mọi tệp JSONL cũ được so khớp byte-level với ZIP 025.
- **Độ dài:** không có phần chữ dài quá **36 ký tự Unicode** giữa thẻ điều khiển; có **4 cảnh báo độ dài tương đối** cần đo font thật. Các mảnh âm thanh chưa rõ `Di...er...` và `Embo...div...wer.` giữ nguyên tiếng nguồn vì chưa đủ dữ kiện diễn giải.
- **Chưa có bản ROM tiếng Việt đã nhúng font/QA trên NDS**; ZIP checkpoint 026 gồm 33 JSONL, patch, glossary **412 mục**, danh bạ nhân vật, quy tắc xưng hô và QA.
- **Đợt 027:** `05-hoi-thoai-025.jsonl` còn **422 mục**.

## Khôi phục bản dịch từ GitHub

Trong nhánh có **13.596 patch records** từ các đợt 001–029 và 034–037 (bỏ qua đợt 030 vì trùng nhóm hệ thống/credit), không trùng ID. Công cụ kiểm tra của bộ nguồn xác nhận 0 lỗi cấu trúc; vẫn cần kiểm tra hiển thị sau khi bổ sung font.

```bash
python Ragnarok-DS/tools/apply_patches.py \
  --handoff RagnarokDS_USA_BanGiao_Cloud.zip \
  --patch-dir Ragnarok-DS/translation \
  --output RagnarokDS_VH_Checkpoint_037_GitHub.zip
```

Lệnh chỉ xuất ZIP dịch thuật, không chỉnh ROM hay font và không xóa dòng chưa dịch. Bản ZIP đã xuất trực tiếp trong phiên chat còn có danh bạ nhân vật và bảng thuật ngữ cập nhật.

## Kiểm tra khi nhận bản ZIP

```sh
python tools/check_handoff.py --source INPUT/translation --translation KET_QUA/translation
```

Không dùng `--require-complete` cho các đợt chưa dịch xong. Nhớ đối chiếu tên/mô tả và ảnh UI trước khi đóng gói vào game.
