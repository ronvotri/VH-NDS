#!/usr/bin/env python3
"""Hand-authored Vietnamese translations by exact repeated English text, batch 054."""
from pathlib import Path
import re,json,collections
ROOT=Path(__file__).resolve().parent
PREFIX=re.compile(r'^(?:\$(?:024|023|022|034|040)(?:[\'0-9-]+)*;)+')
VI_005='''nhưng tớ nghĩ đã đến lúc dừng▼chuyện yêu đương sướt mướt này.
Dù không còn là một đôi,▼tớ vẫn muốn đi chơi với cậu▼như hai người bạn!¤¤
Chúng mình đã hẹn hò▼được một thời gian rồi...
Hửm? Cậu cần gì à?¤¤
Giờ tớ chẳng có chuyện gì▼thú vị để kể cả.¤
Trò chuyện¤
Tặng đồ¤
Đi chơi¤
Đến trường¤
Không có gì¤
Hả? Cậu định tặng tớ thứ gì à?▼Tuyệt quá đi!¤¤
Ngay bây giờ à? Xin lỗi nhé,▼tớ không đi được đâu!
Cậu biết đấy, tớ nổi tiếng lắm.▼Ai cũng muốn được dành▼thời gian bên tớ.
Để hôm khác mình đi chơi nhé?¤
Ừ...¤¤
Cậu chắc chứ? Cần gì thì▼cứ bảo tớ một tiếng nhé.¤
Sao thế? Cậu cần gì à?¤¤
Giờ tớ chẳng có chuyện gì▼hay ho để kể cả...¤
Kể tớ nghe chuyện đi.¤
Tớ có quà cho cậu này.¤
Đi chơi nhé!¤
Cùng đến trường nào!¤
Thôi, không có gì.¤
Thật sao? Quà gì thế?¤¤
Đi chơi thôi! Nhanh nào!¤¤
Được rồi...¤¤
Ừ. Có chuyện gì thì cậu▼biết tìm tớ ở đâu rồi đấy.¤
Ừ? Cậu cần gì sao?¤¤
Kể tớ nghe chuyện đi.¤
Tớ có quà cho cậu này.¤
Cùng đến trường nào!¤
Thôi, không có gì.¤
Ừ. Cần gì thì cậu cứ▼đến tìm tớ nhé.¤
Này!¤
À mà này, hôm nọ tớ thấy...
¤ với ¤▼¤▼¤.
Hai người đó tình tứ quá trời.▼Thú thật, tớ hơi ghen tị đấy.
Nhưng mà sến quá, chẳng hợp▼với một anh chàng lịch lãm▼như tớ chút nào.
Họ vui vẻ thì cũng tốt thôi,▼nhưng mà...
ồn ào quá! Tớ chẳng sao▼tập trung câu cá nổi!
ồn thế thì còn bắt côn trùng▼kiểu gì được chứ?
Không biết hai người đang niệm▼thần chú gì nhỉ? Tớ ghen tị quá.
Ước gì có người cùng tớ▼niệm chú nữa...
Hai người ấy tình cảm ghê.▼Thú thật, tớ hơi ghen tị đấy.
Tớ bận giữ vẻ ngoài▼lịch lãm suốt ngày...
nhưng thỉnh thoảng được▼ngồi thư giãn cùng ai đó▼cũng thích thật!
Tán chuyện mãi mà không líu lưỡi,▼hai người đó giỏi thật đấy!
Nếu là món quà thật sành điệu,▼tớ cũng muốn nhìn thử.
Trông họ vui vẻ thật...▼Bao giờ tớ mới có▼bạn gái của riêng mình đây?
Không biết giữa họ▼đã xảy ra chuyện gì nữa...
Dù sao, dám thử rồi thất bại▼vẫn hơn chưa từng thử nhỉ.
Hai người hợp nhau quá chừng.▼Nhìn mà tớ cũng ghen tị.
Nhưng sến quá, chẳng hợp▼với một anh chàng lịch lãm▼như tớ chút nào.'''
VI_006='''¤ và ¤▼¤▼¤.
Tán chuyện mãi mà không líu lưỡi,▼hai người đó giỏi thật đấy!
À mà này, hôm nọ tớ thấy...
Tuyệt thật! Tớ cũng muốn▼đánh nhau giỏi như thế!
¤ đang vui vẻ▼¤▼¤.
Tớ nghĩ làm gì cũng vậy,▼có bạn bè bên cạnh sẽ▼vui hơn nhiều.
Hay hôm nào tớ rủ ¤▼đi chơi cùng nhỉ.
Không biết ¤ đang▼bắt được thứ gì nhỉ...
Lẽ ra tớ nên lén nhìn một chút...
¤ đang mải mê▼¤▼¤.
Không biết ¤ đã dùng▼thần chú gì nhỉ...
Lẽ ra tớ phải hỏi mới đúng...
Không biết ¤ đang▼làm phép gì nhỉ...
¤ đang ¤▼một mình ¤.
Dù trông cứ như đang▼ngồi mơ mộng thôi...
chắc ¤ đang nghĩ▼đến chuyện gì thú vị lắm.
Không biết sao ¤▼lại làm thế nhỉ...
Nhìn vui thật! Âm nhạc▼đúng là khiến lòng người▼nhẹ nhõm hơn nhiều.
¤ đang thong thả▼¤▼¤.
Trông chán chết đi được.▼Là tớ thì bỏ cuộc lâu rồi.
Không hiểu nhặt rác▼có gì thú vị nhỉ.▼À, cũng là việc tốt mà...
Không biết ở đó có gì▼hay ho không nữa...
Tớ cũng muốn tham gia▼mấy trò nghịch ngợm!▼Lần tới rủ ¤ mới được...
À mà này, đoán xem▼tớ nghe được chuyện gì!
¤ và ¤▼đang ¤▼¤.
Hai người đó tình tứ quá trời.▼Thú thật, tớ hơi ghen tị đấy.
Nhưng sến quá, chẳng hợp▼với một anh chàng lịch lãm▼như tớ chút nào.
Họ vui vẻ thì cũng tốt thôi,▼nhưng mà...
ồn ào quá! Tớ chẳng sao▼tập trung câu cá nổi!
ồn thế thì còn bắt côn trùng▼kiểu gì được chứ?
Không biết hai người đang niệm▼thần chú gì nhỉ? Tớ ghen tị quá.
Ước gì có người cùng tớ▼niệm chú nữa...
Hai người ấy tình cảm ghê.▼Thú thật, tớ hơi ghen tị đấy.
Nhưng sến quá, chẳng hợp▼với một anh chàng lịch lãm▼như tớ chút nào.
Tớ bận giữ vẻ ngoài▼lịch lãm suốt ngày...
nhưng thỉnh thoảng được▼ngồi thư giãn cùng ai đó▼cũng thích thật!
¤ đang▼¤ ¤▼¤.
Nếu là món quà thật sành điệu,▼tớ cũng muốn nhìn thử.
Nghe cũng vui đấy.▼Bao giờ tớ mới có▼bạn gái của riêng mình nhỉ...
¤ đang ¤▼¤▼¤.
Không biết giữa họ▼đã xảy ra chuyện gì nữa...
Dù sao, dám thử rồi thất bại▼vẫn hơn chưa từng thử nhỉ.
Hai người hợp nhau quá chừng.▼Nhìn mà tớ cũng ghen tị.
Nhưng sến quá, chẳng hợp▼với một anh chàng lịch lãm▼như tớ chút nào.
Nhưng sến quá, chẳng hợp▼với một anh chàng lịch lãm▼như tớ chút nào.'''
for suffix,spec in [('0040.005',VI_005),('0040.006',VI_006)]:
    path=ROOT/'translation/04-thoai'/f'talkfigs__0eng__data__{suffix}.jsonl'
    rows=[json.loads(l) for l in path.read_text(encoding='utf8').splitlines() if l.strip()]
    keys=list(dict.fromkeys(PREFIX.sub('',r['en']) for r in rows))
    translations=spec.splitlines()
    if len(keys)!=len(translations):
        raise ValueError(f'{suffix} keys={len(keys)} translations={len(translations)}')
    mapping=dict(zip(keys,translations))
    out=[mapping[PREFIX.sub('',r['en'])] for r in rows]
    assert len(out)==120
    (ROOT/f'vi_{suffix.replace(".","_")}_raw.txt').write_text('\n'.join(out)+'\n',encoding='utf8')
    print(f'{suffix}: {len(keys)} unique lines -> {len(out)} translated pages')