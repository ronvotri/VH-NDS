# Kết quả rà soát cuối kho văn bản — Ni no Kuni DS

- Nguồn English ROM: `Ni No Kuni - The Jet Black Mage (Japan) [T-En by Anjiera v1.0] [n].nds`.
- Ngày: 2026-11-06.
- Mốc cũ: **17.821/17.935**.
- Khôi phục hai đoạn có thể hiểu nghĩa, sửa thẻ tô màu theo cú pháp câu lân cận: **+2**.
- Mốc mới: **17.823/17.935 = 99.38%**, còn **112** mã nguồn chưa gộp thành bản dịch.
- 112 ID đều có đường dẫn nguồn gốc rõ ràng trong `DANH_SACH_112_MUC_CAN_RA.json`.

## Phân loại chính xác

| Phân loại | Số lượng | Quyết định |
|---|---:|---|
| Trích nhầm byte tài nguyên nhị phân | 74 | Không dịch vì phá dữ liệu |
| Chuỗi mẫu/tạm trong script | 31 | Chưa đưa vào bản chính; có bản nháp riêng cho 9+ dòng đọc được |
| Nhãn debug nội bộ | 4 | Không tính là nội dung gameplay |
| Đáp án puzzle `BURN`/`FREEZE` | 2 | Giữ nguyên |
| `Missing number` | 1 | Không thể đoán nghĩa ngữ cảnh |

## Không nên gọi đây là patch hoàn thiện

Độ phủ dịch là phần văn bản tìm thấy trong gói trích xuất, **không phải tỷ lệ Việt hóa thực trong ROM**. Không có ROM nguồn để chạy pipeline nhúng, không có bản test font/hiển thị trên máy. Nhiều chuỗi trong bản đồ, hình ảnh và menu chỉ kiểm chứng được bằng chơi thử thực tế. Các thẻ màu hai câu mới là **dựng lại hợp lý**, phải được đối chiếu chuỗi lệnh gốc trước khi phát hành.

## Chính sách tên riêng

1.860 mục `TEN_` là tên riêng/biệt danh và tên loài Imagen, có các tên như `Mite`, `Mitt`, `Dinoceros` và `Blubber Bubbler`. Để giữ tính nhất quán với lời thoại, **không tự dịch tên riêng bằng máy**. Bảng `TEN_RIENG_1860_GIU_GOC.jsonl` ghi đầy đủ ID và cách xử lý, không được nhập như câu Việt hóa.

## Bàn giao cho Codex

- Dùng `BAN_DICH_GOP_DOT_01_99.jsonl` **hoặc** các tệp `translations/dot_*`, không cả hai.
- Dùng vị trí offset gốc trong `Goi_dich_NiNoKuni/BAN_DO_VI_TRI.jsonl`; **không chép Unicode đè theo byte offset cố định**.
- Đọc `KE_HOACH_TIEP_THEO.md`, `QA_DOT_99.json`, `DANH_SACH_112_MUC_CAN_RA.json`.
