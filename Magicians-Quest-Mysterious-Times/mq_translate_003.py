#!/usr/bin/env python3
"""Checkpoint 003 hand-authored Vietnamese strings; ONLY modifies JSONL `vi` fields.
Use from its current checkpoint directory. All translations are authored for this batch.
"""
import json, pathlib, re, unicodedata, collections
ROOT=pathlib.Path(__file__).parent
TRANS=ROOT/'translation'
changes=[]

def set_vi(file, fun):
    p=TRANS/file
    data=[json.loads(x) for x in p.read_text(encoding='utf8').splitlines()]
    original=[dict(x) for x in data]
    for x in data:
        result=fun(x)
        if result is not None and x['vi']!=result:
            if x['vi'] is not None and x['vi']!=result and file.as_posix().startswith('03-so-tay'):
                raise ValueError('Overwriting an existing translation: '+x['id'])
            result=unicodedata.normalize('NFC',result)
            x['vi']=result
            changes.append({'file':str(file),'id':x['id'],'en':x['en'],'old':original[data.index(x)]['vi'],'vi':result})
    if data!=original:
        p.write_text(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n' for x in data),encoding='utf8')

def lines(s): return [x.strip() for x in s.strip().splitlines() if x.strip()]

BUG_NAMES=lines('''
bướm trắng bắp cải
bướm phượng
ngài tằm sồi
bướm hoàng đế tím
bướm đêm
bướm cánh xanh
bướm bắt ruồi xanh
chuồn chuồn Akiakane
chuồn chuồn Ginyanma
chuồn chuồn Oniyanma
chuồn chuồn Chotombo
ve sầu nâu lớn
ve sầu Mingming
ve cuối hạ
ve chiều tà
ve Kuroiwa
bọ hung sắc màu
bọ cánh cứng ngọc
bọ xít khiên
bọ xít mặt người
bọ kẹp kìm răng cưa
bọ kẹp kìm núi sâu
bọ kẹp kìm khổng lồ
bọ kẹp kìm hươu cao cổ
bọ tê giác
bọ sừng Caucasus
bọ sừng Hercules
châu chấu di cư
muồm muỗm săn mồi
muồm muỗm
dế mèn
dế chuông
bọ que
bọ ngựa
kiến
gián
rết
bọ xén tóc xanh
rùa tai đỏ
kỳ giông
thằn lằn
ruồi
ong mật
bọ rùa
muỗi
muỗi hạc
phù du
đom đóm
ốc sên
nhện
sâu róm
bọ lá
ngài mặt người
ruồi rết
chuồn chuồn cổ đại
cá trời
chuồn chuồn Dracula
bọ đầu kéo
muồm muỗm mê tiệc
Keseranpasaran đen
Mandragora
Tsuchinoko
Keseranpasaran
Hyoro-Hyoro
''')
FISH_NAMES=lines('''
cá diếc
cá chép
cá chạch
cá chép Koi
cá trê
cá ốtme ao
cá Ayu
cá hồi vua
cá mang xanh
cá vược đen
cá tầm
cá bảy màu
cá neon
cá thần tiên
cá piranha
cá rồng đỏ
cá sấu mõm dài
kỳ giông Axolotl
cá hồi anh đào
cá hồi vân
sa giông
cá sóc
cá tráp
cá nục
cá đục
cá chình biển
cá bò da
cá nóc hổ
cá ngừ
cá mập trắng
cá mập yêu tinh
cá đuối manta
cá nóc hộp đốm xanh
cá hề
tôm càng
ếch
ếch phi tiêu độc
ếch trong suốt
bạch tuộc
mực
sứa
thiên thần biển
cá ngựa
tôm hùm gai
tôm hùm
cá mặt trăng
sam biển
ốc anh vũ
cá vây tay
cá răng nanh
cá mập miệng rộng
cá mái chèo
bọ ba thùy
thằn lằn cá
rùa Archelon
sinh vật Cambri A
sinh vật Cambri B
cá mập đầu búa
mực ma cà rồng
quái vật biển khổng lồ
hộp cá ngừ
miếng sushi
con non Leviathan
cá mặt người
mẩu rác
mẩu rác
chìa khóa cửa
''')
assert len(BUG_NAMES)==64,len(BUG_NAMES)
assert len(FISH_NAMES)==67,len(FISH_NAMES)

# Descriptions keep the meaning while sounding like a natural, sometimes mischievous field guide.
BUG_DESC=lines('''
Bướm trắng, cánh có vài đốm đen xinh xinh.
Bướm to, đuôi cánh nhỏ như hai chiếc nơ.
Ngài trông dữ dằn, nhộng lại bọc tơ mềm.
Bướm lớn, đôi cánh tím đẹp hết chỗ chê.
Bướm đêm nghỉ ngơi là xòe cánh nằm bẹp.
Đôi cánh xanh có hoa văn đẹp mê ly.
Đẹp nức tiếng, nhưng sắp tuyệt chủng rồi.
Chuồn chuồn mê nơi mát mẻ giữa mùa hè.
Chuồn chuồn to, bụng dưới ánh bạc.
Phải mất hai năm mới lớn thành chuồn chuồn.
Chuồn chuồn mà bay cứ như bươm bướm.
Tiếng ve kêu như dầu đang sôi ùng ục.
Ve cất tiếng là biết hè tới rồi!
Cuối mùa hè, tiếng ve này vang khắp nơi.
Tiếng ve báo mặt trời sắp lặn.
Ve xanh bé xíu, lại hiếm gặp nữa.
Bọ cánh bóng loáng, khoái gặm rễ và lá.
Trông cứ như một viên ngọc biết bò.
Bọ xít hôi, dáng lại giống rùa.
Trên lưng có hoa văn như mặt người.
Hàm bọ lởm chởm như lưỡi cưa.
Bọ to, có thể dài tới tận 8 cm.
To xác thế thôi, nhát gan lắm nhé!
Đôi hàm dài cong như gạc hươu.
Được phong danh hiệu Vua Bọ Cánh Cứng.
Bốn chiếc sừng, sức mạnh khỏi bàn!
Đặt tên theo anh hùng Hy Lạp Hercules.
Châu chấu nhảy lóc chóc, tiếng rất lạ.
Muồm muỗm ăn thịt, không hiền đâu nha.
Tiếng kêu rả rích nghe phát bực.
Dế đực có tiếng gáy rất dễ nhận ra.
Tiếng gáy hay đến mức nổi tiếng luôn.
Ngụy trang như cành cây, nhìn kỹ mới thấy.
Chân trước có gai, chuyên chộp con mồi.
Kiến nhỏ mà khỏe, chăm chỉ số một!
Gián đã sống trên Trái Đất từ ngàn xưa.
Rết vừa hung dữ vừa có nọc độc.
Bọ xanh da trời, điểm những đốm đen.
Rùa bé lúc mới nở, lớn lên khá to đấy.
Trông như thằn lằn, thật ra là lưỡng cư.
Bị tóm đuôi là thằn lằn bỏ đuôi chạy!
Ruồi chà hai chân để tự vệ sinh.
Loài ong tạo ra món mật ngọt lịm.
Bọ rùa thích bay về phía ánh nắng.
Muỗi hút máu để nuôi trứng.
Ruồi chân dài ngoằng nhưng vô hại.
Lớn lên chỉ sống vài ngày, ngắn ngủi ghê.
Đom đóm thích sống bên dòng nước sạch.
Ốc sên có vỏ, họ hàng với sên trần.
Nhện có tám chân, chẳng phải côn trùng.
Sâu bướm là ấu trùng của bướm và ngài.
Ngụy trang thành lá cây, quá đỉnh!
Ngài có hoa văn đầu lâu để dọa kẻ thù.
Trông như con rết mọc thêm cánh.
Chuồn chuồn từng bị tưởng đã tuyệt chủng.
Cá trời bay nhanh đến chóng mặt.
Chuồn chuồn có răng nanh sắc như Dracula.
Đầu kéo có hàm và răng bén ngót.
Mải chơi quên ăn, đói meo luôn!
Sinh ra ban đêm, cứ lơ lửng bay quanh.
Cây thuốc quý, đừng nhổ bừa nhé!
Sinh vật huyền thoại, trông tựa rắn.
Sinh vật bông xù rất mê ăn đồ trang điểm.
Nấm gì mà nghe nhạc là lắc lư theo!
Cá thích dòng sông chảy êm đềm.
Cá thân to, ria mép dài thườn thượt.
Cá có ria, thích chui rúc trong bùn.
Cá có ria, đủ màu đủ họa tiết.
Cá nước ngọt có ria, đêm mới hoạt động.
Cá ngon, lại đẻ rất nhiều trứng.
Cá sông ướp muối nướng là hết sảy.
Cá bơi về đúng nơi mình chào đời.
Cá ngon mà màu chẳng xanh hoàn toàn.
Cá ăn được, dân câu cá rất chuộng.
Cá cổ đại nổi tiếng vì món trứng cá muối.
Cá được cưng vì sắc màu rực rỡ.
Cá có những sọc đỏ xanh đẹp mắt.
Cá bơi uyển chuyển như thiên thần.
Cá ăn thịt nhưng lại khá nhát gan.
Cá đỏ, nuốt chửng cá bé trong một phát.
Cá có chiếc mõm dài nhọn hoắt.
Kỳ giông có tay chân bé tí, cưng xỉu!
Cá cảnh giác cao, bắt được chẳng dễ.
Cá toàn thân óng ánh sắc cầu vồng.
Sa giông rụng đuôi, rồi mọc lại được.
Cá mê sống ở vùng nước trong lành.
Cá hay được đãi trong dịp lễ mừng.
Cá lưng sẫm màu, bụng lại nhạt.
Cá ngon, sống ở vùng biển nông.
Cá chình dài, thân mảnh và không vảy.
''')
assert len(BUG_DESC)==90,len(BUG_DESC)

SEA_DESC=lines('''
Cá da nhám, lột da ra khá dễ.
Cá có độc, lại còn đắt đỏ.
Cá ngon, nhà nhà đều mê.
Cá to, răng sắc, bụng lúc nào cũng đói.
Cá mập biển sâu, đầu nhọn hoắt.
Sinh vật biển to lớn, bơi rất duyên dáng.
Sinh vật thân vuông, vỏ ngoài cứng cáp.
Cá sặc sỡ, thân với hải quỳ lắm.
Giáp xác nổi giận là giơ càng lên kẹp.
Ếch cái thường to hơn ếch đực.
Ếch sặc sỡ, đẹp mà có độc đấy!
Con ếch trong veo, nhìn xuyên được luôn.
Sinh vật biển thông minh có tám chân.
Sinh vật mười chân, giỏi phun mực.
Sinh vật biển, chỉ vài loài biết chích.
Sinh vật biển có họ với sên biển.
Sinh vật biển mà con đực lại sinh con!
Tôm hùm đắt tiền, bạch tuộc khoái lắm.
Tôm hùm vừa to vừa ngon miệng.
Cá bơi chậm, đi đâu cũng vụng về.
Con sam dẹt, lột lớp vỏ cứng ngoài.
Sinh vật dùng khí để nổi lên, lặn xuống.
Cá cổ đại, nghe đồn mang lại may mắn.
Cá dữ dùng ánh sáng dụ con mồi.
Cá mập có cái miệng to bất thường.
Cá biển sâu, thân dài và dẹt.
Sinh vật vỏ cứng, hóa thạch sống đấy!
Thú biển giống cá heo nhưng răng to.
Rùa biển cổ đại, to mà lại nhẹ.
Sinh vật biển với đôi mắt lồi.
Sinh vật biển chân dài, gai nhọn.
Cá mập đầu búa, nghe đồn phá được đá!
Sinh vật biển dùng sóng âm để săn.
Quái biển khổng lồ, chuyên tấn công tàu.
Cá da dai, thịt thì ngon.
Có loại sushi đắt tới mức choáng váng.
Con non hung dữ, sợ xô bị ném tới.
Cá bí ẩn, biết đâu từ hành tinh khác!
''')
assert len(SEA_DESC)==38,len(SEA_DESC)

MYSTERY_DESC=lines('''
Khủng long già từ hồ Loch Ness, cổ dài, mê nhạc hay.
Dân sông lấp lánh, rác càng nhiều càng bẩn.
Bôi toàn thân bằng đồ ngọt để ruồi bu đầy!
Chân dung thầy hiệu trưởng cũ, nói dai bất tận...
Ma quý ông hiền khô, nổi giận là rung chuyển đồ đạc.
Sinh vật hiểu chuyện yêu đương, chỉ các cô gái thấy.
Người gác trường mê đố vui, trả lời sai là nổi nóng.
Giả làm rương báu, ai sơ ý sẽ bị cắn ngay!
Thông minh cực, vừa bay vừa phun lửa ầm ầm.
Dân sao Hỏa nói ngược, nghe rối cả đầu!
Bản sao ở thế giới gương, giống hệt mà không phải bạn.
Trăng tròn là hóa sói, rất sợ đồ bằng bạc.
Ma đáng sợ đưa linh hồn sang thế giới bên kia.
Tượng âm thầm bảo vệ trường, chẳng ai thấy nhúc nhích.
Trị kẻ xấu, giúp người tốt; ghét mọi thứ cong queo.
Đầu bò mình người từ Hy Lạp, mở trại tập thể dục.
Quái tinh nghịch, chạy nhanh đến mức khó bắt nổi!
Bóng ma nữ thích để dấu lên tường nơi mình đi qua.
Cậu chàng mê vui, bé người mà khỏe đáng gờm.
Sinh vật tí hon từ đất sạch, cần nước và chăm sóc.
Anh bạn tuyết tròn trịa, cứ nắng lên là sợ tan.
Người bạn phép thuật bé xíu, chỉ mong được học thêm.
Kẻ láu cá từ cõi xa, được triệu hồi bằng đại phép.
Nửa người nửa cá, hát mê hồn mà nói thì lắm!
Nàng cá hát hay đến mức thủy thủ lạc đường.
Quái vật to xác mới năm tuổi, còn gọi là Bigfoot.
Chó gác cõi âm ba đầu, mê những khúc xương to.
Cá sấu mặt dữ mà hiền, đến từ New York xưa.
Sinh vật hang sâu lên mặt đất vì tò mò quá mức.
Cuốn sách biết tuốt, thường ngủ khì trong tháp.
Đầu bí ngô, mỗi năm về một lần để ăn kẹo.
Người sáng lập trường phép, vẫn dõi theo mọi người.
Người vô tội bị cuốn đi; trở về mới thật gian nan.
Quái vật tạo ác mộng, lại ghét chính ác mộng!
Mê ăn ác mộng, cho bao nhiêu cũng xơi sạch.
Cún cô đơn từ cõi khác, mê khoe hơi thở lửa.
Trùm ma dùng đàn em hù trẻ con thức khuya.
Kẻ lãng du mê nhạc, tóc dài mà nhất quyết không gội.
Sinh vật nhỏ xíu, ai tin vào chúng sẽ thấy.
Người phát quà lễ hội cho những ai ngoan ngoãn.
Vật thể lạ xuất hiện khi bạn gửi lòng vào âm nhạc.
Chớp mắt đã biến mất, đến gần dễ bị ngáng chân!
Hoa văn lạ trên mặt đất, nghi nhất là người ngoài hành tinh.
Hiệp sĩ rời đầu; đầu với thân hay cãi nhưng vẫn thân.
Sư tử khổng lồ ham ăn, chẳng biết điểm dừng!
Nửa sư tử nửa đại bàng, giữ kho báu rất nghiêm.
Sinh vật chăm làm, mê nhạc, ít nói nên hay bị hiểu lầm.
Cô bé bán diêm can đảm, nay sống với bà yêu quý.
Quái biển giống mực khổng lồ, vụng về mà tốt bụng.
Người đất từ phép mạnh; mỗi năm có hội thi làm golem.
Sống ở sông sạch, thích trêu người và thách vật tay.
Người xanh bé tí mê đố vui, giống nhau mà chẳng quen.
''')
assert len(MYSTERY_DESC)==52,len(MYSTERY_DESC)

LABELS={
'52.10':'Tí hon','52.11':'Nhỏ','52.12':'Vừa','52.13':'Khá lớn','52.14':'Lớn','52.15':'Rất lớn','52.16':'Khổng lồ','52.17':'Huyền thoại','52.18':'Chìa khóa cũ',
'52.20':'Tí hon','52.21':'Nhỏ','52.22':'Vừa','52.23':'Khá lớn','52.24':'Lớn','52.25':'Rất lớn','52.26':'Khổng lồ','52.27':'Huyền thoại',
'61.40':'Ghi nhận','61.41':'Chiều dài','61.42':'Mùa xuân','61.43':'Mùa hè','61.44':'Thu/Đông','61.45':'Đồng cỏ','61.46':'Rừng cây','61.47':'Hang động','61.48':'Bãi biển','61.49':'Hòn đảo','61.50':'Ký túc xá','61.51':'Rừng Nấm','61.52':'Biển','61.53':'Sông','61.54':'Ao','61.55':'Hang động',
'61.58':'cm','61.59':'m','61.80':'Chuông','61.81':'Đô','61.83':'Rê','61.85':'Mi','61.86':'Fa','61.88':'Sol','61.90':'La','61.92':'Si','61.93':'Đô','61.95':'Rê','61.96':'OK',
'62.60':'Vụ đã phá','62.61':'Người giải:','62.63':'Chân dung','62.64':'Hiệu trưởng đầu tiên'}

MANUAL={
'52.0':'Dây câu đứt rồi!▼Cá đang sung thì cứ▼bình tĩnh, chớ nóng vội.',
'52.1':'Cá chuồn mất rồi!▼Kéo cần trước khi▼cá hết hứng nhé.',
}

def wrap_display(s,maxwidth=147,max_lines=3):
    # Use a conservative 11px DejaVu Sans proxy; ROM uses its own 9x16 bitmap font.
    from PIL import ImageFont
    font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',11)
    if '▼' in s: return s
    words=s.split(' ')
    if len(words)==1:return s
    out=[];current=''
    for word in words:
        candidate=(current+' '+word).strip()
        if current and font.getlength(candidate)>maxwidth:
            out.append(current);current=word
        else:current=candidate
    if current:out.append(current)
    if len(out)>max_lines:
        # Fallback to shorter lines? This is a quality gate, not an automatic truncation.
        raise ValueError(f'Too many NDS lines ({len(out)}): {s!r}')
    return '▼'.join(out)

def book_translation(row):
    if row['vi'] is not None: return None
    m=re.search(r'#(\d+)\.(\d+)#page:',row['id']); assert m,row['id']
    sect,sub=map(int,m.groups());key=f'{sect}.{sub}'
    text=None
    if sect==50:
        text=f'Bắt được {BUG_NAMES[sub]}!'
    elif sect==51:
        text=f'Câu trúng {FISH_NAMES[sub]}!' if sub<=66 else None
        if sub in (60,61,64,65):text=f'Câu lên {FISH_NAMES[sub]}!'
    elif sect==60:
        if 0<=sub<64:text=BUG_DESC[sub]
        elif 70<=sub<=95:text=BUG_DESC[sub-70+64]
        elif 96<=sub<=99:text=SEA_DESC[sub-96]
    elif sect==61 and sub<=33:text=SEA_DESC[sub+4]
    elif sect==62 and 0<=sub<=51:text=MYSTERY_DESC[sub]
    if key in MANUAL:text=MANUAL[key]
    if key in LABELS:text=LABELS[key]
    if text is None:raise KeyError((row['id'],row['en']))
    if sect==50 or sect==51:return wrap_display(text,maxwidth=148,max_lines=3)
    if sect in (60,61,62) and key not in LABELS:return wrap_display(text,maxwidth=150,max_lines=3)
    return text

for f in sorted((TRANS/'03-so-tay').glob('talkfigs*.jsonl')):
    set_vi(f.relative_to(TRANS),book_translation)

# Keep the user's explicitly approved young playful register, without breaking narrator -> pupil address.
OPENING={
'120.18#page:1':'Em siêng khỏi bàn,▼làm gì cũng ngay thẳng!',
'120.19#page:1':'Đầu em đầy ý tưởng,▼sáng tạo không chịu nổi!',
'120.20#page:1':'Em tốt bụng quá,▼ai nhờ cũng gật đầu!',
'120.21#page:1':'Em sinh ra là để▼làm đầu tàu cả hội!',
'120.22#page:1':'Em nói là làm,▼trách nhiệm khỏi bàn!',
'120.23#page:1':'Đi đâu em cũng có hội,▼kết bạn như cơm bữa!',
'120.24#page:1':'Em nhạy cảm ghê,▼chuyện gì cũng để tâm!',
'120.25#page:1':'Em mê tụ tập,▼quẩy banh nóc với bạn bè!',
'120.26#page:1':'Em chăm học, kỹ tính▼đến từng dấu chấm!',
'120.27#page:1':'Em điềm tĩnh, lịch sự,▼chuẩn con nhà người ta!',
'120.28#page:1':'Em tò mò số một,▼chuyện gì cũng muốn hóng!',
'120.29#page:1':'Em lanh trí khỏi bàn,▼gặp khó cũng xoay được!'}

def opening(row):
    if row['vi'] is None:return None
    m=re.search(r'#([\d.]+#page:\d+)$',row['id'])
    if m:return OPENING.get(m.group(1))
set_vi(pathlib.Path('00-mo-dau/talkfigs__0eng__data__0999.001.jsonl'),opening)

# Item translations will be added next; preserve original names in a reversible list.
itemfile=pathlib.Path('02-vat-pham/item__ItemName_e.ofs.001.jsonl')
print('Modified',len(changes),'translation fields')
(ROOT/'CHANGES-003.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in changes),encoding='utf8')