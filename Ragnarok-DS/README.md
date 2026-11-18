# Ragnarok DS (USA) — Việt hóa NDS

Nhánh độc lập `vh/ragnarok-ds-usa` của kho `VH-NDS`. Không trộn với các dự án Ni no Kuni, Magician’s Quest hoặc Ragnarok Odyssey ACE.

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

## Khôi phục bản dịch từ GitHub

Trong nhánh có **4.914 patch records** từ các đợt 001–012, không trùng ID. Công cụ kiểm tra của bộ nguồn xác nhận 0 lỗi cấu trúc; vẫn cần kiểm tra hiển thị sau khi bổ sung font.

```bash
python Ragnarok-DS/tools/apply_patches.py \
  --handoff RagnarokDS_USA_BanGiao_Cloud.zip \
  --patch-dir Ragnarok-DS/translation \
  --output RagnarokDS_VH_Checkpoint_012_GitHub.zip
```

Lệnh chỉ xuất ZIP dịch thuật, không chỉnh ROM hay font và không xóa dòng chưa dịch. Bản ZIP đã xuất trực tiếp trong phiên chat còn có danh bạ nhân vật và bảng thuật ngữ cập nhật.

## Kiểm tra khi nhận bản ZIP

```sh
python tools/check_handoff.py --source INPUT/translation --translation KET_QUA/translation
```

Không dùng `--require-complete` cho các đợt chưa dịch xong. Nhớ đối chiếu tên/mô tả và ảnh UI trước khi đóng gói vào game.
