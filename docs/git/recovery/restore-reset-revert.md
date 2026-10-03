# Git restore·reset·revert 선택

> 복구 명령은 파일·스테이징·브랜치 이력 중 무엇을 되돌릴지 먼저 정해 선택한다.

- restore는 작업 트리나 인덱스의 파일 내용을 복원한다.
- reset은 사용 형태와 옵션에 따라 인덱스·브랜치·작업 트리를 바꾼다.
- revert는 기존 변경을 취소하는 새 커밋을 만든다.

<details>
<summary>설명과 꼬리질문 펼치기</summary>

## 설명

아직 커밋하지 않은 파일의 변경을 버릴 때는 git restore 파일을, 스테이징만 해제할 때는 git restore --staged 파일을 검토한다. 파일을 지정하는 reset과 커밋을 지정하는 reset도 구별한다. git reset --soft HEAD~1은 브랜치 끝을 옮기면서 인덱스·작업 트리를 유지하고, --mixed는 인덱스도 바꾼다. --hard는 작업 트리의 추적 파일까지 바꾸므로 저장하지 않은 변경을 잃을 수 있다.

공유한 커밋의 효과를 취소할 때는 git revert 커밋처럼 새 취소 커밋을 만드는 방법을 먼저 검토한다. 이전 커밋을 찾아야 한다면 git log와 git reflog로 참조 이동 기록을 확인한다.

## 주의점

먼저 git status·diff를 확인하고 필요한 변경을 보존한다. reflog는 모든 미커밋 파일 내용을 보관하는 백업이 아니며 revert에도 충돌이 날 수 있다.

## 꼬리질문

1. 파일 내용은 유지하고 스테이징만 해제하려면 어느 영역을 바꿔야 할까?
2. 커밋 전 상태를 보존하려는 상황에서 --soft와 --hard는 어떻게 다른가?
3. 동료가 이미 받은 커밋을 취소할 때 revert가 협업에 유리한 이유는 무엇일까?

</details>

## 참고 자료

- [Git · restore](https://git-scm.com/docs/git-restore) — 작업 트리·인덱스 복원 옵션을 비교한다.
- [Git · reset](https://git-scm.com/docs/git-reset) — 경로 지정과 커밋 지정 형태, 각 모드의 변경 영역을 확인한다.
- [Git · revert](https://git-scm.com/docs/git-revert) — 취소 커밋·충돌·공유 이력에서의 사용법을 읽는다.
