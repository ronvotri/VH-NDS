# Ragnarok DS — Checkpoint 038 (20/11/2026)

## Tiến độ trên nhánh GitHub
- Nguồn: **14.616 ID** trong 33 tệp JSONL.
- Checkpoint 037: **13.596 ID**.
- Checkpoint 038: **475 ID Job/Skill** mới, patch `translation/PATCH-DOT038.jsonl`.
- Tích lũy sau patch: **14.071/14.616 = 96,27%**, còn **545 ID Quest**.
- Không áp dụng patch 030 vì 815 mục hệ thống/credit bị xử lý lại, trùng dữ liệu đã có từ các đợt 001–002.

## Hạng mục Job/Skill
- File nguồn `translation/03-nghe-ky-nang-001.jsonl`: **529 ID**.
- `PATCH-DOT001-jobs-skills.jsonl`: 54 ID từ các lần trước.
- `PATCH-DOT038.jsonl`: 475 ID mới, không trùng với 54 ID cũ.
- 282 mục được Việt hóa gồm mô tả hiệu ứng Skill, điều kiện học Skill và gợi ý thao tác.
- 193 mục chủ động giữ nguyên: tên Job/Skill và 14 nhãn tiếng Nhật nội bộ chưa đủ điều kiện thay.
- Tất cả tên Job/Skill và màu nhấn `<CFFEF>`/`<CFFF4>` được bảo toàn.

## QA
- Kiểm tra cấu trúc bằng `tools/check_handoff.py` của bộ nguồn: **14.616 ID**, `errors=[]`.
- ZIP cục bộ chứa 2.685 mục đã điền từ patch 027–029 và 034–038, KHÔNG chứa 11.386 bản dịch patch cũ 001–026; vì vậy số `translated=2685` trong QA của ZIP chỉ phản ánh các patch có trong ZIP.
- Kiểm tra riêng patch 038: 475 ID duy nhất, bảo toàn thứ tự thẻ `<Cxxxx>`, toàn bộ trường `en` và metadata nguồn không thay đổi.
- GitHub blob SHA của patch 038: `371a5017c1800bde8845e893a6304e9d46e0d0f6`, đã tải lại và so khớp SHA ZIP.
- Chưa nhúng font Việt, chưa vá ROM, chưa kiểm tra độ rộng glyph/pixel hay hiệu ứng trong game trên máy NDS.

## Bước kế tiếp
- Dịch `04-nhiem-vu-001.jsonl` gồm 545 mục Quest chưa xử lý.
- Sau đó hợp nhất patch 001–029, 034–038 và patch Quest hoàn chỉnh, chạy QA toàn dự án với `--require-complete` và kiểm tra hiển thị trên giả lập hoặc Nintendo DS.
