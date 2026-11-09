# Yu-Gi-Oh! World Championship 2008 — Checkpoint G01 (10/11/2026)

## Hoàn thành bản dịch nháp

Đã điền bản Việt **8.156/8.156 chuỗi** (100% về độ phủ), chia thành:

| Nhóm | Nội dung | Có bản Việt |
|---|---|---:|
| A | Mô tả lá bài | 2.009/2.009 |
| B | Cốt truyện | 1.618/1.618 |
| C | Thoại Duel | 1.962/1.962 |
| D | Hướng dẫn | 649/649 |
| E | Thuật ngữ Duel | 240/240 |
| F | Menu & thông báo | 1.257/1.257 |
| G | Hộp thoại Duel | 421/421 |

## G01

- `G_HOI_THOAI_DUEL_DLG_01.csv`: 250 câu.
- `G_HOI_THOAI_DUEL_DLG_02.csv`: 171 câu.
- 421 câu đã đối chiếu tiếng Anh gốc, **399 câu sửa** so với bản tiếng Việt tham khảo và **22 câu giữ lại** sau đối chiếu.
- Thống nhất thuật ngữ: Triệu hồi, Triệu hồi Đặc biệt, Hiến tế, Đặt úp, Sân, Mộ, Bộ bài, Giai đoạn, Bộ đếm Phép, Tộc/Thuộc tính, Phép/Bẫy.
- Ưu tiên câu hiển thị ngắn, chọn đúng mục tiêu thao tác, số quái thú, phí LP, số lá và thứ tự.

## Kiểm tra kỹ thuật

- **421/421 G01** đạt: không quá `toi_da_ky_tu`, không mất/đổi token `@0`–`@7`, `%d`, `%s`, `%%`, không sai số mã `\n`/`\r`.
- **8.156/8.156** bản Việt hợp lệ với `check_import.py` trên toàn bộ 64 CSV. Có **1 cảnh báo độ dài nguồn gốc** ở `story|1486|0` (ba mã `\n` làm chuỗi thô 10 > giới hạn 8, nhưng hiển thị 7 ký tự). Không sửa/cắt mã nguồn.
- Chỉ điền `tieng_Viet_MOI` trong hai CSV G; dữ liệu A–F được giữ nguyên tuyệt đối, ngoại trừ `ket_qua_dich.json` hợp nhất theo công cụ nhập.
- `QA/DOI_CHIEU_G01_421.csv`, `QA/G01_CHI_TIET_DA_SUA.csv` và `QA/G01_MANIFEST.json` phục vụ tra cứu và kiểm toán.
- ZIP chứa dữ liệu A–G, bản JSON hợp nhất và công cụ `check_import.py`.

**Lưu ý:** 100% độ phủ bản dịch nháp **không đồng nghĩa 100% chất lượng đã được duyệt**. Chưa tích hợp patch ROM, chưa kiểm tra font tiếng Việt, độ tràn UI trong Nintendo DS hoặc toàn bộ ngữ nghĩa; nhóm A mô tả lá bài cần đặc biệt soát kỹ.

## Bước kế tiếp

1. Tạo bản vá ROM với font Việt và kiểm tra hiển thị trên NDS/giả lập.
2. Hiệu đính sau kiểm thử theo bố cục thực tế, nhất là màn hình dài, đa lựa chọn, tên lá và thuật ngữ.
3. Chốt bản patch phát hành sau khi QA thực máy/giả lập.
