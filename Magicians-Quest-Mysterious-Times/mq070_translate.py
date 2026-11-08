#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Magician's Quest NDS, batch 070: manually reviewed unique translations with exact EN reuse.
Preserves all 501 original JSONL files, all IDs/EN/CTX, and all translated rows from checkpoint 069.
"""
import pathlib, zipfile, json, re, collections, unicodedata, hashlib, datetime, os, sys
OLD=pathlib.Path('/mnt/data/MagiciansQuest-VietHoa-Checkpoint-069.zip')
OUT=pathlib.Path('/mnt/data/MagiciansQuest-VietHoa-Checkpoint-070.zip')
OLD_ROOT='MagiciansQuest_069/'
ROOT='MagiciansQuest_070/'
SUFFIXES=('0041.015','0041.016')
NEXT=('0041.017','0041.018')
PRE=re.compile(r"^(?:\$\d{3}(?:[\d'-]+)?;)+")
TOK=re.compile(r"\$\d{3}(?:[\d'-]+)?;")

# Translation index is assigned to unique EN content after removing initial engine prefixes.
# All other keys are carried over only on exactly matching EN; their prefix controls are reapplied verbatim.
T={
    1:'Hai người đó buôn chuyện suốt!▼Chẳng biết nghỉ miệng▼một lúc sao?',
    6:'Này, nghe tin sốt dẻo chưa...',
    9:'Hai người ấy thân ghê!▼Đi chơi thì rủ cả tớ▼đi cùng chứ!',
    21:'$530\'0; đang niệm▼thần chú gì vậy?▼Đùa thôi à?',
    23:' đang▼$532;▼một mình $531;.',
    30:'Bọn tớ đang bàn về▼tin đồn mới nhất...',
    31:' và $530\'1;▼$533;.',
    32:'Cậu biết chuyện đó chưa?',
    35:' và $530\'1;▼đã $533;.',
    36:'Hừm, không biết họ▼đang làm gì nhỉ...',
    37:' và $530\'1;▼trông vui vẻ bên nhau,▼$533;.',
    38:' và $530\'1;▼$533; đến mức▼trông như giả vờ.',
    39:'Có gì đó sai sai...▼Chắc chắn đang có▼chuyện mờ ám!',
    # Bốn bản cũ vô tình nhân đôi biến đầu câu sau khi bỏ prefix; sửa tại batch mới, không đụng dữ liệu cũ.
    41:' bị bắt gặp▼$531; và trông▼rất $533;.',
    43:' bị bắt gặp▼$531; khi dùng▼$533; kỳ lạ.',
    44:' bị bắt gặp▼$531; khi đang▼$533; rất kỳ lạ.',
    45:' bị bắt gặp▼$531; khi▼$533; rất cẩn thận.',
    46:'Cậu đang giấu chuyện à?▼Cứ nghe có bí mật▼là tớ tò mò ngay!',
    49:'▼$533;▼vì biết quan tâm.',
    52:'Nghịch ngợm ư? Tớ là▼TRÙM quậy phá đấy!▼Phải luyện thêm thôi!',
    63:' có hành động▼đáng ngờ▼$533;.',
    65:'rồi trở thành▼$533;.',
    67:'Ồ, $500;! Chuyện này▼tớ không thể bật mí đâu.',
    68:'Cơ mật đấy nhé!▼Tuyệt mật luôn!',
}

def read_jsonl(z, path):
    return [json.loads(x) for x in z.read(path).decode('utf-8').splitlines()]

def process():
    if not OLD.exists():raise FileNotFoundError(OLD)
    with zipfile.ZipFile(OLD) as z:
        assert z.testzip() is None,'Input ZIP CRC error'
        old_entries={name.removeprefix(OLD_ROOT):z.read(name) for name in z.namelist() if not name.endswith('/')}
        jsonl_paths=sorted(p for p in old_entries if p.startswith('translation/') and p.endswith('.jsonl'))
        assert len(jsonl_paths)==501,len(jsonl_paths)
        old_rows={p:[json.loads(x) for x in old_entries[p].decode().splitlines()] for p in jsonl_paths}
        assert sum(len(v) for v in old_rows.values())==55976
        lookup=collections.defaultdict(collections.Counter)
        for rows in old_rows.values():
            for r in rows:
                if r['vi'] is not None:
                    lookup[PRE.sub('',r['en'])][PRE.sub('',r['vi'])]+=1
        new_source={s:old_rows[f'translation/04-thoai/talkfigs__0eng__data__{s}.jsonl'] for s in SUFFIXES}
        assert all(len(new_source[s])==120 for s in SUFFIXES)
        assert all(r['vi'] is None for rows in new_source.values() for r in rows)
        keys=list(dict.fromkeys(PRE.sub('',r['en']) for s in SUFFIXES for r in new_source[s]))
        assert len(keys)==131,len(keys)
        missing=[(i,k) for i,k in enumerate(keys) if i not in T and k not in lookup]
        assert not missing,missing
        reuse_count=sum(i not in T for i in range(len(keys)))
        assert reuse_count==107, reuse_count
        trans={}
        for i,k in enumerate(keys):
            v=T[i] if i in T else lookup[k].most_common(1)[0][0]
            assert TOK.findall(k)==TOK.findall(v),('token',i,k,v,TOK.findall(k),TOK.findall(v))
            assert unicodedata.normalize('NFC',v)==v,('NFC',i,v)
            lens=[len(TOK.sub('',x)) for x in v.split('▼')]
            assert max(lens)<=34,('width',i,lens,v)
            assert len(lens)<=4,('breaks',i,v)
            assert not v.endswith((' ','\n','\r','\t')),('trailing whitespace',i,v)
            trans[k]=v
        changes=[];files={}
        for s,rows in new_source.items():
            translated=[]
            for row in rows:
                key=PRE.sub('',row['en'])
                pre=row['en'][:len(row['en'])-len(key)]
                vi=pre+trans[key]
                assert TOK.findall(row['en'])==TOK.findall(vi),(s,row['id'])
                new=dict(row,vi=vi)
                translated.append(new)
                changes.append(dict(new,file=f'translation/04-thoai/talkfigs__0eng__data__{s}.jsonl'))
            path=f'translation/04-thoai/talkfigs__0eng__data__{s}.jsonl'
            files[path]=''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n' for x in translated)
            sid=s.replace('.','_')
            files[f'manual_{sid}.tsv']='id\ten\tvi\tctx\n'+''.join('\t'.join((r['id'],r['en'],r['vi'],str(r.get('ctx',''))))+'\n' for r in translated)
            files[f'vi_{sid}.txt']=''.join(r['vi']+'\n' for r in translated)
        files['DELTA-070.jsonl']=''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in changes)
        for s in NEXT:
            p=f'translation/04-thoai/talkfigs__0eng__data__{s}.jsonl'
            assert p in old_rows and len(old_rows[p])==120 and all(r['vi'] is None for r in old_rows[p]),('Next batch missing',s)
        files['CHECKPOINT-2026-11-09-DOT-70.md']="""# Magician's Quest: Mysterious Times — checkpoint 070

- Ngày: 09/11/2026
- Tổng tiến độ: **18.852 / 55.976 (33,68%)**, tăng **240** so với checkpoint 069.
- Hội thoại NPC: **15.727 / 52.608**.
- Phạm vi: `0041.015` và `0041.016` (120 trang/tệp).
- 131 mẫu câu EN (bỏ mã tiền tố): **107 mẫu tái dùng** theo EN khớp hoàn toàn từ các bản dịch trước, **20 mẫu mới** và **4 mẫu đã có nhưng phải sửa lỗi nhân đôi token** trong lần xuất hiện cũ. Không thay bản dịch cũ.
- Phong cách: giọng NPC bạn bè tớ–cậu, tự nhiên dí dỏm, không lạm dụng meme; thuật ngữ kỳ bí nhất quán.
- Giữ nguyên các mã `$...;`, `▼`, ID, EN và CTX; chỉ điền trường `vi` còn trống.
- QA: toàn bộ 501 JSONL / 55.976 mục so với 069, chỉ bổ sung đúng 240 trường `vi`; giữ nguyên 18.612 bản dịch cũ.
- Đã kiểm tra Unicode NFC, token, tối đa 34 ký tự tĩnh mỗi đoạn, không quá 3 dấu `▼` trên trang.
- Chưa kiểm thử trên ROM Nintendo DS; độ rộng khi thay biến tên động vẫn cần thử thực tế.
- Nguồn tiếp: `0041.017` và `0041.018` (120 trang/tệp, `vi: null`).
"""
        # Apply source + documentation changes to an in-memory copy.
        new_entries=dict(old_entries)
        for p,s in files.items():new_entries[p]=s.encode('utf-8')
        intro=f'**Checkpoint mới nhất: 070 (09/11/2026) — 18.852/55.976 (33,68%).** Tăng 240 thoại NPC qua `0041.015`–`0041.016`. Xem `CHECKPOINT-2026-11-09-DOT-70.md`, `QA-070.md`, `DELTA-070.jsonl`. Nguồn 071: `0041.017`, `0041.018`.\n\n'
        handoff=f'## Checkpoint 070 — 09/11/2026\n\n- Đã dịch `0041.015` + `0041.016`: +240 trang (18.852/55.976; 33,68%).\n- 107 mẫu EN tái sử dụng bản dịch cũ, 20 mẫu mới, 4 mẫu chỉnh token khi áp dụng lại; thống nhất tớ–cậu và mã NDS.\n- QA so sánh 501 JSONL: giữ 18.612 `vi` cũ, chỉ thêm 240; không thay ID, EN, CTX.\n- ZIP đầy đủ trong Thư viện `/Dịch giả lập/MagiciansQuest-VietHoa-Checkpoint-070.zip`.\n- Chưa thử trên ROM. Tiếp `0041.017` và `0041.018` (2×120 trang).\n\n'
        new_entries['README.md']=(intro+old_entries['README.md'].decode('utf-8')).encode('utf-8')
        new_entries['BAN_GIAO.md']=(handoff+old_entries['BAN_GIAO.md'].decode('utf-8')).encode('utf-8')
        total=old_total=0;diff=[]; errors=[]
        for p in jsonl_paths:
            old=old_rows[p];new=[json.loads(x) for x in new_entries[p].decode('utf-8').splitlines()]
            if len(old)!=len(new):errors.append(('count',p));continue
            for i,(a,b) in enumerate(zip(old,new)):
                if (a['id'],a['en'],a.get('ctx'))!=(b['id'],b['en'],b.get('ctx')):errors.append(('core changed',p,i))
                old_total+=a['vi'] is not None
                total+=b['vi'] is not None
                if a['vi']!=b['vi']:
                    diff.append((p,i))
                    if a['vi'] is not None or not p.endswith(('0041.015.jsonl','0041.016.jsonl')):
                        errors.append(('unexpected change',p,i))
                    elif TOK.findall(b['en'])!=TOK.findall(b['vi']):errors.append(('tokens',p,i))
                    elif unicodedata.normalize('NFC',b['vi'])!=b['vi']:errors.append(('NFC',p,i))
                    elif len(b['vi'].split('▼'))>4 or max(len(TOK.sub('',s)) for s in b['vi'].split('▼'))>34:errors.append(('width',p,i))
        assert old_total==18612,old_total
        assert total==18852,total
        assert len(diff)==240,len(diff)
        assert not errors,errors[:20]
        qa=f"""# QA checkpoint 070

- **PASS**: {len(jsonl_paths)} JSONL / 55.976 bản ghi.
- So sánh checkpoint 069 → 070: **18.612 → 18.852**, đúng **240** `vi` mới.
- Chỉ sửa `vi` của `0041.015` (120) và `0041.016` (120). Các `vi` cũ, ID, EN và CTX giữ nguyên.
- Đã rà 131 mẫu câu phân biệt: 107 mẫu trùng EN tái dùng bản dịch trước; 20 mẫu EN mới dịch thủ công; 4 mẫu cũ tái biên tập để tránh lặp token.
- Đã so khớp thứ tự token `$...;`, Unicode NFC, mỗi đoạn thoại tối đa 34 ký tự tĩnh (loại trừ token), tối đa 3 ngắt trang `▼`.
- Hai tệp đợt 071 còn nguyên 120 bản ghi/tệp, `vi: null`.
- **Giới hạn**: Chưa kiểm thử ROM NDS hoặc độ rộng mở rộng của biến tên nhân vật.
"""
        new_entries['QA-070.md']=qa.encode('utf-8')
        # The script is included in the archive for reproducible generation.
        script_path=pathlib.Path(__file__)
        new_entries['mq070_translate.py']=script_path.read_bytes()
        with zipfile.ZipFile(OUT,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as target:
            for p,b in sorted(new_entries.items()):target.writestr(ROOT+p,b)
        with zipfile.ZipFile(OUT) as target:
            assert target.testzip() is None
            assert len([n for n in target.namelist() if n.endswith('.jsonl') and '/translation/' in n])==501
            nfiles=len(target.namelist())
        print('PASS: output',OUT,'bytes',OUT.stat().st_size,'files',nfiles,
            'SHA256',hashlib.sha256(OUT.read_bytes()).hexdigest(), 'changed',len(diff))
        print('UNIQUE',len(keys),'reused',reuse_count,'new',len(T),'total translated',total)

if __name__=='__main__':process()
