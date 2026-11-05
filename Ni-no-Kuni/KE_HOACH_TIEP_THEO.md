# Những nhóm chưa dịch sau đợt 79 — Ni no Kuni DS

Mốc 05/11/2026: đã dịch **14.831/17.935 mục ưu tiên**; còn **3.104 mục ưu tiên**. Đối chiếu toàn bộ ID trong gói nguồn với 79 tệp JSONL checkpoint.

| Nhóm nguồn | Mục chưa dịch | Gợi ý xử lý |
|---|---:|---|
| `vat_pham_ky_nang_*` | **2.540** | Dịch tên/mô tả vật phẩm và kỹ năng; rà chiều rộng UI |
| `lua_chon_thong_bao_*` | **270** | Dịch nút chọn và thông báo; ưu tiên màn hình hiển thị |
| `nhiem_vu_phu_*` | **236** | Dịch tên nhiệm vụ, yêu cầu và phần thưởng |
| `hoi_thoai_*` | **58** | Các dòng đã hoãn do là dữ liệu thử nghiệm/mã hỏng; không đoán |
| **Tổng ưu tiên** | **3.104** | |

Ngoài tập ưu tiên còn **1.860 mục `ten_rieng_tuy_chon_*`** (tên loài/nhân vật). Không tính chúng trong mẫu số 17.935, nhưng vẫn phải rà khi tuyên bố hoàn tất Việt hóa toàn game; một số tên nên giữ nguyên.

Gói nguồn chỉ có `hoi_thoai_001–080`; tệp cuối 75 dòng. **Không có `hoi_thoai_081` trong gói.** Đợt tiếp theo nên chuyển sang `lua_chon_thong_bao_001` và/hoặc `vat_pham_ky_nang_001`, rồi hoàn thiện nhiệm vụ phụ.

Đây là kiểm tra độ phủ theo ID, **không phải xác nhận ghép ROM hay chạy được trên NDS**.
