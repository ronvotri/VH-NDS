# Pokémon Dash — từ điển và quy chuẩn giao diện

Nguồn duyệt: bản Việt hóa v0.1–v0.6 và các yêu cầu sửa trực tiếp của người dùng. Từ điển dùng chung mọi vị trí, bao gồm các màn 2D/3D sau khi giải mã.

## Thuật ngữ menu

| English | Tiếng Việt |
|---|---|
| Practice | Luyện tập |
| Checkpoint | Chốt kiểm tra |
| Next | Tiếp |
| Ranking | Xếp hạng |
| Total Ranking | Tổng hạng |
| Best Record | Kỷ lục |
| New Record | Kỷ lục mới (chỉ viết tắt khi giới hạn pixel bắt buộc) |
| Time Attack | Đua tính giờ |
| Total Time | Tổng thời gian |
| Special | Đặc biệt |
| Yes / No / OK | Có / Không / Đồng ý |
| Create / Delete | Tạo / Xóa |
| Retry / Replay | Thử lại / Phát lại |
| Goal | Về đích |
| Time Up | Hết giờ |
| Pause | Tạm dừng |

## Tên cúp

`Green Cup` → **Cúp Xanh lá**; `White Cup` → **Cúp Trắng**; `Blue Cup` → **Cúp Xanh dương**; `Yellow Cup` → **Cúp Vàng**; `Red Cup` → **Cúp Đỏ**.

Ở nút cúp: **CÚP phía trên**, **tên màu phía dưới**. Đây là yêu cầu bắt buộc đã sửa trong v0.4.

## Tên đường đua đã áp dụng v0.3

| Green | White | Blue | Yellow | Red |
|---|---|---|---|---|
| Đồng cỏ xanh | Miền tuyết trắng | **Đường Zigzag** | Dấu ấn Smeargle | Đồng cỏ lắt léo |
| Băng qua đồng | Đầm lầy thử thách | Suối uốn lượn | Đảo dung nham | Vùng đất nóng |
| Đường ven biển | Hồ bí ẩn | Cao nguyên bùn | Đảo băng | Đầm xoáy |
| Dấu chân Mankey | Đồng bằng nứt nẻ | Hồ Sao | Đảo cát | Vòng xoáy băng |
| Đảo Pikachu | Đảo Luvdisc | Núi Jirachi | Đảo Pallet | Đảo Công viên Pokémon |

**Không** thay `Đường Zigzag` thành `Đường ngoằn ngoèo`.

## Giới hạn kỹ thuật

- Luôn dùng tiếng Việt có dấu nếu font hoặc đồ họa cho phép.
- Dịch nhãn trò chơi; **không dịch tên Pokémon hoặc tên người ghi công**.
- Giữ pixel-art, kích thước bản gốc, bảng màu NDS; không làm tràn hoặc che nút.
- Với các hộp nhỏ, giữ ý ngắn gọn, đừng tự động thay mọi chữ tiếng Anh tìm thấy trong metadata kỹ thuật.
- Các nhãn mô hình 3D chưa được sửa, dù từ điển đã chốt. Cần giải mã và test thật trước.

## Ngoại lệ nhãn 3D hẹp (v0.8.4 Alpha)

- `Retry` → **Đua lại** tại model 3D Pause cao 7 px, thay cho “Thử lại” vì ít dấu khó hiển thị và phù hợp ngữ cảnh đua. Với chỗ có đủ diện tích, vẫn có thể dùng “Thử lại”.
- `Back to Course` → **Trở lại đường đua** (đủ dấu; 17 px).
- Vẫn giữ `Zigzag Road` → **Đường Zigzag**.
- Những bản dịch 3D này là **bản vá Alpha chưa qua gameplay test**, chưa xác nhận hoàn tất.
