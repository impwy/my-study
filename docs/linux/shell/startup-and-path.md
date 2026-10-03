# 셸 초기화와 PATH

> 셸 종류·실행 모드에 맞는 설정 파일과 PATH 검색 순서를 확인한다.

- zshrc는 대화형 zsh의 설정이다.
- PATH는 명령 검색 경로의 순서다.
- Bash와 zsh의 초기화 규칙을 구분한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

대화형 셸·로그인 셸·스크립트 실행은 서로 다른 초기화 경로를 사용할 수 있다. macOS에서 zshrc에 둔 설정이 비대화형 배포 스크립트에 그대로 적용된다고 가정하지 않는다. PATH는 명령 이름을 찾는 순서를 정하므로 앞에 다른 실행 파일이 있으면 같은 명령도 다른 버전이 실행된다. 기존 PATH를 보존하고 추가 경로를 신뢰할 수 있는 위치로 제한한다.

## Java 예제

```java
static void demo() throws Exception {
    System.out.println(System.getenv("PATH"));
    Process child = new ProcessBuilder("/bin/sh", "-c", "command -v java").inheritIO().start();
    System.out.println(child.waitFor());
} // 고정된 명령만 사용; /bin/sh -c에 외부 입력을 문자열로 연결하지 않음
```

## 주의점

zsh 전용 설정을 Bash 스크립트에 복사하지 않는다. 공개 기록에는 개인 환경 파일의 키·접속 정보를 복사하지 않는다.

## 꼬리질문

1. 터미널에서는 실행되는 명령이 CI에서 안 보이면 어떤 초기화 차이를 확인할까?
2. 로그인 셸과 비로그인 CI 셸이 서로 다른 초기화 파일을 읽으면 PATH는 어떻게 달라질까?
3. 명령 이름 대신 절대 실행 경로를 쓰면 줄어드는 불확실성과 남는 환경 차이는 무엇일까?

</details>

## 참고 자료

- [Zsh · Startup Files](https://zsh.sourceforge.io/Doc/Release/Files.html) — 대화형·로그인 셸의 설정 파일 순서를 확인한다.
- [GNU Bash · Reference Manual](https://www.gnu.org/software/bash/manual/bash.html) — 셸 확장·환경 변수·리다이렉션·초기화 규칙을 확인한다.
