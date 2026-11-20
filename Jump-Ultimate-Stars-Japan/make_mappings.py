from pathlib import Path
from functools import lru_cache
import sys, json, re, unicodedata, hashlib, collections
sys.path.insert(0,str(Path(__file__).resolve().parent))
from segments import SEGMENTS
ROOT=Path(__file__).parent
SRC=Path('/mnt/data/JUS_CP053/NGUON_CHUA_DICH_SAU_053.jsonl')
source=[json.loads(ln) for ln in SRC.read_text(encoding='utf-8').splitlines() if ln]
source_by_idx={r['row_index']:r for r in source if r['file']=='00-he-thong-ten-goi-001.jsonl'}

@lru_cache(None)
def segment(txt,n,maxlen=57):
    words=txt.split(' ')
    assert len(words)>=n,(len(words),n)
    pref=[0]
    for w in words:pref.append(pref[-1]+len(w))
    def strlen(i,j):return pref[j]-pref[i]+j-i-1
    goal=len(txt)/n
    @lru_cache(None)
    def dp(i,k):
        if k==0:return (0,[]) if i==len(words) else (float('inf'),[])
        if len(words)-i<k:return (float('inf'),[])
        best=(float('inf'),[])
        for j in range(i+1,min(len(words)-k+2,i+24)):
            lng=strlen(i,j)
            if lng>maxlen:break
            tailcost,tail=dp(j,k-1)
            if tailcost==float('inf'):continue
            end=words[j-1][-1]
            bonus = -32 if end in '.!?:…"' else (-15 if end in ',;' else 0)
            cost=(lng-goal)**2+bonus +tailcost
            if cost<best[0]:best=(cost,[txt if False else ' '.join(words[i:j])]+tail)
        return best
    cost,parts=dp(0,n)
    if cost==float('inf'):
        raise ValueError(f'No segmentation for {len(txt)} chars into {n} lines max {maxlen}')
    assert len(parts)==n and ' '.join(parts)==txt
    return tuple(parts)

out={}
for start,end,heads,story in SEGMENTS:
    assert all(i in source_by_idx for i in range(start,end+1))
    for k,v in enumerate(heads):out[start+k]=v
    n=end-start+1-len(heads)
    chunks=segment(story,n)
    for k,v in enumerate(chunks):out[start+len(heads)+k]=v
# Preserve source control tokens in the same source row and align the question context.
out.update({
  886: 'Tezuka thắng, nhưng nhắn: "Cậu phải<IDEOSP>',
  887: 'trở thành trụ cột Seigaku!" Từ thất bại,',
  888: 'Ryoma càng quyết tâm trở nên mạnh hơn.',
  915: 'Cuộc đấu trí giữa thiên tài giữ sổ tử',
  916: 'thần và những người quyết truy bắt.',
  917: 'Light Yagami, học sinh giỏi nhất nước,',
  918: 'chán ngán cuộc sống. Một ngày, cậu',
  919: 'nhặt được cuốn DEATH<IDEOSP>NOTE kỳ lạ.',
  920: 'Chỉ cần viết tên ai và nhớ mặt người đó,',
  921: 'người ấy sẽ chết. Light bắt đầu dùng sổ',
  922: 'xử lý liên tiếp các tên tội phạm nguy hiểm.',
  923: 'Thiên hạ gọi sát thủ giấu mặt ấy là Kira,',
  924: 'thậm chí có người tung hô hắn như vị cứu tinh.',
  925: 'Nhưng nhiều người cho rằng tự tiện tước',
  926: 'mạng sống cũng là tội ác, nên quyết',
  927: 'tìm bắt Kira. Trong số ấy có một người:',
  928: 'L, thám tử bí ẩn chẳng ai biết mặt,',
  929: 'tên thật hay nơi ở, nhưng phá được mọi án.',
  930: 'Vì DEATH<IDEOSP>NOTE, trận đấu giữa hai',
  931: 'thiên tài Light và L giờ đây chính thức',
  932: 'bắt đầu!',
  1230: 'ngày ra mắt, chú được đặt tên Midori Makibao',
})
assert len(out)==484 and set(out)==set(range(747,1231))
for i in out:
    expected=re.findall(r'<[A-Z][A-Z_]*>',source_by_idx[i]['ja'])
    got=re.findall(r'<[A-Z][A-Z_]*>',out[i])
    assert expected==got,(i,expected,got,out[i])
assert max(len(v) for v in out.values()) <= 57

for i in [886,913,919,930,1218]:
    print('CONTROL ROW before',i,source_by_idx[i]['ja'],'=>',out[i],len(out[i]))
print('Longest chunks:', sorted([(len(v),i,v) for i,v in out.items()],reverse=True)[:20]);print('size',len(out))
(ROOT/'draft_054.tsv').write_text(''.join(f'{i}\t{out[i]}\n' for i in sorted(out)),encoding='utf-8')
