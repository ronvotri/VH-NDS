# Ragnarok DS — Checkpoint 034 | 19/11/2026

## Đã xác minh trên GitHub
- Patch 001–026: **11.386 ID**, không trùng nhau.
- Patch 034: **80 ID** mô tả Item, nằm tại `translation/PATCH-DOT034.jsonl`, blob SHA **efb224594694d220ac7183a6cf46bd1e31a22dc4**, đã so khớp byte-level với ZIP bàn giao.
- Tổng đã có trên nhánh sau patch 034: **11.466/14.616 ID (78,45%)**.

## Bản dịch chưa được đồng bộ
- Patch 027: 422 ID thuộc `05-hoi-thoai-025.jsonl`.
- Patch 028: 439 ID thuộc `05-hoi-thoai-026.jsonl`.
- Patch 029: 275 ID thuộc `05-hoi-thoai-027.jsonl`.
- Tổng chưa đồng bộ: **1.136 ID**, có trong ZIP checkpoint 034 của phiên ChatGPT.
- Patch 030: **815 ID trùng** nhóm hệ thống 779 + credit 36 đã xử lý ở đợt 001–002; KHÔNG ghi đè bản GitHub.

## Tiến độ đúng khi hợp nhất tất cả patch duy nhất
- **12.602/14.616 (86,22%)**, còn **2.014 ID**.
- Phân nhóm còn thiếu: **Item 994**, **Job/Skill 475**, **Quest 545**.
- Số 12.602 chưa phải số được ghi đủ lên GitHub. Số thực tế đã có trên GitHub hiện là **11.466**.

## QA
- Bộ kiểm tra chính thức từ nguồn chạy trên 33 JSONL có patch 027/028/029/034: 14.616 ID, 1.216 bản dịch mới trong ZIP, **0 lỗi**.
- Chưa ghép toàn bộ GitHub 001–026 vào ZIP tại thời điểm báo cáo.
- Chưa nhúng font tiếng Việt, chưa sửa chữ vẽ trong ảnh, chưa patch/test ROM trên máy NDS.
