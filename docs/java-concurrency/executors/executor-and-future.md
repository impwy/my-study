# Executor와 Future

> 작업 제출과 실행 스레드 관리를 분리하고 Future로 완료·실패·취소 결과를 받는다.

- 풀 크기와 작업 대기열을 함께 설계한다.
- Future.get은 완료까지 기다릴 수 있다.
- 종료와 거절·취소 정책도 필요하다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

ExecutorService에 Runnable·Callable을 제출하면 실행기는 자신의 정책으로 작업을 스케줄링한다. Future는 완료 여부 확인과 결과 수신을 맡으며 get에서 작업 실패가 ExecutionException으로 전달될 수 있다. 제출을 무한히 받아 대기열에 쌓는 구조는 스레드 수가 작아도 메모리와 지연을 키운다. CPU 작업과 블로킹 작업의 특성, 의존 관계를 보고 용량을 정한다.

## Java 예제

```java
import java.util.concurrent.*;

static int calculate() throws Exception {
    var pool =
            new ThreadPoolExecutor(
                    2,
                    2,
                    0,
                    TimeUnit.SECONDS,
                    new ArrayBlockingQueue<>(10),
                    new ThreadPoolExecutor.AbortPolicy());
    try {
        Future<Integer> result = pool.submit(() -> 6 * 7);
        return result.get(1, TimeUnit.SECONDS);
    } finally {
        pool.shutdownNow();
    }
}
```

## 주의점

cancel(true)는 인터럽트 요청이며 강제 종료가 아니다. 작업이 인터럽트와 자원 정리에 협조해야 한다. shutdown 뒤 종료 대기·미완료 작업 처리도 정한다.

## 꼬리질문

1. 스레드 수만 제한하고 대기열을 무제한으로 두면 어떤 문제가 남는가?
2. 두 스레드와 큐 10개가 모두 바쁘면 다음 submit은 어떤 결과를 내도록 설정되어 있을까?
3. Future.get의 제한 시간이 끝나도 작업이 자동 중단되지 않는다면 취소·정리 정책을 어떻게 정할까?

</details>

## 참고 자료

- [Java SE 21 · ExecutorService](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/ExecutorService.html) — 작업 제출·종료·Future와 메모리 가시성 계약을 확인한다.
