# QA — Checkpoint A35

Nguồn: **26 CSV A34** và danh sách **120 mục ưu tiên A35**.

| Hạng mục | Kết quả |
|---|---:|
| Mô tả nhóm A có bản Việt | 2.009 |
| Mô tả đối chiếu A35 | 120 |
| Dòng sửa theo tiếng Anh | 47 |
| Dòng đối chiếu giữ nguyên | 73 |
| Lỗi `check_import.py` | 0 |
| Dòng vượt `toi_da_ky_tu` | 0 |
| Mã `@/%, \\n/\\r` bị mất | 0 |

Bản A35 có thể tái tạo **toàn bộ 26 CSV** trực tiếp từ các file trong repo bằng `checkpoints/apply_a35.py`. Các dòng không phải A35 vẫn giữ nội dung tương ứng A34.

**Chưa duyệt ngữ nghĩa cuối toàn bộ 2.009 dòng.** Nhóm B–G giữ nguyên ở ZIP bàn giao, chưa được đẩy sang repo trong commit này. Chưa kiểm thử ROM.
