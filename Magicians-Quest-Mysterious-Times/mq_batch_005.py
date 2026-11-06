#!/usr/bin/env python3
"""Lô 005: dịch lời chào khi gặp bạn và lời thoại cửa hàng/trường học.
@0, @1... trong phần văn bản là mã điều khiển hiện có (không tính mã tiền tố)."""
from pathlib import Path
import json,re,unicodedata
ROOT=Path(__file__).resolve().parent/'translation/04-thoai'
TOK=re.compile(r"\$\d{3}(?:'[^;\r\n\t]*)?;")
PFX=re.compile(r"^(?:(?:\$(?!500|503|000)\d{3}(?:'[^;\r\n\t]*)?;))*")
slot=re.compile(r'@(\d+)')

# Người bán hàng có vai riêng: Piquard (lịch sự), Daisy (ấm áp), Vivian (năng động),
# Roley (điệu), Malila (lớn tuổi), Marcy (hiền), Thom (cộc mà vui), Mah (nói chậm),
# giáo viên (thầy/cô – em khi xác định rõ giới; mặc định không gán giới), bạn bè (tớ – cậu).
shop=r'''0|Xin chào! Tôi là▼@0Piquard@1. Mời ghé cửa hàng!
1|Ở @0Harrows@1, đồ nội thất▼và thảm đủ loại, tha hồ chọn!
2|Tầng hai có thảm, đĩa CD▼và còn khối thứ hay ho nữa.
3|Thích món nào thì đứng trước▼món đó, nhấn @0nút A@1▼để đặt mua nhé.
4|Cứ ngắm nghía thong thả,▼không cần vội đâu.
5|Chào mừng! Cảm ơn đã ghé▼@0Harrows@1 hôm nay!
6|Chào mừng! Cảm ơn đã ghé▼@0Harrows@1 hôm nay!
7|Chào mừng! Cảm ơn đã ghé▼@0Harrows@1 hôm nay!
8|Chào nhé! Mình là @0Daisy@1.▼Đây là tiệm hoa của mình!
9|Ở đây có đủ đồ làm vườn▼và cả một trời hoa xinh!
10|Thấy món nào ưng mắt,▼cứ đứng trước nó và nhấn▼@0nút A@1 nhé.
11|Xin chào! Mời vào tiệm▼@0Daisy's Flowers@1!
12|Xin chào! Mời vào tiệm▼@0Daisy's Flowers@1!
13|Xin chào! Mời vào tiệm▼@0Daisy's Flowers@1!
14|Chào nha! Mình là @0Vivian@1.▼Vào xem đồ đi nào!
15|Tiệm mình có đồ cho mọi dịp!▼Đi tiệc, đi chơi, kiểu gì▼cũng có hết nha!
16|Chuẩn luôn! Muốn lên đồ▼từ đầu đến chân thì cứ▼ghé đây!
17|Muốn thử đồ? Khỏi cần hỏi!▼Đứng trước món thích rồi▼nhấn @0nút A@1 là được.
18|Chào mừng! Vào xem thử đi,▼biết đâu trúng gu đó!
19|Chào mừng! Vào xem thử đi,▼biết đâu trúng gu đó!
20|Chào mừng! Vào xem thử đi,▼biết đâu trúng gu đó!
21|Chào! Ghé salon tóc▼@0Mon Paris@1 chơi chút không?
22|Mình là @0Roley@1, chủ▼tiệm nhỏ xinh này đây!
23|Tóc tai cứ giao mình lo!▼Đảm bảo xinh lung linh!
24|Ối, mình lỡ lời!▼Bạn vốn đã xinh sẵn rồi mà!▼Ngại quá đi mất!
25|Ồ, @0! Vào chơi đi!
26|Ồ, @0! Vào chơi đi!
27|Ồ, @0! Vào chơi đi!
28|Hửm? Hình như ta với▼cháu chưa gặp nhau nhỉ?
29|Ta là @0Malila@1.▼Chào mừng đến tiệm của ta.
30|Đây là @0The Emporium@1.▼Tiệm bán nguyên liệu cần▼cho các loại thần chú.
31|Thần chú hay phép thuật▼trục trặc thì cứ đến tìm ta.
32|Biết đâu ta có đúng thứ▼cháu đang cần đấy.
33|À phải rồi, suýt quên!▼Thấy món nào muốn mua thì...
34|Đứng trước món đó,▼nhấn @0nút A@1 là được.
35|Chào mừng đến @0The Emporium@1,▼tiệm đồ của giới phù thủy!
36|Chào mừng đến @0The Emporium@1,▼tiệm đồ của giới phù thủy!
37|Chào mừng đến @0The Emporium@1,▼tiệm đồ của giới phù thủy!
38|Ồ? Hình như ta chưa gặp em.▼Em mới tới đây à?
39|Ta là @0Marcy@1, quản lý▼@2Limelight@3. Phù thủy nhỏ▼cứ tự nhiên vào nhé.
40|Có chuyện gì muốn tâm sự▼thì cứ ghé đây, ta luôn▼sẵn lòng lắng nghe.
41|Chào! Vào chơi đi nào!
42|Chào! Vào chơi đi nào!
43|Chào! Vào chơi đi nào!
44|Chào em, tôi là @0George@1.
45|Tôi làm việc tại @0ngân hàng@1 này.
46|Cần gửi hay rút tiền▼thì cứ đến gặp tôi nhé.
47|Cứ yên tâm! Đồ quý của em▼được chúng tôi giữ▼cẩn thận lắm.
48|Chào mừng đến @0ngân hàng@1!
49|Chào mừng đến @0ngân hàng@1!
50|Chào mừng đến @0ngân hàng@1!
51|Chưa thấy mặt nhóc bao giờ.▼Mới đến đây hả?
52|Ta là @0Thom@1, coi sóc▼@2bưu điện@3 này.
53|Muốn gửi @0điện tín@1 thì▼cứ réo ta một tiếng.
54|Thư sẽ đến ngay...▼nếu đám mèo đưa thư chịu▼nhấc mông lên làm việc!
55|Đây là @0bưu điện@1. Có gì?▼Đám nhóc với lũ mèo ấy...▼Chẳng cho ta nghỉ phút nào!
56|Đây là @0bưu điện@1. Có gì?▼Đám nhóc với lũ mèo ấy...▼Chẳng cho ta nghỉ phút nào!
57|Đây là @0bưu điện@1. Có gì?▼Đám nhóc với lũ mèo ấy...▼Chẳng cho ta nghỉ phút nào!
58|Ồ... người mới...▼Tôi là... @0Mah@1.
59|Như... bạn thấy đấy...▼Tôi... lái taxi.
60|Cần... đi taxi... không?
61|Cần... đi taxi... không?
62|Cần... đi taxi... không?
63|Ê, nhóc! Mới đến đây à?▼Ồ, ra là thế!
64|Tiệm mì của ta đây!▼Nhưng đâu chỉ bán mì,▼thế thì chán chết!
65|Ngoài mì ngon còn có cả▼tin nóng, chuyện gì cũng hóng▼được ở đây!
66|Ta có khối chuyện thú vị!▼Rảnh thì ghé tán dóc nhé!
67|Chào mừng! Vào đi nào!
68|Chào mừng! Vào đi nào!
69|Chào mừng! Vào đi nào!
70|À, @0 bé bỏng đây rồi!
71|Ồ,@0@1 em đến rồi à...
72|Ồ,@0@1 em đến rồi à...
73|Ồ hô! Đi học vui chứ?▼Nhớ đừng chạy trên▼hành lang đó nhé!
74|Ồ hô! Đi học vui chứ?▼Nhớ đừng chạy trên▼hành lang đó nhé!
75|Ồ hô! Đi học vui chứ?▼Nhớ đừng chạy trên▼hành lang đó nhé!
76|Chào mừng, @0!▼Ta vui lắm khi em gia nhập▼ngôi trường này.
77|Ta là Hiệu trưởng Sol.
78|A!▼Hóa ra là @0!
79|A!▼Hóa ra là @0!
80|A!▼Hóa ra là @0!
81|Ta là @0, phụ trách▼môn Ngôn ngữ Phép thuật.▼Nhớ học chăm đấy!
82|@0, mỗi ngày em nên▼ôn bài cũ và xem trước▼bài mới nhé.
83|@0, mỗi ngày em nên▼ôn bài cũ và xem trước▼bài mới nhé.
84|@0, mỗi ngày em nên▼ôn bài cũ và xem trước▼bài mới nhé.
85|Chào @0! Ta là▼@1, người dạy em▼phép thuật dùng đũa phép.
86|Cả lớp cùng học cho vui nhé!
87|Ối! @0 đấy à!▼Đừng lén xuất hiện làm▼người già hết hồn chứ!
88|Ối! @0 đấy à!▼Đừng lén xuất hiện làm▼người già hết hồn chứ!
89|Ối! @0 đấy à!▼Đừng lén xuất hiện làm▼người già hết hồn chứ!
90|Rất vui được gặp em,▼@0.
91|Ta là @0, giáo viên▼môn Thần chú của em.
92|Cùng cố gắng để em thành▼một phù thủy cừ khôi nhé!
93|Em chăm chỉ quá,▼@0 à!▼Nhìn mà có động lực luôn!
94|Em chăm chỉ quá,▼@0 à!▼Nhìn mà có động lực luôn!
95|Em chăm chỉ quá,▼@0 à!▼Nhìn mà có động lực luôn!
96|Rất vui được gặp em, @0!
97|Ta là @0, sẽ phụ trách▼các buổi học ngoại khóa.
98|Học ngoại khóa vui lắm!▼Vui thật đấy...
99|Chào em, @0!▼Ngoại khóa còn giúp ta▼khám phá thiên nhiên đó!
100|Biết đâu em sẽ tìm ra▼điều bất ngờ ở nơi▼thường chẳng ai để ý.
101|Chào em, @0!▼Ngoại khóa còn giúp ta▼khám phá thiên nhiên đó!
102|Biết đâu em sẽ tìm ra▼điều bất ngờ ở nơi▼thường chẳng ai để ý.
103|Chào em, @0!▼Ngoại khóa còn giúp ta▼khám phá thiên nhiên đó!
104|Biết đâu em sẽ tìm ra▼điều bất ngờ ở nơi▼thường chẳng ai để ý.
105|Meo!
106|Meo meo meo... Meo?
107|Meo! Meo meo! Meo!
108|Meo!'''

peers=r'''0|Ê, cậu là @0 đúng không?▼Nghe danh cậu lâu rồi đó!
1|Tớ là @0.▼Rất vui được gặp cậu!
2|Ủa, hình như chưa gặp cậu▼bao giờ? Hả?▼Muốn biết tên tớ à?
3|Cậu phải xưng tên trước chứ!▼Thế mới lịch sự nha.
4|Dù sao tớ là @0.▼Rất vui được gặp cậu!
5|Cậu mới đến đây đúng không?▼Tớ tên là @0.
6|Tớ nhỏ con thôi,▼nhưng vẫn là quý cô▼đàng hoàng đấy nhé!
7|Cứ đối xử với tớ▼như mọi cô gái khác đi!
8|Ừm... mình chưa gặp nhau nhỉ?▼Tớ là @0.
9|Mong là chúng mình sẽ▼thân nhau hơn nhé!
10|Hí lô! Mới gặp lần đầu à?▼Vậy giới thiệu thôi nào!
11|Tớ là @0.▼Tớ mê hoa cực kỳ!
12|Hình như chúng mình▼chưa quen nhau nhỉ?
13|Tớ là @0.▼Thế là quen rồi nhé!
14|Nhớ tôn trọng tớ đấy,▼không thì biết tay!
15|Chắc mình chưa chào nhau.▼Vậy cậu là @0 hả?
16|Tớ là @0.▼Rất vui được gặp cậu.
17|Chào cậu!▼Cậu tên gì thế?
18|Ơ, tên lạ ghê!▼Tớ là @0 nhé.
19|Đừng có thân thiết quá đấy!▼Không khéo bỏng tay!
20|À mà... rất vui được gặp cậu.
21|Ê, @0!▼Dạo này cậu đi đâu mất hút?
22|Mọi người bắt đầu▼xì xào rồi đấy...
23|Chào @0!▼Lâu lắm không thấy▼cậu đâu cả.
24|Lần sau đi đâu thì▼ghé báo tớ một tiếng nhé!
25|Đừng biến mất tăm nữa nha!
26|A, @0 đấy à!
27|Lần sau đi đâu thì▼nhớ báo tớ một tiếng nhé!
28|Tớ bắt đầu lo cho cậu rồi đó...
29|Lâu lắm không gặp!
30|Cậu đi đâu thế?▼Một mình không buồn à?
31|Ô, lâu quá không gặp.
32|Cậu đi khám phá đâu à?
33|Đi chơi có thấy▼bông hoa nào đẹp không?
34|Lâu lắm mới chịu▼ló mặt ra nhỉ!
35|Đi khám phá đâu à?▼Dám đi mà chẳng báo tớ!
36|Lần sau còn thế nữa,▼tớ móc mắt cậu đấy!
37|Ê, @0!▼Lâu rồi không thấy cậu.
38|Cậu bận gì thế?
39|Ô kìa, @0!▼Lâu lắm không gặp!▼Dạo này sao rồi?
40|Chắc cậu đi tìm▼nửa kia của mình hả?▼Đào hoa dữ ha...
41|...đúng là cao thủ tán tỉnh!
42|Có chuyện muốn tâm sự▼thì tìm @0 nhé!▼Cô nàng số một đấy!
43|@0 ơi!▼Chúc mừng năm mới!
44|Tớ linh cảm năm nay sẽ▼siêu tuyệt! Sẵn sàng quẩy rồi!
45|Ê, @0!
46|Dạo này khỏe không?
47|Chào @0 nha.
48|Ê, thế giới ngoài kia▼có nguy hiểm như lời đồn không?
49|Cậu khỏe không, @0?
50|Tớ vẫn khỏe re như mọi khi!
51|*huýt sáo vui vẻ*
52|Hử?
53|Ủa, tớ đến đây để làm gì ấy nhỉ?
54|*huýt sáo vui vẻ*
55|Nhớ ăn uống cho tử tế nha!
56|*ngồi nhìn xa xăm*
57|*mắt đờ đẫn*
58|Đôi khi tớ thích ngồi▼ngẩn ngơ, nghĩ vẩn vơ...
59|Yay! Trời nắng rồi!
60|Trời đẹp là tự nhiên▼tớ cũng vui theo luôn!
61|Trời mưa thì cẩn thận nha!
62|Vấp ngã một cái là▼quần áo lấm bùn ngay!
63|Ngắm tuyết rơi một hồi,▼chẳng biết thời gian▼trôi đâu mất...
64|HẮT XÌ!
65|Chào buổi sáng!
66|Sáng nay cậu ăn no chưa?
67|Tớ ăn cả núi ngũ cốc luôn!
68|Cứ ăn trưa xong là▼mắt tớ díp cả lại...
69|Ước gì được ngủ trưa▼một mạch đến hết ngày nhỉ?
70|Mặt trời đi ngủ rồi.
71|Chắc tớ cũng nên về thôi.
72|Chào buổi tối.
73|Trời tối là tớ buồn ngủ ngay.
74|*ngáp*
75|Giờ Bí Ẩn đầy những▼bất ngờ cực kỳ thú vị!
76|Phải tranh thủ hết cỡ thôi!
77|Ơ, khoan đã, @0!▼Hôm nay sinh nhật cậu▼đúng không?
78|Biết ngay mà!▼Chúc mừng sinh nhật, @0!▼Cậu mấy tuổi rồi?
79|Xin lỗi nhé...▼Giờ tớ chưa muốn nói▼chuyện với ai cả.@0'''

def parse(blob):
 d={}
 for s in blob.splitlines():
  k,sep,v=s.partition('|')
  assert sep and k.isdecimal(),repr(s)
  n=int(k);assert n not in d,n
  d[n]=v
 return d

MAPPING={
 'talkfigs__0eng__data__0012.001.jsonl': parse(shop),
 'talkfigs__0eng__data__0009.001.jsonl': parse(peers),
}

stats={}
for fname,mapping in MAPPING.items():
 f=ROOT/fname;rows=[json.loads(s) for s in f.read_text(encoding='utf-8').splitlines()]
 assert set(mapping)==set(range(len(rows))), (fname,len(rows),set(range(len(rows)))-set(mapping))
 for ix, row in enumerate(rows):
  assert row['vi'] is None,(fname,ix)
  en=row['en']; prefix=PFX.match(en).group(); suffix=en[len(prefix):]
  tokens=TOK.findall(suffix)
  value=mapping[ix]
  # @0, @1... exclusively for internal control slots, not plain text.
  refs=[int(j) for j in slot.findall(value)]
  assert refs==list(range(len(tokens))), (fname,ix,refs,tokens,value)
  translated=slot.sub(lambda m:tokens[int(m.group(1))],value)
  new=prefix+translated
  assert TOK.findall(en)==TOK.findall(new),(fname,ix)
  assert new.count('▼')<=max(2,en.count('▼')),(fname,ix,'visual',new)
  assert new and unicodedata.normalize('NFC',new)==new,(fname,ix)
  if row.get('max_utf8_bytes') is not None:
   assert len(new.encode('utf8'))<=row['max_utf8_bytes'],(fname,ix,'bytes')
  row['vi']=new
 f.write_text(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n' for x in rows),encoding='utf8')
 stats[fname]=len(rows)
print('Translated',stats,'total',sum(stats.values()))