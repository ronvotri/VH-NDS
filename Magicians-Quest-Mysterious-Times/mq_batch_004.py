#!/usr/bin/env python3
"""Manually composed Vietnamese item names and NPC vocal ticks, checkpoint 004.
Retains original IDs, source, control codes and JSONL order. Does not alter existing vi.
"""
from pathlib import Path
import json, re, collections, unicodedata, importlib.util
ROOT=Path(__file__).resolve().parent; ITEMS=ROOT/'translation/02-vat-pham'; NPC=ROOT/'translation/04-thoai/npc__NpcDataOfs_e.bin.001.jsonl'

def pairs(s):
 d={}
 for line in s.strip().splitlines():
  if not line.strip() or line.lstrip().startswith('#'):continue
  if ' => ' not in line:raise RuntimeError('invalid pair '+line)
  k,v=line.split(' => ',1)
  if k in d:raise RuntimeError('duplicate pair '+k)
  d[k]=v
 return d

def seq(s):return [x.strip() for x in s.strip().splitlines() if x.strip()]

M=pairs('''
Evil Wizard Hat => Mũ Phù Thủy Hắc Ám
Japanese Bridal Wig => Tóc Giả Cô Dâu Nhật
Firefighter Helmet => Mũ Cứu Hỏa
Topknot Wig => Tóc Giả Búi Cao
Cake Hat => Mũ Bánh Kem
Samurai Helmet => Mũ Samurai
Bear Hat => Mũ Gấu
Mouse Hat => Mũ Chuột
Arrow Through Head => Mũ Tên Xuyên Đầu
Afro Wig => Tóc Giả Afro
Dreadlock Wig => Tóc Giả Tết Dây
Shaved Head Wig => Tóc Giả Đầu Trọc
Ear Knit Cap => Mũ Len Tai Thỏ
Biker Helmet => Mũ Bảo Hiểm Biker
Racing Helmet => Mũ Đua Xe
Skull Mask => Mặt Nạ Đầu Lâu
Knight Helmet => Mũ Hiệp Sĩ
Spacesuit Helmet => Mũ Phi Hành Gia
Old Woman Mask => Mặt Nạ Bà Lão
Wild Sunglasses => Kính Râm Cá Tính
Spectacles => Kính Mắt
Dark-Rimmed Glasses => Kính Gọng Đen
Masquerade Mask => Mặt Nạ Hóa Trang
Thick Glasses => Kính Dày Cộp
Twinkling Eye Mask => Mặt Nạ Mắt Long Lanh
Hot-Blooded Eye Mask => Mặt Nạ Mắt Máu Lửa
Robot Visor => Kính Chắn Robot
Hot Water Pot => Bình Nước Nóng
Floor Chair => Ghế Bệt
Heater Table => Bàn Sưởi Kotatsu
Tea Chest => Tủ Đựng Trà
Retro Rice Cooker => Nồi Cơm Cổ Điển
Mosquito Coil Pig => Heo Đốt Nhang Muỗi
Three-Sided Mirror => Gương Ba Mặt
Tea Table => Bàn Trà
Electric Fan => Quạt Điện
Futon Bed => Giường Nệm Futon
Grandfather Clock => Đồng Hồ Quả Lắc
Mantelpiece => Bệ Lò Sưởi
Incense Burner => Lư Hương
Oriental Ornament => Đồ Trang Trí Á Đông
Jewelry Case => Hộp Trang Sức
Gong => Chiêng
Modern Glass Table => Bàn Kính Hiện Đại
Modern TV Stand => Kệ TV Hiện Đại
Modern Chest => Tủ Ngăn Kéo Hiện Đại
Modern Side Table => Bàn Phụ Hiện Đại
Modern Armchair => Ghế Bành Hiện Đại
Counter Table => Bàn Quầy
Modern Light => Đèn Hiện Đại
Blue Magazine Rack => Kệ Tạp Chí Xanh
Red Magazine Rack => Kệ Tạp Chí Đỏ
Magic Candlestick => Chân Nến Phép Thuật
Magic Workbench => Bàn Chế Phép
Magic Bookshelf => Giá Sách Phép Thuật
Celestial Globe => Quả Cầu Thiên Văn
Magic Chemical Shelf => Giá Hóa Chất Phép
Crystal Ball => Quả Cầu Pha Lê
Cauldron => Vạc Phép
Ice Sculpture => Tượng Băng
Icicles => Nhũ Băng
Skull Stand => Kệ Đầu Lâu
Creepy Fireplace => Lò Sưởi Rợn Người
Creepy Candlestick => Chân Nến Rợn Người
Creepy Old Clock => Đồng Hồ Ma Ám
Creepy Armor => Giáp Ma Ám
Forest Washbasin => Chậu Rửa Rừng Xanh
Forest Phone => Điện Thoại Rừng Xanh
Undersea Television => TV Đại Dương
Pink Colored Box => Hộp Đựng Đồ Hồng
White Colored Box => Hộp Đựng Đồ Trắng
Green Colored Box => Hộp Đựng Đồ Xanh Lá
Blue Colored Box => Hộp Đựng Đồ Xanh Dương
Yellow Colored Box => Hộp Đựng Đồ Vàng
Black Colored Box => Hộp Đựng Đồ Đen
Red Colored Box => Hộp Đựng Đồ Đỏ
Halloween Lamp => Đèn Halloween
Bat Clock => Đồng Hồ Dơi
Christmas Candle => Nến Giáng Sinh
Christmas Clock => Đồng Hồ Giáng Sinh
Christmas Cake => Bánh Kem Giáng Sinh
Christmas Stocking => Tất Giáng Sinh
Christmas Tree => Cây Giáng Sinh
Red Ribboned Box => Hộp Thắt Nơ Đỏ
Blue Ribboned Box => Hộp Thắt Nơ Xanh
Green Ribboned Box => Hộp Thắt Nơ Lục
Pine Decoration => Đồ Trang Trí Thông
Spiced Sake Set => Bộ Rượu Sake Gia Vị
Battledore => Vợt Hanetsuki
Rice Cake Decoration => Bánh Mochi Trang Trí
New Year Cuisine => Mâm Cỗ Năm Mới
Gold Folding Screen => Bình Phong Vàng
Samurai Armor => Bộ Giáp Samurai
Paper-Covered Lamp => Đèn Bọc Giấy
Japanese Sword => Kiếm Nhật
Tea Ceremony Set => Bộ Trà Đạo
Treasure Box => Hộp Báu Vật
Cushion & Armrest => Đệm Và Gối Tựa
Japanese Food Tray => Khay Ăn Nhật
Solar System => Hệ Mặt Trời
Seven Sisters => Chòm Thất Nữ
Red Dwarf => Sao Lùn Đỏ
UFO => Đĩa Bay UFO
Asteroid Belt => Vành Đai Tiểu Hành Tinh
Space Station => Trạm Không Gian
Space Shuttle => Tàu Con Thoi
Amazing Telescope => Kính Thiên Văn Kỳ Diệu
Black Hole => Hố Đen
Galactic System => Hệ Thiên Hà
Halley's Comet => Sao Chổi Halley
Moon => Mặt Trăng
Large Boiler => Lò Hơi Lớn
Steam Turbine => Tua-bin Hơi
Steam Generator => Máy Tạo Hơi
Steam Pressure Gauge => Đồng Hồ Áp Suất Hơi
Airship => Khí Cầu Bay
Experiment Tool Set => Bộ Dụng Cụ Thí Nghiệm
Laboratory Table => Bàn Thí Nghiệm
Chemical Rack => Giá Hóa Chất
Tool Box => Hộp Dụng Cụ
Control Device => Thiết Bị Điều Khiển
Capsule Bed => Giường Khoang
Cargo Case => Thùng Hàng
Escape Pod => Khoang Thoát Hiểm
Cockpit Seat => Ghế Buồng Lái
Captain's Seat => Ghế Thuyền Trưởng
Strategy Table => Bàn Chiến Thuật
Transmitter => Máy Phát Tín Hiệu
Monitor => Màn Hình
Radar Clock => Đồng Hồ Ra-đa
LED Lamp => Đèn LED
DJ Booth => Bàn DJ
Spotlight => Đèn Rọi
Drinks Rack => Kệ Đồ Uống
Disco Speaker => Loa Disco
Mirror Ball => Cầu Gương Disco
Chalice Stand => Chân Đế Chén Thánh
Chalice => Chén Thánh
Hieroglyphic Table => Bàn Chữ Tượng Hình
Ancient Throne => Ngai Cổ
Strange Stone Tablet => Phiến Đá Bí Ẩn
Sarcophagus => Quan Tài Đá
Crystal Skull => Sọ Pha Lê
Trapped Skeleton => Bộ Xương Mắc Kẹt
Pillar Relic => Cột Di Tích
Ancient God Statue => Tượng Thần Cổ
Treasure Chest => Rương Báu
Treasure Map Table => Bàn Bản Đồ Kho Báu
Cannon => Đại Bác
Pirate Chair => Ghế Hải Tặc
Saber => Kiếm Cong
Cask => Thùng Gỗ
Compass => La Bàn
Ship's Wheel => Bánh Lái Tàu
Musket Rack => Giá Súng Hỏa Mai
Pirate Flag => Cờ Hải Tặc
Menu Board => Bảng Thực Đơn
Drink Bar => Quầy Đồ Uống
Restaurant Table => Bàn Nhà Hàng
Restaurant Chair => Ghế Nhà Hàng
Restaurant Register => Máy Tính Tiền
Salad Bar => Quầy Salad
Restaurant Partition => Vách Ngăn Nhà Hàng
High Chair Baby Seat => Ghế Ăn Dặm Cho Bé
Stone Desk => Bàn Học Bằng Đá
Stone Table => Bàn Đá
Stone Chair => Ghế Đá
Pelt Bed => Giường Da Thú
Stuffed Mammoth => Voi Ma Mút Nhồi Bông
Meat On Bone => Thịt Có Xương
Stone Currency => Tiền Đá
Earthenware => Đồ Gốm Đất
Roasted Pig => Heo Quay
Stone-Tipped Spears => Lao Đầu Đá
Route 66 Sign => Biển Đường 66
Cruiser Motorcycle => Xe Mô Tô Cruiser
Gas Stand => Trụ Bơm Xăng
Tire Stack => Chồng Lốp Xe
Rusty Drum Can => Thùng Phuy Rỉ Sét
Old Vending Machine => Máy Bán Hàng Cũ
Water Tower => Tháp Nước
Motel Sign => Biển Nhà Nghỉ
Ancient Well => Giếng Cổ
Aged Lantern => Đèn Lồng Cũ
Wisp => Đốm Lửa Ma
Torn Paper Lantern => Đèn Giấy Rách
Grave => Ngôi Mộ
Willow Tree => Cây Liễu
Haunted House Sign => Biển Nhà Ma
Great King Enma => Diêm Vương Đại Đế
Toy Block Train => Tàu Hỏa Lắp Ghép
Study Desk => Bàn Học
Toy Block Castle => Lâu Đài Lắp Ghép
Toy Box => Hộp Đồ Chơi
Jungle Gym => Khung Leo Trèo
Christmas Dinner => Bữa Tối Giáng Sinh
Tea Set => Bộ Ấm Trà
Hand-Rolled Sushi => Sushi Cuốn Tay
Steak Set => Suất Bít Tết
Mandarin Orange => Quả Quýt
Ramen Noodles => Mì Ramen
French Cooking => Món Ăn Pháp
Yam Cha Set => Bộ Điểm Tâm Yum Cha
Hamburger Set => Suất Hamburger
Sukiyaki => Lẩu Sukiyaki
School Lunch => Bữa Trưa Ở Trường
Breakfast => Bữa Sáng
Birthday Cake => Bánh Sinh Nhật
Pizza => Pizza
C-Store Counter => Quầy Cửa Hàng Tiện Lợi
C-Store Cooler => Tủ Mát Cửa Hàng Tiện Lợi
C-Store Bookshelf => Giá Sách Cửa Hàng Tiện Lợi
Product Shelf => Kệ Hàng Hóa
Steamer => Nồi Hấp
Lunch Box Rack => Kệ Hộp Cơm
Hot Pot Heater => Bếp Lẩu
ATM => Máy ATM
Sundries Shelf => Kệ Đồ Linh Tinh
Small Garden Rock => Đá Vườn Nhỏ
Large Garden Rock => Đá Vườn Lớn
Garden Lantern => Đèn Sân Vườn
Bamboo Fountain => Vòi Nước Tre
Garden Pond => Hồ Sân Vườn
Raccoon Dog Statue => Tượng Tanuki
Bamboo Fence => Hàng Rào Tre
Bonsai Stand => Kệ Bonsai
Rose Archway => Cổng Hoa Hồng
Rose Lattice => Giàn Hoa Hồng
Fountain Pond => Hồ Phun Nước
Goddess Statue => Tượng Nữ Thần
Cherub Fountain => Đài Phun Thiên Thần Nhỏ
Garden Gnome => Tượng Chú Lùn Sân Vườn
Lattice Fence => Hàng Rào Mắt Cáo
Torch => Đuốc
White Picket Fence => Hàng Rào Gỗ Trắng
Paddling Pool => Hồ Bơi Trẻ Em
Swing => Xích Đu
Hammock => Võng
Barbeque Set => Bộ Nướng BBQ
Tent => Lều
Lantern => Đèn Lồng
Camp Stove => Bếp Dã Ngoại
Pool Chair => Ghế Hồ Bơi
Garden Table => Bàn Vườn
Garden Chair => Ghế Vườn
Garden Bench => Ghế Dài Sân Vườn
Table & Parasol => Bàn Và Dù Che
Open-Air Bath => Bồn Tắm Ngoài Trời
Pumpkin Coach => Xe Ngựa Bí Ngô
Pandora's Box => Chiếc Hộp Pandora
Magic Lamp => Đèn Thần
Magic Mirror => Gương Thần
Card Soldier => Lính Bài Tây
Giant Peach => Quả Đào Khổng Lồ
Flower Bud Sofa => Sofa Nụ Hoa
Poisoned Apple => Táo Độc
Animal Band => Ban Nhạc Thú
Glass Slipper => Giày Thủy Tinh
Hearth => Lò Sưởi
Loom => Khung Cửi
Pestle & Mortar => Chày Cối
Throne => Ngai Vàng
Magic School Desk => Bàn Học Trường Phép
Magic School Chair => Ghế Trường Phép
Japanese School Desk => Bàn Học Kiểu Nhật
Japanese School Seat => Ghế Học Kiểu Nhật
Modern School Desk => Bàn Học Hiện Đại
Modern School Chair => Ghế Học Hiện Đại
Austere School Desk => Bàn Học Giản Dị
Austere School Chair => Ghế Học Giản Dị
Pachira => Cây Kim Ngân
Weeping Fig => Cây Si Rủ
Areca Palm => Cau Cảnh
Snake Plant => Cây Lưỡi Hổ
Aloe Vera => Nha Đam
Baobab => Cây Bao Báp
Bamboo => Tre
Passionate Heart => Tim Nồng Cháy
Agave Attenuata => Thùa Cảnh
Old Lady Cactus => Xương Rồng Bà Lão
Venus Fly Trap => Cây Bắt Ruồi
Man-Eater => Cây Ăn Thịt Người
Palm Tree => Cây Cọ
Candelabra Cactus => Xương Rồng Chân Nến
Arrowroot => Cây Dong
Traveler's Palm => Cây Chuối Rẻ Quạt
Monstera => Trầu Bà Lá Xẻ
Maple Bonsai => Bonsai Phong
Zelkova Bonsai => Bonsai Du Nhật
Black Bamboo Bonsai => Bonsai Trúc Đen
Plum Bonsai => Bonsai Mai Mận
Quince Bonsai => Bonsai Mộc Qua
Gramophone => Máy Hát Đĩa Cổ
White Stereo => Dàn Âm Thanh Trắng
Stereo => Dàn Âm Thanh
Vacuum Amp => Ampli Đèn
HD Stereo => Dàn Âm Thanh HD
Turntable => Bàn Xoay Đĩa
Dancing Flower => Hoa Nhảy Múa
Teddy Bear Player => Máy Nhạc Gấu Bông
Speaker Chair => Ghế Gắn Loa
Jukebox => Máy Phát Nhạc Tự Động
Futuristic TV => TV Tương Lai
DVD Player => Đầu DVD
Personal Computer => Máy Tính Cá Nhân
Ultra-Thin TV => TV Siêu Mỏng
White Flat-Panel TV => TV Màn Phẳng Trắng
Black Flat-Panel TV => TV Màn Phẳng Đen
Pink Flat-Panel TV => TV Màn Phẳng Hồng
Old-Fashioned TV => TV Cổ Điển
Nightmare TV => TV Ác Mộng
Sub Woofer => Loa Siêu Trầm
Marionette Clock => Đồng Hồ Rối Dây
Wondrous Moon Clock => Đồng Hồ Trăng Kỳ Diệu
Sundial => Đồng Hồ Mặt Trời
Alarm Clock => Đồng Hồ Báo Thức
Cuckoo Clock => Đồng Hồ Chim Cúc Cu
Toy Clock => Đồng Hồ Đồ Chơi
Expensive Clock => Đồng Hồ Đắt Tiền
System Sink => Chậu Rửa Bếp Liền Khối
System Kitchen Bench => Bàn Bếp Liền Khối
System Dishwasher => Máy Rửa Bát Liền Khối
Family Refrigerator => Tủ Lạnh Gia Đình
Sink => Chậu Rửa
Cookware Stand => Kệ Nồi Chảo
Gas Range => Bếp Ga
Spice Rack => Giá Gia Vị
Retro Refrigerator => Tủ Lạnh Cổ Điển
2-Tub Washer/Spinner => Máy Giặt Hai Lồng
Front Load Washer => Máy Giặt Cửa Trước
Microwave => Lò Vi Sóng
Toaster => Máy Nướng Bánh Mì
Rice Cooker => Nồi Cơm Điện
Iron => Bàn Là
Coffee Maker => Máy Pha Cà Phê
Marble Bathtub => Bồn Tắm Cẩm Thạch
Clawfoot Bathtub => Bồn Tắm Chân Sư Tử
Wooden Bathtub => Bồn Tắm Gỗ
Washbasin => Chậu Rửa Mặt
Rose Vase => Bình Hoa Hồng
Single Flower Vase => Bình Hoa Một Bông
French Doll => Búp Bê Pháp
Porcelain Vase => Bình Sứ
Porcelain Platter => Đĩa Sứ
Heater => Máy Sưởi
Exercise Bike => Xe Đạp Tập
Pinball Machine => Máy Pinball
System Tool Rack => Giá Dụng Cụ Liền Khối
Center Speaker => Loa Trung Tâm
Rear Speakers => Loa Phía Sau
Paper Sliding Doors => Cửa Trượt Giấy
Grand Sliding Screen => Bình Phong Trượt Lớn
Grand Tatami => Chiếu Tatami Lớn
Tatami Floor => Sàn Tatami
''')

# Furniture series: "Sofa" is always "sofa", "Wardrobe" is always "tủ áo".
FURN={
'Bed':'Giường','Wardrobe':'Tủ Áo','Chair':'Ghế','Sofa':'Sofa','Table':'Bàn','Low Table':'Bàn Thấp',
'Mini Table':'Bàn Nhỏ','Desk':'Bàn Học','Stand':'Kệ','Lamp':'Đèn','Clock':'Đồng Hồ',
'Dresser':'Bàn Trang Điểm','Bureau':'Tủ Ngăn Kéo','Bookcase':'Giá Sách','Screen':'Bình Phong',
'Armchair':'Ghế Bành','Chaise':'Ghế Nằm','Chest':'Tủ Ngăn Kéo','Cushion':'Gối Đệm',
'Mirror':'Gương','Washbasin':'Chậu Rửa','Television':'TV','Bathtub':'Bồn Tắm','Cupboard':'Tủ Bếp',
'Low Table':'Bàn Thấp'}
SETS={
'Antique':'Cổ','Oriental':'Á Đông','Wooden':'Gỗ','Princess':'Công Chúa','Celebrity':'Ngôi Sao',
'Chinese':'Trung Hoa','Modern':'Hiện Đại','Stripy Blue':'Sọc Xanh','Stripy Red':'Sọc Đỏ',
'Candy':'Kẹo Ngọt','Ice':'Băng','Gothic':'Gothic','Creepy':'Rợn Người','Forest':'Rừng Xanh',
'Daisy':'Cúc Họa Mi','Undersea':'Đại Dương','Brown':'Nâu','Beige':'Be','Pink':'Hồng',
'Sky Blue':'Xanh Da Trời','Halloween':'Halloween','Christmas':'Giáng Sinh'
}
# Flooring and wallpaper patterns: use "Tường ..." and "Sàn ..." consistently.
SURF={
'Austere':'Giản Dị','Oriental':'Á Đông','Wooden':'Gỗ','Princess':'Công Chúa',
'Celebrity':'Ngôi Sao','Chinese':'Trung Hoa','Modern':'Hiện Đại','Blue Stripy':'Sọc Xanh',
'Red Stripy':'Sọc Đỏ','Magic Circle':'Vòng Ma Thuật','Candy':'Kẹo Ngọt',
'Ice':'Băng','Gothic':'Gothic','Creepy':'Rợn Người','Forest':'Rừng Xanh',
'Flower':'Hoa','Undersea':'Đại Dương','Halloween':'Halloween','Christmas':'Giáng Sinh',
'Space':'Không Gian','Laboratory':'Phòng Thí Nghiệm','Cockpit':'Buồng Lái',
'Disco':'Disco','Ancient Ruin':'Di Tích Cổ','Pirate Ship':'Tàu Hải Tặc',
'Restaurant':'Nhà Hàng','Cave':'Hang Động','Route 66':'Đường 66',
'Haunted House':'Nhà Ma','Magic School':'Trường Phép','Japan School':'Trường Nhật',
'Modern School':'Trường Hiện Đại','Austere School':'Trường Giản Dị',
'Concrete':'Bê Tông','Dirty':'Bẩn','Arabian':'Ả Rập','Aristocratic':'Quý Tộc',
'Normal White':'Trắng Trơn','Marble':'Cẩm Thạch','Snow':'Tuyết',
'Timber':'Gỗ Xẻ','Tasteful':'Thanh Lịch','Checkered':'Ô Vuông',
'Diamond':'Hình Thoi','Heart':'Trái Tim','Polka Dot':'Chấm Bi',
'Stained Glass':'Kính Màu','Hellfire':'Lửa Địa Ngục','Farm':'Nông Trại',
'Plain Wood':'Gỗ Trơn','Skyscraper':'Nhà Chọc Trời','Retail Store':'Cửa Hàng',
'Contemporary':'Đương Đại','Blue Pattern':'Hoa Văn Xanh',
'Moon Surface':'Mặt Trăng','Mosaic Tile':'Gạch Mosaic','Pizza':'Pizza',
'Rose Pattern':'Họa Tiết Hoa Hồng','Arabian':'Ả Rập'
}

def vn(en):
 if en in M:return M[en]
 # Wood color series, and one source typo "Wooden Soft - Blue" = Sofa
 if en.startswith('Wooden ') and ' - ' in en:
  left,right=en.split(' - ',1)
  obj=left.replace('Wooden ','').replace('Soft','Sofa')
  if obj in FURN:return f'{FURN[obj]} Gỗ '+{'Red':'Đỏ','Blue':'Xanh'}.get(right,right)
 for k,theme in sorted(SETS.items(),key=lambda kv:-len(kv[0])):
  if en.startswith(k+' '):
   noun=en[len(k)+1:]
   if noun in FURN: return FURN[noun]+' '+theme
 if en.endswith(' Walls'):
  typ=en[:-6]
  if typ in SURF:return 'Tường '+SURF[typ]
 if en.endswith(' Floor'):
  typ=en[:-6]
  if typ in SURF:return 'Sàn '+SURF[typ]
 return None

# Cross-references: fish and insect names exactly as the Vietnamese natural history notebook.
spec=importlib.util.spec_from_file_location('mq003',str(ROOT/'mq_translate_003.py'))
# Do not execute this module (it mutates records); load its authored lists safely via AST.
import ast
source=(ROOT/'mq_translate_003.py').read_text(encoding='utf8')
tree=ast.parse(source)
for node in tree.body:
 if isinstance(node,ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Name) and node.targets[0].id in ('BUG_NAMES','FISH_NAMES'):
  val=node.value
  if not isinstance(val,ast.Call) or not isinstance(val.args[0],ast.Constant):raise RuntimeError('unexpected source list')
  globals()[node.targets[0].id]=seq(val.args[0].value)
assert len(FISH_NAMES)==67 and len(BUG_NAMES)==64

def load(path):return [json.loads(s) for s in path.read_text(encoding='utf8').splitlines()]
def save(path,data):path.write_text(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n' for x in data),encoding='utf8')

changes=[]; unknown=[]
for f in sorted(ITEMS.glob('item__ItemName_e.ofs.*.jsonl')):
 num=int(f.name.split('.')[-2]);d=load(f); prior=[x['vi'] for x in d]
 for i,x in enumerate(d):
  if x['vi'] is not None:continue
  if num==12 and 20<=i<=86: v=FISH_NAMES[i-20]
  elif num==12 and i>=87: v=BUG_NAMES[i-87]
  elif num==13: v=BUG_NAMES[33+i]
  else: v=vn(x['en'])
  if v is None:unknown.append((num,i,x['en']));continue
  v=unicodedata.normalize('NFC',v)
  if num>=12: v=v[0].upper()+v[1:]
  x['vi']=v
  changes.append({'file':str(f.relative_to(ROOT)),'id':x['id'],'en':x['en'],'vi':v,'old':None})
 if prior!=[x['vi'] for x in d]:save(f,d)

print('Translated:',len(changes),'Unmapped:',len(unknown))
for num,i,en in unknown:print(f'UNMAPPED {num:03d} {i:03d} {en}')
(ROOT/'BATCH-004-PART1.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in changes),encoding='utf8')