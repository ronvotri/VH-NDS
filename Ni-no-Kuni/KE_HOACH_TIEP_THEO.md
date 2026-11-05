# Bước kỹ thuật sau đợt 99 — Ni no Kuni DS

**Trạng thái:** 17.823 mục đã dịch; 112 mục bị loại trừ hoặc cần rà; 1.860 tên Imagen và biệt danh giữ nguyên tên gốc (theo chính sách bảo toàn tên riêng).

1. Lấy bản sao ROM tiếng Anh gốc có SHA-256 `1ce3fdaf9d83a813328d642e4c7ef41ec8d6273f497b98a09355f9f6f821c627` để xác định hai thẻ câu màu bị hỏng, không nhập bản trích xuất sai vào ROM.
2. Đọc `DANH_SACH_112_MUC_CAN_RA.json` và đối chiếu `BAN_DO_VI_TRI.jsonl` trong gói nguồn; loại các chuỗi quét nhầm từ `.n3d`, `.tmap`, `.wmap`, `.NPD`.
3. Kiểm tra các script ghi rõ `(Dummy)`, `Temp`, `Sample`, các UI debug; chỉ chuyển bản dịch dự phòng thành chính thức nếu thực sự xuất hiện trong game.
4. Giữ nguyên `BURN`/`FREEZE` và các từ khóa câu đố khi kiểm tra cơ chế nhập liệu.
5. Nhúng JSONL theo ID một lần duy nhất, bảo toàn định dạng điều khiển, tái biên dịch bảng ký tự và font tiếng Việt có dấu. Kiểm tra kích thước ô thoại, gameplay, DLC, các nhiệm vụ phụ, save/load và các phép.
6. Ảnh có chữ, mô hình không chữ và các mục chưa trích xuất nằm ngoài phạm vi tiến độ 17.935: cần kiểm thử trực quan trước khi tuyên bố phát hành đầy đủ.
