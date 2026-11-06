#!/usr/bin/env python3
"""Manually reviewed display item names for the third batch.
Run once against the checkpoint 002/003. Only fills missing `vi` fields.
"""
import json,pathlib,unicodedata
ROOT=pathlib.Path(__file__).parent
SRC=ROOT/'translation/02-vat-pham'

def mappings(s):
    d={}
    for line in s.strip().splitlines():
        line=line.strip()
        if not line or line.startswith('#'):continue
        e,v=line.split(' => ',1)
        if e in d:raise Exception('Duplicate: '+e)
        d[e]=v
    return d

M=mappings('''
Snowflake => Bông Tuyết
Dryad Seedling => Mầm Tiên Cây
Snowman => Người Tuyết
Dullahan's Head => Đầu Dullahan
Forbidden Tome => Cấm Thư
Mushroom => Nấm
Magic Circle => Vòng Ma Thuật
Footprint => Dấu Chân
Manhole => Nắp Cống
Mystery Circle => Vòng Bí Ẩn
Ring => Nhẫn
Cloud Hammock => Võng Mây
Demonslayer Medal => Huân Chương Trừ Quỷ
Pine Decoration => Đồ Trang Trí Thông
Halloween Lantern => Đèn Bí Ngô
Medal of Valor => Huân Chương Dũng Cảm
Treasure Chest => Rương Báu
Written Challenge => Thư Thách Đấu
Matches => Diêm
Christmas Tree => Cây Giáng Sinh
Griffin's Treasure => Báu Vật Griffin
Present => Quà Tặng
Seedling => Cây Non
Blackberry Bush => Bụi Mâm Xôi Đen
Blueberry Bush => Bụi Việt Quất
Cranberry Bush => Bụi Nam Việt Quất
Raspberry Bush => Bụi Mâm Xôi Đỏ
Strawberry Bush => Bụi Dâu Tây
Pine Mushroom => Nấm Tùng
Truffle => Nấm Cục
Tuber Truffle => Nấm Cục Tuber
Blewit Mushroom => Nấm Tím
Laughing Jim => Nấm Cười Jim
Forest Mushroom => Nấm Rừng
Straw Mushroom => Nấm Rơm
Field Mushroom => Nấm Đồng
Porcini Mushroom => Nấm Porcini
Morel Mushroom => Nấm Bụng Dê
Fly Agaric Mushroom => Nấm Độc Đỏ
Veiled Lady Mushroom => Nấm Nàng Mạng Che
Hedgehog Mushroom => Nấm Nhím
Parasol Mushroom => Nấm Dù
Chanterelle Mushroom => Nấm Mào Gà
King Oyster Mushroom => Nấm Đùi Gà
Rosso Coral Mushroom => Nấm San Hô Rosso
Trumpet Mushroom => Nấm Kèn
Hackberry Mushroom => Nấm Gỗ
Viscid Mushroom => Nấm Nhớt
Cauliflower Mushroom => Nấm Súp Lơ
Moonlit Mushroom => Nấm Ánh Trăng
Ram's Head Mushroom => Nấm Đầu Cừu
Pleurote Mushroom => Nấm Bào Ngư
Blackberry => Mâm Xôi Đen
Blueberry => Việt Quất
Cranberry => Nam Việt Quất
Raspberry => Mâm Xôi Đỏ
Strawberry => Dâu Tây
Rotten Berry => Quả Mọng Thối
Bone => Xương
Ore => Quặng
Trash => Rác
Stomach Remedy => Thuốc Đau Bụng
Headache Remedy => Thuốc Đau Đầu
Fever Remedy => Thuốc Hạ Sốt
Rose Seed => Hạt Hoa Hồng
Tulip Seed => Hạt Tulip
Marguerite Seed => Hạt Cúc Marguerite
May Lily Seed => Hạt Linh Lan
Blackberry Seedling => Cây Mâm Xôi Đen Non
Blueberry Seedling => Cây Việt Quất Non
Cranberry Seedling => Cây Nam Việt Quất Non
Raspberry Seedling => Cây Mâm Xôi Đỏ Non
Strawberry Seedling => Cây Dâu Tây Non
Special Rosso Coral => San Hô Rosso Đặc Biệt
Keepsake Furniture => Nội Thất Kỷ Niệm
Candy => Kẹo
Amethyst => Thạch Anh Tím
Aquamarine => Ngọc Xanh Biển
Diamond => Kim Cương
Emerald => Ngọc Lục Bảo
Ruby => Hồng Ngọc
Sapphire => Lam Ngọc
Turquoise => Ngọc Lam
Lapis Lazuli => Đá Lapis Lazuli
Crystal => Pha Lê
Iron Ore => Quặng Sắt
Gold Ore => Quặng Vàng
Silver Ore => Quặng Bạc
Copper Ore => Quặng Đồng
Tin Ore => Quặng Thiếc
Phosphorus Ore => Quặng Phốt Pho
Sulfur Ore => Quặng Lưu Huỳnh
Mandragora Root => Rễ Mandragora
Black Rose Thorn => Gai Hồng Đen
Ancient Dragon Scale => Vảy Rồng Cổ
Shooting Star Sliver => Mảnh Sao Băng
Witch's Claw => Móng Phù Thủy
Silver Scarab => Bọ Hung Bạc
Freaky Frog Fat => Mỡ Ếch Quái
Angel Elixir => Tiên Dược Thiên Thần
Rose Dew => Sương Hoa Hồng
Moondrop => Giọt Trăng
Maiden's Tears => Lệ Thiếu Nữ
Poison Apple Juice => Nước Táo Độc
Small Bone => Xương Nhỏ
Dog Bone => Xương Chó
Animal Bone => Xương Thú
Fish Bone => Xương Cá
Decayed Tooth => Răng Mục
Iron Bone => Xương Sắt
Old Umbrella Frame => Khung Ô Cũ
Pork Bones => Xương Heo
Chicken Bone => Xương Gà
Crystal Bone => Xương Pha Lê
Giant Fish Bone => Xương Cá Khổng Lồ
Dentures => Răng Giả
Pirate Bone => Xương Hải Tặc
Werewolf Fang => Nanh Người Sói
Mammoth Bones => Xương Voi Ma Mút
Inscribed Bone => Xương Khắc Chữ
Bone of a Lost Race => Xương Tộc Thất Lạc
Subterranean Bone => Xương Dưới Lòng Đất
Fossilized Bone => Xương Hóa Thạch
Giant's Bone => Xương Người Khổng Lồ
Ancient Dragon Bones => Xương Rồng Cổ
Ogre Horns => Sừng Yêu Tinh
Cursed Bones => Xương Bị Nguyền
Graveyard Bone => Xương Nghĩa Địa
Shade Remains => Di Hài Bóng Ma
Shovel => Xẻng
Fishing Pole => Cần Câu
Insect Net => Vợt Bắt Bọ
Watering Can => Bình Tưới
Cleaning Broom => Chổi Quét Dọn
Hot Rod Broom => Chổi Đua
Deck Brush => Bàn Chải Chà Sàn
White Stallion Broom => Chổi Bạch Mã
''')
COLORS={'White':'Trắng','Red':'Đỏ','Yellow':'Vàng','Pink':'Hồng','Blue':'Xanh','Orange':'Cam','Black':'Đen'}
FLOWERS={'Rose':'Hoa Hồng','Tulip':'Tulip','Marguerite':'Cúc Marguerite','May Lily':'Linh Lan','Heartflower':'Hoa Trái Tim','Skullflower':'Hoa Đầu Lâu','Gemflower':'Hoa Ngọc','Candyflower':'Hoa Kẹo'}
for species,vi in FLOWERS.items():
    for color,cvi in COLORS.items():
        M.setdefault(f'{color} {species}',f'{vi} {cvi}')
    M.setdefault(f'Wilted {species}',f'{vi} Héo')
for v in (1,10,100,1000,10000,100000):M[f'{v} Ritch']=f'{v:,} Ritch'.replace(',','.')

# Flying brooms, rods, fashion. Names are menu labels, not dialogue: favor concise words over slang.
M.update(mappings('''
Butterfly Broom => Chổi Bướm
Candy Broom => Chổi Kẹo
Flower Broom => Chổi Hoa
Lightning Broom => Chổi Sấm Sét
Off-Road Broom => Chổi Địa Hình
Aluminum Broom => Chổi Nhôm
Mini Vacuum Cleaner => Máy Hút Bụi Mini
Home Vacuum Cleaner => Máy Hút Bụi Gia Đình
Lantern Broom => Chổi Đèn Lồng
Reindeer Broom => Chổi Tuần Lộc
Snow Broom => Chổi Tuyết
Heart Broom => Chổi Trái Tim
Dragonfly Broom => Chổi Chuồn Chuồn
Phoenix Broom => Chổi Phượng Hoàng
Peacock Broom => Chổi Công
Dragon Broom => Chổi Rồng
Bone Broom => Chổi Xương
Dumpling Broom => Chổi Bánh Trôi
Spoon Broom => Chổi Muỗng
Shooting Star Broom => Chổi Sao Băng
Flute => Sáo
Violin => Vĩ Cầm
Saxophone => Kèn Saxophone
Acoustic Guitar => Guitar Mộc
Electric Guitar => Guitar Điện
Double Bass => Đàn Contrabass
Mini Drum Kit => Bộ Trống Mini
Maracas => Lắc Maracas
Star Staff => Trượng Ngôi Sao
Ring Wand => Đũa Phép Nhẫn
Pretty Cane => Gậy Xinh
Crystal Cane => Gậy Pha Lê
Magical Parasol => Dù Phép
Magic Hand => Bàn Tay Ma Thuật
Skull Staff => Trượng Đầu Lâu
Sunflower Cane => Gậy Hướng Dương
Wooden Cane => Gậy Gỗ
Poseidon Staff => Trượng Poseidon
Thunder Cane => Gậy Sấm Sét
Gentleman's Cane => Gậy Quý Ông
Boy's Uniform Top => Áo Đồng Phục Nam
Girl's Uniform Top => Áo Đồng Phục Nữ
Blazer Top => Áo Blazer
Standing Collar Top => Áo Cổ Đứng
Summer Sailor Top => Áo Thủy Thủ Hè
Winter Sailor Top => Áo Thủy Thủ Đông
Necktie & Blouse => Sơ Mi Kèm Cà Vạt
Ribbon & Blouse => Sơ Mi Kèm Nơ
Necktie & Knit Vest => Áo Len Cà Vạt
Ribbon & Knit Vest => Áo Len Thắt Nơ
Pink Logo Shirt => Áo Logo Hồng
Pastel Pink Shirt => Áo Hồng Pastel
Rainbow Cloud Shirt => Áo Mây Cầu Vồng
Cat Print Shirt => Áo Hình Mèo
Star Orange Shirt => Áo Sao Cam
Heart Pattern Shirt => Áo Họa Tiết Tim
Stripy Pastel Shirt => Áo Sọc Pastel
White Floral Tunic => Áo Tunic Hoa Trắng
Blue Pastel Parka => Áo Khoác Xanh Pastel
Number Logo Parka => Áo Khoác Logo Số
Heart Mark Parka => Áo Khoác Trái Tim
Sporty Camisole => Áo Hai Dây Thể Thao
Frilly Camisole => Áo Hai Dây Bèo
Cropped Denim Jacket => Áo Khoác Jean Ngắn
Layered Blouson => Áo Khoác Nhiều Lớp
Pink Down Vest => Áo Gile Phao Hồng
Stripy Wool Cardigan => Cardigan Len Sọc
Leopard Print Cami => Áo Hai Dây Da Báo
Red Letter Shirt => Áo Chữ Đỏ
Anarchy Symbol Shirt => Áo Logo Vô Chính Phủ
Peace Sign Shirt => Áo Ký Hiệu Hòa Bình
Techno Shirt => Áo Techno
Reggae Shirt => Áo Reggae
Stripy Orange Shirt => Áo Cam Kẻ Sọc
Camo Shirt Top => Áo Rằn Ri
Tulip Shirt => Áo Tulip
No. 5 Shirt => Áo Số 5
Cow Print Shirt => Áo Họa Tiết Bò
Diamond Shirt => Áo Kim Cương
Blue Star Shirt => Áo Sao Xanh
Flannel Shirt => Áo Flannel
Cowboy Shirt => Áo Cao Bồi
Checkered Shirt => Áo Carô
Blue Patchwork Shirt => Áo Chắp Vá Xanh
Simple Parka => Áo Khoác Đơn Giản
Zip Up Parka => Áo Khoác Có Khóa
Polo Shirt => Áo Polo
Purple Scarf Shirt => Áo Khăn Tím
Fluffy Sweater => Áo Len Bông Xù
Earth Color Sweater => Áo Len Màu Đất
Love Sweater => Áo Len Tình Yêu
Bluish Jumper => Áo Chui Đầu Xanh
Down Vest => Áo Gile Phao
Open Western Shirt => Sơ Mi Cao Bồi Mở
Layered Parka => Áo Khoác Phối Lớp
Plain V-Neck Sweater => Áo Len Cổ V Trơn
Zip Up Blouson => Áo Khoác Khóa Kéo
Blue Down Jacket => Áo Phao Xanh
Green Stadium Jacket => Áo Varsity Xanh
Blue Denim Jacket => Áo Jean Xanh
Red Leather Jacket => Áo Da Đỏ
Snakeskin Shirt => Áo Da Rắn
Special Forces Top => Áo Đặc Nhiệm
Black Skull Shirt => Áo Đầu Lâu Đen
Flame Print Shirt => Áo In Họa Tiết Lửa
Punk Shirt => Áo Punk
Magic Time Shirt => Áo Giờ Phép Thuật
Peach Tie-Dye Shirt => Áo Loang Màu Đào
Black Biker Gear Top => Áo Biker Đen
Camo Down Vest => Gile Phao Rằn Ri
Suave Purple Shirt => Sơ Mi Tím Lịch Lãm
Leopard Print Shirt => Áo Da Báo
Nurse Jacket => Áo Y Tá
C-Store Uniform => Đồng Phục Cửa Hàng
Pilot Uniform Top => Áo Phi Công
Attendant Outfit Top => Áo Tiếp Viên
Firefighter Gear Top => Áo Lính Cứu Hỏa
Scientist Coat => Áo Nhà Khoa Học
Racing Suit Top => Áo Đua Xe
Officer Uniform Top => Áo Cảnh Sát
'''))

touched=[]
for number in (1,2,3):
    file=SRC/f'item__ItemName_e.ofs.{number:03}.jsonl'
    data=[json.loads(x) for x in file.read_text().splitlines()]
    for row in data:
        if row['vi'] is not None: continue
        en=row['en']
        if en not in M:raise KeyError(f'Missing item translation {number}: {en!r}')
        vi=unicodedata.normalize('NFC',M[en])
        if row.get('max_utf8_bytes') and len(vi.encode())>row['max_utf8_bytes']:
            raise Exception(f'Too long byte count {en}: {vi}')
        row['vi']=vi
        touched.append({'file':str(file.relative_to(ROOT)),'id':row['id'],'en':en,'vi':vi})
    file.write_text(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n' for x in data),encoding='utf8')
print(f'Added {len(touched)} item records')
(ROOT/'CHANGES-003-ITEMS.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in touched),encoding='utf8')