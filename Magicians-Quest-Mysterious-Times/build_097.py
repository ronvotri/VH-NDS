#!/usr/bin/env python3
"""Build Magician's Quest checkpoint 097 from 096 without rewriting older content.
All manual translation strings are embedded below; only checkpoint 096 ZIP is needed.
This is a source-data checkpoint, not a tested ROM patch.
"""
import collections
import hashlib
import json
import re
import unicodedata
import zipfile
from pathlib import Path

ROOT = Path('/mnt/data')
PREV = ROOT / 'MagiciansQuest-VietHoa-Checkpoint-096.zip'
OUT = ROOT / 'MagiciansQuest-VietHoa-Checkpoint-097.zip'
STAGE = ROOT / 'MQ097/stage'
STAGE.mkdir(parents=True, exist_ok=True)
OLD = 'MagiciansQuest_096/'
NEW = 'MagiciansQuest_097/'
TALK = 'translation/04-thoai/talkfigs__0eng__data__'
TARGETS = ['0044.001', '0044.002']
NEXT = ['0044.003', '0044.004']
LEAD = re.compile(r"^(?:\$(?:024|023|022|034|040|004)(?:'[-\d]+)*;)+")
TOKEN = re.compile(r"\$\d{3}(?:'[-\d]+)*;")

# Index is first occurrence of stripped English body among the 240 target pages.
MANUAL = {1: 'Này! Đừng đẩy nữa!▼Đau đấy...$079;', 2: 'Cậu cố tình à?▼Định bắt nạt tớ sao?$079;', 3: 'Chọc phá bạn bè▼vui đến thế sao?!$079;', 4: 'Hả? Ô! Có phải thứ▼tớ đang nghĩ không nhỉ?', 5: 'Tớ mê mấy thứ này lắm!', 6: 'Cậu tặng cho tớ thật à?!▼Thật không đấy?', 7: 'Không ngờ tớ lại được tặng!▼Cảm ơn cậu nhiều lắm!▼Tớ vui quá đi!', 8: 'Cái này để làm gì thế?', 9: 'Hả? Cậu cho tớ à?▼Ồ...', 10: 'Cảm ơn... Tớ sẽ... ừm...▼cất nó đi vậy...', 11: 'Hả? Tặng tớ thật sao?▼Oa! Cảm ơn! Tớ vui quá!', 12: 'Cậu muốn làm gì vậy?', 13: 'Ơ? Cậu còn mất công▼mang thuốc đến cho tớ sao?', 14: 'Tớ đâu định khiến cậu▼phải lo lắng thế này.', 15: 'Nhưng cảm ơn nhé.▼Lát nữa tớ sẽ uống.', 16: 'Cảm ơn cậu!▼Cậu mang thuốc đến rồi!', 17: 'Cứu tinh của tớ đây rồi!▼Tớ mệt đến mức chẳng▼đi mua nổi nữa.', 18: 'Lại thuốc nữa à?▼Lần trước cậu cho▼tớ đủ rồi mà.', 19: 'Cậu không biết uống▼quá nhiều thuốc▼còn mệt hơn sao?', 20: 'Dù sao tớ cũng▼cảm ơn lòng tốt của cậu.', 21: 'Ôi, tớ thấy khó chịu quá...', 22: 'Hả? Quà à?', 23: 'Nhưng tớ ốm thế này,▼cảm ơn cũng chẳng▼ra hơi nữa...', 24: 'Tớ rất cảm kích,▼nhưng giờ chưa nhận được.▼Xin lỗi nhé.', 25: 'Tớ đang làm giấy tờ▼chuyển trường đây.', 26: 'Cậu quyết định ở lại à,▼$500;?', 27: 'Tớ cũng quyết định▼không đi nữa.', 28: "Cho tớ chuyển trường▼cùng cậu nhé.$019'103;", 31: 'Vậy là xong xuôi rồi,▼chúng mình đi thôi.', 32: 'Tiếc thật đấy.▼Lần sau cho tớ▼đi cùng nhé.', 33: 'Ừm... chúc mừng▼sinh nhật nhé, $500;!', 34: 'Tớ có món này cho cậu.▼Thấy nó là tớ nhớ đến cậu.▼Mong cậu thích nhé!', 35: 'Có người bạn như cậu▼thật là may mắn!▼Chúc cậu một ngày tuyệt vời!', 36: 'Chà, tớ không ngờ đấy!', 37: 'Cậu còn nhớ sinh nhật tớ!▼Chuyện này đáng▼ăn mừng đấy chứ!', 38: 'Cảm ơn nhé, $500;!', 39: 'Cảm ơn cậu đã mời tớ.', 40: 'Tớ háo hức xem▼phòng cậu lắm đấy.', 41: 'Không muốn chê đâu,▼nhưng mà... ừm...▼phòng bừa bộn quá.', 42: 'Đơn giản thì tốt,▼nhưng cũng phải▼có giới hạn chứ...', 43: 'Ừ, căn phòng khá bình thường.▼Nhưng tớ thấy cũng thư thái.', 44: 'Oa, phòng đẹp ghê!▼Tớ chịu, chẳng trang trí▼được như cậu đâu!', 45: 'Căn phòng tuyệt thật!▼Cả đời tớ chưa từng▼thấy phòng nào như thế!', 46: 'Không ngờ cậu thích▼màu này, $500;.▼Nó... khá táo bạo đấy.', 47: 'Thú vị thật, cậu có▼nguyên bộ nội thất▼cùng một phong cách!', 48: 'Đồ đạc đồng bộ thế này▼tạo ra bầu không khí▼rất riêng đấy.', 49: 'Cậu có nhiều món giống nhau.▼Ít đa dạng mà lại▼thú vị thật.', 50: 'Tớ cũng muốn thử▼tạo ra một nơi▼như thế này.', 51: 'Cảm ơn vì đã cho tớ▼một tấm gương hay nhé.', 52: 'Cảm ơn nhiều! Thú vị lắm.▼Khi nào muốn, cứ mời▼tớ sang chơi nhé!', 53: 'Đã đến đây rồi,▼uống trà một chút nhé.', 54: 'Không muốn chê đâu,▼nhưng tớ thích uống trà▼ở nơi hợp hơn cơ.', 55: 'Vẫn thiếu gì đó...▼Không khí này▼chưa đủ tuyệt...', 56: 'Trà ngon thật đấy!▼Có vẻ cậu đang▼thư giãn rồi.', 57: 'Thư giãn như thế này▼thật dễ chịu.▼Miễn trà ngon là được!', 58: 'Tách trà thơm, lòng thư thái...▼Tiệc trà đúng là▼dễ chịu thật.', 59: 'Ăn chút gì cùng trà▼khiến hương vị ngon hơn.▼Tớ thích lắm!', 60: 'Lần sau mở tiệc trà,▼nhớ mời tớ nhé.▼Tớ mong lắm đấy!', 61: 'Cuối cùng cũng tới nơi.', 62: 'Cậu có thích món này▼không, $500;?', 63: 'Người quen vừa cho tớ▼món này. Cậu lấy đi.', 64: 'Tớ chẳng còn chỗ▼để cất nó nữa.', 65: 'Nếu cậu chịu nhận,▼tớ sẽ đỡ khổ lắm!', 66: 'Dạo này cậu sao rồi, $500;?▼Lâu quá không gặp.', 67: 'Tớ cứ lo cậu▼gặp chuyện gì.▼Mãi chẳng thấy đâu.', 68: 'Cậu không quên tớ đấy chứ?▼Tớ hay bị người ta▼quên mất lắm...', 69: 'Thấy cậu khỏe là tớ yên tâm!▼Giữ gìn sức khỏe nhé.▼Hẹn gặp lại!', 70: '$500;! Giờ cậu rảnh không?', 71: 'Tớ đang định ra ngoài chơi.▼Cậu đi cùng nhé?', 72: "Được đấy!$019'-1;", 74: 'Hay quá! Đi đâu nhỉ?▼Cậu chọn chỗ đi!', 75: 'Ừ, tớ hiểu mà.▼Tớ rủ hơi đột ngột.▼Để lần khác nhé!', 76: 'Tớ muốn hỏi cậu một chuyện...', 77: "$000'4;$507'663;$000'1; dùng để▼niệm $000'4;phép Hoa Bí Ẩn$000'1;,▼đúng không?", 81: 'Thần chú thú vị thật,▼nhưng tớ niệm mãi▼chẳng ra hồn...', 82: 'Thôi, cảm ơn cậu nhé.▼Gặp lại sau!', 83: 'Tớ nhầm à?▼Giờ càng rối hơn rồi.', 84: 'Hay là tớ tạm▼nghỉ học một chút nhỉ...', 85: 'Sao nào? Tớ không chắc▼cậu có thích không,▼nhưng mong là có!', 86: '$500; đấy à?▼Tớ giúp gì được cho cậu?', 87: 'Cậu nghe tớ huýt sáo à?▼Xin lỗi nhé.', 88: 'Tự dưng tớ nổi hứng thôi.', 89: 'Biết có người nghe,▼tớ thấy ngượng quá...', 90: 'Nếu biết giai điệu ấy,▼cậu cũng muốn huýt sáo thôi.▼Muốn tớ dạy không?', 91: "Ừ, dạy tớ nhé.$019'-1;", 92: "Cảm ơn, nhưng thôi.$018'2;", 93: 'Tốt! Giờ nghe cho kỹ nhé.', 94: 'Tiếc quá. Nếu đổi ý,▼cứ bảo tớ nhé.▼Vui lắm đấy!', 95: 'Ồ, chào $500;.▼Tớ giúp gì được cho cậu?', 96: 'Rung lắc ấy hả?▼Tớ niệm thần chú▼sai mất rồi.', 97: 'Tớ không chắc, nhưng▼hình như sai ngay▼từ khâu chuẩn bị...', 98: "$000'4;Phép Sét$000'1; phải▼dùng những thứ▼sau đây, đúng không...?", 99: 'Ra thế... Vậy thì▼tớ chẳng hiểu mình▼sai ở đâu nữa.', 100: 'Xin lỗi vì đã làm phiền▼cậu nhé, $500;.', 101: 'À... Nếu thế thì▼không ra kết quả▼như ý cũng phải thôi.', 102: 'Có lẽ lần sau tớ nên▼nhờ thầy cô đứng xem.', 103: 'Á á...!', 104: '$500;...? Cậu...▼cậu đến thật rồi.', 105: 'Tớ gặp ác mộng,▼giờ chẳng ngủ được.', 107: "Tớ hiểu rồi.$019'-1;", 109: 'Hừm... Sao tớ lại sợ▼một thứ vô hại thế nhỉ?', 110: 'Nghĩ lại thì▼đâu có đáng sợ lắm.', 111: 'Xin lỗi đã để cậu▼thấy tớ thế này.▼Ngượng thật... Cảm ơn nhé.', 112: 'Dù sao tớ cũng muốn học,▼đêm nay thức luôn vậy.', 114: 'Tớ định làm bài,▼nhưng phòng bừa quá nên▼đành dọn trước.', 115: 'Dọn mãi chẳng xong.▼Sao mà lắm việc thế nhỉ...', 116: 'Tớ không làm phiền▼cậu đấy chứ?', 119: 'Đáng ra tớ nên▼làm xong bài trước,▼để mai dọn phòng.', 120: 'Đúng là sai lầm...', 121: 'Cảm ơn cậu, $500;.', 122: 'Giờ này không phải lúc▼làm chuyện đó nhỉ...', 123: 'Xin lỗi vì đã▼làm phiền cậu.', 124: '$500;? Cậu nghe thấy▼tiếng đó không?', 125: 'Xin lỗi, hóa ra tớ▼hiểu nhầm ngớ ngẩn thôi.', 126: "Tớ cứ tưởng đó là▼$000'4;$507'2146;$000'1;,▼ai dè chỉ tưởng tượng.", 127: 'Cảm ơn cậu đã lo cho tớ,▼$500;. Tớ thấy▼yên tâm hơn rồi.', 128: 'Chào buổi sáng, $500;!▼Hôm nay cậu cần gì?', 129: 'Chuông báo thức của tớ▼làm cậu tỉnh à?', 130: 'Xin lỗi, tớ quên tắt nó.▼Từ nay tớ sẽ cẩn thận hơn.', 131: 'Đã tới đây rồi thì▼cùng học nào!', 132: 'Chính xác!', 133: 'Không, không. Sai rồi.', 134: 'Tớ sẽ hỏi vài câu,▼cậu cứ trả lời▼hết sức mình nhé.', 135: 'Sẵn sàng chưa?▼Câu đầu tiên...', 136: 'Được rồi. Câu tiếp theo!', 137: 'Xong rồi đấy.▼Để xem cậu▼làm được bao nhiêu nhé.', 138: 'Tuyệt quá, $500;!▼Cậu trả lời đúng hết!', 139: "Cậu đúng $550'78; câu.▼Cũng khá đấy.", 140: 'Nghe tớ này, $500;.▼Cậu nên học hành▼nghiêm túc hơn đi.', 141: 'Cậu tiến bộ nhiều rồi.▼Muốn học thêm thì▼cứ tìm tớ nhé.', 142: 'Tớ kể cậu nghe▼một chuyện được không?', 143: 'Thật ra...▼tớ sắp chuyển trường.', 144: "Tớ hơi lo khi đến▼nơi mới. Chúc tớ▼may mắn nhé?$019'601;", 147: 'Cậu đang buồn▼đến thế sao?', 148: 'Cảm ơn. Tình cảm của cậu▼tiếp thêm can đảm▼cho tớ, $500;.', 149: 'Có lẽ tớ phải suy nghĩ▼lại về tương lai.▼Đừng buồn vội nhé.', 150: 'Cảm ơn nhiều lắm!▼Cậu là người bạn▼rất tốt, $500;!', 151: 'Tớ sẽ không bao giờ▼quên cậu đâu!', 152: 'Chúc cậu mọi điều tốt đẹp!▼Tạm biệt, bạn của tớ!', 153: 'Xin lỗi vì mọi chuyện▼đến quá đột ngột.▼Lẽ ra tớ nên nói sớm.', 154: 'Mong tình bạn này▼mãi bền lâu!▼Tạm biệt, giữ gìn nhé!', 155: 'Cậu sẽ nhớ tớ sao?', 156: 'Cảm ơn cậu, nhưng▼tớ buộc phải rời▼thị trấn này.', 157: 'Tớ muốn khám phá▼thế giới và▼mở mang kiến thức.', 158: 'Tớ vui vì cậu muốn tớ ở lại.▼Tớ sẽ chẳng quên cậu đâu.', 159: "Tớ tên là $503'562;,▼từ nay sẽ học▼cùng mọi người.", 160: 'Nếu gặp khó trong học tập,▼cứ đến hỏi tớ nhé.', 161: '$500;! Vào đi!▼Hôm nay cậu có▼món nào hay ho không?', 162: "Có phải cậu muốn▼đổi lấy $540'4; không?", 163: "Đổi đồ nào.$019'652;", 165: 'Được, cậu muốn đổi▼món nội thất nào?', 166: 'Hả? À, vậy để▼lần khác nhé.', 167: 'Cậu chắc muốn▼đổi món đó chứ?', 168: 'Vì cậu sắp khiến▼tớ vui hết cỡ đấy!', 169: 'Vui quá! Vậy là▼cả hai đều có lợi!', 170: 'Xin lỗi, $500;.▼Tớ không thể đổi món đó.', 171: 'Tớ muốn đổi▼đồ nội thất cơ.', 172: 'Có món nội thất nào▼muốn đổi thì▼đến tìm tớ nhé.', 173: 'Xin lỗi, $500;, tớ chỉ▼đổi đồ nội thất▼cùng kích cỡ thôi.', 174: 'Cậu không có món nào▼cùng kích cỡ sao?', 175: 'Không có ý chê đâu,▼nhưng thứ đó... ừm...▼rẻ quá.', 176: 'Tớ không đổi được▼món đó đâu.', 177: 'Khi tìm được món▼giá trị hơn,▼cứ quay lại nhé.', 178: 'Gì đây? Không được rồi.▼Đó là loại nội thất▼hoàn toàn khác mà.', 179: 'Có món cùng loại thì▼đến gặp tớ nhé.', 180: 'Ơ?! Đây là▼cùng một món mà?', 181: 'Tớ chẳng hiểu▼sao cậu lại muốn▼đổi hai món giống hệt.', 182: 'Chọn món khác đi nhé.', 183: 'Cậu muốn ghé▼hội chợ đồ cũ của tớ không?', 184: 'Dừng ngay đi!▼Tớ bắt đầu cáu rồi đấy!$079;', 185: 'Gì đây?▼Bản sao của tớ à?', 186: 'Trông thông minh ghê...▼Khoan... tớ...▼chóng mặt quá...$079;', 187: '$500; đấy à?▼T-tớ vừa ngủ gật sao...$079;', 188: 'Cái gì?! Phòng tớ▼biến thành cả một▼vườn nấm tí hon rồi!', 189: 'Hay lấy nó làm đề tài▼nghiên cứu tiếp theo nhỉ...$079;', 190: 'Ối, $500;?▼T-tớ vừa làm gì thế?!$079;', 191: '$500;, cậu dễ thương quá...', 192: 'H-hình như tớ thích cậu rồi!▼Tớ thuộc về cậu!$079;', 193: '$500;! Hình như tớ▼bị một sức hút kỳ lạ▼tác động mất rồi!', 194: 'Cứu tớ với! $500;...!$079;', 195: 'Ơ... tớ định nói gì ấy nhỉ?$079;', 196: 'Tớ có một vấn đề.', 197: 'Tớ cảm kích cậu▼đã quan tâm, nhưng...', 198: 'Tớ sẽ tự dùng▼khả năng suy luận▼để giải quyết!$079;', 199: 'Tớ đang nghỉ ngơi,▼nhưng thật ra...', 200: 'trong đầu tớ đang▼lập kế hoạch tương lai.$079;', 201: 'Cậu không biết không thể▼niệm chú khi có người▼đứng xem sao?', 202: 'Để tớ yên một chút đi...!$079;', 203: 'Tớ muốn mua một món,▼nhưng đã tiêu sạch tiền▼vào thí nghiệm rồi.$079;', 204: 'Chào $500;.▼Có chuyện gì vậy?', 205: 'Tớ đang nghĩ xem▼tiếp theo nên▼nghiên cứu môn gì...$079;', 206: 'Dạo này đầu tớ▼cứ nặng nặng.', 207: 'Nhưng tớ chẳng lo đâu!▼Như tớ vẫn nói:▼cứ nghĩ tích cực lên!', 208: 'Bụng tớ hơi khó chịu.', 209: 'Không biết tớ▼ăn nhầm gì không...', 210: 'Ừm... xin lỗi, cậu nói gì?▼Hôm nay tớ hơi▼lơ mơ một chút.', 211: 'Chắc tại học nhiều quá...', 212: 'Hôm nay tớ nghỉ học▼vì đau đầu kinh khủng.', 213: "Xin lỗi, để hôm khác▼cùng chơi nhé.$073'705'2'1;", 214: 'Hôm nay tớ nghỉ học▼vì đau bụng dữ dội.', 215: "Xin lỗi, giờ tớ chẳng▼có sức đi chơi.$073'705'2'1;", 216: 'Tiếc phải báo là▼hôm nay tớ bị sốt.', 217: "Xin lỗi, tớ nghĩ▼giờ ra ngoài chơi▼không ổn đâu.$073'705'2'1;", 218: "Tớ đau nửa đầu quá.▼Không thể ra ngoài được.$073'705'2'1;", 219: "Bụng dạ tớ đang có vấn đề.▼Tớ nên ở gần... ừm...▼nhà vệ sinh thì hơn.$073'705'2'1;", 220: "Có vẻ tớ đang sốt.▼Lại còn mệt và chóng mặt.$073'705'2'1;", 221: 'Ngồi đây nhâm nhi đồ uống▼thật dễ nảy ra ý tưởng...', 222: 'Uống gì cùng tớ nhé,▼$500;?', 223: 'Chào $500;!▼Cùng đi câu cá nào!', 224: 'Biết đâu ta câu được▼cá quý để nghiên cứu▼sinh vật đấy!$079;', 225: 'Á! $500;!▼Sao cậu lại ở đây?!', 226: 'Tớ đang bận!▼Để lát nữa nhé!$079;', 227: 'Tớ thích đọc sách lắm!▼Đọc vui cực kỳ!', 228: 'Tớ đặc biệt thích▼từ điển đấy.', 229: 'Đọc rồi thu nạp cả kho▼kiến thức trong đó▼thích mê luôn!$079;', 230: 'Biển rộng thật.▼Một ngày nào đó,▼tớ muốn vượt qua nó...', 231: 'và ghi lại mọi quan sát▼để tự vẽ bản đồ▼thế giới thật chi tiết!$079;', 232: 'Từ Mũi Tình Nhân▼nhìn ra đẹp thật,▼gió cũng mát nữa!', 233: 'Nhưng phải luôn▼cẩn thận kẻo ngã đấy.$079;', 234: 'Học tập là điều cần thiết!▼Có học mới trưởng thành được.'}
assert len(MANUAL) == 220

with zipfile.ZipFile(PREV) as zin:
    assert zin.testzip() is None, 'Invalid baseline ZIP CRC'
    oldfiles = {
        name[len(OLD):]: zin.read(name)
        for name in zin.namelist() if name.startswith(OLD) and not name.endswith('/')
    }
assert len(oldfiles) == 1411, len(oldfiles)
jsonl = [name for name in oldfiles if name.startswith('translation/') and name.endswith('.jsonl')]
assert len(jsonl) == 501, len(jsonl)
oldrows = {
    name: [json.loads(line) for line in oldfiles[name].decode('utf8').splitlines() if line.strip()]
    for name in jsonl
}
assert sum(map(len, oldrows.values())) == 55976
assert sum(sum(row.get('vi') is not None for row in rows) for rows in oldrows.values()) == 24935

targetset = {TALK + key + '.jsonl' for key in TARGETS}
prior = collections.defaultdict(collections.Counter)
for name, rows in oldrows.items():
    if name in targetset:
        continue
    for row in rows:
        if isinstance(row.get('en'), str) and isinstance(row.get('vi'), str):
            prior[LEAD.sub('', row['en'])][LEAD.sub('', row['vi'])] += 1

unique = {}
for key in TARGETS:
    name = TALK + key + '.jsonl'
    rows = oldrows[name]
    assert len(rows) == 120 and all(r['vi'] is None for r in rows), key
    for row in rows:
        unique.setdefault(LEAD.sub('', row['en']), None)
assert len(unique) == 234, len(unique)
assert set(MANUAL) == {i for i, en in enumerate(unique, 1) if not prior[en]}, 'Manual/index reuse mismatch'

translations = {}
report = []
for i, en in enumerate(unique, 1):
    isnew = i in MANUAL
    vi = MANUAL[i] if isnew else prior[en].most_common(1)[0][0]
    assert vi and '\n' not in vi, (i, 'missing translation')
    assert TOKEN.findall(en) == TOKEN.findall(vi), (i, en, vi, 'token mismatch')
    assert unicodedata.normalize('NFC', vi) == vi, (i, 'non-NFC')
    assert vi.count('▼') <= 3, (i, 'too many line breaks')
    for segment in vi.split('▼'):
        static = TOKEN.sub('', segment)
        assert len(static) <= 34, (i, 'segment overflow', len(static), static)
        assert not re.search('[“”‘’—–«»…\u3000]', static), (i, 'punctuation', static)
    translations[en] = vi
    report.append((i, en, vi, 'DỊCH MỚI' if isnew else 'TÁI DÙNG'))

patch = {}
changed = []
for key in TARGETS:
    name = TALK + key + '.jsonl'
    rows = []
    for original in oldrows[name]:
        row = original.copy()
        lead = LEAD.match(row['en'])
        row['vi'] = (lead.group(0) if lead else '') + translations[LEAD.sub('', row['en'])]
        assert TOKEN.findall(row['en']) == TOKEN.findall(row['vi']), row['id']
        assert {k:v for k,v in original.items() if k!='vi'} == {k:v for k,v in row.items() if k!='vi'}
        rows.append(row)
    data = ''.join(json.dumps(row, ensure_ascii=False, separators=(',', ':')) + '\n' for row in rows).encode('utf8')
    patch[name] = data
    (STAGE / (key + '.jsonl')).write_bytes(data)
    short = key.replace('.', '_')
    (STAGE / ('manual_' + short + '.tsv')).write_text(
        'id\ten\tvi\tctx\n' + ''.join(f"{r['id']}\t{r['en']}\t{r['vi']}\t{r.get('ctx', '')}\n" for r in rows), encoding='utf8')
    (STAGE / ('vi_' + short + '.txt')).write_text(
        ''.join(f"{r['id']}\t{r['vi']}\n" for r in rows), encoding='utf8')
    changed.extend(rows)
assert len(changed) == 240 and len({r['id'] for r in changed}) == 240
(STAGE / 'DELTA-097.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False, separators=(',', ':')) + '\n' for r in changed), encoding='utf8')
(STAGE / 'unique_097.tsv').write_text('index\ten_body\tvi_body\torigin\n' + ''.join(f'{i}\t{en}\t{vi}\t{origin}\n' for i,en,vi,origin in report), encoding='utf8')
for key in NEXT:
    name = TALK + key + '.jsonl'
    rows = oldrows[name]
    assert len(rows) == 120 and all(row['vi'] is None for row in rows), key
    (STAGE / (key + '.jsonl')).write_bytes(oldfiles[name])

qa = '''# QA — Magician's Quest Checkpoint 097 (10/11/2026)

- **PASS:** 501 JSONL / 55,976 records compared with checkpoint 096.
- **24,935 → 25,175 / 55,976 (44.97%)**: +240 NPC dialogue pages.
- `0044.001`: 120/120; `0044.002`: 120/120.
- 234 unique English bodies, of which 14 reuse prior EN–VI pairs and **220 are new Vietnamese translations**.
- 24,935 previous translated records unchanged; all **499 non-target JSONLs byte-identical**.
- `id`, `en`, `ctx`, all other JSON fields and ordering preserved in target rows.
- Exact NDS control-token sequence preserved in every target; Unicode NFC PASS, max 3 breaks, <=34 static codepoints per segment.
- ZIP CRC PASS; 501 JSONL parse, 55,976 rows, 25,175 translated; archive reconstruction script provided.
- **In-ROM font rendering and dynamic token expansion have not been tested.**
- Next 098: `0044.003` + `0044.004` (120 pages each), sources included in ZIP.
'''
cp = '''# Magician's Quest — Checkpoint 097

**Date:** 10/11/2026
**Repository:** `ronvotri/VH-NDS` / `Magicians-Quest-Mysterious-Times/`.

- +240 NPC dialogue pages: `0044.001` (120) + `0044.002` (120).
- Total **25,175/55,976 (44.97%)**; NPC **22,050/52,608**.
- 234 unique English bodies: 14 reused; 220 translated manually. Stories include scholarly student interactions, gifts, room and tea visits, studying and transferring schools.
- Full QA: 501 JSONLs PASS; existing 24,935 translations preserved; all 499 non-target JSONLs byte-identical.
- Handoff: `DELTA-097.jsonl`, `unique_097.tsv`, EN–VI TSVs, `QA-097.md`, `build_097.py`, full ZIP in Library.
- Next 098: `0044.003` and `0044.004` (240 pages, untranslated, staged in ZIP).
- ROM visual test remains outstanding.
'''
(STAGE / 'QA-097.md').write_text(qa, encoding='utf8')
(STAGE / 'CHECKPOINT-2026-11-10-DOT-97.md').write_text(cp, encoding='utf8')
intro_rm = '**Checkpoint mới nhất: 097 (10/11/2026) — 25.175/55.976 (44,97%).** +240 trang thoại NPC (`0044.001`: 120; `0044.002`: 120); 220 mẫu mới, 14 mẫu tái sử dụng; QA 501 JSONL PASS. Tiếp `0044.003` và `0044.004` (240 trang). Xem `CHECKPOINT-2026-11-10-DOT-97.md`, `QA-097.md`.\n\n'
intro_bd = '''## Checkpoint 097 — 10/11/2026

- +240 trang NPC `0044.001` (120) và `0044.002` (120); tổng **25.175/55.976 (44,97%)**, NPC 22.050/52.608.
- 234 mẫu EN riêng: 14 mẫu tái dùng, 220 mẫu dịch mới.
- QA 501 JSONL PASS, không sửa 24.935 bản dịch cũ và 499 JSONL ngoài đợt.
- ZIP đầy đủ, EN–VI TSV, delta, QA, script; chưa test ROM.
- Tiếp đợt 098: `0044.003`, `0044.004` (240 trang).

'''
patch['README.md'] = (intro_rm + oldfiles['README.md'].decode('utf8')).encode('utf8')
patch['BAN_GIAO.md'] = (intro_bd + oldfiles['BAN_GIAO.md'].decode('utf8')).encode('utf8')
for name in ['README.md','BAN_GIAO.md']:
    (STAGE / name).write_bytes(patch[name])
for name in ['QA-097.md','CHECKPOINT-2026-11-10-DOT-97.md','DELTA-097.jsonl','unique_097.tsv',
             'manual_0044_001.tsv','manual_0044_002.tsv','vi_0044_001.txt','vi_0044_002.txt']:
    assert name not in oldfiles, name
    patch[name] = (STAGE / name).read_bytes()
patch['build_097.py'] = Path(__file__).read_bytes()
with zipfile.ZipFile(OUT, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zout:
    for name, payload in sorted({**oldfiles, **patch}.items()):
        zout.writestr(NEW + name, payload)
with zipfile.ZipFile(OUT) as zout:
    names = zout.namelist()
    assert len(names) == len(set(names)) and zout.testzip() is None
    jsonlnames = [name for name in names if name.startswith(NEW + 'translation/') and name.endswith('.jsonl')]
    assert len(jsonlnames) == 501
    total = done = 0
    for name in jsonl:
        if name not in targetset:
            assert zout.read(NEW + name) == oldfiles[name], 'Non-target JSONL altered: '+name
        rows = [json.loads(s) for s in zout.read(NEW + name).decode('utf8').splitlines() if s.strip()]
        total += len(rows)
        done += sum(r.get('vi') is not None for r in rows)
        if name in targetset:
            assert all(r['vi'] is not None for r in rows)
    assert (total, done) == (55976, 25175), (total, done)
print(json.dumps({'status':'PASS','path':str(OUT),'bytes':OUT.stat().st_size,
                  'entries':len(names),'jsonl':len(jsonlnames),'records':total,'translated':done,
                  'new_pages':len(changed),'unique':len(unique),'new_unique':len(MANUAL),
                  'reused_unique':len(unique)-len(MANUAL),
                  'sha256':hashlib.sha256(OUT.read_bytes()).hexdigest()},ensure_ascii=False))