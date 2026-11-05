# Cần rà — Đợt 84–85

1. **Nguồn lỗi ở `vat_pham_ky_nang_003` dòng 34:** `VAT_59fc215d13cd8a`, nguồn kết thúc `...when they.` dù mệnh đề chưa hoàn chỉnh. Bản dịch đặt dấu ba chấm, không đoán phần thiếu. Cần truy hồi từ ROM nguồn/trích xuất khác.
2. **Tên khí tài:** `Lockpick Gun` → *Súng Mở Khóa*, `Unlock Gun` → *Súng Phá Khóa*, `Bad Emperor` → *Hoàng Đế Xấu Xa* (tạm); xem item list thực tế để tránh nhầm chức năng.
3. **Hiệu ứng:** `Positional Effects`, `Fatal Blow`, `Increase Critical` dịch ngắn; chưa chắc tên kỹ năng/buff thống nhất với giao diện thực tế.
4. **Tên riêng/địa danh:** Old Smoky, Bờ biển Trail, Đầm Lầy Chướng Khí, Hang Băng cần soát danh mục map của bản DS.
5. **Mô tả Imagen:** Các tên loài từ nguồn như Ogrrr, Paraphim, Flash Fry, Hurly được giữ nguyên; chú ý không dịch chéo tên từ bản PS3.
6. **QA được thực hiện:** 333 ID duy nhất, khớp thứ tự nguồn và 15.373 ID cũ; mã bảo vệ không mất; các câu mới tối đa 3 dòng × 48 Unicode ký tự. Đây là kiểm tra dữ liệu, không phải đo pixel hay chứng nhận chất lượng thuật ngữ.
7. **Chưa thực hiện:** nhúng/đóng ROM, kiểm font tiếng Việt, offset/byte-length, gameplay test trên giả lập hoặc NDS thật.
