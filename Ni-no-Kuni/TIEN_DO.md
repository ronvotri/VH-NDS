# Ni no Kuni DS — Tiến độ Việt hóa

**06/11/2026 — 99 đợt — 17.823 / 17.935 mục ưu tiên (99,38%).**

## Đợt 99: cứu 2 câu thoại gốc bị hỏng thẻ

- `hoi_thoai_079` — 2 câu hướng dẫn Nhiệm vụ Tải Về và trao đổi Imagen, được dựng lại **`{3:4}` / `{1:2}`** theo quy luật các câu sát bên.
- Giữ 17.821 câu cũ, không ghi đè.
- **Cần đọc trực tiếp tệp gốc trong ROM để xác nhận thẻ đã dựng lại**; trích xuất hiện tại bị thiếu dấu ngoặc.

## 112 mục còn treo đã được kiểm tra nguồn

| Nhóm | Số mục | Cách xử lý |
|---|---:|---|
| Byte trong dữ liệu bản đồ / 3D / hiệu ứng, không phải chữ hiển thị | 74 | Loại khỏi tệp nhập ROM |
| Lời thoại mẫu / nhãn tạm / placeholder trong script | 31 | Chưa ghép; bản dịch dự phòng nếu cần |
| Menu debug của nhà phát triển | 4 | Không tính là menu game |
| Từ khóa giải đố `BURN` / `FREEZE` | 2 | Cố ý giữ nguyên đáp án |
| Nhãn dữ liệu `Missing number` | 1 | Rà dữ liệu Imagen, không dịch đoán |
| **Tổng** | **112** | Chi tiết trong `DANH_SACH_112_MUC_CAN_RA.json` |

Ngoài ưu tiên: **1.860 tên riêng/tên gợi ý Imagen**, mặc định giữ cách viết nguyên gốc; dữ liệu thống kê trong `TEN_RIENG_1860_GIU_GOC.jsonl` chỉ phục vụ rà soát, **không nhập như bản dịch**.

**Chưa có bản patch/ROM đã Việt hóa.** Phải có bản sao ROM trùng SHA-256 nguồn, bộ ghép văn bản xử lý độ dài/control/Unicode và thử nghiệm trực tiếp trên NDS hoặc giả lập.
