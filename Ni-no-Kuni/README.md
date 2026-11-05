# Ni no Kuni DS — Việt hóa Votri Valley

**Checkpoint 06/11/2026: 99 đợt, 17.823/17.935 mục ưu tiên (99,38%).**

Đợt 99 khôi phục **2 câu thoại thực** trong `hoi_thoai_079` vốn bị hỏng ký hiệu `{3:4}` / `{1:2}` ở nguồn trích xuất; cần đối chiếu chuỗi byte trực tiếp với ROM trước khi đưa vào patch.

**112 mục ưu tiên không dịch đoán:** 74 chuỗi bytes không phải lời thoại, 31 placeholder/thoại mẫu, 4 nhãn debug, 2 đáp án câu đố cần giữ nguyên, 1 nhãn dữ liệu lỗi. Xem `DANH_SACH_112_MUC_CAN_RA.json` và `BAO_CAO_CHOT_DU_LIEU.md`.

- `translations/dot_*/`: các JSONL đã dịch, theo ID không trùng; chỉ gộp 99 đợt khi xuất checkpoint.
- `TIEN_DO.json` / `TIEN_DO.md`: tiến độ và ghi chú chưa hoàn tất.
- `THUAT_NGU.md`: từ điển tên riêng và phép thuật.
- `QA_DOT_99.json`: QA kiểm tra dữ liệu mới.
- `DICH_DU_PHONG_TAM.jsonl`: **chỉ để tham khảo**, tuyệt đối không nhập chung với bản dịch chính.
- `TEN_RIENG_1860_GIU_GOC.jsonl`: tên người, biệt danh và tên Imagen, thống nhất giữ nguyên danh xưng tiếng Anh, không tăng số mục được dịch.

Bản gộp `BAN_DICH_GOP_DOT_01_99.jsonl` nằm trong ZIP: **không nhập cùng JSONL từng đợt** để tránh hai bản cùng ID.

**Không phải bản ROM đã ghép/kiểm thử; giữ riêng thư mục `Ni-no-Kuni/` trong `VH-NDS`.**
