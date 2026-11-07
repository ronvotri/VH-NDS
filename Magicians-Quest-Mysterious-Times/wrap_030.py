from pathlib import Path
import re,json,unicodedata
R=Path(__file__).resolve().parent
TOK=re.compile(r"\$\d+(?:'[-\d]+)*;")
LEAD=re.compile(r"^(?:\$(?:034|024|023|022|040)'[-\d]+(?:'[-\d]+)*;)+")
TAIL=re.compile(r"(?:\$\d+(?:'[-\d]+)*;)+$")
def visible(x): return len(TOK.sub('',x))
def wrap(s,limit=32):
    words=s.strip().split()
    lines=[];cur=''
    for w in words:
        trial=(cur+' '+w).strip() if cur else w
        if cur and visible(trial)>limit:
            lines.append(cur);cur=w
        else:cur=trial
    if cur:lines.append(cur)
    return '▼'.join(lines)
for n,expected in [('0028.003',120),('0028.004',120)]:
    raw=(R/f'vi_{n.replace(".","_")}_raw.txt').read_text('utf8').splitlines()
    src=[json.loads(l) for l in (R/f'translation/04-thoai/talkfigs__0eng__data__{n}.jsonl').read_text('utf8').splitlines()]
    assert len(raw)==len(src)==expected
    out=[];issues=[]
    for i,(line,row) in enumerate(zip(raw,src)):
        s=row['en'];p=LEAD.match(s);prefix=p.group(0) if p else ''
        t=TAIL.search(s);suffix=t.group(0) if t and t.start()>len(prefix) else ''
        vi=prefix+wrap(line)+suffix
        vi=unicodedata.normalize('NFC',vi)
        if TOK.findall(vi)!=TOK.findall(s):issues.append((i,'TOK',TOK.findall(s),TOK.findall(vi)))
        if vi.count('▼')>3: issues.append((i,'PAGES',vi.count('▼'),vi))
        if any(visible(chunk)>34 for chunk in vi.split('▼')):issues.append((i,'WIDTH',vi))
        if any(c in vi for c in '\t\r\n'):issues.append((i,'WHITESPACE',vi))
        out.append(wrap(line))
    (R/f'vi_{n.replace(".","_")}.txt').write_text('\n'.join(out)+'\n','utf8')
    print(n,'issues',len(issues),'lineMax',max([len(TOK.sub('',l)) for v in out for l in v.split('▼')]),'pageMax',max(v.count('▼') for v in out))
    for x in issues:print(x)