#!/usr/bin/env python3
"""Curated clothing and accessory translations, preserving exact JSONL indices and source fields."""
import json, pathlib, unicodedata
R=pathlib.Path(__file__).resolve().parent
D=R/'translation/02-vat-pham'
def entries(raw):return [x.strip() for x in raw.strip().splitlines() if x.strip()]
V={
4:entries('''
Áo Rocker
Áo Ngủ
Áo Mưa
Áo Aloha Xanh
Áo Nửa Tim Trái
Áo Nửa Tim Phải
Áo Mầm Non Hồng
Áo Ông Lão
Áo Diễn Viên Hài
Áo Cao Bồi
Áo Vest Lịch Lãm
Áo Nhà Thám Hiểm
Áo Tù Nhân
Áo Thân Robot
Áo Happi Xanh
Áo Happi Đỏ Khuyến Mãi
Áo Hình Bộ Xương
Áo UFO
Áo Giáp Hiệp Sĩ
Áo Chú Hề
Áo Ông Già Noel
Áo Quý Tộc
Áo Hải Tặc
Áo Gile Biker Da
Tạp Dề
Áo Hoàng Tử
Áo Phi Hành Gia
Áo Bánh Quy
Áo Lấm Lem
Áo Đồ Bay
Áo Dân Làng
Áo Người Lùn
Áo Thể Thao
Áo Võ Judo
Áo Tennis
Áo Bóng Chày
Áo Bóng Rổ
Áo Bóng Đá
Áo Vest Công Sở
Áo Vest Trơn
Áo Khoác Bomber Đỏ
Áo Khoác Bomber Xanh Trời
Áo Tuxedo
Áo Jinbei
Áo Hakama Huy Hiệu
Áo Giáp Samurai
Áo Mông Cổ
Áo Cận Vệ Hoàng Cung
Áo Miền Núi Alpine
Áo Sơ Mi Kẻ Xanh
Áo Sơ Mi Hồng
Áo Dấu Chân Thú
Áo Khoác Đắt Tiền
Áo Khoác Kẻ Sọc
Áo Khoác Lịch Sự
Áo Khoác Dự Tiệc
Áo Đỏ Trơn
Áo Khoác Túi Hoa
Áo Len Hoang Dã
Áo Cổ Vàng
Áo Thắt Đai
Áo Len Dày
Áo Gile Đỏ
Áo Khoác Hai Hàng Cúc
Áo Khoác Cổ Điển
Áo Khoác Xanh Lá
Áo Khoác Kimono Xanh
Áo Sắc Cầu Vồng
Áo Ba Lỗ Denim Đỏ
Áo Khoác Nút Đỏ
Áo Len Hình Thoi
Áo Chấm Bi Đỏ
Áo Họa Tiết Hoa
Áo Hồng Trơn
Áo Ngôi Sao
Áo Vá Xanh Lá
Áo Vá Xanh Dương
Áo Dây Đan Chéo
Áo Trẻ Con Đỏ
Áo Túi Hoa
Áo Tím Trơn
Áo Hình Thoi Đen
Gile Len Kỳ Lạ
Gile Da Hổ
Sườn Xám
Áo Chữ Hán
Áo Chữ Số Điện Tử
Áo Tunic Bèo Nhún
Áo Cổ Ngữ Phép Thuật
Áo Hồng Chuyển Màu
Áo Màu Bột Ca Cao
Áo Trắng Tinh
Áo Dưa Lưới
Áo Sơ Mi Người Lớn
Áo Cổ Thủy Thủ
Áo Ả Rập
Áo Thắt Nơ
Áo Lộng Lẫy
Áo Hạt Dẻ
Áo Cánh Bướm
Gile Len Hồng
Áo Kiểu Nữ
Áo Chấm Bi Xanh
Áo Toga Hy Lạp
Áo Sặc Sỡ
Áo Cardigan Nơ
Đồ Múa Nhật Bản
Áo Khoác Bomber Đen
Áo Mầm Non Xanh
Áo Vàng Pastel
Áo Mèo Trái Tim
Áo Tunic Hoa Đào
Áo Khoác Kem
Áo Chữ Xanh Lá
Áo Sọc Sành Điệu
Áo Flannel Thanh Lịch
Áo Mặt Trời Mọc
Áo Len Vitamin
Áo Len Màu Đào
Áo Khoác Denim Nâu
'''),
5:entries('''
Áo Ngọn Lửa Đen
Áo Đầu Lâu Xanh Lá
Áo Cam Lịch Lãm
Áo Biker Đỏ
Áo Số 7
Áo Nhuộm Loang Rực Rỡ
Áo Khoác Phao Trắng
Áo Biểu Tượng Hòa Bình Cam
Áo Xanh Cực Ngầu
Áo Sơ Mi Nữ
Áo Chắp Vá Hồng
Áo Rằn Ri Hồng
Áo Nút Vàng
Áo Khoác Da Đen
Áo Aloha Đỏ
Áo Happi Đỏ
Quần Đồng Phục
Quần Denim
Quần Denim Xanh
Quần Denim Hồng
Quần Chuyển Màu
Quần Jean Rách
Quần Legging
Quần Kaki Chino
Quần Jean Gập Gấu Nhuộm Màu
Quần Jean Gập Gấu
Quần Túi Hộp
Quần Reggae
Quần Khóa Kéo
Quần Jean Gắn Xích
Quần Tartan Xanh
Quần Tartan Đỏ
Quần Punk Đầu Lâu
Quần Chắp Vá
Quần Họa Tiết Lửa
Quần Họa Tiết Hoa
Quần Jean Chỉ Nổi
Quần Tất Chấm Bi
Quần Âu Blazer
Quần Gập Gấu
Quần Legging Phù Thủy
Quần Legging Đại Pháp Sư
Quần Rằn Ri
Quần Đặc Nhiệm
Quần Biker
Quần Phi Công
Quần Lính Cứu Hỏa
Quần Đồ Đua
Quần Sĩ Quan
Quần Rocker
Quần Ngủ
Quần Mầm Non
Quần Ông Lão
Quần Diễn Viên Hài
Quần Cao Bồi
Quần Vest Lịch Lãm
Quần Nhà Thám Hiểm
Quần Tù Nhân
Quần Robot
Quần Lễ Hội
Quần Bộ Xương
Quần Giáp Hiệp Sĩ
Quần Chú Hề
Quần Ông Già Noel
Quần Hải Tặc
Quần Da Biker
Quần Hoàng Tử
Quần Phi Hành Gia
Quần Bánh Quy
Quần Lấm Lem
Quần Đồ Bay
Quần Dân Làng
Quần Người Lùn
Quần Thể Thao
Quần Võ Judo
Quần Tennis
Quần Bóng Chày
Quần Bóng Rổ
Quần Bóng Đá
Quần Vest Công Sở
Quần Tuxedo
Quần Jinbei
Quần Giáp Samurai
Quần Mông Cổ
Quần Cận Vệ Hoàng Cung
Quần Alpine
Váy Tartan Xanh
Váy Denim
Váy Denim Xanh
Váy Denim Bèo Nhún
Váy Chuyển Màu Nóng
Váy Chuyển Màu Lạnh
Váy Ô Vuông
Váy Bèo Nhún
Váy Hoa
Váy Chấm Bi Hồng
Váy Y Tá
Váy Thắt Nơ
Váy Denim Viền Ren
Váy Tartan Đỏ
Váy Da Báo
Váy Punk Đầu Lâu
Váy Chấm Bi Xanh
Váy Trời Đêm
Váy Reggae
Quần Quý Tộc
Váy Blazer
Váy Thủy Thủ
Váy Lấp Lánh
Váy Bèo Nhiều Tầng
Váy Rằn Ri
Váy Nhân Viên Phục Vụ
Váy Sĩ Quan
Váy Rocker
Váy Mầm Non
Váy Nhà Thám Hiểm
Quần UFO
Váy Ông Già Noel
Váy Bánh Quy
Váy Lấm Lem
'''),
6:entries('''
Váy Tennis
Váy Trơn
Quần Hakama Huy Hiệu
Váy Mông Cổ
Váy Alpine
Váy Đồng Phục
Áo Choàng Phù Thủy Xanh
Áo Choàng Đại Pháp Sư
Áo Khoác Đồng Phục
Đầm Len
Đầm Kẻ Sọc
Đầm Hồng Thắt Nơ
Đầm Cổ Vắt Chéo
Đầm Xếp Nếp
Đầm Tartan
Đầm Gothic Lolita
Đầm Sọc Xanh
Đầm Trắng Tinh
Đầm Trắng Bèo Nhún
Đầm Hoa
Đầm Hiện Đại
Đầm Cổ Điển
Đầm Hai Dây
Đầm Len Trắng
Đầm Len Dài
Đầm Eo Cao
Đầm Denim Xanh
Đầm Denim Đen
Đầm Chiffon
Yukata Cá Vàng
Yukata Hoa Cẩm Tú Cầu
Đầm Công Chúa
Đầm Đi Chơi Chủ Nhật
Đầm Xanh Hải Quân
Tạp Dề Xanh
Đầm Biểu Diễn
Đầm Hầu Gái
Váy Cưới
Đầm Cocktail
Áo Khoác Duffle Sang Trọng
Đồng Phục Bồi Bàn
Áo Khoác Thám Tử
Áo Lông Giả Vàng
Áo Khoác Trench
Áo Khoác Da Cao Cấp
Áo Choàng Nhà Vua
Áo Choàng Phù Thủy Đỏ
Đầm Len Xanh
Đầm Xanh Da Trời
Đầm Sọc Vàng
Tạp Dề Hồng
Áo Khoác Duffle Xanh
Áo Lông Giả Trắng
Giày Da Thường
Dép Đi Hành Lang
Giày Loafer
Dép Xăng Đan
Xăng Đan Thắt Nơ
Giày Da Thời Trang
Giày Moccasin
Giày Cao Gót Hồng
Giày Cao Gót Đỏ
Giày Thể Thao Công Nghệ
Giày Da Nổi Bật
Bốt Phù Thủy
Dép Thủy Tinh
Dép Zori
Dép Đi Trong Trường
Giày Miền Tây
Giày Thể Thao Ngầu
Giày Thể Thao Thường
Giày Đinh
Giày Ô Vuông
Giày Leo Núi
Giày Họa Tiết Hoa
Giày Cài Nút
Giày Cài Khóa
Bốt Ông Già Noel
Giày Bạc
Giày Kêu Chít Chít
Giày Rằn Ri
Giày Hoàng Tử
Giày Công Chúa
Vương Miện Công Chúa
Vương Miện Hầu Gái
Vương Miện Cô Dâu
Mũ Y Tá
Mũ Đội Đầu Chiến Binh
Vương Miện Nhà Vua
Mũ Pháp Sư Tập Sự
Mũ Pháp Sư 1 Sao
Mũ Pháp Sư 2 Sao
Mũ Pháp Sư 3 Sao
Mũ Pháp Sư 4 Sao
Mũ Đại Pháp Sư
Mũ Bảo Hiểm Rằn Ri
Mũ Phi Công
Mũ Sĩ Quan
Mũ Diễn Viên Hài
Mũ Mầm Non
Mũ Cao Bồi
Mũ Nhà Thám Hiểm
Mũ Thám Tử
Mũ Chú Hề
Mũ Ông Già Noel
Mũ Hải Tặc
Mũ Người Lùn
Mũ Bóng Chày
Mũ Da Gấu
Mũ Lưỡi Trai Xanh
Mũ Lưỡi Trai Lục
Mũ Len Thường
Mũ Len Có Quả Bông
Mũ Rơm
Mũ Chống Nắng Trắng
Mũ Quý Ông
Mũ Có Vành Phẳng
Mũ Tốt Nghiệp
Mũ Thợ Săn
Mũ Phù Thủy Đáng Yêu
''')}
assert all(len(v)==120 for v in V.values()),{k:len(v) for k,v in V.items()}
extra={
'Rocking Chair':'Ghế Bập Bênh',
'Wood Fired Stove':'Bếp Củi',
'Stuffed Mammoth ':'Voi Ma Mút Nhồi Bông'
}
changes=[]
for num in (4,5,6,7,9):
 p=D/f'item__ItemName_e.ofs.{num:03d}.jsonl'
 rows=[json.loads(s) for s in p.read_text(encoding='utf8').splitlines()]
 for i,x in enumerate(rows):
  if x['vi'] is not None:continue
  v=V[num][i] if num in V else extra.get(x['en'])
  if v is None:continue
  v=unicodedata.normalize('NFC',v)
  x['vi']=v
  changes.append({'file':str(p.relative_to(R)),'id':x['id'],'en':x['en'],'old':None,'vi':v})
 p.write_text(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n' for x in rows),encoding='utf8')
(R/'BATCH-004-PART2.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in changes),encoding='utf8')
print('Fashion, isolated furniture:',len(changes))