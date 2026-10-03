"""Publication tests use an in-memory GitHub; no network or user drafts are modified."""
import base64
from contextlib import redirect_stdout
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

SPEC=importlib.util.spec_from_file_location('archive',Path(__file__).resolve().parents[1]/'scripts/archive.py')
a=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(a)
CATEGORIES=[{'slug':'java-concurrency','title':'Java 병렬 프로그래밍','sections':{'memory-model':'가시성·원자성'}}]
TOPIC='java-concurrency/memory-model/volatile'
PATH='docs/'+TOPIC+'.md'
NOTE='''# volatile

> 가시성과 복합 연산의 원자성을 구분한다.

- 증가 연산은 별도 보호한다.

<details>
<summary>설명</summary>

volatile count++는 원자적이지 않다.

## Java 예제

```java
volatile int count;
void increment() { count++; }
```

## 꼬리질문

1. count++가 왜 복합 연산인가?
2. 두 스레드가 같은 값을 읽으면 어떤 증가를 잃는가?
3. 두 변수 사이 불변식을 보호하려면 어떤 경계가 필요한가?

</details>

## 참고 자료

- [JLS](https://docs.oracle.com/javase/specs/jls/se21/html/jls-17.html) — 보장 범위를 확인한다.
'''

class FakeGitHub:
    def __init__(self):
        self.files={'categories.json':json.dumps(CATEGORIES),'user-note.txt':'사용자가 작성한 파일\n'}
        self.blobs={};self.trees={};self.commits={};self.posted_commits=0;self.patch_calls=[];self.race=None
        self.install()
    def install(self):
        for content in self.files.values():self.blobs[a.blob_sha(content)]=content
        tree={p:a.blob_sha(c) for p,c in self.files.items()};key='tree'+str(len(self.trees));self.trees[key]=tree
        self.head='head'+str(len(self.commits));self.commits[self.head]={'tree':{'sha':key}}
    def call(self,endpoint,method='GET',payload=None):
        if endpoint.startswith('git/ref/'):return {'object':{'sha':self.head}}
        if endpoint.startswith('git/commits/') and method=='GET':return self.commits[endpoint.split('/')[-1]]
        if endpoint.startswith('git/trees/') and method=='GET':
            t=self.trees[endpoint.split('/')[-1].split('?')[0]]
            return {'tree':[{'path':p,'sha':s,'type':'blob'} for p,s in t.items()]}
        if endpoint.startswith('git/blobs/'):
            content=self.blobs[endpoint.split('/')[-1]];return {'content':base64.b64encode(content.encode()).decode()}
        if endpoint=='git/blobs':
            sha=a.blob_sha(payload['content']);self.blobs[sha]=payload['content'];return {'sha':sha}
        if endpoint=='git/trees':
            t=dict(self.trees[payload['base_tree']]);t.update({x['path']:x['sha'] for x in payload['tree']})
            key='tree'+str(len(self.trees));self.trees[key]=t;return {'sha':key}
        if endpoint=='git/commits':
            self.posted_commits+=1;key='commit'+str(len(self.commits));self.commits[key]={'tree':{'sha':payload['tree']},'parents':payload['parents']};return {'sha':key}
        if endpoint.startswith('git/refs/'):
            self.patch_calls.append(payload)
            if self.race:
                mode=self.race;self.race=None
                if mode=='document':self.files[PATH]=NOTE.replace('별도 보호','최신 원격에서 추가 보호')
                else:self.files['user-new.txt']='동시 원격 변경\n'
                self.install();raise a.ArchiveError('non-fast-forward')
            commit=self.commits[payload['sha']]
            if commit['parents'][0]!=self.head:raise a.ArchiveError('non-fast-forward')
            self.head=payload['sha'];self.files={p:self.blobs[s] for p,s in self.trees[commit['tree']['sha']].items()};return {}
        raise AssertionError((endpoint,method))

class ArchiveTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.state=Path(self.temp.name);self.remote=FakeGitHub()
        self.mock=patch.object(a,'api',self.remote.call);self.mock.start()
    def tearDown(self):self.mock.stop();self.temp.cleanup()
    def draft(self,session='chat-a',content=NOTE,verified=True,base=None,unknown=False):
        dest=self.state/'pending'/session/(TOPIC.replace('/','-')+'.json')
        a.atomic_json(dest,{'session':session,'topic':TOPIC,'content':content,'verified':verified,'base_sha':base,'base_unknown':unknown});return dest
    def publish(self,session='chat-a',all_sessions=False,dry=False):
        with redirect_stdout(io.StringIO()) as out:a.publish(self.state,session,all_sessions,dry)
        return json.loads(out.getvalue())
    def test_question_stages_without_publication(self):
        file=self.state/'note.md';file.write_text(NOTE)
        argv=['archive','--state-dir',str(self.state),'stage','--session','chat-a','--topic',TOPIC,'--file',str(file)]
        with patch.object(sys,'argv',argv),redirect_stdout(io.StringIO()):a.main()
        self.assertEqual(len(a.pending_records(self.state,'chat-a')),1);self.assertEqual(self.remote.posted_commits,0)
    def test_preview_and_current_chat_publish_are_atomic(self):
        selected=self.draft();other=self.draft('chat-b')
        result=self.publish(dry=True);self.assertEqual(result['status'],'preview');self.assertTrue(selected.exists());self.assertEqual(self.remote.posted_commits,0)
        result=self.publish();self.assertEqual(result['status'],'published');self.assertEqual(self.remote.posted_commits,1)
        self.assertFalse(selected.exists());self.assertTrue(other.exists());self.assertEqual(self.remote.files[PATH],NOTE)
        self.assertIn('volatile',self.remote.files['README.md']);self.assertIn('가시성',self.remote.files['docs/java-concurrency/README.md']);self.assertEqual(self.remote.files['user-note.txt'],'사용자가 작성한 파일\n')
        self.assertNotIn('CONTRIBUTING.md',self.remote.files['README.md']);self.assertNotIn('LEARNING_PATH.md',self.remote.files['README.md'])
    def test_same_topic_same_content_does_not_commit(self):
        self.draft();self.publish();count=self.remote.posted_commits
        self.draft(base=a.blob_sha(NOTE));result=self.publish();self.assertEqual(result['status'],'unchanged');self.assertEqual(count,self.remote.posted_commits)
    def test_exclusion_discards_current_topic_only(self):
        target=self.draft();other=self.draft('chat-b')
        argv=['archive','--state-dir',str(self.state),'discard','--session','chat-a','--topic',TOPIC]
        with patch.object(sys,'argv',argv),redirect_stdout(io.StringIO()):a.main()
        self.assertFalse(target.exists());self.assertTrue(other.exists());self.assertEqual(self.remote.posted_commits,0)
    def test_unverified_draft_is_preserved(self):
        path=self.draft(verified=False)
        with self.assertRaises(a.ArchiveError):self.publish()
        self.assertTrue(path.exists());self.assertEqual(self.remote.posted_commits,0)
    def test_auth_failure_preserves_draft(self):
        path=self.draft()
        with patch.object(a,'api',side_effect=a.ArchiveError('authentication failed')):
            with self.assertRaises(a.ArchiveError):self.publish()
        self.assertTrue(path.exists())
    def test_offline_stage_preserves_new_draft(self):
        file=self.state/'note.md';file.write_text(NOTE)
        argv=['archive','--state-dir',str(self.state),'stage','--session','chat-a','--topic',TOPIC,'--file',str(file)]
        with patch.object(sys,'argv',argv),patch.object(a,'snapshot',side_effect=FileNotFoundError('gh')),redirect_stdout(io.StringIO()):a.main()
        records=a.pending_records(self.state,'chat-a');self.assertEqual(len(records),1);self.assertTrue(records[0][1]['base_unknown'])
        with self.assertRaises(a.ArchiveError):self.publish()
    def test_unrelated_remote_race_retries_once_preserving_change(self):
        self.draft();self.remote.race='unrelated';self.publish()
        self.assertEqual(len(self.remote.patch_calls),2);self.assertTrue(all(x['force'] is False for x in self.remote.patch_calls));self.assertEqual(self.remote.files['user-new.txt'],'동시 원격 변경\n')
    def test_document_race_preserves_both_and_can_merge_once(self):
        path=self.draft();self.remote.race='document'
        with self.assertRaises(a.ArchiveError):self.publish()
        latest=self.remote.files[PATH];self.assertTrue(path.exists());self.assertIn('최신 원격',latest)
        merged=latest.replace('원자적이지 않다.','원자적이지 않다. 추가 설명을 보존했다.')
        self.draft(content=merged,base=a.blob_sha(latest));self.publish();self.assertEqual(self.remote.files[PATH],merged)
    def test_all_chat_duplicate_conflict_is_visible_and_preserved(self):
        first=self.draft();second=self.draft('chat-b',NOTE.replace('별도 보호','다르게 보호'))
        self.assertEqual(len(a.pending_records(self.state,all_sessions=True)),2)
        with self.assertRaises(a.ArchiveError):self.publish(all_sessions=True)
        self.assertTrue(first.exists());self.assertTrue(second.exists());self.assertEqual(self.remote.posted_commits,0)
    def test_all_identical_topics_publish_one_document(self):
        one=self.draft();two=self.draft('chat-b');self.publish(all_sessions=True)
        self.assertFalse(one.exists());self.assertFalse(two.exists());self.assertEqual(self.remote.posted_commits,1)
    def test_rejects_private_paths_and_wrong_category(self):
        with self.assertRaises(a.ArchiveError):a.note_meta(PATH,NOTE.replace('count++','/Users/private/secret'))
        with self.assertRaises(a.ArchiveError):a.topic_path('../../escape',CATEGORIES)
    def test_old_format_is_not_published_and_draft_is_preserved(self):
        old=NOTE.replace('## 꼬리질문','## 복습 질문')
        path=self.draft(content=old)
        with self.assertRaises(a.ArchiveError):self.publish()
        self.assertTrue(path.exists());self.assertEqual(self.remote.posted_commits,0)

if __name__=='__main__':unittest.main()
