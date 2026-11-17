# Ragnarok DS (USA) — Việt hóa NDS

Nhánh độc lập `vh/ragnarok-ds-usa` của kho `VH-NDS`. Không trộn với các dự án Ni no Kuni, Magician’s Quest hoặc Ragnarok Odyssey ACE.

## Nguồn dữ liệu
- Bàn giao: `RagnarokDS_USA_BanGiao_Cloud.zip` (ROM USA, mã YRBE).
- Tổng 14.616 mục trong 33 tệp JSONL: 14.597 chuỗi và 19 nhãn ảnh; không bao gồm ROM.
- Đợt 001: 304 mục đã điền `vi` (219 bản Việt khác nguồn, 85 mục giữ nguyên), 14.312 mục còn `null`.
- Kiểm tra bằng `tools/check_handoff.py`: 14.616 ID; **0 lỗi**, chưa bật `--require-complete` vì đây là bản dịch từng phần.

## Quy ước
- Giữ nguyên **tên riêng, tên Job, item, skill, quái, địa điểm, tên Guild, Zeny, HP, SP, ATK, DEF và thuật ngữ gameplay chủ chốt**. 
- Việt hóa thông báo, hội thoại, mô tả, hướng dẫn, credit và nhãn UI không phải thuật ngữ chính.
- Giọng tự nhiên, gần gũi, điểm hài vừa phải; cảnh bi kịch phải được tôn trọng. Không thêm meme làm sai tính cách.
- Giữ nguyên **ID, trường en, thứ tự JSONL và mọi thẻ <Cxxxx>**, biến dạng %s/%d và ngắt dòng mã hóa.
- Ngôi xưng dựa trên lời thoại lân cận, không đoán quan hệ/tuổi/giới tính.
- Không tự sửa/đăng ROM thương mại. Chưa có font Việt, chưa patch và chưa test giả lập/máy thật.

## Tập tin bàn giao

Bản ZIP đầy đủ của đợt 001 đã được xuất trong phiên ChatGPT, gồm toàn bộ 33 JSONL với `vi=null` cho phần chưa dịch, `THUAT_NGU.json`, `QUY_TAC_XUNG_HO.md`, `DANH_BA_NHAN_VAT.json`, `BAO_CAO.txt` và `PATCH-DOT001.jsonl`.


## Checkpoint 002 — 18/11/2026

- **Đợt 002 thêm 759 ID:** +669 hệ thống và +90 hội thoại đầu game.
- **Tổng cộng 1.063/14.616 mục:** 922 bản Việt khác nguồn, 141 mục giữ nguyên tiếng Anh, 13.553 mục chưa xử lý.
- **QA chính thức:** 0 lỗi ID và mã điều khiển, không thay `en` hoặc các trường ngữ cảnh; chưa test font/máy thật.
- Đợt 002 ở `translation/PATCH-DOT002.jsonl`; đợt 001 ở 5 tệp `PATCH-DOT001-*.jsonl`. Công cụ `tools/apply_patches.py` sẽ tự áp dụng **cả hai** theo ID.
- Bộ ZIP đủ 33 JSONL đã xuất riêng trong phiên trò chuyện, kèm `THUAT_NGU.json`, hồ sơ xưng hô, báo cáo QA. Không đưa ROM lên GitHub.

## Khôi phục bản dịch từ GitHub

Trong nhánh có **1.063 patch records** từ cả đợt 001 và 002, không trùng ID; đối chiếu với source gốc trước khi áp dụng.

```bash
python Ragnarok-DS/tools/apply_patches.py \
  --handoff RagnarokDS_USA_BanGiao_Cloud.zip \
  --patch-dir Ragnarok-DS/translation \
  --output RagnarokDS_VH_Checkpoint_002_GitHub.zip
```

Lệnh chỉ xuất ZIP dịch thuật, không chỉnh ROM hay font và không xóa dòng chưa dịch. Bản ZIP đã xuất trực tiếp trong phiên chat còn có danh bạ nhân vật và bảng thuật ngữ cập nhật.

## Kiểm tra khi nhận bản ZIP

```sh
python tools/check_handoff.py --source INPUT/translation --translation KET_QUA/translation
```

Không dùng `--require-complete` cho các đợt chưa dịch xong. Nhớ đối chiếu tên/mô tả và ảnh UI trước khi đóng gói vào game.
