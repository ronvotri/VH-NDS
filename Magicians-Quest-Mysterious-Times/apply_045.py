#!/usr/bin/env python3
"""Checkpoint 045: compile authored VI scripts and replace only new vi fields.

The `¤` positions in a source translation explicitly mark where source control-token
runs inside the visible text must be reinserted. Edge token runs are retained
without markers. Abort on any token mismatch rather than silently deleting code.
"""
from pathlib import Path
import json,re,unicodedata
ROOT=Path(__file__).resolve().parent
STAGE=ROOT
TOKEN=re.compile(r"\$[0-9'\-]+;")
TARGET=['0033.008','0033.009']

def fmt_visible(s):return len(TOKEN.sub('',s))

def merge_codes(en,txt):
    txt=txt.strip()
    # Prefix tokens and suffix token-run are preserved exactly.
    pref=re.match(r"(?:\$[0-9'\-]+;)*",en).group()
    middle=en[len(pref):]
    suffmatch=re.search(r"(?:\$[0-9'\-]+;)+$",middle)
    suff=suffmatch.group() if suffmatch else ''
    if suff:middle=middle[:-len(suff)]
    groups=re.findall(r"(?:\$[0-9'\-]+;)+",middle)
    pieces=txt.split('¤')
    if len(pieces)-1!=len(groups):
        raise ValueError(f'marker mismatch: {len(pieces)-1} vs {len(groups)} internal groups in {en!r}: {txt!r}')
    core=pieces[0]+''.join(group+piece for group,piece in zip(groups,pieces[1:]))
    return pref+core+suff

def wrap(s,limit=34):
    # Input has no display breaks; wrap by Vietnamese word boundaries.
    # Game control sequences contribute 0 visible glyphs.
    words=s.split(' ')
    lines=[];current=''
    for word in words:
        if not word: continue
        candidate=current+' '+word if current else word
        if fmt_visible(candidate)>limit and current:
            lines.append(current);current=word
        else:current=candidate
        if fmt_visible(current)>limit:
            raise ValueError(f'Word/segment exceeds {limit} chars: {current!r}')
    if current: lines.append(current)
    if len(lines)>4:
        raise ValueError(f'Too many lines ({len(lines)}) for {s!r}: {lines!r}')
    return '▼'.join(lines)

def run():
    updates=[]
    for id in TARGET:
        path=ROOT/'translation'/'04-thoai'/f'talkfigs__0eng__data__{id}.jsonl'
        rows=[json.loads(s) for s in path.read_text('utf8').splitlines()]
        vi=(STAGE/f'vi_{id.replace(".","_")}_raw.txt').read_text('utf8').splitlines()
        assert len(rows)==len(vi)==120,(id,len(rows),len(vi))
        for idx,(row,new) in enumerate(zip(rows,vi),1):
            if row.get('vi') and row['vi']!=wrap(merge_codes(row['en'],new)):
                raise ValueError(f'Existing translation differs: {id}:{idx}')
            try:
                trans=wrap(merge_codes(row['en'],new))
                assert TOKEN.findall(row['en'])==TOKEN.findall(trans)
                assert trans.count('▼')<=3
                assert all(fmt_visible(x)<=34 for x in trans.split('▼'))
                assert unicodedata.normalize('NFC',trans)==trans
                assert not any(c in trans for c in '\n\r\t')
                if 'max_utf8_bytes' in row and row['max_utf8_bytes'] is not None:
                    assert len(trans.encode('utf8'))<=row['max_utf8_bytes']
            except Exception as e:
                print('PROBLEM',id,idx,str(e))
                continue
            row['vi']=trans
            updates.append({'file':'04-thoai/'+path.name,'id':row['id'],'en':row['en'],'old_vi':None,'vi':trans,'ctx':row.get('ctx')})
        if any(not r.get('vi') for r in rows):
            print('NOT WRITING INCOMPLETE',id,'missing',[(i+1) for i,r in enumerate(rows) if not r.get('vi')]);
            continue
        path.write_text('\n'.join(json.dumps(x,ensure_ascii=False,separators=(',',':')) for x in rows)+'\n','utf8')
        (ROOT/f'vi_{id.replace(".","_")}.txt').write_text('\n'.join(x['vi'] for x in rows)+'\n','utf8')
        (ROOT/f'vi_{id.replace(".","_")}_raw.txt').write_text('\n'.join(vi)+'\n','utf8')
        with (ROOT/f'manual_{id.replace(".","_")}.tsv').open('w',encoding='utf8') as f:
            f.write('id\ten\tvi\tctx\n')
            for row in rows: f.write('\t'.join(str(row.get(k) or '') for k in ['id','en','vi','ctx'])+'\n')
    if len(updates)==240:
        (ROOT/'DELTA-045.jsonl').write_text('\n'.join(json.dumps(x,ensure_ascii=False,separators=(',',':')) for x in updates)+'\n','utf8')
        print('COMPILED ALL 240')
    else:print('COMPILED ONLY',len(updates),'of 240. Fix issues and run again.')
if __name__=='__main__':run()