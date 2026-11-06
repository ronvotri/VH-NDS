# Magician's Quest: Mysterious Times — Việt hóa Nintendo DS

Dự án Việt hóa tiếng Việt trên repo chung [VH-NDS](https://github.com/ronvotri/VH-NDS), thư mục riêng `Magicians-Quest-Mysterious-Times/` để không lẫn Ni no Kuni và Pokémon Dash.

## Trạng thái mới nhất — Checkpoint 011 · 06/11/2026

- **5.137/55.976 mục (9,18%)** có trường `vi` được điền, **+207 trang thoại so với checkpoint 010**.
- Mở đầu **106/106**, hệ thống **1.086/1.087**, vật phẩm **1.501/1.501**, sổ tay **432/432**, hội thoại **2.012/52.608**, credit **0/242**.
- Phần đợt 011: **87 trang `0020.005`** + **120 trang `0021.001`**, bản dịch tay tiếng Việt dấu, phong cách học đường hài hước Gen Z, không nhồi meme.
- **QA:** 501 tệp JSONL đối chiếu; 0 thay đổi ngoài `vi`, 0 lỗi mã `$...;` và 0 vi phạm ngưỡng 34 ký tự/dòng. Chưa thử trong ROM/emulator.

## Nguồn và tài liệu

- [Checkpoint 011](CHECKPOINT-2026-11-06-DOT-11.md), [QA 011](QA-011.md), [bản đối chiếu 011](DELTA-011.jsonl)
- Các tệp JSONL mới trong `translation/04-thoai/` và bản dịch tay `manual_0020_005.txt`, `manual_0021_001.txt`
- [Quy ước giọng văn/ngôi xưng](QUY_UOC_DICH_VI.md): người dẫn chuyện ta–em, giáo viên thầy/cô–em (khi rõ vai), bạn bè tớ–cậu; không đoán giới tính.
- `apply_011.py` và `qa_011.py` để áp và xác thực thay đổi.

## Quy tắc

- Chỉ sửa trường `vi`, bảo toàn ID, EN, metadata, mã điều khiển, tên file và thứ tự.
- Tránh những câu tiếng lóng làm biến nghĩa hoặc vượt kích thước hộp thoại.
- Không đăng ROM bản quyền lên GitHub. ZIP checkpoint đầy đủ được bàn giao riêng để dựng/kiểm thử với ROM sạch do người dùng cung cấp.

**Đợt kế tiếp:** tiếp tục `0021.002` trở đi và kiểm tra thống nhất tên riêng `The Emporium`/`Bách Hóa Tổng Hợp` trước khi thay đổi hàng loạt.