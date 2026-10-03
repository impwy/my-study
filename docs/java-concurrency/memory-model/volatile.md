# volatile의 가시성과 원자성

> volatile은 해당 변수의 읽기·쓰기에 가시성·순서 보장을 주지만 증가 연산 전체를 원자적으로 만들지 않는다.

- volatile 쓰기와 이후 읽기는 happens-before 관계를 만든다.
- count++는 읽기·계산·쓰기의 복합 연산이다.
- 복합 상태는 락이나 원자 연산으로 보호한다.

<details>
<summary>설명과 예제 펼치기</summary>

## 설명

한 스레드가 volatile 변수에 기록하고 다른 스레드가 이후 그 변수를 읽는 관계를 통해 앞선 작업의 결과가 보이도록 메모리 모델이 보장한다. 그래서 종료 플래그처럼 독립된 상태 전달에 유용하다. 그러나 count++는 현재 값 읽기, 1 더하기, 저장으로 구성된다. 두 스레드가 같은 이전 값을 읽으면 증가 결과 하나를 잃을 수 있다. 가시성과 복합 연산의 원자성을 분리해서 판단한다.

## Java 예제

```java
import java.util.concurrent.atomic.AtomicInteger;

static class State {
    volatile boolean running = true;
    volatile int unsafeCount; // 여러 스레드의 unsafeCount++는 증가를 잃을 수 있음
    final AtomicInteger count = new AtomicInteger();

    void increment() {
        count.incrementAndGet();
    }

    void stop() {
        running = false;
    }
}
```

## 주의점

volatile 참조가 가리키는 객체의 모든 필드를 자동으로 동기화하지 않는다. AtomicInteger도 두 개의 변수 사이 불변식까지 보호하지 않는다.

## 꼬리질문

1. volatile count가 0일 때 두 스레드가 각각 count++를 하면 왜 1이 될 수 있는가?
2. volatile 플래그로 종료를 알리는 것과 카운터 증가를 보호하는 것은 어떤 보장이 다를까?
3. AtomicInteger 두 개의 합을 일정하게 유지해야 한다면 각각의 원자 연산만으로 충분할까?

함께 복습: [스레드 안전성과 불변식](../safety/thread-safety.md) · [모니터와 명시적 락](../locks/monitor-and-lock.md)

</details>

## 참고 자료

- [JLS 17 · Threads and Locks](https://docs.oracle.com/javase/specs/jls/se21/html/jls-17.html) — happens-before와 모니터·volatile의 보장 범위를 확인한다.
