# Đối chiếu file dịch tay Ni no Kuni 2024

Nguồn do người dùng cung cấp: `Ninokuni-ALL_FINAL_2024.xlsx`. **Chỉ dùng để tham khảo, chưa chép đè vào dữ liệu đang chạy.**

## Kiểm tra ngày 04/11/2026

- Sheet chính `ALL FULL` có **32.819** dòng có cả tiếng Anh và tiếng Việt.
- Toàn bộ các sheet song ngữ: **34.146** dòng, khử trùng lặp còn **25.253 cặp Anh–Việt** trong kho tra cứu.
- ROM nguồn bản DS: `Ni No Kuni - The Jet Black Mage [T-En by Anjiera v1.0].nds`; xuất **19.795** mục, trong đó **17.935** mục ưu tiên.
- So sánh nội dung câu gốc (chuẩn hóa chữ hoa, dấu nháy, dấu xuống dòng) tìm được **325 ID giống nhau**; **70** ID đã dịch, **255** ID chưa dịch.
- Trong 255 ID chưa dịch: **81 hội thoại**, **38 vật phẩm/kỹ năng**, **136 tên riêng tùy chọn**.
- **72** ID trùng câu gốc nhưng bản Excel có nhiều cách dịch tiếng Việt (khác người nói/xưng hô).
- Đối chiếu gần giống tìm thêm **18 ID** ngoài nhóm trùng, tất cả cần người kiểm tra.

## Khác biệt quan trọng

Excel có `Drippy`, `Ding Dong Dell`, `Mornstar`; bản DS đang dịch dùng `Shizuku`, `Catnap`, `Gladion`. Đây không phải hai bản xuất kịch bản đồng nhất. Hầu hết 325 câu giống nhau là câu giao tiếp ngắn như `Huh?`, `Okay`, `What?`. **Không thể chuyển tất cả lời thoại bằng cách nối theo thứ tự hàng Excel, và cũng không nên tự động thay ngôi xưng của 5.270 mục đang có.**

## Cách tận dụng

1. Giữ file gốc 2024 như một **translation memory** độc lập, không nhập trực tiếp vào ROM hay thay JSONL trong `translations/`.
2. Đối chiếu *câu tiếng Anh* và người nói của từng bản DS. Dùng bản dịch tay để gợi ý khi thực sự cùng nghĩa, rồi sửa tên và xưng hô theo `THUAT_NGU.md`.
3. Các trường hợp không đồng nhất / nhãn nội bộ / token đặc biệt phải tạm hoãn.
4. Chỉ đánh dấu hoàn thành và cập nhật `TIEN_DO.json` với **ID đã được duyệt và đưa vào bản dịch chính**, không tính kho tham khảo.
5. Bản đầy đủ của bảng đối chiếu, 255 mục gợi ý và translation memory được lưu trong gói ZIP bàn giao; **không đưa bản gốc Excel hoặc toàn bộ văn bản trò chơi khác lên repo công khai**.

**Mốc tiến độ bản DS không đổi: 5.270 / 17.935 mục (25 đợt).** Chưa nhập ROM/chạy thử trên máy DS.
