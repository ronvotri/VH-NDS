# Jump Ultimate Stars — CP051: đính chính CP050A

**10 mục sửa (không tăng số ID dịch); số liệu giữ 32.746/34.919 = 93,78%.**

## Sửa theo JA và quiz_context

- `06-jquiz-009.jsonl`, row_index 842–846: câu hỏi mẹ Hiei đã bị dịch trôi sang đáp án; phục hồi câu hỏi ở 842, các phương án Hina / Rui / Ruka / Shizuru theo đúng ID và thứ tự gốc ở 843–846.
- row_index 847–849: ngắt đúng hai câu hỏi độc lập về Kurama và Raizen, không chuyển một câu sang ID câu khác.
- row_index 1230: `Goddess of Reversal` thành tên thẻ bài chính thức `Gyakutenno Megami`.
- row_index 1350: `Ritual of the Masked Beast` thành tên thẻ bài chính thức `Curse of the Masked Beast`.

## Dữ liệu

- [BAN_DINH_CHINH_050A.jsonl](BAN_DINH_CHINH_050A.jsonl): 10 bản ghi đầy đủ để chồng lên CP050 theo ID, **chỉ ghi đè `vi`**. Không cộng thêm ID.
- [AP_DINH_CHINH_050A.py](AP_DINH_CHINH_050A.py): script tạo bản gộp cập nhật và kiểm tra JA/metadata/tags/giới hạn 37 ký tự. Dùng bản gộp cũ `BAN_DICH_TONG_HOP_038-050.jsonl` và 10 sửa.
- [QA_050A.json](QA_050A.json): báo cáo QA tĩnh.

Chạy ở thư mục chứa dữ liệu:
```bash
python AP_DINH_CHINH_050A.py BAN_DICH_TONG_HOP_038-050.jsonl --overlay BAN_DINH_CHINH_050A.jsonl --output BAN_DICH_TONG_HOP_038-050A.jsonl
```

**Không thay đổi:** 9.150 ID trong CP038–050; 32.746 ID dịch trên 34.919 ID toàn bộ nguồn. Chưa kiểm tra font NDS, vá ROM, thực nghiệm quiz.

## Bước chờ nguồn

Vẫn còn 1.744 ID cần tìm và 429 dòng Deck/Credits chưa dịch. Tệp ZIP Nhật ở Library phiên cũ không có quyền đọc bytes; khi có ZIP nguồn thật mới tiến hành dịch mới.

## Nguồn kiểm chứng tên gọi

- [Gyakutenno Megami — cơ sở dữ liệu thẻ bài chính thức](https://www.db.yugioh-card.com/yugiohdb/card_search.action?cid=4096&ope=2)
- [Curse of the Masked Beast — Yu-Gi-Oh!](https://www.yugioh.com/cards/curse-of-the-masked-beast)
- [Hina — mẹ của Hiei](https://yuyuhakusho.fandom.com/wiki/Hina)
