# merge와 rebase

> merge는 이력을 합치는 커밋을 만들 수 있고 rebase는 커밋을 새 기반에 다시 적용한다.

- merge는 두 갈래의 관계를 보존한다.
- rebase는 커밋 ID를 바꿀 수 있다.
- 공유 이력은 재작성 영향을 고려한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

갈라진 브랜치를 merge하면 공통 조상과 두 끝의 변경을 합쳐 결과를 만든다. fast-forward가 가능하면 참조만 이동할 수도 있다. rebase는 자신의 커밋을 다른 기반 위에 다시 적용하므로 부모·커밋 ID가 달라질 수 있다. 깔끔한 선형 이력과 기존 공유 참조의 보존은 각각의 비용이 있다. 협업 중 이미 공유한 커밋을 다시 쓰는 정책은 팀 규칙을 따른다.

## Java 예제

현재 저장소의 기록을 읽는다. merge·rebase는 예제에서 실행하지 않는다.

```java
static int graph() throws Exception {
    return new ProcessBuilder("git", "log", "--graph", "--oneline", "--decorate", "-10")
            .inheritIO()
            .start()
            .waitFor();
} // merge의 두 부모와 rebase 후 다시 만들어진 선형 커밋을 비교
```

## 주의점

rebase가 충돌을 자동 없애거나 merge보다 항상 안전한 것은 아니다. 충돌한 파일의 의미를 읽고 통합한다.

## 꼬리질문

1. rebase 뒤 내용이 같아도 커밋 ID가 달라질 수 있는 이유는?
2. merge commit의 부모가 두 개인 것과 rebase가 새 커밋을 만드는 것은 기록에서 어떻게 보일까?
3. 다른 사람이 사용하는 브랜치를 rebase한 뒤 일반 push가 거절되면 어떤 공유 기록 문제를 먼저 확인할까?

</details>

## 참고 자료

- [Pro Git · 무료 공식 교재](https://git-scm.com/book/ko/v2) — 필요한 브랜치·병합·복구 장에서 명령의 의미를 확인한다.
