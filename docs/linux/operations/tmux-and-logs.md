# tmux와 원격 작업 관찰

> 원격 접속과 작업 세션을 분리하고 로그·프로세스 상태로 실제 실행을 확인한다.

- session·window·pane을 구분한다.
- detach와 프로세스 종료는 다르다.
- 서비스 수명은 별도 관리 정책이 필요하다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

tmux는 서버 프로세스가 유지되는 동안 터미널 세션을 보존하며 분리했다가 다시 붙을 수 있게 한다. session 안에 window와 pane을 나누어 작업·로그를 볼 수 있다. SSH 연결이 끊겨도 tmux 안의 작업을 계속 둘 수 있지만 서버 재부팅·프로세스 종료에 대한 영속 실행 관리를 대신하지 않는다. 운영 서비스는 서비스 관리자와 재시작·로그 정책을 검토한다.

## Java 예제

작업 로그를 읽는 Java 예제다. tmux 실행·세션 관리는 별도의 셸 도구가 맡는다.

```java
import java.nio.file.*;
import java.util.stream.Stream;

static long errorCount(Path log) throws java.io.IOException {
    try (Stream<String> lines = Files.lines(log)) {
        return lines.filter(line -> line.contains("ERROR")).count();
    }
}
```

## 주의점

운영 작업을 남겨 둔 tmux에 중요한 비밀이 보이지 않게 한다. kill-session은 작업을 종료할 수 있으므로 detach와 구분한다.

## 꼬리질문

1. SSH 재접속이 가능한 것과 서버 재부팅 후 작업 복원이 가능한 것은 왜 다른가?
2. tmux 세션이 연결 종료를 견뎌도 로그 파일과 종료 코드를 따로 남겨야 하는 이유는 무엇일까?
3. 서버 재부팅 뒤에도 작업을 복원하려면 tmux 외에 어떤 서비스 관리·체크포인트 정책이 필요할까?

</details>

## 참고 자료

- [tmux · Getting Started](https://github.com/tmux/tmux/wiki/Getting-Started) — 세션·창·패널과 attach·detach 사용법을 확인한다.
