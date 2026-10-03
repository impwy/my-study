#!/usr/bin/env python3
"""Private drafts and atomic GitHub study-note publication. Requires Python 3 and gh."""
import argparse
import base64
from contextlib import contextmanager
from datetime import datetime
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import quote

REPO = 'impwy/my-study'
BRANCH = 'main'
DEFAULT_STATE = Path(os.environ.get('CODEX_HOME',str(Path.home()/'.codex'))) / 'archives' / 'my-study'

class ArchiveError(Exception): pass

def blob_sha(content):
    data=content.encode('utf-8')
    return hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()

def api(endpoint, method='GET', payload=None):
    command=['gh','api',f'repos/{REPO}/{endpoint}','--method',method]
    if payload is not None: command+=['--input','-']
    p=subprocess.run(command,input=json.dumps(payload) if payload is not None else None,text=True,capture_output=True)
    if p.returncode:
        raise ArchiveError(p.stderr.strip() or 'GitHub 요청 실패')
    return json.loads(p.stdout) if p.stdout.strip() else {}

def load_json(path, default):
    return json.loads(path.read_text(encoding='utf-8')) if path.exists() else default

def atomic_json(path,data):
    path.parent.mkdir(parents=True,exist_ok=True,mode=0o700)
    temp=path.with_suffix(path.suffix+'.tmp')
    temp.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    temp.chmod(0o600)
    temp.replace(path)

@contextmanager
def locked(state):
    state.mkdir(parents=True,exist_ok=True,mode=0o700)
    with (state/'lock').open('a') as handle:
        fcntl.flock(handle,fcntl.LOCK_EX)
        yield

def topic_path(topic,categories):
    parts=topic.split('/')
    if len(parts)!=3 or not all(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',p) for p in parts):
        raise ArchiveError('주제는 category/subcategory/topic 형식의 소문자·숫자·하이픈이어야 합니다.')
    category=next((c for c in categories if c['slug']==parts[0]),None)
    if category is None or parts[1] not in category['sections']:
        raise ArchiveError('등록되지 않은 대분류·소분류입니다. categories.json을 확인하세요.')
    return 'docs/'+topic+'.md'

def note_meta(path,content):
    outside_code=re.sub(r'(?ms)^```[^\n]*\n.*?^```\s*$', '',content)
    title=re.search(r'^# (.+)$',outside_code,re.M)
    summary=re.search(r'^> (.+)$',outside_code,re.M)
    if not title or not summary: raise ArchiveError(f'{path}: 제목과 한 줄 요약이 필요합니다.')
    if '<details>' not in content or '</details>' not in content or '## 참고 자료' not in content:
        raise ArchiveError(f'{path}: 접기 영역과 참고 자료가 필요합니다.')
    if content.count('<details>')!=1 or content.count('</details>')!=1 or content.index('</details>')<content.index('<details>'):
        raise ArchiveError(f'{path}: 접기 영역은 한 개여야 합니다.')
    details=content.split('<details>',1)[1].split('</details>',1)[0]
    if not re.search(r'(?ms)^```java\s*\n\S.*?^```\s*$',details):
        raise ArchiveError(f'{path}: 접기 영역에 Java 코드 예제가 필요합니다.')
    questions=re.search(r'(?ms)^## 꼬리질문\s*\n(.*?)(?=^## |</details>|\Z)',outside_code)
    if not questions or re.findall(r'^(\d+)\. .+',questions.group(1),re.M)!=['1','2','3']:
        raise ArchiveError(f'{path}: 꼬리질문은 1·2·3번으로 세 개 작성합니다.')
    if re.search(r'^자료\s*구분\s*:|honglab\.co\.kr',content,re.M|re.I):
        raise ArchiveError(f'{path}: 제외한 자료 구분 줄·출처가 있습니다.')
    if len(re.findall(r'^- ',content.split('<details>',1)[0],re.M))>3:
        raise ArchiveError(f'{path}: 핵심 사항은 최대 3개입니다.')
    if content.index('## 참고 자료')<content.index('</details>'):
        raise ArchiveError(f'{path}: 참고 자료는 접기 영역 아래에 둡니다.')
    references=content.rsplit('## 참고 자료',1)[1]
    if not re.search(r'\]\(https?://[^)]+\)',references): raise ArchiveError(f'{path}: 공개 참고 링크가 필요합니다.')
    if 'example.com' in references or re.search(r'/Users/|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|\b(?:AKIA|ASIA)[A-Z0-9]{16}\b|\bgh[pousr]_[A-Za-z0-9]{25,}',content):
        raise ArchiveError(f'{path}: 자리표시자 또는 공개할 수 없는 개인 경로·키가 있습니다.')
    return {'title':title.group(1).strip(),'summary':summary.group(1).strip(),'content_sha':blob_sha(content)}

def escaped(value):
    return value.replace('|','&#124;').replace('\n',' ').replace('[','\\[').replace(']','\\]')

def table(entries,base):
    if not entries: return '아직 정리된 문서가 없습니다.\n'
    lines=['| 문서 | 한 줄 요약 |','| --- | --- |']
    for path,item in sorted(entries.items(),key=lambda x:x[1]['title']):
        rel=os.path.relpath(path,base).replace(os.sep,'/')
        lines.append(f"| [{escaped(item['title'])}]({quote(rel,safe='/.-')}) | {escaped(item['summary'])} |")
    return '\n'.join(lines)+'\n'

def catalog_files(entries,categories):
    outputs={}
    intro='# my-study\n\n짧은 요약과 원문 링크로 남기는 기술 학습 기록.\n\n'
    root=intro+'## 분류\n\n| 카테고리 | 문서 | 소분류 |\n| --- | ---: | --- |\n'
    docs=intro+'## 분류\n\n| 카테고리 | 문서 |\n| --- | ---: |\n'
    for category in categories:
        slug=category['slug']
        group={p:e for p,e in entries.items() if p.startswith(f'docs/{slug}/')}
        root+=f"| [{category['title']}](docs/{slug}/README.md) | {len(group)} | {' · '.join(category['sections'].values())} |\n"
        docs+=f"| [{category['title']}]({slug}/README.md) | {len(group)} |\n"
        body=f"# {category['title']}\n\n[전체 목록](../../README.md)\n\n"
        for section,title in category['sections'].items():
            selected={p:e for p,e in group.items() if p.startswith(f'docs/{slug}/{section}/')}
            body+=f'## {title}\n\n'+table(selected,f'docs/{slug}')+'\n'
        outputs[f'docs/{slug}/README.md']=body
    root+='\n## 문서 목록\n\n'
    for category in categories:
        group={p:e for p,e in entries.items() if p.startswith(f"docs/{category['slug']}/")}
        if group:
            root+=f"<details>\n<summary>{category['title']} · {len(group)}개</summary>\n\n"+table(group,'.')+'\n</details>\n\n'
    outputs['README.md']=root
    outputs['docs/README.md']=docs
    outputs['catalog.json']=json.dumps(entries,ensure_ascii=False,indent=2,sort_keys=True)+'\n'
    return outputs

def snapshot(state):
    head=api(f'git/ref/heads/{BRANCH}')['object']['sha']
    commit=api(f'git/commits/{head}')
    tree=api(f"git/trees/{commit['tree']['sha']}?recursive=1")
    if tree.get('truncated'): raise ArchiveError('저장소 파일 목록이 잘렸습니다. 게시를 중단합니다.')
    paths={p['path']:p['sha'] for p in tree['tree'] if p['type']=='blob'}
    cache=state/'blobs'
    cache.mkdir(parents=True,exist_ok=True,mode=0o700)
    def read(path):
        sha=paths.get(path)
        if sha is None: return None
        cached=cache/sha
        if cached.exists(): return cached.read_text(encoding='utf-8')
        data=api('git/blobs/'+sha)
        content=base64.b64decode(data['content']).decode('utf-8')
        cached.write_text(content,encoding='utf-8')
        cached.chmod(0o600)
        return content
    return head,commit['tree']['sha'],paths,read

def current_catalog(paths,read):
    old=json.loads(read('catalog.json') or '{}')
    entries={}
    for path,sha in paths.items():
        if path.startswith('docs/') and path.endswith('.md') and not path.endswith('/README.md'):
            entries[path]=old[path] if path in old and old[path].get('content_sha')==sha else note_meta(path,read(path))
    return entries

def selected_pending(state,session=None,all_sessions=False):
    records=[]
    for path in sorted((state/'pending').glob('*/*.json')):
        record=load_json(path,{})
        if all_sessions or record.get('session')==session: records.append((path,record))
    by_topic={}
    for path,record in records:
        if record['topic'] in by_topic and by_topic[record['topic']][1]['content']!=record['content']:
            raise ArchiveError('서로 다른 대화에 같은 주제의 초안이 있습니다. 읽고 통합한 뒤 다시 게시하세요: '+record['topic'])
        by_topic[record['topic']]=(path,record)
    return records,by_topic

def pending_records(state,session=None,all_sessions=False):
    return [(p,load_json(p,{})) for p in sorted((state/'pending').glob('*/*.json')) if all_sessions or load_json(p,{}).get('session')==session]

def publish(state,session,all_sessions,dry_run):
    records,selected=selected_pending(state,session,all_sessions)
    if not records:
        print(json.dumps({'status':'no-pending'},ensure_ascii=False)); return
    for _,record in records:
        if not record.get('verified'): raise ArchiveError('출처 검증이 끝나지 않은 초안: '+record['topic'])
    for attempt in range(2):
        head,tree,paths,read=snapshot(state)
        categories=json.loads(read('categories.json') or '[]')
        entries=current_catalog(paths,read)
        changes={}
        for _,record in selected.values():
            path=topic_path(record['topic'],categories)
            sha=blob_sha(record['content'])
            if paths.get(path)==sha: continue
            if record.get('base_unknown') or paths.get(path)!=record.get('base_sha'):
                raise ArchiveError('원격 문서가 초안 작성 후 변경되었습니다. 최신 문서와 통합하세요: '+path)
            entries[path]=note_meta(path,record['content'])
            changes[path]=record['content']
        changes.update({p:c for p,c in catalog_files(entries,categories).items() if paths.get(p)!=blob_sha(c)})
        if dry_run:
            print(json.dumps({'status':'preview','repository':REPO,'paths':sorted(changes),'notes':len(selected)},ensure_ascii=False,indent=2)); return
        if not changes:
            for path,_ in records: path.unlink()
            print(json.dumps({'status':'unchanged','notes':len(selected)})); return
        objects=[]
        for path,content in changes.items():
            sha=api('git/blobs','POST',{'content':content,'encoding':'utf-8'})['sha']
            objects.append({'path':path,'mode':'100644','type':'blob','sha':sha})
        new_tree=api('git/trees','POST',{'base_tree':tree,'tree':objects})['sha']
        commit=api('git/commits','POST',{'message':f'docs: archive {len(selected)} study topics','tree':new_tree,'parents':[head]})['sha']
        try:
            api(f'git/refs/heads/{BRANCH}','PATCH',{'sha':commit,'force':False})
        except ArchiveError:
            if attempt==0 and api(f'git/ref/heads/{BRANCH}')['object']['sha']!=head: continue
            raise
        for path,_ in records: path.unlink()
        links=[f'https://github.com/{REPO}/blob/{BRANCH}/docs/{r["topic"]}.md' for _,r in selected.values()]
        print(json.dumps({'status':'published','commit':commit,'documents':links},ensure_ascii=False,indent=2)); return

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--state-dir',type=Path,default=DEFAULT_STATE)
    sub=parser.add_subparsers(dest='action',required=True)
    stage=sub.add_parser('stage')
    stage.add_argument('--file',type=Path,required=True)
    stage.add_argument('--topic',required=True)
    stage.add_argument('--session',required=True)
    stage.add_argument('--verified',action='store_true')
    stage.add_argument('--base-sha',help='SHA returned by show; use absent for a verified new topic')
    for action in ['pending','publish']:
        p=sub.add_parser(action)
        group=p.add_mutually_exclusive_group(required=True)
        group.add_argument('--session')
        group.add_argument('--all',action='store_true')
        if action=='publish': p.add_argument('--dry-run',action='store_true')
    show=sub.add_parser('show'); show.add_argument('--topic',required=True)
    discard=sub.add_parser('discard'); discard.add_argument('--session',required=True); discard.add_argument('--topic')
    catalog=sub.add_parser('catalog'); catalog.add_argument('--root',type=Path,required=True); catalog.add_argument('--dry-run',action='store_true')
    args=parser.parse_args()
    state=args.state_dir.resolve()
    with locked(state):
        if args.action=='catalog':
            categories=load_json(args.root/'categories.json',[])
            entries={p.relative_to(args.root).as_posix():note_meta(p.as_posix(),p.read_text(encoding='utf-8')) for p in (args.root/'docs').rglob('*.md') if p.name!='README.md'}
            outputs=catalog_files(entries,categories)
            if args.dry_run:
                changed=[p for p,c in outputs.items() if not (args.root/p).exists() or (args.root/p).read_text(encoding='utf-8')!=c]
                print(json.dumps({'status':'preview-local','notes':len(entries),'categories':len(categories),'index_changes':changed,'documents':sorted(entries)},ensure_ascii=False,indent=2))
            else:
                for path,content in outputs.items():
                    output=args.root/path; output.parent.mkdir(parents=True,exist_ok=True); output.write_text(content,encoding='utf-8')
                print(json.dumps({'status':'catalog','notes':len(entries)}))
        elif args.action=='stage':
            categories=load_json(Path(__file__).resolve().parents[1]/'references/categories.json',[])
            path=topic_path(args.topic,categories)
            content=args.file.read_text(encoding='utf-8')
            note_meta(path,content)
            session_key=hashlib.sha256(args.session.encode()).hexdigest()[:20]
            topic_key=hashlib.sha256(args.topic.encode()).hexdigest()[:20]
            dest=state/'pending'/session_key/(topic_key+'.json')
            previous=load_json(dest,{})
            base_unknown=False
            if args.base_sha is not None:
                if args.base_sha!='absent' and not re.fullmatch(r'[0-9a-f]{40}',args.base_sha):
                    raise ArchiveError('--base-sha는 show의 40자리 SHA 또는 absent여야 합니다.')
                base_sha=None if args.base_sha=='absent' else args.base_sha
            elif previous:
                base_sha=previous.get('base_sha'); base_unknown=previous.get('base_unknown',False)
            else:
                try: base_sha=snapshot(state)[2].get(path)
                except (ArchiveError,OSError): base_sha=None; base_unknown=True
            atomic_json(dest,{'session':args.session,'topic':args.topic,'content':content,'base_sha':base_sha,'base_unknown':base_unknown,'verified':args.verified,'updated_at':datetime.now().astimezone().isoformat()})
            print(json.dumps({'status':'staged','topic':args.topic,'file':str(dest)},ensure_ascii=False))
        elif args.action=='show':
            _,_,paths,read=snapshot(state)
            categories=json.loads(read('categories.json') or '[]')
            path=topic_path(args.topic,categories)
            pending=[r for _,r in pending_records(state,all_sessions=True) if r['topic']==args.topic]
            print(json.dumps({'path':path,'base_sha':paths.get(path),'content':read(path),'pending':pending},ensure_ascii=False,indent=2))
        elif args.action=='pending':
            records=pending_records(state,args.session,args.all)
            print(json.dumps([r for _,r in records],ensure_ascii=False,indent=2))
        elif args.action=='discard':
            records=pending_records(state,args.session,False)
            selected=[p for p,r in records if args.topic is None or r['topic']==args.topic]
            for path in selected: path.unlink()
            print(json.dumps({'status':'discarded','count':len(selected)}))
        elif args.action=='publish': publish(state,args.session,args.all,args.dry_run)

if __name__=='__main__':
    try: main()
    except (ArchiveError,OSError,json.JSONDecodeError) as error:
        print('Archive error: '+str(error),file=sys.stderr)
        sys.exit(1)
