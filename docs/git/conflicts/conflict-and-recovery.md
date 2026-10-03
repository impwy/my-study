# 충돌 해결과 변경 보존

> 충돌한 양쪽의 의도를 읽어 통합하고 되돌리기 전에 현재 변경을 보존한다.

- 충돌 표식 제거만으로 해결되지 않는다.
- diff와 status로 해결 범위를 확인한다.
- 복구 명령의 작업 트리 영향을 확인한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

충돌은 같은 구간의 변경을 자동으로 결정하지 못한 상태다. 한쪽을 기계적으로 선택하기보다 최신 요구와 양쪽 의도를 읽고 결과를 작성한다. 해결 뒤 실행·문서 링크·목록을 확인하고 다음 단계를 진행한다. abort·restore·reset 등은 서로 다른 상태를 바꾸므로 미커밋 변경의 손실 가능성을 확인한다. 필요하면 먼저 파일 복사·커밋·stash로 보존한다.

## Java 예제

미해결 충돌과 로컬 참조 이동을 조회한다. 복구·삭제 명령은 실행하지 않는다.

```java
static void inspect() throws Exception {
    new ProcessBuilder("git", "diff", "--name-only", "--diff-filter=U")
            .inheritIO()
            .start()
            .waitFor();
    new ProcessBuilder("git", "reflog", "-5", "--oneline").inheritIO().start().waitFor();
}
```

## 주의점

reset --hard를 일상적인 충돌 해결로 사용하지 않는다. reflog로 찾을 수 있는 커밋과 아직 커밋하지 않은 파일의 복구 가능성은 다르다.

## 꼬리질문

1. 충돌한 파일에서 “ours”를 고르면 어떤 상대 변경을 잃을 수 있는가?
2. 충돌 표시가 사라진 것과 두 변경의 업무 의도가 모두 보존된 것은 어떻게 다를까?
3. reflog에서 찾은 이전 커밋을 복구할 때 reset보다 새 브랜치로 확인하는 방식은 무엇을 보존할까?

</details>

## 참고 자료

- [Pro Git · 무료 공식 교재](https://git-scm.com/book/ko/v2) — 필요한 브랜치·병합·복구 장에서 명령의 의미를 확인한다.
