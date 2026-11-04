# Pokémon Dash v0.8.4 Alpha — bổ sung 2 nhãn 3D Pause

Ngày: 04/11/2026. **ALPHA / CHƯA KIỂM THỬ BẰNG MELONDS HOẶC DS.**

Bắt đầu từ đúng ROM v0.8.2 Alpha (SHA-256: `acf443cba3c4333867e29d4df733fc896f561d7365b5f6f3420bbd25a95794e0`).

## Nhãn đã vá

| Model RelocMod | Nguyên bản | Bản dịch | Lý do |
| --- | --- | --- | --- |
| `en/mdl_pause_retry.rel` | Retry | **Đua lại** | Ngữ cảnh chơi đua; ngắn và dễ đọc trong 7 px hơn “Thử lại” |
| `en/mdl_pause_course.rel` | Back to Course | **Trở lại đường đua** | Hai trạng thái cao 17 px đủ cho chữ đầy đủ có dấu |

### Retry

- Mô hình dài 4096 byte, relocation từ `0xB48`, giữ nguyên đầu/cuối và bảng relocation.
- Bốn vị trí ảnh chữ ở row 0–6, x=73, 110, 200, 237; bản cuối **quấn qua mép x=255 sang x=0**, không thể vá như ảnh liên tục.
- Dùng font bitmap trực tiếp 7 px, bảng màu A3I5 kế thừa từ bản gốc; 805 byte mô hình thay đổi.

### Back to Course

- Mô hình dài 10752 byte, relocation từ `0x26B8`; hai bản chữ cao 17 px, mỗi bản dài 128 px, bắt đầu x=160 và quấn qua mép dữ liệu.
- Render `Trở lại đường đua` bằng font đậm 13 px trực tiếp ở độ phân giải 128×17, có dấu; không kéo ngang.
- 3484 byte mô hình thay đổi.

## Kiểm tra

- ROM v0.8.4 Alpha: SHA-256 `823e6818bf32ed91e015c23c9ccfcda1089afa040c9d90834527a8e467e6237e`.
- ROM đầu vào (v0.8.2) và đầu ra đều 16 MiB, mã APDE.
- Trong nested archive 318 tài nguyên, đúng **2 mô hình** thay đổi so với v0.8.2, **316 mô hình/tài nguyên khác** giữ nguyên.
- Các bản IPS v0.8.2→v0.8.3 và v0.8.3→v0.8.4 khớp byte; bản IPS tích lũy v0.8.2→v0.8.4 cũng đã được kiểm chứng cục bộ.
- **Chưa kiểm thử gameplay**: không khẳng định texture format/UV/hiển thị chắc chắn đúng hoặc game không crash.

## Mã và bản vá

- `patches/v082_to_v083_alpha_retry.ips` (Git blob SHA `f192644c493582306cf45468ab9aef7ad1fc139e`)
- `patches/v083_to_v084_alpha_course.ips` (Git blob SHA `d882cc32f3999886f9978c62600df8f90e7df799`)
- Công cụ áp patch có kiểm tra SHA: `tools/apply_v084_alpha.py`.
- Script dựng mẫu và ảnh preview nằm trong gói nguồn ZIP của bản Alpha tại phiên ChatGPT này. **Không lưu ROM gốc/ROM đã sửa lên GitHub.**

## QA cần thực hiện

1. Vào một chặng đua, Pause, kiểm tra cả nhãn **Đua lại** và **Trở lại đường đua** ở trạng thái thường/được chọn.
2. Chú ý chữ Đ, dấu nặng của “lại”, chữ ở mép phải và chữ quấn qua mép x=0.
3. Nhấn từng nút, kiểm tra hoạt động, crash và save.
4. Nếu có bất kỳ lỗi nào, quay lại bản v0.6 đã dùng trước đó.

**Trạng thái:** v0.8.4 Alpha chỉ là bản kiểm thử; không phải bản Việt hóa full. Tiếp theo còn nhiều mô hình chữ như GOAL, TIME'S UP, tên đường đua 3D.
