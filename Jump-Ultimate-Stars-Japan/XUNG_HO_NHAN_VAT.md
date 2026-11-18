# Quy tắc xưng hô — Jump Ultimate Stars (v1)

**Nguyên tắc quan trọng:** Đây là trò chơi crossover. Quy định xưng hô theo **người đang nói × người nghe × quan hệ × tình huống**; không dùng một bảng xưng hô cố định cho mọi câu. Dữ liệu `context` chỉ cho biết tài nguyên nguồn, không luôn xác nhận danh tính người phát ngôn. Nếu chưa xác định được người nói, để ghi chú `speaker_unverified`; tuyệt đối không tự gán nhân vật theo mã tệp viết tắt.

| Người nói / quan hệ | Xưng với người nghe | Giọng và mức xác nhận |
|---|---|---|
| **JUMP Pirates → người chơi** | **ta – cậu** | ĐÃ XÁC MINH từ `battle/tutorial0.bin` và các bài hướng dẫn cùng chuỗi; hoạt bát, đầy nhiệt huyết, có thể hô hào nhưng không nhét meme. |
| **Người dẫn Info Character chưa xác nhận → người chơi** | tớ/mình – cậu, hoặc lời chỉ dẫn không xưng hô | TẠM THỜI. Kiểm tra giọng trong từng `bin/info/*.bin` trước khi chốt; không tự suy mã `bb` là Bobobo. |
| **Luffy ↔ đồng đội thân** | tớ – cậu | QUY ƯỚC ĐỀ XUẤT, cần đối chiếu lời thoại tại chỗ; bộc trực, hồn nhiên, không nói kiểu học giả. |
| **Naruto ↔ đồng đội / Sasuke** | tớ – cậu ở cảnh thân; tao – mày khi mâu thuẫn gay gắt nếu bản gốc cho phép | QUY ƯỚC ĐỀ XUẤT; tuyệt đối không tự tăng độ thù địch. |
| **Goku ↔ bạn hữu** | tớ – cậu | QUY ƯỚC ĐỀ XUẤT; thoải mái, thẳng thắn, rất mê đấu. |
| **Gintoki ↔ bạn hữu / người lạ** | tôi – cậu / tôi – anh, thay đổi theo sắc thái | QUY ƯỚC ĐỀ XUẤT; giữ lối hài tỉnh queo, không xưng bừa kiểu hạ nhục. |
| **Bobobo ↔ đối thủ** | linh hoạt theo lối chọc ghẹo của nguyên tác | CHƯA CHỐT; đừng gắn giọng Bobobo lên tất cả thông tin trợ giúp. |
| **Người kể trong Library / câu hỏi J-Quiz** | thường không xưng hô hoặc dùng lời kể khách quan | Không tự chuyển thành ngôi tôi hoặc áp cách nói của nhân vật được nhắc đến. |

## Bảng kiểm cho từng đoạn thoại

1. Từ `context` truy ra tài nguyên; nếu là đoạn ghép, đọc câu trước/sau. Người nhắc tên Naruto **không có nghĩa Naruto là người đang nói**.
2. Ghi bộ `speaker_id`, `listener_id`, `relationship`, `tone`, `confidence` khi có căn cứ. Dùng `unknown` nếu thiếu chứng cứ.
3. Dịch chính xác sắc thái Nhật: `私`/`僕`/`俺`/`わし`, `君`/`お前`/`貴様` không tự động thành một cặp Việt cố định.
4. Xưng hô có thể đổi khi đang đấu, thân thiết, tức giận, kính trọng. Bắt buộc soi truyện gốc khi nghĩa không rõ.
5. Hội thoại Gen Z **chỉ chấm nhẹ**, không gắn tiếng lóng trái tính cách hoặc lệch thời đại của manga.

## Theo dõi cần làm

- Lập `speaker_registry.jsonl` sau khi xác nhận danh tính các Info Character; mã `bb.bin` hiện chưa đủ căn cứ là một nhân vật cụ thể.
- QA xưng hô trong `02-thoai-tro-giup`, `05-thu-vien-nhan-vat`, và tương tác có tên riêng.

## Cập nhật Checkpoint 002

- **JUMP Pirates**: hoàn tất 281/281 dòng thuộc nhóm hướng dẫn; giữ “ta – cậu” qua cả phần Deck Make.
- **Info Character**: nhóm `02-thoai-tro-giup-001` dòng 75–151 giọng thân thiện, ít kéo âm; dòng 152–230 giọng kéo dài tươi vui. Hai phong cách **không tự động chứng minh** ai là người nói, vì cùng một chuỗi có thể được dùng ở nhiều tài nguyên.
- Dòng `197–198` có nhắc tên “Kyoko” (キョウコ), nhưng phải kiểm tra `context` và file nguồn theo lượt nói trước khi khóa ngôi xưng của các câu lân cận. Các câu trung tính ưu tiên cách gọi “cậu”, không gắn lời tự xưng cho người chưa biết.
- Dòng giới thiệu Ability, luật thi đấu không phải lời nhân vật, ưu tiên mô tả trung tính thay vì “ta – cậu”.

## Checkpoint 003 — giữ giọng và xưng hô theo tài nguyên

- `02-thoai-tro-giup-001`, dòng **231–273**: câu hiển thị dùng lại trong nhiều `info/*.bin`, giọng thân thiện, hạn chế tự nhận người nói (dùng “cậu”, “mình” khi có căn cứ; không gán giới).
- Dòng **274–383**: nhóm `info/bl.bin`, giọng **cộc cằn, khoác lác**, xưng “ta – ngươi”, mệnh lệnh gọn; danh tính nhân vật chưa được xác thực độc lập.
- Dòng **384–495**: nhóm `info/bu.bin`, giọng **kiêu ngạo, kiểu cách**, xưng “ta – ngươi” khi có xưng hô; chơi chữ `蝶/超` được diễn đạt tự nhiên, không tự khai tên nhân vật từ mã `bu`.
- Dòng **496–608**: nhóm giọng hướng dẫn **điềm tĩnh, hơi sắc sảo**, thường không xưng tôi hoặc dùng “tôi – cậu”; một số chuỗi dùng lại giữa các file `info/` nên **speaker_unverified**.
- `04-koma-chieu-thuc-001`, dòng **137–329**: tên và chiêu của Dragon Ball giữ bản tiếng Anh thông dụng. Đoạn trích thoại từ manga **không tự khóa speaker** khi thiếu nhãn người nói, kể cả khi nhân vật nằm gần dòng thoại.
- Những tên kỹ năng chưa đối chiếu tên tiếng Anh canonical có `status=provisional_literal_jp_qa` trong bảng thuật ngữ.

## Checkpoint 004 — quy tắc giọng nói bổ sung

- `02-thoai-tro-giup-001`, dòng **609–717**, chủ yếu `info/ct.bin`: hướng dẫn tự tin, ngắn gọn, xưng “tôi – cậu” hoặc bỏ ngôi cho câu menu. Nhóm có những dòng tái sử dụng giữa các tệp Info; không suy tự động nhân vật từ mã `ct`.
- Dòng **718–796**, `info/db.bin`: giọng nữ tự tin, hơi đá xoáy; câu hướng dẫn dùng “cậu” và không thêm tên nhân vật khi chưa được xác minh.
- Dòng **797–888**, `info/dg.bin`: giọng thân thiện, hơi nhí nhảnh, dùng “tớ – cậu” khi rõ ngôi trong nguyên tác.
- Dòng **889–980**, `info/dn.bin`: có câu tự xưng **Misa** và nhắc **Light**; giữ tên tiếng Anh và sắc thái nói hơi làm nũng, không biến lời của nhân vật thành lời thuyết minh chung. Nhiều câu có `uses` lớn hơn 1 dùng chung giữa các `info` khác: tránh đổi ngôi quá đặc thù ở những dòng ấy.
- `04-koma-chieu-thuc-001`, dòng **330–561**: phân biệt **tên nhân vật / tên Skill / furigana / mô tả cơ chế / lời trích manga**. Tên người, Skill, Item giữ tiếng Anh (đặt tên chưa chắc vào bảng `provisional_literal_jp_qa`); lời trích được dịch đúng sắc thái, chưa tự gán nguồn speaker nếu không có metadata xác minh.
- Tuyệt đối không đọc cặp dòng văn bản tách ra như hai câu độc lập nếu chúng ghép thành một câu dài. Mỗi ID giữ đúng mảnh ý để màn hình nối lại tự nhiên.

## Checkpoint 005 — Info Character và Naruto

- `02-thoai-tro-giup-001`, dòng 981–1088 (`info/ds`): lịch thiệp, tươi vui, có lối nói kéo đuôi; dùng **cậu**, chỉ tự xưng khi câu gốc có căn cứ. `先生` tại dòng 1020 dịch trung tính **người hướng dẫn**, **không suy ra danh tính**.
- Dòng 1089–1156 (chủ yếu `info/es`): hướng dẫn điềm tĩnh; dùng **mình – cậu** khi có chủ ngữ và phù hợp.
- Dòng 1157–1275 (chủ yếu `info/gt`): người nói cứng cỏi, khẩu ngữ kiểu lớn tuổi; lời mời và mệnh lệnh gần gũi, tránh tự xác quyết giới tính/người nói từ tên tệp.
- Dòng 1276–1371 (chủ yếu `info/hh`): giọng khẩu ngữ, quả quyết, có nhịp riêng, tránh gán danh tính.
- Dòng 1372–1447 (chủ yếu `info/hk`): hướng dẫn dịu, rõ ràng. Dòng 1443 là **mảnh câu** dùng chung, cần đối chiếu bản hiển thị.
- `04-koma-chieu-thuc-001`, dòng 562–703: giới thiệu Naruto Uzumaki, Sasuke Uchiha, Sakura Haruno, Kakashi Hatake và Nine-Tails Naruto. Tên người/Skill dùng Anh hoặc phiên âm chuẩn; riêng một số tên thuật do game đặt được đánh dấu **provisional_literal_jp_qa** trong `THUAT_NGU.json`.
- Câu trích manga không đương nhiên do nhân vật đang được giới thiệu phát ngôn. Chỉ suy giọng từ ngữ pháp Nhật rõ ràng; **không khóa speaker_id** khi chưa kiểm tra Koma/nguồn manga.
- `すれちがい通信` của NDS **không phải StreetPass 3DS**; diễn đạt là kết nối/trao đổi dữ liệu khi đi ngang nhau.

## Checkpoint 006 — Info Character, Shaman King, JoJo, Hunter × Hunter và Yu Yu Hakusho

- `02-thoai-tro-giup-002` dòng 0–1: cuối nhóm `info/hk`; chưa xác nhận danh tính.
- Dòng 2–114, chủ yếu `info/hs`: giọng `っス`, hoạt bát, thân thiện. Dùng **tớ – cậu** nếu ngữ cảnh yêu cầu; không tự gán tên từ mã `hs`.
- Dòng 115–227, chủ yếu `info/ig`: lịch thiệp, có `あたし` tại dòng 157. Có thể dùng **tôi – cậu**, thi thoảng chọc ghẹo nhẹ theo nguyên tác.
- Dòng 228–305, chủ yếu `info/is`: vui, gần gũi; ưu tiên **tớ – cậu** khi rõ xưng hô, hạn chế gán người nói ở chuỗi dùng chung.
- Dòng 306–360, chủ yếu `info/jj`: điềm tĩnh, hơi kiểu cách; dùng **tôi – cậu** hoặc bỏ ngôi ở câu hướng dẫn.
- `04-koma-chieu-thuc-001` dòng 704–963: **Shaman King**, **JoJo's Bizarre Adventure**, **Hunter × Hunter**, **Yu Yu Hakusho**. Văn bản mô tả cơ chế không cần xưng hô; lời trích nhân vật được giữ sắc thái nhưng chưa khóa `speaker_id` nếu dữ liệu thiếu căn cứ.
- Các Skill romanized/provisional chưa phải English chính thức. Giữ các thẻ `<IDEOSP>`, `<PERCENT_FULL>` đúng thứ tự; không biến NDS thành StreetPass 3DS.

