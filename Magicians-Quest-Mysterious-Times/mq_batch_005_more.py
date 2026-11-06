#!/usr/bin/env python3
"""Cụm 005C — NPC rock, vua tự phong, người mê bay chổi và robot."""
import re,json,unicodedata
from pathlib import Path
f=Path(__file__).resolve().parent/'translation/04-thoai/talkfigs__0eng__data__0001.001.jsonl'
TOK=re.compile(r"\$\d{3}(?:'[^;\r\n\t]*)?;")
PFX=re.compile(r"^(?:(?:\$(?!500|503|000)\d{3}(?:'[^;\r\n\t]*)?;))*")
SLOT=re.compile(r'@(\d+)')
raw=r'''0|Hửm? Mặt mới này!▼Hình như chưa gặp cậu nhỉ...
1|Tớ là @0!▼Có gặp rắc rối gì thì▼cứ gọi tớ một tiếng!
2|Ê, trước giờ tớ có▼gặp cậu ở đây chưa nhỉ?
3|Tớ là @0.▼Còn cậu tên gì...?
4|@0 à? Tên hay ghê!▼Hẹn gặp lại nha!
5|Ê hê! Ai mới tới đây thế?
6|Tớ là @0, fan metal▼chính hiệu! Hẹn gặp lại!▼Rock hết mình!
7|Ê, cậu kia!▼Biết kính trọng người ta không?!
8|Dù chưa từng gặp nhau▼cũng chẳng sao. Nhưng▼nếu cậu nhất quyết hỏi...
9|Ta chính là @0,▼vị vua tương lai đây!
10|Từ nay ngươi sẽ là▼cận vệ hầu hạ ta!
11|Được rồi... hôm nay▼ta cho ngươi tạm nghỉ.
12|Hừm... chưa từng thấy▼cậu bao giờ. Vậy là▼lần đầu gặp nhau nhỉ.
13|Tớ là @0.▼Hẹn gặp lại nha.
14|Hay quá! Chào cậu!▼Tớ là @0! Còn cậu...?
15|Thật á? @0 hả?▼Tên hay đấy!▼Vui được gặp cậu!
16|Ồ, ai đây?▼Lần đầu mình gặp nhau à?
17|Tớ là @0.▼Người ta gọi tớ là▼"Tay đua chổi @1" đấy!
18|Trông cậu cũng đáng▼làm đối thủ đó...▼Thôi, hẹn gặp lại!
19|Bíp búp?▼Lần đầu nhận diện cậu.
20|Vui lòng đợi...▼Bíp búp búp bíp bíp...
21|Cậu là... bíp búp...▼@0. Tớ là @1.▼Kết nối thành công!
22|Ê, cậu là @0 đúng không?▼Lâu quá không gặp!
23|Tớ không thấy cậu▼mấy bữa nay. Khỏe không?
24|Cần gì thì cứ gọi tớ!▼Biết tìm ai rồi đấy!
25|Chào @0!▼Lâu lắm mới gặp nhỉ?
26|Cậu vừa đi đâu về à?
27|Yo, @0!▼Cậu biến đâu mất tiêu vậy?
28|Nhớ cảnh tớ quẩy▼nhạc metal điên đảo▼lắm rồi chứ gì? Rock nào!
29|Ê, @0!▼Ngươi đi đâu vậy hả?!
30|Sao dám bỏ bê việc▼hầu hạ vua tương lai▼@0 này hả?!
31|Lần này ta tha!▼Nhưng đừng tái phạm!
32|Ồ, @0 đây rồi.▼Đi đâu thế?▼Tớ lo phát khiếp!
33|Mong là cậu không▼gặp chuyện gì...
34|Không sao là tốt rồi...
35|Ê hê hê! Đồng đội▼quậy phá của tớ, @0!
36|Lâu phát khiếp luôn!▼Sao rồi, chiến hữu?!
37|Ê @0! Lâu quá!▼Vắng cậu ở đây▼buồn hẳn luôn!
38|Đừng nói cậu quên▼@0 vĩ đại này nhé!
39|Đùa thôi! Bữa nào▼đi chơi chung nha!
40|Bíp búp búp bíp?▼Lâu rồi không thấy cậu.
41|Gọi điện cũng không...▼Bíp bíp búp bíp.▼Vui lòng truyền dữ liệu!
42|Ê @0!▼Chúc mừng năm mới!
43|Năm nay tớ sẽ quẩy▼tung trời! Cậu tham gia không?
44|Ê @0!
45|Có tin nóng gì không?
46|Ê @0!▼Dạo này sao rồi?
47|Ê, @0!▼Trông cậu ngầu ghê!
48|Làm tốt lắm!
49|Sao rồi, @0?
50|Ê @0, khỏe không?
51|Ê, @0!
52|Bầu trời xanh đẹp quá!▼Thấy đời đáng yêu ghê!
53|Ê @0! Dạo này sao?
54|Khỏe chứ?
55|Dạo này trời cứ▼xanh trong veo...▼Đỉnh thật!
56|Ngửi thấy mùi▼không khí trong lành không?
57|Mưa rào suốt ngày!▼Tiếng mưa gõ mái nhà▼nghe như nhạc ấy!
58|Cả dàn nhạc của▼mẹ Thiên Nhiên luôn!
59|Tuyết trắng tinh làm▼tớ nhớ tới đầu óc mình...
60|Như trang giấy trắng▼chờ viết điều mới lên!
61|Chào buổi sáng!▼Ngày phiêu lưu bắt đầu!
62|Đừng phí thời gian nữa!
63|Sao rồi, @0?
64|Tập thể dục chung▼với tớ không?
65|Chào ngày mới? Hay tối rồi?▼Nhìn mặt trời thì...
66|...chắc phải chào tạm biệt!
67|Ê @0!▼Cậu cũng mê ban đêm chứ?
68|Tới rồi! Tới rồi!▼Cuối cùng cũng tới!▼Giờ Bí Ẩn đóoooo!!!
69|Cậu định làm gì thế,▼@0?
70|Ê, hôm nay sinh nhật▼cậu đúng không?
71|Chúc mừng sinh nhật, @0!▼Hẹn gặp lại nhé!
72|Xin lỗi... bây giờ▼tớ muốn ở một mình...@0'''
M={}
for line in raw.splitlines():
 k,sep,v=line.partition('|');assert sep and k.isdecimal();n=int(k);assert n not in M;M[n]=v
rows=[json.loads(s) for s in f.read_text().splitlines()];assert set(M)==set(range(len(rows)))
for i,o in enumerate(rows):
 assert o['vi'] is None
 en=o['en'];pfx=PFX.match(en).group();tok=TOK.findall(en[len(pfx):]);v=M[i]
 assert [int(x) for x in SLOT.findall(v)]==list(range(len(tok))),(i,tok,v)
 vi=pfx+SLOT.sub(lambda m:tok[int(m.group(1))],v)
 assert TOK.findall(en)==TOK.findall(vi)
 assert vi.count('▼')<=max(2,en.count('▼')),(i,'pages',vi)
 assert unicodedata.normalize('NFC',vi)==vi
 o['vi']=vi
f.write_text(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n' for x in rows),encoding='utf8')
print('Translated',len(rows),f.name)