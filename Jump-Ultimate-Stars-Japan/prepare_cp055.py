#!/usr/bin/env python3
"""CP055 human-authored VN blocks, split over original piece.bin segments without altering source ID order."""
import json, re, math, unicodedata
from pathlib import Path
ROOT=Path(__file__).resolve().parent
blocks={
(0,3): "— mang lời chúc: 'Hãy trở thành vua của nông trại Midori!' Cái tên ấy rồi sẽ được khắc vào lịch sử đua ngựa Nhật Bản với biệt danh 'Phép màu trắng'...!",
(6,23): "Đây là câu chuyện pha màu kinh dị về Muhyo, một Chấp hành viên của giới Ma luật chuyên xét xử tội ác do linh hồn gây ra, và Roji, cậu trợ lý hơi hậu đậu. Văn phòng Ma luật Rokuhyo là nơi những ai khổ sở vì hiện tượng tâm linh tìm đến cầu cứu. Cơ quan mới thành lập này ra đời để ngăn tội phạm do hồn ma gây ra, vốn ngày càng nhiều. Toru Rokuhyo (Muhyo) là thần đồng trẻ nhất đạt tới chức Chấp hành viên, cấp bậc cao nhất của Ma luật gia. Sát cánh cùng cậu là Jiro Kusano (Roji), trợ lý chẳng mấy đáng tin. Ngày nào cũng có khách tìm tới bộ đôi trái tính này: người mong cứu bạn hóa ác linh, người nhờ trừ hồn ma ám ký túc xá. Qua bao vụ việc, bóng dáng Enchu, bạn cũ nay thành kẻ phản bội của Muhyo, dần lộ diện. Cuối cùng Muhyo và Roji bị cuốn vào cuộc đại chiến giữa các Ma luật gia và phe Cấm Ma luật đã nổi loạn!",
(27,44): "Một câu chuyện đấu bài nơi chàng học sinh trầm tính Yugi Muto bị cuốn vào cuộc chiến ánh sáng và bóng tối kéo dài 3.000 năm sau khi giải được Millennium Puzzle, bảo vật bóng tối từ Ai Cập cổ đại. Yugi thuộc kiểu học sinh hay bị bắt nạt: giờ nghỉ trưa, thay vì ra sân thể thao như mọi người, cậu chỉ thích ngồi một mình trong lớp chơi game. Nhưng từ khi giải chiếc Millennium Puzzle ông nội tặng, đời cậu đảo lộn. Một Yugi khác thức tỉnh trong cậu, kế thừa những Shadow Game và trừng trị cái ác như một người bảo vệ công lý. Yugi thứ hai ấy rốt cuộc là ai? Bí mật của Millennium Items là gì? Trưởng thành qua vô số trận Duel với các đối thủ, Yugi quyết tìm lời giải về con người còn lại trong mình. Và phía sau tất cả là mối duyên nợ với Seto Kaiba kéo dài từ tận Ai Cập cổ đại.",
(47,64): "Yusuke Urameshi là tay quậy số một trường Sarayashiki, mê đánh nhau hơn ăn cơm. Câu chuyện theo chân cậu và bạn bè qua những số phận kỳ lạ. Một ngày, Yusuke lao ra đường cứu một đứa trẻ rồi bị xe đâm chết. Nhưng cái chết ấy nằm ngoài dự tính của Spirit World, nên cậu có cơ hội làm thử thách để sống lại. Sau khi vượt những phép thử của cõi linh hồn và trở về thế giới người sống, Yusuke trở thành Spirit Detective, đấu với đủ loại tội phạm từ linh giới. Cậu khiến đám yêu quái phải kiêng dè, đồng thời biến mình thành mục tiêu của những kẻ muốn nổi danh bằng cách hạ gục cậu. Được mời tới Dark Tournament, Yusuke phải đối đầu Toguro với sức mạnh áp đảo và hàng loạt địch thủ đáng gờm: muốn sống chỉ còn cách chiến thắng. Tiếp đó, cuộc chiến vì đường hầm nối Nhân giới với Ma giới đẩy cả nhóm tới Demon World, nơi cán cân các thế lực đang sụp đổ. Chuyện của Yusuke và đồng đội sẽ kết thúc ra sao?",
(67,84): "Lấy bối cảnh Nhật Bản đầu thời Minh Trị, thiên truyện kiếm hiệp lãng mạn theo chân Kenshin Himura, kiếm sĩ mang lời thề không giết người, và các đồng đội. Tự xưng là lãng khách, Kenshin từng khiến Kyoto thời Mạc mạt khiếp sợ dưới biệt danh Hitokiri Battosai. Khi thời đại mới đến, anh chọn dùng kiếm cứu người thay vì sát sinh. Chính niềm tin và nhân cách ấy lôi cuốn bạn hữu đến bên Kenshin, nhưng cũng kéo theo vô số kẻ thù muốn hạ anh để xưng bá thiên hạ. Khi phải ngăn âm mưu lật đổ chính quyền của Makoto Shishio, Kenshin quyết chiến đấu một mình để không liên lụy đồng đội. Thế nhưng, bạn bè vẫn đuổi theo anh, đặc biệt là tấm lòng chân thành của Kaoru Kamiya khiến anh thay đổi: anh phải sống vì những người mình yêu quý. Cũng chính ý chí sống ấy là chìa khóa lĩnh ngộ tuyệt kỹ tối thượng Hiten Mitsurugi-ryu. Với thanh Sakabato trong tay, Kenshin chiến đấu để được sống!",
(88,105): "Taison Maeda, học sinh trường Teiken, đánh nhau thì cừ mà học hành thì... thôi khỏi nói. Giấc mơ của cậu là trở thành vô địch boxing thế giới, nhưng quanh cậu lúc nào cũng đầy chuyện gây gổ. Qua những trận đấu với Shimabukuro của trường Yonekura Thương mại và Akagi của trường Kyoei, Taison dần nổi danh. Sau đó, cùng Onizuka của Rakusui ở Shibuya, Yakushiji của Sasazuka ở Asakusa và Kasai của Seidokan ở Ikebukuro, cậu được gọi là một trong 'Tứ Thiên Vương Tokyo'. Dẫu vậy, Taison không đánh nhau để khoe sức mạnh. Cậu chiến đấu đơn giản vì chẳng bao giờ muốn thua bất kỳ ai. Đôi lúc, nhìn Hatanaka và Harada, bạn cùng trường Teiken, lần lượt bước vào sự nghiệp boxing, Taison cũng thấy sốt ruột. Nhưng ai cũng có con đường của riêng mình. Cậu quyết tiếp tục vui buồn cùng đám bạn trong những năm trung học; kinh nghiệm từ những trận chiến tại Teiken rồi sẽ trở thành hành trang quý giá khi cậu thực sự lên võ đài boxing.",
(108,118): "Cậu bé Luffy ăn Gomu Gomu no Mi, một Devil Fruit, để rồi có cơ thể cao su. Sau đó cậu ra khơi làm hải tặc, cùng hội bạn tốt bụng đi khắp thế giới trong cuộc phiêu lưu biển cả. Kho báu, danh vọng, quyền lực — Gol D. Roger, người từng nắm cả thế giới và được gọi là Pirate King, đã để lại đại kho báu One Piece. Từ đó, ai nấy đều ra khơi săn kho báu, mở ra Kỷ nguyên Đại Hải Tặc. Tại một thị trấn cảng nhỏ, cũng có cậu nhóc ôm giấc mơ trở thành Pirate King! Thuở bé, Luffy từng lập lời hứa với đại hải tặc Shanks Tóc Đỏ:",
(122,125): "bắt đầu cuộc phiêu lưu vĩ đại! Grand Line đầy rẫy hiểm nguy, rồi những chuyến đi lên Sky Island huyền thoại! Dù phải đối đầu Chính phủ Thế giới, hành trình của Straw Hat Pirates vẫn cứ tiếp diễn!!!",
}
fixed={
4:'Yoshiyuki Nishi', 5:'Từ số 53 năm 2004',
24:'Kazuki Takahashi',25:'Từ số 42 năm 1996',26:'Đến số 15 năm 2004',
45:'Từ số 51 năm 1990',46:'Đến số 32 năm 1994',
65:'Từ số 19 năm 1994',66:'Đến số 43 năm 1999',
85:'Masanori Morita',86:'Từ số 25 năm 1988',87:'Đến số 10 năm 1997',
106:'Eiichiro Oda',107:'Từ số 34 năm 1997',
119:'“Một ngày nào đó<IDEOSP>tớ sẽ có đồng đội không thua băng này!!',
120:'<IDEOSP>Kiếm kho báu lớn nhất thế giới!!!<IDEOSP>Và trở thành',
121:'Pirate King!!!” Mười năm sau, Luffy',
126:'Ngôi sao mới nổi',127:'Genin cuồng phong',128:'Chunin lốc xoáy',129:'Jonin bão tố',130:'Ninja bóng tối nhanh như gió',
131:'Trung đội tia chớp',132:'Sư đoàn sấm sét',133:'Lữ đoàn lôi kích',134:'Quân đoàn chim sấm',
135:'Hiệp đạo',136:'Siêu đạo chích',137:'Treasure Hunter',138:'Siêu trộm múa trong đêm',
139:'Thần đồng cô độc',140:'Tài nhân kiêu hãnh',141:'Kỳ nhân cô độc giữa đời',142:'Đại hào kiệt hồn nhiên',
143:'Võ sĩ',144:'Võ sĩ quyền cương mãnh',145:'Cao thủ Thần Quyền',146:'Võ thần huyền thoại còn sống',
147:'Quái nhân trong lời đồn',148:'Ma nhân bí ẩn',149:'Ma vương huyền bí',150:'Đại ma vương thâm sâu',
151:'Kẻ làm chủ đường thẳng',152:'Kẻ thao túng mặt phẳng',153:'Kẻ xé toạc không gian',154:'Kẻ vượt mọi thời không',
155:'Tay chơi tùy hứng',156:'Lãng khách nổi danh',157:'Cánh chim phiêu bạt',158:'Kẻ lãng du theo gió',
159:'Chojin dẻo dai',160:'Chojin bất khuất',161:'Chojin bất tử',162:'Chojin huyền thoại lúc nguy nan',
163:'Người tài đích thực',164:'Thiên tài hiếm có',165:'Hiền nhân vĩ đại',166:'Đại hiền giả thông suốt thế gian',
167:'Ora!',168:'Ora ora!',169:'Ora ora ora!',170:'ORA ORA ORA!!',
171:'Hiệp sĩ tập sự',172:'Hiệp sĩ Đồng',173:'Thánh Kỵ Sĩ Bạc',174:'Thánh Kỵ Sĩ Vàng được chọn',
175:'Tay lão luyện',176:'Ra đòn điêu luyện',177:'Bậc cao thủ uyển chuyển',178:'Mưa phùn đêm tối không dứt',
179:'Thị trưởng độc ác',180:'Quốc vương độc ác',181:'Bạo chúa thống trị Trái Đất',182:'Đế vương tà ác khắp vũ trụ',
183:'Ngôi sao của lớp',184:'Siêu sao',185:'Đại minh tinh quốc dân',186:'Ultimate Star',
187:'Hoàng tử',188:'Hoàng tử hoa hồng',189:'Đại quân vương khiêu vũ thanh tao',190:'Thánh đế tung cánh khắp trời',
191:'Dũng sĩ',192:'Dũng sĩ dày dạn trận mạc',193:'Dũng sĩ mạnh nhất',194:'Vua dũng sĩ huyền thoại',
195:'Kiếm sĩ nhanh như chớp mắt',196:'Kiếm khách chớp sáng',197:'Kiếm hào sao băng',198:'Kiếm thánh rực sáng như sao chổi',
199:'Người Trái Đất',200:'Siêu người Trái Đất',201:'Siêu người Trái Đất 3',202:'Người Trái Đất vượt giới hạn',
203:'Anh hùng',204:'Anh hùng vang danh',205:'Anh hùng vô địch',206:'Vua anh hùng lưu danh muôn đời',
207:'Solo 1',208:'Solo 2',209:'Solo 3',210:'Solo 4',211:'Solo 5',212:'Solo 6',213:'Solo 7',214:'Solo 8',
215:'Đấu trường',216:'Tournament Mountain',217:'Đồn cảnh sát Kameari giữa trời tuyết',218:'Đấu trường số 3 trên đảo Meiho',
219:'Mười hai cung hoàng đạo giữa vũ trụ',220:'Hành tinh Namek và Porunga',221:'Heavens Arena',
222:'Soul Society và thế giới Zanpakuto',223:'Bắc Đẩu Thất Tinh trên hoang mạc',224:'Vương quốc Tóc mới',225:'Davy Back Fight',
226:'Thiên nhiên',227:'Thành phố',228:'Trường học',229:'Vũ trụ',230:'Thế giới đang sụp đổ',
231:'Lễ hội Ransen',232:'Nhà Tsuna',233:'Great Spirits',234:'DIO\'s Mansion',235:'Nhà thể chất trường Shohoku',
236:'Thế giới Shinigami',237:'Sân tennis Arena',238:'Nhà Senbei',239:'Cây sáo khổng lồ',
240:'Căn cứ L.X.E.',241:'Biệt thự thế giới méo mó',242:'Cổng Minh Giới',243:'Sân đấu Dark Tournament',
244:'Đạo trường Kamiya',245:'Chấn động',246:'Sụp đổ',247:'Khác',
}

def wrap_exact(text,n):
    words=text.split(' ')
    if len(words)<n:raise ValueError('Not enough words')
    out=[];i=0
    for j in range(n):
        remaining=n-j-1
        remaining_text=' '.join(words[i:]);remaining_char=len(remaining_text)
        ideal=remaining_char/(remaining+1)
        min_end=i+1;max_end=len(words)-remaining
        candidates=[]
        for e in range(min_end,max_end+1):
            frag=' '.join(words[i:e]);length=len(frag)
            if length>max(90,ideal*2):break
            boundary = frag.endswith(('.', '?', '!', ':', ';'))
            score=abs(length-ideal) - (1.4 if boundary else 0)
            candidates.append((score,e))
        if not candidates: raise ValueError('bad wrapping '+str(j))
        e=min(candidates)[1]
        out.append(' '.join(words[i:e]));i=e
    assert i==len(words),(i,len(words))
    return out

for (start,end),text in blocks.items():
    vals=wrap_exact(text,end-start+1)
    for off,val in enumerate(vals):
        assert start+off not in fixed
        fixed[start+off]=val

assert set(fixed)==set(range(248)),sorted(set(range(248))-set(fixed))
source=[json.loads(x) for x in (ROOT.parent/'JUS_CP054'/'NGUON_CHUA_DICH_SAU_054.jsonl').read_text().splitlines()]
for x in source:
 i=x['row_index'];v=fixed[i]
 if unicodedata.normalize('NFC',v)!=v:fixed[i]=unicodedata.normalize('NFC',v)
 assert v.strip(),i
 assert len(re.findall(r'<[A-Z_]+>',v))==len(re.findall(r'<[A-Z_]+>',x['ja'])), (i,x['ja'],v)
 assert '<IDEOSP>' in x['ja'] or '<IDEOSP>' not in v
(ROOT/'draft_055.tsv').write_text(''.join(f'{i}\t{fixed[i]}\n' for i in range(248)),encoding='utf8')
print('Wrote',len(fixed),'chunks')
for x in source:
 i=x['row_index'];print(f'{i:03} ({len(fixed[i]):2}): {fixed[i]}')
