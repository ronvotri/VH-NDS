# Jump Ultimate Stars — Kiểm toán phần còn lại sau Checkpoint 050

Đã dịch **32.746/34.919 ID (93,78%)**. **2.173 ID** chưa có trong tổng số checkpoint đang theo dõi.

## Đối chiếu theo cấu trúc ZIP nguồn Nhật

- Tệp nguồn: `JumpUltimateStars_Japan_BanGiao_Cloud.zip`, tổng **34.919 bản ghi** trong 30 tệp `translation/*.jsonl`.
- Các tệp nguồn từ đầu đến hết `06-jquiz-004.jsonl`, cộng 4 dòng đầu `06-jquiz-005.jsonl`: **25.340 dòng**.
- Bản gộp CP001–037 theo `PHUC_HOI_TONG_HOP_037.md`: **23.596 ID**, kết thúc ngay trước `06-jquiz-005.jsonl` `row_index=4`. **Chênh 1.744**. Cần lấy lại bản gộp CP001–037 và thực hiện so ID để xác định chính xác các dòng bị bỏ qua; **chưa được coi là đã dịch**.
- CP038–050: **9.150 ID**, đúng bằng số dòng liên tiếp từ `06-jquiz-005.jsonl` `row_index=4` cho đến hết `06-jquiz-009.jsonl`. Bộ J-Quiz đã kết thúc ở `question_index=3005`.
- Phần nguồn sau J-Quiz: `07-deck-001.jsonl` **352 dòng**, SHA256 `dc52ad7a1a57f2298c576f6783c4fe2b915ff7947a0f987d643682cdfa789950`; `08-credit-001.jsonl` **77 dòng**, SHA256 `08982eb9c40751e1ce85f90349b1194e2ae12d1ca8e40c47c95b447398914224`.

**Tổng cần xử lý: 1.744 + 352 + 77 = 2.173 ID.**

## Bước tiếp theo — CP051

1. Dịch `07-deck-001.jsonl` và `08-credit-001.jsonl` từ nguồn gốc, dùng quy tắc tên/item/skill giữ tiếng Anh.
2. Chú ý `source_fixed_field_bytes` trong Deck/Credits. Giới hạn **37 ký tự Unicode của J-Quiz không thay thế được giới hạn byte hoặc chiều rộng font của những trường này**.
3. Khôi phục CP001–037 theo `PHUC_HOI_TONG_HOP_037.md`. So tập ID từ ZIP gốc với tập ID CP001–037 + CP038–050; xuất danh sách ID thiếu theo `file` và `row_index`. Tránh giả định chênh lệch chỉ nằm trong một tệp hay dịch bù trùng.
4. Chỉ cộng tỷ lệ hoàn thành khi có `vi` thật, không trùng ID, metadata đúng nguồn và QA tĩnh đạt. Kiểm tra font và ROM vẫn là một bước riêng.

Bản gộp CP038–050 đã giữ sửa **Shunrei** từ CP046A. Overlay 037B/C khi phục hồi dùng **ghi đè `vi` theo ID**, không cộng bản ghi.


## Kiểm tra bổ sung ngày 20/11/2026 — CP051 (chưa thêm bản dịch)

Đã đọc trực tiếp các delta BAN_DICH_001–037 từ nhánh
vh/jump-ultimate-stars-japan và kiểm tra các dải file/row_index;
đã đối chiếu bản gộp CP038–050 từ ZIP CP050.

- CP001–037: 23.596 bản ghi, bao phủ 22 tên tệp nguồn.
- CP038–050: 9.150 ID duy nhất, bao phủ 06-jquiz-005 đến
  06-jquiz-009; bốn tên tệp mới bổ sung ngoài 22 tệp trước.
- Tổng cộng đã đụng tới 26 tên tệp nguồn; J-Quiz 005 có 4 dòng
  đầu ở CP037 và 1.877 dòng sau ở CP038–050, nối thành 1.881 dòng.
- Trong tất cả các dải file/row_index đã quan sát trên GitHub,
  không có lỗ hổng nội bộ: các phần được ghi liên tục từ 0 tới
  row_index lớn nhất đã xuất hiện của từng tệp.
- Nhật ký CP050 ghi tổng cộng 30 tệp nguồn (34.919 ID).
  Ngoài 26 tệp đã dịch và hai tệp 07-deck/08-credit (429 ID),
  có thể còn hai **tệp nguồn hoàn toàn chưa được dịch**.
  Đây chỉ là giả thuyết cần đối chiếu với danh sách tên tệp gốc,
  không phải kết luận chắc chắn rằng mọi ID thiếu thuộc hai tệp.
- 1.744 ID chênh lệch trước Deck/Credits vẫn là **chưa xác định**:
  không được tự tổng hợp câu Nhật, tự đặt ID hoặc tự nhận đã dịch.

**Trở ngại truy cập:** ZIP nguồn có trong Library cũ nhưng bản
gốc không được cấp quyền đọc byte ở phiên hiện tại; vì vậy không
thể nêu tên chính xác hai tệp nghi thiếu, đọc 352+77 dòng Deck/
Credits, hoặc hoàn thành phép so toàn bộ 34.919 ID ngay trong phiên này.

### Công cụ đã thêm lên GitHub

[AUDIT_CP051.py](AUDIT_CP051.py) là công cụ kiểm toán nguồn theo ID
không có thư viện ngoài Python chuẩn. Từ thư mục làm việc chứa repo,
chạy:

    python Jump-Ultimate-Stars-Japan/AUDIT_CP051.py JumpUltimateStars_Japan_BanGiao_Cloud.zip --translations Jump-Ultimate-Stars-Japan

Công cụ tìm JSONL trong ZIP lồng ZIP, xác thực tổng 30 tệp/34.919
ID, kiểm SHA256 gốc của Deck/Credits, so 50 tệp delta, từ chối ID
lạ/trùng, sai JA, sai file, sai row_index và xuất ra thư mục audit-051:

- CHUA_DICH_051.jsonl — đúng các dòng nguồn chưa có bản Việt;
- NGUON_DECK_CREDITS_051.jsonl — riêng 07/08 chưa dịch;
- QA_KIEM_TOAN_051.json — bảng chi tiết số dòng còn thiếu theo tệp.

**Trạng thái:** CP051 là giai đoạn kiểm toán/chuẩn bị; **0 bản dịch
mới**, không thay đổi số liệu 32.746/34.919. Chưa có QA font NDS,
kiểm byte thực tế của Deck/Credits, kiểm đáp án trong ROM hoặc patch.

## Xác nhận dứt điểm bằng ZIP nguồn Nhật (CP051)

**Nguồn đã mở thành công ở lượt tiếp theo.** Bộ dữ liệu đủ 30 JSONL/34.919 ID.
Đã đối chiếu ID + JA + file/row_index của **9.150 bản dịch CP038–050A** với ZIP gốc.
Bản dịch CP051 thêm **429 ID** từ Deck/Credits. Đối chiếu vùng chỉ mục CP001–037
đã xác minh trong GitHub, phần nguồn chưa được dịch xác định dứt điểm:

| Tệp gốc | Số ID thiếu | Chỉ mục |
| --- | ---: | --- |
| `00-he-thong-ten-goi-001.jsonl` | 1.231 | 0–1230 |
| `00-he-thong-ten-goi-002.jsonl` | 248 | 0–247 |
| `03-nhiem-vu-luat-001.jsonl` | 265 | 184–448 |
| **Tổng** | **1.744** | |

Không còn 429 ID Deck/Credits trong danh sách cần dịch.
Tiến độ sau CP051 **33.175 / 34.919 (95,01%)**.
Các đoạn CP050 đầu ghi 2.173 ID thiếu chỉ còn ý nghĩa lịch sử.
Nội dung từ `00` có nhiều dòng mô tả manga bị cắt nối, phải duyệt theo đoạn.
Danh sách chính xác 1.744 JSONL chưa dịch nằm trong gói ZIP CP051 bàn giao.

**Giới hạn kiểm toán:** CP001–037 được lấy theo các dải và số lượng đã
xác minh trước trên GitHub (23.596 ID), chưa thực hiện lại so checksum
từng byte của bản gộp CP001–037 trong lượt này. QA font và ROM vẫn chờ.
