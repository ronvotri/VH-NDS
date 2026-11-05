# Ni no Kuni DS — Tiến độ Việt hóa

**05/11/2026 — 79 đợt — 14.831 / 17.935 mục ưu tiên (82,69%). Còn 3.104 mục.**

Giữ nguyên **14.601 bản dịch cũ**, bổ sung **230 câu mới** từ nguồn.

| Đợt | Tệp nguồn | Dòng nguồn | Đã dịch | Hoãn |
|---|---|---:|---:|---:|
| 78 | `hoi_thoai_079.jsonl` | 180 | 178 | 2 |
| 79 | `hoi_thoai_080.jsonl` | 75 | 52 | 23 |
| **Tổng mới** | | **255** | **230** | **25** |

**Lý do hoãn:** Hai dòng `hoi_thoai_079` số 63 và 93 có mã tô màu lỗi ngay trong nguồn. Các dòng 53–75 của `hoi_thoai_080` là chuỗi bất thường, không đủ căn cứ xác nhận là lời thoại. Xem `DEFERRED_SOURCE_079_080.json` để đối chiếu ID.

**QA:** 14.831 ID duy nhất, JSONL mới đọc hợp lệ, mã điều khiển có cấu trúc hợp lệ được giữ nguyên; ngắt dòng sơ bộ không quá 3 dòng × 48 ký tự mỗi câu.

`hoi_thoai_080` là tệp hội thoại cuối của gói nguồn đang có; không suy diễn có `hoi_thoai_081`. Những mục ưu tiên còn lại thuộc các nhóm nguồn khác hoặc chuỗi hoãn. Cần kiểm tra các danh mục nhiệm vụ, vật phẩm, hướng dẫn và lựa chọn.

**Chưa kiểm thử:** dựng font Việt, độ rộng pixel, giới hạn byte, nhúng ROM và chạy trên NDS.

**Không nhập đồng thời bản dịch gộp trong ZIP cùng các tệp rời** để tránh trùng ID.
