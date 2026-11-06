# Magician’s Quest — Quy ước giọng văn Việt hóa (11/06/2026)

## Mục tiêu
Dịch đúng ngữ cảnh học đường phù thủy NDS, ấm áp, tinh nghịch, có duyên, gần gũi với người chơi Gen Z. Hài hước nằm ở cách nói và tính cách, không phải thay nội dung gốc bằng meme hay ngôn ngữ mạng.

## Khóa ngôi xưng

1. **Người dẫn chuyện/phù thủy lớn tuổi ở Căn Phòng Khởi Đầu và Kết Thúc**: **ta – em**; phong thái thông thái, hơi nghịch, đôi lúc “Hô hô…”. Không tự ý đổi thành “tôi – bạn”, “ông – cháu” trong cùng nhân vật.
2. **Giáo viên – học sinh**: **thầy/cô – em** khi xác định rõ vai; chưa chắc vai thì chưa gán chức danh, cần đọc các câu liền trước/sau cùng `ctx`.
3. **Bạn bè đồng trang lứa, nói trực tiếp**: **tớ – cậu** làm mặc định; có thể nói “mình” khi ngữ cảnh thích hợp nhưng không trộn trong cùng hội thoại. Chọc ghẹo nhẹ như “Chuẩn luôn!”, “Quẩy banh nóc với bạn bè!” là hợp nếu đúng tính cách và ngữ cảnh.
4. **Thông báo hệ thống/menu**: trung tính, súc tích; cần xưng hô thì dùng “bạn”. Không dùng “em” trong thông báo lưu game, lỗi hệ thống.
5. **Lựa chọn của người chơi nói với người dẫn chuyện**: dùng **em** khi cần đại từ, ví dụ “Để em tự chọn”, “Vâng ạ”. Lựa chọn nói với bạn bè phải theo tớ/cậu.
6. **Nhân vật chưa rõ quan hệ**: tránh gán xưng hô tùy tiện; đọc chung mã `ctx`, kiểm tra tên NPC và lịch sử thoại, sau đó mới chọn.

## Cập nhật theo duyệt ngày 06/11/2026
- Người dùng duyệt câu: **“Em mê tụ tập, quẩy banh nóc với bạn bè!”** (trong JSONL: `Em mê tụ tập,▼quẩy banh nóc với bạn bè!`).
- Các nhận xét tính cách tại màn mở đầu nên **ngắn, lém lỉnh, chất Gen Z** như “chuẩn con nhà người ta”, “đầu tàu cả hội”, “gì cũng muốn hóng”, thay vì giọng cứng và sáo.
- Có thể bỏ tiếng đệm cổ điển “Hô hô...” khi câu cần mạnh và gọn hơn, nhưng giữ bản chất nhân vật lớn tuổi và quan hệ **ta–em** qua cả đoạn hội thoại.
- Không dịch chữ trong tên vật phẩm kiểu meme; với lời thoại cảm động, thông báo hệ thống và mô tả kỹ thuật phải ưu tiên rõ nghĩa.

## Mức độ hài hước
- Ưu tiên tự nhiên, dí dỏm, ngắn gọn: “Tên hay đấy chứ!”, “Chuẩn luôn!”, “Hô hô…”.
- Không nhồi từ lóng quá thời vụ, tục ngữ hiện đại quá xa bối cảnh, hoặc giễu nhại ở đoạn cảm động.
- Hội thoại nghiêm túc, lời dạy và hướng dẫn cơ chế phép thuật phải giữ đúng nghĩa.
- Không thêm giới tính/ngôi xưng khi nguyên văn không đủ ngữ cảnh.

## Từ vựng cơ chế
- `magic` = **phép thuật**; `incantation` = **thần chú**; `transform` = **biến hình**; `say the words` = **đọc thần chú / đọc chú** tùy chỗ hiển thị; `staff` = **trượng phép**; `familiar` = **linh thú**.
- Tên người, tên NPC, tên công ty và bản quyền giữ nguyên cho đến khi duyệt thuật ngữ.
- Tên chòm sao, địa điểm và vật phẩm quan trọng dùng đúng theo `translation/GLOSSARY.tsv`. Đổi một tên phải dò các nhóm liên quan trước khi sửa đồng loạt.

## Kỹ thuật bắt buộc
- Chỉ chỉnh trường `vi`; giữ `id`, `en`, `ctx`, `max_utf8_bytes`, tên file và thứ tự mục.
- Không thay hoặc đảo `$019'...;`, `$545'...;`, `$000'...;`, các mã bắt đầu `$`, `%s`, `[$end_word]`, tab, CR/LF và khoảng trắng cấu trúc.
- `▼` là ngắt dòng màn hình. Mỗi trang thường tối đa ba dòng (đối với bản gốc có ba dấu ngắt, được phép bốn dòng). Tránh dài quá 160 px, trừ trường hợp đã kiểm thử in-game.
- Tên vật phẩm/lệnh menu phải tuân thủ `max_utf8_bytes`; byte UTF-8 có dấu không bằng số ký tự.
- Câu trang dài phải ngắn đúng nghĩa; không bớt điều kiện thực hiện phép.

## Chưa chốt / cần lưu ý
- Danh xưng ông/cô của `Mr. Vlad`, `Mr. Oakley`, `Miss Strawe`, `Mr. Graves` hiện dựa trên danh xưng gốc; cần xác nhận chức vụ khi dịch NPC.
- Một số tên vật phẩm như Marguerite, Lapis Lazuli, Phantasm là tên riêng/đặc thù thế giới game; không tự thay nghĩa khi chưa đối chiếu UI và danh mục vật phẩm.