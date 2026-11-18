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


## Checkpoint 006 — các nhóm Info Character, Shaman King, JoJo, Hunter × Hunter và Yu Yu Hakusho

- `02-thoai-tro-giup-002` dòng 0–1: cuối nhóm `info/hk`; chưa tự gán danh tính.
- Dòng 2–114, chủ yếu `info/hs`: lối nói `っス`, thân thiện, hơi nhí nhảnh; dùng **tớ – cậu** nếu cần xưng hô, không xác định tên từ mã `hs`.
- Dòng 115–227, chủ yếu `info/ig`: lịch thiệp, tự xưng `あたし` tại dòng 157; có thể dùng **tôi – cậu**, một số đoạn chọc ghẹo nhẹ theo gốc.
- Dòng 228–305, chủ yếu `info/is`: trẻ trung, chọc nhẹ, dùng **tớ – cậu** khi ngữ cảnh cho phép; hạn chế tự xưng ở dòng đa dụng.
- Dòng 306–360, chủ yếu `info/jj`: điềm đạm và hơi kiểu cách, dùng **tôi – cậu** và câu hỏi lịch sự.
- `04-koma-chieu-thuc-001` dòng 704–963: nhóm **Shaman King**, **JoJo's Bizarre Adventure**, **Hunter × Hunter** và **Yu Yu Hakusho**. Các mô tả cơ chế không có nhân xưng; thoại nhân vật có thể giữ sắc thái riêng nếu câu Nhật thể hiện rõ, nhưng chưa gán speaker từ vị trí kế bên trong tệp.
- Giữ nguyên các dấu phân mảnh `IDEOSP` và `PERCENT_FULL` theo thứ tự Nhật; thuật ngữ phiên âm được ghi cờ cần đối chiếu.

## Checkpoint 007 — Wi-Fi / Info Character và các manga mới

- `02-thoai-tro-giup-002`, dòng **361–387**, chủ yếu tệp `info/jj.bin`: giọng điềm đạm, hơi kiểu cách; ưu tiên **tôi – cậu** hoặc lược chủ ngữ. Dòng 370 có tự xưng **Kishibe Rohan** từ chính lời thoại, không tự áp tên này cho những câu dùng lại ở tài nguyên khác.
- Dòng **388–573**: các mảng hướng dẫn hệ thống (Jump Galaxy, Koma, Deck, Friend, Wi-Fi, Quiz và giao diện Deck Make). Nhiều câu bị cắt giữa hai ID: giữ đúng thứ tự và dấu phân cách; không thêm xưng hô vào mô tả cơ chế.
- Dòng **574–683**: kiểu nói Kansai với `うち` và `～やで`, chuyển thành giọng **tui – cậu** thân thiện, nhịp nhanh, trêu nhẹ, **không** tự gán nhân vật qua mã tài nguyên.
- Dòng **684–764**: phong cách hướng dẫn động viên, có `ユー` (you) và `セコンド` (người hỗ trợ); dùng **tôi – cậu** khi cần; thuật ngữ kết nối giữ đúng công nghệ NDS.
- Dòng **765–853**: giọng thô, hơi bất cần (`～やがれ`, `～ねぇ`), dùng câu gọn, cà khịa vừa phải; không thêm tục tĩu mới vào bản dịch.
- `04-koma-chieu-thuc-001`, dòng **964–1133**: **Yu-Gi-Oh!**, **Rurouni Kenshin**, **Black Cat**, **Bleach**. Tên người và Skill giữ tiếng Anh/phiên âm. **Phần mô tả gameplay không phải lời nhân vật**, không gán người nói theo vị trí. Lời trích manga giữ sắc thái nhưng `speaker=unverified` nếu không có metadata.
- Các tên Skill có `status=romanized_japanese_qa` hoặc `provisional_literal_jp_qa` cần QA trước khi chốt bản patch; chúng **không mặc nhiên là tên tiếng Anh chính thức**.


## Checkpoint 009 — Info Character và Koma/Skill (18/11/2026)

- `02-thoai-tro-giup-003.jsonl` 0–129 (`info/pj.bin`): giọng **tsundere**, hơi hách dịch và ngượng ngùng. Dùng **tôi–cậu**, không tự đặt thêm tên người nói; tiếng lóng vừa phải, câu nhiều ID ghép liền.
- Dòng 130–227 (`info/rb.bin`): giọng **mạnh mẽ, trực tính**, nói gọn, có thể tự xưng **ta**, gọi người chơi **cậu**; không suy nhân vật.
- Dòng 228–279 (`info/rk.bin`): giọng **nữ tự tin**, bình tĩnh, hơi khịa nhẹ, dùng **tôi–cậu** khi tự xưng.
- Dòng 280–353 (`info/sd.bin`): lịch thiệp, chậm rãi, có tiếng cười `ほっほっ`; ưu tiên lời chỉ dẫn rõ, không tự xác định danh tính.
- Dòng 354–421 (`info/sk.bin`): giọng **trẻ, hơi rụt rè**, câu ngắn, dùng **mình–cậu** khi nguyên tác có ngôi.
- Dòng 422–504 (`info/ss.bin`): trang trọng, hướng dẫn hùng hồn, thuật ngữ **Cosmo** theo Saint Seiya; có thể dùng **ta–ngươi** khi gốc có chủ ngữ. Chưa xác định người nói ở những câu dùng chung.
- `04-koma-chieu-thuc-002.jsonl` 0–165: các dòng **Skill/Ability** giữ tên tiếng Anh/romanized; các dòng mô tả là trung tính. Lời trích manga giữ dấu hiệu giọng Nhật; vị trí gần tên nhân vật không tự chứng minh danh tính người nói.
- Các mục `provisional_english_qa` trong bảng thuật ngữ không phải tuyên bố về tên dịch chính thức. Đoạn Nhật bị cắt giữa từ (như `けを締め切った`, `しれない`) cần QA theo cảnh game khi có ROM writer.


## Bổ sung CP010 — các nhóm trong `02-thoai-tro-giup-003.jsonl`

- Dòng **505–564**: người hướng dẫn nữ thẳng thắn; chỉ thị trực diện, không ép cách xưng hô cố định; **speaker chưa xác minh**.
- Dòng **565–664**: người hướng dẫn hào hứng, hô hào chiến thắng; thường dùng câu thúc giục có dấu `!`; **speaker chưa xác minh**.
- Dòng **665–719**: giọng nam điềm tĩnh, dứt khoát; dùng “ta – cậu” khi nguồn buộc xưng hô; **speaker chưa xác minh**.
- Dòng **720–790**: hướng dẫn giọng nữ thân thiện, nhiều “nha”, “nè”, “tớ”; **speaker chưa xác minh**.
- Dòng **791–834**: giọng nữ sắc sảo, kiệm lời; không cố tình tăng mức xúc phạm; **speaker chưa xác minh**.
- Dòng **835–907**: giọng nữ chững chạc, hơi bông đùa. **Dòng 868–869 nêu đích danh Botan** (“このぼたんちゃん”), nhưng không mặc định mọi ID bên ngoài cụm này đều do Botan nói.
- Dòng **908–957**: giọng nữ hoạt bát; **speaker chưa xác minh**.
- Koma 002 dòng **166–365** đi qua Jaguar, Arale, Dr. Mashirito, Muhyo, Neuro/Yako, Kenshiro. Phân biệt **câu mô tả gameplay** và **câu thoại có người nói**, không tự chọn ngôi bằng tên Koma đứng cạnh.

**Chú ý:** tên Skill ít phổ biến là bản English tạm/romanized và có trạng thái QA trong `THUAT_NGU.json`. Không tuyên bố đã đối chiếu localized English chính thức.


## Bổ sung CP011 — `04-koma-chieu-thuc-002.jsonl` dòng 366–1054

- Dòng 366–426: Kenshiro và Raoh (Fist of the North Star). Trong đoạn Ken nói với người thân/bằng hữu dùng “cậu/tớ”, lời Raoh và các cao thủ dùng “ta/ngươi” **chỉ khi câu gốc hỗ trợ**. Không tự coi tất cả các câu thuộc Koma Kenshiro là lời Kenshiro.
- 427–470: Saint Seiya. Giữ Seiya, Cosmo, Pegasus, Sagittarius; nhóm thoại gốc thiên về tình anh em và hy sinh, tránh nhét câu đùa quá trớn.
- 471–517: Kinnikuman. Mô tả gameplay trung tính, thoại hoàng tử/đồng đội dùng sắc thái cổ vũ thân thiện; Kinnikuman có chất hài nhưng không thêm ý ngoài bản Nhật.
- 518–568: Otokojuku. Edajima nói đầy uy quyền; Momotaro và các bạn chiến đấu khí chất võ hiệp. Người giữ chức quyền: cách xưng “ngài/tôi” nếu thoại gốc thể hiện.
- 569–601: Taikobo (Houshin Engi). Giọng Taikobo thư thái, nhưng tài trí; thuộc hạ dùng “chủ nhân”. Không gán cứng người nói trong những câu thiếu speaker.
- 602–626: Ninku; Fuusuke, Aichou, Toji; nhân vật gọi thân mật tùy thoại gốc. Dòng 615 dùng Aichou theo đối chiếu danh sách nhân vật, không gán nhầm Aira.
- 627–701: Koma mascot, Dragon Ball, One Piece. Giữ tên chiêu, tránh đổi “J-Soul”, “Special Soul” giữa các đoạn.
- 702–895: One Piece, Naruto, Shaman King, JoJo, Hunter × Hunter. Các câu trong phần mô tả **không được mặc định là lời thoại** chỉ vì gần tên nhân vật.
- 896–1054: Yu Yu Hakusho, Yu-Gi-Oh!, Rurouni Kenshin, Black Cat, Bleach. Giữ nguyên tên Skill/Stand/Zanpakuto bằng tiếng Anh hoặc phiên âm; trạng thái ``_qa`` cho tên chưa xác nhận phiên bản tiếng Anh.

**Chú ý:** Bản Nhật tách nhiều câu thành 2–3 ID liên tiếp. Dịch có tính liên kết nhưng không được gộp ID hoặc xóa thẻ `<IDEOSP>`. Các thoại chưa xác minh người nói không tự tạo quan hệ xưng hô mới.


## Bổ sung Checkpoint 012 — hệ thống xưng hô và tên riêng

- `04-koma-chieu-thuc-002.jsonl` dòng 1055–1363: **Bleach**, **D.Gray-man**, **Bobobo-bo Bo-bobo**, **Kochikame**, **Gintama**, **Reborn!**. Phần lớn là mô tả Skill trung tính, không tự quy là lời nhân vật. Tên người, Skill và dạng phiên âm giữ chữ Latinh; tên chưa xác nhận ghi `working_romanization_qa`.
- **Gintama:** Gintoki/Kagura/Shinpachi dùng xưng hô thân mật theo ngữ cảnh, không ép mọi câu thành kiểu cộc cằn. Hijikata/Okita/Kondo thuộc Shinsengumi có vai vế rõ ràng, nhưng nhãn Skill không phải thoại trực tiếp.
- **Reborn!:** Reborn hướng dẫn sắc sảo; Lambo trẻ con, dễ bị tổn thương; Gokudera rất kính trọng Tsuna; Yamamoto thân mật. Chỉ áp dụng các sắc thái này khi xác nhận được người nói, không thêm vào mô tả cơ chế.
- `04-koma-chieu-thuc-003.jsonl` dòng 0–300: **Reborn!**, **Jaguar**, **Dr. Slump**, **The Prince of Tennis**, **Eyeshield 21**, **Slam Dunk**, **Death Note**. Chú ý manga Slam Dunk cần trầm hơn ở lời động viên; Death Note nghiêm túc, không nhét tiếng lóng vào lời phán quyết.
- Độ dí dỏm chỉ dùng cho tình huống nguyên gốc hài (Bobobo/Gintama/Jaguar). Không tự chế chiêu thức, luật chơi hoặc quan hệ.


## Bổ sung Checkpoint 013 — Death Note và dàn Koma hỗ trợ

- `04-koma-chieu-thuc-003.jsonl` dòng 301–1006 là **nhãn nhân vật, tên Skill và mô tả cơ chế**, không mặc nhiên là câu nói trực tiếp của nhân vật. Không gán ngôi xưng tùy tiện cho phần mô tả.
- **Near / Mello (Death Note):** tên giữ Latin; Near bình tĩnh, phân tích; Mello nóng nảy, quyết liệt. Khi là mô tả cơ chế, giữ văn phong khách quan, không tự nhét thoại vào.
- **Ichigo 100%:** Aya Tojo dè dặt, Tsukasa Nishino thẳng thắn, Satsuki Kitaoji hoạt bát; lời thoại đúng nhân vật mới được áp dụng giọng, không suy từ tên Skill.
- **Muhyo & Roji:** thuật ngữ pháp thuật giữ tên Latin nhất quán. Roji rụt rè; Yoichi nhanh nhẹn; phần cơ chế chỉ dùng diễn đạt khách quan.
- **Saint Seiya:** tôn trọng cách gọi Saints, Athena, Cloth; không tự chuyển lời mô tả sang kiểu 'ta–ngươi'.
- **Kinnikuman, Captain Tsubasa, Dr. Slump, Luckyman:** tên chính thức/Latin được ưu tiên; chất hài chỉ thêm khi có nền từ bản Nhật, tránh tự bịa biệt danh và đòn đánh.
- **Tên rút gọn trong danh sách cuối file:** dịch sang Latin phổ biến theo ngữ cảnh franchise (ví dụ `悟空` → Goku, `一護` → Ichigo). Một số tên ngắn mơ hồ vẫn đánh dấu `character_name_qa` để kiểm tra với hình Koma/ROM.


## CP014 — Thư viện nhân vật (Bobobo / Black Cat / Bleach)

- **Các đoạn tiểu sử và tóm tắt truyện** là giọng người kể chuyện, không tự động gán nhân vật trong tiêu đề là người phát ngôn. Ưu tiên câu kể không xưng hô.
- **Bobobo và Don Patch**: hoạt bát và phi lý, được pha chút giọng hài; khi có lời quát đối thủ có thể dùng “ta – ngươi / mày”, nhưng chỉ theo sắc thái câu Nhật.
- **Beauty**: thường là người phản ứng, tức giận trước trò lố của đồng đội; không dịch thành tục tĩu.
- **Eve → Sven/Train**: giữ sắc thái còn nhỏ, chủ động, đôi khi ghen với Train vì muốn thành bạn đồng hành của Sven; ưu tiên “em – anh” khi thật sự là lời thoại trực tiếp, không áp cho lời kể.
- **Train → Creed**: đối địch, có thể dùng “ta – ngươi” khi câu Nhật cứng rắn; **Train → Saya**: giọng dịu hơn, thân thiết.
- **Ichigo → Byakuya**: căng thẳng, nói thẳng; **Renji → Byakuya**: vẫn tôn trọng chức đội trưởng trong lời gọi chính thức, dù quyết vượt qua; **Toshiro → Gin**: cảnh cáo gay gắt khi Momo gặp nguy hiểm.
- **Rukia → Ichigo**: thân thiết nhưng có lối nói hơi cổ; **Kon → Rukia**: ngưỡng mộ quá mức, nên giữ sự lố bịch kiểu nguyên tác.
- Những ngôi xưng này là **quy tắc dịch theo cảnh**; từng trích dẫn thư viện cần soát nguồn manga trước khi xác định speaker chắc chắn.


## CP015 — Bleach / Buso Renkin / Cobra / Captain Tsubasa / Dragon Ball

- **Thư viện nhân vật**: phần tiểu sử dùng giọng kể thứ ba, không suy ra nhân vật đang tự nói; chỉ dùng đại từ khi có lời thoại trực tiếp được trích dẫn.
- **Uryu Ishida**: kín đáo, tự trọng, lời thề với Mayuri mạnh nhưng không văng tục; giữ tên Quincy, Ransotengai và Ashisogi Jizo.
- **Chad**: trầm, ít nói, với Shunsui dùng “tôi”, thái độ kiên định nhưng có lễ. **Orihime**: thân mật với Tatsuki, cảm xúc rõ mà không biến thành lời nói nhõng nhẽo tùy tiện.
- **Yoruichi**: điềm nhiên, tự tin, trêu chọc khi thích hợp; trong lời đối đầu Soi Fon có thể xưng “ta”, không mặc định mọi cảnh. **Byakuya**: lời ngắn, lạnh và trang trọng; không dùng slang tùy tiện. **Aizen**: lịch thiệp, lạnh nhẫn. **Kon**: lố, háo sắc theo nguyên tác nhưng tránh tự thêm lời tục.
- **Kazuki → Tokiko**: Kazuki trẻ, thẳng thắn, gọi “chị Tokiko” khi lời Nhật cho thấy sự kính trọng (斗貴子さん); lời kể bên ngoài không tự áp quan hệ. **Papillon**: khoa trương nhưng vẫn giữ sự u ám của tiểu sử.
- **Cobra**: tự tin, bông đùa kiểu giang hồ không gian; với Crystal Boy dùng “ta – ngươi” ở lời đe dọa. **Lady**: thông minh, chuyên nghiệp; robot hầu gái nói vụng thì dịch vụng có chủ đích.
- **Captain Tsubasa**: Tsubasa/Misaki dùng “tớ – cậu” trong cảnh đồng đội; Hyuga mạnh mẽ, hiếu thắng; nhân vật trẻ không bị lão hóa giọng.
- **Goku**: vô tư, giản dị, hồn nhiên kể cả khi kết hôn; lúc nổi giận chuyển giọng dữ dội có căn cứ. **Vegeta**: kiêu ngạo “ta – ngươi” khi nói với kẻ thù; câu thoại của Vegeta không pha hài trừ khi Nhật gốc đã hài.
- Các nguyên tắc trên là **đề xuất theo cảnh đã dịch**, không coi là speaker ID cố định; cần QA với ảnh thực tế trên NDS.


## Checkpoint 016 — nhóm Dragon Ball, D.Gray-man, Death Note

- **Vegeta** trong trích thoại: cách nói ngạo nghễ, khiêu khích; có thể xưng “ta – ngươi” với đối thủ, nhưng trong lời cuối với Trunks/Bulma dùng giọng cha/chồng trầm lắng. Lời kể trong Library giữ ngôi thứ ba.
- **Gohan** thuở nhỏ: “cháu/con” với người lớn, Goku/Piccolo; khi phẫn nộ xưng hô gắt hơn nhưng không tự chèn tiếng lóng.
- **Piccolo** đối đầu Raditz/Frieza: nói ngắn, cứng; với Gohan là thầy trò, kín tiếng nhưng quan tâm. **Gotenks** tự tin và trẻ con, **Frieza** điềm tĩnh nhưng tàn nhẫn.
- **Allen Walker** với người khác: lịch sự, dùng “tôi/cậu” tùy đối tượng, không tự đổi thành giọng bặm trợn; **Lenalee** với Allen: thân thiện, giữa cô với **Komui** dùng “em – anh”.
- **Kanda** cáu kỉnh, gọi Allen là “giá đỗ”, giữ sự đối lập với giọng Allen; **Lavi** vui vẻ, có chất khẩu ngữ nhưng tránh bịa phương ngữ vượt chứng cứ.
- **Light Yagami** trong lời độc thoại Kira: lạnh và chắc thắng; **L/Near** hỏi đáp bình tĩnh, lập luận rành rọt; **Misa** có giọng hồn nhiên và hâm mộ Light; **Mello** nóng nảy, cạnh tranh với Near.
- Các tiểu sử là **người dẫn chuyện ngôi thứ ba**. Không lấy một câu dẫn trích (`『...』`) làm bằng chứng tất cả dòng kề bên đều do nhân vật đó phát ngôn.


## Checkpoint 017 – Dr. Slump / Eyeshield 21 / Gintama

- **Arale:** ngây thơ, vô tư; lời chào đặc trưng “N'cha!”. Với Senbei, dùng giọng trẻ con, thân mật; không tự thêm lời cà khịa của người lớn. **Senbei:** người lớn, thường xưng “ta/ông” hoặc “chú” theo đối tượng, nhưng câu trần thuật phải ở ngôi thứ ba. **Obotchaman:** lễ phép, có thể dùng “cháu/em” với người lớn, “tớ/cậu” với Arale tùy cảnh. **Dr. Mashirito:** tự tôn quá mức, thường “ta/ngươi”, không dùng kiểu nói teen vô cớ.
- **Sena:** hiền, lịch sự; với Hiruma và đàn anh: “em/anh” khi thực sự nói chuyện, với bạn cùng lớp: “tớ/cậu”. **Hiruma:** cộc và áp đặt; “tao/mày” chỉ ở cảnh đối đầu/đe dọa, không áp dụng vào lời dẫn của thư viện. **Kurita:** chân thành, nhẹ nhàng. **Shin:** chừng mực, nghiêm túc.
- **Gintoki:** nói năng tùy hứng, đôi lúc cộc và ngông nhưng không biến mọi câu thành tục tĩu. Với **Shinpachi**, thường “anh/cậu” hoặc “tôi/cậu” theo ngữ cảnh. **Shinpachi:** giữ vai người thường tỉnh táo, kính trọng người lớn hơn khi thích hợp nhưng có thể bật lại bằng “anh/tôi”. **Kagura:** bộc trực, tinh nghịch, không cần máy móc thêm đuôi tiếng Nhật “aru” vào mọi câu tiếng Việt; vẫn giữ đặc trưng qua nhịp điệu và từ ngữ.
- Các dòng phần lớn là **lời kể/tiểu sử**. Chỉ sử dụng ngôi xưng trực tiếp trong đoạn trích/đối thoại được nguồn đánh dấu. Khi file không có người nói thì không tự gắn tên.
- Những tên chiêu được tạm Latin hóa phải mang nhãn QA, tuyệt đối không nhận là official English khi chưa kiểm chứng.


## Checkpoint 018 – Gintama / Hunter × Hunter / Fist of the North Star / Hoshin Engi
- **Gintama:** giọng dẫn tiểu sử trung tính; với lời thoại phải xét người nói. Katsura có lối nói nghiêm túc, thích chỉnh “Zura” thành “Katsura”. Sacchan nói đùa khá lố khi ở cạnh Gintoki; Hijikata thẳng, nóng tính, nghiện mayonnaise; Okita có nét bình thản mà hiểm. Kondo chân thành, hơi ngốc và bám Otae. Không tự chuyển câu kể thành thoại của nhân vật.
- **Hunter × Hunter:** Gon bộc trực, dùng “tớ/cậu” với Killua trong tình huống thường; Killua nhanh nhạy và mạnh miệng nhưng không tự biến thành kiểu xấc xược. Kurapika kiềm chế, nghiêm nghị; Hisoka đùa cợt nguy hiểm; Chrollo điềm tĩnh, lạnh lùng. Hệ Nen/Skill giữ tên tiếng Anh hoặc phiên âm nhất quán.
- **Fist of the North Star:** Kenshiro và Raoh mang giọng uy nghiêm, trực diện; Toki trầm tĩnh; Rey/Rei nghĩa hiệp. Trong trích dẫn từ manga phải bám sát ngữ cảnh (anh/em, ta/ngươi, tôi/anh) thay vì khóa ngôi xưng một kiểu cho cả thư viện.
- **Hoshin Engi:** Taikobo có nét lười biếng hài hước, nhưng ở cảnh nghiêm túc nói sắc sảo; tránh thêm mảng miếng ngoài bản Nhật. Các tên riêng Taikobo, Dakki, Taikyokuzu, Super Paopei giữ tiếng Anh hoặc phiên âm; từ nào chưa chắc chuẩn chính thức cần QA.
- Tất cả văn bản của `05-thu-vien-nhan-vat-003.jsonl` đã có bản Việt; `05-thu-vien-nhan-vat-004.jsonl` hiện đã dịch 300 dòng đầu (0–299).

## Checkpoint 019 — thư viện nhân vật 004 (dòng 300–948)

- **Hoshin Engi (300–365):** Taikobo có giọng thoải mái, đôi lúc cố tình đùa; Dakki tự xưng cao ngạo (`わらわ`), dùng **ta – ngươi** trong câu đe dọa, không biến lời kể thành câu của Dakki. Otenkun lạnh lùng; Supushan thân thiết với Taikobo, không tự gán ngôi cho lời tiểu sử.
- **Ichigo 100% (366–494):** Aya, Tsukasa, Satsuki, Yui và Junpei là học sinh thân quen: **tớ – cậu** khi nhân vật trò chuyện. Những cảnh tỏ tình, từ chối, chia tay giữ cảm xúc thật, không cà khịa vô cớ. Tên nhân vật Latinh, không Việt hóa tên riêng. **I''s (495–566):** Ichitaka, Iori, Itsuki cùng thế hệ; dùng **tớ – cậu**, biệt danh **Icchan** giữ như gốc. Tránh nhập nhằng hai truyện có tên gần giống nhau.
- **JoJo (567–862):** Jotaro ngắn gọn, kiệm lời (“Yare yare daze” giữ phiên âm); DIO khoa trương, khinh địch, có thể **ta – ngươi** khi đối đầu. Joseph lanh lợi, Josuke dễ bùng nổ vì bị chê tóc, Giorno nghiêm túc với giấc mơ, Jolyne quyết đoán. **Stand names, Hamon, Star Platinum, The World, Crazy Diamond, Gold Experience, Stone Free, Steel Ball Run** giữ tên Anh. Lời tường thuật không tự đổi thành góc nhìn của nhân vật.
- **Kochikame (863–948):** Ryotsu bộc trực, giọng đời thường/hài khi truyện có chất chọc cười; Ohara nghiêm khắc với cấp dưới. Không gọi Ryotsu theo quân hàm bịa ra, không thêm slang nếu đoạn kể nghiêm túc.
- Các dòng Nhật bị chia ở giữa từ/câu: luôn ghép mạch nghĩa liên tiếp nhưng ghi lại đúng một trường `vi` cho mỗi `id`, không chuyển token `<IDEOSP>` sang ID khác. **Tất cả đoạn này là nội dung tiểu sử hoặc trích thoại, chưa phải xác nhận speaker_id của engine.**


## Checkpoint 020 — Kochikame / Kinnikuman / Midori no Makibao

- **Kochikame:** Ryotsu gọi Ohara là sếp, nói bông đùa/cà khịa; Ohara mắng Ryotsu theo vai cấp trên nghiêm khắc. Nakagawa, Reiko lịch thiệp hơn; câu thuyết minh giữ ngôi thứ ba. Không tự gán lời kể cho nhân vật.
- **Kinnikuman:** Kinnikuman nhiệt huyết, đôi lúc hậu đậu; Robin Mask và Terryman chững chạc; Warsman ít lời, lạnh lùng. Giữ tên Kinniku Buster, Kinniku Driver, Face Flash, Robin Special và Kaji-ba no Kuso Chikara; không dịch tên chiêu như tên chính thức.
- **Midori no Makibao:** Makibao và Cascade là đối thủ truyền cảm hứng cho nhau; phần kể trận đua dùng giọng thể thao rõ ràng. Chubei tự nhiên, bộc trực. Chưa có bằng chứng câu thoại cụ thể thuộc về người nào thì không ép cách xưng hô.
- **Lưu ý:** Khi Nhật gốc bị cắt thành nhiều ID, bản dịch có thể nối giữa các dòng; chỉ kết luận ngôi xưng sau khi xem cả cảnh. Tên chưa xác minh English chính thức vẫn có trạng thái provisional trong bảng thuật ngữ.


## Checkpoint 021 — Muhyo & Roji / Naruto / Nube / Ninku

- **Muhyo → Roji:** Muhyo nói cộc, hay mỉa mai, có thể xưng “tôi–cậu” hoặc bỏ chủ ngữ. Roji/Rosie nói nhẹ nhàng, nhiệt tình, dùng “tớ–cậu” khi phù hợp. Giữ tên nhân vật theo bảng thuật ngữ dự án là **Roji**.
- **Enchu → Muhyo:** giọng nhẫn tâm, thù hận nhưng kiềm chế, xưng “tớ–cậu” khi nhắc quan hệ học trò cũ; không tự gán người nói ở đoạn kể. Yoichi bông đùa, Biko trẻ con, Page điềm tĩnh.
- **Naruto/Sakura/Sasuke:** Naruto xưng “tớ–cậu” với Sakura và Sasuke khi thân quen, nóng nảy khi đối đầu Orochimaru. Sakura nóng tính nhưng quan tâm đồng đội; Sasuke ít lời, lạnh lùng; Kakashi bình thản, nói như thầy với trò. Không đổ giọng Gen Z quá mạnh vào những cảnh bi kịch.
- **Nube/Yukime:** Nube nói với học trò bằng vai thầy, Yukime nói dịu dàng với Nube; chỉ bật chất địa phương khi nguồn có dấu hiệu rõ.
- **Ninku:** Fuusuke hồn nhiên và tốt bụng, bùng nổ khi bạn bè bị đe dọa. Toji, Aichou là đồng đội; các tên Ninku-ro, Ninei-bara, Kokoro no Ie và Shaka no Akashi là phiên âm *provisional* để đối chiếu sau.
- **Mã game:** giữ `<IDEOSP>` theo từng ID, không chuyển sang hàng khác. Tên Skill, Item, nhân vật chính và thuật ngữ quan trọng giữ tiếng Anh/romaji theo glossary.


## Checkpoint 022 — Neuro / Otokojuku / One Piece

- **Neuro và Yako:** Neuro tự xưng “ta”, gọi đối phương “ngươi” trong các câu ra lệnh/đe dọa; Yako phản ứng đời thường, đôi khi lúng túng, không biến thành giọng vô lễ. Lời kể hồ sơ dùng ngôi thứ ba. Akane-chan chủ yếu là tóc được hồi sinh, không tự gán thoại.
- **Otokojuku:** Edajima uy quyền, xưng “ta” trong lời tuyên bố; Momotaro nghiêm nghị, dứt khoát, coi trọng đồng đội. Hien lịch sự (“tôi – anh”), J pha tiếng Anh nhưng không viết lại những câu English gốc bằng tên đòn khác. Những tên võ phái/chiêu hiếm được giữ romanization và gắn nhãn QA, không nhận là tên chính thức.
- **One Piece:** Luffy thẳng thắn, đơn giản, xưng “tớ – cậu” với đồng đội khi cần; Zoro ít lời, quyết đoán; Nami lanh lợi, đôi lúc trêu; Sanji lịch lãm với phụ nữ và cộc cằn với đối thủ; Robin điềm đạm, ít lời; Franky khoa trương, hài tự nhiên; Usopp khoác lác nhưng rất tình cảm; Chopper trẻ con, ngây thơ. Không lạm dụng Gen Z trong cảnh bi thương như Robin muốn sống, lời Zeff tiễn Sanji.
- **Speaker QA:** Đoạn tóm tắt truyện chỉ là người dẫn, không tự gán câu văn là lời nhân vật. Chỉ dùng dấu trích dẫn và xưng hô khi Nhật gốc cho thấy lời nói trực tiếp.
- **Nối 006→007:** Hồ sơ Usopp tiếp tục sang file 007, không cắt bỏ ý câu về trò 'búa 5 tấn'. Đoạn Chopper được dịch trọn để checkpoint dừng tại điểm chuyển nhân vật Shanks.


## Checkpoint 023 – quy tắc thư viện nhân vật 007

- **One Piece – Shanks:** lời kể trung tính; câu Shanks dặn Luffy dùng giọng đàn anh ân cần (anh–em).
- **Pyu to Fuku! Jaguar:** Jaguar quái chiêu, đanh nhây; Piyohiko bình thường, hay bất lực; Hamer thích phô trương, tự xưng *tại hạ* khi làm màu. Không gán ID người nói chỉ dựa vào vị trí.
- **Rokudenashi Blues:** Taison nói mạnh, cộc, nghĩa khí; Nanase Chiaki nói dịu. Những câu trích nguyên văn có giọng gắt được giữ sắc thái, không áp dụng cho lời kể.
- **Rurouni Kenshin:** Kenshin thường lịch sự, khi trở lại Battosai nghiêm và sắc; Sanosuke dùng giọng bạt mạng; Saito tiết chế, lạnh; Shishio trịch thượng. Dùng anh–em với Kaoru ở câu hứa đón cô; ngoài ngữ cảnh này không mặc định xưng hô.
- **Slam Dunk:** Hanamichi tự tin hài hước; Rukawa ít lời, sắc lạnh; Akagi nghiêm; Mitsui cứng đầu nhưng giàu tình cảm; lời kể thể thao giữ tính mô tả.
- **Shaman King:** Yoh nói thoải mái, dùng mình hoặc tớ tùy người nghe; tên kỹ năng/thuật ngữ chính để nguyên.

Các tên Romanization có trạng thái `working_romanization_qa` cần so lại với ấn bản chính thức trước khi khóa thuật ngữ.


## Checkpoint 023 – quy tắc thư viện nhân vật 007

- **One Piece – Shanks:** lời kể trung tính; câu Shanks dặn Luffy dùng giọng đàn anh ân cần (anh–em).
- **Pyu to Fuku! Jaguar:** Jaguar quái chiêu, đanh nhây; Piyohiko bình thường, hay bất lực; Hamer thích phô trương, tự xưng *tại hạ* khi làm màu. Không gán ID người nói chỉ dựa vào vị trí.
- **Rokudenashi Blues:** Taison nói mạnh, cộc, nghĩa khí; Nanase Chiaki nói dịu. Những câu trích nguyên văn có giọng gắt được giữ sắc thái, không áp dụng cho lời kể.
- **Rurouni Kenshin:** Kenshin thường lịch sự, khi trở lại Battosai nghiêm và sắc; Sanosuke dùng giọng bạt mạng; Saito tiết chế, lạnh; Shishio trịch thượng. Dùng anh–em với Kaoru ở câu hứa đón cô; ngoài ngữ cảnh này không mặc định xưng hô.
- **Slam Dunk:** Hanamichi tự tin hài hước; Rukawa ít lời, sắc lạnh; Akagi nghiêm; Mitsui cứng đầu nhưng giàu tình cảm; lời kể thể thao giữ tính mô tả.
- **Shaman King:** Yoh nói thoải mái, dùng mình hoặc tớ tùy người nghe; tên kỹ năng/thuật ngữ chính để nguyên.

Các tên Romanization có trạng thái `working_romanization_qa` cần so lại với ấn bản chính thức trước khi khóa thuật ngữ.

## Checkpoint 024 — Shaman King / Saint Seiya / Prince of Tennis

- **Yoh – Ren – Anna (Shaman King):** Yoh nói điềm nhiên, xuề xòa, dùng “tớ–cậu” khi nói với bạn ngang tuổi. Ren thường gay gắt, tự trọng cao, có thể dùng “ta–ngươi” trong câu đấu đối kháng. Anna mạnh mẽ, dứt khoát; khi nói với Silva hay Hao, không tự chuyển tất cả thành “mày–tao”. Giữ Furyoku, Oversoul, Shaman Fight và Shikigami.
- **Seiya, Shiryu, Hyoga, Shun, Ikki (Saint Seiya):** lời trích anh em cùng phe gần gũi nhưng không suồng sã; Shiryu và Ikki mạnh mẽ, trực diện; Shun dịu dàng, dùng “anh” với Ikki. Gold Saint/đối thủ dùng giọng đối chiến trang trọng hoặc gay gắt theo từng câu. Lời kể sự kiện ở ngôi thứ ba; giữ Cloth, Cosmo, Gold/Silver/Bronze Saint và tên đòn.
- **Ryoma – Tezuka – Fuji – Kikumaru/Oishi (Prince of Tennis):** Ryoma nói tự tin, hơi khiêu khích nhưng vẫn phân biệt cấp trên “anh–em”. Tezuka kiệm lời, nghiêm túc; Fuji điềm tĩnh với lời nói mềm; Kikumaru vui vẻ. Momoshiro nhiệt huyết; Kaido cộc và ít lời. Không biến lời kể trận đấu thành lời của người chơi.
- **Tar-chan / Lucky Man:** đoạn hài có thể dùng lối nói duyên, hơi lầy mà không thêm câu thoại hoặc thông tin ngoài Nhật gốc. Không gán người nói cho lời thuyết minh.
- **Cắt dòng & mã:** những câu mô tả nhân vật kéo qua nhiều ID phải giữ đúng ranh giới và số lượng `<IDEOSP>` trên chính ID đó. Bản dịch đoạn dài chưa qua QA font/pixel nên cần kiểm tra trên ROM khi tích hợp.
