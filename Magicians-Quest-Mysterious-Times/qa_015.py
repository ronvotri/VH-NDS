#!/usr/bin/env python3
"""Compare checkpoint 015 to 014; ensure new data changes ONLY vi fields."""
import collections,json,pathlib,re,sys,unicodedata,zipfile
ROOT=pathlib.Path(__file__).resolve().parent
BASE=ROOT.parent/'MagiciansQuest-VietHoa-Checkpoint-014.zip'
TOKEN=re.compile(r"\$\d+(?:'[-\d]+)*;")
EXPECTED={'translation/04-thoai/talkfigs__0eng__data__0022.003.jsonl':120,
          'translation/04-thoai/talkfigs__0eng__data__0022.004.jsonl':120}
problems=[]; changes=[]; total=filled=0; counts=collections.Counter()
with zipfile.ZipFile(BASE) as z:
    files=sorted(x for x in z.namelist() if x.startswith('MagiciansQuest_014/translation/') and x.endswith('.jsonl'))
    if len(files)!=501:problems.append(f'Wrong file count {len(files)}')
    for name in files:
        rel=name.split('/',1)[1]
        old=[json.loads(s) for s in z.read(name).decode('utf-8').splitlines()]
        path=ROOT/rel
        if not path.exists():problems.append('Missing '+rel);continue
        new=[json.loads(s) for s in path.read_text(encoding='utf-8').splitlines()]
        if len(old)!=len(new):problems.append('Count changed '+rel);continue
        for before,after in zip(old,new):
            total+=1
            if before['id']!=after['id']:problems.append('ID changed '+rel);continue
            for key in set(before)|set(after):
                if key!='vi' and before.get(key)!=after.get(key):problems.append('Changed '+key+' '+rel+' '+before['id'])
            vi=after.get('vi')
            if vi not in (None,''):filled+=1
            prev=before.get('vi')
            if vi==prev:continue
            if prev not in ('',None):problems.append('Overwrote existing VI '+rel+' '+before['id'])
            if vi in ('',None):problems.append('Blank translation '+rel+' '+before['id']);continue
            if TOKEN.findall(before['en'])!=TOKEN.findall(vi):problems.append('Lost token '+rel+' '+before['id'])
            if unicodedata.normalize('NFC',vi)!=vi:problems.append('Non-NFC '+rel+' '+before['id'])
            if any(c in vi for c in '\t\n\r'):problems.append('Bad whitespace '+rel+' '+before['id'])
            if vi.count('▼')>3:problems.append('Many breaks '+rel+' '+before['id'])
            if any(len(TOKEN.sub('',seg))>34 for seg in vi.split('▼')):problems.append('Long line '+rel+' '+before['id'])
            if after.get('max_utf8_bytes') is not None and len(vi.encode('utf-8'))>after['max_utf8_bytes']:
                problems.append('Byte overflow '+rel+' '+before['id'])
            counts[rel]+=1
            changes.append({'file':rel.removeprefix('translation/'),'id':after['id'],'en':after['en'],'old_vi':prev,'vi':vi,'ctx':after.get('ctx')})
if total!=55976:problems.append('Wrong total '+str(total))
if filled!=6045:problems.append('Wrong translated total '+str(filled))
if len(changes)!=240:problems.append('Wrong changed rows '+str(len(changes)))
if dict(counts)!=EXPECTED:problems.append('Unexpected changed files '+str(dict(counts)))
if problems:
    print('FAIL',len(problems),'\n'+'\n'.join(problems[:120]));sys.exit(1)
(ROOT/'DELTA-015.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n' for x in changes),encoding='utf-8')
(ROOT/'QA-015.md').write_text('''# QA — Magician’s Quest checkpoint 015

- So với checkpoint 014 bất biến, **501 tệp JSONL**, **55.976** bản ghi.
- **240 trang thoại mới**, chia đều `0022.003` và `0022.004` (120 trang mỗi tệp).
- **6.045 / 55.976** trường `vi` đã điền, trong đó hội thoại: **2.920 / 52.608**.
- Chỉ trường `vi` thay đổi, **0 lỗi** ID, `en`, `ctx`, metadata, mã điều khiển `$...;`, NFC, TAB/CR/LF, ngưỡng 34 ký tự/đoạn, `max_utf8_bytes` khi có.
- Bảo toàn mã tên người chơi `$500;`, tên NPC `$503'307;`, `$503'309;` và toàn bộ mã lựa chọn `$019'...;` đúng thứ tự.
- Dịch tay theo từng trang, giữ giọng NPC có phần tự phụ, hài tự trào; ngôi xưng tớ–cậu với bạn bè.
- **Chưa kiểm thử font/chiều rộng pixel trên ROM thật**; 34 ký tự chỉ là bước rà văn bản, không bảo đảm vừa khung 160 px của NDS.
''',encoding='utf-8')
print('PASS:',len(files),'JSONL',total,'rows',filled,'filled',len(changes),'new',dict(counts))