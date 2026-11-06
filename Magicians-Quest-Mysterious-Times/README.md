# Magician's Quest: Mysterious Times — Việt hóa Nintendo DS

Dự án Việt hóa tiếng Việt của **Magician's Quest: Mysterious Times** (NDS / bản Mỹ), thuộc kho chung [VH-NDS](https://github.com/ronvotri/VH-NDS). Thư mục dự án riêng để tránh lẫn với Ni no Kuni và Pokémon Dash.

**Ngày bắt đầu:** 2026-11-06 · **Checkpoint nguồn:** `MagiciansQuest_BanGiao_Cloud.zip` · **Checkpoint 001:** 655/55.976 mục có `vi` (trong đó 120 giữ nguyên nguồn sau khi rà).

## Nguyên tắc
- Vui nhộn, trong sáng, gần gũi Gen Z mà không lạm dụng meme.
- Người dẫn chuyện lớn tuổi: **ta–em**; giáo viên: **thầy/cô–em**; bạn bè: **tớ–cậu**; hệ thống: trung tính.
- Chỉ sửa trường `vi`; giữ nguyên ID, thứ tự, các mã điều khiển, giới hạn byte và bố cục trang.
- Không cung cấp ROM thương mại, chỉ lưu tài liệu, bản dịch, công cụ và checkpoint hợp lệ.
- Mọi lần dịch tiếp phải bổ sung tiến độ/checkpoint vào đúng thư mục này.

## Sơ đồ dự án
- `CHECKPOINT.md`: tiến độ và trạng thái được xác minh.
- `QUY_UOC_DICH_VI.md`: giọng văn/ngôi xưng/thuật ngữ.
- `translation/`: những tệp JSONL đã cập nhật kể từ checkpoint nguồn.
- ZIP checkpoint đầy đủ là phương thức bàn giao để vá ROM khi có bản ROM sạch hợp lệ.

## Môi trường dựng
Mục tiêu bản Mỹ: Game ID YNNE; SHA-256 ROM gốc `5c1d3e9cb8a5351f9c949bc758d9aed94479abc17eb41b6d93cbe8d4e15cca36`. Người dùng tự cung cấp ROM phù hợp để kiểm thử.