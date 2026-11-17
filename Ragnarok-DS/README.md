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

## Kiểm tra khi nhận bản ZIP

```sh
python tools/check_handoff.py --source INPUT/translation --translation KET_QUA/translation
```

Không dùng `--require-complete` cho các đợt chưa dịch xong. Nhớ đối chiếu tên/mô tả và ảnh UI trước khi đóng gói vào game.
