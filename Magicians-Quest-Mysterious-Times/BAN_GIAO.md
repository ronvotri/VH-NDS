# Magician’s Quest · Bàn giao Việt hóa cho Votri Valley

> **Checkpoint 040 · 07/11/2026:** **11.749/55.976 mục (20,99%)**, +240 trang (`0032.003` và `0032.004`, mỗi tệp 120). QA đã đối chiếu 501 JSONL/55.976 bản ghi, giữ nguyên 11.509 bản dịch trước. Nội dung: thầy Vlad, thầy Oakley, Ngôn ngữ Phép thuật, bà Malila, mèo đưa thư, chuyện cũ của hiệu trưởng Sol và mở nhiệm vụ tiên. Xem `CHECKPOINT-2026-11-07-DOT-40.md`, `QA-040.md`, `DELTA-040.jsonl`. **Đợt tiếp:** `0032.005` + `0033.001` (240 trang), cả hai nguồn đã stage lên GitHub.


> **Checkpoint 039 · 07/11/2026:** **11.509/55.976 mục (20,56%)**, +240 trang sự kiện (`0032.001`: 120; `0032.002`: 120). QA đối chiếu 501 JSONL và 55.976 bản ghi, giữ 11.269 bản dịch cũ. Đã dịch tiệc trà mùa xuân, thi thử gan mùa hè, hội thi lẩu nấm mùa thu và lễ hội tuyết cầu vồng. Xem `CHECKPOINT-2026-11-07-DOT-39.md`, `QA-039.md`, `DELTA-039.jsonl`. **Đợt tiếp:** `0032.003` + `0032.004` (240 trang); hai tệp nguồn được giữ trên GitHub.


> **Checkpoint 038 · 07/11/2026:** **11.269/55.976 mục (20,13%)**, +221 trang thoại (`0031.004`: 120; `0031.005`: 101). QA đối chiếu toàn bộ 501 JSONL/55.976 bản ghi, bảo toàn 11.048 mục dịch cũ. Xem `CHECKPOINT-2026-11-07-DOT-38.md`, `QA-038.md`, `DELTA-038.jsonl`. **Đợt tiếp:** `0032.001` + `0032.002` (240 trang).

> **Checkpoint 037 · 07/11/2026:** **11.048/55.976 mục (19,74%)**, +240 trang thoại (`0031.002`: 120; `0031.003`: 120). QA so sánh toàn bộ 501 JSONL/55.976 bản ghi, giữ nguyên 10.808 mục dịch cũ. Xem `CHECKPOINT-2026-11-07-DOT-37.md`, `QA-037.md`, `DELTA-037.jsonl`. **Đợt tiếp:** `0031.004` (120) và `0031.005` (101).

> **Checkpoint 036 · 07/11/2026:** **10.808/55.976 mục (19,31%)**; +240 trang thoại (`0030.005`: 120, `0031.001`: 120). QA đối chiếu 501 JSONL/55.976 bản ghi, 0 lỗi cấu trúc, giữ 10.568 bản dịch cũ. Xem `CHECKPOINT-2026-11-07-DOT-36.md`, `QA-036.md`, `DELTA-036.jsonl`. **Đợt tiếp:** `0031.002` và `0031.003`. Giữ nguyên mã điều khiển, ngôi xưng và thuật ngữ.
## Bắt đầu trong phiên cloud

Giải nén gói này. Đọc tệp này và `translation/INDEX.tsv` trước. Mở từng nhóm JSONL theo thứ tự dưới đây. Mỗi tệp tối đa 120 mục. Tệp tiếng Anh nguồn và vị trí chèn đã có sẵn, nên có thể bắt đầu dịch ngay cả khi phiên cloud chưa có ROM.

| Nhóm | Số mục | Nội dung |
| --- | ---: | --- |
| `00-mo-dau` | 106 | Lời chào, đặt tên, khai sinh, chọn trường và các nhánh tại Căn Phòng Khởi Đầu và Kết Thúc. Hai trang đầu đã dịch và đã được người dùng thử trong game. |
| `01-he-thong` | 1.087 | Lưu game, kết nối, bạn bè, thư, thông báo, tên phép, từ vựng phép thuật, danh hiệu và nhãn hệ thống dạng chữ. |
| `02-vat-pham` | 1.501 | Tên vật phẩm, nội thất, quần áo, sinh vật, thao tác túi đồ và menu tương tác. |
| `03-so-tay` | 432 | Tên chủ đề học, mô tả và thông báo bắt cá, côn trùng, sinh vật kỳ bí. |
| `04-thoai` | 52.608 | Lời thoại NPC, thư, sự kiện, bài học, tin đồn, câu ngắn theo tính cách và câu cửa miệng. |
| `05-credit` | 242 | Credit cuối game của bản Mỹ. Dịch chức danh và mục, giữ tên người, công ty, tên game và copyright. |

Tổng cộng **55.976 trường văn bản từ 71 tài nguyên**. Một mục thường là một trang, một lựa chọn hoặc một nhãn. Nhiều mục trùng nguyên văn, nhất là tên đồ và câu theo tính cách. Có **30.079 chuỗi nguồn khác nhau** trên toàn bộ gói. Tái dùng bản dịch khi ngữ cảnh và mã điều khiển giống nhau. Xử lý `00`, `01`, `02` và `03` trước rồi mới mở các tệp thoại được giao trong `04`.

Đếm riêng 43 kho `talkfigs/0eng/data` cho ra **25.426 bản ghi có ID**, **59.482 trường không trắng** và **51.038 trường được xuất**. Có 8.444 trường được giữ nguyên trong ROM, chủ yếu là lệnh, biến, số hoặc dấu câu. Trong số đó có 5 mục chỉ ghi `予備` (dự phòng). Kho `0053` có 2.426 bản ghi nhưng chỉ 32 trường có nội dung, gồm một số câu tiếng Nhật lặp lại. Xem số liệu từng kho trong `audit/dialogue-count.tsv`. Ước tính theo các từ dùng chữ cái Latin sau khi bỏ mã điều khiển, toàn bộ gói có khoảng **475.000 từ nguồn** nếu tính cả phần lặp.

## Quy tắc dịch

- Chỉ điền trường `vi`. Giữ nguyên `id`, `en`, thứ tự mục và tên tệp. `vi: null` giữ nguyên tiếng Anh. Với tên riêng giữ nguyên mà vẫn muốn đánh dấu đã duyệt, chép nguyên nội dung `en` sang `vi`.
- `ctx` là mã thoại đối với kho thoại hoặc tên NPC đối với câu cửa miệng. Ghép các trang liên tiếp theo cùng mã để hiểu ngữ cảnh. Cùng một mã trong kho khác có thể là đoạn khác.
- Giữ nguyên thứ tự và tham số các mã như `$500;`, `$545'0;`, `$019'12008;`, `$000'5;`, `[$end_word]`, `%s`. Giữ nguyên tab, CR/LF và chỗ trống cấu trúc. Dấu `▼` là xuống dòng hiển thị. Có thể dời hoặc đổi số dấu `▼` trong trường `page:`, thường tối đa ba dòng mỗi trang. Với các trường khác giữ nguyên dấu này. Mỗi trang đã được tách thành một mục riêng.
- Tệp dùng UTF-8 và bản dựng chuẩn hóa NFC. `max_utf8_bytes` là giới hạn byte thực tế của trường cố định, bao gồm mã điều khiển và trừ chỗ cho byte kết thúc. Đặc biệt `ItemOpe` và `SelMsg` chỉ có 31 byte hữu dụng.
- Mốc kiểm tra độ dài trang là khoảng 160 px với font đã chốt. Công cụ đếm độ rộng của chữ thấy được trước khi game thay tên người chơi hoặc biến, nên chừa chỗ cho các biến đó. Hộp thoại, menu và tên vật phẩm vẫn cần kiểm thử thực tế.
- Giữ văn phong xưng hô của từng NPC. Mẫu mở đầu dùng “ta/em”, “Căn Phòng Khởi Đầu và Kết Thúc”. Giữ tên riêng đến khi có bảng thuật ngữ chốt. Tách nghĩa của “magic” và “incantation” theo cơ chế chơi. Một số dòng tiếng Nhật là ký tự dự phòng hoặc nhãn sót trong nhánh Anh, cần xét ngữ cảnh trước khi đổi.

## Dựng và kiểm tra ROM

Gói ZIP chứa văn bản, mã nguồn và danh mục, dùng ROM sạch do bạn cung cấp. ROM đích là **USA, mã YNNE, 128 MiB**, SHA-256 `5c1d3e9cb8a5351f9c949bc758d9aed94479abc17eb41b6d93cbe8d4e15cca36`. Chạy với Python 3.10+ và Pillow. Ví dụ Linux trên cloud:

```bash
python -m pip install Pillow
export MQ_ROM="/path/to/clean_usa.nds"
python mqhandoff.py check
python mqhandoff.py build --output MagiciansQuest_VietHoa.nds
```

Đặt `MQ_ROM` thành đường dẫn thực trên máy bạn. PowerShell dùng `$env:MQ_ROM = "C:/.../Magician's Quest - Mysterious Times (USA) (En,Fr,Es).nds"`. Nếu chưa đặt biến, công cụ tìm bản USA trong Downloads.

`check` kiểm tra ID, nguồn, mã điều khiển, ký tự có trong font và giới hạn byte. `build` hỗ trợ bản dịch từng phần, giữ mã ID của game, chèn font 9 × 16 px đã duyệt, chèn dòng “Việt hóa bởi Votri Valley” dưới logo, cập nhật FAT và CRC header. Câu cửa miệng NPC được chèn đồng thời vào bảng rời và bản sao khối tiếng Anh. File đầu ra phải là tên mới. `dump --text thu-muc-moi` tạo lại bộ mẫu từ ROM sạch. `mqhandoff_test.py` kiểm tra trích/chèn lại và dựng ROM thử trong thư mục tạm.

Kiểm thử ở nhánh **tiếng Anh**. Dùng New Game cho đoạn mở đầu, tránh save state cũ mang theo dữ liệu font và asset từ bản trước. Tiếp theo vào túi đồ, shop, phép thuật, thư, hội thoại NPC và ít nhất một đoạn thoại ba dòng để kiểm tra độ rộng, vị trí dấu và phần đuôi chữ.

## Phần ngoài bảng dịch

- **Chữ trong ảnh.** `audit/graphics.tsv` ghi 141 tài nguyên đồ họa cần xem, gồm ứng viên có tên hậu tố Anh và đồ họa dùng chung. Ưu tiên `title/menu_e.bin` cho New Game/Continue, `picstat/key/` và `picstat/sfnd/` cho nút/tiêu đề, `2d/sell/`, `2d/mydesign/`, `bank/`, `hair/`, `music/`, `board/`, `book/`, `stamp/`, `trashbox/`, cùng ảnh cảnh `script/pic_e.dat`. Đây là danh sách ứng viên dựa trên các khối Nitro, cần mở sprite hoặc tilemap để xác nhận từng nhãn. Một số tệp chỉ chứa palette, ô hoặc hoạt ảnh đi kèm.
- **Quy trình ảnh.** `python mqhandoff.py extract --asset title/menu_e.bin --output menu_e.bin` xuất nguyên tài nguyên. Giải gói theo bảng `u32 count` và cặp `u32 offset, u32 length`, lớp LZ10 có thể ở ngoài hoặc ở từng mục. Giữ cặp NCGR, NCLR, NCER hoặc NSCR cùng nhóm. Khi đã đóng gói lại asset, đặt nó theo đường dẫn NitroFS trong một thư mục riêng, ví dụ `anh/title/menu_e.bin`, rồi dựng với `--asset-dir anh`. Với asset cùng đường dẫn đã có bản vá text/font/credit, công cụ báo trùng để tránh ghi đè.
- **Vật phẩm và sinh vật.** `item/ItemMsg.dat` có 1.635 mục. Sau giải nén, mục 0 là bảng ID, 1.634 mục còn lại chỉ chứa `▼\r\n`, nên không có mô tả để dịch ở đó. Tên lấy từ `ItemName_e.ofs`. Nội dung sổ tay và thông báo bắt sinh vật nằm trong kho thoại `0999` cùng với đồ họa trong `book/`.
- **Tên NPC.** Bảng `NpcDataOfs_e.bin` có 245 hồ sơ. Gói xuất câu cửa miệng và tên NPC làm ngữ cảnh. Giữ tên nhân vật vì chúng có thể xuất hiện ở nhiều nơi. Nếu đổi tên, rà thêm bảng từ vựng phép thuật và cả bản sao tiếng Anh trong `NpcData.bin`.
- **Logic và bộ lọc.** `script/event/`, `script/start/`, `talk/TStart.dat`, `talk/topic/cond_*` chứa điều kiện hoặc lệnh. `sys/taboo.bin` là danh sách từ lọc đầu vào, xử lý riêng nếu cần. `title/stfrll.txt` là credit mang tên bản Châu Âu. Bảng dịch ưu tiên `title/stfrll_a.txt` của bản Mỹ.
- **Mã và Wi-Fi.** `audit/code-clues.tsv` liệt kê chuỗi gợi ý từ ARM9 và 39 overlay đã bung nén BLZ. Kết quả chủ yếu thuộc SDK mạng, chứng chỉ và log. `dwc/utility.bin` là giao diện Nintendo Wi-Fi đóng gói riêng. Cần tách riêng nếu phạm vi bao gồm cả trình cấu hình Wi-Fi.
- **Phạm vi rà soát.** `audit/nitrofs.tsv` ghi toàn bộ 1.162 đường dẫn của ROM. `audit/text-clues.tsv` lưu các dấu vết chữ ngoài bảng dịch để kiểm tra thêm. Quét dữ liệu xác nhận các nguồn chữ chính nhưng chưa thay cho kiểm thử từng màn chơi hoặc kiểm tra trực quan từng ảnh. Nhóm đồ họa trong danh mục chưa được Việt hóa.

## Lệnh giao cho phiên cloud

> Đọc BAN_GIAO.md và translation/INDEX.tsv. Bắt đầu từ 00-mo-dau và 01-he-thong. Chỉ sửa trường vi trong các JSONL được giao, giữ mã điều khiển và ID, kiểm tra giới hạn byte. Dịch từng lô để dễ kiểm tra và tái dùng câu trùng đã duyệt khi ngữ cảnh phù hợp. Sau khi xong văn bản, dùng audit/graphics.tsv để rà phần chữ nằm trong ảnh. Dựng ROM từ bản USA sạch bằng mqhandoff.py và liệt kê các màn cần test.
