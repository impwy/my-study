# 커밋·브랜치와 세 작업 영역

> 작업 트리·인덱스·커밋을 구분하고 브랜치를 커밋을 가리키는 이름으로 이해한다.

- add는 다음 커밋 내용을 준비한다.
- commit은 인덱스의 스냅샷을 기록한다.
- 브랜치는 이동하는 커밋 참조다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

파일을 수정하면 작업 트리가 바뀌고 add로 변경을 인덱스에 준비한다. 이후 commit은 그 인덱스의 내용을 기록한다. add 뒤 같은 파일을 더 수정하면 준비된 내용과 현재 파일이 다를 수 있다. 브랜치는 파일 복제본 폴더가 아니라 커밋을 가리키는 참조이며 새 커밋으로 이동한다. HEAD는 현재 체크아웃의 위치를 나타낸다.

## Java 예제

Git 저장소에서 실행하는 Java ProcessBuilder 예제이며 조회 명령만 사용한다.

```java
static void inspect() throws Exception {
    for (String[] args :
            new String[][] {
                {"diff", "--stat"}, {"diff", "--cached", "--stat"}, {"log", "-1", "--oneline"}
            }) {
        var command = new java.util.ArrayList<String>();
        command.add("git");
        command.addAll(java.util.List.of(args));
        new ProcessBuilder(command).inheritIO().start().waitFor();
    }
}
```

## 주의점

학습 자료의 개발·배포 명령을 근거로 정리한 기본 개념이다. 사용자의 모든 Git 사용 이력을 조사한 것으로 해석하지 않는다.

## 꼬리질문

1. add한 뒤 같은 파일을 수정하면 commit에는 어떤 버전이 들어가는가?
2. 첫 diff와 --cached diff는 각각 어떤 두 영역을 비교할까?
3. add 후 파일을 다시 수정하면 한 파일이 두 diff에 동시에 보일 수 있는 이유는 무엇일까?

</details>

## 참고 자료

- [Pro Git · 무료 공식 교재](https://git-scm.com/book/ko/v2) — 필요한 브랜치·병합·복구 장에서 명령의 의미를 확인한다.
